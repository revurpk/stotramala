#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Triage a stotra/sukta source and recommend a model + reasoning effort.

Run this FIRST, before any extraction. The categories differ enormously in
how much careful judgement the extraction and translation need, and picking
the model/effort up front is cheaper than discovering mid-way that a source
is a scanned PDF or a commentary-riddled mess. If you are not already running
under the recommended model, say so and let the user re-invoke before you do
the heavy work — don't quietly grind through a max-effort job on a small model.

    python triage.py <url-or-path>

It fetches (wiki pages are pulled as raw wikitext) or reads the source,
measures a few signals, and prints a category + (model, effort) + why.
Heuristics only — trust your eyes over the number if they disagree.
"""
import sys
import os
import re
import urllib.request
import urllib.parse


def fetch(src):
    if os.path.exists(src):
        with open(src, "rb") as f:
            return f.read(), src
    url = src
    # Wikisource: pull raw wikitext, and percent-encode the (often Devanāgarī,
    # space-bearing) title so urllib accepts it.
    if "wikisource.org" in url and "action=raw" not in url:
        if "/wiki/" in url:
            base, title = url.split("/wiki/", 1)
            q = urllib.parse.quote(title, safe="/")
            url = f"{base}/w/index.php?title={q}&action=raw"
        elif "title=" in url:
            head, title = url.split("title=", 1)
            title = title.split("&", 1)[0]
            q = urllib.parse.quote(title, safe="/")
            url = f"{head}title={q}&action=raw"
        else:
            url += ("&" if "?" in url else "?") + "action=raw"
    else:
        # encode any non-ASCII left in the path/query
        url = urllib.parse.quote(url, safe=":/?&=%#")
    req = urllib.request.Request(url, headers={"User-Agent": "stotramala-triage/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), url


def classify(raw):
    if raw[:4] == b"%PDF":
        return dict(cat="scanned-pdf", model="opus", effort="high",
                    signals={"format": "PDF"},
                    why="PDF: the text layer is often missing, English-only, or a "
                        "copyrighted edition. Devanāgarī usually needs OCR / visual "
                        "reading page by page — slow and error-prone, and it may carry "
                        "a redistribution caveat. Verify every verse.")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return dict(cat="binary/image", model="opus", effort="high",
                    signals={"format": "non-utf8 binary"},
                    why="Looks like an image or binary — plan on OCR / visual "
                        "transcription and heavy verification.")

    dev = len(re.findall(r"[ऀ-ॿ]", text))
    svara = len(re.findall(r"[॒॑]", text))
    poem = "<poem>" in text
    bhashya = len(re.findall(r"भाष्य|भाष्यम्|ऽभाष्य", text))
    # rough verse count: numbered daṇḍas ॥ १ ॥ etc., or plain ॥
    verses = len(re.findall(r"॥\s*[०-९]+", text)) or len(re.findall(r"॥", text)) // 2
    sig = {"devanāgarī chars": dev, "svara marks": svara, "<poem>": poem,
           "commentary markers": bhashya, "approx verses": verses,
           "size (chars)": len(text)}

    if dev < 40:
        return dict(cat="little-devanagari", model="opus", effort="high", signals=sig,
                    why="Barely any Devanāgarī — likely the wrong page, a stub, a "
                        "disambiguation/index page, or an English-only copy. Find the "
                        "real text before committing to a model.")
    # Check svaras BEFORE bhāṣya: an accented Ṛgveda page usually also carries
    # Sāyaṇa's commentary, but the saṃhitā is extracted by its svara-lines, so
    # the surrounding bhāṣya is irrelevant there. Only an UNACCENTED mūla that is
    # interleaved with bhāṣya (e.g. Taittirīya) needs the separation path.
    if svara >= 20:
        return dict(cat="accented-vedic", model="opus", effort="high", signals=sig,
                    why="Accented Vedic text. You must pull the saṃhitā out of the "
                        "pratīka/padapāṭha lines, carry svaras as _/^ after the vowel, "
                        "and round-trip byte-exact against the source. Precise, "
                        "judgement-heavy work — and the translations are usually the "
                        "harder, archaic kind.")
    if bhashya >= 3:
        return dict(cat="commentary-interleaved", model="opus", effort="high", signals=sig,
                    why="Unaccented mūla interleaved with commentary (bhāṣya). "
                        "Separating scripture from commentary across every anuvāka is "
                        "delicate — get it wrong and commentary bleeds into the text. "
                        "Consider finding a mūla-only source instead.")
    if len(text) > 6000 or verses > 30:
        return dict(cat="clean-but-large", model="opus", effort="medium", signals=sig,
                    why="Unaccented and reasonably clean, but long / many sections / "
                        "prose-mantra. The mechanics are easy; the volume of accurate, "
                        "original translation is what wants a stronger model.")
    return dict(cat="clean-stotra", model="sonnet", effort="medium", signals=sig,
                why="Clean, short, unaccented Wikisource stotra. Extraction is "
                    "mechanical (dev2iast + structure + build). Still write careful "
                    "original translations and verify the round-trip.")


def main(argv):
    if not argv:
        print(__doc__); sys.exit(1)
    raw, where = fetch(argv[0])
    r = classify(raw)
    print(f"SOURCE: {where}")
    for k, v in r["signals"].items():
        print(f"  {k}: {v}")
    print()
    print(f"CATEGORY:       {r['cat']}")
    print(f"RECOMMENDATION: model = {r['model']},  effort = {r['effort']}")
    print(f"WHY: {r['why']}")
    print()
    print("NEXT: if you are not already running under the recommended model, tell the "
          "user and let them re-invoke before the heavy extraction. Trust your eyes: "
          "if the text looks messier (OCR errors, odd conjuncts) than the numbers "
          "suggest, bump the effort up.")


if __name__ == "__main__":
    main(sys.argv[1:])
