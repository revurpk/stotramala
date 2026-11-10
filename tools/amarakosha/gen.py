# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write the Amarakośa data files.

Input (in DIR): vargas.json from parse.py (the e-text with print1882.tsv's readings
applied), align.json and slokas.json from align.py / number.py (the 1882 print's
śloka division). Output, in tools/stotras/:

  amarakosha.py           contents of the whole work, by kāṇḍa
  amarakosha-K-VV.py      one varga a page, numbered as the 1882 print numbers it

A kṣepaka (a verse the print sets in quotation marks) is set a size smaller under a
rubric; so is a line the e-text has and the print lacks. Devanāgarī → IAST by the
skill's dev2iast. An existing data file is left alone unless --force is given.
usage: gen.py DIR [--force]
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
from dev2iast import dev2iast  # noqa: E402

OUT = TOOLS / "stotras"
# the print numbers the first kāṇḍa's closing verse on its own; it is shown at the end of the vārivarga
APPEND = {"1.11": "1.12"}
KANDA = {1: ("Svargādikāṇḍa", "the first kāṇḍa: heaven, sky, time, mind, speech, the underworld and the waters"),
         2: ("Bhūvargādikāṇḍa", "the second kāṇḍa: the earth, plants, animals and people"),
         3: ("Sāmānyakāṇḍa", "the third kāṇḍa: adjectives, words of several meanings, indeclinables and gender")}
# print varga: (Devanāgarī name for the closing line, IAST title, English)
VARGA = {
    "1.1": ("स्वर्गवर्गः", "Svargavarga", "heaven, the gods and their attendants — with the opening verses"),
    "1.2": ("व्योमवर्गः", "Vyomavarga", "the sky"),
    "1.3": ("दिग्वर्गः", "Digvarga", "the quarters, clouds, sun, moon and stars"),
    "1.4": ("कालवर्गः", "Kālavarga", "time"),
    "1.5": ("धीवर्गः", "Dhīvarga", "mind and understanding; tastes, smells, colours"),
    "1.6": ("शब्दादिवर्गः", "Śabdādivarga", "speech and sound"),
    "1.8": ("नाट्यवर्गः", "Nāṭyavarga", "music, dance and drama"),
    "1.9": ("पातालभोगिवर्गः", "Pātālabhogivarga", "the underworld and serpents"),
    "1.10": ("नरकवर्गः", "Narakavarga", "hell"),
    "1.11": ("वारिवर्गः", "Vārivarga", "waters, the sea and its creatures, lotuses — with the kāṇḍa's closing verse"),
    "2.1": ("भूमिवर्गः", "Bhūmivarga", "the earth and its lands"),
    "2.2": ("पुरवर्गः", "Puravarga", "towns and buildings"),
    "2.3": ("शैलवर्गः", "Śailavarga", "mountains"),
    "2.4": ("वनौषधिवर्गः", "Vanauṣadhivarga", "forests, trees and plants"),
    "2.5": ("सिंहादिवर्गः", "Siṃhādivarga", "beasts, birds and insects"),
    "2.6": ("मनुष्यवर्गः", "Manuṣyavarga", "people: kin, the body, dress and ornament"),
    "2.7": ("ब्रह्मवर्गः", "Brahmavarga", "brāhmaṇas, ritual and the stages of life"),
    "2.8": ("क्षत्रियवर्गः", "Kṣatriyavarga", "kings, statecraft and war"),
    "2.9": ("वैश्यवर्गः", "Vaiśyavarga", "trade, farming, cattle, measures and food"),
    "2.10": ("शूद्रवर्गः", "Śūdravarga", "crafts, the mixed castes and labour"),
    "3.1": ("विशेष्यनिघ्नवर्गः", "Viśeṣyanighnavarga", "adjectives, which take the gender of their noun"),
    "3.2": ("संकीर्णवर्गः", "Saṅkīrṇavarga", "miscellaneous words"),
    "3.3": ("नानार्थवर्गः", "Nānārthavarga", "words of several meanings, by final consonant — with the indeclinables of several meanings"),
    "3.5": ("अव्ययवर्गः", "Avyayavarga", "indeclinables"),
    "3.6": ("लिङ्गादिसंग्रहवर्गः", "Liṅgādisaṅgrahavarga", "the rules of gender"),
}
# headings inside a page where the print runs one e-text section into the next
HEADS = {(1, 0, 1): "Maṅgalācaraṇa · invocation", (1, 0, 3): "Prastāvanā · the plan of the work",
         (1, 0, 5): "Paribhāṣā · how the work marks gender", (1, 1, 11): "Svarga · heaven and the gods",
         (1, 7, 399): "Śabda · sound", (1, 12, 605): "Kāṇḍa-samāpti · the close of the first kāṇḍa",
         (2, 0, 1): "Vargabheda · the vargas of this kāṇḍa", (2, 1, 3): "Bhūmi · the earth",
         (3, 0, 1): "The vargas of this kāṇḍa", (3, 1, 3): "Paribhāṣā · adjectives",
         (3, 4, 856): "Nānārthāvyaya · indeclinables of several meanings"}
KS_RUBRIC = "kṣepaka — an added verse, in quotation marks in the 1882 print"
NIP_RUBRIC = "in the e-text only — not in the 1882 print"
NOTE = ("Amarasiṃha's Nāmaliṅgānuśāsana, the Amarakośa, in Sanskrit: the Sanskrit Wikisource text read against "
        "the 1882 Bombay print with Maheśvara's Amaraviveka, numbered as that print numbers it. Verses the print "
        "marks as later additions (kṣepaka) are set smaller. Translations will follow.")
FOOTER = ("Source: Sanskrit Wikisource — अमरकोशः (public domain), converted to IAST; structure, kṣepakas and "
          "readings from the 1882 print (ed. Thatte under Kielhorn, Bombay; archive.org), every change listed in "
          "SOURCES §5.29; translations original")
COLO = re.compile(r"^इत्यमरसिंहकृतौ")
COLO_GLOSS = {1: "Thus, in Amarasiṃha's Nāmaliṅgānuśāsana, the first kāṇḍa, beginning with heaven, is set out complete with its parts.",
              2: "Thus, in Amarasiṃha's Nāmaliṅgānuśāsana, the second kāṇḍa, beginning with the earth, is set out complete with its parts.",
              3: "Thus, in Amarasiṃha's Nāmaliṅgānuśāsana, the third, general kāṇḍa is set out complete with its parts."}


def iast(s):
    t = dev2iast(re.sub(r"\s+", " ", s).strip())
    t = t.replace("॥", "||").replace("।", "|").replace("ऽ", "'")
    return re.sub(r"\s+", " ", t).strip()


def slug(kv):
    k, v = kv.split(".")
    return f"amarakosha-{k}-{int(v):02d}"


def q(s):
    return repr(s) if isinstance(s, bool) else json.dumps(s, ensure_ascii=False)


def write(name, st, force):
    path = OUT / f"{name}.py"
    if path.exists() and not force:
        return False
    secs = st.pop("sections")
    body = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
            "# Amarakośa, Sanskrit Wikisource → IAST, structured and read against the 1882 print;",
            "# written by tools/amarakosha/gen.py. See SOURCES §5.29.", "", "STOTRA = {"]
    for k, v in st.items():
        body.append(f"    {q(k)}: {q(v) if not isinstance(v, list) else '[' + ', '.join('(' + ', '.join(q(x) for x in t) + ')' for t in v) + ']'},")
    body.append('    "sections": [')
    body += [f"    {s!r}," for s in secs]
    body += ["    ],", "}", ""]
    path.write_text("\n".join(body), encoding="utf-8", newline="\n")
    return True


def main(argv):
    d = pathlib.Path(argv[0]); force = "--force" in argv
    V = json.load(open(d / "vargas.json", encoding="utf-8"))
    A = json.load(open(d / "align.json", encoding="utf-8"))
    S = json.load(open(d / "slokas.json", encoding="utf-8"))
    text = {(r["k"], r["v"], float(n)): t for r in V for t, n in r["lines"]}
    marks = {(r["k"], r["v"], float(n)): m for r in V for n, m in r["marks"].items()}
    missing = [(a["k"], a["v"], a["n"]) for a in A if (a["k"], a["v"], float(a["n"])) not in text]
    if missing:
        sys.exit(f"align.json is stale: {len(missing)} lines not in vargas.json (rerun align.py, number.py): {missing[:3]}")
    nips = set()                                    # lines the print lacks (print1882.tsv, op nip)
    for l in (HERE / "print1882.tsv").read_text(encoding="utf-8").splitlines():
        f = l.split("	")
        if len(f) > 2 and not l.startswith("#") and f[2] == "nip":
            k_, v_ = map(int, f[0].split(".")); a_, _, b_ = f[1].partition("-")
            nips |= {(k_, v_, float(x)) for x in range(int(a_), int(b_ or a_) + 1)}
    keys = list(VARGA)
    written, contents = 0, {1: [], 2: [], 3: []}
    for i, kv in enumerate(keys):
        k = int(kv.split(".")[0])
        secs, nsl, nks, colophon = [], 0, 0, None
        for g in S[kv] + S.get(APPEND.get(kv, ""), []):
            lines = [A[j] for j in g["lines"]]
            keyof = lambda a: (a["k"], a["v"], float(a["n"]))
            first = lines[0]
            h = HEADS.get((first["k"], first["v"], int(float(first["n"]))))
            if h and float(first["n"]) == int(float(first["n"])):
                secs.append({"heading": h})
            devs = [text[keyof(a)] for a in lines]
            if COLO.match(devs[0]):
                colophon = iast(" ".join(devs)) + " ||"
                continue
            padas = [iast(t) for t in devs]
            padas = [p + (" |" if j < len(padas) - 1 else "") for j, p in enumerate(padas)]
            if g["ks"]:
                nip = any(keyof(a) in nips for a in lines)
                rub = NIP_RUBRIC if nip else KS_RUBRIC
                if nip and len(secs) >= 2 and secs[-2] == {"rubric": rub} and secs[-1].get("prose"):
                    prev = secs[-1]["padas"]                   # a run of such lines: one passage
                    prev[-1] = prev[-1] + " |"
                    prev += padas
                else:
                    secs.append({"rubric": rub})
                    secs.append({"padas": padas, "num": "", "gloss": "", "prose": True})
                    nks += 0 if nip else 1
            else:
                nsl += kv in S and g in S[kv]
                secs.append({"padas": padas, "num": f"|| {g['n']} ||", "gloss": ""})
            for a in lines:
                if keyof(a) in marks:
                    secs.append({"colophon": iast(marks[keyof(a)]) + " ||"})
        dev, title, eng = VARGA[kv]
        secs.append({"colophon": iast("इति " + dev) + " ||"})
        if colophon:
            secs += ["ornament", {"colophon": colophon, "gloss": COLO_GLOSS[k]}]
        nav = ([("‹ " + VARGA[keys[i - 1]][1], slug(keys[i - 1]) + "-iast.html")] if i else []) \
            + [("all vargas", "amarakosha-iast.html")] \
            + ([(VARGA[keys[i + 1]][1] + " ›", slug(keys[i + 1]) + "-iast.html")] if i + 1 < len(keys) else [])
        st = {"deity": "amarakosha", "doc_title": f"Amarakośa · {title}", "app_title": f"Amarakośa · {title}",
              "h1": "Amarakośa", "subtitle": f"{KANDA[k][0]} · {title} — {eng}",
              "note": NOTE, "nav": nav, "footer": FOOTER, "sections": secs}
        written += write(slug(kv), st, force)
        contents[k].append((title, slug(kv) + "-iast.html", f"{eng} · {nsl} ślokas" + (f", {nks} kṣepaka" if nks else "")))
    secs = []
    for k in (1, 2, 3):
        secs += [{"heading": f"{KANDA[k][0]} · {KANDA[k][1]}"}, {"links": contents[k]}]
    st = {"deity": "amarakosha", "doc_title": "Amarakośa", "app_title": "Amarakośa", "h1": "Amarakośa",
          "subtitle": "Nāmaliṅgānuśāsana of Amarasiṃha · three kāṇḍas, twenty-five vargas",
          "note": NOTE, "footer": FOOTER, "sections": secs}
    written += write("amarakosha", st, force)
    print(written, "data files written")


if __name__ == "__main__":
    main(sys.argv[1:])
