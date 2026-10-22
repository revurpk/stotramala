# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Parse the Rāmāyaṇa sarga pages into verses and report anomalies.

Every layout (poem with ॥k-s-v॥, pre blocks with ॥ v॥, <br> runs) is reduced
to plain lines; a verse ends at a line closing in a ॥ number ॥ mark. The
sarga's opening title and closing colophon (…सर्गः ॥k-s॥) are kept apart.
writes sargas.json {kāṇḍa: {sarga: {"title", "colophon", "verses": [[n, [lines]]], "loose": [lines]}}}
usage: parse.py DIR
"""
import collections, json, re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
d = pathlib.Path(sys.argv[1])
pages = json.load(open(d / "pages.json", encoding="utf-8"))
DIG = str.maketrans("०१२३४५६७८९", "0123456789")
ORDER = ["बालकाण्डम्", "अयोध्याकाण्डम्", "अरण्यकाण्डम्", "किष्किन्धाकाण्डम्", "सुन्दरकाण्डम्", "युद्धकाण्डम्", "उत्तरकाण्डम्"]
# a verse-final number: ॥१-१-१॥ / ॥ १॥ / ।। 12 ।। / ॥१२॥ — the verse number is the last component
VNUM = re.compile(r"(?:॥|।।)\s*(?:(?:[०-९0-9]+\s*[-.]\s*[०-९0-9]+\s*[-.]\s*)?([०-९0-9]+)\s*(?:॥|।।)|[०-९0-9]+\s*-\s*[०-९0-9]+\s*-\s*([०-९0-9]+))\s*$")   # closing ॥ may be missing after k-s-v
SARGA = re.compile(r"सर्गः\s*(?:(?:॥|।।)[\s०-९0-9.-]*(?:॥|।।)?)?\s*$")
COLO = re.compile(r"^(?:इति|इत्यार्षे)\S*\s.*सर्ग")

def clean(x):
    x = x.split("==स्रोतः==")[0]
    x = re.sub(r"\{\{[^{}]*\}\}", "", x, flags=re.S)
    x = re.sub(r"\[\[(?:File|सञ्चिका|चित्रम्):[^\]]*\]\]", "", x)
    x = re.sub(r"^\s*(==.*==|\*.*|\[http\S+[^\]]*\].*|पाठकौ .*)\s*$", "", x, flags=re.M)
    x = re.sub(r"\[\[वर्गः:[^\]]*\]\]", "", x)
    x = re.sub(r"<br\s*/?>", "\n", x, flags=re.I)
    x = re.sub(r"</?(poem|pre|div|span|font|center|p)[^>]*>", "\n", x, flags=re.I)
    x = x.replace("'''", "").replace("''", "")
    x = re.sub(r"<ref.*?</ref>", "", x, flags=re.S)
    x = re.sub(r"[‌‍﻿”’“‘]", "", x)   # zero-width marks hide ॥ N ॥ (Yuddha 117); stray quotes
    x = re.sub(r"((?:॥|।।)\s*[०-९0-9]+\s*(?:॥|।।))\s*\(\d+\)", r"\1", x)   # "॥ १॥(4)"
    x = re.sub(r"\[https?://\S+[^\]]*\]", "", x)          # inline links to outside notes
    x = x.replace("ऺ", "")                           # a stray sign typed through Ayodhyā 89–119
    n_colon = len(re.findall(r"(?<=[ऀ-ॿ]):", x))
    x = re.sub(r"(?<=[ऀ-ॿ]):", "ः", x)           # visarga typed as a colon (same sargas)
    if n_colon:
        MIDLOG.append(f"{n_colon} visargas typed as “:” restored")
    lines = []
    for l in x.split("\n"):
        l = l.strip().lstrip(":").strip()                 # "::" indents a long-metre line
        if re.search(r"[A-Za-z]{3}", l) or re.match(r"^[०-९]{3}\s", l) or re.fullmatch(r"\(.*\)", l):
            if l:
                MIDLOG.append(f"dropped non-text line “{l[:50]}”")
            continue                                      # audio-player text, a reciter's credit
        for g in re.findall(r"\s*\([^)]*\)", l):
            MIDLOG.append(f"bracketed note “{g.strip()}” removed")
        l = re.sub(r"\s*\([^)]*\)", "", l)
        lines.append(l)
    # a number inside a line ends a verse there; what follows is either the next
    # verse's start or (Uttara) a stray copy of nearby text, dropped when it is
    out = []
    for i, l in enumerate(lines):
        m = MID.search(l)
        while m:
            head, tail = l[:m.end() - 1].rstrip(), l[m.end() - 1:].strip()
            near = " ".join(lines[max(0, i - 3):i] + lines[i + 1:i + 4])
            frag = re.sub(r"\s*(?:॥|।।|।)+\s*$", "", tail)
            if not frag or "ा" <= frag[0] <= "्" or frag in near:
                MIDLOG.append(f"dropped stray “{tail[:40]}” after {m.group(0)[:-1].strip()}")
                l = head; break
            out.append(head); l = tail
            MIDLOG.append(f"split line at {m.group(0)[:-1].strip()}")
            m = MID.search(l)
        out.append(l)
    return out

MID = re.compile(r"(?:॥|।।)\s*(?:[०-९0-9]+\s*[-.]\s*)*[०-९0-9]+\s*(?:॥|।।)\s*(?![॥।०-९0-9\s])\S")
PRAK = re.compile(r"^([०-९0-9]+)\s*(अ|आ|इ|ब|क)?\s*प्रक्षिप्त")

def repair(verses, where, log):
    """Split a block that fuses k verses whose numbers the e-text dropped (it has
    exactly 2k lines and the next number jumps by k), then number by position.
    Every place where the result differs from the e-text's number is logged."""
    src = [n for n, _ in verses]
    if not src or src == list(range(1, len(src) + 1)):
        return [[n, ls] for n, ls in verses]
    # a run whose numbers are mostly wrong (Bāla 29: 25, 2, 25, 25 …) is numbered by position
    if sum(1 for i, n in enumerate(src) if n != i + 1) > len(src) // 2 and len(set(src)) < len(src) // 2:
        log.append(f"{where}: e-text numbers garbled ({src[:4]}…); numbered by position 1–{len(src)}")
        return [[i + 1, ls] for i, (_, ls) in enumerate(verses)]
    out, prev = [], 0
    for i, (n, ls) in enumerate(verses):
        nxt = verses[i + 1][0] if i + 1 < len(verses) else None
        k = n - prev                      # e.g. prev 2, this 4 → it holds 3 and 4
        if n == prev and (nxt is None or nxt == prev + 2):
            out.append([prev + 1, ls]); log.append(f"{where}: second {n} read as {prev + 1}")
            prev += 1; continue
        if n != prev + 1 and nxt == prev + 2 and len(ls) == 2:   # 2, 13, 4 → the 13 is 3
            out.append([prev + 1, ls]); log.append(f"{where}: number {n} between {prev} and {nxt} read as {prev + 1}")
            prev += 1; continue
        if n == prev + 2 and nxt == n and len(ls) == 2:     # 13, 15, 15 → the first 15 is 14
            out.append([prev + 1, ls]); log.append(f"{where}: first {n} read as {prev + 1}")
            prev += 1; continue
        if k >= 2 and len(ls) == 2 * k and (nxt is None or nxt == n + 1):
            for j in range(k):
                out.append([prev + 1 + j, ls[2 * j:2 * j + 2]])
            log.append(f"{where}: block {n} split into {prev + 1}–{n} (their numbers were dropped)")
        else:
            if k >= 2:
                log.append(f"{where}: e-text has no verse {prev + 1}" + (f"–{n - 1}" if k > 2 else "") + " (gap kept)")
            elif k <= 0:
                log.append(f"{where}: number {n} after {prev} kept as printed")
            out.append([n, ls])
        prev = out[-1][0]
    return out

MIDLOG = []
out, report, fixes = {}, collections.defaultdict(list), collections.defaultdict(list)
for k in ORDER:
    out[k] = {}
    titles = sorted((t for t in pages if t.startswith(f"रामायणम्/{k}/सर्गः ")),
                    key=lambda t: int(t.rsplit(" ", 1)[1].translate(DIG)))
    for t in titles:
        s = int(t.rsplit(" ", 1)[1].translate(DIG))
        rec = {"title": "", "colophon": "", "verses": [], "loose": []}
        cur = []
        MIDLOG.clear()
        for l in clean(pages[t]["text"]):
            if not l:
                continue
            if COLO.search(l) or SARGA.search(l):
                if not rec["verses"] and not cur and not COLO.search(l):
                    rec["title"] = l
                else:
                    if cur:
                        rec["loose"] += cur; cur = []
                    rec["colophon"] = l
                continue
            pm = PRAK.match(l)
            if pm:                            # an interpolated sarga printed after this one
                if cur:
                    rec["loose"] += cur; cur = []
                rec.setdefault("parts", []).append({"label": l, "start": len(rec["verses"])})
                continue
            if re.fullmatch(r"(?:॥|।।)?\s*(?:इत्य|श्रीसीताराम).*(?:समाप्तः|सम्पूर्णम्|मस्तु)\s*(?:॥|।।)?", l):
                rec.setdefault("end", []).append(l)     # closing formulas after the last sarga
                continue
            cur.append(l)
            m = VNUM.search(l)
            if m:
                body = l[:m.start()]
                while VNUM.search(body.rstrip()):          # "॥ १६ ॥१-३४-१६॥": both markers go
                    body = body[:VNUM.search(body.rstrip()).start()]
                body = re.sub(r"(?:॥|।।)\s*[०-९0-9]+\s*$", "", body)
                cur[-1] = body.rstrip(" ।")
                rec["verses"].append([int((m.group(1) or m.group(2)).translate(DIG)), cur]); cur = []
        fixes[k] += [f"{k} {s}: {x}" for x in MIDLOG]
        rec["loose"] += cur
        # split off interpolated parts, each with its own numbering, then repair each run
        cuts = [0] + [p["start"] for p in rec.get("parts", [])] + [len(rec["verses"])]
        runs = [rec["verses"][a:b] for a, b in zip(cuts, cuts[1:])]
        rec["verses"] = repair(runs[0], f"{k} {s}", fixes[k])
        for p, run in zip(rec.get("parts", []), runs[1:]):
            p["verses"] = repair(run, f"{k} {s} {p['label']}", fixes[k])
            del p["start"]
        if rec["loose"]:
            report[k].append(f"{s}: loose {rec['loose'][:3]}")
        if not rec["colophon"]:
            report[k].append(f"{s}: no colophon")
        out[k][s] = rec
json.dump(out, open(d / "sargas.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(fixes, open(d / "fixes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k in ORDER:
    n = sum(len(r["verses"]) + sum(len(p["verses"]) for p in r.get("parts", [])) for r in out[k].values())
    parts = sum(len(r.get("parts", [])) for r in out[k].values())
    print(f"{k}: {len(out[k])} sargas (+{parts} interpolated), {n} verses, {len(fixes[k])} repairs, {len(report[k])} anomalies")
    for line in report[k][:8] + fixes[k][:6]:
        print("   ", line)
