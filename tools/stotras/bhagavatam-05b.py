# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE work (src="tel"). Pōtana's Telugu Bhāgavatam, TTD edition;
# written by tools/bhagavatam/gen.py, now edited by hand. See SOURCES §6.12.

def _v(lines, num, prose=False, gloss="", words=None):
    v = {"padas": lines, "num": num, "gloss": gloss}
    if prose:
        v["prose"] = True
    if words:
        v["words"] = words
    return v


STOTRA = {
    "src": "tel",
    "deity": "bhagavatam",
    "doc_title": "Pōtana Bhāgavatam · Skandha 5 · second āśvāsa",
    "app_title": "Bhāgavatam 5.2",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 5 · second āśvāsa · contents · 168 verses in 2 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 5 · first āśvāsa", "bhagavatam-05a-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 6 ›", "bhagavatam-06-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. III (Skandha 4 & 5), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1239, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–76", "bhagavatam-05b-01-iast.html", "Invocation · Śuka describes the shape of the earth"),
        ("2 · verses 77–167", "bhagavatam-05b-02-iast.html", "The courses of the heavenly bodies · Śuka describes the hells to Parīkṣit"),
    ]},
    ],
}
