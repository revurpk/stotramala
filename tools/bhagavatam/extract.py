# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Extract Pōtana's verses from all eight TTD volumes.

For every page whose running head names a skandha, collect the verse rows
(PriyaankaBold 18 pt), the section titles (20 pt and up) and the verse
numbers (margin numbers, or a four-digit number glued to a line's end).
Pages of introductions, summaries and indexes are skipped.

usage: extract.py OUTDIR PDFDIR   (PDFDIR holds "Bhagavatham Volume 1.pdf" … 8)
writes OUTDIR/items.json  [{"sk": "10.1", "num": 1680, "lines": [...], "page": [vol, pno]}
                           | {"sk": .., "head": "...", "page": ..}]
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / ".claude" / "skills" / "add-stotra" / "scripts"))
import pymupdf
from priyaanka import convert

SRC = str(pathlib.Path(sys.argv[2]) / "Bhagavatham Volume {}.pdf")
SK = [("ప్రథమస్కంధ", "1"), ("ద్వితీయస్కంధ", "2"), ("తృతీయస్కంధ", "3"), ("చతుర్థస్కంధ", "4"),
      ("పంచమస్కంధము – ప్రథమాశ్వాస", "5.1"), ("పంచమస్కంధము – ద్వితీయాశ్వాస", "5.2"),
      ("షష్ఠస్కంధ", "6"), ("సప్తమస్కంధ", "7"), ("అష్టమస్కంధ", "8"), ("నవమస్కంధ", "9"),
      ("దశమస్కంధము – పూర్వభాగ", "10.1"), ("దశమస్కంధము – ఉత్తరభాగ", "10.2"),
      ("ఏకాదశస్కంధ", "11"), ("ద్వాదశస్కంధ", "12")]
SKIP = ("పీఠిక", "సూచి", "కథాసార", "కల్పతరువు", "విషయ", "ముందుమాట", "అనుక్రమ")

def unpua(s):
    b = bytes((ord(c) - 0xF000) if 0xF000 <= ord(c) <= 0xF0FF else ord(c) if ord(c) < 256 else 63 for c in s)
    return b.decode("mac_roman", "replace")

def conv(s):
    return " ".join(convert(unpua(s), alveolar_ra=True).split())

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
items, report = [], []
for vol in range(1, 9):
    doc = pymupdf.open(SRC.format(vol))
    sk, cur, pending = None, None, []
    for pno, page in enumerate(doc):
        spans = [s for b in page.get_text("dict")["blocks"] for l in b.get("lines", []) for s in l["spans"]
                 if s["text"].strip()]
        top = [conv(s["text"]) for s in spans if s["bbox"][1] < 130 and round(s["size"]) in (16, 17)]
        head_text = " ".join(top)
        if any(k in head_text for k in SKIP):
            sk, cur = None, None
            continue
        for key, val in SK:
            if key in head_text:
                if sk != val:
                    cur = None
                    if sk is None and pending:     # head-less pages before it
                        first = next((p for p in pending if "num" in p), None)
                        pending[:] = [p for p in pending if first and p["page"][1] >= first["page"][1]]
                        for p in pending:
                            p["sk"] = val
                        items.extend(pending)
                        pending.clear()
                sk = val
                break
        if sk is None:
            if re.sub(r"[\s\d]|శ్రీమహాభాగవతము", "", head_text):
                continue                           # some other titled page
            sk_hold = True                         # no running head: hold it
        else:
            sk_hold = False
        rows = {}
        for s in spans:
            if s["bbox"][1] < 130 and round(s["size"]) in (16, 17):
                continue                                  # running head / page number
            size, bold = round(s["size"]), "Bold" in s["font"]
            raw = unpua(s["text"]).strip()
            fs = s["size"]
            if raw.isdigit() and s["bbox"][0] > 450 and bold:
                kind = "verse"                       # a margin verse number, at any size
            elif fs >= 21 and not raw.isdigit():
                kind = "head"                        # section titles (22 pt, several fonts)
            elif 17 <= fs < 20.5 and bold and "Priyaanka" in s["font"]:
                kind = "verse"                       # verse text: 18 pt, sometimes 17–19.7
            else:
                continue
            y = round(s["bbox"][1])
            key = min((k for k in rows if abs(k - y) <= 3), default=y)
            rows.setdefault(key, []).append((s["bbox"][0], kind, s["text"], s["font"]))
        for y in sorted(rows):
            sp = sorted(rows[y])
            kind = "head" if any(k == "head" for _, k, _, _ in sp) else "verse"
            if kind == "head":
                text = conv("".join(t for _, k, t, _ in sp if k == "head"))
                text = re.sub(r"^[ఈ\s]+|[ఈ\s]+$", "", text).strip()   # ornament glyphs around titles
                if text:
                    (pending if sk_hold else items).append({"sk": sk, "head": text, "page": [vol, pno]})
                    cur = None
                continue
            isnum = lambda x, t: unpua(t).strip().isdigit() and x > 450
            text = conv("".join(t for x, _, t, _ in sp if not isnum(x, t)))
            digits = "".join(unpua(t).strip() for x, _, t, _ in sp if isnum(x, t))
            num = [int(digits)] if digits else []        # "16" may arrive as "1" + "6"
            m = re.search(r"\s*(\d{1,4})$", text)        # verse text never ends in digits
            if m and not num:
                text, num = text[:m.start()].strip(), [int(m.group(1))]
            if cur is None:
                cur = {"sk": sk, "lines": [], "page": [vol, pno]}
                (pending if sk_hold else items).append(cur)
            if text:
                cur["lines"].append(text)
            if num:
                cur["num"] = num[0]
                cur = None
    print(f"vol {vol} done: {sum(1 for i in items if 'lines' in i)} units so far", flush=True)

# A skandha's first page has no running head, so its opening verses inherit
# the previous skandha. Where the numbering restarts (a verse ≤ 5 after a
# verse > 50 in the same skandha), move everything from the item after the
# last numbered unit up to the next explicit skandha into the following one.
ORDER = [v for _, v in SK]
i, last, last_idx = 0, {}, {}
while i < len(items):
    it = items[i]
    n = it.get("num")
    if n is not None:
        sk = it["sk"]
        if n <= 5 and last.get(sk, 0) > 50:
            nxt = ORDER[ORDER.index(sk) + 1]
            j = last_idx[sk] + 1
            while j < len(items) and items[j]["sk"] == sk:
                items[j]["sk"] = nxt
                j += 1
            print(f"restart in {sk} at item {i}: moved {j - last_idx[sk] - 1} items to {nxt}")
            last.pop(sk); i = last_idx.pop(sk) + 1
            continue
        last[sk], last_idx[sk] = n, i
    i += 1
# Clean-up: drop empty rows and the closing formula; rejoin a unit split at a
# page turn (an unnumbered piece followed by a numbered piece in the same
# skandha whose first line carries no metre label).
LABEL = re.compile(r"^[ఀ-౿]{1,7}\.")
# Image-verified repairs where the PDF's text layer lacks a glyph (SOURCES).
FIXES = {("10.2", 275): [("ధాతునిరరరంజిత", "ధాతునిర్ఝరరంజిత")]}
clean, dropcap = [], False
for it in items:
    if it.get("head") == "శ్రీ":         # a skandha's opening drop cap, set at 25 pt
        dropcap = True
        continue
    if "lines" in it and dropcap:
        m = LABEL.match(it["lines"][0])
        k = m.end() if m else 0
        it["lines"][0] = it["lines"][0][:k] + "శ్రీ" + it["lines"][0][k:].lstrip()
        dropcap = False
    if "lines" in it:
        # bare commentary labels set at verse size; a talakaṭṭu tick wrapped to a line start
        it["lines"] = [re.sub(r"^°", "", l) for l in it["lines"]
                       if not re.fullmatch(r"(?:ప్రతి|తా|విశే)\s*:", l.strip())]
        for a, b in FIXES.get((it["sk"], it.get("num")), []):
            assert any(a in l for l in it["lines"]), (it["sk"], it.get("num"), a)
            it["lines"] = [l.replace(a, b) for l in it["lines"]]
        if not it["lines"] or re.fullmatch(r"[:\s]*శ్రీ\s*కృష్ణార్పణమస్తు[:\s]*", " ".join(it["lines"])):
            continue
        prev = clean[-1] if clean else None
        if (prev and "lines" in prev and "num" not in prev and prev["sk"] == it["sk"]
                and "num" in it and not LABEL.match(it["lines"][0])):
            prev["lines"] += it["lines"]; prev["num"] = it["num"]
            continue
    clean.append(it)
items = clean
json.dump(items, open(out / "items.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
