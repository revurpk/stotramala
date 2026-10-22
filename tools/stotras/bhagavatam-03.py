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
    "doc_title": "Pōtana Bhāgavatam · Skandha 3",
    "app_title": "Bhāgavatam 3",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 3 · contents · 1055 verses in 10 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 2", "bhagavatam-02-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 4 ›", "bhagavatam-04-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. II (Skandha 3), ed. Vidwan Mudivarthi Kondamacharyulu, T.T.D. Religious Publications Series No. 1238, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–113", "bhagavatam-03-01-iast.html", "Invocation · Vidura's pilgrimage · Vidura meets Uddhava and asks after Kṛṣṇa and his people"),
        ("2 · verses 114–202", "bhagavatam-03-02-iast.html", "Vidura and Maitreya converse"),
        ("3 · verses 203–295", "bhagavatam-03-03-iast.html", "A daṇḍaka to Hari; the unfolding of creation"),
        ("4 · verses 296–406", "bhagavatam-03-04-iast.html", "Svāyambhuva Manu multiplies the creatures"),
        ("5 · verses 407–501", "bhagavatam-03-05-iast.html", "The avatāra of Yajña-Varāha · Brahmā and the gods praise Yajña-Varāha · Maitreya tells Vidura of Hiraṇyākṣa and Hiraṇyakaśipu"),
        ("6 · verses 502–600", "bhagavatam-03-06-iast.html", "Sanaka, Sanandana and their brothers go to Vaikuṇṭha · Sanaka and his brothers praise Nārāyaṇa"),
        ("7 · verses 601–717", "bhagavatam-03-07-iast.html", "Jaya and Vijaya are born of Diti as Hiraṇyākṣa and Hiraṇyakaśipu · Hiraṇyākṣa fights Hari, the Boar of sacrifice"),
        ("8 · verses 718–835", "bhagavatam-03-08-iast.html", "Brahmā creates the yakṣas and other orders of beings · With the Lord's leave, Kardama marries Devahūti · Kardama makes a sky-chariot by yoga and roams with his wife"),
        ("9 · verses 836–950", "bhagavatam-03-09-iast.html", "Viṣṇu is born of Devahūti as Kapila · Devahūti learns the truth of things from her son Kapila"),
        ("10 · verses 951–1055", "bhagavatam-03-10-iast.html", "Kapila teaches Devahūti the yoga of devotion · Kapila tells Devahūti how the body forms in the womb · The soul in the womb praises the Lord"),
    ]},
    ],
}
