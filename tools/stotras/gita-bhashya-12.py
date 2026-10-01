# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 12 (Bhakti Yoga), with Śaṅkara's bhāṣya. The Sanskrit
# (mūla and bhāṣya, both public domain) is converted from the text layer of
# the Ramakrishna Math, Hyderabad edition (2013), whose legacy Telugu font was
# mapped to Unicode glyph by glyph; its Telugu translation is not used. Collated
# against Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; every
# correction is logged in SOURCES §7.4. The English of the verses and of the
# bhāṣya is original, made from the Sanskrit. Generated from the collated text — edit here, not
# upstream.


def _v(padas, num, gloss, bhashya=None):
    d = {"padas": padas, "num": num, "gloss": gloss}
    if bhashya:
        d["bhashya"] = bhashya
    return d


STOTRA = {
    "deity": "gita",
    "doc_title": "Bhagavad Gītā 12 · Bhakti Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 12",
    "h1": "Bhagavad Gītā · Chapter 12",
    "subtitle": "Bhakti Yoga · the yoga of devotion · with Śaṅkara's bhāṣya",
    "note": "Arjuna asks who is the better yogin — the devotee of the Lord with form, or the worshipper of the unmanifest Imperishable. Kṛṣṇa answers, lays out a graded path for one who cannot at once fix the mind on him, and describes the devotee who is dear to him.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 11', 'gita-bhashya-11-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 13 ›', 'gita-bhashya-13-iast.html')],
    "sections": [
        {"speaker": "arjuna uvāca"},
        _v([
            "evaṃ satatayuktā ye bhaktāstvāṃ paryupāsate |",
            "ye cāpyakṣaramavyaktaṃ teṣāṃ ke yogavittamāḥ",
        ], "|| 1 ||",
           "Arjuna said: Those devotees who, ever disciplined, worship you in this way, and those who worship the imperishable unmanifest — which of them best knows yoga?",
           bhashya=[
               {"text": "dvitīya prabhṛtiṣu adhyāyeṣu vibhūtyanteṣu paramātmanaḥ brahmaṇaḥ akṣarasya vidhvastasarva upādhiviśeṣasya upāsanam uktam. sarvayogaiśvarya sarvajñānaśaktimatsattvopādheḥ īśvarasya tava ca upāsanaṃ tatra tatra uktam. viśvarūpādhyāye tu aiśvaram ādyaṃ samastajagadātmarūpaṃ viśvarūpaṃ tvadīyaṃ darśitam upāsanārthameva tvayā. tacca darśayitvā uktavānasi “matkarmakṛt” ityādi. ataḥ aham anayoḥ ubhayoḥ pakṣayoḥ viśiṣṭatarabubhutsayā tvāṃ pṛcchāmi iti –", "intro": True, "tr": "In the chapters from the second up to the one on the glories, meditation was taught on the supreme Self, Brahman, the imperishable, from which every particular adjunct has been removed. And here and there meditation was taught on you, the Lord, whose adjunct is pure sattva, possessed of all the lordship of yoga, all knowledge and all power. In the chapter on the universal form you showed your primal, sovereign, universal form, the Self of the whole world, for the sake of meditation; and having shown it you said 'he who does my work' and so on. So, wishing to know which of these two positions is superior, I ask you —"},
               {"text": "evamiti atītānantara ślokena uktam arthaṃ parāmṛśati “matkarmakṛt” (11.55) ityādinā. evaṃ satatayuktāḥ nairantaryeṇa bhagavatkarmādau yathokte'rthe samāhitāḥ santaḥ pravṛttā ityarthaḥ. ye bhaktāḥ ananyaśaraṇāḥ santaḥ tvāṃ yathādarśitaṃ viśvarūpaṃ paryupāsate dhyāyanti, te, ye cānye'pi tyaktasarvaiṣaṇāḥ sannyastasarvakarmāṇaḥ yathāviśeṣitaṃ brahma akṣaraṃ nirastasarvopādhitvāt avyaktam akaraṇagocaraṃ, yat hi loke karaṇagocaraṃ tat vyaktam ucyate. ajñeḥ dhātoḥ tatkarmakatvāt, idaṃ tu akṣaraṃ tadviparītaṃ, śiṣṭaiśca ucyamānaiḥ viśeṣaṇaiḥ viśiṣṭaṃ tat ye cāpi paryupāsate teṣām ubhayeṣāṃ madhye ke yogavittamāḥ, ke atiśayena yogavidaḥ ityarthaḥ.", "tr": "'Thus' refers to the meaning stated in the verse just before, 'he who does my work' (11.55). Thus ever disciplined — set about continuously, collected in what has been described, such as the Lord's work. The devotees who, with no other refuge, worship, meditate on, you in the universal form as shown; and those others too who, having given up all cravings and renounced all actions, worship the imperishable Brahman, as described — unmanifest because all adjuncts are removed, beyond the range of the senses; for what is within the range of the senses is called manifest in the world, since the root añj has that as its object; but this imperishable is the opposite of that, and qualified by the attributes still to be stated — those who worship that: of these two, which are the better knowers of yoga — which know yoga most, that is?"},
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "mayyāveśya mano ye māṃ nityayuktā upāsate |",
            "śraddhayā parayopetāste me yuktatamā matāḥ",
        ], "|| 2 ||",
           "The Blessed Lord said: Those who fix their minds on me and worship me, ever disciplined, endowed with supreme faith — them I hold to be the most disciplined.",
           bhashya=[
               {"text": "ye tvakṣaropāsakāḥ samyagdarśinaḥ nivṛttaiṣaṇāḥ te tāvattiṣṭhantu. tān prati yadvaktavyaṃ tadupariṣṭāt vakṣyāmaḥ (12.20). ye tu itare –", "intro": True, "tr": "Let those who meditate on the imperishable, who have right vision and have ceased from cravings, wait for now; what is to be said of them we shall say further on (12.20). But the others —"},
               {"text": "mayi viśvarūpe parameśvare, āveśya samādhāya, manaḥ ye bhaktāḥ santaḥ māṃ sarvayogeśvarāṇām adhīśvaraṃ sarvajñaṃ, vimuktarāgādikleśatimiradṛṣṭiṃ nityayuktāḥ atītānantarādhyāyānte uktaślokārthanyāyena satatayuktāḥ santaḥ upāsate, śraddhayā parayā prakṛṣṭayā upetāḥ ye, te me mama yuktatamāḥ matāḥ abhipretāḥ yuktatamāḥ iti. nairantaryeṇa hi te maccittatayā ahorātram ativāhayanti, ataḥ yuktaṃ tān prati yuktatamāḥ iti vaktum.", "tr": "Those who, being devotees, fixing, collecting, the mind on me, the supreme Lord in the universal form, worship me — the Lord over all the lords of yoga, all-knowing, whose vision is free of the darkness of the afflictions such as passion — ever disciplined, continually disciplined in the manner of the verse at the end of the preceding chapter, endowed with supreme, highest, faith — they are held by me, considered, the most disciplined. For they pass day and night continuously with their minds on me; so it is right to call them most disciplined."},
           ]),
        _v([
            "ye tvakṣaramanirdeśyamavyaktaṃ paryupāsate |",
            "sarvatragamacintyaṃ ca kūṭasthamacalaṃ dhruvam",
        ], "|| 3 ||",
           "But those who worship the Imperishable, the indefinable, the unmanifest, the all-pervading and unthinkable, the unchanging, the immovable, the constant,",
           bhashya=[
               {"text": "kiṃ itare yuktatamāḥ na bhavanti? na, kintu tān prati yat vaktavyaṃ tat śṛṇu –", "intro": True, "tr": "Are the others not most disciplined? No; but hear what is to be said of them:"},
           ]),
        _v([
            "sanniyamyendriyagrāmaṃ sarvatra samabuddhayaḥ |",
            "te prāpnuvanti māmeva sarvabhūtahite ratāḥ",
        ], "|| 4 ||",
           "restraining all the senses, even-minded everywhere, delighting in the welfare of all beings — they too reach me alone.",
           bhashya=[
               {"text": "ye tu akṣaram, anirdeśyam avyaktatvāt aśabdagocaram iti na nirdeṣṭuṃ śakyate, ataḥ anirdeśyam, avyaktaṃ na kenāpi pramāṇena vyajyate iti avyaktam, paryupāsate pari samantāt upāsate, upāsanaṃ nāma yathāśāstram upāsyasya arthasya viṣayīkaraṇena, sāmīpyam upagamya tailadhārāvat samānapratyayapravāheṇa dīrghakālaṃ yat āsanaṃ tat upāsanam ācakṣate. akṣarasya viśeṣaṇam āha upāsyasya sarvatragaṃ vyomavat vyāpi, acintyaṃ ca avyaktatvāt acintyam. yat hi karaṇagocaraṃ tat manasā'pi cintyaṃ, tadviparītatvāt acintyam akṣaram kūṭastham – dṛśyamānaguṇakam antardoṣaṃ vastukūṭaṃ, kūṭarūpakaṃ kūṭasākṣyam ityādau kūṭaśabdaḥ prasiddho loke. tathā ca avidyādyanekasaṃsārabījam antardoṣavat māyā'vyākṛtādi aneka śabdavācyatayā – “māyāṃ tu prakṛtiṃ vidyāt māyinaṃ tu maheśvaram” (śve. u.4.10) “mama māyā duratyayā” (7.14) ityādau prasiddhaṃ yat tat kūṭam, tasmin kūṭe sthitaṃ kūṭasthaṃ tadadhyakṣatayā. athavā – rāśiḥ iva sthitaṃ kūṭastham, ataḥ eva acalaṃ, yasmāt acalaṃ tasmāt dhruvaṃ nityamityarthaḥ.", "tr": "But those who worship the imperishable, the indefinable — being unmanifest it is beyond the reach of words and cannot be pointed out, so it is indefinable; the unmanifest, made manifest by no means of knowledge — worship it all round. Worship means approaching the object of worship, making it one's object in accordance with scripture, and dwelling on it for a long time with a continuous flow of the same idea, like a stream of oil; that is called worship. He gives the attributes of the imperishable to be worshipped: all-pervading, pervasive like space; and unthinkable, because unmanifest — for what is within the range of the senses can be thought of by the mind too, and the imperishable, being the opposite, is unthinkable. Kūṭastha: kūṭa is well known in the world, as in 'a false coin', 'a false witness', for a thing that shows good qualities outwardly but is faulty within. So kūṭa is that which is well known as māyā — the seed of saṃsāra with its many forms such as ignorance, inwardly flawed, called by many words such as māyā and the undifferentiated — as in 'know māyā to be nature and the great Lord the wielder of māyā' (Śvetāśvatara 4.10) and 'my māyā is hard to cross' (7.14). Standing in that kūṭa as its overseer is kūṭastha. Or else, kūṭastha means standing like a heap; therefore unmoving; and since it is unmoving it is constant, eternal, that is."},
               {"text": "sanniyamyeti : sanniyamya samyak niyamya upasaṃhṛtya, indriyagrāmam indriyasamudāyaṃ, sarvatra sarvasmin kāle samabuddhayaḥ – samā tulyā buddhiḥ yeṣāṃ iṣṭāniṣṭa prāptau te samabuddhayaḥ. te ye evaṃvidhāḥ te prāpnuvanti mām eva sarvabhūtahite ratāḥ. na tu teṣāṃ vaktavyaṃ kiñcit “māṃ te prāpnuvantīti”, “jñānītvātmaiva me matam” (7.18) iti hi uktam. na hi bhagavatsvarūpāṇāṃ satāṃ yuktatamatvam ayuktatamatvaṃ vā vācyam. kintu –", "tr": "'Restraining all the senses…' Restraining, controlling well, withdrawing, the host of the senses; same-minded everywhere, at all times — whose understanding is the same, equal, on gaining what is welcome or unwelcome; those who are such, delighting in the welfare of all beings, attain me alone. Nothing needs to be said of them — that they attain me — for it has been said, 'but the man of knowledge is my very Self' (7.18). Of those who are the Lord's very nature, neither 'most disciplined' nor 'not most disciplined' is to be said. But —"},
           ]),
        _v([
            "kleśo'dhikatarasteṣāmavyaktāsaktacetasām |",
            "avyaktā hi gatirduḥkhaṃ dehavadbhiravāpyate",
        ], "|| 5 ||",
           "The difficulty is greater for those whose minds are set on the unmanifest; for the goal that is unmanifest is hard for embodied beings to reach.",
           bhashya=[
               {"text": "kleśaḥ adhikataraḥ – yadyapi matkarmādiparāṇāṃ kleśaḥ adhikaḥ eva, kleśaḥ adhikataraḥ tu akṣarātmanāṃ paramātmadarśināṃ dehābhimānaparityāganimittaḥ, avyaktāsaktacetasām – avyakte āsaktaṃ cetaḥ yeṣāṃ te avyaktāsaktacetasaḥ teṣām avyaktāsaktacetasām. avyaktā hi yasmāt, yā gatiḥ akṣarātmikā, duḥkhaṃ sā dehavadbhiḥ dehābhimānavadbhiḥ avāpyate, ataḥ kleśaḥ adhikataraḥ, akṣaropāsakānāṃ yadvartanaṃ tat upariṣṭāt (12.13'20) vakṣyāmaḥ.", "tr": "Greater is the toil — though the toil of those devoted to my work and the like is great, greater still is the toil, arising from giving up identification with the body, for those whose self is the imperishable, who see the supreme Self — for those whose minds are attached to the unmanifest. For the goal that is unmanifest, consisting in the imperishable, is reached with difficulty by the embodied, by those who identify with the body; therefore the toil is greater. How those who meditate on the imperishable live we shall tell further on (12.13–20)."},
           ]),
        _v([
            "ye tu sarvāṇi karmāṇi mayi sannyasya matparāḥ |",
            "ananyenaiva yogena māṃ dhyāyanta upāsate",
        ], "|| 6 ||",
           "But those who offer all their actions to me, intent on me, worshipping me with undivided yoga and meditating on me —"),
        _v([
            "teṣāmahaṃ samuddhartā mṛtyusaṃsārasāgarāt |",
            "bhavāmi na cirāt pārtha mayyāveśitacetasām",
        ], "|| 7 ||",
           "for them, whose minds have entered into me, I soon become the one who lifts them out of the ocean of death and rebirth, Pārtha.",
           bhashya=[
               {"text": "ye tviti – ye tu sarvāṇi karmāṇi mayi īśvare sannyasya, matparāḥ ahaṃ paraḥ yeṣāṃ te matparāḥ santaḥ, ananyena eva – avidyamānam anyat ālambanaṃ viśvarūpaṃ devam ātmānaṃ muktvā yasya saḥ ananyaḥ, tena ananyenaiva, kena? yogena samādhinā, māṃ dhyāyantaḥ cintayantaḥ upāsate. teṣāṃ kiṃ –", "tr": "'But those who…' But those who, renouncing all actions in me, the Lord, intent on me — for whom I am the highest — worship me, meditating, thinking, with undivided — having no other support but the god, the universal form, the Self — with that undivided yoga, samādhi. What of them?"},
               {"text": "teṣāṃ madupāsanaikaparāṇām. aham īśvaraḥ, samuddhartā – kutaḥ ityāha – mṛtyusaṃsārasāgarāt, mṛtyuyuktaḥ saṃsāraḥ mṛtyusaṃsāraḥ, sa eva sāgaraḥ iva sāgaraḥ, dustaratvāt. tasmāt mṛtyusaṃsārasāgarāt, ahaṃ teṣāṃ samuddhartā bhavāmi, na cirāt, kiṃ tarhi? kṣipram eva, he pārtha, mayi āveśitacetasām – mayi viśvarūpe āveśitaṃ praveśitaṃ samāhitaṃ cetaḥ yeṣāṃ te mayyāveśitacetasaḥ, teṣām. yataḥ evaṃ, tasmāt –", "tr": "For them, solely devoted to worshipping me, I, the Lord, become the deliverer — from what? He says: from the ocean of mortal saṃsāra — saṃsāra joined with death is mortal saṃsāra, and it is like an ocean, being hard to cross; from that ocean of mortal saṃsāra I become their deliverer, before long — rather, very soon, Pārtha — of those whose minds are fixed on me, whose mind is fixed, entered, collected, in me, the universal form. Since this is so, therefore —"},
           ]),
        _v([
            "mayyeva mana ādhatsva mayi buddhiṃ niveśaya |",
            "nivasiṣyasi mayyeva ata ūrdhvaṃ na saṃśayaḥ",
        ], "|| 8 ||",
           "Fix your mind on me alone; let your understanding enter into me. Then you will dwell in me alone hereafter; of this there is no doubt.",
           bhashya=[
               {"text": "mayyeva viśvarūpe īśvare, manaḥsaṅkalpavikalpātmakam, ādhatsva sthāpaya. mayyeva adhyavasāyaṃ kurvatīṃ buddhim, ādhatsva niveśaya. tataḥ te kiṃ syāditi śṛṇu – nivasiṣyasi nivatsyasi, niścayena madātmanā mayi nivāsaṃ kariṣyasyeva, ataḥ śarīrapātāt ūrdhvaṃ. na saṃśayaḥ, saṃśayaḥ atra na kartavyaḥ.", "tr": "Fix, place, your mind, whose nature is resolving and doubting, on me alone, the Lord in the universal form; set, settle, your understanding, which determines, on me alone. Hear what will come to you then: you will dwell, will certainly make your dwelling, in me, as my very self, hereafter, after the fall of the body. There is no doubt; no doubt is to be entertained here."},
           ]),
        _v([
            "atha cittaṃ samādhātuṃ na śaknoṣi mayi sthiram |",
            "abhyāsayogena tato māmicchāptuṃ dhanañjaya",
        ], "|| 9 ||",
           "But if you cannot keep your mind steadily fixed on me, then seek to reach me by the yoga of practice, Dhanañjaya.",
           bhashya=[
               {"text": "atheti – atha evaṃ yathā avocaṃ tathā mayi cittaṃ samādhātuṃ sthāpayituṃ, sthiram acalaṃ, na śaknoṣi cet, tataḥ paścāt, abhyāsayogena cittasya ekasmin ālambane sarvataḥ samāhṛtya punaḥ punaḥ sthāpanam abhyāsaḥ, tatpūrvakaḥ yogaḥ samādhānalakṣaṇaḥ, tena abhyāsayogena, māṃ viśvarūpam, iccha prārthayasva, āptuṃ prāptuṃ, he dhanañjaya.", "tr": "'If you cannot…' If you cannot fix, settle, your mind firmly, immovably, on me, as I have said, then by the yoga of practice — practice is bringing the mind back from everything and settling it again and again on one support; the yoga, consisting in collectedness, that is based on it is the yoga of practice — by that, seek, long, to attain, to reach, me, the universal form, O Dhanañjaya."},
           ]),
        _v([
            "abhyāse'pyasamartho'si matkarmaparamo bhava |",
            "madarthamapi karmāṇi kurvan siddhimavāpsyasi",
        ], "|| 10 ||",
           "If you are unable even to practise, be intent on work for me; by doing actions for my sake you will attain perfection.",
           bhashya=[
               {"text": "abhyāse'pīti – abhyāse'pi, asamarthaḥ aśaktaḥ, asi tarhi, matkarmaparamaḥ bhava. madarthaṃ karma, matkarma tatparamaḥ matkarmapradhānaḥ ityarthaḥ. abhyāsena vinā madartham api karmāṇi kevalaṃ kurvan, siddhiṃ sattvaśuddhiyogajñānaprāptidvāreṇa avāpsyasi.", "tr": "'If you are unable even to practise…' If you are unable, incapable, even of practice, then be intent on my work: work for my sake is my work, and one intent on it gives it first place, that is. Even doing actions for my sake alone, without practice, you will attain perfection, through purification of mind, yoga and the attainment of knowledge."},
           ]),
        _v([
            "athaitadapyaśakto'si kartuṃ madyogamāśritaḥ |",
            "sarvakarmaphalatyāgaṃ tataḥ kuru yatātmavān",
        ], "|| 11 ||",
           "If you cannot do even this, then, taking refuge in my yoga and controlling yourself, give up the fruit of all actions.",
           bhashya=[
               {"text": "athaitaditi – atha punaḥ etadapi yat uktaṃ matkarmaparatvaṃ tat kartum aśaktaḥ asi, madyogam āśritaḥ – mayi kriyamāṇāni sannyasya yatkaraṇaṃ teṣām anuṣṭhānaṃ saḥ madyogaḥ, tam āśritaḥ san sarvakarmaphalatyāgaṃ – sarveṣāṃ karmaṇāṃ phalasannyāsaṃ sarvakarma phalatyāgaṃ, tataḥ anantaraṃ, kuru, yatātmavān saṃyatacittaḥ san ityarthaḥ.", "tr": "'If you are unable even to do this…' But if you are unable to do even this that was said, being intent on my work, then taking refuge in my yoga — my yoga is performing actions while renouncing them to me as they are done; taking refuge in that — then, after that, practise the giving up of the fruit of all actions, the renouncing of the fruit of all actions, self-controlled, with restrained mind, that is."},
           ]),
        _v([
            "śreyo hi jñānamabhyāsāt jñānāddhyānaṃ viśiṣyate |",
            "dhyānātkarmaphalatyāgastyāgācchāntiranantaram",
        ], "|| 12 ||",
           "For knowledge is better than practice; meditation is superior to knowledge; the giving up of the fruit of action is better than meditation; and from giving up follows peace at once.",
           bhashya=[
               {"text": "idānīṃ sarvakarmaphalatyāgaṃ stauti –", "intro": True, "tr": "Now he praises the giving up of the fruit of all actions:"},
               {"text": "śreyaḥ hi praśasyataraṃ jñānaṃ, kasmāt? (a)vivekapūrvakāt abhyāsāt, tasmādapi jñānāt jñānapūrvakaṃ dhyānaṃ viśiṣyate. jñānavataḥ dhyānādapi karmaphalatyāgaḥ “viśiṣyate” ityanuṣajyate. evaṃ karmaphalatyāgāt pūrvoktaviśeṣaṇavataḥ śāntiḥ upaśamaḥ sahetukasya saṃsārasya anantarameva syāt, na tu kālāntaram apekṣate.", "tr": "For knowledge is better, more praiseworthy. Than what? Than practice without discrimination. Than that knowledge, meditation based on knowledge is superior. Than the meditation even of one who has knowledge, giving up the fruit of action is 'superior' — the word carries over. Thus from the giving up of the fruit of action by one with the qualities described above, peace — the cessation of saṃsāra together with its cause — follows immediately; it does not wait for another time."},
               {"text": "ajñasya karmaṇi pravṛttasya pūrvopadiṣṭopāyānuṣṭhānāśaktau sarvakarmaṇāṃ phalatyāgaḥ śreyaḥ sādhanam upadiṣṭaṃ, na prathamameva, ataḥ ca “śreyo hi jñānamabhyāsāt” iti uttarottara viśiṣṭatvopadeśena sarvakarmaphalatyāgaḥ stūyate, sampannasādhanānuṣṭhānāśaktau anuṣṭheyatvena śrutatvāt. kena dharmeṇa stutitvam? “yadā sarve pramucyante” (kaṭha. u.6.14) iti sarvakāmaprahāṇāt amṛtatvam uktaṃ tat prasiddham. kāmāśca sarve śrautasmārtakarmaṇāṃ phalāni. tattyāge ca viduṣaḥ jñānaniṣṭhasya ananta raiva śāntiḥ. iti sarvakāmatyāgasāmānyam ajñakarmaphalatyāgasya api asti iti tatsāmānyāt sarvakarmaphalatyāgastutiḥ iyaṃ prarocanārthā. yathā agastyena brāhmaṇena samudraḥ pītaḥ iti idānīntanāḥ api brāhmaṇāḥ brāhmaṇatvasāmānyāt stūyante. evaṃ karmaphalatyāgāt karmayogasya śreyaḥ sādhanatvam abhihitam.", "tr": "For the ignorant man engaged in action, unable to practise the means taught earlier, the giving up of the fruit of all actions has been taught as a means to the highest good, not at the very first. And so, by teaching each later step as superior to the one before in 'for knowledge is better than practice', the giving up of the fruit of all actions is praised, since it is enjoined as what is to be practised when one is unable to practise the means already given. By what feature is it praised? It is well known that immortality has been declared to come from the abandonment of all desires: 'when all desires are released' (Kaṭha 6.14). And all desires are the fruits of Vedic and smārta actions; and when they are given up, the knower steadfast in knowledge has peace immediately. Since the giving up of the fruit of action by the ignorant shares the common feature of giving up all desire, this praise of giving up the fruit of all actions on the strength of that common feature is meant to stir interest — just as brāhmaṇas of today are praised, by virtue of being brāhmaṇas, with 'the ocean was drunk by the brāhmaṇa Agastya'. Thus the yoga of action has been declared a means to the highest good through the giving up of the fruit of action."},
           ]),
        _v([
            "adveṣṭā sarvabhūtānāṃ maitraḥ karuṇa eva ca |",
            "nirmamo nirahaṅkāraḥ samaduḥkhasukhaḥ kṣamī",
        ], "|| 13 ||",
           "He who bears no ill will to any being, who is friendly and compassionate, free from 'mine' and from 'I', even in pleasure and pain, forbearing,",
           bhashya=[
               {"text": "atra ca ātmeśvarabhedam āśritya viśvarūpe īśvare cetaḥ samādhānalakṣaṇaḥ yogaḥ uktaḥ, īśvarārthaṃ karmānuṣṭhānādi ca. “athaitadapyaśakto'si” (12.11) iti ajñānakāryasūcanāt na abhedadarśinaḥ akṣaropāsakasya karmayogaḥ upapadyate iti darśayati. tathā karmayoginaḥ akṣaropāsanānupattiṃ darśayati bhagavān “te prāpnuvanti māmeva” (12.4) iti akṣaropāsakānāṃ kaivalya prāptau svātantryam uktvā itareṣāṃ pāratantryāt īśvarādhīnatāṃ darśitavān “teṣāmahaṃ samuddhartā” (12.7)iti. yadi hi īśvarasya ātmabhūtāḥ te matāḥ abhedadarśitvāt akṣarasvarūpā eva te iti samuddharaṇakarmaviṣayavacanaṃ tān prati apeśalaṃ syāt. yasmācca arjunasya atyantameva hitaiṣī bhagavān tasya samyagdarśanānvitaṃ karmayogaṃ bhedadṛṣṭimantam eva upadiśati. na ca ātmānam īśvaraṃ pramāṇataḥ buddhvā kasyacit guṇabhāvaṃ jigamiṣati kaścit, virodhāt. tasmāt akṣaropāsakānāṃ samyagdarśananiṣṭhānāṃ sannyāsināṃ tyaktasarvaiṣaṇānāṃ “adveṣṭā sarvabhūtānām” ityādi dharmapūgaṃ sākṣāt amṛtatvakāraṇaṃ vakṣyāmīti pravartate.", "intro": True, "tr": "Here, relying on the distinction between the self and the Lord, the yoga consisting in collecting the mind on the Lord in the universal form has been taught, as well as the performance of action for the Lord's sake and the rest. With 'if you are unable even to do this' (12.11), which points to an effect of ignorance, he shows that the yoga of action is not fitting for one who meditates on the imperishable and sees non-difference. Likewise the Lord shows that meditation on the imperishable is not fitting for the man of the yoga of action: having stated with 'they attain me alone' (12.4) the independence of those who meditate on the imperishable in attaining aloneness, he showed the dependence of the others on the Lord with 'for them I become the deliverer' (12.7). For if they were held to be the Lord's very Self, being the imperishable itself because they see non-difference, speech about delivering them as objects of an action would be unsuitable. And since the Lord is exceedingly well-disposed to Arjuna, he teaches him the yoga of action accompanied by right vision, involving the vision of difference. Nor does anyone, having understood through valid knowledge the Self as the Lord, wish to become subordinate to anyone, for that is contradictory. Therefore he begins to tell, with 'without hatred towards all beings', the set of qualities that is the direct cause of immortality for renouncers who meditate on the imperishable, are steadfast in right vision, and have given up all cravings."},
               {"text": "adveṣṭā sarvabhūtānām, sarveṣām bhūtānām na dveṣṭā adveṣṭā ātmanaḥ duḥkhahetumapi na kiñcit dveṣṭi, sarvāṇi bhūtāni ātmatvena hi paśyati. maitraḥ – mitrabhāvaḥ maitrī. mitratayā vartate iti maitraḥ. karuṇaḥ eva ca karuṇā kṛpā duḥkhiteṣu dayā. tadvān karuṇaḥ, sarvabhūtānām: abhayapradaḥ sannyāsī ityarthaḥ. nirmamaḥ – mamapratyayavarjitaḥ. nirahaṅkāraḥ nirgatāhampratyayaḥ. samaduḥkhasukhaḥ. same duḥkhasukhe dveṣarāgayoḥ apravartake yasya saḥ samaduḥkhasukhaḥ kṣamī kṣamāvān ākruṣṭaḥ abhihitaḥ vā avikriyaḥ eva āste.", "tr": "Without hatred towards all beings: he hates no being, not even one that causes him pain, for he sees all beings as his Self. Friendly: friendliness is the state of a friend, and one who behaves as a friend is friendly. And compassionate: compassion is mercy, kindness to the suffering; one who has it is compassionate — towards all beings: a renouncer who grants fearlessness, that is. Without 'mine': free of the notion of 'mine'. Without egoism: free of the notion of 'I'. The same in pain and pleasure: one to whom pain and pleasure are the same, not prompting aversion or attachment. Patient: possessed of patience, he remains unchanged when abused or struck."},
           ]),
        _v([
            "santuṣṭaḥ satataṃ yogī yatātmā dṛḍhaniścayaḥ |",
            "mayyarpitamanobuddhiryo madbhaktaḥ sa me priyaḥ",
        ], "|| 14 ||",
           "ever content, a yogin, self-controlled, firm in resolve, with mind and understanding offered to me — he who is thus my devotee is dear to me.",
           bhashya=[
               {"text": "santuṣṭa iti : santuṣṭaḥ, satataṃ nityaṃ dehasthitikāraṇasya lābhe alābhe ca utpannālampratyayaḥ. tathā guṇavallābhe viparyaye ca santuṣṭhaḥ. satataṃ, yogī samāhita cittaḥ, yatātmā saṃyatasvabhāvaḥ, dṛḍhaniścayaḥ – dṛḍhaḥ sthiraḥ niścayaḥ adhyavasāyaḥ yasya ātmatattvaviṣaye saḥ dṛḍhaniścayaḥ, mayi arpitamanobuddhiḥ saṅkalpavikalpātmakaṃ manaḥ adhyavasāyalakṣaṇā buddhiḥ, te mayyeva arpite sthāpite yasya sannyāsinaḥ saḥ mayi arpitamanobuddhiḥ. yaḥ īdṛśaḥ madbhaktaḥ saḥ me priyaḥ. “priyo hi jñānino'tyarthamahaṃ sa ca mama priyaḥ” (7.17) iti saptame adhyāye sūcitaṃ, tat iha prapañcyate.", "tr": "'Content…' Content always, at all times, with the sense of 'enough' whether or not he gains what keeps the body going; likewise content whether he gains what is good or its opposite. Always a yogin, collected in mind; self-controlled, of restrained nature; of firm resolve, whose resolve, whose determination regarding the reality of the Self, is firm, steady; with mind and understanding offered to me — the renouncer whose mind, whose nature is resolving and doubting, and whose understanding, whose mark is determining, are offered, placed, in me alone. Such a devotee of mine is dear to me. What was hinted at in the seventh chapter, 'for I am exceedingly dear to the man of knowledge, and he is dear to me' (7.17), is elaborated here."},
           ]),
        _v([
            "yasmānnodvijate loko lokānnodvijate ca yaḥ |",
            "harṣāmarṣabhayodvegairmukto yaḥ sa ca me priyaḥ",
        ], "|| 15 ||",
           "He by whom the world is not troubled, and who is not troubled by the world, who is free from elation, impatience, fear and agitation, is dear to me.",
           bhashya=[
               {"text": "yasmāditi – yasmāt sannyāsinaḥ. na udvijate na udvegaṃ gacchati na santapyate na saṅkṣubhyati lokaḥ, tathā lokāt na udvijate ca yaḥ, harṣāmarṣabhayodvegaiḥ – harṣaśca amarṣaśca bhayaṃ ca udvegaśca taiḥ harṣāmarṣabhayodvegaiḥ muktaḥ. harṣaḥ priyalābhe antaḥkaraṇasya utkarṣaḥ romāñcanāśrupātādiliṅgaḥ amarṣaḥ asahiṣṇutā, bhayaṃ trāsaḥ, udvegaḥ udvignatā, taiḥ muktaḥ yaḥ saḥ ca me priyaḥ.", "tr": "'From whom the world does not shrink…' From whom, from which renouncer, the world does not shrink, is not agitated, pained or disturbed; and who does not shrink from the world; who is free from elation, impatience, fear and agitation — elation is the swelling of the inner organ on gaining what is dear, marked by hair standing on end, tears and the like; impatience is intolerance; fear is dread; agitation is anxiety — he who is free from these is dear to me."},
           ]),
        _v([
            "anapekṣaḥ śucirdakṣa udāsīno gatavyathaḥ |",
            "sarvārambhaparityāgī yo madbhaktaḥ sa me priyaḥ",
        ], "|| 16 ||",
           "He who is free from wants, pure, capable, indifferent, untroubled, who has renounced all undertakings — he who is thus my devotee is dear to me.",
           bhashya=[
               {"text": "anapekṣaḥ iti – dehendriyaviṣayasambandhādiṣu apekṣā viṣayeṣu apekṣā yasya nāsti saḥ anapekṣaḥ niḥspṛhaḥ, śuciḥ bāhyena ābhyantareṇa ca śaucena sampannaḥ, dakṣaḥ pratyutpanneṣu kāryeṣu sadyaḥ yathāvat pratipattuṃ samarthaḥ, udāsīnaḥ na kasyacit mitrādeḥ pakṣaṃ bhajate yaḥ sa udāsīnaḥ, yatiḥ. gatavyathaḥ gatabhayaḥ, sarvārambhaparityāgī ārabhyante iti ārambhāḥ, ihāmutrārthaphalabhogārthāni kāmahetūni karmāṇi sarvārambhāḥ, tān parityaktuṃ śīlam asyeti sarvārambhaparityāgī yaḥ madbhaktaḥ saḥ me priyaḥ. kiñca –", "tr": "'Without expectation…' He who has no expectation, no reliance, on objects — on the body, the senses, their objects and their connections — free of longing; pure, endowed with outer and inner purity; capable, able to grasp at once and rightly what must be done as it arises; indifferent, who takes no one's side, friend or other — an ascetic; free of distress, without fear; renouncing all undertakings — undertakings are what are begun: actions done for enjoying fruits here and hereafter, the causes of desire; one whose nature is to renounce them all — such a devotee of mine is dear to me. Moreover —"},
           ]),
        _v([
            "yo na hṛṣyati na dveṣṭi na śocati na kāṅkṣati |",
            "śubhāśubhaparityāgī bhaktimān yaḥ sa me priyaḥ",
        ], "|| 17 ||",
           "He who neither rejoices nor hates, neither grieves nor desires, who has renounced good and evil, and is full of devotion, is dear to me.",
           bhashya=[
               {"text": "yaḥ na hṛṣyati iṣṭaprāptau, na dveṣṭi aniṣṭaprāptau, na śocati priyaviyoge, na ca aprāptaṃ kāṅkṣati, śubhāśubhe karmaṇī parityaktuṃ śīlam asyeti śubhāśubhaparityāgī, bhaktimān yaḥ, sa me priyaḥ.", "tr": "He who does not rejoice on gaining what he wants, does not hate on meeting what he does not want, does not grieve at separation from what is dear, and does not long for what he has not got; who renounces good and evil — whose nature is to renounce good and evil actions — full of devotion: he is dear to me."},
           ]),
        _v([
            "samaḥ śatrau ca mitre ca tathā mānāpamānayoḥ |",
            "śītoṣṇasukhaduḥkheṣu samaḥ saṅgavivarjitaḥ",
        ], "|| 18 ||",
           "He who is the same to foe and friend, in honour and dishonour, in cold and heat, in pleasure and pain, and free from attachment;",
           bhashya=[
               {"text": "samaḥ iti – samaḥ śatrau ca mitre ca tathā, mānāpamānayoḥ pūjāparibhavayoḥ, śītoṣṇasukhaduḥkheṣu samaḥ sarvatra ca saṅgavarjitaḥ. kiñca", "tr": "'The same to foe and friend…' The same to foe and friend, likewise in honour and dishonour, in worship and contempt; the same in cold and heat, pleasure and pain; and free from attachment everywhere. Moreover —"},
           ]),
        _v([
            "tulyanindāstutirmaunī santuṣṭo yena kena cit |",
            "aniketaḥ sthiramatirbhaktimān me priyo naraḥ",
        ], "|| 19 ||",
           "to whom blame and praise are equal, who is silent, content with whatever comes, without a fixed home, steady of mind and full of devotion — that man is dear to me.",
           bhashya=[
               {"text": "tulyanindāstutiḥ nindā ca stutiśca nindāstutī. te tulye yasya saḥ tulyanindāstutiḥ. maunī maunavān saṃyatavāk, santuṣṭaḥ yena kenacit śarīrasthitimātreṇa, tathā coktam. “yena kena cidācchanno yena kenacidāśitaḥ | yatra kvacana śāyī syāttaṃ devā brāhmaṇaṃ viduḥ” || (śāṃ.pa. 245.12) iti. kiṃ ca aniketaḥ niketaḥ āśrayaḥ nivāsaḥ niyataḥ na vidyate yasya saḥ aniketaḥ “nāgāre” ityādi smṛtyantarāt. sthiramatiḥ – sthirā paramārthavastuviṣayā matiḥ yasya saḥ sthiramatiḥ, bhaktimān me priyaḥ naraḥ.", "tr": "Equal in blame and praise — he to whom blame and praise are equal; silent, observing silence, restrained in speech; content with anything whatever, with the bare maintenance of the body — as it has been said, 'Clothed with anything, fed with anything, lying down anywhere — him the gods know as a brāhmaṇa' (Śāntiparvan 245.12). Moreover homeless — who has no fixed shelter, refuge, dwelling — according to another smṛti, 'not in a house' and so on. Steady of mind — whose mind, concerned with the supreme reality, is steady; full of devotion: such a man is dear to me."},
           ]),
        _v([
            "ye tu dharmyāmṛtamidaṃ yathoktaṃ paryupāsate |",
            "śraddadhānā matparamā bhaktāste'tīva me priyāḥ",
        ], "|| 20 ||",
           "But those who, with faith, holding me supreme, follow this nectar of dharma as it has been taught — those devotees are exceedingly dear to me.",
           bhashya=[
               {"text": "“adveṣṭā sarvabhūtānām” (13) ityādinā akṣarasyopāsakānāṃ nivṛttasarvaiṣaṇānāṃ sannyāsināṃ paramārthajñānaniṣṭhānāṃ dharmajātaṃ upakrāntam upasaṃharati.", "intro": True, "tr": "He concludes the set of qualities, begun with 'without hatred towards all beings' (12.13), of the renouncers who meditate on the imperishable, who have ceased from all cravings and are steadfast in the knowledge of the supreme truth."},
               {"text": "ye tu sannyāsinaḥ dharmyāmṛtaṃ dharmāt anapetaṃ dharmyaṃ ca tat amṛtaṃ ca tat, amṛtatvahetutvāt idaṃ yathoktam “adveṣṭā sarvabhūtānām” ityādinā, paryupāsate anutiṣṭhanti, śraddadhānāḥ santaḥ matparamāḥ yathoktāḥ aham akṣarātmā paramaḥ niratiśayāgatiḥ, yeṣāṃ te matparamāḥ, madbhaktāḥ ca uttamāṃ paramārthajñānalakṣaṇāṃ bhaktim āśritāḥ, te atīva me priyāḥ “priyo hi jñānino'tyartham” (7.17) iti yat sūcitaṃ tad vyākhyāya upasaṃhṛtaṃ “bhaktāste'tīva me priyāḥ” iti. yasmāt dharmyāmṛtam idaṃ yathoktam anutiṣṭhan bhagavataḥ viṣṇoḥ parameśvarasya atīva me priyaḥ bhavati tasmāt idaṃ dharmyāmṛtaṃ mumukṣuṇā yatnataḥ anuṣṭheyaṃ viṣṇoḥ priyaṃ paraṃ dhāma jigamiṣuṇā – iti vākyārthaḥ.", "tr": "But those renouncers who follow, practise, this righteous nectar — righteous, not departing from dharma, and nectar, being the cause of immortality — as described in 'without hatred towards all beings' and so on; who have faith, intent on me — for whom I, as described, the imperishable Self, am the supreme, the unsurpassed goal; and devoted to me, having taken to the highest devotion, which is knowledge of the supreme truth — they are exceedingly dear to me. What was hinted at in 'for I am exceedingly dear to the man of knowledge' (7.17) has been explained and is concluded with 'those devotees are exceedingly dear to me'. Since by practising this righteous nectar as described one becomes exceedingly dear to me, the Lord Viṣṇu, the supreme Lord, therefore this righteous nectar is to be practised with effort by the seeker of liberation who wishes to reach the supreme abode, dear to Viṣṇu — this is the meaning of the passage."},
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsu upaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjunasaṃvāde bhaktiyogo nāma dvādaśo– dhyāyaḥ", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the twelfth chapter, Bhakti Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣyaśrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye bhaktiyogo nāma dvādaśo'dhyāyaḥ", "gloss": "Thus ends the twelfth chapter, Bhakti Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
