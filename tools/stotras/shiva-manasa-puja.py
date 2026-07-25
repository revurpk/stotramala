# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain) via teltools dev2iast.
# Translations original. See SOURCES.md §5.6. Śiva Mānasa Pūjā of Ādi
# Śaṅkara — a worship of Śiva performed entirely in the mind.

def _v(p1, p2, p3, p4, n, gloss):
    return {"padas": [p1 + " |", p2 + " |", p3 + " |", p4], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "shiva",
    "doc_title": "Śiva Mānasa Pūjā",
    "app_title": "Śiva Mānasa Pūjā",
    "h1": "Śiva Mānasa Pūjā",
    "subtitle": "Mental Worship of Śiva · Ādi Śaṅkara",
    "footer": "Source: Sanskrit Wikisource — Śiva Mānasa Pūjā (public domain)",
    "sections": [
        _v("ratnaiḥ kalpitamāsanaṃ himajalaiḥ snānaṃ ca divyāmbaraṃ",
           "nānāratnavibhūṣitaṃ mṛgamadāmodāṅkitaṃ candanam",
           "jātīcampakabilvapatraracitaṃ puṣpaṃ ca dhūpaṃ tathā",
           "dīpaṃ deva dayānidhe paśupate hṛtkalpitaṃ gṛhyatām", 1,
           "A throne fashioned of jewels, a bath in cool water, divine raiment set "
           "with many gems; sandal-paste scented with musk; flowers of jasmine, "
           "campaka, and bilva leaves, incense, and a lamp — O God, ocean of "
           "compassion, Lord of creatures, receive all this, shaped within my "
           "heart."),
        _v("sauvarṇe navaratnakhaṇḍaracite pātre ghṛtaṃ pāyasaṃ",
           "bhakṣyaṃ pañcavidhaṃ payodadhiyutaṃ rambhāphalaṃ pānakam",
           "śākānāmayutaṃ jalaṃ rucikaraṃ karpūrakhaṇḍojjvalam",
           "tāmbūlaṃ manasā mayā viracitaṃ bhaktyā prabho svīkuru", 2,
           "In a golden vessel inlaid with the nine gems, ghee and sweet pāyasa; "
           "the fivefold food with milk and curds, plantains, and a sweet drink; a "
           "myriad of vegetables, delicious water bright with a piece of camphor, "
           "and betel — all this I have made in my mind. Accept it with love, O "
           "Lord."),
        _v("chatraṃ cāmarayoryugaṃ vyajanakaṃ cādarśakaṃ nirmalaṃ",
           "vīṇābherimṛdaṅgakāhalakalā gītaṃ ca nṛtyaṃ tathā",
           "sāṣṭāṅgaṃ praṇatiḥ stutirbahuvidhā hyetatsamastaṃ mayā",
           "saṅkalpena samarpitaṃ tava vibho pūjāṃ gṛhāṇa prabho", 3,
           "A parasol, a pair of yak-tail fans, a whisk, and a spotless mirror; "
           "the music of vīṇā, kettledrum, mṛdaṅga, and horn, with song and dance; "
           "prostration with the eight limbs, and praise of many kinds — all this "
           "I offer You by my resolve, O all-pervading Lord; accept my worship."),
        _v("ātmā tvaṃ girijā matiḥ sahacarāḥ prāṇāḥ śarīraṃ gṛhaṃ",
           "pūjā te viṣayopabhogaracanā nidrā samādhisthitiḥ",
           "sañcāraḥ padayoḥ pradakṣiṇavidhiḥ stotrāṇi sarvā giro",
           "yadyatkarma karomi tattadakhilaṃ śambho tavārādhanam", 4,
           "You are the Self; Girijā is my intellect; my life-breaths are Your "
           "companions; my body, Your house; my worship is the play of enjoying "
           "the senses; my sleep, the state of samādhi; the movement of my feet, "
           "circumambulation; all my words are hymns — whatever act I do, all of "
           "it, O Śambhu, is worship of You."),
        _v("karacaraṇakṛtaṃ vākkāyajaṃ karmajaṃ vā",
           "śravaṇanayanajaṃ vā mānasaṃ vāparādham",
           "vihitamavihitaṃ vā sarvametatkṣamasva",
           "jaya jaya karuṇābdhe śrīmahādeva śambho", 5,
           "Whatever wrong I have done — by hand or foot, by speech, body, or "
           "deed, by ear or eye, or in the mind; whatever, prescribed or "
           "forbidden — forgive it all. Victory, victory to You, O ocean of "
           "compassion, Śrī Mahādeva, Śambhu!"),
    ],
}
