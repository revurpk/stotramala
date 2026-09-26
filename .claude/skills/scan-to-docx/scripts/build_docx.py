# /// script
# requires-python = ">=3.10"
# dependencies = ["python-docx>=1.1"]
# ///
"""Build a Word document from a compilation file (see compile_lib.py for the
format): a title page, then one section per snippet with its provenance and
the text, stanza by stanza.

    uv run build_docx.py <compilation.txt> [-o out.docx] [--font dev=Siddhanta]
                         [--font tel="Nirmala UI"] [--size 14]

Indic text needs its font set on the *complex-script* slot (w:rFonts/@w:cs,
w:szCs) — setting only run.font.name leaves Word to substitute a font that
may lack conjuncts or Vedic marks. Defaults: Devanāgarī → Siddhanta (full
Vedic-accent support; installed on this machine), Telugu → Gautami (renders
svaras on Telugu letters; verified), falling back to Nirmala UI;
every other script → Nirmala UI. Uncertain readings [?…?] and illegible
stretches […] are highlighted yellow so a proofreader finds them.

Word's shaping of stacked Vedic marks is weaker than a browser's; the HTML
companion (build_html.py) is the faithful rendering when accents matter.
"""
import pathlib
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from compile_lib import UNCERTAIN, lint, parse  # noqa: E402

DEFAULT_FONTS = {"dev": "Siddhanta", "tel": "Gautami", "iast": "Cambria"}
FALLBACK = "Nirmala UI"


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


def main(argv):
    if not argv:
        sys.exit(__doc__)
    src = pathlib.Path(argv[0])
    out = pathlib.Path(argv[argv.index("-o") + 1]) if "-o" in argv else src.with_name(src.name.removesuffix(".txt").removesuffix(".compile") + ".docx")
    size = float(argv[argv.index("--size") + 1]) if "--size" in argv else 14
    fonts = dict(DEFAULT_FONTS)
    for i, a in enumerate(argv):
        if a == "--font":
            k, _, v = argv[i + 1].partition("="); fonts[k] = v
    meta, snippets = parse(src)
    for w in lint(snippets):
        print("WARN", w)

    doc = Document()
    doc.core_properties.title = meta.get("title", src.stem)
    doc.core_properties.author = meta.get("compiler", "")
    t = doc.add_heading(meta.get("title", src.stem), level=0)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if meta.get("note"):
        doc.add_paragraph().add_run(meta["note"]).italic = True
    lines = [f"{n}. {s['source']}" + (f" — p. {s['pages']}" if s.get("pages") else "")
             for n, s in enumerate(snippets, 1)]
    doc.add_paragraph("Sources\n" + "\n".join(lines))

    for n, s in enumerate(snippets, 1):
        doc.add_page_break() if n > 1 else None
        doc.add_heading(s.get("title") or s["source"], level=1)
        prov = doc.add_paragraph()
        for key in ("source", "file", "pages", "status", "accents", "note"):
            if s.get(key):
                r = prov.add_run(f"{key}: {s[key]}\n")
                r.font.size = Pt(9); r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
        font = fonts.get(s["script"], FALLBACK)
        for stanza in s["text"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(10)
            for i, line in enumerate(stanza):
                add_text(p, line, font, size)
                if i < len(stanza) - 1:
                    p.add_run().add_break()
    doc.save(out)
    print(f"{len(snippets)} snippets -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
