# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Draft tools/stories/jatakamala.src.txt from scratch/pt/jataka.txt (Sanskrit Wikisource, Āryaśūra's Jātakamālā, SOURCES §11)."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[2]
L = (ROOT / "scratch" / "pt" / "jataka.txt").read_text(encoding="utf-8").replace("�", "").split("\n")
TAG = re.compile(r"॥\s*ज्म्_([०-९0-9]+)\.([०-९0-9]+)\s*॥\s*$")
def clean(l):
    l = re.sub(r"\(वैद्य\s*[०-९0-9]+\)", "", l)
    l = re.sub(r"<[^>]+>", "", l)
    l = l.replace("[", "").replace("]", "")
    l = TAG.sub(lambda m: "॥ " + m.group(1) + "." + m.group(2) + " ॥", l)
    return re.sub(r"\s+", " ", l).strip()
MARK = re.compile(r"॥\s*[०-९0-9.]+\s*॥\s*$")
def story(title, a, b):
    ls = [clean(l) for l in L[a - 1:b]]
    ls = [l for l in ls if l and not l.startswith("____")]
    out, i = [], 0
    while i < len(ls):
        l = ls[i]
        if MARK.search(l):
            # verse: pull preceding short non-marker lines already in out
            grp = [l]
            if (out and len(out[-1]) == 1 and len(out[-1][0]) < 130 and not MARK.search(out[-1][0])
                    and not re.search(r"[-,?:]$", out[-1][0]) and not out[-1][0].startswith(("इति", "तत्", "अथ", "अपि"))):
                grp.insert(0, out.pop()[0])
            out.append(grp)
        else:
            out.append([l])
        i += 1
    return "# " + title + "\n\n" + "\n\n".join("\n".join(u) for u in out) + "\n"
SPECS = [("The Hare | शशजातकम्", 656, 810), ("The Fish and the Rain | मत्स्यजातकम्", 2291, 2362),
         ("The Quail Chick and the Fire | वर्तकापीतकजातकम्", 2366, 2414)]
if __name__ == "__main__":
    sys.stdout.write("\n".join(story(*s) for s in SPECS))
