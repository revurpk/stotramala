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
    "doc_title": "Pōtana Bhāgavatam · Skandha 1",
    "app_title": "Bhāgavatam 1",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 1 · contents · 529 verses in 5 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("all parts", "bhagavatam-iast.html"), ("Skandha 2 ›", "bhagavatam-02-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. I (Skandha 1 & 2), ed. Vidwan Mudivarthi Kondamacharyulu, T.T.D. Religious Publications Series No. 1237, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–102", "bhagavatam-01-01-iast.html", "Invocation · The work is dedicated to Śrī Rāma · The poet's family · Dedicatory verses · The story begins · The questions of Śaunaka and the sages · Sūta praises the stories of Nārāyaṇa · The twenty-one avatāras of the Lord · Vyāsa, troubled in mind, reflects · Nārada comes to Vyāsa"),
        ("2 · verses 103–217", "bhagavatam-01-02-iast.html", "Nārada's former life · Arjuna humbles Aśvatthāmā, slayer of the children · Draupadī sees Aśvatthāmā and speaks · Kṛṣṇa shields the child in Uttarā's womb with his discus · Kuntī's praise of Kṛṣṇa · Dharmarāja goes with Kṛṣṇa to Bhīṣma"),
        ("3 · verses 218–336", "bhagavatam-01-03-iast.html", "Bhīṣma's praise of Kṛṣṇa · Kṛṣṇa sets out for Dvārakā · Kṛṣṇa enters Dvārakā · Kṛṣṇa visits the women of his household · Parīkṣit is born to Uttarā · Gāndhārī and Dhṛtarāṣṭra give up their bodies · Dharmarāja is troubled by ill omens"),
        ("4 · verses 337–455", "bhagavatam-01-04-iast.html", "Dharmarāja tells Bhīma of the portents · Arjuna returns from Dvārakā with news of Kṛṣṇa's passing · Dharmarāja crowns Parīkṣit and sets out on the great journey · Parīkṣit overhears the Earth and Dharma · Kali kicks Dharma · Parīkṣit subdues Kali and rules by dharma"),
        ("5 · verses 456–529", "bhagavatam-01-05-iast.html", "Out hunting, Parīkṣit drapes a dead snake on Śamīka · Śṛṅgi, Śamīka's son, curses Parīkṣit · Learning of the curse, Parīkṣit sits to fast unto death · Śuka comes to Parīkṣit"),
    ]},
    ],
}
