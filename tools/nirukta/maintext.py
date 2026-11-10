# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Crop the main text of a page of Sarup's 1927 Nirukta: the Sanskrit text sits above a
long horizontal rule, the footnotes below it. Find the rule (the first row, below the
running head, where most of the width is ink) and keep what lies above it (running head included). Needs Pillow.
usage: maintext.py IN.jpg OUT.png [--thresh 145]
"""
import sys
from PIL import Image, ImageFilter, ImageOps

a = sys.argv[1:]
t = int(a[a.index("--thresh") + 1]) if "--thresh" in a else 145
im = ImageOps.grayscale(Image.open(a[0]))
w, h = im.size
small = im.resize((w // 4, h // 4))
sw, sh = small.size
px = small.load()


# the rule: a row with a long unbroken run of ink (allowing a slight tilt: a pixel counts
# if any of three rows is dark there), below the top 10% of the page
rule = None
for y in range(int(sh * 0.10), int(sh * 0.98) - 3):
    run = best = 0
    for x in range(sw):
        run = run + 1 if min(px[x, y + k] for k in range(3)) < 150 else 0
        best = max(best, run)
    if best > sw * 0.4:
        rule = y
        break
bottom = (rule * 4 - 6) if rule else h
# keep the running head: telling it from a first line of text set close under it is
# not reliable, and it is easily skipped when reading
top = 0
crop = im.crop((0, top, w, bottom))
crop = crop.filter(ImageFilter.MedianFilter(3)).point(lambda p: 255 if p > t else 0, "1")
crop.save(a[1])
print(f"{a[0]}: rule {'at ' + str(bottom) if rule else 'not found'}, head to {top}")
