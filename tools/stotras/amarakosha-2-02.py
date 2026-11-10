# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Amarakośa, Sanskrit Wikisource → IAST, structured and read against the 1882 print;
# written by tools/amarakosha/gen.py. See SOURCES §5.29.

STOTRA = {
    "deity": "amarakosha",
    "doc_title": "Amarakośa · Puravarga",
    "app_title": "Amarakośa · Puravarga",
    "h1": "Amarakośa",
    "subtitle": "Bhūvargādikāṇḍa · Puravarga — towns and buildings",
    "note": "Amarasiṃha's Nāmaliṅgānuśāsana, the Amarakośa, in Sanskrit: the Sanskrit Wikisource text read against the 1882 Bombay print with Maheśvara's Amaraviveka, numbered as that print numbers it. Verses the print marks as later additions (kṣepaka) are set smaller. Translations will follow.",
    "nav": [("‹ Bhūmivarga", "amarakosha-2-01-iast.html"), ("all vargas", "amarakosha-iast.html"), ("Śailavarga ›", "amarakosha-2-03-iast.html")],
    "footer": "Source: Sanskrit Wikisource — अमरकोशः (public domain), converted to IAST; structure, kṣepakas and readings from the 1882 print (ed. Thatte under Kielhorn, Bombay; archive.org), every change listed in SOURCES §5.29; translations original",
    "sections": [
    {'padas': ['pūḥ strī purīnagaryau vā pattanaṃ puṭabhedanam |', "sthānīyaṃ nigamo'nyattu yanmūlanagarātpuram"], 'num': '|| 1 ||', 'gloss': ''},
    {'padas': ['tacchākhānagaraṃ veśo veśyājanasamāśrayaḥ |', 'āpaṇastu niṣadyāyāṃ vipaṇiḥ paṇyavīthikā'], 'num': '|| 2 ||', 'gloss': ''},
    {'padas': ['rathyā pratolī viśikhā syāccayo vapramastriyām |', 'prākāro varaṇaḥ sālaḥ prācīnaṃ prātanto vṛtiḥ'], 'num': '|| 3 ||', 'gloss': ''},
    {'padas': ['bhittiḥ strī kuḍyameḍūkaṃ yadantarnyastakīkasam |', 'gṛhaṃ gehadavasitaṃ veśma sadma niketanam'], 'num': '|| 4 ||', 'gloss': ''},
    {'padas': ['niśāntaṃ pastyasadanaṃ bhavanāgāramandiram |', 'gṛhāḥ puṃsi ca bhūmnyeva nikāyyanilayālayāḥ'], 'num': '|| 5 ||', 'gloss': ''},
    {'padas': ['vāsaḥ kuṭī dvayoḥ śālā sabhā saṃjavanaṃ tvidam |', "catuḥśālaṃ munīnāṃ tu parṇaśāloṭajo'striyām"], 'num': '|| 6 ||', 'gloss': ''},
    {'padas': ['caityamāyatanaṃ tulye vājiśālā tu mandurā |', 'āveśanaṃ śilpiśālā prapā pānīyaśālikā'], 'num': '|| 7 ||', 'gloss': ''},
    {'padas': ['maṭhaśchātrādinilayo gañjā tu madirāgṛham |', 'garbhāgāraṃ vāsagṛhamariṣṭaṃ sūtikāgṛham'], 'num': '|| 8 ||', 'gloss': ''},
    {'rubric': 'kṣepaka — an added verse, in quotation marks in the 1882 print'},
    {'padas': ["kuṭṭimo'strī nibaddhā bhūścandraśālā śirogṛham"], 'num': '', 'gloss': '', 'prose': True},
    {'padas': ["vātāyanaṃ gavākṣo'tha maṇḍapo'strī janāśrayaḥ |", 'harmyādi dhanināṃ vāsaḥ prāsādo devabhūbhujām'], 'num': '|| 9 ||', 'gloss': ''},
    {'padas': ["saudho'strī rājasadanamupakāryopakārikā |", "svastikaḥ sarvatobhadro nandyāvartādayo'pi ca"], 'num': '|| 10 ||', 'gloss': ''},
    {'padas': ['vicchandakaḥ prabhedā hi bhavantīśvarasadmanām |', 'stryagāraṃ bhūbhujāmantaḥpuraṃ syādavarodhanam'], 'num': '|| 11 ||', 'gloss': ''},
    {'padas': ['śuddhāntaścāvarodhaśca syādaṭṭaḥ kṣaumamastriyām |', 'praghāṇapraghaṇālindā bahirdvāraprakoṣṭhake'], 'num': '|| 12 ||', 'gloss': ''},
    {'padas': ['gṛhāvagrahaṇī dehalyaṅgaṇaṃ catvarājire |', 'adhastāddāruṇi śilā nāsā dārupari sthitam'], 'num': '|| 13 ||', 'gloss': ''},
    {'padas': ['pracchannamantardvāraṃ syātpakṣadvāraṃ tu pakṣakam |', "valīkanīdhre paṭalaprānte'tha paṭalaṃ chadiḥ"], 'num': '|| 14 ||', 'gloss': ''},
    {'padas': ['gopānasī tu valabhī chādane vakradāruṇi |', 'kapotapālikāyāṃ tu viṭaṅkaṃ puṃnapuṃsakam'], 'num': '|| 15 ||', 'gloss': ''},
    {'padas': ['strī dvārdvāraṃ pratīhāraḥ syāddhitardistu vedikā |', "toraṇo'strī bahirdvāraṃ puradvāraṃ tu gopuram"], 'num': '|| 16 ||', 'gloss': ''},
    {'padas': ['kūṭaṃ pūrdvāri yaddhastinakhastasminnatha triṣu |', "kapāṭamararaṃ tulye tadviṣkambho'rgalaṃ na nā"], 'num': '|| 17 ||', 'gloss': ''},
    {'padas': ['ārohaṇaṃ syātsopānaṃ niśreṇistvadhirohiṇī |', "saṃmārjanī śodhanī syātsaṃkaro'vakarastathā"], 'num': '|| 18 ||', 'gloss': ''},
    {'padas': ['kṣipte mukhaṃ niḥsaraṇaṃ saṃniveśo nikarṣaṇam |', 'samau saṃvasathagrāmau veśmabhūrvāsturastriyām'], 'num': '|| 19 ||', 'gloss': ''},
    {'padas': ['grāmānta upaśalyaṃ syātsīmasīme striyāmubhe |', 'ghoṣa ābhīrapallī syātpakkaṇaḥ śabarālayaḥ'], 'num': '|| 20 ||', 'gloss': ''},
    {'colophon': 'iti puravargaḥ ||'},
    ],
}
