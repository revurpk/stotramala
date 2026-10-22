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
    "doc_title": "Pōtana Bhāgavatam · Skandha 10 · first part",
    "app_title": "Bhāgavatam 10.1",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 10 · first part · contents · 1792 verses in 18 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 9", "bhagavatam-09-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 10 · second part ›", "bhagavatam-10b-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. VI (Skandha 10-1), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1242, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–104", "bhagavatam-10a-01-iast.html", "Parīkṣit's question to Śuka · Brahmā and the gods praise Kṛṣṇa in Devakī's womb"),
        ("2 · verses 105–210", "bhagavatam-10a-02-iast.html", "Kṛṣṇa is born · Devakī praises the Lord · The former lives of Devakī and Vasudeva"),
        ("3 · verses 211–306", "bhagavatam-10a-03-iast.html", "Sent by Kaṃsa, the demoness Pūtanā comes to Vraja · The child Kṛṣṇa kicks over the cart · Tṛṇāvarta, as a whirlwind, carries Kṛṣṇa off · The childhood games of Kṛṣṇa and Balarāma"),
        ("4 · verses 307–421", "bhagavatam-10a-04-iast.html", "The gopīs tell Yaśodā of Kṛṣṇa's mischief · Kṛṣṇa eats earth and shows the universe in his mouth · The former lives of Yaśodā and Nanda · Yaśodā catches Kṛṣṇa, who broke the curd-pot · Kṛṣṇa is tied to the mortar · Little Kṛṣṇa fells the twin arjuna trees"),
        ("5 · verses 422–500", "bhagavatam-10a-05-iast.html", "Nanda and the others move to Vṛndāvana · The killing of Vatsāsura · The killing of Bakāsura · Kṛṣṇa takes the cowherd boys to the forest for a picnic · The killing of Aghāsura · The cowherd boys share their meal with Kṛṣṇa"),
        ("6 · verses 501–610", "bhagavatam-10a-06-iast.html", "Brahmā hides the calves and the cowherd boys · Brahmā praises Kṛṣṇa"),
        ("7 · verses 611–725", "bhagavatam-10a-07-iast.html", "Balarāma kills Dhenuka, the ass-demon · Kṛṣṇa subdues Kāliya · Kāliya's wives praise Kṛṣṇa · The earlier story of Kāliya · A forest fire surrounds the cows, the cowherds and the gopīs · The hot season"),
        ("8 · verses 726–810", "bhagavatam-10a-08-iast.html", "Balarāma kills Pralamba · Kṛṣṇa swallows the forest fire and saves the herd · The rains · Autumn · The cold season"),
        ("9 · verses 811–912", "bhagavatam-10a-09-iast.html", "Kṛṣṇa takes the gopīs' clothes · The sages' wives bring food and feed Kṛṣṇa · Nanda and the others consult Kṛṣṇa about Indra's sacrifice"),
        ("10 · verses 913–966", "bhagavatam-10a-10-iast.html", "Kṛṣṇa lifts Govardhana · Kṛṣṇa brings Nanda back from Varuṇa's city"),
        ("11 · verses 967–1081", "bhagavatam-10a-11-iast.html", "Kṛṣṇa sings on an autumn night and the gopīs come · The songs of the gopīs"),
        ("12 · verses 1082–1188", "bhagavatam-10a-12-iast.html", "The rāsa dance · Play in the water · The gandharva Sudarśana, cursed into a serpent, is freed · Kṛṣṇa kills Śaṅkhacūḍa, a guhyaka in Kubera's service · The killing of Ariṣṭa, the bull-demon · Kṛṣṇa kills Keśī and Vyomāsura"),
        ("13 · verses 1189–1302", "bhagavatam-10a-13-iast.html", "Sent by Kaṃsa, Akrūra comes to Vṛndāvana · Akrūra sees Rāma and Kṛṣṇa in the Yamunā and praises them · Kṛṣṇa enters Mathurā · Kṛṣṇa kills the washerman and blesses the weaver and Sudāmā for their gifts · Sunset and moonrise"),
        ("14 · verses 1303–1388", "bhagavatam-10a-14-iast.html", "Sunrise · Kṛṣṇa kills the elephant Kuvalayāpīḍa · Kṛṣṇa and Balarāma kill Cāṇūra and Muṣṭika · Kṛṣṇa kills Kaṃsa"),
        ("15 · verses 1389–1506", "bhagavatam-10a-15-iast.html", "Kṛṣṇa frees Devakī and Vasudeva and crowns Ugrasena · Kṛṣṇa sends Uddhava to the gopīs · The songs to the bee · Kṛṣṇa goes with Uddhava to Kubjā's house"),
        ("16 · verses 1507–1615", "bhagavatam-10a-16-iast.html", "Kṛṣṇa sends Akrūra to Hastināpura · Akrūra counsels Dhṛtarāṣṭra · Jarāsandha marches on Mathurā and fights Kṛṣṇa · Kālayavana besieges Mathurā · At Kṛṣṇa's command Viśvakarmā builds Dvārakā in the sea"),
        ("17 · verses 1616–1714", "bhagavatam-10a-17-iast.html", "Unarmed, Kṛṣṇa runs, with Kālayavana in pursuit · The earlier story of Mucukunda · Mucukunda's hymn to Kṛṣṇa · Jarāsandha burns Mount Pravarṣaṇa · The tale of Rukmiṇī's wedding begins"),
        ("18 · verses 1715–1792", "bhagavatam-10a-18-iast.html", "Kṛṣṇa sets out by chariot for Kuṇḍina · Rukmiṇī bows to Agnidyotana, the brāhmaṇa messenger · Kṛṣṇa carries off Rukmiṇī as the enemy kings look on · Balabhadra consoles Rukmiṇī, grieving at her brother's humbling · Kṛṣṇa weds Rukmiṇī"),
    ]},
    ],
}
