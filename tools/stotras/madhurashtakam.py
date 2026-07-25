# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain) via teltools dev2iast.
# Translations original. See SOURCES.md §5.7. Madhurāṣṭakam of
# Vallabhācārya — the eightfold sweetness of Kṛṣṇa, Lord of Mathurā.

def _v(l1, l2, n, gloss):
    return {"padas": [l1 + " |", l2], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "vishnu",
    "doc_title": "Madhurāṣṭakam",
    "app_title": "Madhurāṣṭakam",
    "h1": "Madhurāṣṭakam",
    "subtitle": "Eight Verses on Sweetness · Vallabhācārya",
    "footer": "Source: Sanskrit Wikisource — Madhurāṣṭakam (public domain)",
    "sections": [
        _v("adharaṃ madhuraṃ vadanaṃ madhuraṃ nayanaṃ madhuraṃ hasitaṃ madhuram",
           "hṛdayaṃ madhuraṃ gamanaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 1,
           "Sweet are his lips, sweet his face, sweet his eyes, sweet his smile; "
           "sweet his heart, sweet his gait — everything of the Lord of Mathurā, "
           "the Lord of sweetness, is sweet."),
        _v("vasanaṃ madhuraṃ caritaṃ madhuraṃ vacanaṃ madhuraṃ valitaṃ madhuram",
           "calitaṃ madhuraṃ bhramitaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 2,
           "Sweet his garment, sweet his deeds, sweet his speech, sweet his "
           "swaying; sweet his moving, sweet his wandering — everything of the "
           "Lord of sweetness is sweet."),
        _v("veṇurmadhuro reṇurmadhuraḥ pāṇirmadhuraḥ pādau madhurau",
           "nṛtyaṃ madhuraṃ sakhyaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 3,
           "Sweet his flute, sweet the dust of his feet, sweet his hand, sweet "
           "his two feet; sweet his dance, sweet his friendship — everything of "
           "the Lord of sweetness is sweet."),
        _v("gītaṃ madhuraṃ pītaṃ madhuraṃ bhuktaṃ madhuraṃ suptaṃ madhuram",
           "rūpaṃ madhuraṃ tilakaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 4,
           "Sweet his song, sweet his drinking, sweet his eating, sweet his "
           "sleeping; sweet his form, sweet his tilaka — everything of the Lord "
           "of sweetness is sweet."),
        _v("karaṇaṃ madhuraṃ taraṇaṃ madhuraṃ haraṇaṃ madhuraṃ ramaṇaṃ madhuram",
           "vamitaṃ madhuraṃ śamitaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 5,
           "Sweet his acting, sweet his rescuing, sweet his stealing, sweet his "
           "loving; sweet his casting-off, sweet his quelling — everything of the "
           "Lord of sweetness is sweet."),
        _v("guñjā madhurā mālā madhurā yamunā madhurā vīcī madhurā",
           "salilaṃ madhuraṃ kamalaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 6,
           "Sweet the berry-ornament, sweet the garland, sweet the Yamunā, sweet "
           "its waves; sweet the water, sweet the lotus — everything of the Lord "
           "of sweetness is sweet."),
        _v("gopī madhurā līlā madhurā rādhā madhurā milanaṃ madhuram",
           "dṛṣṭaṃ madhuraṃ śiṣṭaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 7,
           "Sweet the cowherd-girl, sweet his play, sweet Rādhā, sweet their "
           "meeting; sweet his glance, sweet his courtesy — everything of the "
           "Lord of sweetness is sweet."),
        _v("gopā madhurā gāvo madhurā yaṣṭirmadhurā sṛṣṭirmadhurā",
           "dalitaṃ madhuraṃ phalitaṃ madhuraṃ madhurādhipaterakhilaṃ madhuram", 8,
           "Sweet the cowherds, sweet the cows, sweet his staff, sweet his "
           "creation; sweet what is trodden, sweet what bears fruit — everything "
           "of the Lord of sweetness is sweet."),
    ],
}
