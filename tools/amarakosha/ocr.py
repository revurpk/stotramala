# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Pull the mūla lines out of the 1882 print's OCR (archive.org 20231127_20231127_1402,
the item's _djvu.xml). The kośa is set in large type above Maheśvara's commentary
in small type; a line is mūla when its words are tall against the page's body text.

Writes mula.json [{"leaf", "y", "h", "text"}] in reading order.
usage: ocr.py DJVU.xml OUT.json [--show LEAF]
"""
import json, re, statistics, sys
import xml.etree.ElementTree as ET
sys.stdout.reconfigure(encoding="utf-8")


def lines(path):
    for leaf, obj in enumerate(ET.parse(path).getroot().iter("OBJECT")):
        out = []
        for ln in obj.iter("LINE"):
            ws = ln.findall("WORD")
            if not ws:
                continue
            boxes = [tuple(map(int, w.get("coords").split(",")[:4])) for w in ws]
            hs = [b[1] - b[3] for b in boxes]                  # coords: left,bottom,right,top
            out.append({"leaf": leaf, "y": min(b[3] for b in boxes), "x": min(b[0] for b in boxes),
                        "h": statistics.median(hs), "text": " ".join(w.text or "" for w in ws)})
        yield leaf, out


def split(ls):
    """Index where the commentary starts: the cut into a tall top and a short foot
    with the least spread of heights within each; a page of one type only is
    judged by its median (the kośa's type measures about 140, the commentary's 90)."""
    h = [l["h"] for l in ls[1:]]                                # [0] is the running head
    best, k = None, None
    for i in range(1, len(h)):
        a, b = h[:i], h[i:]
        if statistics.mean(a) < statistics.mean(b) * 1.2:
            continue
        cost = sum((x - statistics.mean(a)) ** 2 for x in a) + sum((x - statistics.mean(b)) ** 2 for x in b)
        if best is None or cost < best:
            best, k = cost, i + 1
    if k is None:
        return len(ls) if h and statistics.median(h) > 118 else 1
    return k


def main(argv):
    show = int(argv[argv.index("--show") + 1]) if "--show" in argv else None
    mula = []
    for leaf, ls in lines(argv[0]):
        if not ls:
            continue
        # the commentary is the run of small-type lines that ends the page; everything
        # above it but the running head is the kośa (OCR heights are too noisy to
        # classify line by line: a mūla line can measure as small as 105)
        ls.sort(key=lambda l: l["y"])
        ls = [l for l in ls if l["h"] >= 50]                    # specks, signatures
        if not ls:
            continue
        k = split(ls)
        for i, l in enumerate(ls):
            head = i == 0 and re.search(r"कोश|काण्ड|कांड|वर्ग|वगे|^\S*\s*[०-९]+\s*$", l["text"])
            l["big"] = i < k and not head and len(l["text"]) > 8
            if show == leaf:
                print(f"{l['h']:4.0f} {'M' if l['big'] else ' '} y{l['y']:5d} {l['text']}")
        mula += [{k: l[k] for k in ("leaf", "y", "h", "text")} for l in ls if l["big"]]
    if show is None:
        json.dump(mula, open(argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print(len(mula), "mūla lines")


if __name__ == "__main__":
    main(sys.argv[1:])
