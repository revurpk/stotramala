# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/<slug>.py for the name-lists from tools/nama/<name>.dev.txt (Devanāgarī; units separated by a
blank line; a unit ending  ॥ N ॥ or ॥ ध्यानम् ॥ is a verse, otherwise prose) and <name>.gloss.txt (key | English |;
key = the unit's number from 1).   usage: gen_nama.py NAME|all"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
import dev2iast as D  # noqa: E402
SRC = "Sanskrit Wikisource — बृहत्स्तोत्ररत्नाकरः, भागः १ (1953), pp. {pp} (public domain); English translation original; editorial notes in SOURCES §12"
META = {
 "subrahmanya108": dict(slug="subrahmanya-ashtottara-shatanama-stotram", deity="subrahmanya", t="Subrahmaṇya Aṣṭottaraśatanāmastotram",
     app="Subrahmaṇya 108 Names", sub="The One Hundred and Eight Names of Subrahmaṇya, in verse",
     note="One hundred and eight names of Subrahmaṇya (Skanda, Kārttikeya) set in anuṣṭubh verses, so that they can be recited as a hymn or taken singly. The text is a nāma-stotra in verse (not a ‘namaḥ’ list); the source does not number the names, and a few verse-numbers in it are missing or run together (see SOURCES §12).",
     foot=SRC.format(pp="96–97")),
 "ganesha16": dict(slug="ganesha-shodashanama-stotram", deity="ganesha", t="Gaṇeśa Ṣoḍaśanāmastotram", app="Gaṇeśa 16 Names", sub="The Sixteen Names of Gaṇeśa",
     note="The sixteen names of Gaṇeśa, in two verses, with the verses on the occasions for reciting them. This text is the traditional one, written from memory and not collated with a printed edition (see SOURCES §12.2).",
     foot="Text: traditional, written from memory of the standard verses and not collated with a printed edition; English translation original; editorial notes in SOURCES §12.2"),
 "subrahmanya16": dict(slug="subrahmanya-shodashanama-stotram", deity="subrahmanya", t="Subrahmaṇya Ṣoḍaśanāmastotram",
     app="Subrahmaṇya 16 Names", sub="The Sixteen Names of Subrahmaṇya",
     note="The sixteen names of Subrahmaṇya, given in order (‘the first is…, the second is…’), with a meditation verse and the benefits of reciting them.",
     foot=SRC.format(pp="136–137")),
}
def iast(line): return re.sub(r"\s+", " ", D.dev2iast(line.replace("ऽ", "'")).replace("॥", "||").replace("।", "|")).strip()
MARK = re.compile(r"॥\s*([०-९0-9]+|ध्यानम्)\s*॥\s*$")
def an(x): return "".join(str("०१२३४५६७८९".index(c)) if c in "०१२३४५६७८९" else c for c in x)
def main(name):
    m = META[name]
    txt = (HERE / f"{name}.dev.txt").read_text(encoding="utf-8")
    gl = {}
    gp = HERE / f"{name}.gloss.txt"
    for l in gp.read_text(encoding="utf-8").splitlines():
        if l.strip() and l[0] != "#":
            k, e = [x.strip() for x in l.split("|", 1)]; gl[k] = e.rstrip("|").strip()
    secs, missing = [], 0
    for i, blk in enumerate(re.split(r"\n\s*\n", txt.strip()), 1):
        lines = [l.strip() for l in blk.strip().split("\n") if l.strip()]
        mm = MARK.search(lines[-1])
        if mm:
            body = [MARK.sub("", l).rstrip() for l in lines]
            pad = [iast(l) for l in body]
            if len(pad) == 2: pad[0] = pad[0].rstrip("|").strip() + " |"
            d = {"padas": pad, "num": "" if mm.group(1) == "ध्यानम्" else f"|| {an(mm.group(1))} ||"}
            if mm.group(1) == "ध्यानम्": d["padas"][-1] += " (dhyānam)"
        else:
            d = {"padas": [iast(" ".join(lines))], "num": "", "prose": True}
        d["gloss"] = gl.get(str(i), "(translation to follow)")
        if str(i) not in gl: missing += 1
        secs.append(d)
    st = {"deity": m["deity"], "doc_title": m["t"], "app_title": m["app"], "h1": m["t"], "subtitle": m["sub"], "note": m["note"],
          "footer": m["foot"], "sections": secs}
    q = lambda v: json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# {m['t']}; written by tools/nama/gen_nama.py from tools/nama/{name}.dev.txt and .gloss.txt. See SOURCES §12.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"{m['slug']}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{m['slug']}: {len(secs)} units, {missing} without a translation")
if __name__ == "__main__":
    for n in (list(META) if sys.argv[1] == "all" else sys.argv[1:]): main(n)
