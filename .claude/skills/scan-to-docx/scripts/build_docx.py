# /// script
# requires-python = ">=3.10"
# dependencies = ["python-docx>=1.1"]
# ///
"""Build a Word document from a compilation file (see compile_lib.py for the
format): a title page with a linked table of contents, then one section per
snippet with its provenance and the text, stanza by stanza.

    uv run build_docx.py <compilation.txt> [-o out.docx] [--font dev=Siddhanta]
                         [--font tel=Gautami] [--size 14]

Navigation, for long pieces: every snippet title and every `##`/`###`
heading becomes a Word heading (so it shows in the Navigation Pane) carrying
a bookmark, and the contents page links to those bookmarks with the printed
page from the nearest `[p. N]` marker. The links work as soon as the file
opens — no "update field" step.

Indic text needs its font set on the *complex-script* slot (w:rFonts/@w:cs,
w:szCs) — setting only run.font.name leaves Word to substitute a font that
may lack conjuncts or Vedic marks. Defaults: Devanāgarī → Siddhanta (full
Vedic-accent support; installed on this machine), Telugu → Gautami (renders
svaras on Telugu letters; verified), falling back to Nirmala UI; every other
script → Nirmala UI. Uncertain readings [?…?] and illegible stretches […]
are highlighted yellow so a proofreader finds them.

Word's shaping of stacked Vedic marks is weaker than a browser's; the HTML
companion (build_html.py) is the faithful rendering when accents matter.
"""
import pathlib
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from compile_lib import UNCERTAIN, lint, parse, toc  # noqa: E402

DEFAULT_FONTS = {"dev": "Siddhanta", "tel": "Gautami", "iast": "Cambria"}
FALLBACK = "Nirmala UI"
GREY = RGBColor(0x66, 0x66, 0x66)


def set_font(run, name, size):
    run.font.name = name
    run.font.size = Pt(size)
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = rpr.makeelement(qn("w:rFonts"), {}); rpr.insert(0, rf)
    for slot in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(slot), name)
    szcs = rpr.find(qn("w:szCs"))
    if szcs is None:
        szcs = rpr.makeelement(qn("w:szCs"), {}); rpr.append(szcs)
    szcs.set(qn("w:val"), str(int(size * 2)))


def add_text(par, text, font, size):
    """Write text into a paragraph, highlighting uncertain spans."""
    pos = 0
    for m in UNCERTAIN.finditer(text):
        if m.start() > pos:
            set_font(par.add_run(text[pos:m.start()]), font, size)
        r = par.add_run(m.group()); set_font(r, font, size)
        r.font.highlight_color = WD_COLOR_INDEX.YELLOW
        pos = m.end()
    if pos < len(text):
        set_font(par.add_run(text[pos:]), font, size)


_bm = [0]


def bookmark(par, name):
    """Wrap the paragraph's content in a bookmark (Word: Insert > Bookmark)."""
    _bm[0] += 1
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(_bm[0])); start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd"); end.set(qn("w:id"), str(_bm[0]))
    par._p.insert(1 if par._p.pPr is not None else 0, start)
    par._p.append(end)


def link(par, anchor, text, font, size):
    """An internal hyperlink to a bookmark."""
    h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), anchor); h.set(qn("w:history"), "1")
    run = par.add_run(text); set_font(run, font, size)
    run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x9A)
    h.append(run._r)
    par._p.append(h)


def heading(doc, text, level, font, bm):
    h = doc.add_heading(level=level)
    set_font(h.add_run(text), font, {1: 18, 2: 15, 3: 13}[level])
    bookmark(h, bm)
    return h


def main(argv):
    if not argv:
        sys.exit(__doc__)
    src = pathlib.Path(argv[0])
    out = pathlib.Path(argv[argv.index("-o") + 1]) if "-o" in argv else \
        src.with_name(src.name.removesuffix(".txt").removesuffix(".compile") + ".docx")
    size = float(argv[argv.index("--size") + 1]) if "--size" in argv else 14
    fonts = dict(DEFAULT_FONTS)
    for i, a in enumerate(argv):
        if a == "--font":
            k, _, v = argv[i + 1].partition("="); fonts[k] = v
    meta, snippets = parse(src)
    for w in lint(snippets):
        print("WARN", w)
    font_of = {s["id"]: fonts.get(s["script"], FALLBACK) for s in snippets}

    doc = Document()
    doc.core_properties.title = meta.get("title", src.stem)
    doc.core_properties.author = meta.get("compiler", "")
    t = doc.add_heading(meta.get("title", src.stem), level=0)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if meta.get("note"):
        doc.add_paragraph().add_run(meta["note"]).italic = True

    # contents: one linked line per snippet / heading, with its printed page
    doc.add_paragraph().add_run("Contents").bold = True
    for level, bid, text, page in toc(meta, snippets):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Pt(18 * (level - 1))
        p.paragraph_format.space_after = Pt(2)
        sid = bid.split("-")[0]
        link(p, bid.replace("-", "_"), text, font_of[sid] if level > 1 else "Cambria",
             12 if level == 1 else 11)
        if page:
            r = p.add_run(f"   p. {page}"); r.font.size = Pt(9); r.font.color.rgb = GREY

    for s in snippets:
        doc.add_page_break()
        font = font_of[s["id"]]
        heading(doc, s.get("title") or s["source"], 1, "Cambria", s["id"])
        prov = doc.add_paragraph()
        for key in ("source", "file", "pages", "status", "accents", "note"):
            if s.get(key):
                r = prov.add_run(f"{key}: {s[key]}\n"); r.font.size = Pt(9); r.font.color.rgb = GREY
        for b in s["blocks"]:
            if b["kind"] == "page":
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                r = p.add_run(f"[p. {b['text']}]"); r.font.size = Pt(8); r.font.color.rgb = GREY
            elif b["kind"] in ("h2", "h3"):
                heading(doc, b["text"], int(b["kind"][1]), font, b["id"].replace("-", "_"))
            elif b["kind"] == "fn":
                p = doc.add_paragraph()
                r = p.add_run(f"({b['mark']}) " if b["mark"] else ""); r.font.size = Pt(9)
                add_text(p, b["text"], font, size * 0.7)
            else:
                p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(10)
                for i, line in enumerate(b["lines"]):
                    add_text(p, line, font, size)
                    if i < len(b["lines"]) - 1:
                        p.add_run().add_break()
    doc.save(out)
    print(f"{len(snippets)} snippets, {sum(1 for x in toc(meta, snippets) if x[0] > 1)} "
          f"headings -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
