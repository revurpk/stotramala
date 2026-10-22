# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by
# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.

def _v(padas, num, gloss=""):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ramayana",
    "doc_title": "Vālmīki Rāmāyaṇa · Bālakāṇḍa",
    "app_title": "Rāmāyaṇa 1",
    "h1": "Vālmīki Rāmāyaṇa",
    "subtitle": "Bālakāṇḍa · contents · 77 sargas in 17 pages",
    "note": "Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. Verse numbers are the e-text's, sarga by sarga. Translations will follow.",
    "nav": [("all kāṇḍas", "ramayana-iast.html"), ("Ayodhyākāṇḍa ›", "ramayana-2-iast.html")],
    "footer": "Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public domain), converted to IAST; repairs to the e-text (numbering, markup, typing slips) are listed in SOURCES §5.25; translations original",
    "sections": [
    {"links": [
        ("1 · sargas 1–2", "ramayana-1-01-iast.html", "143 verses"),
        ("2 · sargas 3–7", "ramayana-1-02-iast.html", "150 verses"),
        ("3 · sargas 8–12", "ramayana-1-03-iast.html", "130 verses"),
        ("4 · sargas 13–15", "ramayana-1-04-iast.html", "135 verses"),
        ("5 · sargas 16–19", "ramayana-1-05-iast.html", "150 verses"),
        ("6 · sargas 20–25", "ramayana-1-06-iast.html", "150 verses"),
        ("7 · sargas 26–30", "ramayana-1-07-iast.html", "144 verses"),
        ("8 · sargas 31–35", "ramayana-1-08-iast.html", "124 verses"),
        ("9 · sargas 36–40", "ramayana-1-09-iast.html", "139 verses"),
        ("10 · sargas 41–44", "ramayana-1-10-iast.html", "115 verses"),
        ("11 · sargas 45–49", "ramayana-1-11-iast.html", "145 verses"),
        ("12 · sargas 50–54", "ramayana-1-12-iast.html", "124 verses"),
        ("13 · sargas 55–59", "ramayana-1-13-iast.html", "120 verses"),
        ("14 · sargas 60–64", "ramayana-1-14-iast.html", "132 verses"),
        ("15 · sargas 65–69", "ramayana-1-15-iast.html", "131 verses"),
        ("16 · sargas 70–73", "ramayana-1-16-iast.html", "134 verses"),
        ("17 · sargas 74–77", "ramayana-1-17-iast.html", "105 verses"),
    ]},
    ],
}
