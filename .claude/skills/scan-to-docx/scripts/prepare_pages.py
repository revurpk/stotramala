# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.24", "pillow>=10"]
# ///
"""Turn scanned pages (PDF, multi-page TIFF, JPEG/PNG) into images sized for
reading: one full-page PNG per page plus overlapping horizontal STRIPS.

WHY STRIPS: an image handed to the Read tool is downscaled to fit its budget.
A full A4 page of dense Indic print at that size loses exactly what matters —
the vowel signs, conjunct stacks, and above all the tiny Vedic svara strokes.
Strips of a few text lines each stay near full resolution. They overlap so a
line cut at one strip's edge is whole in the next.

    uv run prepare_pages.py <file> [<file> ...] --out DIR
        [--pages 3-5,9] [--dpi 300] [--strips 4] [--overlap 0.12]
        [--crop] [--gray]

  --pages   1-based pages to take (PDF/TIFF); default all
  --dpi     PDF render resolution (default 300; scans rarely gain above 400)
  --strips  horizontal strips per page (default 4; 0 = full page only)
  --crop    trim uniform margins before stripping (saves resolution for text)
  --gray    convert to grayscale (smaller files; keeps faint accents legible)
  --sheets  also tile the pages 12 to an image (DIR/sheet-NN.png) — a quick
            survey of a long book's structure before transcribing
  --lines N instead of strips, cut the page into its TEXT LINES (found from
            the blank rows between them) and each line into N overlapping
            pieces (default 2) — DIR/<stem>-pNNN-LL-k.png. For accented text:
            at this size each svara stroke/bar sits unmistakably over or under
            its own akṣara, which a multi-line strip leaves ambiguous.
  --gap     blank rows (at the render dpi) that separate two lines (default
            dpi/16; raise it if accents split off as their own "line")

Writes DIR/<stem>-pNNN.png (full page), DIR/<stem>-pNNN-sK.png (strips) and
DIR/manifest.json listing every image with its source file and page number —
the provenance the compilation needs later.
"""
import json
import pathlib
import sys

from PIL import Image, ImageChops, ImageDraw, ImageOps

Image.MAX_IMAGE_PIXELS = None


def parse_pages(spec):
    if not spec:
        return None
    out = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out.update(range(int(a), int(b or a) + 1))
    return out


def load(path, pages, dpi):
    """Yield (page_number, PIL.Image) for a PDF, TIFF or single image."""
    suf = path.suffix.lower()
    if suf == ".pdf":
        import pymupdf
        doc = pymupdf.open(path)
        for i, page in enumerate(doc, 1):
            if pages and i not in pages:
                continue
            pix = page.get_pixmap(dpi=dpi)
            yield i, Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    else:
        im = Image.open(path)
        n = getattr(im, "n_frames", 1)
        for i in range(1, n + 1):
            if pages and i not in pages:
                continue
            im.seek(i - 1)
            yield i, ImageOps.exif_transpose(im.convert("RGB"))


def crop_margins(im, pad=24):
    g = im.convert("L")
    bg = Image.new("L", g.size, g.getpixel((0, 0)))
    diff = ImageChops.difference(g, bg).point(lambda v: 255 if v > 40 else 0)
    box = diff.getbbox()
    if not box:
        return im
    l, t, r, b = box
    return im.crop((max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad)))


def strips(im, n, overlap):
    if n <= 1:
        return []
    h = im.height / n
    ov = int(h * overlap)
    out = []
    for k in range(n):
        top = max(0, int(k * h) - ov)
        bot = min(im.height, int((k + 1) * h) + ov)
        out.append(im.crop((0, top, im.width, bot)))
    return out


def text_lines(im, gap):
    """(top, bottom) of each text line. The dense CORE of a line (the letter
    bodies) is found from rows with substantial ink; faint rows (svara
    strokes, anudātta bars, matra tips) never form a core. Lines are cut at
    the midpoint between neighbouring cores, so each accent stays with the
    line it belongs to even when it nearly touches the next one."""
    g = im.convert("L").point(lambda v: 1 if v < 128 else 0)
    w, h = g.size
    data = g.tobytes()
    ink = [sum(data[y * w:(y + 1) * w]) for y in range(h)]
    peak = max(ink) or 1
    core = [v > peak * 0.12 for v in ink]
    runs, y = [], 0
    while y < h:
        if core[y]:
            s = y
            while y < h and core[y]:
                y += 1
            runs.append([s, y])
        y += 1
    cores = []
    for r in runs:                                 # join a core split by a thin gap
        if cores and r[0] - cores[-1][1] < gap:
            cores[-1][1] = r[1]
        else:
            cores.append(r)
    cores = [c for c in cores if c[1] - c[0] >= gap // 2]
    # A line whose type is broken across a scan crease can split into two
    # short cores; a core much shorter than a typical line is a fragment —
    # merge it into whichever neighbour is closer.
    if len(cores) > 2:
        med = sorted(b - a for a, b in cores)[len(cores) // 2]
        k = 0
        while k < len(cores) and len(cores) > 1:
            a, b = cores[k]
            if b - a < 0.6 * med:
                up = a - cores[k - 1][1] if k else 1 << 30
                dn = cores[k + 1][0] - b if k + 1 < len(cores) else 1 << 30
                j = k - 1 if up <= dn else k + 1
                lo, hi = sorted((k, j))
                cores[lo] = [cores[lo][0], cores[hi][1]]
                del cores[hi]
                k = max(0, lo - 1)
                continue
            k += 1
    def cut(lo, hi):
        """Row to cut at between two cores: the middle of the longest blank
        band (svarita strokes of the lower line and anudātta bars of the upper
        one sit on either side of it), else the faintest row."""
        best, run, start = None, 0, None
        for y in range(lo, hi):
            if ink[y] == 0:
                start = y if start is None else start
                if y - start + 1 > run:
                    run, best = y - start + 1, (start + y) // 2
            else:
                start = None
        return best if best is not None else min(range(lo, hi), key=lambda y: ink[y], default=lo)

    out = []
    for k, (a, b) in enumerate(cores):
        top = cut(cores[k - 1][1], a) if k else max(0, next((y for y in range(a) if ink[y]), a) - 4)
        if k < len(cores) - 1:
            bot = cut(b, cores[k + 1][0])
        else:
            bot = min(h, max((y for y in range(b, h) if ink[y]), default=b) + 4)
        out.append((top, bot))
    return out


def line_pieces(im, n, gap, pad=0, overlap=0.08):
    out = []
    for a, b in text_lines(im, gap):
        top, bot = max(0, a - pad), min(im.height, b + pad)
        wpiece = im.width / n
        ov = int(im.width * overlap)
        out.append([im.crop((max(0, int(k * wpiece) - ov), top,
                             min(im.width, int((k + 1) * wpiece) + ov), bot)) for k in range(n)])
    return out


def contact_sheets(out, manifest, per=12, cols=6, w=330, h=540):
    for s in range(0, len(manifest), per):
        sheet = Image.new("L", (w * cols, h * (per // cols)), 255); d = ImageDraw.Draw(sheet)
        for i, m in enumerate(manifest[s:s + per]):
            im = Image.open(out / m["image"]).convert("L"); im.thumbnail((w - 6, h - 24))
            x, y = (i % cols) * w, (i // cols) * h
            sheet.paste(im, (x + 3, y + 20)); d.text((x + 5, y + 3), f"p{m['page']}", fill=0)
        sheet.save(out / f"sheet-{s // per + 1:02d}.png")


def main(argv):
    if not argv or "--out" not in argv:
        sys.exit(__doc__)
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    out = pathlib.Path(opt("--out")); out.mkdir(parents=True, exist_ok=True)
    pages = parse_pages(opt("--pages"))
    dpi, n = int(opt("--dpi", 300)), int(opt("--strips", 4))
    overlap = float(opt("--overlap", 0.12))
    flags = {"--out", "--pages", "--dpi", "--strips", "--overlap", "--lines", "--gap"}
    nlines = int(opt("--lines", 0)) if "--lines" in argv else 0
    gap = int(opt("--gap", dpi // 20))
    files = [a for i, a in enumerate(argv)
             if not a.startswith("--") and argv[i - 1] not in flags]
    manifest = []
    for f in map(pathlib.Path, files):
        for pno, im in load(f, pages, dpi):
            if "--crop" in argv:
                im = crop_margins(im)
            if "--gray" in argv:
                im = im.convert("L")
            stem = f"{f.stem}-p{pno:03d}"
            full = out / f"{stem}.png"; im.save(full, optimize=True)
            parts = []
            if nlines:
                for li, pieces in enumerate(line_pieces(im, nlines, gap), 1):
                    for k, pc in enumerate(pieces, 1):
                        p = out / f"{stem}-{li:02d}-{k}.png"; pc.save(p, optimize=True); parts.append(p.name)
            else:
                for k, s in enumerate(strips(im, n, overlap), 1):
                    p = out / f"{stem}-s{k}.png"; s.save(p, optimize=True); parts.append(p.name)
            manifest.append({"source": str(f.resolve()), "page": pno, "image": full.name,
                             "strips": parts, "size": [im.width, im.height]})
            print(f"{f.name} p{pno}: {im.width}x{im.height}, {len(parts)} pieces")
    if "--sheets" in argv:
        contact_sheets(out, manifest)
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(manifest)} pages -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
