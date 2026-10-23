# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Parse Sanskrit Wikisource's Devī Bhāgavatam (pages.json from fetch.py).

Each adhyāya page is a <poem> of verses ending ॥ N ॥ (sometimes ।। s.a.N ।।),
speaker lines (… उवाच) and a colophon (after the poem, or inside it). The
e-text's numbering slips are repaired by the same rules as the Rāmāyaṇa
(tools/ramayana/parse.py), each logged. Writes adhyayas.json
{part: {adhyāya: {"verses": [{"n", "lines", "sp"}], "colophon"}}} and fixes.json.
Parts are "0" (the māhātmya) and "1"…"12".
usage: parse.py DIR
"""
import collections, json, re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
d = pathlib.Path(sys.argv[1])
pages = json.load(open(d / "pages.json", encoding="utf-8"))
DIG = str.maketrans("०१२३४५६७८९", "0123456789")
VNUM = re.compile(r"(?:(?:॥|।।|।)\s*|(?<=[\u0900-\u0963])|(?<=[\u0900-\u0963]\s))(?:[०-९0-9]+\s*\.\s*[०-९0-9]+\s*\.\s*)?([०-९0-9]+)[\s।॥]*\.?\s*$")   # closing ॥ sometimes missing
COLO = re.compile(r"^(?:(?:इ)?ति\s*श्र\S*\s*(?:देवी\s?भागवत\S*|स्कन्द)\s|इति\s*श्री\S*\s*(?:मद्)?\s*(?:देवी\s?भागवते|स्कन्द\s?पुराणे|स्कान्दे|देवीभागवतमाहात्म्ये)|समाप्त(?:ः|ोऽ|मिदम्|मिदं))")   # not समाप्ते, समाप्ति…
SPEAK = re.compile(r"^(?:\S+\s+){0,2}\S*(?:वाच|ऊचुः|ऊचतुः)\s*[-–—:।॥]*\s*(?:[०-९0-9]+\s*[।॥]*\s*)?$")
AHEAD = re.compile(r"^(?:अथ\s+)?\S*अध्याय[ः:]?\s*[०-९0-9]*\s*[।॥]*\s*$")
TITLE = re.compile(r"देवीभागवतपुराणम्/(?:स्कन्धः\s*([०-९]+)|(माहात्म्यम्))/अध्याय[ः]?\s*([०-९]+)")


def repair(vs, where, log):
    prose = [v for v in vs if v["n"] is None]
    vs = [v for v in vs if v["n"] is not None]
    if prose:
        log.append(f"{where}: {len(prose)} unnumbered prose passage(s) kept")
    merged, carry = [], None                                # a bare-॥ block: a verse whose number
    for i, v in enumerate(vs):                              # was dropped, or only a half-verse
        if carry:
            v = {**v, "lines": carry["lines"] + v["lines"], "sp": carry["sp"] + v["sp"]}; carry = None
        if v["n"] == -1:
            prevn = merged[-1]["n"] if merged else 0
            nxt = next((w["n"] for w in vs[i + 1:] if w["n"] != -1), None)
            if nxt == prevn + 2:
                log.append(f"{where}: verse after {prevn} closed by a bare ॥, numbered {prevn + 1}")
                v = {**v, "n": prevn + 1}
            else:
                carry = v; continue
        merged.append(v)
    vs = merged
    out2 = []
    for v in vs:                                            # a verse typed twice in a row
        if out2 and v["lines"] == out2[-1]["lines"]:
            log.append(f"{where}: verse {v['n']} repeated in the e-text, second copy dropped"); continue
        out2.append(v)
    vs = out2
    src = [v["n"] for v in vs]
    if not src or src == list(range(1, len(src) + 1)):
        return vs + prose
    out, prev = [], 0
    for i, v in enumerate(vs):
        n, ls = v["n"], v["lines"]
        nxt = vs[i + 1]["n"] if i + 1 < len(vs) else None
        k = n - prev
        if n != prev + 1 and nxt == prev + 2 and len(ls) == 2:
            log.append(f"{where}: number {n} between {prev} and {nxt} read as {prev + 1}")
            out.append({**v, "n": prev + 1})
        elif n == prev and (nxt is None or nxt == prev + 2):
            log.append(f"{where}: second {n} read as {prev + 1}")
            out.append({**v, "n": prev + 1})
        elif k >= 2 and len(ls) == 2 * k and (nxt is None or nxt == n + 1):
            for j in range(k):
                out.append({"n": prev + 1 + j, "lines": ls[2 * j:2 * j + 2], "sp": v["sp"] if j == 0 else []})
            log.append(f"{where}: block {n} split into {prev + 1}–{n} (their numbers were dropped)")
        else:
            if k >= 2:
                log.append(f"{where}: e-text has no verse {prev + 1}" + (f"–{n - 1}" if k > 2 else "") + " (gap kept)")
            elif k <= 0:
                log.append(f"{where}: number {n} after {prev} kept as printed")
            out.append(v)
        prev = out[-1]["n"]
    return out + prose


out, report, fixes = collections.defaultdict(dict), [], []
# a duplicate title spelled अध्याय (no visarga) sorts after the proper one
for t, p in sorted(pages.items(), key=lambda kv: (kv[0].replace("अध्याय ", "अध्यायः ") , "अध्याय " in kv[0])):
    m = TITLE.fullmatch(t)
    if not m:
        continue
    part = "0" if m.group(2) else str(int(m.group(1).translate(DIG)))
    ch = int(m.group(3).translate(DIG))
    x = p["text"]
    x = re.sub(r"<ref.*?</ref>|<ref[^>]*/>", "", x, flags=re.S)
    x = re.sub(r"\{\{[^{}]*\}\}", "", x)
    x = re.sub(r"\[\[(?:वर्गः|Category):[^\]]*\]\]", "", x)
    x = x.replace("‌", "").replace("‍", "")
    x = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", x)   # an outside link around a word: keep the word
    nb = len(re.findall(r"[\[\]`]", re.sub(r"\[\[[^\]]*\]\]", "", x)))
    if nb:
        fixes.append(f"{part}.{ch}: {nb} brackets/backticks removed")
    x = re.sub(r"(?<!\[)\[(?!\[)|(?<!\])\](?!\])|`", "", x)
    x = re.sub(r"(?<=[ऀ-ॿ])H", "ः", x)           # visarga typed as H
    pre, _, rest = x.partition("<poem>")
    if not rest:
        pre, rest = "", x
    head = [l.strip() for l in re.sub(r"<[^>]+>", "\n", pre).splitlines() if l.strip()]
    body = re.sub(r"<[^>]+>", "\n", rest)                   # every poem block, and what follows
    colo = []
    colo_lines, tail_colo = [], colo
    vs, cur, sp, incolo, done, end = [], [], [], False, False, []
    raw = []
    for l in (l.strip() for l in body.splitlines()):
        # a verse number inside a line ends the verse there (…च्छिदम् ॥ ७ । सूत उवाच)
        while True:
            mm = re.search(r"(?:(?:॥|।।)\s*|(?<=[\u0900-\u0963]))([०-९]+)\s*(?:॥|।।|।)\s*।?\s*(?=[^\s।॥.])", l)
            if not mm or mm.end() >= len(l):
                break
            raw.append(l[:mm.end()].rstrip(" ।") + " ॥" if l[mm.end() - 1] == "।" else l[:mm.end()])
            fixes.append(f"{part}.{ch}: verse {mm.group(1)} ended mid-line")
            l = l[mm.end():].strip()
        raw.append(l)
    # a page that ends half-verses with ॥ (5.17 …) cannot use a bare ॥ as a verse end
    nb = sum(1 for l in raw if re.search(r"\S\s*(?:॥|।।)\s*$", l) and not VNUM.search(l))
    bare_ok = nb <= max(2, len(raw) // 40)
    for l in raw:
        if not l:
            continue
        l = re.sub(r"[“”\"]", "", l).strip()
        if l in ("ॐ", "-", "—", ""):
            continue
        if done:                                           # after the colophon: end-notes
            end.append(l); continue
        if AHEAD.match(l) and not cur:                    # "अथ त्रयस्त्रिंशोऽध्यायः" set in the poem
            head.append(l); continue
        if SPEAK.match(l) and cur and not vs and not any("।" in c or "॥" in c for c in cur):
            head += cur; cur = []                          # an adhyāya title set inside the poem
        if not cur and SPEAK.match(l):
            sp.append(re.sub(r"\s*[-–—:]\s*$", "", l)); continue
        if incolo:                                         # a colophon runs on to its ॥ N ॥
            colo.insert(len(colo) - len(tail_colo), l) if False else colo_lines.append(l)
            incolo = not VNUM.search(l); done = not incolo; continue
        if COLO.match(l):
            if cur:                                        # unnumbered prose before it (12.4)
                vs.append({"n": None, "lines": cur, "sp": sp, "prose": True}); cur, sp = [], []
            colo_lines.append(l); incolo = not VNUM.search(l); done = not incolo; continue
        if re.fullmatch(r"अध्याय\s+\S+\s+समाप्त", l):    # a Marathi end-note (skandha 8)
            continue
        cur.append(l)
        mm = VNUM.search(l)
        if not mm and bare_ok and re.search(r"\S\s*(?:॥|।।)\s*$", l) and len(cur) >= 2:
            cur[-1] = re.sub(r"\s*(?:॥|।।)\s*$", "", l)        # closed by a bare ॥: number dropped
            vs.append({"n": -1, "lines": cur, "sp": sp}); cur, sp = [], []
            continue
        if mm:
            cur[-1] = l[:mm.start()].rstrip(" ।")
            vs.append({"n": int(mm.group(1).translate(DIG)), "lines": cur, "sp": sp})
            cur, sp = [], []
    colo = colo_lines + colo
    colophon = re.sub(r"\s*(?:॥|।।)?\s*[०-९0-9]*\s*(?:॥|।।)?\s*\.?\s*$", "", " ".join(c for c in colo if COLO.match(c) or c.startswith(("प्रथम", "द्वितीय")) or "स्कन्धे" in c))
    if cur:
        report.append(f"{part}.{ch}: loose {cur[:2]}")
    if ch in out[part]:
        report.append(f"{part}.{ch}: DUPLICATE page {t}")
        continue
    vs = repair(vs, f"{part}.{ch}", fixes)
    nums = [v["n"] for v in vs if v["n"] is not None]
    if nums != list(range(1, len(nums) + 1)):
        report.append(f"{part}.{ch}: numbering left with gaps (n={len(nums)}, last={nums[-1]})")
    if not colophon:
        report.append(f"{part}.{ch}: no colophon")
    out[part][ch] = {"verses": vs, "colophon": colophon, "head": " ".join(head), "end": end, "rev": p["rev"], "title": t}
json.dump(out, open(d / "adhyayas.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(fixes, open(d / "fixes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for part in sorted(out, key=int):
    chs = sorted(out[part])
    n = sum(len(out[part][c]["verses"]) for c in chs)
    print(f"part {part}: {len(chs)} adhyāyas, {n} verses")
print(len(fixes), "repairs;", len(report), "anomalies")
for r in report[:40]:
    print("  ", r)
