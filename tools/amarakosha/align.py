# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Align the e-text's half-verses (vargas.json) with the 1882 print's mūla lines
(mula.json from ocr.py), so each half-verse learns its leaf, the print's śloka
number (the ॥ N ॥ that closes the print's second half) and whether the print sets
it in quotation marks or brackets (a kṣepaka).

Banded global alignment; a pair scores its similarity on a normalised skeleton
(class nasal → anusvāra, no spaces or punctuation), less 0.45, so only a real
match pays. Writes align.json [{"k","v","n","text","ocr","leaf","sim","num","q"}].
usage: align.py DIR (holding vargas.json and ia/mula.json)
"""
import difflib, json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
LAST = 375                                   # leaves from here on are the word index
DIG = str.maketrans("०१२३४५६७८९", "0123456789")
CONS = "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळ"


def skel(s):
    s = s.replace("‍", "").replace("‌", "").replace("़", "").replace("ँ", "ं").replace("ळ", "ल")
    s = re.sub(r"[ङञणनम]्(?=[" + CONS + "])", "ं", s)
    s = re.sub(r"[^ऀ-ॣ]", "", s)            # letters only: no danda, digits, spaces
    return s.replace("ऽ", "")


def num(s):
    m = re.search(r"[॥|]{1,2}\s*([०-९0-9]{1,3})\s*[॥|]{0,2}\s*[\)\]”\"]*\s*(?:\([०-९0-9]\))?\s*$", s)
    return int(m.group(1).translate(DIG)) if m else None


def main(d):
    d = pathlib.Path(d)
    E = [{"k": r["k"], "v": r["v"], "n": n, "text": t} for r in json.load(open(d / "vargas.json", encoding="utf-8"))
         for t, n in r["lines"]]
    O = [o for o in json.load(open(d / "ia" / "mula.json", encoding="utf-8")) if o["leaf"] < LAST]
    es, os_ = [skel(e["text"]) for e in E], [skel(o["text"]) for o in O]
    n, m, band = len(E), len(O), 220
    NEG = -1e9
    S = [dict() for _ in range(n + 1)]
    B = [dict() for _ in range(n + 1)]
    S[0][0] = 0.0
    for j in range(1, band + 1):
        S[0][j], B[0][j] = 0.0, "o"
    for i in range(1, n + 1):
        c = round(i * m / n)
        for j in range(max(0, c - band), min(m, c + band) + 1):
            best, bk = S[i - 1].get(j, NEG), "e"               # e-line without a print line
            v = S[i].get(j - 1, NEG)
            if v > best:
                best, bk = v, "o"                               # print line without an e-line
            if j:
                p = S[i - 1].get(j - 1, NEG)
                if p > NEG:
                    sm = difflib.SequenceMatcher(None, es[i - 1], os_[j - 1], autojunk=False)
                    r = sm.ratio() if sm.real_quick_ratio() > 0.45 else 0.0
                    if p + r - 0.45 > best:
                        best, bk = p + r - 0.45, "m"
            S[i][j], B[i][j] = best, bk
    j = max(S[n], key=S[n].get)
    i, pairs = n, {}
    while i > 0 or j > 0:
        bk = B[i].get(j, "o" if i == 0 else "e")
        if bk == "m":
            pairs[i - 1] = j - 1; i -= 1; j -= 1
        elif bk == "e":
            i -= 1
        else:
            j -= 1
    out = []
    for i, e in enumerate(E):
        rec = dict(e)
        if i in pairs:
            o = O[pairs[i]]
            rec.update(ocr=o["text"], leaf=o["leaf"], oi=pairs[i],
                       sim=round(difflib.SequenceMatcher(None, es[i], os_[pairs[i]], autojunk=False).ratio(), 2),
                       num=num(o["text"]), q=bool(re.search(r"[“”\"(\[]", o["text"])))
        out.append(rec)
    json.dump(out, open(d / "align.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    got = [r for r in out if "ocr" in r]
    print(f"{len(got)}/{len(out)} half-verses matched; {sum(r['sim'] < 0.6 for r in got)} weak (<0.6)")
    used = set(pairs.values())
    extra = [o for k, o in enumerate(O) if k not in used]
    print(len(extra), "print lines (before the index) unmatched")
    json.dump(extra, open(d / "unmatched.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main(sys.argv[1])
