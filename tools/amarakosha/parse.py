# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Parse Sanskrit Wikisource's Amarakośa (pages.json from tools/devibhagavatam/fetch.py,
run with the prefix अमरकोशः/).

The e-text sets one half-verse a line, each closed by ॥ K.V.N ॥ (kāṇḍa, varga, a
running half-verse count through the kāṇḍa). Between them stand varga headings,
the e-text's own end-of-group markers (इति धान्ताः …) and editors' tallies of
the verses (अत्र मूलश्लोकाः …). This groups the half-verses by varga and pairs
them into ślokas, numbered from 1 in each varga; tallies are dropped and logged.

Writes vargas.json [{"k", "v", "lines": [[text, n]…], "marks": {after_n: text}}]
and prints a report.  usage: parse.py DIR
"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
d = pathlib.Path(sys.argv[1])
pages = json.load(open(d / "pages.json", encoding="utf-8"))
DIG = str.maketrans("०१२३४५६७८९", "0123456789")
KAND = {"प्रथमकाण्डम्": 1, "द्वितीयकाण्डम्": 2, "तृतीयकाण्डम्": 3}
LINE = re.compile(r"^(.*?)\s*(?:॥|।।)\s*([०-९]+)\.([०-९]+)\.([०-९]+)\s*(?:॥|।।)\s*$")
TALLY = re.compile(r"मूलश्लोकाः|क्षे\s*\.?\s*श्लो|^\s*सर्वे च मिलित्वा|मू श्लो")
MARK = re.compile(r"^इति\s+\S+न्ताः$|^इति\s+\S+\s*संग्रहः$|^इति\s+\S+शेषसंग्रहः$")
HEAD = re.compile(r"^\S*वर्गः$")                               # a varga title numbered as a verse
FIX_MARK = {"इति क्षेपकच्छान्ताः": "इति छान्ताः"}               # e-text's note fused into the marker

out, log = {}, []
for title, page in pages.items():
    k = KAND[title.split("/")[1]]
    last_n = None
    for raw in page["text"].splitlines():
        s = re.sub(r"<br\s*/?>|'''|==|<poem>|</poem>", "", raw).strip()
        if not s or s.startswith(("{{", "|", "}}")):
            continue
        m = LINE.match(s)
        if m:
            text, kk, v, n = m.group(1).strip(), *(int(x.translate(DIG)) for x in m.groups()[1:])
            if kk != k:
                log.append(f"{k}: line numbered kāṇḍa {kk}: {s}")
            if TALLY.search(text):
                log.append(f"{k}.{v}: tally dropped (numbered {n}): {text}")
                continue
            text = FIX_MARK.get(text, text)
            clean = re.sub(r"\s*\(.*$", "", text)                      # a contributor's query: (ऽबहूनिऽ?
            clean = re.sub(r"\s+[०-९]{3,4}$", "", clean)               # the e-text's running count, 970 …
            clean = re.sub(r"\s*।\s*", " ", clean)                    # stray daṇḍas inside a half-verse
            clean = re.sub(r"\.+$", "", clean)                          # a stray full stop at the end
            clean = re.sub(r"\s+", " ", clean).strip()
            if clean != text:
                if clean.replace(" ", "") != text.replace(" ", ""):
                    log.append(f"{k}.{v}.{n}: cleaned '{text}' → '{clean}'")
                text = clean
            if MARK.match(text) and last_n:
                out[last_n[:2]]["marks"][last_n[2]] = text
                log.append(f"{k}.{v}: group marker numbered {n} set as a marker: {text}")
                continue
            if HEAD.match(text):
                log.append(f"{k}.{v}: heading numbered {n} dropped: {text}")
                continue
            rec = out.setdefault((k, v), {"k": k, "v": v, "lines": [], "marks": {}})
            rec["lines"].append([text, n])
            last_n = (k, v, n)
            continue
        body = re.sub(r"[॥।%]|\s+", " ", s).strip()
        body = re.sub(r"\s*[०-९]+\s*$", "", body).strip()           # 'अथ लिङ्गादिसंग्रहवर्गः ५'
        if TALLY.search(body):
            log.append(f"{k}: tally dropped: {body}")
        elif MARK.match(body) and last_n:
            out[last_n[:2]]["marks"][last_n[2]] = body
        else:
            log.append(f"{k}: heading/other (not kept as text): {body}")

# readings of the 1882 print (print1882.tsv): text ops only; structure is number.py's
TSV = pathlib.Path(__file__).with_name("print1882.tsv")
for row in TSV.read_text(encoding="utf-8").splitlines():
    if not row.strip() or row.startswith("#"):
        continue
    kv, n, op, old, new, *leaf = (row.split("	") + [""] * 6)[:6]
    if op not in ("line", "r", "join", "drop", "add", "mark", "move"):
        continue
    k, v = map(int, kv.split(".")); n = float(n)
    rec = out.get((k, v))
    at = next((j for j, (t, m) in enumerate(rec["lines"]) if m == n), None) if rec else None
    if at is None:
        log.append(f"print1882 {kv}.{n:g} {op}: line not found"); continue
    t = rec["lines"][at][0]
    if op == "line":
        if old and old.replace(" ", "") != t.replace(" ", ""):
            log.append(f"print1882 {kv}.{n:g} line: e-text reads '{t}', not '{old}'")
        rec["lines"][at][0] = new
    elif op == "r":
        if old not in t:
            log.append(f"print1882 {kv}.{n:g} r: '{old}' not in '{t}'"); continue
        rec["lines"][at][0] = t.replace(old, new, 1)
    elif op == "join":
        rec["lines"][at - 1][0] = rec["lines"][at - 1][0].rstrip() + t.strip()
        del rec["lines"][at]
    elif op == "drop":
        del rec["lines"][at]
    elif op == "move":                                          # the print has it after line `new`
        line = rec["lines"].pop(at)
        to = next(j for j, (t2, m) in enumerate(rec["lines"]) if m == float(new))
        rec["lines"].insert(to + 1, line)
    elif op == "mark":                                          # a group marker the e-text lacks
        key = int(n) if n == int(n) else n
        if new:
            rec["marks"][key] = new
        else:                                                   # an empty mark moves one away
            rec["marks"].pop(key, None) or rec["marks"].pop(str(key), None)
    elif op == "add":
        rec["lines"].insert(at + 1, [new, round(n + 0.1, 2)])   # after n: n.1, after n.1: n.2

vargas = [out[key] for key in sorted(out)]
json.dump(vargas, open(d / "vargas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for r in vargas:
    ns = [n for _, n in r["lines"]]
    gaps = [(a, b) for a, b in zip(ns, ns[1:]) if b != a + 1]
    print(f"{r['k']}.{r['v']}: {len(ns)} half-verses ({ns[0]}–{ns[-1]})"
          + (" ODD" if len(ns) % 2 else "") + (f" gaps {gaps}" if gaps else "")
          + (f" marks {len(r['marks'])}" if r["marks"] else ""), "|", r["lines"][0][0])
print("\n".join(log))
