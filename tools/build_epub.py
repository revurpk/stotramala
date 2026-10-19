# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Make an EPUB 3 e-book of selected stotras, in IAST, Devanāgarī or Telugu.

The book is made from the built pages in stotra/, so it carries whatever a
page shows: verses, word-by-word lists, translations, bhāṣya, headings,
rubrics and colophons. The script conversion is the site's own: the
transliterator and converter are read out of the shell page and run with
Node (tools/epub_convert.js), so each line reads exactly as it does on the
site, baked rendering corrections included.

    python tools/build_epub.py --list
    python tools/build_epub.py lingashtakam bilvashtakam --script dev
    python tools/build_epub.py --deity shiva --title "Śiva Stotras"
    python tools/build_epub.py "gita-bhashya-*" --no-bhashya
    python tools/build_epub.py --all --script iast --out dist/all.epub

A selection is any mix of slugs, glob patterns (quote them) and --deity
folders; --all takes every page. Pages appear in the order given, and in
index.html order for --all and --deity.

Options:
    --script tel|dev|iast   script of the Sanskrit (default tel)
    --title T               book title (default from the selection)
    --out FILE              output path (default dist/<selection>-<script>.epub)
    --no-words              leave out the word-by-word lists
    --no-translation        leave out the verse translations
    --no-bhashya            leave out commentary (bhāṣya) and its English
    --no-svara              drop Vedic accents in Devanāgarī
    --no-font               do not embed Baloo Tammudu 2 for Telugu

Telugu is set without svara marks: the site draws them with CSS measured
in the browser, which an e-reader cannot do, and Telugu fonts lack the
glyphs. Devanāgarī keeps them as Unicode marks. Pages whose source is
Telugu (the kīrtanas, daṇḍakams, Gajendra Mokṣam) have no Devanāgarī form
and stay in Telugu when --script dev is asked for. Wording corrections to
the English (the "text" part of a page's corrections) are not applied.

Needs Python 3.9+ (standard library only) and Node.js on PATH. Build the
pages first (python tools/build_stotra.py --all) so the book is current.
"""

import argparse
import datetime
import fnmatch
import html
import html.parser
import json
import pathlib
import re
import shutil
import subprocess
import sys
import uuid
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "stotra"
SHELL = PAGES / "devi" / "durga-saptashloki-iast.html"
CONVERT = ROOT / "tools" / "epub_convert.js"
INDEX = ROOT / "index.html"

SCRIPTS = {"tel": "Telugu", "dev": "Devanāgarī", "iast": "IAST"}
LANG = {("iast", "tel"): "sa-Telu", ("iast", "dev"): "sa-Deva", ("iast", "iast"): "sa-Latn",
        ("tel", "tel"): "te", ("tel", "iast"): "te-Latn"}
VOID = {"br", "hr", "img", "meta", "link", "input", "wbr"}
ATTRIBUTION = "Stotramālā, copyright 2026 Pradyumna Revur, CC BY 4.0."
CHUNK_BYTES = 150_000          # e-readers slow down on very large XHTML files


# ---------------------------------------------------------------- pages

class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.kids = tag, dict(attrs), parent, []
        self.cls = set((self.attrs.get("class") or "").split())

    def text(self):
        return "".join(k if isinstance(k, str) else k.text() for k in self.kids)

    def find(self, pred):
        for k in self.kids:
            if isinstance(k, Node):
                if pred(k):
                    return k
                hit = k.find(pred)
                if hit:
                    return hit
        return None


class Tree(html.parser.HTMLParser):
    """Enough of a DOM for the generated pages, which are well formed."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.cur = Node("#root", {}, None)
        self.sans = []                       # .sans nodes in document order

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        if "sans" in n.cls:
            self.sans.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)


def catalogue():
    """slug → (path, deity), in index.html order, then any unlisted pages."""
    found = {p.name[:-len("-iast.html")]: p for p in sorted(PAGES.glob("*/*-iast.html"))}
    order = []
    for m in re.finditer(r'href="stotra/[^"/]+/([^"/]+)-iast\.html', INDEX.read_text(encoding="utf-8")):
        if m.group(1) in found and m.group(1) not in order:
            order.append(m.group(1))
    order += [s for s in found if s not in order]
    return {s: (found[s], found[s].parent.name) for s in order}


def load_page(path):
    raw = path.read_text(encoding="utf-8")
    src = (re.search(r'<html[^>]*\bdata-src="(\w+)"', raw) or [None, "iast"])[1]
    m = re.search(r"window\.STOTRA_CORRECTIONS\s*=\s*(\{.*?\});\s*</script>", raw, re.S)
    corr = json.loads(m.group(1)) if m else {}
    a = raw.index('<main class="page">')
    b = raw.index("</main>", a)
    t = Tree()
    t.feed(raw[a:b] + "</main>")
    main = t.root.kids[0]
    title = main.find(lambda n: n.tag == "h1")
    return {"main": main, "sans": t.sans, "src": src, "corr": corr,
            "title": " ".join(title.text().split()) if title else path.stem}


def convert(page, script, svara):
    """Set n.out on every .sans node of the page, as the page would show it."""
    sc = script if not (page["src"] == "tel" and script == "dev") else "tel"
    items = [{"t": n.text(), "w": "w" in (n.parent.cls if n.parent else set())} for n in page["sans"]]
    req = {"shell": str(SHELL), "src": page["src"], "script": sc,
           "svara": svara and sc == "dev", "items": items}
    r = subprocess.run(["node", str(CONVERT)], input=json.dumps(req).encode("utf-8"),
                       capture_output=True)
    if r.returncode:
        sys.exit("epub_convert.js failed:\n" + r.stderr.decode("utf-8", "replace"))
    out = json.loads(r.stdout.decode("utf-8"))
    for i, (n, s) in enumerate(zip(page["sans"], out)):
        fix = page["corr"].get(str(i), {}).get(sc)
        n.out = fix if fix is not None else s
    return LANG[(page["src"], sc)]


# ---------------------------------------------------------------- XHTML

DROP_CLS = {"review", "review-note", "guidelink", "add-slot", "scriptbar"}


class Writer:
    """Serialises a page's <main> into XHTML chunks, split at section headings."""

    def __init__(self, opts, lang):
        self.o, self.lang = opts, lang
        self.chunks = [[]]                   # list of chunks, each a list of strings
        self.heads = []                      # (chunk index, id, heading text)

    def esc(self, s):
        return html.escape(s, quote=False)

    def keep(self, n):
        if n.tag in ("script", "style", "button", "nav", "input", "textarea", "footer"):
            return False
        if n.cls & DROP_CLS or n.attrs.get("id") == "contents":
            return False
        if n.tag == "a" and n.attrs.get("href") == "#contents":
            return False
        if n.tag == "p" and "wbw" in n.cls and self.o.no_words:
            return False
        if n.tag == "details" and "bhashya" in n.cls and self.o.no_bhashya:
            return False
        if (n.tag == "p" and self.o.no_translation and n.parent is not None
                and n.parent.tag == "details" and "bhashya" not in n.parent.cls
                and "wbw" not in n.cls):
            return False
        return True

    def emit(self, s):
        self.chunks[-1].append(s)

    def node(self, n):
        if isinstance(n, str):
            self.emit(self.esc(n))
            return
        if not self.keep(n):
            return
        if "sans" in n.cls:
            self.emit(f'<span class="{" ".join(sorted(n.cls))}" lang="{self.lang}" '
                      f'xml:lang="{self.lang}">{self.esc(n.out)}</span>')
            return
        tag, cls = n.tag, set(n.cls)
        if tag == "a":                        # links are site navigation: keep the words
            for k in n.kids:
                self.node(k)
            return
        if tag == "summary":                  # a fold's label; only bhāṣya folds keep one
            d = n.parent
            if d is not None and "bhashya" in d.cls:
                tag, cls = "p", {"fold-title"}
            else:
                return
        if tag == "details":
            tag = "div"
        heading = tag == "p" and "speaker" in cls and not n.find(lambda k: "sans" in k.cls)
        if heading:                           # an English section heading
            tag, cls = "h2", {"section"}
        if tag in VOID:
            self.emit(f"<{tag}{self.attrs(n, cls)}/>")
            return
        if tag == "p" and "wbw" in cls:      # word pairs, separated for reading
            pairs = [k for k in n.kids if isinstance(k, Node) and "w" in k.cls]
            self.emit(f'<p{self.attrs(n, cls)}>')
            for i, k in enumerate(pairs):
                if i:
                    self.emit('<span class="sep"> · </span>')
                self.node(k)
            self.emit("</p>")
            return
        self.emit(f"<{tag}{self.attrs(n, cls)}>")
        for k in n.kids:
            self.node(k)
        self.emit(f"</{tag}>")

    def attrs(self, n, cls):
        out = ""
        if cls:
            out += f' class="{html.escape(" ".join(sorted(cls)))}"'
        if n.attrs.get("id"):
            out += f' id="{html.escape(n.attrs["id"])}"'
        return out

    def size(self):
        return sum(len(s.encode("utf-8")) for s in self.chunks[-1])

    def page(self, main, title):
        for k in main.kids:
            if isinstance(k, Node) and self.size() > CHUNK_BYTES \
                    and k.cls & {"verse", "speaker"}:
                self.chunks.append([])         # long page: next file at a verse boundary
            if isinstance(k, Node) and k.tag == "p" and "speaker" in k.cls \
                    and not k.find(lambda x: "sans" in x.cls):
                text = " ".join(re.sub(r"↑", "", k.text()).split())
                if any(s.strip() for s in self.chunks[-1]):
                    self.chunks.append([])
                hid = k.attrs.get("id") or f"h{len(self.heads) + 1}"
                k.attrs["id"] = hid
                self.heads.append((len(self.chunks) - 1, hid, text))
            if isinstance(k, Node) and k.tag == "footer":
                src = " ".join("".join(x for x in k.kids if isinstance(x, str)).split())
                if src:
                    self.emit(f'<p class="source">{self.esc(src)}</p>')
                continue
            self.node(k)


def xhtml(title, body, lang="en"):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
            f'lang="{lang}" xml:lang="{lang}">\n<head>\n<meta charset="utf-8"/>\n'
            f"<title>{html.escape(title)}</title>\n"
            '<link rel="stylesheet" type="text/css" href="../style.css"/>\n</head>\n'
            f"<body>\n{body}\n</body>\n</html>\n")


CSS = """
@font-face{font-family:"Baloo Tammudu 2";font-style:normal;font-weight:400;src:url(fonts/BalooTammudu2.woff2) format("woff2");}
body{margin:0 4%;line-height:1.5;font-family:serif;}
h1{text-align:center;font-size:1.5em;margin:1.2em 0 .3em;}
h2.section{text-align:center;font-size:1.1em;font-weight:normal;font-variant:small-caps;letter-spacing:.06em;margin:2em 0 1em;page-break-after:avoid;}
.om{text-align:center;font-size:1.6em;margin-top:1em;}
.subtitle{text-align:center;font-style:italic;margin:.2em 0;}
hr.titlerule{width:30%;margin:1em auto;border:0;border-top:1px solid #999;}
.verse{margin:1.4em 0;}
.lines{text-align:center;margin:0 0 .5em;}
.viniyoga .lines{font-size:.92em;}
.num{display:block;text-align:center;margin-top:.2em;}
.sans{font-family:"Noto Serif",serif;}
.sans:lang(sa-Telu),.sans:lang(te){font-family:"Baloo Tammudu 2","Noto Sans Telugu","Gautami",sans-serif;font-size:1.12em;line-height:1.6;}
.sans:lang(sa-Deva){font-family:"Noto Serif Devanagari","Noto Sans Devanagari","Mangal",serif;font-size:1.08em;}
.gloss{margin:.4em 0 0;font-size:.92em;}
.gloss p{margin:.4em 0;text-align:justify;}
p.wbw{text-align:left;font-size:.92em;line-height:1.6;}
.w .sans{font-weight:bold;}
.sep{color:#888;}
.speaker{text-align:center;font-style:italic;margin:1.6em 0 .4em;}
.fold-title{font-variant:small-caps;letter-spacing:.06em;color:#666;margin:1em 0 .3em;}
.bhashya p{text-align:justify;}
.bh-intro{opacity:.85;}
.bh-tr{font-style:italic;margin-left:1em;padding-left:.6em;border-left:2px solid #ccc;}
.colophon{text-align:center;margin:2em 0 .4em;}
.colophon-gloss{text-align:center;font-style:italic;font-size:.92em;margin:.3em 0;}
.ornament{text-align:center;margin:1.5em 0;}
.source{font-size:.8em;text-align:center;color:#666;margin-top:2.5em;border-top:1px solid #ccc;padding-top:.8em;}
.title-page{text-align:center;margin-top:20%;}
.title-page h1{font-size:1.8em;}
.contents-list{list-style:none;padding:0;text-align:center;line-height:1.8;}
"""


# ---------------------------------------------------------------- book

def font_bytes():
    import base64
    s = SHELL.read_text(encoding="utf-8")
    m = re.search(r'font-family:"Baloo Tammudu 2";.*?base64,([A-Za-z0-9+/=]+)', s, re.S)
    return base64.b64decode(m.group(1)) if m else None


def build(slugs, cat, o):
    script = o.script
    files, nav = [], []                      # files: (href, title, xhtml); nav: (title, href, [(t, href)])
    for i, slug in enumerate(slugs, 1):
        path, _ = cat[slug]
        p = load_page(path)
        lang = convert(p, script, not o.no_svara)
        if p["src"] == "tel" and script == "dev":
            print(f"  {slug}: Telugu-language page, kept in Telugu")
        w = Writer(o, lang)
        w.page(p["main"], p["title"])
        many = len(w.chunks) > 1
        hrefs = [f"text/{i:03d}-{slug}" + (f"-{j + 1:02d}" if many else "") + ".xhtml"
                 for j in range(len(w.chunks))]
        for j, chunk in enumerate(w.chunks):
            files.append((hrefs[j], p["title"], xhtml(p["title"], "".join(chunk))))
        subs = [(t, f"{hrefs[c]}#{hid}") for c, hid, t in w.heads]
        nav.append((p["title"], hrefs[0], subs))
        print(f"  {slug}: {len(w.chunks)} file(s)")
    return files, nav


def nav_xhtml(title, nav):
    def ol(items):
        out = "<ol>"
        for t, href, subs in items:
            out += f'<li><a href="{href}">{html.escape(t)}</a>'
            if subs:
                out += ol([(st, sh, []) for st, sh in subs])
            out += "</li>"
        return out + "</ol>"
    body = f'<nav epub:type="toc" id="toc"><h1>{html.escape(title)}</h1>{ol(nav)}</nav>'
    return xhtml("Contents", body).replace('href="../style.css"', 'href="style.css"')


def ncx(uid, title, nav):
    pts, k = [], 0
    for t, href, subs in nav:
        k += 1
        inner = ""
        for st, sh in subs:
            k += 1
            inner += (f'<navPoint id="n{k}" playOrder="{k}"><navLabel><text>{html.escape(st)}</text>'
                      f'</navLabel><content src="{sh}"/></navPoint>')
        pts.append(f'<navPoint id="p{k}" playOrder="{k - len(subs)}"><navLabel><text>{html.escape(t)}'
                   f'</text></navLabel><content src="{href}"/>{inner}</navPoint>')
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
            f'<head><meta name="dtb:uid" content="{uid}"/></head>\n'
            f"<docTitle><text>{html.escape(title)}</text></docTitle>\n"
            f"<navMap>{''.join(pts)}</navMap>\n</ncx>\n")


def opf(uid, title, lang, items, spine, modified):
    man = "".join(f'<item id="{i}" href="{h}" media-type="{t}"{p}/>\n' for i, h, t, p in items)
    sp = "".join(f'<itemref idref="{i}"/>' for i in spine)
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">\n'
            '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
            f'<dc:identifier id="uid">{uid}</dc:identifier>\n'
            f"<dc:title>{html.escape(title)}</dc:title>\n"
            f"<dc:language>en</dc:language>\n<dc:language>{lang}</dc:language>\n"
            "<dc:creator>Pradyumna Revur</dc:creator>\n<dc:publisher>Stotramālā</dc:publisher>\n"
            f"<dc:rights>{html.escape(ATTRIBUTION)}</dc:rights>\n"
            f'<meta property="dcterms:modified">{modified}</meta>\n</metadata>\n'
            f"<manifest>\n{man}</manifest>\n"
            f'<spine toc="ncx">{sp}</spine>\n</package>\n')


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Make an EPUB of selected stotras.")
    ap.add_argument("slugs", nargs="*", help="page slugs or glob patterns")
    ap.add_argument("--deity", action="append", default=[], help="a folder under stotra/, e.g. shiva")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--list", action="store_true", help="list the pages and stop")
    ap.add_argument("--script", choices=SCRIPTS, default="tel")
    ap.add_argument("--title")
    ap.add_argument("--out")
    for f in ("words", "translation", "bhashya", "svara", "font"):
        ap.add_argument(f"--no-{f}", action="store_true")
    o = ap.parse_args(argv)
    cat = catalogue()

    if o.list:
        for slug, (path, deity) in cat.items():
            print(f"{deity:12} {slug:32} {load_page(path)['title']}")
        return

    sel = []
    def add(s):
        if s not in sel:
            sel.append(s)
    if o.all:
        for s in cat:
            add(s)
    for d in o.deity:
        hits = [s for s, (_, dd) in cat.items() if dd == d]
        if not hits:
            sys.exit(f"no pages under stotra/{d}/ (folders: {', '.join(sorted({v[1] for v in cat.values()}))})")
        for s in hits:
            add(s)
    for pat in o.slugs:
        hits = [s for s in cat if fnmatch.fnmatchcase(s, pat)]
        if not hits:
            sys.exit(f"no page matches {pat!r}; see --list")
        for s in hits:
            add(s)
    if not sel:
        ap.error("nothing selected: give slugs, --deity or --all (see --list)")
    if not shutil.which("node"):
        sys.exit("Node.js is needed for the script conversion; install it from https://nodejs.org")

    titles = {s: load_page(cat[s][0])["title"] for s in sel[:2]}
    title = o.title or (titles[sel[0]] if len(sel) == 1 else
                        f"Stotramālā · {', '.join(titles.values())}{' …' if len(sel) > 2 else ''}")
    name = (sel[0] if len(sel) == 1 else "stotramala" if o.all
            else "-".join(o.deity) if o.deity and not o.slugs
            else f"{sel[0]}-and-{len(sel) - 1}-more")
    out = pathlib.Path(o.out) if o.out else ROOT / "dist" / f"{name}-{o.script}.epub"
    print(f"{title} — {len(sel)} page(s), {SCRIPTS[o.script]}")

    files, nav = build(sel, cat, o)
    lang = {"tel": "sa-Telu", "dev": "sa-Deva", "iast": "sa-Latn"}[o.script]
    flags = ",".join(f for f in ("words", "translation", "bhashya", "svara") if getattr(o, f"no_{f}"))
    uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, f"stotramala:{o.script}:{flags}:{','.join(sel)}"))
    modified = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    listing = "".join(f"<li>{html.escape(t)}</li>" for t, _, _ in nav)
    title_body = (f'<div class="title-page"><div class="om">ॐ</div><h1>{html.escape(title)}</h1>'
                  f'<p class="subtitle">{SCRIPTS[o.script]}</p>'
                  f'<ul class="contents-list">{listing}</ul></div>')
    about_body = ("<h2 class=\"section\">About this book</h2>"
                  f"<p>Made from the Stotramālā pages ({html.escape(ATTRIBUTION)}) with "
                  "tools/build_epub.py. The Sanskrit is the site's IAST source rendered by the "
                  "site's own transliterator; translations and word-by-word glosses are original. "
                  "See SOURCES.md in the repository (github.com/revurpk/stotramala) for the "
                  "sources of each text.</p>"
                  + ("<p>Telugu is set in Baloo Tammudu 2 by Ek Type, used under the SIL Open "
                     "Font License 1.1.</p>" if o.script == "tel" and not o.no_font else ""))

    items = [("nav", "nav.xhtml", "application/xhtml+xml", ' properties="nav"'),
             ("ncx", "toc.ncx", "application/x-dtbncx+xml", ""),
             ("css", "style.css", "text/css", ""),
             ("title", "text/000-title.xhtml", "application/xhtml+xml", "")]
    spine = ["title"]
    for k, (href, _, _) in enumerate(files, 1):
        items.append((f"c{k}", href, "application/xhtml+xml", ""))
        spine.append(f"c{k}")
    items.append(("about", "text/999-about.xhtml", "application/xhtml+xml", ""))
    spine += ["nav", "about"]
    font = None
    if o.script == "tel" and not o.no_font:
        font = font_bytes()
        if font:
            items.append(("font", "fonts/BalooTammudu2.woff2", "font/woff2", ""))
    css = CSS if font else CSS.split("\n", 2)[2]

    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        def put(name, data):
            z.writestr("OEBPS/" + name, data, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0" encoding="utf-8"?>\n'
                   '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles></container>\n',
                   compress_type=zipfile.ZIP_DEFLATED)
        put("content.opf", opf(uid, title, lang, items, spine, modified))
        put("nav.xhtml", nav_xhtml(title, nav))
        put("toc.ncx", ncx(uid, title, nav))
        put("style.css", css)
        put("text/000-title.xhtml", xhtml(title, title_body))
        put("text/999-about.xhtml", xhtml("About this book", about_body))
        for href, t, doc in files:
            put(href, doc)
        if font:
            put("fonts/BalooTammudu2.woff2", font)
    print(f"wrote {out}  ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main(sys.argv[1:])
