# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Self-check of the Nighaṇṭu transcription (nighantu.txt).

1. Each khaṇḍa's closing bracket states how many words it holds (गोत्रेत्येकविंशतिः …);
   count the words of the list and compare.
2. Compare each leaf's transcription with Tesseract's reading of the same leaf
   (OCRDIR/nN.txt from ocr.sh) and print the words the OCR does not support, for a
   second look at the page image.
usage: check.py nighantu.txt [OCRDIR]
"""
import difflib, re, sys
sys.stdout.reconfigure(encoding="utf-8")

NUM = {"द्वौ": 2, "त्रीणि": 3, "त्रयः": 3, "चत्वार": 4, "चत्वारः": 4, "चत्वारि": 4, "पञ्च": 5, "षट्": 6, "षळ": 6,
       "सप्त": 7, "अष्ट": 8, "अष्टौ": 8, "नव": 9, "दश": 10, "एकादश": 11, "द्वादश": 12, "त्रयोदश": 13,
       "चतुर्दश": 14, "पञ्चदश": 15, "षोडश": 16, "सप्तदश": 17, "अष्टादश": 18}
TENS = {"विंशति": 20, "त्रिंश": 30, "चत्वारिंश": 40, "पञ्चाश": 50, "पंचाश": 50, "षष्टि": 60, "सप्तति": 70,
        "अशीति": 80, "नवति": 90}
# a unit before a tens word, also in sandhi (इत्येक-, इत्यष्टा-: the vowel is a mātrā there)
PRE = {"एक": 1, "ेक": 1, "द्वा": 2, "द्वि": 2, "त्रयो": 3, "त्रयस्": 3, "त्रि": 3, "चतु": 4, "चतुर्": 4, "पञ्च": 5,
       "पंच": 5, "षड्": 6, "षट्": 6, "षड": 6, "सप्त": 7, "अष्टा": 8, "ष्टा": 8, "नव": 9}


def number(text):
    """The count a bracket states: षड्विंशतिः → 26, द्वाविंशशतं → 122, चतुरुत्तरमशीतिः → 84."""
    t = text.replace(" ", "")
    hundred = 100 if re.search(r"शत(?:ं|म्)?(?:पदानि|गति|$)|च्छतं|शशतं|शतमुदक|एकशत", t) else 0
    if "चतुरुत्तरमशीति" in t:
        return 84
    for w, v in sorted(TENS.items(), key=lambda x: -len(x[0])):
        i = t.find(w)
        if i >= 0:
            head = t[:i]
            u = next((pv for p, pv in sorted(PRE.items(), key=lambda x: -len(x[0])) if head.endswith(p)), 0)
            return hundred + v + u
    if hundred and re.search(r"(?:^|[^ा-ौ])एकशत", t):
        return 101
    for w, v in sorted(NUM.items(), key=lambda x: -len(x[0])):
        if re.search(r"(?:^|ति|इति|\[)" + w, t) or t.startswith(w):
            return v
    return None


def khandas(path):
    leaf = None
    for raw in open(path, encoding="utf-8"):
        l = raw.rstrip("\n")
        if l.startswith("@"):
            leaf = int(l[1:]); continue
        m = re.search(r"॥\s*([०-९]+)\s*॥\s*$", l)
        if m:
            yield leaf, l


def main(argv):
    bad = 0
    for leaf, l in khandas(argv[0]):
        body = re.sub(r"॥.*$", "", l)
        stated = re.findall(r"\[([^\]]*)\]", body)
        listpart = re.sub(r"\[[^\]]*\]", "", body)
        words = [w for w in listpart.split("।") if w.strip()]
        n = len(words)
        # the last item carries "…इति X"; an आदिष्टोपयोजन list or the upamās have no bracketed count
        c = number(stated[-1]) if stated else None
        if c is None:
            m = re.search(r"इति\s*(\S+)", listpart)
            continue
        if c != n:
            bad += 1
            print(f"leaf {leaf}: {n} words, bracket says {c}: {stated[-1][:50]} … {l[:60]}")
    print(f"{bad} count mismatches")
    if len(argv) > 1:
        import pathlib
        cur, text = None, {}
        for raw in open(argv[0], encoding="utf-8"):
            if raw.startswith("@"):
                cur = int(raw[1:]); continue
            if cur and not raw.startswith(("#", "+", "=")):
                text.setdefault(cur, []).append(raw)
        for leaf, ls in sorted(text.items()):
            f = pathlib.Path(argv[1]) / f"n{leaf}.txt"
            if not f.exists():
                continue
            ocr = set(re.findall(r"[ऀ-ॣ॰-ॿ]+", f.read_text(encoding="utf-8")))
            ocr = {re.sub(r"[॒॑]", "", w).replace("ं", "म्") for w in ocr}
            miss = []
            for w in re.findall(r"[ऀ-ॣ॰-ॿ]+", " ".join(ls)):
                if len(w) < 3 or w in ("इति",):
                    continue
                k = w.replace("ं", "म्")
                if k in ocr:
                    continue
                best = difflib.get_close_matches(k, ocr, n=1, cutoff=0.0)
                r = difflib.SequenceMatcher(None, k, best[0]).ratio() if best else 0
                if r < 0.6:
                    miss.append(f"{w}({best[0] if best else '-'})")
            if miss:
                print(f"leaf {leaf}: {len(miss)} weakly supported: {' '.join(miss[:30])}")


if __name__ == "__main__":
    main(sys.argv[1:])
