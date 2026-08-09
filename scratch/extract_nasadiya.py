#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0, ".claude/skills/add-stotra/scripts")
from dev2iast import conv, extract_samhita

text = open("scratch/rv10129.txt", encoding="utf-8").read()
acc = extract_samhita(text)
# padapatha-interleaved: keep pairs where pair-index (i//2) is even
samhita_lines = [acc[i] for i in range(len(acc)) if (i // 2) % 2 == 0]
assert len(samhita_lines) == 14, len(samhita_lines)

for vi in range(7):
    a_raw = samhita_lines[2*vi]
    b_raw = samhita_lines[2*vi + 1]
    a = conv(a_raw)
    b = conv(b_raw)
    # strip trailing single danda on a-line, add explicit " |"
    a = re.sub(r"।\s*$", "", a).strip()
    # strip trailing double danda + verse number on b-line
    b = re.sub(r"॥\s*[0-9]+\s*$", "", b).strip()
    print(f"--- verse {vi+1} ---")
    print(repr(a_raw))
    print(repr(b_raw))
    print(f'"{a} |",')
    print(f'"{b}"')
    print()
