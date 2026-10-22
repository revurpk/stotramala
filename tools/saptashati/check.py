# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Check a transcribed Saptaśatī chapter against the print's own colophon.

Each chapter of the 1917 print ends with its tally: uvāca-mantras, ardha-
(half-) mantras, śloka-mantras and the total. This checks the file's mantra
numbers run 1…N without a break and that the three kinds add up to the
colophon's counts (a one-line mantra ending in …वाच or ऊचुः is an uvāca, any other
one-line mantra an ardha, a two-line mantra a śloka). It also lists any
character outside Devanāgarī, so a stray Latin letter is caught.

With several files in order, the running total (एवमादितः) is checked too.

usage: check.py ch01.txt [ch02.txt …]
"""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
DIG = str.maketrans("०१२३४५६७८९", "0123456789")


def parse(path):
    mantras, colo = [], ""
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        if line.startswith("@C"):
            colo = line
            continue
        if line.startswith("@"):
            continue
        n, *parts = [p.strip() for p in line.split("|")]
        mantras.append((int(n), parts, ln))
    return mantras, colo


def tally(colo, word):
    m = re.search(word + r"[^\d०-९]*([\d०-९]+)", colo)
    return int(m.group(1).translate(DIG)) if m else None


ok, run = True, 0
for path in sys.argv[1:]:
    mantras, colo = parse(path)
    nums = [n for n, _, _ in mantras]
    breaks = [(a, b) for a, b in zip([0] + nums, nums) if b != a + 1]
    uv = sum(1 for _, p, _ in mantras if len(p) == 1 and re.search(r"(वाच|ऊचुः)$", p[0]))
    ardha = sum(1 for _, p, _ in mantras if len(p) == 1) - uv
    shloka = sum(1 for _, p, _ in mantras if len(p) >= 2)
    # later chapters shorten the labels: उवाच ॥ ३ ॥ श्लोक ॥ ४१ ॥ अर्ध ॥ … ॥
    want = {k + "मंत्राः": tally(colo, k + "(?:मंत्राः)?") for k in ("उवाच", "अर्ध", "श्लोक")}
    want["एवं मंत्राः"] = tally(colo, r"एवं(?:\s*मंत्राः)?(?!मादितः)\s*॥?")
    run += len(mantras)
    adi = tally(colo, "एवमादितः")
    got = {"उवाचमंत्राः": uv, "अर्धमंत्राः": ardha, "श्लोकमंत्राः": shloka, "एवं मंत्राः": len(mantras)}
    odd = sorted({c for _, p, _ in mantras for l in p for c in l
                  if not ("ऀ" <= c <= "ॿ" or c in " ।॥'ऽ-")})
    good = not breaks and all(want[k] in (None, got[k]) for k in want) and not odd and adi in (None, run)
    ok &= good
    print(f"{path}: {'OK' if good else 'CHECK'}  mantras {len(mantras)}  uvāca {uv}  ardha {ardha}  śloka {shloka}"
          f"  | colophon {want}" + (f"  running {run} (print {adi})" if adi else "") + (f"  | breaks {breaks}" if breaks else "") + (f"  | odd {odd}" if odd else ""))
sys.exit(0 if ok else 1)
