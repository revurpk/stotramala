#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diff a built data file's text against its SOURCE, with the site's
orthographic conventions erased, so what remains is exactly the list of
textual changes to log in SOURCES.md (or to revert).

WHY THIS EXISTS: verify.py proves the page RENDERS the IAST correctly; it
cannot see whether the IAST still says what the source says. When a text is
re-set by hand (word division re-done, labels dropped, tables re-ordered,
typos fixed), drift creeps in — a word "standardised" that the source never
had, a half-line added or lost. This diff surfaces every such change.

Erased before diffing (conventions, not text): spacing and punctuation;
daṇḍas and digits; the anusvāra / class-nasal distinction (gaṃdha = gandha);
ḷ vs l; avagraha; the labels ślo|| / maṃ||.

    python srcdiff.py <slug> <source.iast.txt> [--from N] [--to N]
                      [--skip PREFIX]... [--rows]

<source.iast.txt> is extract_doc.py's output (or any UTF-8 IAST text, one
paragraph per line). --from/--to limit it to a paragraph-number range;
--skip drops paragraphs starting with PREFIX (e.g. --skip "tā||" for Telugu
tātparya); tables are compared in their column-major reading unless --rows.

Each op prints `…context[source] -> [data file]`. Read them all: every
one is a convention you missed, a logged emendation, an intended omission
(Telugu prose, labels), a table re-ordering — or a mistake to revert.
"""
import difflib
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]


def load_padas(slug):
    path = ROOT / "tools" / "stotras" / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return " ".join(p for s in m.STOTRA["sections"]
                    if isinstance(s, dict) and "padas" in s for p in s["padas"])


def load_source(path, lo, hi, skips, rows):
    out, cur = [], -1                              # cur: last paragraph number seen
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        key, _, text = line.partition("\t")
        if not text:                               # plain text file
            key, text = "", line
        if key.isdigit():
            cur = int(key)
        pos = cur + 0.5 if key.startswith("T") else cur   # a table sits after `cur`
        if key and not (lo <= pos <= hi):
            continue
        if key.startswith("T"):
            if text.startswith("table "):
                continue
            if rows != text.startswith("row "):     # keep rows XOR cols
                continue
            text = re.sub(r"^(row \d+|cols):", "", text).replace(" · ", " ").replace(" | ", " ")
        if any(text.startswith(p) for p in skips):
            continue
        out.append(text)
    return " ".join(out)


def norm(s):
    s = s.replace("ḷ", "l").replace("'", "").replace("’", "")
    s = re.sub(r"(ślo|maṃ)\|\|", "", s)
    s = re.sub(r"[ṅñṇnm](?=[kgcjṭḍtdpbh]|\s|$)", "ṃ", s)
    s = re.sub(r"[\s|\-–—:.,;!?\"“”‘()\[\]…0-9·]+", "", s)
    return s


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    slug, src = argv[0], argv[1]
    lo = int(argv[argv.index("--from") + 1]) if "--from" in argv else 0
    hi = int(argv[argv.index("--to") + 1]) if "--to" in argv else 10**9
    skips = [argv[i + 1] for i, a in enumerate(argv) if a == "--skip"]
    a = norm(load_source(src, lo, hi, skips, "--rows" in argv))
    b = norm(load_padas(slug))
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    sys.stdout.reconfigure(encoding="utf-8")
    n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            n += 1
            print(f"{op:7} …{a[max(0, i1 - 18):i1]}[{a[i1:i2]}] -> [{b[j1:j2]}]")
    print(f"ratio {sm.ratio():.4f}  ops {n}")


if __name__ == "__main__":
    main(sys.argv[1:])
