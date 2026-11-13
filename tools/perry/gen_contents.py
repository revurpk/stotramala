# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/perry.py, the contents page of the Learn lessons: one line for each
lesson that exists (tools/perry/lessonNN.txt), with the subtitle (its "% …" line) under it.
Run after each new lesson (scratch/perry/run.sh does).  usage: gen_contents.py"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(HERE))
from gen_perry import ROMAN, TITLES  # noqa: E402


def main():
    links, last = [], 0
    if (HERE / "intro.txt").exists():
        m = re.search(r"^%\s*(.+)$", (HERE / "intro.txt").read_text(encoding="utf-8"), re.M)
        links.append(("Introduction (§§ 1–91)", "perry-intro-iast.html", m.group(1).strip() if m else ""))
    for f in sorted(HERE.glob("lesson[0-9][0-9].txt")):
        nn = int(f.stem[6:])
        m = re.search(r"^%\s*(.+)$", f.read_text(encoding="utf-8"), re.M)
        links.append((f"Lesson {ROMAN[nn]}", f"perry-{nn:02d}-iast.html", m.group(1).strip() if m else TITLES.get(nn, "")))
        last = nn
    for name, label, href in (("gloss1", "Glossary I", "perry-gloss-1-iast.html"), ("gloss2", "Glossary II", "perry-gloss-2-iast.html"),
                              ("appendix", "Appendix and Corrections", "perry-appendix-iast.html")):
        if (HERE / f"{name}.txt").exists():
            m = re.search(r"^%\s*(.+)$", (HERE / f"{name}.txt").read_text(encoding="utf-8"), re.M)
            links.append((label, href, m.group(1).strip() if m else ""))
    st = {"deity": "learn", "doc_title": "A Sanskrit Primer", "app_title": "Sanskrit Primer",
          "h1": "A Sanskrit Primer", "subtitle": f"E. D. Perry, after Bühler · the whole book: introduction, lessons I–{ROMAN[last]}, glossaries, appendix",
          "note": ("Edward Delavan Perry’s graded course (1885): each lesson has its rules, a vocabulary and "
                   "exercises, with Telugu meanings and English and Telugu translations and answers folded "
                   "under each sentence. Open any lesson to read it in Devanāgarī, Telugu or IAST."),
          "footer": ("Source: Edward Delavan Perry, A Sanskrit Primer, based on the Leitfaden für den "
                     "Elementarcursus des Sanskrit of Georg Bühler (Ginn & Co., 1885; public domain); "
                     "editorial notes in SOURCES §8.1"),
          "sections": [{"rubric": "The book in order: the introduction (§§ 1–91), the 45 lessons, the two glossaries to the exercises, and the appendix with Perry’s corrections."},
                       {"links": links}]}
    q = lambda v: repr(v) if isinstance(v, bool) else json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           "# Contents of the Learn lessons (Perry); written by tools/perry/gen_contents.py.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in st["sections"]] + ["    ],", "}", ""]
    (TOOLS / "stotras" / "perry.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"perry contents: {len(links)} lessons")


if __name__ == "__main__":
    main()
