#!/usr/bin/env python3
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Regenerate the embedded Baloo Tammudu 2 Telugu subset.

The Telugu script on stotra/durga-saptashloki-iast.html is set in
Baloo Tammudu 2 (SIL OFL 1.1), embedded as a base64 woff2 so the page
stays self-contained and offline. This script fetches a fresh subset
from Google Fonts and rewrites the @font-face `src:` in place.

It subsets to a fixed, comprehensive *Sanskrit-in-Telugu* character set
— every Telugu consonant, vowel, sign, mark, and digit that Sanskrit
uses, plus the daṇḍas — so the embed covers any verse this repository
might render, now or later, without having to run the transliterator.

Usage (needs only the Python standard library and network access):

    python tools/regen-telugu-font.py

Re-run after adding stotras, or to pull a newer version of the font.
The change it makes is a new base64 blob inside the one @font-face rule;
review the diff and the rendered Telugu before committing.
"""

import base64
import pathlib
import re
import sys
import urllib.parse
import urllib.request

FAMILY = "Baloo Tammudu 2"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

PAGE = pathlib.Path(__file__).resolve().parent.parent / "stotra" / "durga-saptashloki-iast.html"


def sanskrit_telugu_chars():
    """Every Telugu codepoint Sanskrit needs, plus space and daṇḍas.
    Unassigned codepoints in a range are harmless — the subsetter drops
    them."""
    cps = set()
    cps.update(range(0x0C01, 0x0C04))   # candrabindu, anusvāra, visarga
    cps.update(range(0x0C05, 0x0C15))   # independent vowels a … au
    cps.add(0x0C3D)                     # avagraha
    cps.update(range(0x0C3E, 0x0C4D))   # vowel signs (mātrās)
    cps.add(0x0C4D)                     # virāma
    cps.update(range(0x0C15, 0x0C3A))   # consonants ka … ḷa/ḻa
    cps.update(range(0x0C60, 0x0C64))   # vocalic RR, LL and their signs
    cps.update(range(0x0C66, 0x0C70))   # Telugu digits 0–9
    cps.update((0x20, 0x0964, 0x0965))  # space and the two daṇḍas
    return "".join(chr(c) for c in sorted(cps))


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    text = sanskrit_telugu_chars()
    css_url = ("https://fonts.googleapis.com/css2?family="
               + urllib.parse.quote(FAMILY.replace(" ", "+"), safe="+")
               + "&text=" + urllib.parse.quote(text, safe=""))

    print(f"requesting {len(text)} glyphs of “{FAMILY}” …")
    css = fetch(css_url).decode("utf-8")

    m = re.search(r"url\((https://fonts\.gstatic\.com/[^)]+)\)\s*format\('woff2'\)", css)
    if not m:
        sys.exit("could not find a woff2 URL in the Google Fonts CSS:\n" + css)

    woff2 = fetch(m.group(1))
    if woff2[:4] != b"wOF2":
        sys.exit("downloaded file is not a woff2 (bad magic)")
    b64 = base64.b64encode(woff2).decode("ascii")
    print(f"woff2 {len(woff2):,} bytes  →  base64 {len(b64):,} chars")

    html = PAGE.read_text(encoding="utf-8")
    src_re = re.compile(r"(src:url\(data:font/woff2;base64,)[^)]*(\) format\(\"woff2\"\);)")
    if not src_re.search(html):
        sys.exit(f"no embedded @font-face src found in {PAGE.name}")
    new_html, n = src_re.subn(lambda mm: mm.group(1) + b64 + mm.group(2), html, count=1)
    if n != 1:
        sys.exit(f"expected exactly one @font-face src, replaced {n}")

    PAGE.write_text(new_html, encoding="utf-8", newline="\n")
    print(f"updated {PAGE.name}  ({len(new_html.encode('utf-8')):,} bytes)")


if __name__ == "__main__":
    main()
