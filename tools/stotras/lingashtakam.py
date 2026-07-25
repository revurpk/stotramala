# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain) via teltools dev2iast.
# Translations original. See SOURCES.md §5.8. Liṅgāṣṭakam — eight verses
# to the Sadāśiva liṅga; refrain "tat praṇamāmi sadāśiva liṅgam".

def _v(p1, p2, p3, p4, n, gloss):
    return {"padas": [p1 + " |", p2 + " |", p3 + " |", p4], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "shiva",
    "doc_title": "Liṅgāṣṭakam",
    "app_title": "Liṅgāṣṭakam",
    "h1": "Liṅgāṣṭakam",
    "subtitle": "Eight Verses to the Sadāśiva Liṅga",
    "footer": "Source: Sanskrit Wikisource — Liṅgāṣṭakam (public domain)",
    "sections": [
        _v("brahmamurārī surārcita liṅgaṃ",
           "nirmala bhāsita śobhita liṅgaṃ",
           "janmaja duḥkha vināśaka liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 1,
           "The liṅga worshipped by Brahmā, Murāri, and the gods; the liṅga "
           "shining spotless and resplendent; the liṅga that destroys the "
           "sorrows of birth — to that Sadāśiva liṅga I bow."),
        _v("devamuni pravarārcita liṅgaṃ",
           "kāmadahana karuṇākara liṅgaṃ",
           "rāvaṇa darpa vināśaka liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 2,
           "The liṅga worshipped by the foremost gods and sages; the liṅga that "
           "burned Kāma, the fount of compassion; the liṅga that destroyed "
           "Rāvaṇa's pride — to that Sadāśiva liṅga I bow."),
        _v("sarva sugandha sulepita liṅgaṃ",
           "buddhi vivardhana kāraṇa liṅgaṃ",
           "siddha surāsura vandita liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 3,
           "The liṅga anointed with all fragrances; the liṅga that is the cause "
           "of growing wisdom; the liṅga honoured by siddhas, gods, and demons — "
           "to that Sadāśiva liṅga I bow."),
        _v("kanaka mahāmaṇi bhūṣita liṅgaṃ",
           "phaṇipati veṣṭita śobhita liṅgaṃ",
           "dakṣa suyajña vināśana liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 4,
           "The liṅga adorned with gold and great jewels; the liṅga encircled and "
           "graced by the serpent-king; the liṅga that destroyed Dakṣa's "
           "sacrifice — to that Sadāśiva liṅga I bow."),
        _v("kuṅkuma candana lepita liṅgaṃ",
           "paṅkaja hāra suśobhita liṅgaṃ",
           "sañcita pāpa vināśaka liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 5,
           "The liṅga anointed with kuṅkuma and sandal; the liṅga graced with a "
           "garland of lotuses; the liṅga that destroys accumulated sin — to that "
           "Sadāśiva liṅga I bow."),
        _v("devagaṇārcita sevita liṅgaṃ",
           "bhāvairbhaktibhireva ca liṅgaṃ",
           "dinakara koṭi prabhākara liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 6,
           "The liṅga worshipped and served by hosts of gods, and (approached) "
           "with heartfelt devotions; the liṅga radiant as ten million suns — to "
           "that Sadāśiva liṅga I bow."),
        _v("aṣṭadalopariveṣṭita liṅgaṃ",
           "sarvasamudbhava kāraṇa liṅgaṃ",
           "aṣṭadaridra vināśana liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 7,
           "The liṅga encircled by the eight petals; the liṅga that is the cause "
           "of all that arises; the liṅga that destroys the eight poverties — to "
           "that Sadāśiva liṅga I bow."),
        _v("suraguru suravara pūjita liṅgaṃ",
           "suravana puṣpa sadārcita liṅgaṃ",
           "parātpara paramātmaka liṅgaṃ",
           "tat praṇamāmi sadāśiva liṅgaṃ", 8,
           "The liṅga worshipped by the guru of the gods and the best of gods; "
           "the liṅga ever worshipped with flowers of the celestial groves; the "
           "liṅga higher than the highest, the very Self — to that Sadāśiva liṅga "
           "I bow."),
        "ornament",
        {
            "padas": [
                "liṅgāṣṭakamidaṃ puṇyaṃ yaḥ paṭhet śivasannidhau |",
                "śivalokamavāpnoti śivena saha modate",
            ],
            "num": "",
            "gloss": "Whoever recites this holy Liṅgāṣṭaka in the presence of "
                     "Śiva attains the world of Śiva and rejoices there with Him.",
        },
    ],
}
