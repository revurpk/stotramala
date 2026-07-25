# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain, raw wikitext) via teltools
# dev2iast, rough OCR readings normalised (SOURCES §5.13). Translations
# original. Rāma Rakṣā Stotram of Budha Kauśika — a protective armour
# (kavaca) hymn to Śrī Rāma.

def _v(segs, n, gloss):
    lines = [s + " |" for s in segs[:-1]] + [segs[-1]]
    return {"padas": lines, "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "rama",
    "doc_title": "Rāma Rakṣā Stotram",
    "app_title": "Rāma Rakṣā",
    "h1": "Śrī Rāma Rakṣā Stotram",
    "subtitle": "The Armour of Rāma · Budha Kauśika",
    "footer": "Source: Sanskrit Wikisource — Rāmarakṣāstotram (public domain)",
    "sections": [
        _v(["caritaṃ raghunāthasya śatakoṭipravistaram",
            "ekaikamakṣaram puṃsāṃ mahāpātakanāśanam"], 1,
           "The story of Raghunātha is spread over a hundred crore verses; each "
           "single syllable of it destroys the greatest of sins."),
        _v(["dhyātvā nīlotpalaśyāmaṃ rāmaṃ rājīvalocanam",
            "jānakīlakṣmaṇopetaṃ jaṭāmukuṭamaṇḍitam"], 2,
           "Having meditated on Rāma — dark as the blue lotus, lotus-eyed, "
           "accompanied by Jānakī and Lakṣmaṇa, adorned with a crown of matted "
           "hair —"),
        _v(["sāsitūṇadhanurbāṇapāṇiṃ naktaṃcarāntakam",
            "svalīlayā jagattrātumāvirbhūtamajaṃ vibhum"], 3,
           "bearing sword, quiver, bow, and arrow in hand, the ender of the "
           "night-rangers, who unborn and all-pervading appeared, by his own "
           "play, to protect the world —"),
        _v(["rāmarakṣāṃ paṭhet prājñaḥ pāpaghnīṃ sarvakāmadām",
            "śiro me rāghavaḥ pātu bhālaṃ daśarathātmajaḥ"], 4,
           "let the wise recite the Rāma-rakṣā, destroyer of sin, granter of all "
           "desires. May Rāghava guard my head; may the son of Daśaratha guard "
           "my forehead."),
        _v(["kausalyeyo dṛśau pātu viśvāmitrapriyaḥ śrutī",
            "ghrāṇaṃ pātu makhatrātā mukhaṃ saumitrivatsalaḥ"], 5,
           "May the son of Kausalyā guard my eyes; the beloved of Viśvāmitra, my "
           "ears; the protector of the sacrifice, my nose; he dear to Sumitrā's "
           "son, my face."),
        _v(["jihvāṃ vidyānidhiḥ pātu kaṇṭhaṃ bharatavanditaḥ",
            "skandhau divyāyudhaḥ pātu bhujau bhagneśakārmukaḥ"], 6,
           "May the treasury of knowledge guard my tongue; he whom Bharata "
           "worships, my throat; the bearer of divine weapons, my shoulders; the "
           "breaker of Īśa's bow, my arms."),
        _v(["karau sitāpatiḥ pātu hṛdayaṃ jāmadagnyajit",
            "madhyaṃ pātu kharadhvaṃsī nābhiṃ jāmbavadāśrayaḥ"], 7,
           "May the lord of Sītā guard my hands; the conqueror of Jāmadagnya "
           "(Paraśurāma), my heart; the slayer of Khara, my waist; the refuge of "
           "Jāmbavat, my navel."),
        _v(["sugrīveśaḥ kaṭī pātu sakthinī hanumatprabhuḥ",
            "ūrū raghūttamaḥ pātu rakṣaḥkulavināśakṛt"], 8,
           "May the lord of Sugrīva guard my hips; the master of Hanumān, my "
           "loins; the best of Raghus, destroyer of the demon race, my thighs."),
        _v(["jānunī setukṛtpātu jaṃghe daśamukhāntakaḥ",
            "pādau bibhīṣaṇaśrīdaḥ pātu rāmo'khilaṃ vapuḥ"], 9,
           "May the builder of the bridge guard my knees; the ender of the "
           "ten-faced (Rāvaṇa), my shanks; the giver of fortune to Vibhīṣaṇa, my "
           "feet; may Rāma guard my whole body."),
        _v(["etāṃ rāmabalopetāṃ rakṣāṃ yaḥ sukṛtī paṭhet",
            "sa cirāyuḥ sukhī putrī vijayī vinayī bhavet"], 10,
           "The virtuous one who recites this Rāma-rakṣā, endowed with Rāma's "
           "power, becomes long-lived, happy, blessed with sons, victorious, and "
           "modest."),
        _v(["pātālabhūtalavyomacāriṇaśchadmacāriṇaḥ",
            "na draṣṭumapi śaktāste rakṣitaṃ rāmanāmabhiḥ"], 11,
           "Those roaming the underworld, the earth, and the sky, and those who "
           "move in disguise — they cannot even look upon one guarded by the "
           "names of Rāma."),
        _v(["rāmeti rāmabhadreti rāmacandreti vā smaran",
            "naro na lipyate pāpairbhuktiṃ muktiṃ ca vindati"], 12,
           "Remembering 'Rāma,' or 'Rāmabhadra,' or 'Rāmacandra,' a man is not "
           "stained by sins, and gains both enjoyment and liberation."),
        _v(["jagajjaitraikamantreṇa rāmanāmābhirakṣitam",
            "yaḥ kaṇṭhe dhārayettasya karasthāḥ sarvasiddhayaḥ"], 13,
           "For whoever wears at his throat this (hymn), guarded by Rāma's name, "
           "the one mantra that conquers the world — all attainments rest in the "
           "palm of his hand."),
        _v(["vajrapañjaranāmedaṃ yo rāmakavacaṃ smaret",
            "avyāhatājñaḥ sarvatra labhate jayamaṅgalam"], 14,
           "Whoever remembers this armour of Rāma, named 'the Adamantine Cage,' "
           "becomes one whose command is everywhere unobstructed, and gains "
           "victory and blessing."),
        _v(["ādiṣṭavān yathā svapne rāmarakṣāmimāṃ haraḥ",
            "tathā likhitavān prātaḥ prabuddho budhakauśikaḥ"], 15,
           "As Hara (Śiva) commanded this Rāma-rakṣā in a dream, so, awaking at "
           "dawn, Budha Kauśika wrote it down."),
        _v(["ārāmaḥ kalpavṛkṣāṇāṃ virāmaḥ sakalāpadām",
            "abhirāmastrilokānāṃ rāmaḥ śrīmān sa naḥ prabhuḥ"], 16,
           "A garden of wish-fulfilling trees, the ceasing of all calamities, "
           "the delight of the three worlds — Rāma, the glorious, is our Lord."),
        _v(["taruṇau rūpasaṃpannau sukumārau mahābalau",
            "puṇḍarīkaviśālākṣau cīrakṛṣṇājināmbarau"], 17,
           "Young, endowed with beauty, delicate yet mighty, with wide lotus "
           "eyes, clad in bark and black-deer skin —"),
        _v(["phalamūlāśinau dāntau tāpasau brahmacāriṇau",
            "putrau daśarathasyaitau bhrātarau rāmalakṣmaṇau"], 18,
           "eating fruit and roots, self-controlled ascetics and celibates — "
           "these two sons of Daśaratha, the brothers Rāma and Lakṣmaṇa."),
        _v(["śaraṇyau sarvasattvānāṃ śreṣṭhau sarvadhanuṣmatām",
            "rakṣaḥ kulanihantārau trāyetāṃ no raghūttamau"], 19,
           "The refuge of all beings, the best of all who bear the bow, slayers "
           "of the demon race — may those two best of Raghus protect us."),
        _v(["āttasajyadhanuṣāviṣuspṛśāvakṣayāśuganiṣaṅgasaṅginau",
            "rakṣaṇāya mama rāmalakṣmaṇāvagrataḥ pathi sadaiva gacchatām"], 20,
           "With strung bows, touching their arrows, bearing inexhaustible "
           "quivers — may Rāma and Lakṣmaṇa ever walk before me on the path, for "
           "my protection."),
        _v(["saṃnaddhaḥ kavacī khaḍgī cāpabāṇadharo yuvā",
            "gacchan manoratho'smākaṃ rāmaḥ pātu salakṣmaṇaḥ"], 21,
           "Armoured, girded, bearing sword, bow, and arrow, the youthful Rāma "
           "with Lakṣmaṇa, going forth — may he, our very heart's wish, protect "
           "us."),
        _v(["rāmo dāśarathiḥ śūro lakṣmaṇānucaro balī",
            "kākutsthaḥ puruṣaḥ pūrṇaḥ kausalyeyo raghūttamaḥ"], 22,
           "Rāma, son of Daśaratha, valiant, followed by Lakṣmaṇa, mighty; "
           "Kākutstha, the perfect Puruṣa, son of Kausalyā, best of Raghus;"),
        _v(["vedāntavedyo yajñeśaḥ purāṇapuruṣottamaḥ",
            "jānakīvallabhaḥ śrīmānaprameyaparākramaḥ"], 23,
           "knowable through Vedānta, lord of sacrifice, the ancient Supreme "
           "Person, beloved of Jānakī, glorious, of immeasurable prowess —"),
        _v(["ityetāni japan nityaṃ madbhaktaḥ śraddhayānvitaḥ",
            "aśvamedhādhikaṃ puṇyaṃ saṃprāpnoti na saṃśayaḥ"], 24,
           "reciting these (names) daily, My devotee, filled with faith, gains "
           "merit greater than the Aśvamedha; of this there is no doubt."),
        _v(["rāmaṃ dūrvādalaśyāmaṃ padmākṣaṃ pītavāsasam",
            "stuvanti nāmabhirdivyaiḥ na te saṃsāriṇo naraḥ"], 25,
           "Those who praise with divine names Rāma — dark as a dūrvā-blade, "
           "lotus-eyed, clad in yellow — such men are no longer bound to "
           "saṃsāra."),
        _v(["rāmaṃ lakṣmaṇapūrvajaṃ raghuvaraṃ sītāpatiṃ sundaraṃ",
            "kākutsthaṃ karuṇārṇavaṃ guṇanidhiṃ viprapriyaṃ dhārmikam",
            "rājendraṃ satyasandhaṃ daśarathanayaṃ śyāmalaṃ śāntamūrtiṃ",
            "vande lokābhirāmaṃ raghukulatilakaṃ rāghavaṃ rāvaṇārim"], 26,
           "I bow to Rāma — elder brother's-junior to Lakṣmaṇa, best of Raghus, "
           "lord of Sītā, beautiful; Kākutstha, ocean of compassion, treasury of "
           "virtues, dear to brāhmaṇas, righteous; king of kings, true to his "
           "word, son of Daśaratha, dark, of serene form; the world's delight, "
           "ornament of the Raghu line, Rāghava, foe of Rāvaṇa."),
        _v(["rāmāya rāmabhadrāya rāmacandrāya vedhase",
            "raghunāthāya nāthāya sītāyāḥ pataye namaḥ"], 27,
           "To Rāma, to Rāmabhadra, to Rāmacandra the ordainer, to Raghunātha "
           "the Lord, the husband of Sītā — salutation."),
        _v(["śrīrāma rāma raghunandana rāma rāma",
            "śrīrāma rāma bharatāgraja rāma rāma",
            "śrīrāma rāma raṇakarkaśa rāma rāma",
            "śrīrāma rāma śaraṇaṃ bhava rāma rāma"], 28,
           "O Śrī Rāma, Rāma, delight of the Raghus, Rāma Rāma! O Śrī Rāma, Rāma, "
           "elder of Bharata, Rāma Rāma! O Śrī Rāma, Rāma, fierce in battle, Rāma "
           "Rāma! O Śrī Rāma, Rāma, be my refuge, Rāma Rāma!"),
        _v(["śrīrāmacandracaraṇau manasā smarāmi",
            "śrīrāmacandracaraṇau vacasā gṛṇāmi",
            "śrīrāmacandracaraṇau śirasā namāmi",
            "śrīrāmacandracaraṇau śaraṇaṃ prapadye"], 29,
           "The feet of Śrī Rāmacandra I remember with my mind; the feet of Śrī "
           "Rāmacandra I praise with my speech; the feet of Śrī Rāmacandra I bow "
           "to with my head; to the feet of Śrī Rāmacandra I go for refuge."),
        _v(["mātā rāmo matpitā rāmacandraḥ",
            "svāmī rāmo matsakhā rāmacandraḥ",
            "sarvasvaṃ me rāmacandro dayālurnānyaṃ",
            "jāne naiva jāne na jāne"], 30,
           "Rāma is my mother, Rāmacandra my father; Rāma is my master, "
           "Rāmacandra my friend; the compassionate Rāmacandra is my all — I "
           "know no other, know none at all, none."),
        _v(["dakṣiṇe lakṣmaṇo yasya vāme tu janakātmajā",
            "purato mārutiryasya taṃ vande raghunandanam"], 31,
           "He on whose right is Lakṣmaṇa, on whose left is Janaka's daughter, "
           "and before whom is Māruti (Hanumān) — to that delight of the Raghus "
           "I bow."),
        _v(["lokābhirāmaṃ raṇaraṅgadhīraṃ rājīvanetraṃ raghuvaṃśanātham",
            "kāruṇyarūpaṃ karuṇākaraṃ taṃ śrīrāmacandraṃ śaraṇaṃ prapadye"], 32,
           "The delight of the world, steadfast on the field of battle, "
           "lotus-eyed, lord of the Raghu line, the very form of compassion, "
           "mine of mercy — to that Śrī Rāmacandra I go for refuge."),
        _v(["manojavaṃ mārutatulyavegaṃ",
            "jitendriyaṃ buddhimatāṃ variṣṭhaṃ",
            "vātātmajaṃ vānarayūthamukhyaṃ",
            "śrīrāmadūtaṃ śaraṇaṃ prapadye"], 33,
           "Swift as the mind, equal in speed to the wind, master of the senses, "
           "foremost of the wise, son of the wind, chief of the monkey-hosts, "
           "the messenger of Śrī Rāma — to him I go for refuge."),
        _v(["kūjantaṃ rāmarāmeti madhuraṃ madhurākṣaram",
            "āruhya kavitāśākhāṃ vande vālmīkikokilam"], 34,
           "Cooing 'Rāma, Rāma,' sweet and of sweet syllables, perched upon the "
           "branch of poetry — I salute Vālmīki, the cuckoo."),
        _v(["āpadāmapahartāraṃ dātāraṃ sarvasaṃpadām",
            "lokābhirāmaṃ śrīrāmaṃ bhūyo bhūyo namāmyaham"], 35,
           "The remover of calamities, the giver of all prosperity, the delight "
           "of the world, Śrī Rāma — again and again I bow to him."),
        _v(["bharjanaṃ bhavabījānāmarjanaṃ sukhasaṃpadām",
            "tarjanaṃ yamadūtānāṃ rāmarāmeti garjanam"], 36,
           "The roasting of the seeds of rebirth, the winning of joy and wealth, "
           "the terror of Yama's messengers — such is the roar of 'Rāma, Rāma.'"),
        _v(["rāmo rājamaṇiḥ sadā vijayate rāmaṃ rameśaṃ bhaje",
            "rāmeṇābhihatā niśācaracamū rāmāya tasmai namaḥ",
            "rāmānnāsti parāyaṇaṃ parataraṃ rāmasya dāso'smyahaṃ",
            "rāme cittalayaḥ sadā bhavatu bho rāma māmuddhara"], 37,
           "Rāma, jewel of kings, is ever victorious; Rāma, lord of Ramā, I "
           "worship; by Rāma the host of demons was struck down — to that Rāma, "
           "salutation. There is no refuge higher than Rāma; I am Rāma's "
           "servant; may my mind be ever absorbed in Rāma — O Rāma, lift me up!"),
        _v(["rāmanāmeti rāmeti rame rāme manorame",
            "sahasranāma tattulyaṃ rāmanāma varānane"], 38,
           "Delighting in 'Rāma-nāma,' in 'Rāma,' in the delightful Rāma — the "
           "name of Rāma is equal to the thousand names, O fair-faced one."),
    ],
}
