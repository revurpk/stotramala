#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devanāgarī → IAST for the stotramālā pipeline (the single source of truth
is IAST; Devanāgarī and Telugu are produced in the browser by teltools).

This is the converter that has been re-derived by hand several times — it is
bundled here so every run starts from the same vetted rules instead of
reinventing them. It is deliberately a *faithful* transcriber: it does not
"fix" the text. Any correction you make to the source belongs in a logged
editorial note in SOURCES.md, not silently here.

Encoding conventions (must match the render shell in the -iast.html pages):
  • Vedic svaras are marked RIGHT AFTER the vowel:  '_' = anudātta (U+0952),
    '^' = svarita (U+0951); udātta is unmarked. devSvara() in the page
    reattaches these to the correct akṣara, so placement matters.
  • anunāsika candrabindu (ँ, U+0901) → 'ṁ' (renders as anusvāra in Devanāgarī).
  • anusvāra (ं) → 'ṃ', visarga (ः) → 'ḥ', avagraha (ऽ) → "'".
  • pluta numerals (३ etc. inside a word) → ASCII digits, so they survive.
  • combining nukta / other marks are dropped (see D_STRIP).

CLI:
    python dev2iast.py < in.txt                 # convert each line
    python dev2iast.py --danda < in.txt         # also map । → | and ॥ → ||
    python dev2iast.py --samhita rv.txt         # pull accented saṃhitā ṛcs
                                                 #   from a Ṛgveda wikitext page
Modes print IAST you can paste into a tools/stotras/<slug>.py data file.
"""
import sys
import re

D_CONS = {"क":"k","ख":"kh","ग":"g","घ":"gh","ङ":"ṅ","च":"c","छ":"ch","ज":"j",
"झ":"jh","ञ":"ñ","ट":"ṭ","ठ":"ṭh","ड":"ḍ","ढ":"ḍh","ण":"ṇ","त":"t","थ":"th",
"द":"d","ध":"dh","न":"n","प":"p","फ":"ph","ब":"b","भ":"bh","म":"m","य":"y",
"र":"r","ल":"l","व":"v","श":"ś","ष":"ṣ","स":"s","ह":"h","ळ":"ḷ"}
D_MATRA = {"ा":"ā","ि":"i","ी":"ī","ु":"u","ू":"ū","ृ":"ṛ","ॄ":"ṝ","ॢ":"ḷ",
"े":"e","ै":"ai","ो":"o","ौ":"au"}
D_VOW = {"अ":"a","आ":"ā","इ":"i","ई":"ī","उ":"u","ऊ":"ū","ऋ":"ṛ","ॠ":"ṝ",
"ऌ":"ḷ","ए":"e","ऐ":"ai","ओ":"o","औ":"au"}
DIG = {"०":"0","१":"1","२":"2","३":"3","४":"4","५":"5","६":"6","७":"7","८":"8","९":"9"}
# candrabindu 0x900, nukta 0x93C, and the rarer 0x953/0x954/ZWNJ/ZWJ are dropped
D_STRIP = {0x900, 0x93C, 0x953, 0x954, 0x200C, 0x200D}


def dev2iast(s):
    out = []
    pending = False  # an unwritten inherent 'a' after a bare consonant
    for ch in s:
        cp = ord(ch)
        if cp in D_STRIP:
            continue
        if ch in D_CONS:
            if pending:
                out.append("a")
            out.append(D_CONS[ch]); pending = True
        elif cp == 0x94D:                 # virāma / halant: kill the inherent a
            pending = False
        elif ch in D_MATRA:
            out.append(D_MATRA[ch]); pending = False
        elif ch in D_VOW:
            if pending:
                out.append("a"); pending = False
            out.append(D_VOW[ch])
        elif ch in DIG:                   # pluta numeral inside a word → ASCII
            if pending:
                out.append("a"); pending = False
            out.append(DIG[ch])
        elif cp == 0x952:                 # anudātta ॒
            if pending:
                out.append("a"); pending = False
            out.append("_")
        elif cp == 0x951:                 # svarita ॑
            if pending:
                out.append("a"); pending = False
            out.append("^")
        elif cp == 0x901:                 # candrabindu / anunāsika ँ
            if pending:
                out.append("a"); pending = False
            out.append("ṁ")
        elif cp == 0x902:                 # anusvāra ं
            if pending:
                out.append("a"); pending = False
            out.append("ṃ")
        elif cp == 0x903:                 # visarga ः
            if pending:
                out.append("a"); pending = False
            out.append("ḥ")
        else:
            if pending:
                out.append("a"); pending = False
            out.append(ch)
    if pending:
        out.append("a")
    return "".join(out)


def conv(line, danda=False):
    """Convert one line; join line-break hyphens; normalise whitespace."""
    s = line.replace("-", "")            # source line-break hyphens mark sandhi
    t = dev2iast(s).replace("ऽ", "'")
    if danda:
        t = t.replace("॥", " || ").replace("।", " | ")
    return " ".join(t.split()).strip()


def extract_samhita(text):
    """Return the accented saṃhitā lines of a Ṛgveda wikitext page.

    Ṛgveda pages carry the accented text as pratīka lines (each ṛc is two
    lines ending । then ॥). Some pages (e.g. RV 1.1) interleave the padapāṭha
    right after each saṃhitā pair — keep only the pairs where (index//2) is
    even. Others (e.g. RV 10.90) list the saṃhitā contiguously. This returns
    the accent-bearing lines; eyeball the head of the list to confirm which
    layout you have before pairing them into ṛcs.
    """
    acc = [l.strip() for l in text.splitlines()
           if "॑" in l or "॒" in l]
    return acc


def main(argv):
    if argv and argv[0] == "--samhita":
        text = open(argv[1], encoding="utf-8").read()
        for i, l in enumerate(extract_samhita(text)):
            print(f"[{i}] {conv(l)}")
        return
    danda = bool(argv) and argv[0] == "--danda"
    for line in sys.stdin.read().splitlines():
        s = line.strip()
        if s:
            print(conv(s, danda=danda))


if __name__ == "__main__":
    main(sys.argv[1:])
