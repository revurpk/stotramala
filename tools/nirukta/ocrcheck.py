# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Compare a Nirukta transcription (niruktaN.txt) with Tesseract's reading of the same
leaves (OCRDIR/mN.txt from ocrmain.sh) and print, leaf by leaf, the words the OCR does not
support, for a second look at the page image. A paragraph is filed under the leaf it
starts on and may run onto the next, so each leaf is checked against its own OCR and the
next leaf's.
usage: ocrcheck.py niruktaN.txt OCRDIR [--cutoff 0.6]
"""
import difflib, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")

a = sys.argv[1:]
cut = float(a[a.index("--cutoff") + 1]) if "--cutoff" in a else 0.6
WORD = r"[ऀ-ॣॲ-ॿ]+"
norm = lambda w: re.sub(r"[॒॑]", "", w).replace("ं", "म्").replace("ऽ", "")

text, cur = {}, None
for raw in open(a[0], encoding="utf-8"):
    if raw.startswith("@"):
        cur = int(raw[1:]); continue
    if cur and not raw.startswith("#"):
        text.setdefault(cur, []).append(raw)


def ocr(n):
    f = pathlib.Path(a[1]) / f"m{n}.txt"
    return {norm(w) for w in re.findall(WORD, f.read_text(encoding="utf-8"))} if f.exists() else set()


total = weak = 0
for leaf, ls in sorted(text.items()):
    seen = ocr(leaf) | ocr(leaf + 1)
    miss = []
    for w in re.findall(WORD, " ".join(ls)):
        k = norm(w)
        if len(k) < 3 or k in seen:
            continue
        total += 1
        best = difflib.get_close_matches(k, seen, n=1, cutoff=0.0)
        r = difflib.SequenceMatcher(None, k, best[0]).ratio() if best else 0
        if r < cut:
            miss.append(f"{w}({best[0] if best else '-'})")
    weak += len(miss)
    if miss:
        print(f"leaf {leaf}: {len(miss)} weakly supported: {' '.join(miss)}")
print(f"{weak} weakly supported words")
