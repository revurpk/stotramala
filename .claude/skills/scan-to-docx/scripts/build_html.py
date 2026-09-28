# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools>=4.40"]
# ///
"""Build a self-contained HTML reading copy of a compilation file, with
Vedic accents rendered properly.

    uv run build_html.py <compilation.txt> [-o out.html]
        [--font "Baloo Tammudu 2"] [--css-accents | --font-accents]

  --font         a Google Fonts family to set the Indic text in (first in
                 the stack; loaded from Google Fonts)
  --css-accents  draw the svaras with CSS instead of the font's glyphs
  --font-accents use the font's own svara glyphs even with --font
                 With --font and neither flag, the font's cmap is checked:
                 if it lacks ॑ ॒ ᳚ (most display fonts do — Baloo, Mukta,
                 Ramabhadra…), the accents are drawn with CSS.

CSS ACCENTS: each accented akṣara is wrapped in a span and its stroke or bar
is a pseudo-element placed over or under that span, so it sits on the whole
cluster whatever the font. The real mark stays in the text (zero-size), so
copying and searching still give the accented Unicode.

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
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from compile_lib import UNCERTAIN, has_accents, lint, parse, toc  # noqa: E402

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
nav.toc{border:1px solid var(--rule);border-radius:6px;padding:.8rem 1.2rem;margin:1.6rem 0}
.toch{font-weight:600;margin:0 0 .4rem}
nav.toc ul{list-style:none;margin:0;padding:0}
nav.toc li{margin:.15rem 0}
nav.toc li.l1{font-weight:600;margin-top:.6rem}
nav.toc li.l2{padding-left:1.2rem}
nav.toc li.l3{padding-left:2.4rem;font-size:.92rem}
nav.toc a{color:var(--accent);text-decoration:none}
.pg{color:var(--soft);font-size:.75rem;white-space:nowrap}
.text h3{font-size:1.5rem;color:var(--accent);margin:2rem 0 .8rem;font-weight:600}
.text h4{font-size:1.3rem;color:var(--accent);margin:1.4rem 0 .6rem;font-weight:600}
a.up{font-size:.8rem;color:var(--soft);text-decoration:none;font-family:'Noto Serif',serif}
.pm{text-align:right;font-size:.75rem;color:var(--soft);margin:.4rem 0;font-family:'Noto Serif',serif}
.text p.fn{font-size:1.05rem;line-height:1.9;color:var(--soft);border-top:1px solid var(--rule);padding-top:.4rem}
"""

# CSS-drawn svaras: .ac wraps one akṣara; s = svarita (stroke above),
# a = anudātta (bar below), d = dīrgha svarita (two strokes above).
# Offsets are in em of the text, so they scale with the font size.
CSS_ACCENTS = """
.ac{position:relative}
.acm{font-size:0}
.ac.s::before,.ac.d::before{content:"";position:absolute;left:var(--cx,50%);top:var(--sv-top,%SVTOP%em);
 height:.28em;transform:translateX(-50%);pointer-events:none}
.ac.s::before{width:.06em;background:currentColor}
.ac.d::before{width:.09em;border-left:.06em solid currentColor;border-right:.06em solid currentColor}
.ac.a::after{content:"";position:absolute;left:var(--cx,50%);width:var(--bw,.4em);top:var(--an-top,%ANTOP%em);
 height:.06em;transform:translateX(-50%);background:currentColor;pointer-events:none}
.sv-demo{display:inline-block}
"""

# Fine placement: the pseudo-elements are positioned from the span's box,
# whose height is the font's line metrics, not the ink — display fonts like
# Baloo have a tall box. This measures each akṣara's ink with canvas
# measureText (cached per font+text) and sets its stroke just above the
# highest ink and its bar just below the lowest, centred on the ink. Without
# JS the CSS defaults (from the font's metrics) still apply.
JS_ACCENTS = """<script>
(function(){
 var ctx=document.createElement('canvas').getContext('2d'),cache={};
 function place(){
  document.querySelectorAll('.ac').forEach(function(el){
   var cs=getComputedStyle(el),fs=parseFloat(cs.fontSize),t=el.firstChild&&el.firstChild.nodeValue;
   if(!t||!fs)return;
   var font=cs.fontStyle+' '+cs.fontWeight+' '+cs.fontSize+' '+cs.fontFamily,k=font+'|'+t,m=cache[k];
   if(!m){ctx.font=font;var r=ctx.measureText(t);m=cache[k]={fa:r.fontBoundingBoxAscent,a:r.actualBoundingBoxAscent,
     d:r.actualBoundingBoxDescent,l:r.actualBoundingBoxLeft,w:r.actualBoundingBoxLeft+r.actualBoundingBoxRight,adv:r.width};}
   if(m.fa===undefined)return;
   var g=.05*fs,s=el.style;
   s.setProperty('--sv-top',(m.fa-m.a-g-.28*fs)+'px');
   s.setProperty('--an-top',(m.fa+m.d+1.8*g)+'px');
   s.setProperty('--cx',(m.w/2-m.l)+'px');
   s.setProperty('--bw',Math.max(.3*fs,Math.min(m.w*.7,.6*fs))+'px');
  });
 }
 (document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(place);
})();
</script>"""


def css_defaults(family):
    """Fallback stroke/bar offsets (em, from the span top) from the font's
    line ascent and the height of a plain consonant; used when JS is off."""
    import io, re, urllib.parse, urllib.request
    try:
        from fontTools.ttLib import TTFont
        url = "https://fonts.googleapis.com/css2?family=" + urllib.parse.quote_plus(family)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/4.0"})
        css = urllib.request.urlopen(req, timeout=20).read().decode()
        f = TTFont(io.BytesIO(urllib.request.urlopen(re.findall(r"url\((.*?)\)", css)[0], timeout=30).read()))
        upm, asc = f["head"].unitsPerEm, f["hhea"].ascent
        gs = f.getGlyphSet(); cmap = f.getBestCmap()
        from fontTools.pens.boundsPen import BoundsPen
        pen = BoundsPen(gs); gs[cmap[0x0C15]].draw(pen)   # క
        top = pen.bounds[3] if pen.bounds else .55 * upm
        return round((asc - top) / upm - .05 - .28, 3), round(asc / upm + .2, 3)
    except Exception:
        return -.12, .95


SVARA = {"॑": "s", "॒": "a", "᳚": "d"}


def css_accents(text):
    """Escape text, wrapping each accented akṣara as <span class="ac s|a|d">.

    An akṣara is a letter, any virama+letter conjuncts after it, and its
    combining marks (vowel signs, anusvāra, visarga, a final virama)."""
    out, i, n = [], 0, len(text)
    while i < n:
        j = i
        if unicodedata.category(text[i]) == "Lo":
            j = i + 1
            while j < n:
                c = text[j]
                if c in SVARA:
                    break
                cat = unicodedata.category(c)
                if cat in ("Mn", "Mc"):
                    j += 1
                    if "VIRAMA" in unicodedata.name(c, "") and j < n and unicodedata.category(text[j]) == "Lo":
                        j += 1
                    continue
                break
        else:
            j = i + 1
        k = j
        while k < n and text[k] in SVARA:
            k += 1
        cluster = html.escape(text[i:j])
        if k > j and j > i and not text[i:j].isspace():
            cls = " ".join(dict.fromkeys(SVARA[c] for c in text[j:k]))
            out.append(f'<span class="ac {cls}">{cluster}<span class="acm">{text[j:k]}</span></span>')
        else:
            out.append(cluster + html.escape(text[j:k]))
        i = k
    return "".join(out)


def mark_uncertain(line, esc=html.escape):
    out, pos = [], 0
    for m in UNCERTAIN.finditer(line):
        out.append(esc(line[pos:m.start()]))
        out.append(f'<mark title="uncertain reading">{esc(m.group())}</mark>')
        pos = m.end()
    out.append(esc(line[pos:]))
    return "".join(out)


def font_has_svaras(family):
    """True/False from the Google Fonts file's cmap; None if it can't be fetched."""
    import io
    import re
    import urllib.parse
    import urllib.request
    try:
        from fontTools.ttLib import TTFont
        url = "https://fonts.googleapis.com/css2?family=" + urllib.parse.quote_plus(family)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/4.0"})  # old UA -> TTF
        css = urllib.request.urlopen(req, timeout=20).read().decode()
        cmap = TTFont(io.BytesIO(urllib.request.urlopen(re.findall(r"url\((.*?)\)", css)[0], timeout=30).read())).getBestCmap()
        return all(ord(c) in cmap for c in SVARA)
    except Exception as e:  # offline, unknown family…
        print(f"note: couldn't check {family!r} for svara glyphs ({e.__class__.__name__}); drawing them with CSS")
        return None


def main(argv):
    if not argv:
        sys.exit(__doc__)
    src = pathlib.Path(argv[0])
    out = pathlib.Path(argv[argv.index("-o") + 1]) if "-o" in argv else src.with_name(src.name.removesuffix(".txt").removesuffix(".compile") + ".html")
    font = argv[argv.index("--font") + 1] if "--font" in argv else None
    meta, snippets = parse(src)
    for w in lint(snippets):
        print("WARN", w)
    accented = has_accents(snippets)
    if "--css-accents" in argv:
        use_css = True
    elif "--font-accents" in argv or not font or not accented:
        use_css = False
    else:
        use_css = font_has_svaras(font) is not True
    if font:
        print(f"font: {font}; svaras {'drawn with CSS' if use_css else 'from the font'}")
    stack = dict(STACK)
    fonts = FONTS
    if font:
        for k in stack:
            if k != "iast":
                stack[k] = f"'{font}'," + stack[k]
        fonts += "&family=" + font.replace(" ", "+") + ":wght@400;600"
    esc = css_accents if use_css else html.escape
    acss = ""
    if use_css:
        svtop, antop = css_defaults(font) if font else (-.12, .95)
        acss = CSS_ACCENTS.replace("%SVTOP%", str(svtop)).replace("%ANTOP%", str(antop))
    title = html.escape(meta.get("title", src.stem))
    parts = [f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
             f'<meta name="viewport" content="width=device-width,initial-scale=1">'
             f'<title>{title}</title><link rel="stylesheet" href="{fonts}">'
             f'<style>{CSS}{acss}</style></head>'
             f'<body><main id="top"><h1>{title}</h1>']
    if meta.get("note"):
        parts.append(f'<p class="cover">{html.escape(meta["note"])}</p>')
    if accented:
        if use_css:
            # show each drawn accent on a dotted circle in the text font
            demo = lambda m: f'<span class="sv-demo" style="font-family:{stack["mixed"]}">{css_accents("◌" + m)}</span>'
            parts.append(f'<p class="cover">Vedic accents: anudātta {demo(chr(0x952))} below, '
                         f'svarita {demo(chr(0x951))} above, double svarita {demo(chr(0x1CDA))}; udātta unmarked.</p>')
        else:
            # a bare combining mark has nothing to sit on; show each on ◌ in an Indic font
            parts.append('<p class="cover">Vedic accents: anudātta <span class="sv">◌॒</span> below, '
                         'svarita <span class="sv">◌॑</span> above, double svarita '
                         '<span class="sv">◌᳚</span>; udātta unmarked.</p>')
    # contents: linked, nested by heading level, with the printed page
    parts.append('<nav class="toc"><p class="toch">Contents</p><ul>')
    for level, bid, text, page in toc(meta, snippets):
        sid = bid.split("-")[0]
        scr = next(s["script"] for s in snippets if s["id"] == sid)
        style = "" if level == 1 else f' style="font-family:{stack.get(scr, stack["mixed"])}"'
        pg = f' <span class="pg">p. {html.escape(page)}</span>' if page else ""
        parts.append(f'<li class="l{level}"><a href="#{bid}"{style}>{html.escape(text)}</a>{pg}</li>')
    parts.append("</ul></nav>")
    for n, s in enumerate(snippets, 1):
        scr = s["script"]
        parts.append(f'<section id="{s["id"]}"><h2>{n}. {html.escape(s.get("title") or s["source"])}</h2><dl class="prov">')
        for key in ("source", "file", "pages", "status", "accents", "note"):
            if s.get(key):
                parts.append(f"<dt>{key}</dt><dd>{html.escape(s[key])}</dd>")
        parts.append(f'</dl><div class="text" lang="{LANG.get(scr, "sa")}" '
                     f'style="font-family:{stack.get(scr, stack["mixed"])}">')
        for b in s["blocks"]:
            k = b["kind"]
            if k == "page":
                parts.append(f'<p class="pm">[p. {html.escape(b["text"])}]</p>')
            elif k in ("h2", "h3"):
                tag = "h3" if k == "h2" else "h4"
                parts.append(f'<{tag} id="{b["id"]}">{mark_uncertain(b["text"], esc)} '
                             f'<a class="up" href="#top" title="contents">↑</a></{tag}>')
            elif k == "fn":
                mk = f"({html.escape(b['mark'])}) " if b["mark"] else ""
                parts.append(f'<p class="fn">{mk}{mark_uncertain(b["text"], esc)}</p>')
            else:
                parts.append("<p>" + "<br>".join(mark_uncertain(l, esc) for l in b["lines"]) + "</p>")
        parts.append("</div></section>")
    parts.append("</main>" + (JS_ACCENTS if use_css else "") + "</body></html>")
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"{len(snippets)} snippets -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:])
