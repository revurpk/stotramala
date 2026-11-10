# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/nirukta-N.py from the transcription tools/nirukta/niruktaN.txt and
the English key tools/nirukta/glossN.txt.

niruktaN.txt: one paragraph a line; "> …" a quotation Sarup sets apart; a khaṇḍa closes
with ॥ N ॥; "= …" a closing or opening line in Sanskrit (a colophon); "+ note: [ Sanskrit ]"
an editorial note in English with a Sanskrit passage, set as a rubric and a small passage;
"@N" records the leaf; other "#" lines are comments; a line ending "#v" carries a
number Sarup prints on a quoted verse, kept in the text and not read as a khaṇḍa's.
glossN.txt: "N | heading | gloss" for each khaṇḍa.
Each khaṇḍa becomes a heading (for the contents panel) and one unit whose padas are its
paragraphs and quotations, with the khaṇḍa number and the English gloss.
usage: gen_nirukta.py N
"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
from dev2iast import dev2iast  # noqa: E402

DIG = str.maketrans("०१२३४५६७८९", "0123456789")
SUBTITLE = {1: "Yāska's Nirukta, adhyāya 1 · the introduction: the four kinds of words, "
               "the particles, the derivation of nouns, the meaning of the mantras",
            2: "Yāska's Nirukta, adhyāya 2 · the rules of derivation, and the first word-lists of the Nighaṇṭu: "
               "earth, gold, sky, rays, night, dawn, cloud, speech, water, rivers, horses",
            3: "Yāska's Nirukta, adhyāya 3 · the rest of the Nighaṇṭu's synonyms: offspring and inheritance, "
               "men, the numbers, comparison, and the words that come in pairs"}
NOTE = ("Yāska's Nirukta, the oldest surviving treatise on Vedic etymology and a commentary on the "
        "Nighaṇṭu. The text is Lakshman Sarup's critical edition (1927); words in square brackets are "
        "found in only part of the manuscripts. Quotations Sarup sets apart (mantras, and phrases from "
        "the Brāhmaṇas) are given as separate lines. Sarup prints svaras on the quoted mantras; they are "
        "not carried here. The English under each khaṇḍa is a summary, not a translation.")
FOOTER = ("Source: Lakshman Sarup, The Nighaṇṭu and the Nirukta: Sanskrit text (University of the Panjab, "
          "1927; public domain), read off the scan on archive.org and converted to IAST; editorial notes in "
          "SOURCES §5.31; summaries original")
COLOPHON = {"श्रीयास्कमुनिविरचितं निरुक्तं प्रारभ्यते": "Here begins the Nirukta composed by the sage Yāska.",
            "इति प्रथमोऽध्यायः": "Thus the first adhyāya.",
            "इति निरुक्ते पूर्वषट्के प्रथमोऽध्यायः समाप्तः": "Here ends the first adhyāya of the first six of the Nirukta."}


def iast(s):
    t = dev2iast(re.sub(r"\s+", " ", s).strip())
    t = t.replace("॥", "||").replace("।", "|").replace("ऽ", "'")
    return re.sub(r"\s+", " ", t).strip()


def main(n):
    gloss = {}
    for raw in (HERE / f"gloss{n}.txt").read_text(encoding="utf-8").splitlines():
        if raw.strip() and not raw.startswith("#"):
            k, head, g = (x.strip() for x in raw.split("|", 2))
            gloss[int(k)] = (head, g)
    secs, padas, done = [], [], []
    for raw in (HERE / f"nirukta{n}.txt").read_text(encoding="utf-8").splitlines():
        l = raw.strip()
        if not l or l.startswith(("@", "#")):
            continue
        if l.startswith("="):
            body = l[1:].strip().strip("॥ ").rstrip("।").strip()
            if "|" in body:          # "= Sanskrit | English"
                skt, en = (x.strip() for x in l[1:].split("|", 1))
                secs.append({"colophon": iast(skt), "gloss": en})
                continue
            if body not in COLOPHON:
                sys.exit(f"colophon without an English gloss: {body}")
            secs.append({"colophon": iast(l[1:]), "gloss": COLOPHON[body]})
            continue
        if l.startswith("+"):
            note, _, skt = l[1:].partition(": [")
            secs.append({"rubric": note.strip().rstrip(":") + ("" if note.strip().endswith(".") else ".")})
            if skt:
                secs.append({"padas": [iast("[ " + skt.strip())], "num": "", "gloss": "", "prose": True})
            continue
        if l.startswith(">"):
            l = l[1:].strip()
        verse = l.endswith("#v")      # a number Sarup prints on a quoted verse, not a khaṇḍa's
        l = l[:-2].strip() if verse else l
        m = None if verse else re.search(r"॥\s*([०-९]+)\s*॥\s*$", l)
        if not m:
            padas.append(iast(l))
            continue
        k = int(m.group(1).translate(DIG))
        padas.append(iast(l[:m.start()]))
        if k != len(done) + 1:
            sys.exit(f"khaṇḍa {k} out of order after {len(done)}")
        head, g = gloss[k]
        secs.append({"heading": f"{n}.{k} · {head}"})
        secs.append({"padas": padas, "num": f"|| {k} ||", "gloss": g, "prose": True})
        padas, done = [], done + [k]
    if padas:
        sys.exit(f"text after the last khaṇḍa number: {padas[:2]}")
    if set(gloss) != set(done):
        sys.exit(f"khaṇḍas and glosses differ: {sorted(set(gloss) ^ set(done))}")
    # the opening colophon comes before the first khaṇḍa's heading
    first_head = next(i for i, s in enumerate(secs) if "heading" in s)
    pre = [s for s in secs[:first_head] if "colophon" in s]
    secs = pre + [s for s in secs if s not in pre]
    st = {"deity": "veda", "doc_title": f"Nirukta · Adhyāya {n}", "app_title": f"Nirukta {n}",
          "h1": f"Nirukta · Adhyāya {n}", "subtitle": SUBTITLE[n], "note": NOTE, "footer": FOOTER,
          "toc": True, "sections": secs}
    q = lambda v: repr(v) if isinstance(v, bool) else json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# Nirukta adhyāya {n}, from Sarup's 1927 edition (tools/nirukta/nirukta{n}.txt) → IAST;",
           "# written by tools/nirukta/gen_nirukta.py. See SOURCES §5.31.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"nirukta-{n}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(len(done), "khaṇḍas written")


if __name__ == "__main__":
    main(int(sys.argv[1]))
