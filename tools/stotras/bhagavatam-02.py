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
    "doc_title": "Pōtana Bhāgavatam · Skandha 2",
    "app_title": "Bhāgavatam 2",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 2 · contents · 288 verses in 3 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 1", "bhagavatam-01-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 3 ›", "bhagavatam-03-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. I (Skandha 1 & 2), ed. Vidwan Mudivarthi Kondamacharyulu, T.T.D. Religious Publications Series No. 1237, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–112", "bhagavatam-02-01-iast.html", "Invocation · Śuka teaches Parīkṣit the way to liberation · Śuka shows that devotion is the chief way · Nārada asks Brahmā how the world came to be"),
        ("2 · verses 113–224", "bhagavatam-02-02-iast.html", "The playful avatāras of Nārāyaṇa · Parīkṣit asks Śuka how the world arose"),
        ("3 · verses 225–288", "bhagavatam-02-03-iast.html", "Pleased with Brahmā's austerity, Nārāyaṇa grants him boons"),
    ]},
    ],
}
