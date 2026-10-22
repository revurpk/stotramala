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
    "doc_title": "Pōtana Bhāgavatam · Skandha 6",
    "app_title": "Bhāgavatam 6",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 6 · contents · 530 verses in 7 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 5 · second āśvāsa", "bhagavatam-05b-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 7 ›", "bhagavatam-07-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. IV (Skandha 6 & 7), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1240, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–74", "bhagavatam-06-01-iast.html", "Invocation · Dedicatory verses · The story begins · The story of Ajāmila"),
        ("2 · verses 75–143", "bhagavatam-06-02-iast.html", "The messengers of Viṣṇu and of Yama debate"),
        ("3 · verses 144–251", "bhagavatam-06-03-iast.html", "Dakṣa's hymn, the Haṃsaguhya · Nārada teaches the Śabalāśvas the path of withdrawal"),
        ("4 · verses 252–316", "bhagavatam-06-04-iast.html", "Dakṣa curses Nārada and peoples the world · The war of the gods and asuras begins · The Nārāyaṇa Kavaca"),
        ("5 · verses 317–379", "bhagavatam-06-05-iast.html", "The story of Vṛtra"),
        ("6 · verses 380–485", "bhagavatam-06-06-iast.html", "The story of Citraketu · Citraketu's austerities win the Lord's grace"),
        ("7 · verses 486–530", "bhagavatam-06-07-iast.html", "For slighting Śiva, Citraketu is cursed by Gaurī · The line of Savitṛ, and other stories"),
    ]},
    ],
}
