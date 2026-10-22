# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by
# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.

def _v(padas, num, gloss=""):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ramayana",
    "doc_title": "Vālmīki Rāmāyaṇa · Araṇyakāṇḍa",
    "app_title": "Rāmāyaṇa 3",
    "h1": "Vālmīki Rāmāyaṇa",
    "subtitle": "Araṇyakāṇḍa · contents · 73 sargas in 19 pages",
    "note": "Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. Verse numbers are the e-text's, sarga by sarga. Translations will follow. Sargas 14–15 are not yet included: the e-text gives them as a word-split reading aid, and they are being re-keyed from a printed edition.",
    "nav": [("‹ Ayodhyākāṇḍa", "ramayana-2-iast.html"), ("all kāṇḍas", "ramayana-iast.html"), ("Kiṣkindhākāṇḍa ›", "ramayana-4-iast.html")],
    "footer": "Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public domain), converted to IAST; repairs to the e-text's numbering are listed in SOURCES §5.25; translations original",
    "sections": [
    {"links": [
        ("1 · sargas 1–4", "ramayana-3-01-iast.html", "109 verses"),
        ("2 · sargas 5–9", "ramayana-3-02-iast.html", "146 verses"),
        ("3 · sargas 10–11", "ramayana-3-03-iast.html", "116 verses"),
        ("4 · sargas 12–13", "ramayana-3-04-iast.html", "62 verses"),
        ("5 · sargas 16–20", "ramayana-3-05-iast.html", "142 verses"),
        ("6 · sargas 21–24", "ramayana-3-06-iast.html", "116 verses"),
        ("7 · sargas 25–28", "ramayana-3-07-iast.html", "138 verses"),
        ("8 · sargas 29–32", "ramayana-3-08-iast.html", "144 verses"),
        ("9 · sargas 33–37", "ramayana-3-09-iast.html", "141 verses"),
        ("10 · sargas 38–42", "ramayana-3-10-iast.html", "140 verses"),
        ("11 · sargas 43–45", "ramayana-3-11-iast.html", "118 verses"),
        ("12 · sargas 46–48", "ramayana-3-12-iast.html", "112 verses"),
        ("13 · sargas 49–51", "ramayana-3-13-iast.html", "114 verses"),
        ("14 · sargas 52–55", "ramayana-3-14-iast.html", "137 verses"),
        ("15 · sargas 56–59", "ramayana-3-15-iast.html", "132 verses"),
        ("16 · sargas 60–63", "ramayana-3-16-iast.html", "109 verses"),
        ("17 · sargas 64–67", "ramayana-3-17-iast.html", "143 verses"),
        ("18 · sargas 68–71", "ramayana-3-18-iast.html", "142 verses"),
        ("19 · sargas 72–75", "ramayana-3-19-iast.html", "138 verses"),
    ]},
    ],
}
