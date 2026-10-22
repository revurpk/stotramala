# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by
# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.

def _v(padas, num, gloss=""):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ramayana",
    "doc_title": "Vālmīki Rāmāyaṇa · Sundarakāṇḍa",
    "app_title": "Rāmāyaṇa 5",
    "h1": "Vālmīki Rāmāyaṇa",
    "subtitle": "Sundarakāṇḍa · contents · 68 sargas in 21 pages",
    "note": "Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. Verse numbers are the e-text's, sarga by sarga. Translations will follow.",
    "nav": [("‹ Kiṣkindhākāṇḍa", "ramayana-4-iast.html"), ("all kāṇḍas", "ramayana-iast.html"), ("Yuddhakāṇḍa ›", "ramayana-6-iast.html")],
    "footer": "Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public domain), converted to IAST; repairs to the e-text (numbering, markup, typing slips) are listed in SOURCES §5.25; translations original",
    "sections": [
    {"links": [
        ("1 · sarga 1", "ramayana-5-01-iast.html", "213 verses"),
        ("2 · sargas 2–4", "ramayana-5-02-iast.html", "139 verses"),
        ("3 · sargas 5–8", "ramayana-5-03-iast.html", "96 verses"),
        ("4 · sargas 9–10", "ramayana-5-04-iast.html", "127 verses"),
        ("5 · sargas 11–13", "ramayana-5-05-iast.html", "142 verses"),
        ("6 · sargas 14–16", "ramayana-5-06-iast.html", "138 verses"),
        ("7 · sargas 17–20", "ramayana-5-07-iast.html", "122 verses"),
        ("8 · sargas 21–24", "ramayana-5-08-iast.html", "146 verses"),
        ("9 · sargas 25–29", "ramayana-5-09-iast.html", "150 verses"),
        ("10 · sargas 30–34", "ramayana-5-10-iast.html", "148 verses"),
        ("11 · sargas 35–36", "ramayana-5-11-iast.html", "137 verses"),
        ("12 · sargas 37–38", "ramayana-5-12-iast.html", "138 verses"),
        ("13 · sargas 39–42", "ramayana-5-13-iast.html", "144 verses"),
        ("14 · sargas 43–47", "ramayana-5-14-iast.html", "141 verses"),
        ("15 · sargas 48–51", "ramayana-5-15-iast.html", "145 verses"),
        ("16 · sargas 52–54", "ramayana-5-16-iast.html", "123 verses"),
        ("17 · sargas 55–57", "ramayana-5-17-iast.html", "139 verses"),
        ("18 · sarga 58", "ramayana-5-18-iast.html", "169 verses"),
        ("19 · sargas 59–63", "ramayana-5-19-iast.html", "147 verses"),
        ("20 · sargas 64–67", "ramayana-5-20-iast.html", "132 verses"),
        ("21 · sarga 68", "ramayana-5-21-iast.html", "29 verses"),
    ]},
    ],
}
