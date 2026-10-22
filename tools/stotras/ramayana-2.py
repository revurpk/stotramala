# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by
# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.

def _v(padas, num, gloss=""):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ramayana",
    "doc_title": "Vālmīki Rāmāyaṇa · Ayodhyākāṇḍa",
    "app_title": "Rāmāyaṇa 2",
    "h1": "Vālmīki Rāmāyaṇa",
    "subtitle": "Ayodhyākāṇḍa · contents · 78 sargas in 23 pages",
    "note": "Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. Verse numbers are the e-text's, sarga by sarga. Translations will follow. Sargas 48–88 are not yet included: the e-text gives them as a word-split reading aid, and they are being re-keyed from a printed edition.",
    "nav": [("‹ Bālakāṇḍa", "ramayana-1-iast.html"), ("all kāṇḍas", "ramayana-iast.html"), ("Araṇyakāṇḍa ›", "ramayana-3-iast.html")],
    "footer": "Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public domain), converted to IAST; repairs to the e-text's numbering are listed in SOURCES §5.25; translations original",
    "sections": [
    {"links": [
        ("1 · sargas 1–2", "ramayana-2-01-iast.html", "105 verses"),
        ("2 · sargas 3–6", "ramayana-2-02-iast.html", "148 verses"),
        ("3 · sargas 7–9", "ramayana-2-03-iast.html", "141 verses"),
        ("4 · sargas 10–11", "ramayana-2-04-iast.html", "69 verses"),
        ("5 · sargas 12–13", "ramayana-2-05-iast.html", "138 verses"),
        ("6 · sargas 14–15", "ramayana-2-06-iast.html", "117 verses"),
        ("7 · sargas 16–19", "ramayana-2-07-iast.html", "150 verses"),
        ("8 · sargas 20–22", "ramayana-2-08-iast.html", "149 verses"),
        ("9 · sargas 23–25", "ramayana-2-09-iast.html", "125 verses"),
        ("10 · sargas 26–29", "ramayana-2-10-iast.html", "112 verses"),
        ("11 · sargas 30–32", "ramayana-2-11-iast.html", "128 verses"),
        ("12 · sargas 33–35", "ramayana-2-12-iast.html", "129 verses"),
        ("13 · sargas 36–39", "ramayana-2-13-iast.html", "128 verses"),
        ("14 · sargas 40–43", "ramayana-2-14-iast.html", "128 verses"),
        ("15 · sargas 44–47", "ramayana-2-15-iast.html", "117 verses"),
        ("16 · sargas 89–91", "ramayana-2-16-iast.html", "129 verses"),
        ("17 · sargas 92–96", "ramayana-2-17-iast.html", "143 verses"),
        ("18 · sargas 97–99", "ramayana-2-18-iast.html", "91 verses"),
        ("19 · sargas 100–102", "ramayana-2-19-iast.html", "135 verses"),
        ("20 · sargas 103–106", "ramayana-2-20-iast.html", "140 verses"),
        ("21 · sargas 107–111", "ramayana-2-21-iast.html", "142 verses"),
        ("22 · sargas 112–116", "ramayana-2-22-iast.html", "140 verses"),
        ("23 · sargas 117–119", "ramayana-2-23-iast.html", "102 verses"),
    ]},
    ],
}
