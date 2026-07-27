# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Gaṇapati Atharvaśīrṣa (Gaṇeśa Upaniṣad), an Atharvan Upaniṣad hailing
# Gaṇapati as Brahman. IAST from Sanskrit Wikisource (गणपत्यथर्वशीर्षम्,
# public domain) via the teltools dev2iast port; a couple of source typos
# corrected and a variant reading dropped — logged in SOURCES.md §5.16.
# Translations original. Public-domain source — no redistribution restriction.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "ganesha",
    "doc_title": "Gaṇapati Atharvaśīrṣa",
    "app_title": "Gaṇapati Atharvaśīrṣa",
    "h1": "Gaṇapati Atharvaśīrṣa",
    "subtitle": "The Atharva-Crown of Gaṇapati · Gaṇeśa Upaniṣad",
    "note": "A short Upaniṣad of the Atharvan tradition that hails Gaṇapati as "
            "Brahman itself — the one Reality, source and dissolution of all. "
            "Framed by the peace-invocations (śānti-pāṭha), its heart is fourteen "
            "mantras, including the Gaṇeśa mantra, the Gāyatrī, and the "
            "meditation-verse (dhyāna), closing with the fruits of recitation.",
    "footer": "Source: Sanskrit Wikisource — गणपत्यथर्वशीर्षम् (public domain)",
    "sections": [
        _v([
            "oṃ bhadraṃ karṇebhiḥ śṛṇuyāma devāḥ |",
            "bhadraṃ paśyemākṣabhiryajatrāḥ ||",
            "sthirairaṅgaistuṣṭuvāṃsastanūbhiḥ |",
            "vyaśema devahitaṃ yadāyuḥ ||",
            "oṃ svasti na indro vṛddhaśravāḥ |",
            "svasti naḥ pūṣā viśvavedāḥ ||",
            "svastinastārkṣyo ariṣṭanemiḥ |",
            "svasti no bṛhaspatirdadhātu ||",
            "oṃ tanmāmavatu tad vaktāramavatu avatu mām avatu vaktāram |",
            "oṃ śāntiḥ śāntiḥ śāntiḥ ||",
        ], "",
           "Śānti-pāṭha. Oṃ. May we, O gods, hear what is auspicious with our "
           "ears; may we see what is auspicious with our eyes, O worshipful "
           "ones. With steady limbs and bodies, praising you, may we enjoy the "
           "life the gods have ordained. May Indra of ancient fame bless us; may "
           "all-knowing Pūṣan bless us; may Tārkṣya, averter of harm, bless us; "
           "may Bṛhaspati grant us well-being. Oṃ. May He protect me; may He "
           "protect the teacher; may He protect me; may He protect the teacher. "
           "Oṃ, peace, peace, peace."),
        "ornament",
        _v([
            "hariḥ oṃ namaste gaṇapataye |",
            "tvameva pratyakṣaṃ tattvamasi ||",
            "tvameva kevalaṃ kartā'si |",
            "tvameva kevalaṃ dhartā'si ||",
            "tvameva kevalaṃ hartā'si |",
            "tvameva sarvaṃ khalvidaṃ brahmāsi ||",
            "tvaṃ sākṣādātmā'si nityam",
        ], "|| 1 ||",
           "Hariḥ Oṃ. Salutation to you, Gaṇapati. You alone are the manifest "
           "Reality. You alone are the sole doer; you alone the sole sustainer; "
           "you alone the sole destroyer. You alone are truly all this — Brahman. "
           "You are the very Self, eternally."),
        _v([
            "ṛtaṃ vacmi ||",
            "satyaṃ vacmi",
        ], "|| 2 ||",
           "I speak the cosmic order (ṛta); I speak the truth (satya)."),
        _v([
            "ava tvaṃ mām |",
            "ava vaktāram ||",
            "ava śrotāram |",
            "ava dātāram ||",
            "ava dhātāram |",
            "avānūcānamava śiṣyam ||",
            "ava paścāttāt |",
            "ava purastāt ||",
            "avottarāttāt |",
            "ava dakṣiṇāttāt ||",
            "ava cordhvāttāt |",
            "avādharāttāt ||",
            "sarvato māṃ pāhi pāhi samantāt",
        ], "|| 3 ||",
           "Protect me; protect the speaker; protect the hearer; protect the "
           "giver; protect the sustainer; protect the reciter of tradition and "
           "protect the student. Protect from behind; protect from the front; "
           "protect from the north; protect from the south; protect from above; "
           "protect from below. On every side guard me, guard me from all "
           "around."),
        _v([
            "tvaṃ vāṅmayastvaṃ cinmayaḥ |",
            "tvamānandamayastvaṃ brahmamayaḥ ||",
            "tvaṃ saccidānandādvitīyo'si |",
            "tvaṃ pratyakṣaṃ brahmāsi ||",
            "tvaṃ jñānamayo vijñānamayo'si",
        ], "|| 4 ||",
           "You are made of speech, you are made of consciousness; you are made "
           "of bliss, you are made of Brahman. You are being-consciousness-bliss, "
           "the One without a second. You are the manifest Brahman. You are made "
           "of knowledge and of discernment."),
        _v([
            "sarvaṃ jagadidaṃ tvatto jāyate |",
            "sarvaṃ jagadidaṃ tvattastiṣṭhati ||",
            "sarvaṃ jagadidaṃ tvayi layameṣyati |",
            "sarvaṃ jagadidaṃ tvayi pratyeti ||",
            "tvaṃ bhūmirāpo'nalo'nilo nabhaḥ ||",
            "tvaṃ catvāri vākpadāni",
        ], "|| 5 ||",
           "All this world is born from you; all this world abides in you; all "
           "this world will dissolve into you; all this world returns to you. You "
           "are earth, water, fire, air, and space. You are the four levels of "
           "speech."),
        _v([
            "tvaṃ guṇatrayātītaḥ |",
            "tvamavasthātrayātītaḥ |",
            "tvaṃ dehatrayātītaḥ ||",
            "tvaṃ kālatrayātītaḥ |",
            "tvaṃ mūlādhāraḥ sthito'si nityam ||",
            "tvaṃ śaktitrayātmakaḥ |",
            "tvāṃ yogino dhyāyanti nityam ||",
            "tvaṃ brahmā tvaṃ viṣṇustvaṃ rudrastvamindrastvamagnistvaṃ vāyustvaṃ sūryastvaṃ candramāstvaṃ brahmabhūrbhuvaḥsvarom",
        ], "|| 6 ||",
           "You are beyond the three qualities, beyond the three states, beyond "
           "the three bodies, beyond the three times. You dwell ever in the "
           "root-support (mūlādhāra). You are of the threefold power. Yogins "
           "meditate on you always. You are Brahmā, Viṣṇu, Rudra, Indra, Agni, "
           "Vāyu, Sūrya, Candra — you are Brahman; earth, mid-air, and heaven; "
           "and Oṃ."),
        _v([
            "gaṇādiṃ pūrvamuccārya varṇādīṃstadanantaram |",
            "anusvāraḥ parataraḥ ||",
            "ardhendulasitam |",
            "tāreṇa ṛddham ||",
            "etattava manusvarūpam |",
            "gakāraḥ pūrvarūpam ||",
            "akāro madhyamarūpam |",
            "anusvāraścāntyarūpam ||",
            "binduruttararūpam |",
            "nādaḥ sandhānam ||",
            "saṃhitāsandhiḥ |",
            "saiṣā gaṇeśavidyā ||",
            "gaṇaka ṛṣiḥ |",
            "nicṛdgāyatrīcchandaḥ ||",
            "gaṇapatirdevatā ||",
            "oṃ gaṃ gaṇapataye namaḥ",
        ], "|| 7 ||",
           "The Gaṇeśa mantra. Uttering first the sound ‘ga’ (the head of "
           "gaṇa), then the letter that follows (‘ṇa’), with the anusvāra set "
           "above, graced by the crescent, crowned with the praṇava (oṃ) — this "
           "is the form of your mantra. ‘Ga’ is the first part, ‘a’ the "
           "middle, the anusvāra the last, the dot beyond, the resonance the "
           "joining. Such is its euphonic union: this is the Gaṇeśa-vidyā. Its "
           "seer is Gaṇaka; its metre Nicṛd-Gāyatrī; its deity Gaṇapati. Oṃ Gaṃ, "
           "salutation to Gaṇapati."),
        _v([
            "ekadantāya vidmahe vakratuṇḍāya dhīmahi |",
            "tanno dantiḥ pracodayāt",
        ], "|| 8 ||",
           "The Gaṇeśa Gāyatrī. May we know the One-tusked; may we meditate on "
           "the Curved-trunk; may that Tusked One impel us."),
        _v([
            "ekadantaṃ caturhastaṃ pāśamaṅkuśadhāriṇam |",
            "radaṃ ca varadaṃ hastairbibhrāṇaṃ mūṣakadhvajam ||",
            "raktaṃ lambodaraṃ śūrpakarṇakaṃ raktavāsasam |",
            "raktagandhānuliptāṅgaṃ raktapuṣpaiḥ supūjitam ||",
            "bhaktānukampinaṃ devaṃ jagatkāraṇamacyutam |",
            "āvirbhūtaṃ ca sṛṣṭyādau prakṛteḥ puruṣātparam ||",
            "evaṃ dhyāyati yo nityaṃ sa yogī yogināṃ varaḥ",
        ], "|| 9 ||",
           "The meditation. One-tusked, four-handed, holding noose and goad, "
           "bearing a broken tusk and the boon-gesture in his hands, his emblem "
           "the mouse; red-hued, pot-bellied, with winnowing-fan ears, robed in "
           "red, his limbs anointed with red sandal, worshipped with red "
           "flowers; the God compassionate to devotees, cause of the world, the "
           "imperishable, manifest before creation, beyond Prakṛti and Puruṣa — "
           "whoever meditates on him thus always is a yogin, the best of "
           "yogins."),
        _v([
            "namo vrātapataye namo gaṇapataye namaḥ pramathapataye",
            "namaste'stu lambodarāyaikadantāya vighnanāśine śivasutāya",
            "śrīvaradamūrtaye namo namaḥ",
        ], "|| 10 ||",
           "The eight names. Salutation to the Lord of hosts; salutation to the "
           "Lord of the gaṇas; salutation to the Lord of the Pramathas. "
           "Salutation be to you — Pot-bellied, One-tusked, Destroyer of "
           "obstacles, Son of Śiva, the gracious boon-granting Form — salutation, "
           "salutation!"),
        _v([
            "etadatharvaśīrṣaṃ yo'dhīte |",
            "sa brahmabhūyāya kalpate ||",
            "sa sarvataḥ sukhamedhate |",
            "sa sarva vighnairnabādhyate ||",
            "sa pañcamahāpāpātpramucyate |",
            "sāyamadhīyāno divasakṛtaṃ pāpaṃ nāśayati ||",
            "prātaradhīyāno rātrikṛtaṃ pāpaṃ nāśayati |",
            "sāyamprātaḥ prayuñjāno apāpo bhavati ||",
            "sarvatrādhīyāno'pavighno bhavati |",
            "dharmārthakāmamokṣaṃ ca vindati ||",
            "idamatharvaśīrṣamaśiṣyāya na deyam |",
            "yo yadi mohāddāsyati sa pāpīyān bhavati ||",
            "sahasrāvartanādyaṃ yaṃ kāmamadhīte taṃ tamanena sādhayet",
        ], "|| 11 ||",
           "The fruits of recitation. Whoever studies this Atharvaśīrṣa becomes "
           "fit for union with Brahman. He thrives in happiness on every side; "
           "he is troubled by no obstacle; he is freed from the five great sins. "
           "Reciting it at evening, he destroys the sin done by day; reciting it "
           "at dawn, the sin done by night; reciting it dusk and dawn, he becomes "
           "free of sin. Reciting it everywhere, he becomes free of obstacles, "
           "and gains dharma, wealth, desire, and liberation. This Atharvaśīrṣa "
           "must not be given to one unworthy; whoever gives it out of delusion "
           "becomes a sinner. Whatever end one seeks by a thousand recitations, "
           "that very end one may attain by it."),
        _v([
            "anena gaṇapatimabhiṣiñcati sa vāgmī bhavati ||",
            "caturthyāmanaśnan japati sa vidyāvān bhavati |",
            "sa yaśovān bhavati |",
            "ityatharvaṇavākyam ||",
            "brahmādyācaraṇaṃ vidyāt na bibheti kadācaneti",
        ], "|| 12 ||",
           "Whoever consecrates Gaṇapati with this becomes eloquent. Whoever "
           "recites it fasting on the fourth lunar day becomes learned and "
           "renowned. So runs the Atharvaṇa saying. One who knows the way of "
           "conduct that begins with Brahman fears nothing, ever."),
        _v([
            "yo dūrvāṅkurairyajati sa vaiśravaṇopamo bhavati |",
            "yo lājairyajati sa yaśovān bhavati ||",
            "sa medhāvān bhavati |",
            "yo modakasahasreṇa yajati ||",
            "sa vāñchitaphalamavāpnoti |",
            "yaḥ sājyasamidbhiryajati ||",
            "sa sarvaṃ labhate sa sarvaṃ labhate",
        ], "|| 13 ||",
           "Whoever worships him with sprouts of dūrvā grass becomes the equal "
           "of Kubera. Whoever worships with parched grain becomes renowned, and "
           "wise. Whoever worships with a thousand modakas gains the fruit he "
           "wishes. Whoever worships with fuel-sticks and ghee gains all, gains "
           "all."),
        _v([
            "aṣṭau brāhmaṇān samyaggrāhayitvā sūryavarcasvī bhavati |",
            "sūryagrahe mahānadyāṃ pratimāsannidhau vā japtvā siddhamantro bhavati ||",
            "mahāvighnātpramucyate |",
            "mahādoṣātpramucyate ||",
            "mahāpāpāt pramucyate |",
            "sa sarvavidbhavati sa sarvavidbhavati ||",
            "ya evaṃ veda ityupaniṣat",
        ], "|| 14 ||",
           "Having duly taught it to eight brāhmaṇas, one grows radiant as the "
           "sun. Reciting it during a solar eclipse, on the bank of a great "
           "river, or before the image, one becomes a master of the mantra. He "
           "is freed from great obstacle, from great fault, from great sin. He "
           "becomes all-knowing, he becomes all-knowing — whoever knows thus. "
           "So (declares) the Upaniṣad."),
        "ornament",
        _v([
            "oṃ sahanāvavatu |",
            "sahanaubhunaktu ||",
            "saha vīryaṃ karavāvahai |",
            "tejasvināvadhītamastu mā vidviṣāvahai ||",
            "oṃ bhadraṃ karṇebhiḥ śṛṇuyāma devāḥ |",
            "bhadraṃ paśyemākṣabhiryajatrāḥ ||",
            "sthirairaṅgaistuṣṭuvāṃsastanūbhiḥ |",
            "vyaśema devahitaṃ yadāyuḥ ||",
            "oṃ svasti na indro vṛddhaśravāḥ |",
            "svasti naḥ pūṣā viśvavedāḥ ||",
            "svastinastārkṣyo ariṣṭanemiḥ |",
            "svasti no bṛhaspatirdadhātu ||",
            "oṃ śāntiḥ śāntiḥ śāntiḥ ||",
        ], "",
           "Closing śānti. Oṃ. May He protect us both; may He nourish us both; "
           "may we act together with vigour; may our study be brilliant; may we "
           "never hate each other. — And again: may we hear and see what is "
           "auspicious, praise the gods with steady limbs, and be blessed by "
           "Indra, Pūṣan, Tārkṣya, and Bṛhaspati. Oṃ, peace, peace, peace."),
    ],
}
