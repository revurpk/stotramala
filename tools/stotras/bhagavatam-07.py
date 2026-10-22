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
    "doc_title": "Pōtana Bhāgavatam · Skandha 7",
    "app_title": "Bhāgavatam 7",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 7 · contents · 482 verses in 5 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 6", "bhagavatam-06-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 8 ›", "bhagavatam-08-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. IV (Skandha 6 & 7), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1240, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–114", "bhagavatam-07-01-iast.html", "Invocation · Parīkṣit asks why Nārāyaṇa is hostile to the asuras · Sanaka and his brothers curse Hari's door-keepers · Yama, as a boy, tells the story of Suyajña · Brahmā grants boons to Hiraṇyakaśipu"),
        ("2 · verses 115–206", "bhagavatam-07-02-iast.html", "The story of Prahlāda"),
        ("3 · verses 207–298", "bhagavatam-07-03-iast.html", "The story of Prahlāda (continued)"),
        ("4 · verses 299–390", "bhagavatam-07-04-iast.html", "The story of Prahlāda (continued)"),
        ("5 · verses 391–482", "bhagavatam-07-05-iast.html", "The story of Prahlāda (continued)"),
    ]},
    ],
}
