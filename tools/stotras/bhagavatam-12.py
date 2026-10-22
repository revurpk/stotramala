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
    "doc_title": "Pōtana Bhāgavatam · Skandha 12",
    "app_title": "Bhāgavatam 12",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 12 · contents · 54 verses in 1 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 11", "bhagavatam-11-iast.html"), ("all parts", "bhagavatam-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. VIII (Skandha 11 & 12), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1244, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–54", "bhagavatam-12-01-iast.html", "Invocation · Śuka tells Parīkṣit what the ages to come will bring · The dharma of the ages, and the four dissolutions · Parīkṣit dies of Takṣaka's bite; his son performs the serpent sacrifice · Vyāsa establishes the Vedas and the Purāṇas in the world · The story of Mārkaṇḍeya · The twelve Ādityas through the months from Caitra"),
    ]},
    ],
}
