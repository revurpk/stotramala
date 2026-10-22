# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by
# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.

def _v(padas, num, gloss=""):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ramayana",
    "doc_title": "Vālmīki Rāmāyaṇa",
    "app_title": "Vālmīki Rāmāyaṇa",
    "h1": "Vālmīki Rāmāyaṇa",
    "subtitle": "the seven kāṇḍas",
    "note": "Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. Verse numbers are the e-text's, sarga by sarga. Translations will follow.",
    "footer": "Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public domain), converted to IAST; repairs to the e-text's numbering are listed in SOURCES §5.25; translations original",
    "sections": [
    {"links": [
        ("Bālakāṇḍa", "ramayana-1-iast.html", "77 sargas · 17 pages"),
        ("Ayodhyākāṇḍa", "ramayana-2-iast.html", "78 sargas · 23 pages"),
        ("Araṇyakāṇḍa", "ramayana-3-iast.html", "73 sargas · 19 pages"),
        ("Kiṣkindhākāṇḍa", "ramayana-4-iast.html", "67 sargas · 20 pages"),
        ("Sundarakāṇḍa", "ramayana-5-iast.html", "68 sargas · 21 pages"),
        ("Yuddhakāṇḍa", "ramayana-6-iast.html", "128 sargas · 47 pages"),
        ("Uttarakāṇḍa", "ramayana-7-iast.html", "111 sargas · 27 pages"),
    ]},
    ],
}
