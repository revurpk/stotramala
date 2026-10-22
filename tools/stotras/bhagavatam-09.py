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
    "doc_title": "Pōtana Bhāgavatam · Skandha 9",
    "app_title": "Bhāgavatam 9",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 9 · contents · 737 verses in 8 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 8", "bhagavatam-08-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 10 · first part ›", "bhagavatam-10a-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. V (Skandha 8 & 9), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1241, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–80", "bhagavatam-09-01-iast.html", "Invocation · The line of Vaivasvata Manu"),
        ("2 · verses 81–155", "bhagavatam-09-02-iast.html", "The story of Ambarīṣa"),
        ("3 · verses 156–258", "bhagavatam-09-03-iast.html", "The glory of the Gaṅgā, flowing from Śiva's locks"),
        ("4 · verses 259–374", "bhagavatam-09-04-iast.html", "The story of Śrī Rāma · The kings to come"),
        ("5 · verses 375–428", "bhagavatam-09-05-iast.html", "The kings of the lunar line"),
        ("6 · verses 429–541", "bhagavatam-09-06-iast.html", "The story of Paraśurāma · The story of Yayāti · Devayānī chooses Yayāti"),
        ("7 · verses 542–642", "bhagavatam-09-07-iast.html", "Śukra curses Yayāti · Yayāti tells Devayānī his own story as the parable of the goat · The story of Bharata"),
        ("8 · verses 643–737", "bhagavatam-09-08-iast.html", "The story of Rantideva · The line of Yadu · The descendants of Vasudeva"),
    ]},
    ],
}
