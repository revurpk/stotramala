# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Īśāvāsya (Īśa) Upaniṣad — the closing chapter of the Śukla-Yajurveda
# Vājasaneyi Saṃhitā, 18 mantras. IAST from Sanskrit Wikisource (ईशोपनिषत्,
# public domain) via the teltools dev2iast port (anunāsika ँ → ṁ, line-break
# hyphens joined). Translations original. Public-domain source — no
# redistribution restriction. See SOURCES.md §5.17.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


_SHANTI = _v([
    "oṃ pūrṇamadaḥ pūrṇamidaṃ pūrṇāt pūrṇamudacyate |",
    "pūrṇasya pūrṇamādāya pūrṇamevāvaśiṣyate ||",
    "oṃ śāntiḥ śāntiḥ śāntiḥ ||",
], "",
   "Oṃ. That is full; this is full. From the full, the full arises. Taking "
   "the full from the full, the full alone remains. Oṃ, peace, peace, peace.")


STOTRA = {
    "deity": "advaita",
    "doc_title": "Īśāvāsya Upaniṣad",
    "app_title": "Īśāvāsya Upaniṣad",
    "h1": "Īśāvāsya Upaniṣad",
    "subtitle": "The Lord enfolds all · Īśa Upaniṣad",
    "note": "The first of the principal Upaniṣads — the closing (fortieth) "
            "chapter of the Śukla-Yajurveda saṃhitā, only eighteen mantras, yet "
            "holding the whole of Vedānta: the Lord indwelling all, action "
            "without craving, and the Self beyond death. Framed by the "
            "pūrṇam-invocation of fullness.",
    "footer": "Source: Sanskrit Wikisource — ईशोपनिषत् (public domain)",
    "sections": [
        _SHANTI,
        "ornament",
        _v([
            "oṃ īśā vāsyamidaṁ sarvaṃ yatkiñca jagatyāṃ jagat |",
            "tena tyaktena bhuñjīthā mā gṛdhaḥ kasyasviddhanam",
        ], "|| 1 ||",
           "All this — whatever moves in this moving world — is to be indwelt by "
           "the Lord. By that renunciation, enjoy; do not covet anyone's "
           "wealth."),
        _v([
            "kurvanneveha karmāṇi jijīviṣecchataṁ samāḥ |",
            "evaṃ tvayi nānyatheto'sti na karma lipyate nare",
        ], "|| 2 ||",
           "Ever performing works here, one should wish to live a hundred years. "
           "For you, a man, there is no way other than this by which action does "
           "not cling."),
        _v([
            "asuryā nāma te lokā andhena tamasā''vṛtāḥ |",
            "tāṁste pretyābhigacchanti ye ke cātmahano janāḥ",
        ], "|| 3 ||",
           "Sunless are those worlds, wrapped in blinding darkness; to them, "
           "after death, go those people who are slayers of the Self."),
        _v([
            "anejadekaṃ manaso javīyo nainaddevā āpnuvanpūrvamarṣat |",
            "taddhāvato'nyānatyeti tiṣṭhattasminnapo mātariśvā dadhāti",
        ], "|| 4 ||",
           "Unmoving, one, swifter than the mind — the gods could not overtake "
           "It, for It sped on ahead. Standing still, It outstrips others who "
           "run. In It, Mātariśvā (the cosmic wind) sustains all activity."),
        _v([
            "tadejati tannaijati taddūre tadvantike |",
            "tadantarasya sarvasya tadu sarvasyāsya bāhyataḥ",
        ], "|| 5 ||",
           "It moves, and It moves not; It is far, and It is near; It is within "
           "all this, and It is also outside all this."),
        _v([
            "yastu sarvāṇi bhūtānyātmanyevānupaśyati |",
            "sarvabhūteṣu cātmānaṃ tato na vijugupsate",
        ], "|| 6 ||",
           "But whoever sees all beings in the Self alone, and the Self in all "
           "beings, thereafter shrinks from nothing."),
        _v([
            "yasminsarvāṇi bhūtānyātmaivābhūdvijānataḥ |",
            "tatra ko mohaḥ kaḥ śoka ekatvamanupaśyataḥ",
        ], "|| 7 ||",
           "When, for the knower, all beings have become the very Self, what "
           "delusion, what sorrow can there be for one who sees the oneness?"),
        _v([
            "sa paryagācchukramakāyamavraṇamasnāviraṁ śuddhamapāpaviddham |",
            "kavirmanīṣī paribhūḥ svayambhūryāthātathyato'rthān vyadadhācchāśvatībhyaḥ samābhyaḥ",
        ], "|| 8 ||",
           "He has spread everywhere — radiant, bodiless, unscarred, without "
           "sinews, pure, untouched by evil; the seer, the thinker, "
           "all-surpassing, self-existent — who has duly assigned the ends of "
           "things through the everlasting years."),
        _v([
            "andhaṃ tamaḥ praviśanti ye'vidyāmupāsate |",
            "tato bhūya iva te tamo ya u vidyāyāṁ ratāḥ",
        ], "|| 9 ||",
           "Into blind darkness enter those who worship ignorance; into darkness "
           "greater still, as it were, those who delight in knowledge alone."),
        _v([
            "anyadevāhurvidyayā'nyadāhuravidyayā |",
            "iti śuśruma dhīrāṇāṃ ye nastadvicacakṣire",
        ], "|| 10 ||",
           "One result, they say, comes of knowledge; another, they say, of "
           "ignorance — so we have heard from the wise who explained it to us."),
        _v([
            "vidyāṃ cāvidyāṃ ca yastadvedobhayaṁ saha |",
            "avidyayā mṛtyuṃ tīrtvā vidyayā'mṛtamaśnute",
        ], "|| 11 ||",
           "Whoever knows both knowledge and ignorance together — crossing death "
           "by ignorance, he attains the immortal by knowledge."),
        _v([
            "andhaṃ tamaḥ praviśanti ye'sambhūtimupāsate |",
            "tato bhūya iva te tamo ya u sambhūtyāṁ ratāḥ",
        ], "|| 12 ||",
           "Into blind darkness enter those who worship the unmanifest; into "
           "darkness greater still, as it were, those who delight in the "
           "manifest."),
        _v([
            "anyadevāhuḥ sambhavādanyadāhurasambhavāt |",
            "iti śuśruma dhīrāṇāṃ ye nastadvicacakṣire",
        ], "|| 13 ||",
           "One result, they say, comes of the manifest (becoming); another, "
           "they say, of the unmanifest — so we have heard from the wise who "
           "explained it to us."),
        _v([
            "sambhūtiṃ ca vināśaṃ ca yastadvedobhayaṁ saha |",
            "vināśena mṛtyuṃ tīrtvā sambhūtyā'mṛtamaśnute",
        ], "|| 14 ||",
           "Whoever knows both the manifest (becoming) and destruction together "
           "— crossing death by destruction, he attains the immortal by the "
           "manifest."),
        _v([
            "hiraṇmayena pātreṇa satyasyāpihitaṃ mukham |",
            "tattvaṃ pūṣannapāvṛṇu satyadharmāya dṛṣṭaye",
        ], "|| 15 ||",
           "The face of the Truth is covered over by a golden disc. O Pūṣan, "
           "uncover it — for me, devoted to the truth, that I may see."),
        _v([
            "pūṣannekarṣe yama sūrya prājāpatya vyūha raśmīn samūha tejaḥ |",
            "yatte rūpaṃ kalyāṇatamaṃ tatte paśyāmi yo'sāvasau puruṣaḥ so'hamasmi",
        ], "|| 16 ||",
           "O Pūṣan, sole seer, Yama, Sūrya, son of Prajāpati — spread apart "
           "your rays, gather up your blaze. That form of yours, the most "
           "blessed — that I behold. That Person yonder — He am I."),
        _v([
            "vāyuranilamamṛtamathedaṃ bhasmāṃtaṁ śarīram |",
            "oṃ krato smara kṛtaṁ smara krato smara kṛtaṁ smara",
        ], "|| 17 ||",
           "Let the breath merge in the immortal, all-pervading air; and let "
           "this body end in ashes. Oṃ. O will, remember — remember what was "
           "done; O will, remember — remember what was done."),
        _v([
            "agne naya supathā rāye asmān viśvāni deva vayunāni vidvān |",
            "yuyodhyasmajjuhurāṇameno bhūyiṣṭhāṃ te namauktiṃ vidhema",
        ], "|| 18 ||",
           "O Agni, lead us by the good path to prosperity, O God who knows all "
           "our ways. Keep far from us the crooked-going sin. To you we would "
           "offer the fullest word of homage."),
        "ornament",
        _SHANTI,
    ],
}
