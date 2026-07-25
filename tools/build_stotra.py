# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Generate a stotra page from the shared Durgā shell + per-stotra content.

Every stotra page is one self-contained file: the head, CSS, embedded
Baloo Tammudu 2 subset, script selector, and inlined teltools
transliterator are shared, and only the title and verses differ. Rather
than hand-copy that ~900-line shell, this reads it from the canonical
Durgā page and injects each stotra's header, verses, and footer.

The IAST verse text is the single source of truth; Devanāgarī and Telugu
are produced in the browser at switch time, exactly as on the Durgā page.

Data lives in tools/stotras/<slug>.py as a module-level dict `STOTRA`.
Build one, or all:

    python tools/build_stotra.py ganesha-pancharatnam
    python tools/build_stotra.py --all
"""

import html as _html
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHELL = ROOT / "stotra" / "devi" / "durga-saptashloki-iast.html"   # canonical shell source
DATA_DIR = pathlib.Path(__file__).resolve().parent / "stotras"

HEAD_MARK = '<main class="page">'
TAIL_MARK = '</main>'


def load_shell():
    s = SHELL.read_text(encoding="utf-8")
    hi = s.index(HEAD_MARK) + len(HEAD_MARK)
    ti = s.index(TAIL_MARK)
    return s[:hi], s[ti:]        # head (through <main…>), tail (from </main>)


def esc(t):
    # verses/titles are trusted authored text; escape only &,<,> so the
    # daṇḍa '|' etc. pass through untouched
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def sub_head(head, st, asset):
    head = head.replace("<title>Durgā Saptaślokī</title>",
                        f"<title>{esc(st['doc_title'])}</title>")
    head = head.replace('content="Saptaślokī"', f'content="{esc(st["app_title"])}"')
    head = head.replace('href="../apple-touch-icon.png"',
                        f'href="{asset}apple-touch-icon.png"')
    return head


def render_verse(v, asset):
    padas = v["padas"]
    lines = []
    for i, p in enumerate(padas):
        br = "<br>" if i < len(padas) - 1 or v.get("num") else ""
        lines.append(f'      <span class="sans">{esc(p)}</span>{br}')
    if v.get("num"):
        lines.append(f'      <span class="num sans">{esc(v["num"])}</span>')
    body = "\n".join(lines)
    gloss = esc(v["gloss"])
    return (
        '  <div class="verse">\n'
        f'    <p class="lines">\n{body}</p>\n'
        '    <details class="gloss">\n'
        '      <summary>translation</summary>\n'
        f'      <p>{gloss}</p>\n'
        '    </details>\n'
        '  </div>'
    )


def render_body(st, asset):
    parts = [
        '\n\n  <header>\n'
        '    <div class="om">ॐ</div>\n'
        f'    <h1>{esc(st["h1"])}</h1>\n'
        f'    <p class="subtitle">{esc(st["subtitle"])}</p>\n'
        '    <hr class="titlerule">\n'
        f'    <p class="guidelink"><a href="{asset}pronunciation.html">pronunciation guide</a></p>\n'
        '  </header>\n'
    ]
    for sec in st["sections"]:
        if sec == "ornament":
            parts.append('  <div class="ornament">❧</div>')
        else:
            parts.append(render_verse(sec, asset))
    parts.append(
        '\n  <footer>\n'
        f'    {esc(st["footer"])}\n'
        '  </footer>\n\n'
    )
    return "\n\n".join(parts)


def load_data(slug):
    path = DATA_DIR / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.STOTRA


def build(slug):
    st = load_data(slug)
    out = ROOT / "stotra" / st["deity"] / f"{slug}-iast.html"
    depth = len(out.relative_to(ROOT).parts) - 1        # dirs above the file
    asset = "../" * depth
    head, tail = load_shell()
    page = sub_head(head, st, asset) + render_body(st, asset) + tail
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8", newline="\n")
    print(f"built {out.relative_to(ROOT)}  ({len(page.encode('utf-8')):,} bytes)")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    if argv[0] == "--all":
        slugs = sorted(p.stem for p in DATA_DIR.glob("*.py") if p.stem != "__init__")
    else:
        slugs = argv
    for slug in slugs:
        build(slug)


if __name__ == "__main__":
    main(sys.argv[1:])
