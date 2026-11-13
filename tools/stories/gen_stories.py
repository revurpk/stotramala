# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/<slug>.py for the story pages from tools/stories/<name>.src.txt
(Devanāgarī; "# English title | Sanskrit title" opens a story; units separated by blank lines; a unit whose
last line ends  ॥ N ॥  is a verse, anything else prose) and <name>.gloss*.txt (key | English |;
key = story number, a dot, the unit's number within that story, both from 1).   usage: gen_stories.py NAME|all"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
import dev2iast as D  # noqa: E402
META = {
 "pancatantra": dict(slug="pancatantra-tales", deity="katha", t="Pañcatantra · Selected Tales", app="Pañcatantra",
     sub="Six tales of Viṣṇuśarman’s book of worldly wisdom · Sanskrit with English",
     note="The Pañcatantra (‘five books’) is the great Sanskrit book of animal fables, told to teach statecraft and prudence to three dull princes. Here are six of its tales, in the Sanskrit of the Wikisource text, each with its verses and an English rendering. Some tales are told inside the frame story, and the closing line of each (‘so I say…’) points back to the saying that the tale illustrates; the wording follows the text as transcribed (see SOURCES §11).",
     foot="Sanskrit Wikisource — पञ्चतन्त्रम् (Viṣṇuśarman)"),
 "jatakamala": dict(slug="jatakamala-tales", deity="katha", t="Jātakamālā · Selected Tales", app="Jātakamālā",
     sub="Three birth-stories of the Bodhisattva by Āryaśūra · Sanskrit with English",
     note="Āryaśūra’s Jātakamālā (‘garland of birth-stories’, 4th century or so) retells in ornate Sanskrit, in mixed prose and verse, tales of the Buddha’s earlier lives as the Bodhisattva. Three are given here: the hare who offered himself, the fish who prayed for rain, and the quail chick who stopped a forest fire by an act of truth.",
     foot="Sanskrit Wikisource — जातकमाला (आर्यशूरः)"),
}
def iast(line): return re.sub(r"\s+", " ", D.dev2iast(line.replace("ऽ", "'")).replace("॥", "||").replace("।", "|")).strip()
MARK = re.compile(r"॥\s*([०-९0-9]+(?:\.[०-९0-9]+)?)\s*॥\s*$")
def ascii_num(x): return "".join(str("०१२३४५६७८९".index(c)) if c in "०१२३४५६७८९" else c for c in x)
def main(name):
    m = META[name]
    txt = (HERE / f"{name}.src.txt").read_text(encoding="utf-8")
    gl = {}
    for gp in sorted(HERE.glob(f"{name}.gloss*.txt")):
        for l in gp.read_text(encoding="utf-8").splitlines():
            if l.strip() and l[0] != "#":
                k, e = [x.strip() for x in l.split("|", 1)]; gl[k] = e.rstrip("|").strip()
    secs, missing, story, n = [], 0, 0, 0
    for blk in re.split(r"\n\s*\n", txt.strip()):
        lines = [l.strip() for l in blk.strip().split("\n") if l.strip()]
        if lines[0].startswith("# "):
            en, sa = [x.strip() for x in lines[0][2:].split("|")]
            story += 1; n = 0
            secs.append({"heading": f"{story}. {en} — {iast(sa)}"})
            continue
        n += 1
        mm = MARK.search(lines[-1])
        key = f"{story}.{n}"
        if mm:
            body = [MARK.sub("", l).rstrip() for l in lines]
            if len(body) == 1:
                parts = re.split(r"\s*।\s*", body[0].rstrip("।").strip())
                if len(parts) == 2: body = [parts[0] + " ।", parts[1]]
            pad = [iast(l) for l in body]
            if len(pad) == 2: pad[0] = pad[0].rstrip("|").strip() + " |"
            d = {"padas": pad, "num": f"|| {ascii_num(mm.group(1))} ||"}
        else:
            d = {"padas": [iast(" ".join(lines))], "num": "", "prose": True}
        d["gloss"] = gl.get(key, "(translation to follow)")
        if key not in gl: missing += 1
        secs.append(d)
    st = {"deity": m["deity"], "doc_title": m["t"], "app_title": m["app"], "h1": m["t"], "subtitle": m["sub"], "note": m["note"], "toc": True,
          "footer": "Source: " + m["foot"] + " (public domain); English translation original; editorial notes in SOURCES §11",
          "sections": secs}
    q = lambda v: json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# {m['t']}; written by tools/stories/gen_stories.py from tools/stories/{name}.src.txt and .gloss*.txt. See SOURCES §11.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {v!r}," if isinstance(v, bool) else f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"{m['slug']}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{m['slug']}: {story} stories, {missing} units without a translation")
if __name__ == "__main__":
    for nm in (list(META) if sys.argv[1] == "all" else sys.argv[1:]): main(nm)
