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
    "doc_title": "Pōtana Bhāgavatam · Skandha 4",
    "app_title": "Bhāgavatam 4",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 4 · contents · 977 verses in 11 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 3", "bhagavatam-03-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 5 · first āśvāsa ›", "bhagavatam-05a-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. III (Skandha 4 & 5), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1239, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–106", "bhagavatam-04-01-iast.html", "Invocation · Maitreya tells Vidura the lines of Svāyambhuva Manu's daughters · Kardama's descendants · Dakṣa's descendants · Enmity arises between Śiva and Dakṣa · Satī goes to Dakṣa's sacrifice"),
        ("2 · verses 107–215", "bhagavatam-04-02-iast.html", "Śiva has Vīrabhadra destroy Dakṣa's sacrifice · Routed by Vīrabhadra, the gods appeal to Brahmā · Brahmā and the gods praise Śiva as Dakṣiṇāmūrti · Entreated, Śiva shows grace to Dakṣa and the rest · Dakṣa and the others praise Viṣṇu"),
        ("3 · verses 216–322", "bhagavatam-04-03-iast.html", "The story of Dhruva · Taught by Nārada, Dhruva performs austerities · Dhruva praises the Lord who appears before him · Dhruva returns to his city"),
        ("4 · verses 323–393", "bhagavatam-04-04-iast.html", "Dhruva fights the guhyakas, Kubera's followers"),
        ("5 · verses 394–508", "bhagavatam-04-05-iast.html", "The story of Vena, son of Aṅga · Emperor Pṛthu milks the herbs from the Earth in the form of a cow"),
        ("6 · verses 509–597", "bhagavatam-04-06-iast.html", "Indra steals the horse at Pṛthu's aśvamedha · Nārāyaṇa, pleased, blesses Pṛthu · Pṛthu teaches dharma to his court and praises the brāhmaṇas"),
        ("7 · verses 598–685", "bhagavatam-04-07-iast.html", "Sanaka and his brothers come to Pṛthu · Pṛthu, wise and detached, attains liberation"),
        ("8 · verses 686–741", "bhagavatam-04-08-iast.html", "Rudra teaches the Pracetases a hymn of yoga · Nārada leads Prācīnabarhi to the path of knowledge"),
        ("9 · verses 742–819", "bhagavatam-04-09-iast.html", "The parable of Purañjana"),
        ("10 · verses 820–896", "bhagavatam-04-10-iast.html", "The parable of Purañjana (continued)"),
        ("11 · verses 897–977", "bhagavatam-04-11-iast.html", "Pleased with the Pracetases' austerity, the Lord grants them boons"),
    ]},
    ],
}
