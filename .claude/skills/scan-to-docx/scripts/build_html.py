# /// script
# requires-python = ">=3.10"
# ///
"""Build a self-contained HTML reading copy of a compilation file, with
Vedic accents rendered properly.

    uv run build_html.py <compilation.txt> [-o out.html]

WHY HTML AS WELL AS WORD: svara marks (॑ ॒ and the Vedic Extensions block
U+1CD0–1CFF, e.g. ᳚ double svarita, ꣳ) are combining characters that must
stack over or under the right akṣara. Browsers shape them with HarfBuzz and a
font that carries the marks; Word frequently drops them onto a dotted circle
or the wrong glyph. The font stack prefers fonts known to carry Vedic marks —
Siddhanta, Sanskrit 2003, Chandas (installed locally) — then the Noto Serif
families from Google Fonts (loaded only if the machine is online), then
Nirmala UI. Line height is raised so svarita strokes and anudātta bars don't
collide with the neighbouring line. Uncertain readings are highlighted.
"""
import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from compile_lib import UNCERTAIN, has_accents, lint, parse  # noqa: E402

STACK = {
    "dev": "'Siddhanta','Sanskrit 2003','Chandas','Noto Serif Devanagari','Nirmala UI',serif",
    "tel": "'Gautami','Nirmala UI','Noto Serif Telugu','Vani',serif",  # Gautami: svaras verified
    "kan": "'Noto Serif Kannada','Nirmala UI','Tunga',serif",
    "tam": "'Noto Serif Tamil','Nirmala UI','Latha',serif",
    "mal": "'Noto Serif Malayalam','Nirmala UI','Kartika',serif",
    "gu": "'Noto Serif Gujarati','Nirmala UI','Shruti',serif",
    "bn": "'Noto Serif Bengali','Nirmala UI','Vrinda',serif",
    "iast": "'Noto Serif','Cambria',serif",
    "mixed": "'Siddhanta','Noto Serif Devanagari','Noto Serif Telugu','Nirmala UI',serif",
}
FONTS = ("https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@400;600"
         "&family=Noto+Serif+Telugu:wght@400;600&family=Noto+Serif+Kannada"
         "&family=Noto+Serif+Tamil&family=Noto+Serif:ital@0;1&display=swap")
LANG = {"dev": "sa", "tel": "te", "kan": "kn", "tam": "ta", "mal": "ml", "gu": "gu",
        "bn": "bn", "iast": "sa-Latn", "mixed": "sa"}

CSS = """
:root{--ink:#1d1a16;--soft:#6b6259;--rule:#d9d0c3;--paper:#fbf8f2;--hl:#fff1a8;--accent:#8a2f1f}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#ece6dc;--soft:#a79d90;
 --rule:#4a433b;--paper:#1c1916;--hl:#5c4d12;--accent:#e09a7e}}
body{margin:0;background:var(--paper);color:var(--ink);font-family:'Noto Serif',Cambria,serif}
main{max-width:44rem;margin:0 auto;padding:2rem 16px 4rem}
h1{text-align:center;font-weight:600;margin:.5rem 0 .3rem}
.cover{text-align:center;color:var(--soft);font-style:italic}
h2{font-size:1.15rem;color:var(--accent);border-top:1px solid var(--rule);padding-top:1.4rem;margin-top:2.4rem}
dl.prov{display:grid;grid-template-columns:max-content 1fr;gap:.1rem .8rem;font-size:.8rem;color:var(--soft);margin:0 0 1.2rem}
dl.prov dt{font-weight:600}
dl.prov dd{margin:0;overflow-wrap:anywhere}
.text p{font-size:1.45rem;line-height:2.35;margin:0 0 1.1rem;overflow-wrap:break-word}
mark{background:var(--hl);color:inherit;border-radius:2px;padding:0 .1em;white-space:nowrap}
.sv{font-family:'Siddhanta','Sanskrit 2003','Noto Serif Devanagari','Nirmala UI',serif}
ol.sources{font-size:.9rem}
"""


def mark_uncertain(line):
    out, pos = [], 0
    for m in UNCERTAIN.finditer(line):
        out.append(html.escape(line[pos:m.start()]))
        out.append(f'<mark title="uncertain reading">{html.escape(m.group())}</mark>')
        pos = m.end()
    out.append(html.escape(line[pos:]))
    return "".join(out)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    src = pathlib.Path(argv[0])
    out = pathlib.Path(argv[argv.index("-o") + 1]) if "-o" in argv else src.with_name(src.name.removesuffix(".txt").removesuffix(".compile") + ".html")
    meta, snippets = parse(src)
    for w in lint(snippets):
        print("WARN", w)
    title = html.escape(meta.get("title", src.stem))
    parts = [f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
             f'<meta name="viewport" content="width=device-width,initial-scale=1">'
             f'<title>{title}</title><link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>'
             f'<body><main><h1>{title}</h1>']
    if meta.get("note"):
        parts.append(f'<p class="cover">{html.escape(meta["note"])}</p>')
    if has_accents(snippets):
        # a bare combining mark has nothing to sit on; show each on ◌ in an Indic font
        parts.append('<p class="cover">Vedic accents: anudātta <span class="sv">◌॒</span> below, '
                     'svarita <span class="sv">◌॑</span> above, double svarita '
                     '<span class="sv">◌᳚</span>; udātta unmarked.</p>')
    parts.append('<ol class="sources">' + "".join(
        f'<li><a href="#s{n}">{html.escape(s.get("title") or s["source"])}</a></li>'
        for n, s in enumerate(snippets, 1)) + "</ol>")
    for n, s in enumerate(snippets, 1):
        scr = s["script"]
        parts.append(f'<section id="s{n}"><h2>{n}. {html.escape(s.get("title") or s["source"])}</h2><dl class="prov">')
        for key in ("source", "file", "pages", "status", "accents", "note"):
            if s.get(key):
                parts.append(f"<dt>{key}</dt><dd>{html.escape(s[key])}</dd>")
        parts.append(f'</dl><div class="text" lang="{LANG.get(scr, "sa")}" '
                     f'style="font-family:{STACK.get(scr, STACK["mixed"])}">')
        for st in s["text"]:
            parts.append("<p>" + "<br>".join(mark_uncertain(l) for l in st) + "</p>")
        parts.append("</div></section>")
    parts.append("</main></body></html>")
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"{len(snippets)} snippets -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
