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
    "doc_title": "Pōtana Bhāgavatam · Skandha 8",
    "app_title": "Bhāgavatam 8",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 8 · contents · 744 verses in 9 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 7", "bhagavatam-07-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 9 ›", "bhagavatam-09-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. V (Skandha 8 & 9), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1241, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–79", "bhagavatam-08-01-iast.html", "Invocation · The deliverance of Gajendra"),
        ("2 · verses 80–141", "bhagavatam-08-02-iast.html", "The deliverance of Gajendra (continued)"),
        ("3 · verses 142–251", "bhagavatam-08-03-iast.html", "The churning of the ocean of milk begins · The tortoise avatāra · At the gods' plea, Śiva drinks the hālāhala poison"),
        ("4 · verses 252–325", "bhagavatam-08-04-iast.html", "Airāvata and other treasures rise from the churned ocean · Viṣṇu takes the form of Mohinī"),
        ("5 · verses 326–435", "bhagavatam-08-05-iast.html", "The war of the gods and asuras · With his Mohinī form Hari enchants Śiva"),
        ("6 · verses 436–519", "bhagavatam-08-06-iast.html", "The story of Vāmana begins · Vāmana appears"),
        ("7 · verses 520–619", "bhagavatam-08-07-iast.html", "Vāmana comes to Bali"),
        ("8 · verses 620–689", "bhagavatam-08-08-iast.html", "Vāmana takes the cosmic form and strides out"),
        ("9 · verses 690–744", "bhagavatam-08-09-iast.html", "The fish avatāra"),
    ]},
    ],
}
