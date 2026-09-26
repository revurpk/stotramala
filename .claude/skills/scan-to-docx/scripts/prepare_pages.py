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
    flags = {"--out", "--pages", "--dpi", "--strips", "--overlap"}
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
            for k, s in enumerate(strips(im, n, overlap), 1):
                p = out / f"{stem}-s{k}.png"; s.save(p, optimize=True); parts.append(p.name)
            manifest.append({"source": str(f.resolve()), "page": pno, "image": full.name,
                             "strips": parts, "size": [im.width, im.height]})
            print(f"{f.name} p{pno}: {im.width}x{im.height}, {len(parts)} strips")
    if "--sheets" in argv:
        contact_sheets(out, manifest)
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(manifest)} pages -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
