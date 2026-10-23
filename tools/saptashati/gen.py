# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write the Durgā Saptaśatī data files from the transcribed text files.

Input: tools/saptashati/text/*.txt (see ch01.txt for the format). Output, in
tools/stotras/: saptashati.py (contents), saptashati-purva.py (kavaca, argalā,
kīlaka), saptashati-NN.py (chapters 1–13) and saptashati-uttara.py (the three
rahasyas). Devanāgarī → IAST by the skill's dev2iast. Existing data files are
left alone unless --force is given.

usage: gen.py [--force]
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
from dev2iast import dev2iast  # noqa: E402

TEXT = HERE / "text"
OUT = TOOLS / "stotras"
TITLES = {
    "ch01": "Chapter 1 · Madhu and Kaiṭabha", "ch02": "Chapter 2 · Mahiṣāsura's armies",
    "ch03": "Chapter 3 · Mahiṣāsura slain", "ch04": "Chapter 4 · Śakra's hymn",
    "ch05": "Chapter 5 · the messenger", "ch06": "Chapter 6 · Dhūmralocana",
    "ch07": "Chapter 7 · Caṇḍa and Muṇḍa", "ch08": "Chapter 8 · Raktabīja",
    "ch09": "Chapter 9 · Niśumbha", "ch10": "Chapter 10 · Śumbha",
    "ch11": "Chapter 11 · Nārāyaṇī stuti", "ch12": "Chapter 12 · the Devī's promise",
    "ch13": "Chapter 13 · the boons to Suratha and Samādhi",
}
HEADS = {"प्रथमचरित्रम्": "Prathama carita · first episode", "मध्यमचरित्रम्": "Madhyama carita · middle episode",
         "उत्तमचरित्रम्": "Uttama carita · last episode", "देवीकवचम्": "Devī Kavaca",
         "अर्गलास्तोत्रम्": "Argalā Stotra", "कीलकस्तोत्रम्": "Kīlaka Stotra",
         "प्राधानिकरहस्यम्": "Prādhānika Rahasya", "वैकृतिकरहस्यम्": "Vaikṛtika Rahasya",
         "मूर्तिरहस्यम्": "Mūrti Rahasya"}
SOURCE = ("Source: Saptaśatī, Nirṇaya Sāgara Press, Bombay, Śaka 1839 (1917 CE), "
          "corrected by Vāsudeva Śarmā Paṇaśīkara (public domain; archive.org scan), "
          "transcribed from the page images; numbering as printed; translations original")
NOTE = ("The Durgā Saptaśatī (Devī Māhātmya) as printed by the Nirṇaya Sāgara Press in "
        "1917, in its seven hundred mantras: each chapter counts its uvāca, half-verse "
        "and verse mantras, and the numbers here are the print's. Translations will follow.")


def iast(line):
    t = dev2iast(re.sub(r"\s+", " ", line.replace("ॐ", "ओं")).strip())
    t = t.replace("॥", "||").replace("।", "|").replace("ऽ", "'")
    t = re.sub(r"\s*\|\|\s*", " || ", t)
    t = re.sub(r"(?<!\|)\s*\|(?!\|)\s*", " | ", t)
    return t.strip()


def sections(name):
    secs = []
    for line in (TEXT / f"{name}.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        tag, _, rest = line.partition(" ")
        if tag == "@H":
            secs.append({"heading": HEADS[rest.strip()]})
        elif tag in ("@V", "@P"):
            secs.append({"padas": [iast(rest)], "num": "", "gloss": "", "prose": True})
        elif tag == "@D":
            parts = [p.strip() for p in rest.split("|")][1:]
            padas = [iast(p) for p in parts]
            secs.append({"padas": padas, "num": "", "gloss": ""})
        elif tag == "@C":
            secs.append({"colophon": iast(rest).rstrip(" |") + (" ||" if not rest.rstrip().endswith("॥") else "")})
        else:
            n, *parts = [p.strip() for p in line.split("|")]
            padas = [iast(p) for p in parts]
            if n == "0":                                   # an unnumbered speaker line
                secs.append({"speaker": padas[0]}); continue
            padas = [p if i == len(padas) - 1 or p.endswith("|") else p + " |" for i, p in enumerate(padas)]
            secs.append({"padas": padas, "num": f"|| {n} ||", "gloss": ""})
    return secs


def q(s):
    return repr(s) if isinstance(s, bool) else json.dumps(s, ensure_ascii=False)


def write(slug, st, force):
    path = OUT / f"{slug}.py"
    if path.exists() and not force:
        return False
    secs = st.pop("sections")
    body = ["# -*- coding: utf-8 -*-",
            "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
            "# Durgā Saptaśatī, 1917 Nirṇaya Sāgara print → IAST; written by",
            "# tools/saptashati/gen.py from tools/saptashati/text. See SOURCES §5.26.",
            "", "STOTRA = {"]
    for k, v in st.items():
        body.append(f"    {q(k)}: {q(v) if not isinstance(v, list) else '[' + ', '.join('(' + ', '.join(q(x) for x in t) + ')' for t in v) + ']'},")
    body.append('    "sections": [')
    body += [f"    {s!r}," for s in secs]           # Python literals (True, not true)
    body += ["    ],", "}", ""]
    path.write_text("\n".join(body), encoding="utf-8", newline="\n")
    return True


def main(argv):
    force = "--force" in argv
    pages = ([("saptashati-purva", "Before the text · kavaca, argalā, kīlaka", ["a1_kavaca", "a2_argala", "a3_kilaka"])]
             + [(f"saptashati-{i:02d}", TITLES[f"ch{i:02d}"], [f"ch{i:02d}"]) for i in range(1, 14)]
             + [("saptashati-uttara", "After the text · the three rahasyas", ["b1_pradhanika", "b2_vaikrtika", "b3_murti"])])
    links, written = [], []
    for k, (slug, title, files) in enumerate(pages):
        nav = []
        if k:
            nav.append(("‹ previous", f"{pages[k - 1][0]}-iast.html"))
        nav.append(("contents", "saptashati-iast.html"))
        if k + 1 < len(pages):
            nav.append(("next ›", f"{pages[k + 1][0]}-iast.html"))
        secs = []
        for f in files:
            s = sections(f)
            if len(files) > 1 and secs:
                secs.append("ornament")
            secs += s
        n = sum(1 for s in secs if isinstance(s, dict) and s.get("num"))
        links.append((title, f"{slug}-iast.html", f"{n} mantras" if slug[-2:].isdigit() else f"{n} verses"))
        st = {"deity": "devi", "doc_title": f"Durgā Saptaśatī · {title}", "app_title": f"Saptaśatī · {title.split(' · ')[0]}",
              "h1": "Durgā Saptaśatī", "subtitle": title, "note": NOTE, "nav": nav,
              "toc": len(files) > 1 or any(isinstance(s, dict) and "heading" in s for s in secs),
              "footer": SOURCE, "sections": secs}
        if write(slug, st, force):
            written.append(slug)
    st = {"deity": "devi", "doc_title": "Durgā Saptaśatī", "app_title": "Durgā Saptaśatī",
          "h1": "Durgā Saptaśatī", "subtitle": "Devī Māhātmya · the seven hundred mantras",
          "note": NOTE, "footer": SOURCE, "sections": [{"links": links}]}
    if write("saptashati", st, force):
        written.append("saptashati")
    print(len(written), "data files written")


if __name__ == "__main__":
    main(sys.argv[1:])
