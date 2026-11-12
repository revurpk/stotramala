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
    # word-by-word ("words": [[sanskrit, english], …]) above the translation:
    # one span.w per pair — the Sanskrit word a .sans span (so it follows the
    # script switch), its meaning a bare text node (editable on its own)
    wbw = ""
    if v.get("words"):
        items = "\n".join(f'        <span class="w"><span class="sans">{esc(w)}</span> {esc(m)}</span>'
                          for w, m in v["words"])
        wbw = f'      <p class="wbw">\n{items}</p>\n'
    # a text-only verse (no translation or word list yet) has no fold at all
    fold = ""
    if gloss or wbw:
        fold = ('    <details class="gloss">\n'
                f'      <summary>{"word by word · translation" if wbw else "translation"}</summary>\n'
                + wbw +
                (f'      <p>{gloss}</p>\n' if gloss else "")
                + '    </details>\n')
    # a Telugu rendering of the translation ("te"), for the Learn pages; it is
    # Telugu-language text, so it stays Telugu whatever the script switch says
    if v.get("te"):
        fold = fold.replace('    </details>\n',
                            f'      <p lang="te" style="font-style:normal;{TE_FONT}">{esc(v["te"])}</p>\n    </details>\n')
    return (
        f'  <div class="{cls}">\n'
        f'    <p class="lines">\n{body}</p>\n'
        + fold
        + (render_bhashya(v["bhashya"]) + "\n" if v.get("bhashya") else "")
        + '  </div>'
    )


def render_bhashya(paras, summary="bhāṣya", indent="    "):
    """A commentary fold: Sanskrit prose paragraphs, each one .sans line so it
    renders in all three scripts. A paragraph given as {"text":…, "intro":True}
    is the lead-in the commentator sets before the verse, shown a shade softer;
    a "tr" key adds its English translation beneath it."""
    ps = []
    for p in paras:
        text, intro = (p["text"], p.get("intro")) if isinstance(p, dict) else (p, False)
        cls = ' class="bh-intro"' if intro else ""
        ps.append(f'{indent}  <p{cls}><span class="sans">{esc(text)}</span></p>')
        # an English rendering of the paragraph ({"tr": …}), set under it
        if isinstance(p, dict) and p.get("tr"):
            ps.append(f'{indent}  <p class="bh-tr">{esc(p["tr"])}</p>')
    return (f'{indent}<details class="gloss bhashya">\n'
            f'{indent}  <summary>{esc(summary)}</summary>\n'
            + "\n".join(ps) + "\n"
            f'{indent}</details>')


def inline(t):
    """English prose with Sanskrit inside it (the Learn pages): ⟨…⟩ marks IAST,
    set as a .sans span so it follows the script switch; *…* is italic, as the
    printed primers set words not to be translated."""
    import re
    t = esc(t)
    t = re.sub(r"⟨([^⟩]*)⟩", r'<span class="sans" style="font-style:normal;color:var(--ink);">\1</span>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)      # **…** bold
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)


# Telugu-language glosses: Baloo Tammudu 2, the font the page embeds for Telugu
TE_FONT = "font-family:'Baloo Tammudu 2',sans-serif;"
LEARN_P = ('style="font-style:normal;text-align:left;max-width:34rem;'
           'margin:0 auto 1rem;line-height:1.7;"')


def render_learn(sec):
    """The Learn pages' section types, rendered with inline styles so the
    shared shell is untouched: "para" (prose with ⟨IAST⟩), "table" (a paradigm:
    {"head": [...], "rows": [[...]]}, cells as prose), "vocab" ([[IAST,
    English, Telugu], …]) and "en" (an English sentence to put into Sanskrit,
    with "answer" in IAST and "te" its Telugu, folded)."""
    if "para" in sec:
        return f'  <p class="colophon-gloss" {LEARN_P}>{inline(sec["para"])}</p>'
    if "table" in sec:
        tb = sec["table"]
        cell = 'style="padding:.15rem .45rem;text-align:left;vertical-align:top;"'
        head = ("    <tr>" + "".join(f'<th {cell}>{inline(h)}</th>' for h in tb["head"]) + "</tr>\n"
                if tb.get("head") else "")
        rows = "".join("    <tr>" + "".join(f'<td {cell}>{inline(c)}</td>' for c in r) + "</tr>\n"
                       for r in tb["rows"])
        return ('  <div style="overflow-x:auto;overflow-y:hidden;margin:0 auto 1.4rem;max-width:34rem;">\n'
                '  <table class="colophon-gloss" style="font-style:normal;border-collapse:collapse;'
                'margin:0 auto;font-size:.95rem;">\n' + head + rows + '  </table>\n  </div>')
    if "vocab" in sec:
        items = "<br>\n".join(
            f'    <span class="sans" style="font-style:normal;color:var(--ink);">{esc(w)}</span>'
            f' {inline(en)}' + (f' <span lang="te" style="opacity:.85;{TE_FONT}">· {esc(te)}</span>' if te else "")
            for w, en, te in sec["vocab"])
        return f'  <p class="colophon-gloss" {LEARN_P}>\n{items}</p>'
    if "en" in sec:
        fold = ('    <details class="gloss">\n      <summary>sanskrit</summary>\n'
                f'      <p class="lines"><span class="sans">{esc(sec["answer"])}</span></p>\n'
                + (f'      <p lang="te" style="font-style:normal;{TE_FONT}">{esc(sec["te"])}</p>\n' if sec.get("te") else "")
                + '    </details>\n')
        num = f'{esc(sec["num"])}. ' if sec.get("num") else ""
        return ('  <div class="verse viniyoga">\n'
                f'    <p class="colophon-gloss" style="font-style:normal;margin:0;">{num}{inline(sec["en"])}</p>\n'
                + fold + '  </div>')
    return None


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
        f'    <div class="om"><a href="{asset}index.html" title="all stotras">ॐ</a></div>\n'
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
        elif "links" in sec:
            # a contents list for a multi-page work: [(label, href, detail), …],
            # the detail (English) set a size down under each link
            for label, href, detail in sec["links"]:
                parts.append('  <p class="colophon-gloss" style="font-style:normal;text-align:left;'
                             f'max-width:30rem;margin:0 auto 1.1rem;"><a href="{esc(href)}" '
                             f'style="color:var(--accent);">{esc(label)}</a>'
                             + (f'<br><span style="font-size:.88em;opacity:.8;">{esc(detail)}</span>' if detail else "")
                             + '</p>')
        elif "colophon" in sec:
            parts.append(f'  <p class="colophon"><span class="sans">{esc(sec["colophon"])}</span></p>')
            if sec.get("gloss"):
                parts.append(f'  <p class="colophon-gloss">{esc(sec["gloss"])}</p>')
        elif any(k in sec for k in ("para", "table", "vocab", "en")):
            parts.append(render_learn(sec))
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


def load_words(slug, st):
    """Word-by-word glosses kept beside the data file: tools/words/<slug>.txt,
    one line per verse — `N  word = meaning | word = meaning | …`, where N is
    the verse's position on the page (1 = the first section with padas).
    A verse that already has "words" in the data file keeps them."""
    path = DATA_DIR.parent / "words" / f"{slug}.txt"
    if not path.exists():
        return
    verses = [s for s in st["sections"] if isinstance(s, dict) and "padas" in s]
    for ln, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            n, rest = line.split(None, 1)
            pairs = [[x.strip() for x in item.split(" = ", 1)] for item in rest.split(" | ")]
            v = verses[int(n) - 1]
            assert int(n) >= 1 and all(len(p) == 2 and p[0] and p[1] for p in pairs)
        except Exception:
            sys.exit(f"{path.name} line {ln}: cannot read word glosses")
        v.setdefault("words", pairs)


def load_data(slug):
    path = DATA_DIR / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    load_words(slug, mod.STOTRA)
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
