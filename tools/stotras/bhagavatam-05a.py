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
    "doc_title": "Pōtana Bhāgavatam · Skandha 5 · first āśvāsa",
    "app_title": "Bhāgavatam 5.1",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 5 · first āśvāsa · contents · 184 verses in 2 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 4", "bhagavatam-04-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 5 · second āśvāsa ›", "bhagavatam-05b-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. III (Skandha 4 & 5), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1239, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–91", "bhagavatam-05a-01-iast.html", "Invocation · The story of Priyavrata · Nārāyaṇa takes birth as Ṛṣabha · Ṛṣabha counsels his sons"),
        ("2 · verses 92–184", "bhagavatam-05a-02-iast.html", "The story of Bharata · A robber king's servants carry Bharata off as an offering to Kālī · Bharata answers King Rahūgaṇa"),
    ]},
    ],
}
