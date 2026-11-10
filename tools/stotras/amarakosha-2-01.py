# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Amarakośa, Sanskrit Wikisource → IAST, structured and read against the 1882 print;
# written by tools/amarakosha/gen.py. See SOURCES §5.29.

STOTRA = {
    "deity": "amarakosha",
    "doc_title": "Amarakośa · Bhūmivarga",
    "app_title": "Amarakośa · Bhūmivarga",
    "h1": "Amarakośa",
    "subtitle": "Bhūvargādikāṇḍa · Bhūmivarga — the earth and its lands",
    "note": "Amarasiṃha's Nāmaliṅgānuśāsana, the Amarakośa, in Sanskrit: the Sanskrit Wikisource text read against the 1882 Bombay print with Maheśvara's Amaraviveka, numbered as that print numbers it. Verses the print marks as later additions (kṣepaka) are set smaller. Translations will follow.",
    "nav": [("‹ Vārivarga", "amarakosha-1-11-iast.html"), ("all vargas", "amarakosha-iast.html"), ("Puravarga ›", "amarakosha-2-02-iast.html")],
    "footer": "Source: Sanskrit Wikisource — अमरकोशः (public domain), converted to IAST; structure, kṣepakas and readings from the 1882 print (ed. Thatte under Kielhorn, Bombay; archive.org), every change listed in SOURCES §5.29; translations original",
    "sections": [
    {'heading': 'Vargabheda · the vargas of this kāṇḍa'},
    {'padas': ['vargāḥ pṛthvīpurakṣmābhṛdvanauṣadhimṛgādibhiḥ |', 'nṛbrahmakṣatraviṭśūdraiḥ sāṅgopāṅgairihoditāḥ'], 'num': '|| 1 ||', 'gloss': ''},
    {'heading': 'Bhūmi · the earth'},
    {'padas': ['bhūrbhūmiracalānantā rasā viśvambharā sthitā |', 'dharā dharitrī dharaṇiḥ kṣoṇirjyā kāśyapī kṣitiḥ'], 'num': '|| 2 ||', 'gloss': ''},
    {'padas': ['sarvaṃsahā vasumatī vasudhorvī vasundharā |', 'gotrā kuḥ pṛthivī pṛthvī kṣmāvanirmedinī mahī'], 'num': '|| 3 ||', 'gloss': ''},
    {'rubric': 'kṣepaka — an added verse, in quotation marks in the 1882 print'},
    {'padas': ['vipulā gahvarī dhātrī gaurilā kumbhinī kṣamā |', 'bhūtadhātrī ratnagarbhā jagatī sāgarāmbarā'], 'num': '', 'gloss': '', 'prose': True},
    {'padas': ['mṛnmṛttikā praśastā tu mṛtsā mṛtsnā ca mṛttikā |', 'urvarā sarvasasyāḍhyā syādūṣaḥ kṣāramṛttikā'], 'num': '|| 4 ||', 'gloss': ''},
    {'padas': ['ūṣavānūṣaro dvāvapyanyaliṅgau sthalaṃ sthalī |', 'samānau marudhanvānau dve khilāprahate same'], 'num': '|| 5 ||', 'gloss': ''},
    {'padas': ['triṣvatho jagatī loko viṣṭapaṃ bhuvanaṃ jagat |', "loko'yaṃ bhārataṃ varṣaṃ śarāvatyāstu yo'vadheḥ"], 'num': '|| 6 ||', 'gloss': ''},
    {'padas': ['deśaḥ prāgdakṣiṇaḥ prācya udīcyaḥ paścimottaraḥ |', 'pratyanto mlecchadeśaḥ syānmadhyaddeśastu madhyamaḥ'], 'num': '|| 7 ||', 'gloss': ''},
    {'padas': ['āryāvartaḥ puṇyabhūmirmadhyaṃ vindhyahimālayoḥ |', "nīvṛjjanapado deśaviṣayau tū'pavartanam"], 'num': '|| 8 ||', 'gloss': ''},
    {'padas': ['triṣvāgoṣṭhānnaḍaprāye naḍvānnaḍvala ityapi |', 'kumudvānkumudaprāye vetasvānbahuvetase'], 'num': '|| 9 ||', 'gloss': ''},
    {'padas': ['śādvalaḥ śādaharite sajambāle tu paṅkilaḥ |', 'jalaprāyamanūpaṃ syātpuṃsi kacchastathāvidhaḥ'], 'num': '|| 10 ||', 'gloss': ''},
    {'padas': ['strī śarkarā śarkarilaḥ śārkaraḥ śarkarāvati |', 'deśa evādimāvevamunneyāḥ sikatāvati'], 'num': '|| 11 ||', 'gloss': ''},
    {'padas': ['deśo nadyambuvṛṣṭyambusaṃpannavrīhipālitaḥ |', 'syānnadīmātṛko devamātṛkaśca yathākramam'], 'num': '|| 12 ||', 'gloss': ''},
    {'padas': ["surājñi deśe rājanvānsyāttato'nyatra rājavān |", 'goṣṭhaṃ gosthānakaṃ tattu gauṣṭhīnaṃ bhūtapūrvakam'], 'num': '|| 13 ||', 'gloss': ''},
    {'padas': ['paryantabhūḥ parisaraḥ seturālau striyāṃ pumān |', 'vāmalūraśca nākuśca valmīkaṃ puṃnapuṃsakam'], 'num': '|| 14 ||', 'gloss': ''},
    {'padas': ['ayanaṃ vartma mārgādhvapanthānaḥ padavī sṛtiḥ |', 'saraṇiḥ paddhatiḥ padyā vartanyekapadīti ca'], 'num': '|| 15 ||', 'gloss': ''},
    {'padas': ["atipanthāḥ supanthāśca satpathaścārcite'dhvani |", 'vyadhvo duradhvo vipathaḥ kadadhvā kāpathaḥ samāḥ'], 'num': '|| 16 ||', 'gloss': ''},
    {'padas': ['apanthāstvapathaṃ tulye śṛṇgāṭakacatuṣpathe |', "prāntaraṃ dūraśūnyo'dhvā kāntāraṃ vartma durgamam"], 'num': '|| 17 ||', 'gloss': ''},
    {'padas': ['gavyūtiḥ strī krośayugaṃ nalvaḥ kiṣkucatuḥśatam |', 'ghaṇṭāpathaḥ saṃsaraṇaṃ tatpurasyopaniṣkaram'], 'num': '|| 18 ||', 'gloss': ''},
    {'rubric': 'kṣepaka — an added verse, in quotation marks in the 1882 print'},
    {'padas': ['dyāvāpṛthivyau rodasyau dyāvābhūmī ca rodasī |', 'divaspṛthivyau gañjā tu rumā syāllavaṇākaraḥ'], 'num': '', 'gloss': '', 'prose': True},
    {'colophon': 'iti bhūmivargaḥ ||'},
    ],
}
