# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain) via teltools dev2iast,
# with rough readings normalised to standard (SOURCES §5.10).
# Translations original. Mahālakṣmī Aṣṭakam (from the Padma Purāṇa) —
# eight salutations to Mahālakṣmī; refrain "mahālakṣmi namo'stu te".

def _v(l1, l2, n, gloss):
    return {"padas": [l1 + " |", l2], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "devi",
    "doc_title": "Mahālakṣmī Aṣṭakam",
    "app_title": "Mahālakṣmī Aṣṭakam",
    "h1": "Śrī Mahālakṣmī Aṣṭakam",
    "subtitle": "Eight Verses to Mahālakṣmī",
    "footer": "Source: Sanskrit Wikisource — Śrī Mahālakṣmyaṣṭakam (public domain)",
    "sections": [
        _v("namaste'stu mahāmāye śrīpīṭhe surapūjite",
           "śaṃkhacakragadāhaste mahālakṣmi namo'stu te", 1,
           "Salutation to You, O Great Māyā, throned upon Śrī, worshipped by the "
           "gods; O You who hold the conch, discus, and mace — O Mahālakṣmī, "
           "salutation to You."),
        _v("namaste garuḍārūḍhe kolāsurabhayaṃkari",
           "sarvapāpahare devi mahālakṣmi namo'stu te", 2,
           "Salutation to You, mounted on Garuḍa, terror of the demon Kola; O "
           "Devī who removes all sin — O Mahālakṣmī, salutation to You."),
        _v("sarvajñe sarvavarade sarvaduṣṭabhayaṃkari",
           "sarvaduḥkhahare devi mahālakṣmi namo'stu te", 3,
           "O all-knowing, all-boon-granting, terror of all the wicked; O Devī "
           "who removes all sorrow — O Mahālakṣmī, salutation to You."),
        _v("siddhibuddhiprade devi bhuktimuktipradāyini",
           "mantramūrte sadā devi mahālakṣmi namo'stu te", 4,
           "O Devī who grant attainment and wisdom, bestower of enjoyment and "
           "liberation; O Devī ever the embodiment of the mantra — O Mahālakṣmī, "
           "salutation to You."),
        _v("ādyantarahite devi ādyaśakti maheśvari",
           "yogaje yogasambhūte mahālakṣmi namo'stu te", 5,
           "O Devī without beginning or end, primal Śakti, great Sovereign; O You "
           "born of yoga, arisen from yoga — O Mahālakṣmī, salutation to You."),
        _v("sthūlasūkṣmamahāraudre mahāśakti mahodare",
           "mahāpāpahare devi mahālakṣmi namo'stu te", 6,
           "O You gross and subtle, greatly terrible, great Śakti, vast of womb; "
           "O Devī who removes great sin — O Mahālakṣmī, salutation to You."),
        _v("padmāsanasthite devi parabrahmasvarūpiṇi",
           "parameśi jaganmātarmahālakṣmi namo'stu te", 7,
           "O Devī seated on the lotus, whose very form is the Supreme Brahman; "
           "O supreme Sovereign, Mother of the world — O Mahālakṣmī, salutation "
           "to You."),
        _v("śvetāmbaradhare devi nānālaṃkārabhūṣite",
           "jagatsthite jaganmātarmahālakṣmi namo'stu te", 8,
           "O Devī robed in white, adorned with many ornaments; O You who abide "
           "within the world, Mother of the world — O Mahālakṣmī, salutation to "
           "You."),
        "ornament",
        _v("mahālakṣmyaṣṭakaṃ stotraṃ yaḥ paṭhedbhaktimānnaraḥ",
           "sarvasiddhimavāpnoti rājyaṃ prāpnoti sarvadā", 9,
           "The devout person who recites this Mahālakṣmī Aṣṭaka hymn attains "
           "every accomplishment and gains sovereignty always."),
        _v("ekakāle paṭhennityaṃ mahāpāpavināśanam",
           "dvikālaṃ yaḥ paṭhennityaṃ dhanadhānyasamanvitaḥ", 10,
           "Recited once each day, it destroys great sin; whoever recites it "
           "twice each day is endowed with wealth and grain."),
        _v("trikālaṃ yaḥ paṭhennityaṃ mahāśatruvināśanam",
           "mahālakṣmīrbhavennityaṃ prasannā varadā śubhā", 11,
           "Whoever recites it thrice each day undoes great enmity; and "
           "Mahālakṣmī becomes ever gracious to him, boon-giving and "
           "auspicious."),
    ],
}
