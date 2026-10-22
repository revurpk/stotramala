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
    "doc_title": "Pōtana Bhāgavatam",
    "app_title": "Pōtana Bhāgavatam",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Śrī Mahābhāgavatamu · the twelve skandhas in Telugu",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow. Two episodes also have pages of their own, with translations: Gajendra Mokṣam and Rukmiṇī Kalyāṇam.",
    "nav": [("Gajendra Mokṣam", "../vishnu/gajendra-moksham-iast.html"), ("Rukmiṇī Kalyāṇam", "../vishnu/rukmini-kalyanam-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vols. I–VIII, T.T.D. Religious Publications Series Nos. 1237–1244, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("Skandha 1", "bhagavatam-01-iast.html", "529 verses · 5 pages"),
        ("Skandha 2", "bhagavatam-02-iast.html", "288 verses · 3 pages"),
        ("Skandha 3", "bhagavatam-03-iast.html", "1,055 verses · 10 pages"),
        ("Skandha 4", "bhagavatam-04-iast.html", "977 verses · 11 pages"),
        ("Skandha 5 · first āśvāsa", "bhagavatam-05a-iast.html", "184 verses · 2 pages"),
        ("Skandha 5 · second āśvāsa", "bhagavatam-05b-iast.html", "168 verses · 2 pages"),
        ("Skandha 6", "bhagavatam-06-iast.html", "530 verses · 7 pages"),
        ("Skandha 7", "bhagavatam-07-iast.html", "482 verses · 5 pages"),
        ("Skandha 8", "bhagavatam-08-iast.html", "744 verses · 9 pages"),
        ("Skandha 9", "bhagavatam-09-iast.html", "737 verses · 8 pages"),
        ("Skandha 10 · first part", "bhagavatam-10a-iast.html", "1,792 verses · 18 pages"),
        ("Skandha 10 · second part", "bhagavatam-10b-iast.html", "1,343 verses · 13 pages"),
        ("Skandha 11", "bhagavatam-11-iast.html", "127 verses · 1 page"),
        ("Skandha 12", "bhagavatam-12-iast.html", "54 verses · 1 page"),
    ]},
    ],
}
