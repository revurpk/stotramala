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
    if st.get("src") == "tel":      # Telugu-language page: Telugu is the source
        head = head.replace('<html lang="en" data-script="iast">',
                            '<html lang="en" data-script="tel" data-src="tel">')
    elif st.get("script") == "dev":  # accented Vedic page: open in Devanāgarī
        head = head.replace('<html lang="en" data-script="iast">',
                            '<html lang="en" data-script="dev">')
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
    # "prose": long ritual formulae (saṅkalpa, āvāhana) set a size down,
    # using the shell's existing .viniyoga style
    cls = "verse viniyoga" if v.get("prose") else "verse"
    return (
        f'  <div class="{cls}">\n'
        f'    <p class="lines">\n{body}</p>\n'
        '    <details class="gloss">\n'
        '      <summary>translation</summary>\n'
        f'      <p>{gloss}</p>\n'
        '    </details>\n'
        + (render_bhashya(v["bhashya"]) + "\n" if v.get("bhashya") else "")
        + '  </div>'
    )


def render_bhashya(paras, summary="bhāṣya", indent="    "):
    """A commentary fold: Sanskrit prose paragraphs, each one .sans line so it
    renders in all three scripts. A paragraph given as {"text":…, "intro":True}
    is the lead-in the commentator sets before the verse, shown a shade softer."""
    ps = []
    for p in paras:
        text, intro = (p["text"], p.get("intro")) if isinstance(p, dict) else (p, False)
        cls = ' class="bh-intro"' if intro else ""
        ps.append(f'{indent}  <p{cls}><span class="sans">{esc(text)}</span></p>')
    return (f'{indent}<details class="gloss bhashya">\n'
            f'{indent}  <summary>{esc(summary)}</summary>\n'
            + "\n".join(ps) + "\n"
            f'{indent}</details>')


def load_corrections(slug):
    """Human-reviewed overrides: rendering fixes keyed by .sans node index →
    {script: text}, and under "text" wording fixes keyed by editable-prose
    index → {old, new}. Merged from reviewer exports by
    tools/apply_corrections.py. Absent file → no overrides."""
    import json
    path = pathlib.Path(__file__).resolve().parent / "corrections" / f"{slug}.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    # proposed new verses are a record for the maintainer, not page content:
    # an accepted one goes into the data file instead
    data.pop("additions", None)
    return data


def render_body(st, slug, asset):
    parts = [
        '\n\n  <header>\n'
        '    <div class="om">ॐ</div>\n'
        f'    <h1>{esc(st["h1"])}</h1>\n'
        f'    <p class="subtitle">{esc(st["subtitle"])}</p>\n'
        '    <hr class="titlerule">\n'
        + (f'    <p class="subtitle" style="font-size:.8rem;max-width:26rem;margin:.5rem auto 0;">{esc(st["note"])}</p>\n' if st.get("note") else "")
        # Optional recitation link. The page stays self-contained — this is a
        # plain outbound link the reader chooses to follow, never an embed, so
        # nothing is fetched from YouTube at read time and no one is tracked
        # for simply opening the page.
        + (f'    <p class="guidelink">▸ <a href="{esc(st["audio"])}" target="_blank" rel="noopener noreferrer">listen: {esc(st.get("audio_label", "recitation"))}</a> <span style="opacity:.7">(YouTube)</span></p>\n' if st.get("audio") else "")
        # Optional links between the parts of a multi-page work (the Gītā's
        # chapters): STOTRA["nav"] = [(label, href-relative-to-this-page), …]
        + ('    <p class="guidelink">' + " · ".join(
            f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in st["nav"]) + '</p>\n' if st.get("nav") else "")
        + f'    <p class="guidelink"><a href="{asset}index.html">all stotras</a> · <a href="{asset}pronunciation.html">pronunciation guide</a></p>\n'
        '  </header>\n'
    ]
    # Optional contents panel for long pages (STOTRA["toc"] = True): a
    # collapsible list linking to every `heading`, in the gloss's style, and
    # a small ↑ back-link on each heading. Off by default, so every other
    # page renders byte-identical.
    toc = st.get("toc")
    heads = [s["heading"] for s in st["sections"] if isinstance(s, dict) and "heading" in s]
    if toc and heads:
        links = "<br>\n".join(f'        <a href="#sec-{i}" style="color:var(--accent);'
                              f'text-decoration:none;">{esc(h)}</a>'
                              for i, h in enumerate(heads, 1))
        parts.append(
            '  <details class="gloss" id="contents" style="max-width:26rem;margin:-1rem auto 2.4rem;">\n'
            '    <summary>contents</summary>\n'
            '    <p style="font-style:normal;text-align:left;font-size:.92rem;line-height:1.85;">\n'
            f'{links}</p>\n'
            '  </details>')
    hn = 0
    for sec in st["sections"]:
        if sec == "ornament":
            parts.append('  <div class="ornament">❧</div>')
        elif "heading" in sec:
            # section title (e.g. the parts of a vrata); Latin, not transliterated
            if toc:
                hn += 1
                parts.append(f'  <p class="speaker" id="sec-{hn}">{esc(sec["heading"])} '
                             '<a href="#contents" title="contents" style="color:inherit;'
                             'opacity:.5;text-decoration:none;font-variant:normal;">↑</a></p>')
            else:
                parts.append(f'  <p class="speaker">{esc(sec["heading"])}</p>')
        elif "rubric" in sec:
            # a ritual instruction, in English, between the recited texts
            parts.append('  <p class="colophon-gloss" style="margin:0 auto 1.4rem;'
                         f'max-width:30rem;">{esc(sec["rubric"])}</p>')
        elif "speaker" in sec:
            # who speaks the verses that follow (arjuna uvāca), in Sanskrit
            parts.append(f'  <div class="speaker"><span class="sans">{esc(sec["speaker"])}</span></div>')
        elif "bhashya" in sec and "padas" not in sec:
            # a commentary passage not tied to one verse (a chapter's preamble)
            parts.append('  <div class="verse">\n'
                         + render_bhashya(sec["bhashya"], sec.get("summary", "bhāṣya")) + "\n  </div>")
        elif "colophon" in sec:
            parts.append(f'  <p class="colophon"><span class="sans">{esc(sec["colophon"])}</span></p>')
            if sec.get("gloss"):
                parts.append(f'  <p class="colophon-gloss">{esc(sec["gloss"])}</p>')
        else:
            parts.append(render_verse(sec, asset))
    parts.append(
        '\n  <footer>\n'
        f'    {esc(st["footer"])}\n'
        '    <div class="review">\n'
        '      <button type="button" id="corrToggle" aria-pressed="false">✎ suggest a correction</button>\n'
        '      <button type="button" id="corrExport" hidden>⬇ export corrections</button>\n'
        '    </div>\n'
        '    <p class="review-note">Tap any line to edit its rendering in the\n'
        '      current script, or any title, heading, note or translation (open it\n'
        '      first) to edit its wording; use “+ propose a verse or mantra” to add\n'
        '      one that is missing, with its translation. Then export your corrections\n'
        '      as a file to send to the maintainer. Nothing leaves your device until you export.</p>\n'
        '  </footer>\n'
    )
    import json
    corr = json.dumps(load_corrections(slug), ensure_ascii=False)
    parts.append(
        '  <script>\n'
        f'    document.documentElement.dataset.slug = "{slug}";\n'
        f'    window.STOTRA_CORRECTIONS = {corr};\n'
        '  </script>\n'
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
    page = sub_head(head, st, asset) + render_body(st, slug, asset) + tail
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
