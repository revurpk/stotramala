# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by
# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.

def _v(padas, num, gloss=""):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ramayana",
    "doc_title": "Vālmīki Rāmāyaṇa · Kiṣkindhākāṇḍa",
    "app_title": "Rāmāyaṇa 4",
    "h1": "Vālmīki Rāmāyaṇa",
    "subtitle": "Kiṣkindhākāṇḍa · contents · 67 sargas in 20 pages",
    "note": "Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. Verse numbers are the e-text's, sarga by sarga. Translations will follow.",
    "nav": [("‹ Araṇyakāṇḍa", "ramayana-3-iast.html"), ("all kāṇḍas", "ramayana-iast.html"), ("Sundarakāṇḍa ›", "ramayana-5-iast.html")],
    "footer": "Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public domain), converted to IAST; repairs to the e-text's numbering are listed in SOURCES §5.25; translations original",
    "sections": [
    {"links": [
        ("1 · sarga 1", "ramayana-4-01-iast.html", "130 verses"),
        ("2 · sargas 2–5", "ramayana-4-02-iast.html", "134 verses"),
        ("3 · sargas 6–9", "ramayana-4-03-iast.html", "124 verses"),
        ("4 · sargas 10–11", "ramayana-4-04-iast.html", "128 verses"),
        ("5 · sargas 12–15", "ramayana-4-05-iast.html", "125 verses"),
        ("6 · sargas 16–17", "ramayana-4-06-iast.html", "93 verses"),
        ("7 · sargas 18–21", "ramayana-4-07-iast.html", "136 verses"),
        ("8 · sargas 22–24", "ramayana-4-08-iast.html", "106 verses"),
        ("9 · sargas 25–27", "ramayana-4-09-iast.html", "144 verses"),
        ("10 · sargas 28–29", "ramayana-4-10-iast.html", "99 verses"),
        ("11 · sargas 30–31", "ramayana-4-11-iast.html", "136 verses"),
        ("12 · sargas 32–36", "ramayana-4-12-iast.html", "150 verses"),
        ("13 · sargas 37–39", "ramayana-4-13-iast.html", "115 verses"),
        ("14 · sargas 40–41", "ramayana-4-14-iast.html", "120 verses"),
        ("15 · sargas 42–44", "ramayana-4-15-iast.html", "137 verses"),
        ("16 · sargas 45–50", "ramayana-4-16-iast.html", "142 verses"),
        ("17 · sargas 51–56", "ramayana-4-17-iast.html", "147 verses"),
        ("18 · sargas 57–62", "ramayana-4-18-iast.html", "137 verses"),
        ("19 · sargas 63–66", "ramayana-4-19-iast.html", "110 verses"),
        ("20 · sarga 67", "ramayana-4-20-iast.html", "49 verses"),
    ]},
    ],
}
