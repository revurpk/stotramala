# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Amarakośa, Sanskrit Wikisource → IAST, structured and read against the 1882 print;
# written by tools/amarakosha/gen.py. See SOURCES §5.29.

STOTRA = {
    "deity": "amarakosha",
    "doc_title": "Amarakośa · Dhīvarga",
    "app_title": "Amarakośa · Dhīvarga",
    "h1": "Amarakośa",
    "subtitle": "Svargādikāṇḍa · Dhīvarga — mind and understanding; tastes, smells, colours",
    "note": "Amarasiṃha's Nāmaliṅgānuśāsana, the Amarakośa, in Sanskrit: the Sanskrit Wikisource text read against the 1882 Bombay print with Maheśvara's Amaraviveka, numbered as that print numbers it. Verses the print marks as later additions (kṣepaka) are set smaller. Translations will follow.",
    "nav": [("‹ Kālavarga", "amarakosha-1-04-iast.html"), ("all vargas", "amarakosha-iast.html"), ("Śabdādivarga ›", "amarakosha-1-06-iast.html")],
    "footer": "Source: Sanskrit Wikisource — अमरकोशः (public domain), converted to IAST; structure, kṣepakas and readings from the 1882 print (ed. Thatte under Kielhorn, Bombay; archive.org), every change listed in SOURCES §5.29; translations original",
    "sections": [
    {'padas': ['buddhirmanīṣā dhiṣaṇā dhīḥ prajñā śemuṣī matiḥ |', 'prekṣopalabdhiścitsaṃvitpratipajjñapticetanāḥ'], 'num': '|| 1 ||', 'gloss': ''},
    {'padas': ['dhīrdhāraṇāvatī medhā saṃkalpaḥ karma mānasam |', 'cittābhogo manaskāraścarcā saṃkhyā vicāraṇā'], 'num': '|| 2 ||', 'gloss': ''},
    {'rubric': 'kṣepaka — an added verse, in quotation marks in the 1882 print'},
    {'padas': ['avadhānaṃ samādhānaṃ praṇidhānaṃ tathaiva ca'], 'num': '', 'gloss': '', 'prose': True},
    {'rubric': 'kṣepaka — an added verse, in quotation marks in the 1882 print'},
    {'padas': ['vimarśo bhāvanā caiva vāsanā ca nigadyate'], 'num': '', 'gloss': '', 'prose': True},
    {'padas': ['adhyāhārastarka ūho vicikitsā tu saṃśayaḥ |', 'sandehadvāparau cātha samau nirṇayaniścayau'], 'num': '|| 3 ||', 'gloss': ''},
    {'padas': ['mithyādṛṣṭirnāstikatā vyāpādo drohacintanam |', 'samau siddhāntarāddhāntau bhrāntirmithyāmatirbhramaḥ'], 'num': '|| 4 ||', 'gloss': ''},
    {'padas': ['saṃvidāgūḥ pratijñānam niyamāśravasaṃśravāḥ |', 'aṅgīkārābhyupagamapratiśravasamādhayaḥ'], 'num': '|| 5 ||', 'gloss': ''},
    {'padas': ['mokṣe dhīrjñānamanyatra vijñānaṃ śilpaśāstrayoḥ |', 'muktiḥ kaivalyanirvāṇaśreyoniḥśreyasāmṛtam'], 'num': '|| 6 ||', 'gloss': ''},
    {'padas': ["mokṣo'pavargo'thājñānamavidyāhaṃmatiḥ striyām |", 'rūpaṃ śabdo gandharasasparśāśca viṣayā amī'], 'num': '|| 7 ||', 'gloss': ''},
    {'padas': ['gocarā indriyārthāśca hṛṣīkaṃ viṣayīndriyam |', 'karmendriyaṃ tu pāyvādi manonetrādi dhīndriyam'], 'num': '|| 8 ||', 'gloss': ''},
    {'padas': ["tuvarastu kaṣāyo'strī madhuro lavaṇaḥ kaṭuḥ |", "tikto'mlaśca rasāḥ puṃsi tadvatsu ṣaḍamī triṣu"], 'num': '|| 9 ||', 'gloss': ''},
    {'padas': ['vimardotthe parimalo gandhe janamanohare |', "āmodaḥ so'tinirhārī vācyaliṅgatvamāguṇāt"], 'num': '|| 10 ||', 'gloss': ''},
    {'padas': ['samākarṣī tu nirhārī surabhirghrāṇatarpaṇaḥ |', 'iṣṭagandhaḥ sugandhiḥ syādāmodī mukhavāsanaḥ'], 'num': '|| 11 ||', 'gloss': ''},
    {'padas': ['pūtigandhistu durgandho visraṃ syādāmagandhi yat |', 'śuklaśubhraśuciśvetaviśadaśyetapāṇḍarāḥ'], 'num': '|| 12 ||', 'gloss': ''},
    {'padas': ["avadātaḥ sito gauro'valakṣo dhavalo'rjunaḥ |", 'hariṇaḥ pāṇḍuraḥ pāṇḍurīṣatpāṇḍustu dhūsaraḥ'], 'num': '|| 13 ||', 'gloss': ''},
    {'padas': ['kṛṣṇe nīlāsitaśyāmakālaśyāmalamecakāḥ |', 'pīto gauro haridrābhaḥ palāśo harito harit'], 'num': '|| 14 ||', 'gloss': ''},
    {'padas': ['lohito rohito raktaḥ śoṇaḥ kokanadacchaviḥ |', 'avyaktarāgastvaruṇaḥ śvetaraktastu pāṭalaḥ'], 'num': '|| 15 ||', 'gloss': ''},
    {'padas': ['śyāvaḥ syātkapiśo dhūmradhūmalau kṛṣṇalohite |', 'kaḍāraḥ kapilaḥ piṅgapiśaṅgau kadrupiṅgalau'], 'num': '|| 16 ||', 'gloss': ''},
    {'padas': ['citraṃ kirmīrakalmāṣaśabalaitāśca karbure |', 'guṇe śuklādayaḥ puṃsi guṇiliṅgāstu tadvati'], 'num': '|| 17 ||', 'gloss': ''},
    {'colophon': 'iti dhīvargaḥ ||'},
    ],
}
