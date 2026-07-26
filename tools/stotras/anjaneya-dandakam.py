# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE work (src="tel"): a daṇḍaka — continuous flowing lines, no
# verse numbers. Telugu grammar with Sanskrit invocations woven in. Telugu
# from Telugu Wikisource (public domain); translation original. Āñjaneya
# Daṇḍakam — a hymn to Hanumān recounting his deeds in the Rāmāyaṇa.
# See SOURCES §6.4.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "hanuman",
    "doc_title": "Āñjaneya Daṇḍakam",
    "app_title": "Āñjaneya Daṇḍakam",
    "h1": "Āñjaneya Daṇḍakam",
    "subtitle": "A daṇḍaka to Hanumān",
    "note": "A daṇḍaka — a hymn of long, flowing, unmetered lines with no verse "
            "numbers. The Telugu is the source; the IAST is a reading aid. Sanskrit "
            "invocations open and close it; the body, in Telugu, recounts "
            "Hanumān's deeds in the Rāmāyaṇa in one long sweep.",
    "footer": "Source: Telugu Wikisource — ఆంజనేయ దండకం (public domain)",
    "sections": [
        _v(["శ్రీ ఆంజనేయం ప్రసన్నాంజనేయం ప్రభాదివ్యకాయం ప్రకీర్తిప్రదాయం",
            "భజే వాయుపుత్రం భజే వాలగాత్రం భజే హం పవిత్రం భజే సూర్యమిత్రం",
            "భజే రుద్రరూపం భజే బ్రహ్మతేజం బటంచున్ ప్రభాతంబు సాయంత్రము నీ నామ సంకీర్తనల్ జేసి నీ రూపు వర్ణించి నీ మీద నే దండకంబొక్కటింజేయ నూహించి నీ మూర్తినింగాంచి నీ సుందరంబెంచి నీ దాస దాసుండనై రామ భక్తుండనై నిన్ను నే గొల్చెదన్ నీ కటాక్షంబునన్ జూచితే వేడుకల్ జేసితే నా మొరాలించితే నన్ను రక్షించితే అంజనా దేవి గర్భాన్వయా దేవ"],
           "Śrī Āñjaneya, gracious Āñjaneya, of radiant divine body, giver of "
           "renown; I worship the son of the Wind, I worship the mighty-tailed "
           "one, I worship the pure one, I worship the friend of the Sun; I "
           "worship the form of Rudra, I worship the splendour of Brahman — "
           "saying thus, morning and evening making chants of your name, "
           "describing your form, resolving to make this one daṇḍaka upon you, "
           "beholding your image, dwelling on your beauty, becoming the servant "
           "of your servants and a devotee of Rāma, I worship you. If you look "
           "on me with your gracious glance, delight in me, heed my plea, and "
           "protect me — O God born of the womb of Devī Añjanā!"),
        _v(["నిన్నెంచ నేనెంత వాడన్దయాశాలివై చూచితే, దాతవై బ్రోచితే, దగ్గరన్ నిలిచితే, తొల్లి సుగ్రీవునకున్ మంత్రివై స్వామి కార్యంబు నందుండి,",
            "శ్రీరామసౌమిత్రులం జూచి, వారిన్ విచారించి, సర్వేశు పూజించి, యబ్బానుజున్ బంటుగావించి, యవ్వాలినిన్ జంపి, కాకుస్థతిలకున్ దయా దృష్ఠి వీక్షించి,"],
           "How great am I to reckon you? — yet if, full of compassion, you "
           "looked on me, protected me as a giver, stood close by me… Long ago, "
           "becoming Sugrīva's minister and standing firm in the Lord's task: "
           "seeing Śrī Rāma and Saumitri (Lakṣmaṇa), taking counsel with them, "
           "worshipping the Lord of all, making the Sun's son (Sugrīva) his "
           "master, slaying that Vāli, and being looked upon by the tilaka of "
           "the Kākutstha line (Rāma) with a glance of grace;"),
        _v(["కిష్కింధకేతెంచి, శ్రీరామ కార్యార్థివై, లంకకేతెంచియున్, లంకిణింజంపియున్, లంకనున్ గాల్చియున్, భూమిజన్ జూచి, యానందముప్పొంగ,",
            "యాయుంగరంబిచ్చి, యారత్నమున్ దెచ్చి, శ్రీరాముకున్నిచ్చి, సంతోషనున్ జేసి,",
            "సుగ్రీవునుం అంగదున్ జాంబవంతాది నీలాదులున్ గూడి,యాసేతువున్ దాటి, వానరా మూక పెన్మూకలై, దైత్యులన్ ద్రుంచగా,",
            "రావణుడంత కాలాగ్ని ఉగ్రుండుడై, కోరి, బ్రహ్మాండమైనట్టి యాశక్తినిన్ వేసి, యా లక్ష్మణున్ మూర్ఛనొందింపగ"],
           "coming to Kiṣkindhā; becoming the doer of Śrī Rāma's errand, going "
           "to Laṅkā, slaying Laṅkiṇī, burning Laṅkā, beholding the Earth's "
           "daughter (Sītā), your joy welling up; giving her the ring, bringing "
           "back her jewel, giving it to Śrī Rāma and gladdening him; joining "
           "with Sugrīva, Aṅgada, Jāmbavān, Nīla and the rest, crossing that "
           "bridge, the vānara host swelling into a great army as they crushed "
           "the demons — then, when Rāvaṇa, fierce as the fire of doom, willingly "
           "hurled that world-shattering weapon and made Lakṣmaṇa swoon,"),
        _v(["నప్పుడేపోయి సంజీవనిన్ దెచ్చి,సౌమిత్రికిన్నిచ్చి ప్రాణంబు రక్షింపగా,",
            "కుంభకర్ణాది వీరాదితో పోరాడి, చెండాడి, శ్రీరామబాణాగ్ని వారందరిన్ రావణున్ జంపగా",
            "నంత లోకంబులానందమైయుండనవ్వేళనన్,నవ్విభీషణున్ వేడుకన్ దోడుకన్ వచ్చి, పట్టాభిషేకంబు చేయించి,",
            "సీతామహాదేవినిన్ దెచ్చి, శ్రీరాముకున్ ఇచ్చి, అయోద్యకున్ వచ్చి, పట్టాభిషేకంబు సంరంభమైయున్న నీకన్ననాకెవ్వరున్ గూర్మిలేరంచు మన్నించినన్"],
           "then, going at once, you brought the Sañjīvani, gave it to Saumitri, "
           "and saved his life; fighting and striking down Kumbhakarṇa and the "
           "other heroes, when the fire of Śrī Rāma's arrows slew them all and "
           "Rāvaṇa; then, all the worlds rejoicing, in that hour joyfully "
           "bringing Vibhīṣaṇa along and having him crowned; bringing the great "
           "Devī Sītā, giving her to Śrī Rāma, coming to Ayodhyā — and when the "
           "coronation was in full festivity, (Rāma) honoured you, saying "
           "‘none is dearer to me than you.’"),
        _v(["శ్రీరామభక్తి ప్రశస్థంబుగా నిన్ను నీనామసంకీర్తనల్ చేసితే",
            "పాపముల్ బాయునే భయములున్ దీరునే",
            "భాగ్యముల్ గల్గునే సకలసామ్రాజ్యముల్ సకలసంపత్తులున్ గల్గునే యో వానరాకార! యోభక్తమందార! యోపుణ్యసంచార! యోధీర! యోశూర! యో వీర!",
            "నీవే సమస్తంబు నీవే మహాఫలంబుగా వెలసి యాతారకబ్రహ్మ మంత్రంబు సంధానముంజేయుచు స్థిరముగా వజ్రదేహంబునున్ దాల్చి,"],
           "If, with excellent devotion to Śrī Rāma, one makes chants of your "
           "name — do sins not depart? do fears not end? do fortunes not arise, "
           "do all empires and all riches not come? O you of monkey form! O "
           "wish-tree of devotees! O mover in holiness! O steadfast! O valiant! "
           "O hero! You yourself are all — shining as the great fruit itself, "
           "ever joining that Tāraka-Brahma mantra (‘Rāma’), firmly wearing your "
           "adamantine body,"),
        _v(["శ్రీరామ శ్రీరామ యంచున్ మనఃపూతమై యెప్పుడున్ తప్పకన్ తలచు నాజిహ్వయందుండియున్ నీ దీర్ఘదేహంబు త్రైలోక్యసంచారివై,",
            "శ్రీరామ నామాంకితధ్యానివై బ్రహ్మవై, బ్రహ్మ తేజంబంటచున్ రౌద్ర నీ జ్వాల కల్లోల హావీర హనుమంత!",
            "ఓంకారహ్రీంకార శబ్దంబులన్ క్రూర సర్వ గ్రహ భూత ప్రేత పిశాచంబులన్ గాలి దయ్యంబులన్, నీదు వాలంబునన్ జుట్టి నేలంబడంగొట్టి",
            "నీముష్టిఘాతంబులన్ బాహుదండంబులన్ రోమఖండంబులన్ ద్రుంచి, కాలాగ్ని రుద్రుండవై",
            "బ్రహ్మప్రభా భాసితంబైన నీదివ్యతేజంబునన్ జూచి, రారా నాముద్దు నృసింహాయటంచున్,దయాదృష్ఠివీక్షించి, నన్నేలు నాస్వామీ!"],
           "abiding on my tongue, which ever thinks ‘Śrī Rāma, Śrī Rāma’ with a "
           "pure mind and never fails — with your vast body roaming the three "
           "worlds, a meditator marked by Rāma's name, being Brahman, uttering "
           "‘the splendour of Brahman’ — O fierce Hanumān of billowing flame and "
           "valour! With the sounds Oṃkāra and Hrīṃkāra, seizing with your tail "
           "the cruel planets, ghosts, spectres, goblins, and wind-demons and "
           "dashing them to the ground, crushing them with your fist-blows and "
           "staff-like arms, tearing them to shreds, becoming Rudra the fire of "
           "doom — beholding your divine splendour bright with the radiance of "
           "Brahman, (the Lord calling) ‘come, come, my darling Nṛsiṃha!’ and "
           "looking on you with grace: rule over me, O my Lord!"),
        _v(["ఆంజనేయ నమస్తే సదా బ్రహ్మచారీ నమస్తే! వాయుపుత్రా నమస్తే!నమస్తే నమస్తే నమస్తే నమస్తే నమస్తే నమో నమః"],
           "Āñjaneya, salutation to you! Ever-celibate one, salutation! Son of "
           "the Wind, salutation! Salutation, salutation, salutation, "
           "salutation, salutation, salutation upon salutation."),
        _v(["శ్రీరామ జయ రామ జయ రా రమ జయ రామా రామా"],
           "Śrī Rāma, victory to Rāma, victory to Rāma, victory to Rāma — Rāma!"),
    ],
}
