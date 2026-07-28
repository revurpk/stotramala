#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Browser-free round-trip check: render IAST → Devanāgarī and compare to the
source, in pure Python (no Node, no browser, no dev server).

WHY THIS EXISTS: the render on the live pages is teltools' JS
(iast2tel → tel2hin → post, plus devSvara for accents). Verifying it used to
mean a browser host, but the sandbox can block that (localhost policy) and the
network can drop mid-check. This is a faithful Python port of that exact
pipeline, so the round-trip runs anywhere Python does. It got 37/37 byte-exact
on the Kālabhairavāṣṭakam that first exposed the browser limitation.

KEEP IN SYNC: the tables below are transcribed from the teltools block inlined
in every built page. teltools is stable, but if it ever changes, re-transcribe
iast2tel's tables here (tel2hin is a pure code-point shift and won't change).

CLI:
    # render each IAST line to Devanāgarī (eyeball, or diff against source):
    python verify.py --render < iast_lines.txt

    # line-aligned byte-exact comparison (one IAST line ↔ one source line):
    python verify.py --check iast_lines.txt source_devanagari.txt

Source lines may use the real daṇḍa (।/॥); post() maps ASCII |/|| to those, so
the comparison normalises the source's |/|| the same way before diffing.
"""
import sys
import re

HALANT = "్"
I_CONS2 = {"kh": "ఖ", "gh": "ఘ", "ch": "ఛ", "jh": "ఝ", "ṭh": "ఠ",
           "ḍh": "ఢ", "th": "థ", "dh": "ధ", "ph": "ఫ", "bh": "భ"}
I_CONS1 = {"k": "క", "g": "గ", "ṅ": "ఙ", "c": "చ", "j": "జ", "ñ": "ఞ",
           "ṭ": "ట", "ḍ": "డ", "ṇ": "ణ", "t": "త", "d": "ద", "n": "న",
           "p": "ప", "b": "బ", "m": "మ", "y": "య", "r": "ర", "l": "ల",
           "ḻ": "ళ", "v": "వ", "ś": "శ", "ṣ": "ష", "s": "స", "h": "హ"}
I_MATRA = {"a": "", "ā": "ా", "i": "ి", "ī": "ీ", "u": "ు", "ū": "ూ",
           "ṛ": "ృ", "ṝ": "ౄ", "ḷ": "ౢ", "ḹ": "ౣ", "e": "ే", "ē": "ే", "o": "ో", "ō": "ో"}
I_VOW = {"a": "అ", "ā": "ఆ", "i": "ఇ", "ī": "ఈ", "u": "ఉ", "ū": "ఊ",
         "ṛ": "ఋ", "ṝ": "ౠ", "ḷ": "ఌ", "ḹ": "ౡ", "e": "ఏ", "ē": "ఏ", "o": "ఓ", "ō": "ఓ"}
DIG_DEV = "०१२३४५६७८९"
AVA_DEV = "ऽ"
SVARA = {"_": "॒", "^": "॑"}


def _cons_at(s, j, n):
    if j >= n:
        return None
    if j + 1 < n and s[j:j+2] in I_CONS2:
        return s[j:j+2]
    if s[j] in I_CONS1:
        return s[j]
    return None


def iast2tel(frag):
    s = frag.lower()
    out = []
    i, n = 0, len(s)
    while i < n:
        c = _cons_at(s, i, n)
        if c:
            out.append(I_CONS2[c] if len(c) == 2 else I_CONS1[c])
            i += len(c)
            if i + 1 < n and s[i] == "a" and s[i+1] in ("i", "u"):
                out.append("ై" if s[i+1] == "i" else "ౌ"); i += 2
            elif i < n and s[i] in I_MATRA:
                out.append(I_MATRA[s[i]]); i += 1
            else:
                out.append(HALANT)
            continue
        if i + 1 < n and s[i] == "a" and s[i+1] in ("i", "u"):
            out.append("ఐ" if s[i+1] == "i" else "ఔ"); i += 2; continue
        if s[i] in I_VOW:
            out.append(I_VOW[s[i]]); i += 1; continue
        ch = s[i]
        if ch in ("ṁ", "ṃ"):
            out.append("ం")
        elif ch == "ḥ":
            out.append("ః")
        else:
            out.append(frag[i] if i < len(frag) else ch)
        i += 1
    return "".join(out)


def tel2hin(text):                       # Telugu block → Devanāgarī: -0x300
    return "".join(chr(ord(c) - 0x300) if 0x0C00 <= ord(c) <= 0x0C7F else c
                   for c in text)


def _prep(s):
    return s.replace("-", "").replace("ḷ", "ḻ")


def _post(s):
    s = s.replace("||", "॥").replace("|", "।").replace("'", AVA_DEV).replace("’", AVA_DEV)
    s = "".join(DIG_DEV[int(c)] if c.isdigit() else c for c in s)
    return re.sub(r'(^|[\s।॥])ओं(?=$|[\s।॥])', r'\1ॐ', s)   # standalone praṇava


def to_dev(iast):
    return _post(tel2hin(iast2tel(_prep(iast))))


def dev_svara(iast):
    """The accented render: markers _/^ sit after their vowel; reattach the
    Devanāgarī tone sign to the akṣara ending each chunk, then put a tone mark
    after any visarga/anusvāra (canonical order)."""
    out, last = "", 0
    for m in re.finditer(r"[_^]", iast):
        out += to_dev(iast[last:m.start()]) + SVARA[m.group()]
        last = m.end()
    out += to_dev(iast[last:])
    return re.sub(r"([॒॑])([ःం])", r"\2\1", out)


def _norm_src(s):
    return s.replace("||", "॥").replace("|", "।").strip()


def main(argv):
    if argv and argv[0] == "--check":
        iast = [l.rstrip("\n") for l in open(argv[1], encoding="utf-8") if l.strip()]
        src = [l.rstrip("\n") for l in open(argv[2], encoding="utf-8") if l.strip()]
        fails = 0
        for i, (a, s) in enumerate(zip(iast, src), 1):
            got, want = dev_svara(a.strip()), _norm_src(s)
            if got != want:
                fails += 1
                print(f"#{i} FAIL\n  iast: {a.strip()}\n  got:  {got}\n  src:  {want}")
        print(f"\nTOTAL {min(len(iast),len(src))}  PASS {min(len(iast),len(src))-fails}  FAIL {fails}")
        if len(iast) != len(src):
            print(f"WARNING: {len(iast)} iast lines vs {len(src)} source lines — check alignment.")
        sys.exit(1 if fails else 0)
    # default: --render
    for line in sys.stdin.read().splitlines():
        if line.strip():
            print(dev_svara(line.strip()))


if __name__ == "__main__":
    main(sys.argv[1:])
