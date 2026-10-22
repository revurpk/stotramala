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
    "doc_title": "Pōtana Bhāgavatam · Skandha 10 · second part",
    "app_title": "Bhāgavatam 10.2",
    "h1": "Pōtana Bhāgavatam",
    "subtitle": "Skandha 10 · second part · contents · 1343 verses in 13 pages",
    "note": "Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati Devasthanams. The Telugu is the source; the IAST is a reading aid. Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. vacanam …) and line breaks. Translations will follow.",
    "nav": [("‹ Skandha 10 · first part", "bhagavatam-10a-iast.html"), ("all parts", "bhagavatam-iast.html"), ("Skandha 11 ›", "bhagavatam-11-iast.html")],
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, Vol. VII (Skandha 10-2), ed. Dr. Samudrala Lakshmanaiah, T.T.D. Religious Publications Series No. 1243, Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only (public domain); the edition's commentary is not reproduced; section headings and translations original",
    "sections": [
    {"links": [
        ("1 · verses 1–102", "bhagavatam-10b-01-iast.html", "Invocation · The story of Pradyumna begins · Rati carries Pradyumna through the sky to Dvārakā · To clear his name, Kṛṣṇa recovers the Syamantaka jewel · Śatadhanvā kills Satrājit and steals the jewel"),
        ("2 · verses 103–205", "bhagavatam-10b-02-iast.html", "Kṛṣṇa goes to Indraprastha · Kṛṣṇa weds Kālindī, Mitravindā, Nāgnajitī, Bhadrā and Lakṣaṇā · Kṛṣṇa goes with Satyabhāmā and kills Naraka · Satyabhāmā fights Naraka · Bhūdevī praises Kṛṣṇa"),
        ("3 · verses 206–310", "bhagavatam-10b-03-iast.html", "Kṛṣṇa weds the sixteen thousand maidens and brings the pārijāta from heaven · Kṛṣṇa teases Rukmiṇī in the pleasure-house · Caressed by Kṛṣṇa, Rukmiṇī praises him · Kṛṣṇa consoles Rukmiṇī · At Aniruddha's wedding Balarāma kills Rukmī and others"),
        ("4 · verses 311–401", "bhagavatam-10b-04-iast.html", "Bāṇa wins Śiva's favour · Bāṇa binds Aniruddha with the serpent-noose · Told by Nārada, Kṛṣṇa marches on Bāṇa"),
        ("5 · verses 402–507", "bhagavatam-10b-05-iast.html", "Kṛṣṇa fights Śiva, Bāṇa's ally · Bāṇa returns to battle · Śiva praises Kṛṣṇa to save Bāṇa · Kṛṣṇa returns to Dvārakā with Uṣā and Aniruddha · The story of King Nṛga · Balarāma visits Vraja to see his friends and kin"),
        ("6 · verses 508–597", "bhagavatam-10b-06-iast.html", "Kṛṣṇa marches on Pauṇḍraka Vāsudeva and kills him · Balarāma sets out to drag Hastināpura into the Gaṅgā"),
        ("7 · verses 598–716", "bhagavatam-10b-07-iast.html", "Nārada sees Kṛṣṇa's glory among his sixteen thousand wives · Nārada urges Kṛṣṇa to see Dharmarāja's rājasūya through · On Uddhava's advice Kṛṣṇa goes to Dharmarāja · The Pāṇḍavas go out to meet Kṛṣṇa · With Kṛṣṇa's consent Dharmarāja sends Bhīma and the others to conquer the quarters"),
        ("8 · verses 717–830", "bhagavatam-10b-08-iast.html", "Kṛṣṇa, Bhīma and Arjuna set out to kill Jarāsandha · Aided by Kṛṣṇa, Bhīma fights Jarāsandha · The freed kings praise Kṛṣṇa · At Dharmarāja's rājasūya Kṛṣṇa kills Śiśupāla"),
        ("9 · verses 831–926", "bhagavatam-10b-09-iast.html", "Śālva wins the Saubha from Śiva and attacks Dvārakā · Kṛṣṇa kills Dantavakra"),
        ("10 · verses 927–1033", "bhagavatam-10b-10-iast.html", "Balarāma goes on pilgrimage · The story of Kucela · The fruit of hearing"),
        ("11 · verses 1034–1136", "bhagavatam-10b-11-iast.html", "Kṛṣṇa and his family go to bathe at the eclipse · Lakṣaṇā, Kṛṣṇa's eighth wife, tells Draupadī of her wedding · Nārada and the sages visit Kṛṣṇa and have Vasudeva perform a sacrifice"),
        ("12 · verses 1137–1236", "bhagavatam-10b-12-iast.html", "Kṛṣṇa and Balarāma bring back their dead brothers to Devakī · The wedding of Subhadrā · Kṛṣṇa goes to Mithilā with the sages · The songs of the Vedas · Śuka tells Parīkṣit the excellence of serving Viṣṇu"),
        ("13 · verses 1237–1343", "bhagavatam-10b-13-iast.html", "Vṛkāsura, set on harming Śiva, dies by Viṣṇu's māyā · Bhṛgu goes to test the three gods · Kṛṣṇa brings back the brāhmaṇa's dead sons"),
    ]},
    ],
}
