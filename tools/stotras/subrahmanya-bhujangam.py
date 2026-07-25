# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain, raw wikitext) via teltools
# dev2iast, rough e-text readings normalised to standard (SOURCES §5.11).
# Translations original. Subrahmaṇya Bhujaṅgam of Ādi Śaṅkara — 33 verses
# in the Bhujaṅgaprayāta metre to Skanda / Kārttikeya (Guha, Ṣaṇmukha).

def _v(p1, p2, p3, p4, n, gloss):
    return {"padas": [p1, p2 + " |", p3, p4], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "subrahmanya",
    "doc_title": "Subrahmaṇya Bhujaṅgam",
    "app_title": "Subrahmaṇya Bhujaṅgam",
    "h1": "Śrī Subrahmaṇya Bhujaṅgam",
    "subtitle": "The Serpent-Metre Hymn to Subrahmaṇya · Ādi Śaṅkara",
    "footer": "Source: Sanskrit Wikisource — Subrahmaṇyabhujaṅgam (public domain)",
    "sections": [
        _v("sadā bālarūpāpi vighnādrihantrī",
           "mahādantivaktrāpi pañcāsyamānyā",
           "vidhīndrādimṛgyā gaṇeśābhidhā me",
           "vidhattāṃ śriyaṃ kāpi kalyāṇamūrtiḥ", 1,
           "Though ever child-like in form, she shatters the mountain of "
           "obstacles; though elephant-faced, she is honoured by the five-faced "
           "Śiva; sought by Brahmā, Indra, and the rest, bearing the name Gaṇeśa "
           "— may that indescribable, auspicious form grant me prosperity."),
        _v("na jānāmi śabdaṃ na jānāmi cārthaṃ",
           "na jānāmi padyaṃ na jānāmi gadyam",
           "cidekā ṣaḍāsyā hṛdi dyotate me",
           "mukhānniḥsarante giraścāpi citram", 2,
           "I know no word, nor do I know meaning; I know no verse, I know no "
           "prose. Yet one consciousness, six-faced, shines within my heart, and "
           "words issue wondrously from my mouth."),
        _v("mayūrādhirūḍhaṃ mahāvākyagūḍhaṃ",
           "manohāridehaṃ mahaccittageham",
           "mahīdevadevaṃ mahāvedabhāvaṃ",
           "mahādevabālaṃ bhaje lokapālam", 3,
           "Mounted on the peacock, hidden within the great Vedic sayings; "
           "enchanting of body, dwelling in the great heart; god of the gods of "
           "earth, the very being of the great Vedas — the child of Mahādeva I "
           "worship, protector of the worlds."),
        _v("yadā sannidhānaṃ gatā mānavā me",
           "bhavāmbhodhipāraṃ gatāste tadaiva",
           "iti vyañjayansindhutīre ya āste",
           "tamīḍe pavitraṃ parāśaktiputram", 4,
           "The moment people drew near me, that very moment they reached the "
           "far shore of the ocean of birth — revealing this, he abides on the "
           "sea-shore: him I praise, the pure son of the Supreme Śakti."),
        _v("yathābdhestaraṅgā layaṃ yānti tuṅgāḥ",
           "tathaivāpadaḥ sannidhau sevatāṃ me",
           "itīvormipaṅktīrnṛṇāṃ darśayantaṃ",
           "sadā bhāvaye hṛtsaroje guhaṃ tam", 5,
           "As the ocean's towering waves sink to rest, so too the calamities of "
           "those who serve in my presence — as though showing this to men by "
           "his rows of waves: on that Guha I ever meditate in my heart's "
           "lotus."),
        _v("girau mannivāse narā ye'dhirūḍhāḥ",
           "tadā parvate rājate te'dhirūḍhāḥ",
           "itīva bruvangandhaśailādhirūḍhaḥ",
           "sa devo mude me sadā ṣaṇmukho'stu", 6,
           "Those who have climbed the hill where I dwell have thereby climbed "
           "the silver mountain (Kailāsa) — as if declaring this, seated upon "
           "the fragrant hill: may that six-faced god be ever for my joy."),
        _v("mahāmbhodhitīre mahāpāpacore",
           "munīndrānukūle sugandhākhyaśaile",
           "guhāyāṃ vasantaṃ svabhāsā lasantaṃ",
           "janārtiṃ harantaṃ śrayāmo guhaṃ tam", 7,
           "On the shore of the great ocean, thief of great sins, gracious to "
           "the chief of sages, on the hill named Sugandha — dwelling in a cave, "
           "shining with his own light, taking away the affliction of men: to "
           "that Guha we take refuge."),
        _v("lasatsvarṇagehe nṛṇāṃ kāmadohe",
           "sumastomasaṃchannamāṇikyamañce",
           "samudyatsahasrārkatulyaprakāśaṃ",
           "sadā bhāvaye kārtikeyaṃ sureśam", 8,
           "In a gleaming golden mansion, the wish-granting cow of men, on a ruby "
           "throne canopied with masses of flowers, blazing like a thousand "
           "rising suns — I ever meditate on Kārttikeya, lord of the gods."),
        _v("raṇaddhaṃsake mañjule'tyantaśoṇe",
           "manohārilāvaṇyapīyūṣapūrṇe",
           "manaḥṣaṭpado me bhavatkleśataptaḥ",
           "sadā modatāṃ skanda te pādapadme", 9,
           "On your lotus feet — anklets softly ringing, lovely, deeply crimson, "
           "brimming with the nectar of heart-stealing grace — may the bee of my "
           "mind, scorched by the pain (of separation), ever take its delight, O "
           "Skanda."),
        _v("suvarṇābhadivyāmbarairbhāsamānāṃ",
           "kvaṇatkiṅkiṇīmekhalāśobhamānām",
           "lasaddhemapaṭṭena vidyotamānāṃ",
           "kaṭiṃ bhāvaye skanda te dīpyamānām", 10,
           "Radiant with divine, gold-hued garments, lovely with a girdle of "
           "tinkling bells, shining with a gleaming band of gold — I meditate on "
           "your waist, O Skanda, ablaze with light."),
        _v("pulindeśakanyāghanābhogatuṅga",
           "stanāliṅganāsaktakāśmīrarāgam",
           "namasyāmahaṃ tārakāre tavoraḥ",
           "svabhaktāvane sarvadā sānurāgam", 11,
           "I bow to your chest, O foe of Tāraka — reddened with saffron from "
           "clinging to the full, high breasts of the huntress-maiden (Vallī), "
           "and ever tender in the protection of your devotees."),
        _v("vidhau kḷptadaṇḍānsvalīlādhṛtāṇḍān",
           "nirastebhaśuṇḍāndviṣatkāladaṇḍān",
           "hatendrāriṣaṇḍāñjagatrāṇaśauṇḍān",
           "sadā te pracaṇḍāñśraye bāhudaṇḍān", 12,
           "I ever take refuge in your fierce staff-like arms — which set bounds "
           "even for Brahmā, which bore the cosmic egg in play, which outdo the "
           "elephant's trunk, which are a rod of Death to foes, which slew the "
           "host of Indra's enemies, valiant in guarding the world."),
        _v("sadā śāradāḥ ṣaṇmṛgāṅkā yadi syuḥ",
           "samudyanta eva sthitāścetsamantāt",
           "sadā pūrṇabimbāḥ kalaṅkaiśca hīnāḥ",
           "tadā tvanmukhānāṃ bruve skanda sāmyam", 13,
           "If there were six autumn moons, all newly risen and standing on every "
           "side, ever full-orbed and free of every spot — then, O Skanda, I "
           "might speak of their likeness to your (six) faces."),
        _v("sphuranmandahāsaiḥ sahaṃsāni cañcat",
           "kaṭākṣāvalībhṛṅgasaṃghojjvalāni",
           "sudhāsyandibimbādharāṇīśasūno",
           "tavālokaye ṣaṇmukhāmbhoruhāṇi", 14,
           "O son of Īśa, I gaze on your six lotus-faces — bright with flashing "
           "gentle smiles like swans, ablaze with the swarm of bees that are "
           "your darting glances, their bimba-red lips dripping nectar."),
        _v("viśāleṣu karṇāntadīrgheṣvajasraṃ",
           "dayāsyandiṣu dvādaśasvīkṣaṇeṣu",
           "mayīṣatkaṭākṣaḥ sakṛtpātitaścet",
           "bhavette dayāśīla kā nāma hāniḥ", 15,
           "From your twelve eyes — wide, drawn long to the ears, ceaselessly "
           "streaming compassion — if but once a slight sidelong glance fall "
           "upon me, O compassionate one, what loss, pray, is that to you?"),
        _v("sutāṅgodbhavo me'si jīveti ṣaḍdhā",
           "japanmantramīśo mudā cighrate yān",
           "jagadbhārabhṛdbhyo jagannātha tebhyaḥ",
           "kirīṭojjvalebhyo namo mastakebhyaḥ", 16,
           "'You are born of my body; live long!' — so, joyfully uttering the "
           "six-fold mantra, Īśa kisses those heads. O Lord of the world, to "
           "those heads of yours, bearers of the world's burden and bright with "
           "crowns, salutation."),
        _v("sphuradratnakeyūrahārābhirāmaḥ",
           "calatkuṇḍalaśrīlasadgaṇḍabhāgaḥ",
           "kaṭau pītavāsāḥ kare cāruśaktiḥ",
           "purastānmamāstāṃ purārestanūjaḥ", 17,
           "Lovely with flashing jewelled armlets and necklaces, his cheeks "
           "bright with the splendour of swaying earrings, yellow-robed at the "
           "waist, a fair spear in his hand — may the son of the foe of the "
           "cities (Śiva) stand before me."),
        _v("ihāyāhi vatseti hastānprasārya",
           "āhvayatyādarācchaṃkare māturaṅkāt",
           "samutpatya tātaṃ śrayantaṃ kumāraṃ",
           "harāśliṣṭagātraṃ bhaje bālamūrtim", 18,
           "'Come here, child!' — when Śaṅkara, stretching out his hands, "
           "lovingly calls him from his mother's lap, the boy springs up and "
           "clings to his father: that child-form, his body embraced by Hara, I "
           "worship."),
        _v("kumāreśasūno guha skanda senā",
           "pate śaktipāṇe mayūrādhirūḍha",
           "pulindātmajākānta bhaktārtihārin",
           "prabho tārakāre sadā rakṣa māṃ tvam", 19,
           "O Guha, Skanda, ever-youthful lord, commander of the army, spear in "
           "hand, mounted on the peacock; O beloved of the huntress's daughter, "
           "remover of devotees' distress; O Lord, foe of Tāraka — ever protect "
           "me."),
        _v("praśāntendriye naṣṭasaṃjñe viceṣṭe",
           "kaphodgārivaktre bhayotkampigātre",
           "prayāṇonmukhe mayyanāthe tadānīṃ",
           "drutaṃ me dayālo bhavāgre guhaṃ tvam", 20,
           "When my senses are stilled, awareness lost, limbs motionless, mouth "
           "spilling phlegm, body trembling with fear, and I set out helpless "
           "(in death) — then, O compassionate Guha, swiftly stand before me."),
        _v("kṛtāntasya dūteṣu caṇḍeṣu kopāt",
           "daha cchinddhi bhinddhīti māṃ tarjayatsu",
           "mayūraṃ samāruhya mā bhairiti tvaṃ",
           "puraḥ śaktipāṇirmamāyāhi śīghram", 21,
           "When the fierce messengers of Death, in wrath, threaten me — 'burn! "
           "cut! split!' — then you, mounting your peacock, spear in hand, "
           "saying 'fear not,' come swiftly before me."),
        _v("praṇamyāsakṛtpādayoste patitvā",
           "prasādya prabho prārthaye'nekavāram",
           "na vaktuṃ kṣamo'haṃ tadānīṃ kṛpābdhe",
           "na kāryāntakāle manāgapyupekṣā", 22,
           "Bowing again and again, falling at your feet, propitiating you, O "
           "Lord, I beg many times over: I shall not be able to speak then (at "
           "death), O ocean of grace — so at my final hour show not the least "
           "neglect."),
        _v("sahasrāṇḍabhoktā tvayā śūranāmā",
           "hatastārakaḥ siṃhavaktraśca daityaḥ",
           "mamāntarhṛdisthaṃ manaḥkleśamekaṃ",
           "na haṃsi prabho kiṃ karomi kva yāmi", 23,
           "By you the demon named Śūra, devourer of a thousand worlds, was "
           "slain, and Tāraka, and the lion-faced demon — yet the one grief "
           "lodged deep within my heart you do not slay, O Lord. What shall I "
           "do? Where shall I go?"),
        _v("ahaṃ sarvadā duḥkhabhārāvasanno",
           "bhavāndīnabandhustvadanyaṃ na yāce",
           "bhavadbhaktirodhaṃ sadā klṛptabādhaṃ",
           "mamādhiṃ drutaṃ nāśayomāsuta tvam", 24,
           "I am forever sunk beneath a load of sorrow; you are the friend of "
           "the wretched — I beg of none but you. O son of Umā, swiftly destroy "
           "my anguish, which ever obstructs devotion to you and works me "
           "harm."),
        _v("apasmārakuṣṭhakṣayārśaḥprameha",
           "jvaronmādigulmādirogā mahāntaḥ",
           "piśācāśca sarve bhavatpatrabhūtiṃ",
           "vilokya kṣaṇāttārakāre dravante", 25,
           "Epilepsy, leprosy, consumption, piles, diabetes, fever, madness, "
           "tumours, and other great diseases, and all the demons — beholding "
           "the ash of your leaf-offering, O foe of Tāraka, flee in an instant."),
        _v("dṛśi skandamūrtiḥ śrutau skandakīrtiḥ",
           "mukhe me pavitraṃ sadā taccaritram",
           "kare tasya kṛtyaṃ vapustasya bhṛtyaṃ",
           "guhe santu līnā mamāśeṣabhāvāḥ", 26,
           "Skanda's form in my sight, Skanda's glory in my ears, ever his holy "
           "story in my mouth; his service the work of my hands, my body his "
           "servant — may all my faculties, O Guha, be dissolved into you."),
        _v("munīnāmutāho nṛṇāṃ bhaktibhājāṃ",
           "abhīṣṭapradāḥ santi sarvatra devāḥ",
           "nṛṇāmantyajānāmapi svārthadāne",
           "guhāddevamanyaṃ na jāne na jāne", 27,
           "For sages and for devout men, gods everywhere grant desired boons; "
           "but for bestowing the true good even on the lowest of men, a god "
           "other than Guha I know not — I know not."),
        _v("kalatraṃ sutā bandhuvargaḥ paśurvā",
           "naro vātha nārī gṛhe ye madīyāḥ",
           "yajanto namantaḥ stuvanto bhavantaṃ",
           "smarantaśca te santu sarve kumāra", 28,
           "Wife, children, kinsfolk, cattle, and whoever in my house is mine, "
           "man or woman — may they all, O Kumāra, be ever worshipping, bowing "
           "to, praising, and remembering you."),
        _v("mṛgāḥ pakṣiṇo daṃśakā ye ca duṣṭāḥ",
           "tathā vyādhayo bādhakā ye madaṅge",
           "bhavacchaktitīkṣṇāgrabhinnāḥ sudūre",
           "vinaśyantu te cūrṇitakrauñcaśaile", 29,
           "Beasts, birds, biting things, and the wicked, and the diseases that "
           "afflict my body — pierced by the sharp point of your spear, may they "
           "perish far away, O you who ground Mount Krauñca to dust."),
        _v("janitrī pitā ca svaputrāparādhaṃ",
           "sahete na kiṃ devasenādhinātha",
           "ahaṃ cātibālo bhavānlokatātaḥ",
           "kṣamasvāparādhaṃ samastaṃ maheśa", 30,
           "Do not a mother and father bear their own child's every fault, O "
           "lord of the gods' army? I am but a small child, and you are the "
           "father of the world — forgive, O great Lord, my every offence."),
        _v("namaḥ kekine śaktaye cāpi tubhyaṃ",
           "namaśca tubhyaṃ namaḥ kukkuṭāya",
           "namaḥ sindhave sindhudeśāya tubhyaṃ",
           "punaḥ skandamūrte namaste namo'stu", 31,
           "Salutation to the peacock, and to the spear; salutation to you, "
           "salutation to the rooster (of your banner); salutation to the ocean "
           "and to the sea-land; again, O form of Skanda, salutation, "
           "salutation to you."),
        _v("jayānandabhūmanjayāpāradhāman",
           "jayāmoghakīrte jayānandamūrte",
           "jayānandasindho jayāśeṣabandho",
           "jaya tvaṃ pitā muktidāneśasūno", 32,
           "Victory, O ground of bliss! Victory, O boundless abode! Victory, O "
           "of unfailing fame! Victory, O embodiment of joy! Victory, O ocean of "
           "bliss! Victory, O kinsman of all! Victory to you, our father, O son "
           "of the Lord who grants liberation!"),
        "ornament",
        _v("bhujaṅgākhyavṛttena klṛptaṃ stavaṃ yaḥ",
           "paṭhedbhaktiyukto guhaṃ saṃpraṇamya",
           "sa putrānkalatraṃ dhanaṃ dīrghamāyuḥ",
           "labhetskandasāyujyamante naraḥ saḥ", 33,
           "The man who, filled with devotion, recites this hymn composed in the "
           "serpent (Bhujaṅgaprayāta) metre, having bowed low to Guha, gains "
           "sons, wife, wealth, and long life, and at the end union with "
           "Skanda."),
    ],
}
