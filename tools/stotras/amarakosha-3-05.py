# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Amarakośa, Sanskrit Wikisource → IAST, structured and read against the 1882 print;
# written by tools/amarakosha/gen.py. See SOURCES §5.29.

STOTRA = {
    "deity": "amarakosha",
    "doc_title": "Amarakośa · Avyayavarga",
    "app_title": "Amarakośa · Avyayavarga",
    "h1": "Amarakośa",
    "subtitle": "Sāmānyakāṇḍa · Avyayavarga — indeclinables",
    "note": "Amarasiṃha's Nāmaliṅgānuśāsana, the Amarakośa, in Sanskrit: the Sanskrit Wikisource text read against the 1882 Bombay print with Maheśvara's Amaraviveka, numbered as that print numbers it. Verses the print marks as later additions (kṣepaka) are set smaller. Translations will follow.",
    "nav": [("‹ Nānārthavarga", "amarakosha-3-03-iast.html"), ("all vargas", "amarakosha-iast.html"), ("Liṅgādisaṅgrahavarga ›", "amarakosha-3-06-iast.html")],
    "footer": "Source: Sanskrit Wikisource — अमरकोशः (public domain), converted to IAST; structure, kṣepakas and readings from the 1882 print (ed. Thatte under Kielhorn, Bombay; archive.org), every change listed in SOURCES §5.29; translations original",
    "sections": [
    {'padas': ['cirāya cirarātrāya cirasyādyāścirārthakāḥ |', 'muhuḥ punaḥ punaḥ śaśvadabhīkṣṇamasakṛtsamāḥ'], 'num': '|| 1 ||', 'gloss': ''},
    {'padas': ['srāgjhaṭityañjasāhnāya drāṅmaṅkṣu sapadi drute |', 'balavatsuṣṭhu kimuta svatyatīva ca nirbhare'], 'num': '|| 2 ||', 'gloss': ''},
    {'padas': ['pṛthagvināntareṇarte hiruṅnānā ca varjane |', 'yattadyatastato hetāvasākalye tu ciccana'], 'num': '|| 3 ||', 'gloss': ''},
    {'padas': ['kadācijjātu sārdhaṃ tu sākaṃ satrā samaṃ saha |', 'ānukūlyārthakaṃ prādhvaṃ vyarthake tu vṛthā mudhā'], 'num': '|| 4 ||', 'gloss': ''},
    {'padas': ['āho utāho kimuta vikalpe kiṃ kimūta ca |', 'tu hi ca sma ha vai pādapūraṇe pūjane svati'], 'num': '|| 5 ||', 'gloss': ''},
    {'padas': ['divāhnītyatha doṣā ca naktaṃ ca rajanāviti |', "tiryagarthe sāci tiro'pyatha saṃbodhanārthakāḥ"], 'num': '|| 6 ||', 'gloss': ''},
    {'padas': ['syuḥ pyāṭpāḍaṅga he hai bhoḥ samayā nikaṣā hiruk |', "atarkite tu sahasā syātpuraḥ purato'grataḥ"], 'num': '|| 7 ||', 'gloss': ''},
    {'padas': ['svāhā devahavirdāne śrauṣaṭvauṣaṭvaṣaṭsvadhā |', 'kiñcidīṣanmanāgalpe pretyāmutra bhavāntare'], 'num': '|| 8 ||', 'gloss': ''},
    {'padas': ["va vā yathā tathevaivaṃ sāmye'ho hīti vismaye |", 'maune tu tūṣṇīṃ tūṣṇīkāṃ sadyaḥ sapadi tatkṣaṇe'], 'num': '|| 9 ||', 'gloss': ''},
    {'padas': ["diṣṭyā samupajoṣaṃ cetyānande'thāntare'ntarā |", 'antareṇa ca madhye syuḥ prasahya tu haṭhārthakam'], 'num': '|| 10 ||', 'gloss': ''},
    {'padas': ["yukte dve sāṃprataṃ sthāne'bhīkṣṇaṃ śaśvadanārate |", 'abhāve nahya no nāpi mā sma mālaṃ ca vāraṇe'], 'num': '|| 11 ||', 'gloss': ''},
    {'padas': ['pakṣāntare cedyadi ca tattve tvaddhāñjasā dvayam |', 'prākāśye prādurāviḥ syādomevaṃ paramaṃ mate'], 'num': '|| 12 ||', 'gloss': ''},
    {'padas': ['samantatastu paritaḥ sarvato viṣvagityapi |', 'akāmānumatau kāmamasūyopagamestu ca'], 'num': '|| 13 ||', 'gloss': ''},
    {'padas': ['nanu ca syādvirodhoktau kaścitkāmapravedane |', 'niṣṣamaṃ duṣṣamaṃ garhye yathāsvaṃ tu yathāyatham'], 'num': '|| 14 ||', 'gloss': ''},
    {'padas': ['mṛṣā mithyā ca vitathe yathārthaṃ tu yathātatham |', 'syurevaṃ tu punarvai vetyavadhāraṇavācakāḥ'], 'num': '|| 15 ||', 'gloss': ''},
    {'padas': ['prāgatītārthakaṃ nūnamavaśyaṃ niścaye dvayam |', "saṃvadvarṣe'vare tvarvāgāmevaṃ svayamātmanā"], 'num': '|| 16 ||', 'gloss': ''},
    {'padas': ['alpe nīcairmahatyuccaiḥ prāyo bhūmnyadrute śanaiḥ |', "sanā nitye bahirbāhye smātīte'stamadarśane"], 'num': '|| 17 ||', 'gloss': ''},
    {'padas': ["asti satve ruṣoktāvu ūṃ praśne'nunaye tvayi |", 'huṃ tarke syāduṣā rātreravasānenamo natau'], 'num': '|| 18 ||', 'gloss': ''},
    {'padas': ["punararthe'ṅga nindāyāṃ duṣṭhu suṣṭhu praśaṃsane |", 'sāyaṃ sāye prage prātaḥ prabhāte nikaṣāntike'], 'num': '|| 19 ||', 'gloss': ''},
    {'rubric': 'in the e-text only — not in the 1882 print'},
    {'padas': ['amānuguṇye smaraṇe huṃ phaḍvighnanirākṛtau |', 'aṅgīkṛtau syādarthe hūṃ hīnasaṃbodhate tvare'], 'num': '', 'gloss': '', 'prose': True},
    {'padas': ["parutparārthaiṣamo'bde pūrve pūrvatare yati |", "adya'trāhnyatha pūrve'hnītyādau pūrvottarāparāt"], 'num': '|| 20 ||', 'gloss': ''},
    {'padas': ['tathādharānyānyataretarātpūrvedyurādayaḥ |', 'ubhayadyuścobhayedyuḥ paretvahni paredyavi'], 'num': '|| 21 ||', 'gloss': ''},
    {'padas': ["hyo gate'nāgate'hni śvaḥ paraśvastu pare'hani |", 'tadā tadānīṃ yugapadekadā sarvadā sadā'], 'num': '|| 22 ||', 'gloss': ''},
    {'padas': ["etarhi saṃpratī'dānīmadhunā sāmprataṃ tathā |", 'digdeśakāle pūrvādau prāgudakpratyagādayaḥ'], 'num': '|| 23 ||', 'gloss': ''},
    {'colophon': 'iti avyayavargaḥ ||'},
    ],
}
