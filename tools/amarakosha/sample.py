# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Sample collation helper: for a leaf of the 1882 print, list the e-text half-verses
(with every print1882.tsv reading applied) that the alignment places on it, to be read
against the page image. With no leaf, pick the middle leaf of each print varga.
usage: sample.py DIR [LEAF]
"""
import collections, json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
d = pathlib.Path(sys.argv[1])
A = json.load(open(d / "align.json", encoding="utf-8"))
V = {(r["k"], r["v"], float(n)): t for r in json.load(open(d / "vargas.json", encoding="utf-8")) for t, n in r["lines"]}
MERGE = {"1.0": "1.1", "1.7": "1.6", "2.0": "2.1", "3.0": "3.1", "3.4": "3.3"}
if len(sys.argv) > 2:
    leaf = int(sys.argv[2])
    for r in A:
        if r.get("leaf") == leaf:
            print(f"{r['k']}.{r['v']}.{r['n']}  {V.get((r['k'], r['v'], float(r['n'])), '(dropped)')}")
else:
    leaves = collections.defaultdict(list)
    for r in A:
        if r.get("leaf") is not None:
            kv = f"{r['k']}.{r['v']}"
            leaves[MERGE.get(kv, kv)].append(r["leaf"])
    print(" ".join(f"{kv}:{sorted(set(l))[len(set(l)) // 2]}" for kv, l in leaves.items()))
