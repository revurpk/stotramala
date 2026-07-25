# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain) via teltools dev2iast, with
# readings normalised to the standard recitation (the e-text is loose; see
# SOURCES.md §5.9). Translations original. Bilvāṣṭakam — the offering of the
# bilva leaf to Śiva; refrain "ekabilvaṃ śivārpitam".

def _v(l1, l2, n, gloss):
    return {"padas": [l1 + " |", l2], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "shiva",
    "doc_title": "Bilvāṣṭakam",
    "app_title": "Bilvāṣṭakam",
    "h1": "Bilvāṣṭakam",
    "subtitle": "Eight Verses on the Bilva Leaf",
    "footer": "Source: Sanskrit Wikisource — Bilvāṣṭakam (public domain)",
    "sections": [
        _v("tridalaṃ triguṇākāraṃ trinetraṃ ca triyāyudham",
           "trijanmapāpasaṃhāram ekabilvaṃ śivārpitam", 1,
           "Three-leaved, of the form of the three guṇas, three-eyed and bearing "
           "the trident, destroyer of the sins of three births — one bilva leaf, "
           "offered to Śiva."),
        _v("triśākhairbilvapatraiśca acchidraiḥ komalaiḥ śubhaiḥ",
           "tava pūjāṃ kariṣyāmi ekabilvaṃ śivārpitam", 2,
           "With three-branched bilva leaves — unbroken, tender, and auspicious "
           "— I will perform your worship: one bilva leaf, offered to Śiva."),
        _v("darśanaṃ bilvavṛkṣasya sparśanaṃ pāpanāśanam",
           "aghorapāpasaṃhāram ekabilvaṃ śivārpitam", 3,
           "The sight of the bilva tree, its very touch, destroys sin, undoing "
           "even the most dreadful sin — one bilva leaf, offered to Śiva."),
        _v("sālagrāmeṣu vipreṣu taṭāke vanakūpayoḥ",
           "yajñakoṭisahasrāṇāṃ ekabilvaṃ śivārpitam", 4,
           "Worth more than gifts at śālagrāma shrines, to brāhmaṇas, at tanks, "
           "groves, and wells, and than ten thousand million sacrifices — one "
           "bilva leaf, offered to Śiva."),
        _v("dantikoṭisahasreṣu aśvamedhaśatāni ca",
           "koṭikanyāpradānena ekabilvaṃ śivārpitam", 5,
           "Worth more than a thousand million elephants, than a hundred "
           "horse-sacrifices, than the gift of ten million maidens — one bilva "
           "leaf, offered to Śiva."),
        _v("ekaṃ ca bilvapatraṃ ca koṭiyajñaphalaṃ labhet",
           "mahādevasya pūjārtham ekabilvaṃ śivārpitam", 6,
           "With even a single bilva leaf one gains the fruit of ten million "
           "sacrifices; for the worship of Mahādeva — one bilva leaf, offered to "
           "Śiva."),
        _v("kāśīkṣetre nivāsaṃ ca kālabhairavadarśanam",
           "prayāge mādhavaṃ dṛṣṭvā ekabilvaṃ śivārpitam", 7,
           "As good as dwelling in holy Kāśī, as the sight of Kālabhairava, as "
           "beholding Mādhava at Prayāga — one bilva leaf, offered to Śiva."),
        _v("umayā saha deveśaṃ vāhanaṃ nandiśaṅkaram",
           "mucyate sarvapāpebhyo ekabilvaṃ śivārpitam", 8,
           "The Lord of gods with Umā, whose mount is Nandi — by this one is "
           "freed from all sins: one bilva leaf, offered to Śiva."),
        "ornament",
        {
            "padas": [
                "tulasī bilva nirguṇḍī apāmārgakapitthakaḥ |",
                "śamī cāmalakaṃ dūrvā aṣṭabilvāḥ prakīrtitāḥ",
            ],
            "num": "",
            "gloss": "Tulasī, bilva, nirguṇḍī, apāmārga, kapittha, śamī, āmalaka, "
                     "and dūrvā — these are proclaimed the eight sacred leaves.",
        },
    ],
}
