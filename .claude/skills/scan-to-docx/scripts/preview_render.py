# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.24"]
# ///
"""Render the HTML companion to PNG pages so you can LOOK at how the accents
shaped — the check that the transcription and the fonts actually work.

    uv run preview_render.py <file.html> [--font tel=gautami.ttf]
                             [--font dev=siddhanta.ttf] [--dpi 120]

WHY: the in-app browser can't script a local file, and "the text is right"
doesn't mean "the marks land on the right akṣara" — a missing glyph shows as
a box, a mark in the wrong Unicode order shows on a dotted circle. MuPDF's
HTML engine shapes with HarfBuzz like a browser, but it does no per-character
font fallback, so name the font file for each script explicitly (files in
C:\\Windows\\Fonts). Defaults: tel → gautami.ttf, dev → siddhanta.ttf.
Latin (titles, provenance) may show boxes for bare combining marks; that is
this renderer, not the page. Writes <file>-render-N.png next to the HTML.
"""
import io
import pathlib
import re
import sys

import pymupdf

FONTS = {"tel": "gautami.ttf", "dev": "siddhanta.ttf"}
FAMILY = {"tel": "'Gautami'", "dev": "'Siddhanta'"}   # first family in build_html's stacks


def main(argv):
    if not argv:
        sys.exit(__doc__)
    src = pathlib.Path(argv[0])
    fonts = dict(FONTS)
    for i, a in enumerate(argv):
        if a == "--font":
            k, _, v = argv[i + 1].partition("="); fonts[k] = v
    dpi = int(argv[argv.index("--dpi") + 1]) if "--dpi" in argv else 120
    body = re.sub(r"<link[^>]+>", "", src.read_text(encoding="utf-8"))
    css = ""
    for k, f in fonts.items():
        css += "@font-face{font-family:f%s;src:url(%s);}" % (k, f)
        if k in FAMILY:
            body = body.replace(f"font-family:{FAMILY[k]}", f"font-family:f{k},{FAMILY[k]}")
    story = pymupdf.Story(html=body, user_css=css, archive=pymupdf.Archive(r"C:\Windows\Fonts"))
    buf = io.BytesIO()                      # in memory: Windows locks temp files
    w = pymupdf.DocumentWriter(buf)
    rect, more = pymupdf.paper_rect("a4"), 1
    while more:
        dev = w.begin_page(rect); more, _ = story.place(rect + (36, 36, -36, -36))
        story.draw(dev); w.end_page()
    w.close()
    doc = pymupdf.open("pdf", buf.getvalue())
    for n, page in enumerate(doc):
        out = src.with_name(f"{src.stem}-render-{n}.png")
        page.get_pixmap(dpi=dpi).save(out); print(out)
    doc.close()


if __name__ == "__main__":
    main(sys.argv[1:])
