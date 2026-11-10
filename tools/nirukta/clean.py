# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Clean a page image of Sarup's 1927 Nirukta for OCR: the scan is grainy, so
median-filter the speckle away, then threshold. Needs Pillow.
usage: clean.py IN.jpg OUT.png [--median 3] [--thresh 150] [--scale 1.0]
"""
import sys
from PIL import Image, ImageFilter, ImageOps
a = sys.argv[1:]
opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
im = ImageOps.grayscale(Image.open(a[0]))
s = opt("--scale", 1.0)
if s != 1.0:
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
m = opt("--median", 3)
if m > 1:
    im = im.filter(ImageFilter.MedianFilter(m))
t = opt("--thresh", 150)
im = im.point(lambda p: 255 if p > t else 0, "1")
im.save(a[1])
