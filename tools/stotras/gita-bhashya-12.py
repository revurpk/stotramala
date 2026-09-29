# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 12 (Bhakti Yoga), with Śaṅkara's bhāṣya. The Sanskrit
# (mūla and bhāṣya, both public domain) is converted from the text layer of
# the Ramakrishna Math, Hyderabad edition (2013), whose legacy Telugu font was
# mapped to Unicode glyph by glyph; its Telugu translation is not used. Collated
# against Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; every
# correction is logged in SOURCES §7.4. Verse translations are original; the
# bhāṣya is untranslated. Generated from the collated text — edit here, not
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
               {"text": "dvitīya prabhṛtiṣu adhyāyeṣu vibhūtyanteṣu paramātmanaḥ brahmaṇaḥ akṣarasya vidhvastasarva upādhiviśeṣasya upāsanam uktam. sarvayogaiśvarya sarvajñānaśaktimatsattvopādheḥ īśvarasya tava ca upāsanaṃ tatra tatra uktam. viśvarūpādhyāye tu aiśvaram ādyaṃ samasta– jagadātmarūpaṃ viśvarūpaṃ tvadīyaṃ darśitam upāsanārthameva tvayā. tacca darśayitvā uktavānasi “matkarmakṛt” ityādi. ataḥ aham anayoḥ ubhayoḥ pakṣayoḥ viśiṣṭatarabubhutsayā tvāṃ pṛcchāmi iti –", "intro": True},
               "evamiti atītānantara ślokena uktam arthaṃ parāmṛśati “matkarmakṛt” (11.55) ityādinā. evaṃ satatayuktāḥ nairantaryeṇa bhagavatkarmādau yathokte'rthe samāhitāḥ santaḥ pravṛttā ityarthaḥ. ye bhaktāḥ ananyaśaraṇāḥ santaḥ tvāṃ yathādarśitaṃ viśvarūpaṃ paryupāsate dhyāyanti, te, ye cānye'pi tyaktasarvaiṣaṇāḥ sannyastasarvakarmāṇaḥ yathāviśeṣitaṃ brahma akṣaraṃ nirastasarvopādhitvāt avyaktam akaraṇagocaraṃ, yat hi loke karaṇagocaraṃ tat vyaktam ucyate. ajñeḥ dhātoḥ tatkarmakatvāt, idaṃ tu akṣaraṃ tadviparītaṃ, śiṣṭaiśca ucyamānaiḥ viśeṣaṇaiḥ viśiṣṭaṃ tat ye cāpi paryupāsate teṣām ubhayeṣāṃ madhye ke yogavittamāḥ, ke atiśayena yogavidaḥ ityarthaḥ.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "mayyāveśya mano ye māṃ nityayuktā upāsate |",
            "śraddhayā parayopetāste me yuktatamā matāḥ",
        ], "|| 2 ||",
           "The Blessed Lord said: Those who fix their minds on me and worship me, ever disciplined, endowed with supreme faith — them I hold to be the most disciplined.",
           bhashya=[
               {"text": "ye tvakṣaropāsakāḥ samyagdarśinaḥ nivṛttaiṣaṇāḥ te tāvattiṣṭhantu. tān prati yadvaktavyaṃ tadupariṣṭāt vakṣyāmaḥ (12.20). ye tu itare –", "intro": True},
               "mayi viśvarūpe parameśvare, āveśya samādhāya, manaḥ ye bhaktāḥ santaḥ māṃ sarvayogeśvarāṇām adhīśvaraṃ sarvajñaṃ, vimuktarāgādikleśatimiradṛṣṭiṃ nityayuktāḥ atītānantarādhyāyānte uktaślokārthanyāyena satatayuktāḥ santaḥ upāsate, śraddhayā parayā prakṛṣṭayā upetāḥ ye, te me mama yuktatamāḥ matāḥ abhipretāḥ yuktatamāḥ iti. nairantaryeṇa hi te maccittatayā ahorātram ativāhayanti, ataḥ yuktaṃ tān prati yuktatamāḥ iti vaktum.",
           ]),
        _v([
            "ye tvakṣaramanirdeśyamavyaktaṃ paryupāsate |",
            "sarvatragamacintyaṃ ca kūṭasthamacalaṃ dhruvam",
        ], "|| 3 ||",
           "But those who worship the Imperishable, the indefinable, the unmanifest, the all-pervading and unthinkable, the unchanging, the immovable, the constant,",
           bhashya=[
               {"text": "kiṃ itare yuktatamāḥ na bhavanti? na, kintu tān prati yat vaktavyaṃ tat śṛṇu –", "intro": True},
           ]),
        _v([
            "sanniyamyendriyagrāmaṃ sarvatra samabuddhayaḥ |",
            "te prāpnuvanti māmeva sarvabhūtahite ratāḥ",
        ], "|| 4 ||",
           "restraining all the senses, even-minded everywhere, delighting in the welfare of all beings — they too reach me alone.",
           bhashya=[
               "ye tu akṣaram, anirdeśyam avyaktatvāt aśabdagocaram iti na nirdeṣṭuṃ śakyate, ataḥ anirdeśyam, avyaktaṃ na kenāpi pramāṇena vyajyate iti avyaktam, paryupāsate pari samantāt upāsate, upāsanaṃ nāma yathāśāstram upāsyasya arthasya viṣayīkaraṇena, sāmīpyam upagamya tailadhārāvat samānapratyayapravāheṇa dīrghakālaṃ yat āsanaṃ tat upāsanam ācakṣate. akṣarasya viśeṣaṇam āha upāsyasya sarvatragaṃ vyomavat vyāpi, acintyaṃ ca avyaktatvāt acintyam. yat hi karaṇagocaraṃ tat manasā'pi cintyaṃ, tadviparītatvāt acintyam akṣaram kūṭastham – dṛśyamānaguṇakam antardoṣaṃ vastukūṭaṃ, kūṭarūpakaṃ kūṭasākṣyam ityādau kūṭaśabdaḥ prasiddho loke. tathā ca avidyādyanekasaṃsārabījam antardoṣavat māyā'vyākṛtādi aneka śabdavācyatayā – “māyāṃ tu prakṛtiṃ vidyāt māyinaṃ tu maheśvaram” (śve. u.4.10) “mama māyā duratyayā” (7.14) ityādau prasiddhaṃ yat tat kūṭam, tasmin kūṭe sthitaṃ kūṭasthaṃ tadadhyakṣatayā. athavā – rāśiḥ iva sthitaṃ kūṭastham, ataḥ eva acalaṃ, yasmāt acalaṃ tasmāt dhruvaṃ nityamityarthaḥ.",
               "sanniyamyeti : sanniyamya samyak niyamya upasaṃhṛtya, indriyagrāmam indriyasamudāyaṃ, sarvatra sarvasmin kāle samabuddhayaḥ – samā tulyā buddhiḥ yeṣāṃ iṣṭāniṣṭa prāptau te samabuddhayaḥ. te ye evaṃvidhāḥ te prāpnuvanti mām eva sarvabhūtahite ratāḥ. na tu teṣāṃ vaktavyaṃ kiñcit “māṃ te prāpnuvantīti”, “jñānītvātmaiva me matam” (7.18) iti hi uktam. na hi bhagavatsvarūpāṇāṃ satāṃ yuktatamatvam ayuktatamatvaṃ vā vācyam. kintu –",
           ]),
        _v([
            "kleśo'dhikatarasteṣāmavyaktāsaktacetasām |",
            "avyaktā hi gatirduḥkhaṃ dehavadbhiravāpyate",
        ], "|| 5 ||",
           "The difficulty is greater for those whose minds are set on the unmanifest; for the goal that is unmanifest is hard for embodied beings to reach.",
           bhashya=[
               "kleśaḥ adhikataraḥ – yadyapi matkarmādiparāṇāṃ kleśaḥ adhikaḥ eva, kleśaḥ adhikataraḥ tu akṣarātmanāṃ paramātmadarśināṃ dehābhimānaparityāganimittaḥ, avyaktāsaktacetasām – avyakte āsaktaṃ cetaḥ yeṣāṃ te avyaktāsaktacetasaḥ teṣām avyaktāsaktacetasām. avyaktā hi yasmāt, yā gatiḥ akṣarātmikā, duḥkhaṃ sā dehavadbhiḥ dehābhimānavadbhiḥ avāpyate, ataḥ kleśaḥ adhikataraḥ, akṣaropāsakānāṃ yadvartanaṃ tat upariṣṭāt (12.13'20) vakṣyāmaḥ.",
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
               "ye tviti – ye tu sarvāṇi karmāṇi mayi īśvare sannyasya, matparāḥ ahaṃ paraḥ yeṣāṃ te matparāḥ santaḥ, ananyena eva – avidyamānam anyat ālambanaṃ viśvarūpaṃ devam ātmānaṃ muktvā yasya saḥ ananyaḥ, tena ananyenaiva, kena? yogena samādhinā, māṃ dhyāyantaḥ cintayantaḥ upāsate. teṣāṃ kiṃ –",
               "teṣāṃ madupāsanaikaparāṇām. aham īśvaraḥ, samuddhartā – kutaḥ ityāha – mṛtyusaṃsārasāgarāt, mṛtyuyuktaḥ saṃsāraḥ mṛtyusaṃsāraḥ, sa eva sāgaraḥ iva sāgaraḥ, dustaratvāt. tasmāt mṛtyusaṃsārasāgarāt, ahaṃ teṣāṃ samuddhartā bhavāmi, na cirāt, kiṃ tarhi? kṣipram eva, he pārtha, mayi āveśitacetasām – mayi viśvarūpe āveśitaṃ praveśitaṃ samāhitaṃ cetaḥ yeṣāṃ te mayyāveśitacetasaḥ, teṣām. yataḥ evaṃ, tasmāt –",
           ]),
        _v([
            "mayyeva mana ādhatsva mayi buddhiṃ niveśaya |",
            "nivasiṣyasi mayyeva ata ūrdhvaṃ na saṃśayaḥ",
        ], "|| 8 ||",
           "Fix your mind on me alone; let your understanding enter into me. Then you will dwell in me alone hereafter; of this there is no doubt.",
           bhashya=[
               "mayyeva viśvarūpe īśvare, manaḥsaṅkalpavikalpātmakam, ādhatsva sthāpaya. mayyeva adhyavasāyaṃ kurvatīṃ buddhim, ādhatsva niveśaya. tataḥ te kiṃ syāditi śṛṇu – nivasiṣyasi nivatsyasi, niścayena madātmanā mayi nivāsaṃ kariṣyasyeva, ataḥ śarīrapātāt ūrdhvaṃ. na saṃśayaḥ, saṃśayaḥ atra na kartavyaḥ.",
           ]),
        _v([
            "atha cittaṃ samādhātuṃ na śaknoṣi mayi sthiram |",
            "abhyāsayogena tato māmicchāptuṃ dhanañjaya",
        ], "|| 9 ||",
           "But if you cannot keep your mind steadily fixed on me, then seek to reach me by the yoga of practice, Dhanañjaya.",
           bhashya=[
               "atheti – atha evaṃ yathā avocaṃ tathā mayi cittaṃ samādhātuṃ sthāpayituṃ, sthiram acalaṃ, na śaknoṣi cet, tataḥ paścāt, abhyāsayogena cittasya ekasmin ālambane sarvataḥ samāhṛtya punaḥ punaḥ sthāpanam abhyāsaḥ, tatpūrvakaḥ yogaḥ samādhānalakṣaṇaḥ, tena abhyāsayogena, māṃ viśvarūpam, iccha prārthayasva, āptuṃ prāptuṃ, he dhanañjaya.",
           ]),
        _v([
            "abhyāse'pyasamartho'si matkarmaparamo bhava |",
            "madarthamapi karmāṇi kurvan siddhimavāpsyasi",
        ], "|| 10 ||",
           "If you are unable even to practise, be intent on work for me; by doing actions for my sake you will attain perfection.",
           bhashya=[
               "abhyāse'pīti – abhyāse'pi, asamarthaḥ aśaktaḥ, asi tarhi, matkarmaparamaḥ bhava. madarthaṃ karma, matkarma tatparamaḥ matkarmapradhānaḥ ityarthaḥ. abhyāsena vinā madartham api karmāṇi kevalaṃ kurvan, siddhiṃ sattvaśuddhiyogajñānaprāptidvāreṇa avāpsyasi.",
           ]),
        _v([
            "athaitadapyaśakto'si kartuṃ madyogamāśritaḥ |",
            "sarvakarmaphalatyāgaṃ tataḥ kuru yatātmavān",
        ], "|| 11 ||",
           "If you cannot do even this, then, taking refuge in my yoga and controlling yourself, give up the fruit of all actions.",
           bhashya=[
               "athaitaditi – atha punaḥ etadapi yat uktaṃ matkarmaparatvaṃ tat kartum aśaktaḥ asi, madyogam āśritaḥ – mayi kriyamāṇāni sannyasya yatkaraṇaṃ teṣām anuṣṭhānaṃ saḥ madyogaḥ, tam āśritaḥ san sarvakarmaphalatyāgaṃ – sarveṣāṃ karmaṇāṃ phalasannyāsaṃ sarvakarma phalatyāgaṃ, tataḥ anantaraṃ, kuru, yatātmavān saṃyatacittaḥ san ityarthaḥ.",
           ]),
        _v([
            "śreyo hi jñānamabhyāsāt jñānāddhyānaṃ viśiṣyate |",
            "dhyānātkarmaphalatyāgastyāgācchāntiranantaram",
        ], "|| 12 ||",
           "For knowledge is better than practice; meditation is superior to knowledge; the giving up of the fruit of action is better than meditation; and from giving up follows peace at once.",
           bhashya=[
               {"text": "idānīṃ sarvakarmaphalatyāgaṃ stauti –", "intro": True},
               "śreyaḥ hi praśasyataraṃ jñānaṃ, kasmāt? (a)vivekapūrvakāt abhyāsāt, tasmādapi jñānāt jñānapūrvakaṃ dhyānaṃ viśiṣyate. jñānavataḥ dhyānādapi karmaphalatyāgaḥ “viśiṣyate” ityanuṣajyate. evaṃ karmaphalatyāgāt pūrvoktaviśeṣaṇavataḥ śāntiḥ upaśamaḥ sahetukasya saṃsārasya anantarameva syāt, na tu kālāntaram apekṣate.",
               "ajñasya karmaṇi pravṛttasya pūrvopadiṣṭopāyānuṣṭhānāśaktau sarvakarmaṇāṃ phalatyāgaḥ śreyaḥ sādhanam upadiṣṭaṃ, na prathamameva, ataḥ ca “śreyo hi jñānamabhyāsāt” iti uttarottara viśiṣṭatvopadeśena sarvakarmaphalatyāgaḥ stūyate, sampannasādhanānuṣṭhānāśaktau anuṣṭheyatvena śrutatvāt. kena dharmeṇa stutitvam? “yadā sarve pramucyante” (kaṭha. u.6.14) iti sarvakāmaprahāṇāt amṛtatvam uktaṃ tat prasiddham. kāmāśca sarve śrautasmārtakarmaṇāṃ phalāni. tattyāge ca viduṣaḥ jñānaniṣṭhasya ananta raiva śāntiḥ. iti sarvakāmatyāgasāmānyam ajñakarmaphala– tyāgasya api asti iti tatsāmānyāt sarvakarmaphalatyāgastutiḥ iyaṃ prarocanārthā. yathā agastyena brāhmaṇena samudraḥ pītaḥ iti idānīntanāḥ api brāhmaṇāḥ brāhmaṇatvasāmānyāt stūyante. evaṃ karmaphalatyāgāt karmayogasya śreyaḥ sādhanatvam abhihitam.",
           ]),
        _v([
            "adveṣṭā sarvabhūtānāṃ maitraḥ karuṇa eva ca |",
            "nirmamo nirahaṅkāraḥ samaduḥkhasukhaḥ kṣamī",
        ], "|| 13 ||",
           "He who bears no ill will to any being, who is friendly and compassionate, free from 'mine' and from 'I', even in pleasure and pain, forbearing,",
           bhashya=[
               {"text": "atra ca ātmeśvarabhedam āśritya viśvarūpe īśvare cetaḥ samādhānalakṣaṇaḥ yogaḥ uktaḥ, īśvarārthaṃ karmānuṣṭhānādi ca. “athaitadapyaśakto'si” (12.11) iti ajñānakāryasūcanāt na abhedadarśinaḥ akṣaropāsakasya karmayogaḥ upapadyate iti darśayati. tathā karmayoginaḥ akṣaropāsanānupattiṃ darśayati bhagavān “te prāpnuvanti māmeva” (12.4) iti akṣaropāsakānāṃ kaivalya prāptau svātantryam uktvā itareṣāṃ pāratantryāt īśvarādhīnatāṃ darśitavān “teṣāmahaṃ samuddhartā” (12.7)iti. yadi hi īśvarasya ātmabhūtāḥ te matāḥ abhedadarśitvāt akṣarasvarūpā eva te iti samuddharaṇakarmaviṣayavacanaṃ tān prati apeśalaṃ syāt. yasmācca arjunasya atyantameva hitaiṣī bhagavān tasya samyagdarśanānvitaṃ karmayogaṃ bhedadṛṣṭimantam eva upadiśati. na ca ātmānam īśvaraṃ pramāṇataḥ buddhvā kasyacit guṇabhāvaṃ jigamiṣati kaścit, virodhāt. tasmāt akṣaropāsakānāṃ samyagdarśananiṣṭhānāṃ sannyāsināṃ tyaktasarvaiṣaṇānāṃ “adveṣṭā sarvabhūtānām” ityādi dharmapūgaṃ sākṣāt amṛtatvakāraṇaṃ vakṣyāmīti pravartate.", "intro": True},
               "adveṣṭā sarvabhūtānām, sarveṣām bhūtānām na dveṣṭā adveṣṭā ātmanaḥ duḥkhahetumapi na kiñcit dveṣṭi, sarvāṇi bhūtāni ātmatvena hi paśyati. maitraḥ – mitrabhāvaḥ maitrī. mitratayā vartate iti maitraḥ. karuṇaḥ eva ca karuṇā kṛpā duḥkhiteṣu dayā. tadvān karuṇaḥ, sarvabhūtānām: abhayapradaḥ sannyāsī ityarthaḥ. nirmamaḥ – mamapratyaya– varjitaḥ. nirahaṅkāraḥ nirgatāhampratyayaḥ. samaduḥkhasukhaḥ. same duḥkhasukhe dveṣarāgayoḥ apravartake yasya saḥ samaduḥkhasukhaḥ kṣamī kṣamāvān ākruṣṭaḥ abhihitaḥ vā avikriyaḥ eva āste.",
           ]),
        _v([
            "santuṣṭaḥ satataṃ yogī yatātmā dṛḍhaniścayaḥ |",
            "mayyarpitamanobuddhiryo madbhaktaḥ sa me priyaḥ",
        ], "|| 14 ||",
           "ever content, a yogin, self-controlled, firm in resolve, with mind and understanding offered to me — he who is thus my devotee is dear to me.",
           bhashya=[
               "santuṣṭa iti : santuṣṭaḥ, satataṃ nityaṃ dehasthitikāraṇasya lābhe alābhe ca utpannālampratyayaḥ. tathā guṇavallābhe viparyaye ca santuṣṭhaḥ. satataṃ, yogī samāhita cittaḥ, yatātmā saṃyatasvabhāvaḥ, dṛḍhaniścayaḥ – dṛḍhaḥ sthiraḥ niścayaḥ adhyavasāyaḥ yasya ātmatattvaviṣaye saḥ dṛḍhaniścayaḥ, mayi arpitamanobuddhiḥ saṅkalpavikalpātmakaṃ manaḥ adhyavasāyalakṣaṇā buddhiḥ, te mayyeva arpite sthāpite yasya sannyāsinaḥ saḥ mayi arpitamanobuddhiḥ. yaḥ īdṛśaḥ madbhaktaḥ saḥ me priyaḥ. “priyo hi jñānino'tyarthamahaṃ sa ca mama priyaḥ” (7.17) iti saptame adhyāye sūcitaṃ, tat iha prapañcyate.",
           ]),
        _v([
            "yasmānnodvijate loko lokānnodvijate ca yaḥ |",
            "harṣāmarṣabhayodvegairmukto yaḥ sa ca me priyaḥ",
        ], "|| 15 ||",
           "He by whom the world is not troubled, and who is not troubled by the world, who is free from elation, impatience, fear and agitation, is dear to me.",
           bhashya=[
               "yasmāditi – yasmāt sannyāsinaḥ. na udvijate na udvegaṃ gacchati na santapyate na saṅkṣubhyati lokaḥ, tathā lokāt na udvijate ca yaḥ, harṣāmarṣabhayodvegaiḥ – harṣaśca amarṣaśca bhayaṃ ca udvegaśca taiḥ harṣāmarṣabhayodvegaiḥ muktaḥ. harṣaḥ priyalābhe antaḥkaraṇasya utkarṣaḥ romāñcanāśrupātādiliṅgaḥ amarṣaḥ asahiṣṇutā, bhayaṃ trāsaḥ, udvegaḥ udvignatā, taiḥ muktaḥ yaḥ saḥ ca me priyaḥ.",
           ]),
        _v([
            "anapekṣaḥ śucirdakṣa udāsīno gatavyathaḥ |",
            "sarvārambhaparityāgī yo madbhaktaḥ sa me priyaḥ",
        ], "|| 16 ||",
           "He who is free from wants, pure, capable, indifferent, untroubled, who has renounced all undertakings — he who is thus my devotee is dear to me.",
           bhashya=[
               "anapekṣaḥ iti – dehendriyaviṣayasambandhādiṣu apekṣā viṣayeṣu apekṣā yasya nāsti saḥ anapekṣaḥ niḥspṛhaḥ, śuciḥ bāhyena ābhyantareṇa ca śaucena sampannaḥ, dakṣaḥ pratyutpanneṣu kāryeṣu sadyaḥ yathāvat pratipattuṃ samarthaḥ, udāsīnaḥ na kasyacit mitrādeḥ pakṣaṃ bhajate yaḥ sa udāsīnaḥ, yatiḥ. gatavyathaḥ gatabhayaḥ, sarvārambhaparityāgī ārabhyante iti ārambhāḥ, ihāmutrārthaphalabhogārthāni kāmahetūni karmāṇi sarvārambhāḥ, tān parityaktuṃ śīlam asyeti sarvārambhaparityāgī yaḥ madbhaktaḥ saḥ me priyaḥ. kiñca –",
           ]),
        _v([
            "yo na hṛṣyati na dveṣṭi na śocati na kāṅkṣati |",
            "śubhāśubhaparityāgī bhaktimān yaḥ sa me priyaḥ",
        ], "|| 17 ||",
           "He who neither rejoices nor hates, neither grieves nor desires, who has renounced good and evil, and is full of devotion, is dear to me.",
           bhashya=[
               "yaḥ na hṛṣyati iṣṭaprāptau, na dveṣṭi aniṣṭaprāptau, na śocati priyaviyoge, na ca aprāptaṃ kāṅkṣati, śubhāśubhe karmaṇī parityaktuṃ śīlam asyeti śubhāśubhaparityāgī, bhaktimān yaḥ, sa me priyaḥ.",
           ]),
        _v([
            "samaḥ śatrau ca mitre ca tathā mānāpamānayoḥ |",
            "śītoṣṇasukhaduḥkheṣu samaḥ saṅgavivarjitaḥ",
        ], "|| 18 ||",
           "He who is the same to foe and friend, in honour and dishonour, in cold and heat, in pleasure and pain, and free from attachment;",
           bhashya=[
               "samaḥ iti – samaḥ śatrau ca mitre ca tathā, mānāpamānayoḥ pūjāparibhavayoḥ, śītoṣṇasukhaduḥkheṣu samaḥ sarvatra ca saṅgavarjitaḥ. kiñca",
           ]),
        _v([
            "tulyanindāstutirmaunī santuṣṭo yena kena cit |",
            "aniketaḥ sthiramatirbhaktimān me priyo naraḥ",
        ], "|| 19 ||",
           "to whom blame and praise are equal, who is silent, content with whatever comes, without a fixed home, steady of mind and full of devotion — that man is dear to me.",
           bhashya=[
               "tulyanindāstutiḥ nindā ca stutiśca nindāstutī. te tulye yasya saḥ tulyanindāstutiḥ. maunī maunavān saṃyatavāk, santuṣṭaḥ yena kenacit śarīrasthitimātreṇa, tathā coktam. “yena kena cidācchanno yena kenacidāśitaḥ | yatra kvacana śāyī syāttaṃ devā brāhmaṇaṃ viduḥ” || (śāṃ.pa. 245.12) iti. kiṃ ca aniketaḥ niketaḥ āśrayaḥ nivāsaḥ niyataḥ na vidyate yasya saḥ aniketaḥ “nāgāre” ityādi smṛtyantarāt. sthiramatiḥ – sthirā paramārthavastuviṣayā matiḥ yasya saḥ sthiramatiḥ, bhaktimān me priyaḥ naraḥ.",
           ]),
        _v([
            "ye tu dharmyāmṛtamidaṃ yathoktaṃ paryupāsate |",
            "śraddadhānā matparamā bhaktāste'tīva me priyāḥ",
        ], "|| 20 ||",
           "But those who, with faith, holding me supreme, follow this nectar of dharma as it has been taught — those devotees are exceedingly dear to me.",
           bhashya=[
               {"text": "“adveṣṭā sarvabhūtānām” (13) ityādinā akṣarasyopāsakānāṃ nivṛttasarvaiṣaṇānāṃ sannyāsināṃ paramārthajñānaniṣṭhānāṃ dharmajātaṃ upakrāntam upasaṃharati.", "intro": True},
               "ye tu sannyāsinaḥ dharmyāmṛtaṃ dharmāt anapetaṃ dharmyaṃ ca tat amṛtaṃ ca tat, amṛtatvahetutvāt idaṃ yathoktam “adveṣṭā sarvabhūtānām” ityādinā, paryupāsate anutiṣṭhanti, śraddadhānāḥ santaḥ matparamāḥ yathoktāḥ aham akṣarātmā paramaḥ niratiśayāgatiḥ, yeṣāṃ te matparamāḥ, madbhaktāḥ ca uttamāṃ paramārthajñānalakṣaṇāṃ bhaktim āśritāḥ, te atīva me priyāḥ “priyo hi jñānino'tyartham” (7.17) iti yat sūcitaṃ tad vyākhyāya upasaṃhṛtaṃ “bhaktāste'tīva me priyāḥ” iti. yasmāt dharmyāmṛtam idaṃ yathoktam anutiṣṭhan bhagavataḥ viṣṇoḥ parameśvarasya atīva me priyaḥ bhavati tasmāt idaṃ dharmyāmṛtaṃ mumukṣuṇā yatnataḥ anuṣṭheyaṃ viṣṇoḥ priyaṃ paraṃ dhāma jigamiṣuṇā – iti vākyārthaḥ.",
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsu upaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjunasaṃvāde bhaktiyogo nāma dvādaśo– dhyāyaḥ", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the twelfth chapter, Bhakti Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣyaśrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye bhaktiyogo nāma dvādaśo'dhyāyaḥ", "gloss": "Thus ends the twelfth chapter, Bhakti Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
