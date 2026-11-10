# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Syllable counts of the Amarakośa e-text's half-verses (vargas.json from parse.py).

An anuṣṭubh half-verse has 16 syllables; anything else is a line the e-text
joined, split or set in another metre (the kośa has some āryās). Prints every
line that is not 16, so the pairing into ślokas can be checked by eye.
usage: metre.py DIR [K.V …]
"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
V = "अआइईउऊऋॠऌॡएऐओऔ"
M = "ािीुूृॄॢॣेैोौ"


def syl(s):
    s = re.sub(r"[^ऀ-ॿ]", "", s)
    n = 0
    for i, c in enumerate(s):
        if c in V:
            n += 1
        elif "क" <= c <= "ह" or c in "ळ":
            nxt = s[i + 1] if i + 1 < len(s) else ""
            if nxt != "्":
                n += 1                       # consonant with inherent a or a mātrā
    return n


if __name__ == "__main__":
    d = pathlib.Path(sys.argv[1])
    want = set(sys.argv[2:])
    for r in json.load(open(d / "vargas.json", encoding="utf-8")):
        key = f"{r['k']}.{r['v']}"
        if want and key not in want:
            continue
        for t, n in r["lines"]:
            c = syl(t)
            if c != 16:
                print(f"{key} {n:5d} [{c}] {t}")
