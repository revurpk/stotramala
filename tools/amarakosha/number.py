# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Group the e-text's half-verses into the 1882 print's ślokas.

In the print a śloka's second half closes with ॥ N ॥, and every kṣepaka
(interpolated verse) stands in quotation marks. The OCR (mula.json) misreads the
digits often but rarely loses the closing mark itself, so: walk the e-text
half-verses of each varga (align.json maps each to its print line) and close a
group wherever the print line carries a closing number. Within a group, a line
the print quotes is a kṣepaka line (the quote state is reset each group, so a
lost closing quote cannot run on). The rest of the group is the śloka, numbered
in sequence through the varga; the OCR's own digits are only a cross-check.

Overrides settled on the page image (FILE, tab-separated): K.V, e-text n, and
one of  ks | main | end (closes a śloka here) | open (does not) | drop.
Writes slokas.json {"K.V": [{"n", "ks", "lines": [i…]}]} (i indexes align.json)
and anomalies.txt.   usage: number.py DIR [--overrides FILE]
"""
import collections, json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
QUOTE = "“”\"„"
# a closing number: ॥ N ॥ with N any short non-letter token (the OCR reads ८ as <, ४ as १ …),
# or digits with the last ॥ lost, or with the first one lost
END = re.compile(r"[॥।|]{1,2}\s*[^\s॥।|अ-ह]{1,4}(?:\s[०-९0-9]{1,2})?\s*[॥।|]{1,2}\W*(?:\([०-९0-9]\))?\s*$"
                 r"|[॥।|]{1,2}\s*[०-९0-9]{1,3}\W*$|\s[०-९]{1,3}\s*[॥।|]{1,2}\W*$")


# The print's vargas, where they differ from the e-text's sections: it numbers the
# preface on into the svargavarga, the śabdavarga on from the vāgvarga, the
# kāṇḍa-openings into the first varga, and the avyayas on from the nānārthas.
MERGE = {"1.0": "1.1", "1.7": "1.6", "2.0": "2.1", "3.0": "3.1", "3.4": "3.3"}


def spans(A, idx):
    """Per position in idx: inside a kṣepaka? A span runs from a line with an
    opening quote to the first line, at most SPAN lines on, with a closing one;
    an opening quote that never closes is a speck the OCR read as a quote."""
    out = [False] * len(idx)
    texts = [A[i].get("ocr", "") for i in idx]
    pos = 0
    while pos < len(idx):
        t = texts[pos]
        o = max(t.rfind("“"), t.rfind("„"), t.find('"'))
        if o >= 0 and not ("”" in t[o + 1:] or '"' in t[o + 1:]):
            # closes at a closing quote; failing one (the OCR loses quotes), at the
            # kṣepaka's own small number
            rng = range(pos + 1, min(len(idx), pos + SPAN))
            close = next((k for k in rng if "”" in texts[k] or '"' in texts[k]), None)
            if close is None:
                close = next((k for k in rng if A[idx[k]].get("end") and (A[idx[k]].get("num") or 99) <= 5), None)
            if close is not None:
                for k in range(pos, close + 1):
                    out[k] = True
                pos = close + 1
                continue
        elif o >= 0:
            out[pos] = True                                   # opens and closes on one line
        pos += 1
    return out


SPAN = 8


def load_overrides(path):
    ov = {}
    if path and pathlib.Path(path).exists():
        for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
            if l.strip() and not l.startswith("#"):
                kv, n, what, *_ = l.split("\t")
                if what.strip() in ("ks", "nip", "main", "end", "open"):
                    a, _, b = n.partition("-")                  # n or a range a-b
                    for x in range(int(float(a)), int(float(b or a)) + 1):
                        ov[(kv, float(x))] = what.strip()
    return ov


def main(argv):
    d = pathlib.Path(argv[0])
    ov = load_overrides(argv[argv.index("--overrides") + 1] if "--overrides" in argv
                        else pathlib.Path(__file__).with_name("print1882.tsv"))
    A = json.load(open(d / "align.json", encoding="utf-8"))
    for r in A:
        t = r.get("ocr", "")
        # a group marker can follow the number (॥४४॥ इति ढांताः), and a number can stand bare (… च ३९)
        core = re.sub(r"[॥।|:\s]*इति\s*\S+[॥।|:\s]*$", "", t)
        r["end"] = bool(END.search(core) or re.search(r"\s[०-९]{1,3}\s*$", core)) if t else None
        if r["end"] and core != t:
            t = core
        r["qt"] = any(c in QUOTE for c in t)
        if r["end"] and r.get("num") is None:                  # ॥” २० ॥ — a quote between ॥ and the digits
            m = re.search(r"([०-९]{1,3})\D{0,4}$", t)
            if m:
                r["num"] = int(m.group(1).translate(str.maketrans("०१२३४५६७८९", "0123456789")))
        r["ov"] = ov.get((f"{r['k']}.{r['v']}", float(r["n"])))
        if r["ov"] in ("end", "open"):
            r["end"] = r["ov"] == "end"
    by = collections.OrderedDict()
    for i, r in enumerate(A):
        if r["ov"] != "drop":
            kv = f"{r['k']}.{r['v']}"
            by.setdefault(MERGE.get(kv, kv), []).append(i)
    out, report, stat = {}, [], [0, 0]
    for key, idx in by.items():
        groups, n, main_, ks = [], 0, [], []
        held = []                                   # kṣepakas met inside a śloka, shown after it

        def close_main():
            nonlocal n, main_, held
            n += 1
            last = A[main_[-1]]
            pn = last.get("num")
            if pn is not None and last["end"]:
                stat[1] += 1
                stat[0] += pn == n
                if pn != n:
                    report.append(f"{key} {n}: print digits read {pn} (e-text {last['n']}, leaf {last.get('leaf')}) — {last['text'][:44]}")
            if len(main_) != 2:
                report.append(f"{key} {n}: {len(main_)} half-verse(s) (e-text {A[main_[0]]['n']}, leaf {A[main_[0]].get('leaf')}) — {A[main_[0]]['text'][:44]}")
            groups.append({"n": n, "ks": False, "lines": main_})
            groups.extend(held)
            main_, held = [], []

        def close_ks():
            nonlocal ks
            g = {"n": None, "ks": True, "lines": ks}
            report.append(f"{key} after {n + (1 if main_ else 0) - (0 if main_ else 0)}: kṣepaka, {len(ks)} half-verse(s) (e-text {A[ks[0]]['n']}, leaf {A[ks[0]].get('leaf')}) — {A[ks[0]]['text'][:44]}")
            (held if main_ else groups).append(g)
            ks = []

        ksf = spans(A, idx)
        for pos, i in enumerate(idx):
            r = A[i]
            q = ksf[pos]
            if r["ov"] in ("ks", "nip"):
                q = True
            elif r["ov"] == "main":
                q = False
            if q:
                ks.append(i)
                if r["end"] or pos + 1 == len(idx) or not ksf[pos + 1]:
                    close_ks()
                    # a kṣepaka set inside a śloka can carry the śloka's own number (॥” २० ॥)
                    # — told from the kṣepaka's own count (॥ १ ॥”) by the digits following the quote
                    t = r.get("ocr", "")
                    after = t[max(t.rfind("”"), t.rfind('"')) + 1:] if ("”" in t or '"' in t) else ""
                    if r["end"] and main_ and r.get("num") == n + 1 and re.search(r"[०-९0-9]", after):
                        close_main()
                continue
            if ks:
                close_ks()
            main_.append(i)
            closes = r["end"] if r["end"] is not None else len(main_) >= 2
            if closes:
                close_main()
        if ks:
            close_ks()
        if main_:
            close_main()
        out[key] = groups
        print(f"{key}: {n} ślokas, {sum(g['ks'] for g in groups)} kṣepaka passages")
    print(f"print digits agree {stat[0]}/{stat[1]}; {len(report)} notes")
    (d / "anomalies.txt").write_text("\n".join(report), encoding="utf-8")
    json.dump(out, open(d / "slokas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main(sys.argv[1:])
