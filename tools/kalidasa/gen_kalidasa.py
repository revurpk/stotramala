# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/<slug>.py for the Kālidāsa-attributed pages from tools/kalidasa/<name>.dev.txt
(Devanāgarī, verses separated by a blank line, or by a line "@" for the daṇḍaka's paragraphs)
and <name>.gloss.txt (key | English; key = the unit's number from 1).   usage: gen_kalidasa.py NAME|all"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
import dev2iast as D  # noqa: E402
META = {
 "syamala": dict(slug="syamala-dandakam", deity="devi", t="Śyāmalā Daṇḍakam", app="Śyāmalā Daṇḍakam",
     sub="The Hymn to Śyāmalā (Mātaṅgī) · attributed to Kālidāsa", prose=True,
     note="A daṇḍaka — a hymn of long, unmetred, rhyming epithets — to Śyāmalā, the dark goddess Mātaṅgī, patron of music and speech, traditionally ascribed to the poet Kālidāsa. It opens with two verses, then five long invocations, and closes with a verse. The Sanskrit text of the 1929 Kāvyamālā print is damaged in places and has been repaired (see SOURCES §10.1); please read it with that in mind."),
 "ambashtaka": dict(slug="ambashtakam", deity="devi", t="Ambāṣṭakam", app="Ambāṣṭakam",
     sub="Eight Verses to the Mother · in the Aśvadhāṭī metre",
     note="Eight verses to Pārvatī, Kālī and the Mother of the worlds in the swift, galloping Aśvadhāṭī metre (the name means ‘a horse’s gallop’), famous for its rhymes. The Kāvyamālā print, from which the text is taken, gives it to Śaṅkarācārya; the tradition that calls it Kālidāsa’s Aśvadhāṭī stotra is also current."),
 "shringaratilaka": dict(slug="shringaratilakam", deity="kavya", t="Śṛṅgāratilakam", app="Śṛṅgāratilaka",
     sub="The Ornament of Love · attributed to Kālidāsa",
     note="A short collection of love-verses, in the voices of lovers, friends and a woman left alone, attributed to Kālidāsa; the text of this printing is in places corrupt. The verse numbers are those of the print (the numbering here is by order, 1–31)."),
}
def iast(line): return re.sub(r"\s+", " ", D.dev2iast(line.replace("ऽ", "'")).replace("॥", "||").replace("।", "|")).strip()
def units(name):
    txt = (HERE / f"{name}.dev.txt").read_text(encoding="utf-8")
    if "\n@\n" in txt: blocks = txt.split("\n@\n")
    else: blocks = re.split(r"\n\s*\n", txt.strip())
    out = []
    for b in blocks:
        lines = [l.strip() for l in b.strip().split("\n") if l.strip()]
        out.append(lines)
    return out
def main(name):
    m = META[name]
    us = units(name)
    gl = {}
    gp = HERE / f"{name}.gloss.txt"
    if gp.exists():
        for l in gp.read_text(encoding="utf-8").splitlines():
            if l.strip() and l[0] != "#":
                k, e = [x.strip() for x in l.split("|", 1)]; gl[k] = e
    secs, missing = [], 0
    for i, lines in enumerate(us, 1):
        last = lines[-1]
        mm = re.search(r"[।॥]+\s*([०-९0-9]*)\s*[।॥]*\s*$", last)
        num = ""
        if mm and mm.group(1):
            num = "|| " + str(int("".join(str("०१२३४५६७८९".index(c)) if c in "०१२३४५६७८९" else c for c in mm.group(1)))) + " ||"
        body = [re.sub(r"\s*[।॥]+\s*[०-९0-9]*\s*[।॥]*\s*$", "", l) for l in lines[:-1]] + [re.sub(r"\s*[।॥]+\s*[०-९0-9]*\s*[।॥]*\s*$", "", last)]
        if m.get("prose") and len(lines) == 1 and len(last) > 200:
            pad = [iast(body[0])]
            d = {"padas": pad, "num": num, "gloss": gl.get(str(i), "(translation to follow)"), "prose": True}
        else:
            ip = [iast(l) for l in body]
            if m.get("prose"):
                pad = [ip[0] + " |", ip[1]] if len(ip) == 2 else ip
            else:
                pad = [ip[0], ip[1] + " |", ip[2], ip[3]] if len(ip) == 4 else ([ip[0] + " |", ip[1]] if len(ip) == 2 else ip)
            d = {"padas": pad, "num": "" if m.get("prose") and not num else num, "gloss": gl.get(str(i), "(translation to follow)")}
        if str(i) not in gl: missing += 1
        secs.append(d)
    if not m.get("prose"):
        for i, d in enumerate(secs, 1):
            if not d["num"]: d["num"] = f"|| {i} ||"
    st = {"deity": m["deity"], "doc_title": m["t"], "app_title": m["app"], "h1": m["t"], "subtitle": m["sub"], "note": m["note"],
          "footer": "Source: Sanskrit Wikisource — " + {"syamala": "श्यामलादण्डकम् (Kāvyamālā, part 1, 1929)", "ambashtaka": "अम्बाष्टकम् (Kāvyamālā, part 2)", "shringaratilaka": "शृङ्गारतिलकम् (Ṛtusaṃhāra edition, 1910)"}[name] + " (public domain); English translation original; editorial notes in SOURCES §10",
          "sections": secs}
    q = lambda v: json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# {m['t']}; written by tools/kalidasa/gen_kalidasa.py from tools/kalidasa/{name}.dev.txt and .gloss.txt. See SOURCES §10.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"{m['slug']}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{m['slug']}: {len(secs)} units, {missing} without a translation")
if __name__ == "__main__":
    for n in (META if sys.argv[1] == "all" else [sys.argv[1]]): main(n)
