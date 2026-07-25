# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain) via teltools dev2iast.
# Translations original. See SOURCES.md §5.5. Kanakadhārā of Ādi Śaṅkara,
# a hymn to Śrī Lakṣmī: praise of the sidelong glance (apāṅga/kaṭākṣa)
# of the Goddess resting on the breast of Viṣṇu (Hari, Mukunda, Murāri).

def _v(p1, p2, p3, p4, n, gloss):
    return {"padas": [p1, p2 + " |", p3, p4], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "devi",
    "doc_title": "Kanakadhārā Stotram",
    "app_title": "Kanakadhārā",
    "h1": "Śrī Kanakadhārā Stotram",
    "subtitle": "The Stream of Gold · a Hymn to Lakṣmī",
    "footer": "Source: Sanskrit Wikisource — Śrī Kanakadhārā Stotram (public domain)",
    "sections": [
        _v("aṅgaṃ hareḥ pulakabhūṣaṇamāśrayantī",
           "bhṛṅgāṅganeva mukulābharaṇaṃ tamālam",
           "aṅgīkṛtākhilavibhūtirapāṅgalīlā",
           "māṅgalyadā'stu mama maṅgaladevatāyāḥ", 1,
           "Resting on the body of Hari — thrilled to horripilation as its "
           "ornament — like a she-bee upon a budding tamāla tree; her sidelong "
           "play has taken to itself every splendour. May that glance of the "
           "Goddess of good fortune bring me blessing."),
        _v("mugdhā muhurvidadhatī vadane murāreḥ",
           "prematrapāpraṇihitāni gatāgatāni",
           "mālā dṛśormadhukarīva mahotpale yā",
           "sā me śriyaṃ diśatu sāgarasambhavāyāḥ", 2,
           "Charmingly, again and again, she casts to Murāri's face her glances "
           "of love and shy modesty, coming and going; that garland of her eyes, "
           "like a line of bees over a great blue lotus — may it grant me the "
           "wealth of her who rose from the ocean."),
        _v("āmīlitākṣamadhigamya mudā mukundam-",
           "ānandakandamanimeṣamanaṅgatantram",
           "ākekarasthitakanīnikapakṣmanetraṃ",
           "bhūtyai bhavenmama bhujaṅgaśayāṅganāyāḥ", 3,
           "Reaching Mukunda with joy — the root of bliss, unwinking, ruled by "
           "love — her eyes half-closed, pupils and lashes set in a sidelong "
           "gaze: may that glance of the consort of the serpent-recliner be for "
           "my prosperity."),
        _v("bāhvantare madhujitaḥ śritakaustubhe yā",
           "hārāvalīva harinīlamayī vibhāti",
           "kāmapradā bhagavato'pi kaṭākṣamālā",
           "kalyāṇamāvahatu me kamalālayāyāḥ", 4,
           "On the breast of the slayer of Madhu, where the Kaustubha rests, she "
           "shines like a string of sapphire jewels; that garland of sidelong "
           "glances, granting wishes even to the Lord himself — may it, of her "
           "who dwells in the lotus, bring me weal."),
        _v("kālāmbudālilalitorasi kaiṭabhārer-",
           "dhārādhare sphurati yā taḍidaṅganeva",
           "mātuḥ samastajagatāṃ mahanīyamūrtir-",
           "bhadrāṇi me diśatu bhārgavanandanāyāḥ", 5,
           "On the dark-cloud-lovely breast of Kaiṭabha's foe, the rain-bearer, "
           "she flashes like a woman of lightning; the venerable form of the "
           "Mother of all worlds — may she, daughter of Bhṛgu, grant me every "
           "blessing."),
        _v("prāptaṃ padaṃ prathamataḥ khalu yatprabhāvān-",
           "māṅgalyabhāji madhumāthini manmathena",
           "mayyāpatettadiha mantharamīkṣaṇārdhaṃ",
           "mandālasaṃ ca makarālayakanyakāyāḥ", 6,
           "By whose power Kāma first won his footing in the auspicious slayer of "
           "Madhu — may that same slow, languid, half-lidded sidelong look of the "
           "ocean's daughter fall here upon me."),
        _v("viśvāmarendrapadavibhramadānadakṣam-",
           "ānandaheturadhikaṃ muravidviṣo'pi",
           "īṣanniṣīdatu mayi kṣaṇamīkṣaṇārdham-",
           "indīvarodarasahodaramindirāyāḥ", 7,
           "Able to bestow the dazzling rank of the gods' own Indra, and a source "
           "of surpassing joy even to the foe of Mura — may Indirā's half-glance, "
           "sister to the heart of the blue lotus, rest on me a moment, however "
           "slightly."),
        _v("iṣṭāviśiṣṭamatayo'pi yayā dayārdra-",
           "dṛṣṭyā triviṣṭapapadaṃ sulabhaṃ labhante",
           "dṛṣṭiḥ prahṛṣṭakamalodaradīptiriṣṭāṃ",
           "puṣṭiṃ kṛṣīṣṭa mama puṣkaraviṣṭarāyāḥ", 8,
           "By whose compassion-melting gaze even the undistinguished easily win "
           "heaven — may that gaze, bright as the joyful heart of a lotus, work "
           "in me the prosperity I long for: the gaze of her enthroned upon the "
           "lotus."),
        _v("dadyāddayānupavano draviṇāmbudhārām-",
           "asminnakiñcanavihaṅgaśiśau viṣaṇṇe",
           "duṣkarmadharmamapanīya cirāya dūraṃ",
           "nārāyaṇapraṇayinīnayanāmbuvāhaḥ", 9,
           "Driven by the breeze of compassion, may the rain-cloud of the eyes of "
           "Nārāyaṇa's beloved pour its stream of wealth upon this dejected, "
           "penniless fledgling, driving the burden of ill deeds far off for "
           "long."),
        _v("gīrdevateti garuḍadhvajasundarīti",
           "śākambharīti śaśiśekharavallabheti",
           "sṛṣṭisthitipralayakeliṣu saṃsthitāyai",
           "tasyai namastribhuvanaikagurostaruṇyai", 10,
           "As the goddess of speech, as the beauty of the eagle-bannered, as "
           "Śākambharī, as the beloved of the moon-crested — to her who abides "
           "through the play of creation, sustenance, and dissolution: salutation "
           "to the youthful consort of the one Guru of the three worlds."),
        _v("śrutyai namo'stu śubhakarmaphalaprasūtyai",
           "ratyai namo'stu ramaṇīyaguṇārṇavāyai",
           "śaktyai namo'stu śatapatraniketanāyai",
           "puṣṭyai namo'stu puruṣottamavallabhāyai", 11,
           "Salutation to Śruti, who brings forth the fruit of good deeds; to "
           "Rati, ocean of delightful virtues; to Śakti, whose home is the "
           "hundred-petalled lotus; to Puṣṭi, beloved of the Supreme Person."),
        _v("namo'stu nālīkanibhānanāyai",
           "namo'stu dugdhodadhijanmabhūtyai",
           "namo'stu somāmṛtasodarāyai",
           "namo'stu nārāyaṇavallabhāyai", 12,
           "Salutation to her whose face is like a lotus; to her, the glory born "
           "of the milk-ocean; to the sister of the moon and of nectar; to the "
           "beloved of Nārāyaṇa."),
        _v("namo'stu hemāmbujapīṭhikāyai",
           "namo'stu bhūmaṇḍalanāyikāyai",
           "namo'stu devādidayāparāyai",
           "namo'stu śārṅgāyudhavallabhāyai", 13,
           "Salutation to her seated on the golden lotus; to the mistress of the "
           "earth-sphere; to her intent on compassion for gods and all; to the "
           "beloved of the wielder of the Śārṅga bow."),
        _v("namo'stu devyai bhṛgunandanāyai",
           "namo'stu viṣṇorurasi sthitāyai",
           "namo'stu lakṣmyai kamalālayāyai",
           "namo'stu dāmodaravallabhāyai", 14,
           "Salutation to the Goddess, daughter of Bhṛgu; to her who abides on "
           "Viṣṇu's chest; to Lakṣmī, dweller in the lotus; to the beloved of "
           "Dāmodara."),
        _v("namo'stu kāntyai kamalekṣaṇāyai",
           "namo'stu bhūtyai bhuvanaprasūtyai",
           "namo'stu devādibhirarcitāyai",
           "namo'stu nandātmajavallabhāyai", 15,
           "Salutation to Kānti, the lotus-eyed; to Bhūti, mother of the worlds; "
           "to her worshipped by the gods and all; to the beloved of the son of "
           "Nanda."),
        _v("sampatkarāṇi sakalendriyanandanāni",
           "sāmrājyadānavibhavāni saroruhākṣi",
           "tvadvandanāni duritoddharaṇodyatāni",
           "māmeva mātaraniśaṃ kalayantu mānye", 16,
           "O lotus-eyed, O honoured Mother — may acts of homage to you, which "
           "bring wealth, gladden every sense, hold power to bestow empire, and "
           "are bent on lifting away sin, make me their own forever."),
        _v("yatkaṭākṣasamupāsanāvidhiḥ",
           "sevakasya sakalārthasampadaḥ",
           "santanoti vacanāṅgamānasais-",
           "tvāṃ murārihṛdayeśvarīṃ bhaje", 17,
           "With word, body, and mind I worship you, sovereign of Murāri's heart "
           "— you whose sidelong glance, duly adored, spreads out for your servant "
           "every wealth and aim fulfilled."),
        _v("sarasijanilaye sarojahaste",
           "dhavalatamāṃśukagandhamālyaśobhe",
           "bhagavati harivallabhe manojñe",
           "tribhuvanabhūtikari prasīda mahyam", 18,
           "O dweller in the lotus, lotus in hand, radiant with purest garment, "
           "fragrance, and garland; O blessed one, beloved of Hari, enchanting, "
           "bestower of the three worlds' welfare — be gracious to me."),
        _v("digghastibhiḥ kanakakumbhamukhāvasṛṣṭa-",
           "svarvāhinīvimalacārujalaplutāṅgīm",
           "prātarnamāmi jagatāṃ jananīmaśeṣa-",
           "lokādhināthagṛhiṇīmamṛtābdhiputrīm", 19,
           "At dawn I bow to the Mother of the worlds — her body bathed by the "
           "clear, lovely waters of the celestial river poured from golden "
           "pitchers at the mouths of the elephants of the quarters — housewife of "
           "the Lord of all worlds, daughter of the ocean of nectar."),
        _v("kamale kamalākṣavallabhe tvaṃ",
           "karuṇāpūrataraṅgitairapāṅgaiḥ",
           "avalokaya māmakiñcanānāṃ",
           "prathamaṃ pātramakṛtrimaṃ dayāyāḥ", 20,
           "O Kamalā, beloved of the lotus-eyed one — with your sidelong glances "
           "rippling with floods of compassion, look upon me: of all the "
           "destitute the foremost, an unfeigned vessel of your mercy."),
        _v("devi prasīda jagadīśvari lokamātaḥ",
           "kalyāṇagātri kamalekṣaṇajīvanāthe",
           "dāridryabhītihṛdayaṃ śaraṇāgataṃ mām-",
           "ālokaya pratidinaṃ sadayairapāṅgaiḥ", 21,
           "Be gracious, O Goddess, sovereign of the world, Mother of all; O "
           "fair-limbed one, life's mistress of the lotus-eyed Lord — look each "
           "day, with compassionate sidelong glances, upon me who have come to "
           "your refuge, my heart afraid of poverty."),
        _v("stuvanti ye stutibhiramūbhiranvahaṃ",
           "trayīmayīṃ tribhuvanamātaraṃ ramām",
           "guṇādhikā gurutarabhāgyabhāgino",
           "bhavanti te bhuvi budhabhāvitāśayāḥ", 22,
           "Those who day by day praise with these hymns Ramā — embodiment of the "
           "three Vedas, Mother of the three worlds — become on earth rich in "
           "virtue, sharers of surpassing fortune, their hearts esteemed by the "
           "wise."),
        "ornament",
        {
            "padas": [
                "iti śrīmacchaṅkarācāryakṛtaṃ",
                "śrīkanakadhārāstotraṃ sampūrṇam",
            ],
            "num": "",
            "gloss": "Thus concludes the Śrī Kanakadhārā Stotram composed by Śrī "
                     "Śaṅkarācārya.",
        },
    ],
}
