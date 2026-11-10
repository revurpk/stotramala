# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Fetch page images of the 1882 print (archive.org 20231127_20231127_1402, public
domain) for collation, one JPEG a leaf, politely and cached. Leaf numbers are the
scan's (n0 = the first image), as in the OCR. Nothing fetched is committed.
usage: leaf.py OUTDIR LEAF [LEAF …] [--w 1200]
"""
import pathlib, sys, time, urllib.request

ITEM = "20231127_20231127_1402"
UA = {"User-Agent": "stotramala-source/1.0 (personal research; https://github.com/revurpk/stotramala)"}
args = sys.argv[1:]
w = int(args[args.index("--w") + 1]) if "--w" in args else 1200
if "--w" in args:
    i = args.index("--w"); del args[i:i + 2]
out = pathlib.Path(args[0]); out.mkdir(parents=True, exist_ok=True)
for p in args[1:]:
    f = out / f"n{int(p):03d}-{w}.jpg"
    if not f.exists():
        # the plain page endpoint (the IIIF one times out)
        url = f"https://archive.org/download/{ITEM}/page/n{int(p)}_w{w}.jpg"
        for k in range(5):
            try:
                f.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read())
                break
            except Exception as e:
                print("retry", p, e, file=sys.stderr); time.sleep(10 * (k + 1))
        time.sleep(1.5)
    print(f)
