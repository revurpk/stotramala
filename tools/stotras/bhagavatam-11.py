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
    "doc_title": "Pōtana Bhāgavatam · Skandha 11",
    "app_title": "Bhāgavatam 11",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 11 · contents · 127 verses in 1 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 10 · second part", "bhagavatam-10b-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 12 ›", "bhagavatam-12-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. VIII (Skandha 11 & 12), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1244, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–127", "bhagavatam-11-01-iast.html", "Parīkṣit's question to Śuka · Viśvāmitra, Vasiṣṭha, Nārada and other sages come to see Kṛṣṇa · Nārada tells Vasudeva the ancient dialogue of King Videha and the nine sages · Brahmā and the gods come to call Kṛṣṇa back to Vaikuṇṭha · Seeing ill omens, Kṛṣṇa sends the Yādavas from Dvārakā to Prabhāsa · Kṛṣṇa teaches Uddhava the highest truth · The avadhūta and King Yadu · Kṛṣṇa and Balarāma go to Vaikuṇṭha"),
    ]},
    ],
}
