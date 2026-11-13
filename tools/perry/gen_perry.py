# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/perry-NN.py, a Learn page, from the transcription of one lesson of
E. D. Perry's A Sanskrit Primer (tools/perry/lessonNN.txt).

lessonNN.txt, one item a line ("|" separates fields):
  ## text          a heading (English)
  ¶ text           a paragraph of Perry's prose; ⟨…⟩ marks Sanskrit (IAST), *…* italic,
                   **…** bold
  T a | b | …      a table's head row (optional); R a | b | … its rows (cells as prose)
  V iast | English | Telugu      a vocabulary entry (consecutive V lines make one list)
  S n | iast | English | Telugu  a sentence into English, with the editor's translations
  E n | English | iast | Telugu  a sentence into Sanskrit, with the editor's answer
  @N  the leaf;  # a comment;  % the page subtitle;  ! a note for SOURCES (read by wire.py)
Sanskrit is written in IAST: Perry's ç is ś, his accent marks are left out, and a nasal he
writes ṅ before a sibilant is ṃ where his Devanāgarī has anusvāra (see SOURCES).
The English in [square brackets] and all Telugu are the editor's.
usage: gen_perry.py NN
"""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV",
         "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI",
         "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI",
         "XXXVII", "XXXVIII", "XXXIX", "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV"]
NOTE = ("From E. D. Perry’s A Sanskrit Primer (1885), after Georg Bühler’s Leitfaden. Sanskrit "
        "words follow the script switch above, so the lesson reads in Devanāgarī, Telugu or IAST. "
        "Perry’s rules, vocabulary and exercises are given as he prints them; the English in "
        "[square brackets], the Telugu meanings, and the translations and answers under the "
        "exercises (open each to see them) are the editor’s.")
FOOTER = ("Source: Edward Delavan Perry, A Sanskrit Primer, based on the Leitfaden für den "
          "Elementarcursus des Sanskrit of Georg Bühler (Ginn & Co., 1885; public domain), read off "
          "the scan on archive.org; editorial notes in SOURCES §8.1; Telugu glosses, translations and "
          "answers original")


def fields(l, n):
    f = [x.strip() for x in l[1:].split("|")]
    if len(f) != n:
        sys.exit(f"expected {n} fields: {l[:70]}")
    return f


EXTRA = {"intro": ("Introduction", "perry-intro", "Perry intro"),
         "gloss1": ("Glossary I · Sanskrit–English", "perry-gloss-1", "Perry glossary I"),
         "gloss2": ("Glossary II · English–Sanskrit", "perry-gloss-2", "Perry glossary II"),
         "appendix": ("Appendix and Corrections", "perry-appendix", "Perry appendix")}


def main(nn):
    if isinstance(nn, str):
        name, (ttl, slug, app) = nn, EXTRA[nn]
        r = ""
    else:
        name, slug, r = f"lesson{nn:02d}", f"perry-{nn:02d}", ROMAN[nn]
        ttl, app = f"Lesson {r}", f"Perry {r}"
    src = (HERE / f"{name}.txt").read_text(encoding="utf-8").splitlines()
    secs, table, vocab = [], None, None
    sub = next((x.strip()[1:].strip() for x in src if x.strip().startswith("%")), None)
    for raw in src:
        l = raw.strip()
        if l.startswith(("%", "!")):
            continue
        if not l or l.startswith(("#", "@")) and not l.startswith("##"):
            continue
        kind = l[:2] if l.startswith("##") else l[0]
        if kind != "R" and table is not None:
            secs.append({"table": table}); table = None
        if kind != "V" and vocab is not None:
            secs.append({"vocab": vocab}); vocab = None
        if kind == "##":
            secs.append({"heading": l[2:].strip()})
        elif kind == "¶":
            secs.append({"para": l[1:].strip()})
        elif kind == "T":
            table = {"head": [x.strip() for x in l[1:].split("|")], "rows": []}
        elif kind == "R":
            if table is None:
                table = {"rows": []}
            table["rows"].append([x.strip() for x in l[1:].split("|")])
        elif kind == "V":
            vocab = (vocab or []) + [fields(l, 3)]
        elif kind == "S":
            n, iast, en, te = fields(l, 4)
            secs.append({"padas": [iast], "num": n, "gloss": en, "te": te, "prose": True})
        elif kind == "E":
            n, en, iast, te = fields(l, 4)
            secs.append({"en": en, "num": n, "answer": iast, "te": te})
        else:
            sys.exit(f"unparsed line: {l[:70]}")
    if table is not None:
        secs.append({"table": table})
    if vocab is not None:
        secs.append({"vocab": vocab})
    st = {"deity": "learn", "doc_title": f"Perry · {ttl}", "app_title": app,
          "h1": f"Sanskrit Primer · {ttl}", "subtitle": sub or TITLES[nn], "note": NOTE,
          "footer": FOOTER, "toc": True, "sections": secs}
    q = lambda v: repr(v) if isinstance(v, bool) else json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# Perry, A Sanskrit Primer, {ttl.lower()} (tools/perry/{name}.txt); written by",
           "# tools/perry/gen_perry.py. See SOURCES §8.1.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"{slug}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{name}: {len(secs)} sections")


TITLES = {1: "Verbs: the present indicative of the a-class (vadati); visarga at the end of a word",
          2: "Verbs: the a-class continued (gacchati, tiṣṭhati); nouns in a (deva, phala); the combination of vowels",
          3: "Verbs: the accented a-class (kṣipati, siñcati); the other cases of nouns in a; the force of the cases"}

if __name__ == "__main__":
    main(int(sys.argv[1]) if sys.argv[1].isdigit() else sys.argv[1])
