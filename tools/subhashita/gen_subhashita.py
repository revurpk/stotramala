# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/subhashita-<name>.py (Bhartṛhari's Śatakatraya) from
tools/subhashita/<name>.verses.txt (key | shown number | pādas separated by " / ")
and <name>.gloss.txt (key | English | Telugu).   usage: gen_subhashita.py NAME|all"""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
META = {
 "niti": ("Nītiśatakam", "Nītiśataka", "The Hundred Verses on Wise Conduct · Bhartṛhari",
          "Bhartṛhari’s hundred verses on worldly wisdom: fools and the learned, good company, pride and generosity, fortune and fate. The verse numbers are those of the Wikisource text; the first two verses, unnumbered there, are a benediction and the poet’s well-known verse on his own disappointed love."),
 "shringara": ("Śṛṅgāraśatakam", "Śṛṅgāraśataka", "The Hundred Verses on Love · Bhartṛhari",
          "Bhartṛhari’s hundred verses on love and the women who inspire it. Numbers are the book’s own (the second śataka); those with an asterisk (35*1 …) are verses the critical text sets apart as doubtful additions."),
 "sumati": ("సుమతీ శతకము", "Sumati Śatakamu", "Sumati Śatakamu · Baddena",
          "A Telugu-language śataka of moral counsel, attributed to Baddena (Bhadrabhūpāla), each verse ending with the address “sumatī” (“O wise one”). The Telugu is the source; the IAST is a reading aid for pronunciation. The English is original.", "tel"),
 "vemana": ("వేమన శతకము", "Vemana Śatakamu", "Vemana Śatakamu · a hundred verses of Vemana",
          "A selection of a hundred of the Telugu poet Vemana’s verses, each ending with the signature line “viśvadābhirāma vinura vēma” (“Hear, Vema, delight of the world”). The Telugu is the source; the IAST is a reading aid for pronunciation. The English is original.", "tel"),
 "vairagya": ("Vairāgyaśatakam", "Vairāgyaśataka", "The Hundred Verses on Dispassion · Bhartṛhari",
          "Bhartṛhari’s hundred verses on renunciation, the third of the three śatakas. Numbers are the book’s own (the third śataka); those with an asterisk (3.8*1 …) are verses the critical text sets apart as doubtful additions, and a few verses that the source leaves without a number are given without one."),
}
FOOT = ("Source: Sanskrit Wikisource — {t} (Bhartṛhari; public domain), converted to IAST; "
        "English and Telugu translations original; editorial notes in SOURCES §9")
FOOT_TEL = ("Source: Telugu Wikisource — {t} (public domain); English translations original; "
            "editorial notes in SOURCES §9")
def load(name):
    verses = []
    for l in (HERE / f"{name}.verses.txt").read_text(encoding="utf-8").splitlines():
        if not l.strip() or l[0] == "#": continue
        k, shown, pad = [x.strip() for x in l.split("|", 2)]
        verses.append((k, shown, [p.strip() for p in pad.split(" / ")]))
    gl = {}
    for gp in sorted(HERE.glob(f"{name}.gloss*.txt")):
        for l in gp.read_text(encoding="utf-8").splitlines():
            if not l.strip() or l[0] == "#": continue
            f = [x.strip() for x in l.split("|")]
            if len(f) != 3: sys.exit(f"{name}: bad gloss line: {l[:60]}")
            gl[f[0]] = (f[1], f[2])
    return verses, gl
def padas(p):
    if len(p) == 2: return [p[0] + " |", p[1]]
    if len(p) == 4: return [p[0], p[1] + " |", p[2], p[3]]
    if len(p) == 3: return [p[0], p[1] + " |", p[2]]
    return p[:-1] + [p[-1]]
def main(name):
    verses, gl = load(name)
    m = META[name]
    t, app, sub, note = m[:4]
    tel = len(m) > 4
    secs, missing = [], []
    for k, shown, p in verses:
        e = gl.get(k)
        if not e: missing.append(k)
        d = {"padas": p if tel else padas(p), "num": (shown if tel else f"|| {shown} ||") if shown else "", "gloss": e[0] if e else "(translation to follow)"}
        if e and e[1]: d["te"] = e[1]
        secs.append(d)
    st = {**({"src": "tel"} if tel else {}), "deity": "subhashita", "doc_title": t, "app_title": app, "h1": t, "subtitle": sub, "note": note,
          "footer": (FOOT_TEL if tel else FOOT).format(t=t), "sections": secs}
    q = lambda v: json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# {t}; written by tools/subhashita/gen_subhashita.py from tools/subhashita/{name}.verses.txt and .gloss.txt. See SOURCES §9.",
           "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"subhashita-{name}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"subhashita-{name}: {len(secs)} verses, {len(missing)} without a translation yet")
if __name__ == "__main__":
    for n in (META if sys.argv[1] == "all" else [sys.argv[1]]): main(n)
