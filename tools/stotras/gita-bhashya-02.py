# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 2 (Sāṅkhya Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 2 · Sāṅkhya Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 2",
    "h1": "Bhagavad Gītā · Chapter 2",
    "subtitle": "Sāṅkhya Yoga · the yoga of knowledge · with Śaṅkara's bhāṣya",
    "note": "Kṛṣṇa answers Arjuna's grief with the teaching of the undying Self and the discipline of action without attachment, and closes with the portrait of the sage of steady wisdom (sthitaprajña). Śaṅkara's commentary begins at 2.10–11 with a long introduction on the two paths, knowledge and action, which sets the frame for the whole bhāṣya.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 1', 'gita-bhashya-01-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 3 ›', 'gita-bhashya-03-iast.html')],
    "sections": [
        {"speaker": "sañjaya uvāca"},
        _v([
            "taṃ tathā kṛpayāviṣṭamaśrupūrṇākulekṣaṇam |",
            "viṣīdantamidaṃ vākyamuvāca madhusūdanaḥ",
        ], "|| 1 ||",
           "Sañjaya said: To him, thus overcome with pity, his eyes troubled and filled with tears, despairing, Madhusūdana spoke these words."),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "kutastvā kaśmalamidaṃ viṣame samupasthitam |",
            "anāryajuṣṭamasvargyamakīrtikaramarjuna",
        ], "|| 2 ||",
           "The Blessed Lord said: Whence has this faintness come upon you in a time of crisis, Arjuna? It is unworthy of a noble man; it leads neither to heaven nor to honour."),
        _v([
            "klaibyaṃ mā sma gamaḥ pārtha naitattvayyupapadyate |",
            "kṣudraṃ hṛdayadaurbalyaṃ tyaktvottiṣṭha parantapa",
        ], "|| 3 ||",
           "Do not yield to unmanliness, Pārtha; it does not become you. Cast off this petty weakness of heart and rise up, scorcher of foes!"),
        {"speaker": "arjuna uvāca"},
        _v([
            "kathaṃ bhīṣmamahaṃ saṅkhye droṇaṃ ca madhusūdana |",
            "iṣubhiḥ pratiyotsyāmi pūjārhāvarisūdana",
        ], "|| 4 ||",
           "Arjuna said: How shall I fight Bhīṣma and Droṇa in battle with arrows, O Madhusūdana, when both deserve my worship, O slayer of enemies?"),
        _v([
            "gurūnahatvā hi mahānubhāvān śreyo bhoktuṃ bhaikṣyamapīha loke |",
            "hatvārthakāmāṃstu gurūnihaiva bhuñjīya bhogān rudhirapradigdhān",
        ], "|| 5 ||",
           "Better to live even by begging in this world than to slay these noble teachers. For having slain my elders, however bent on gain, I would enjoy here only pleasures smeared with blood."),
        _v([
            "na caita dvidmaḥ kataranno garīyo yadvā jayema yadi vā no jayeyuḥ |",
            "yāneva hatvā na jijīviṣāma ste'vasthitāḥ pramukhe dhārtarāṣṭrāḥ",
        ], "|| 6 ||",
           "Nor do we know which is better for us — that we conquer them or that they conquer us. Those very sons of Dhṛtarāṣṭra stand before us, after killing whom we would not wish to live."),
        _v([
            "kārpaṇyadoṣopahatasvabhāvaḥ pṛcchāmi tvāṃ dharmasammūḍhacetāḥ |",
            "yacchreyaḥ syānniścitaṃ brūhi tanme śiṣyaste'haṃ śādhi māṃ tvāṃ prapannam",
        ], "|| 7 ||",
           "My very nature is stricken by the fault of pity; my mind is confused about dharma. I ask you: tell me for certain what is best. I am your disciple; teach me, who have taken refuge in you."),
        _v([
            "na hi prapaśyāmi mamāpanudyā dyacchokamucchoṣaṇamindriyāṇām |",
            "avāpya bhūmāvasapatnamṛddhaṃ rājyaṃ surāṇāmapi cādhipatyam",
        ], "|| 8 ||",
           "For I do not see what could drive away this grief that dries up my senses, even if I were to gain unrivalled, prosperous rule on earth, or even lordship over the gods."),
        {"speaker": "sañjaya uvāca"},
        _v([
            "evamuktvā hṛṣīkeśaṃ guḍākeśaḥ parantapaḥ |",
            "na yotsya iti govindamuktvā tūṣṇīṃ babhūva ha",
        ], "|| 9 ||",
           "Sañjaya said: Having spoken thus to Hṛṣīkeśa, Guḍākeśa, the scorcher of foes, said to Govinda, 'I will not fight,' and fell silent."),
        _v([
            "tamuvāca hṛṣīkeśaḥ prahasanniva bhārata |",
            "senayorubhayormadhye viṣīdantamidaṃ vacaḥ",
        ], "|| 10 ||",
           "Then, O Bhārata, Hṛṣīkeśa, as if smiling, spoke these words to him as he sat despondent between the two armies."),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "aśocyānanvaśocastvaṃ prajñāvādāṃśca bhāṣase |",
            "gatāsūnagatāsūṃśca nānuśocanti paṇḍitāḥ",
        ], "|| 11 ||",
           "The Blessed Lord said: You grieve for those who should not be grieved for, and yet you speak words of wisdom. The wise grieve neither for the dead nor for the living.",
           bhashya=[
               {"text": "atra “dṛṣṭvā tu pāṇḍavānīkam” (1.2) iti ārabhya yāvat na yotsya iti govindamuktvā tūṣṇīṃ babhūva ha” (2.9) ityetadantaḥ prāṇināṃ śokamohādi saṃsārabījabhūtadoṣodbhava kāraṇa pradarśanārthatvena vyākhyeyaḥ granthaḥ. tathā hi – arjunena rājyaguruputramitrasuhṛtsvajana sambandhibāndaveṣu “aham eṣām” “mama ete” ityevaṃ bhrāntipratyayanimittasnehavicchedādi nimittau ātmanaḥ śokamohau pradarśitau – “kathaṃ bhīṣmamahaṃ saṅkhye” (2.4) ityādinā. śokamohābhyāṃ hi abhibhūtavivekavijñānaḥ svata eva kṣattradharme yuddhe pravṛtto'pi tasmāt yuddhāt upararāma. paradharmaṃ ca bhikṣājīvanādikaṃ kartuṃ pravavṛte. tathā ca sarvaprāṇināṃ śokamohādi doṣāviṣṭa cetasāṃ svabhāvataḥ eva svadharmaparityāgaḥ pratiṣiddha sevā ca syāt. svadharme pravṛttānāmapi teṣāṃ vāñmanaḥ kāyādīnāṃ pravṛttiḥ phalābhisandhipūrvikā eva sāhaṅkārā ca bhavati. tatra evaṃ sati dharmādharmopacayāt iṣṭāniṣṭa– janma sukhaduḥkhaprāptilakṣaṇaḥ saṃsāraḥ anuparataḥ bhavati. ityataḥ saṃsāra bījabhūtau śokamohau. tayośca sarvakarmasannyāsapūrvakāt ātmajñānāt nānyataḥ nivṛttiḥ iti tat upadidikṣuḥ sarvalokānugrahārtham arjunaṃ nimittīkṛtya āha bhagavān vāsudevaḥ – aśocyānityādi.", "intro": True},
               {"text": "atra kecit āhuḥ – sarvakarmasannyāsapūrvakāt ātmajñānaniṣṭhāmātrāt eva kevalāt kaivalyaṃ na prāpyate eva. kiṃ tarhi? agnihotrādi śrautasmārta karma sahitāt jñānāt kaivalyaprāptiḥ iti sarvāsu gītāsu niścitaḥ arthaḥ iti. jñāpakaṃ ca āhuḥ asya arthasya– “atha cettvamimaṃ dharmyaṃ saṅgrāmaṃ na kariṣyasi” (2.33), “karmaṇyevādhikāraste” (2.47), “kuru karmaiva tasmāttvam” (4.15) ityādi.hiṃsādi yuktatvāt vaidika karma adharmāya iti iyam api āśaṅkā na kāryā. katham? kṣāttraṃ karma yuddhalakṣaṇaṃ gurubhrātṛputrādi hiṃsālakṣaṇaṃ atyantakrūram api svadharmaḥ iti kṛtvā na adharmāyanu tadakaraṇe ca – “tataḥ svadharmaṃ kīrtiṃ ca hitvā pāpamavāpsyasi” (2.33). iti bruvatā yāvajjīvādi śruti coditānāṃ paśvādihiṃsālakṣaṇānāṃ ca karmaṇāṃ prāgeva na adharmatvamiti suniścitaṃ uktaṃ bhavati – iti.", "intro": True},
               {"text": "tat asatnu jñānakarmaniṣṭhayoḥ vibhāgavacanāt buddhidvayāśrayayoḥ. “aśocyān” (2.11) ityādinā bhagavatā yāvat “svadharmamapi cāvekṣya” (2.31) ityetadantena granthena yatparamārthātmatattva nirūpaṇaṃ kṛtam, tat sāṅkhyam. tadviṣayā buddhiḥ, ātmanaḥ janmādi ṣaḍvikriyābhāvāt akartā ātmā iti prakaraṇārthanirūpaṇāt yā jāyate, sā sāṅkhyabuddhiḥ. sā yeṣāṃ jñānināṃ ucitā bhavati, te sāṅkhyāḥ, etasyāḥ buddheḥ janmanaḥ prāk ātmanaḥ dehādi vyatiriktatvakartṛttvabhoktṛttvādyapekṣaḥ dharmādharmaviveka pūrvakaḥ mokṣasādhanānuṣṭhāna– lakṣaṇaḥ yogaḥ tadviṣayā buddhiḥ, yogabuddhiḥ. sā yeṣāṃ karmiṇāṃ ucitā bhavati te yoginaḥ. tathā ca bhagavatā vibhakte dve buddhī nirdiṣṭe “eṣā te'bhihitā sāṅkhye buddhiryoge tvimāṃ śṛṇu” (2.39) iti. tayośca sāṅkhyabuddhyāśrayāṃ jñānayogena niṣṭhāṃ sāṅkhyānāṃ vibhaktāṃ vakṣyati – “purāvedātmanā mayā proktā” (3.3) iti. tathā ca yogabuddhyāśrayāṃ karmayogena niṣṭhāṃ vibhaktāṃ vakṣyati – “karmayogena yoginām” (3.3) iti. evaṃ sāṅkhyabuddhiṃ yogabuddhiṃ ca āśritya dve niṣṭhe vibhakte bhagavatā eva ukte jñānakarmaṇoḥ kartṛtvākartṛtvaikatvānekatva buddhyāśrayayoḥ yugapat ekapuruṣāśrayatvāsambhavaṃ paśyatā.", "intro": True},
               {"text": "yathā etadvibhāga vacanaṃ tathaiva darśitaṃ śātapathīyabrāhmaṇe – “etameva pravrājino lokamicchanto brāhmaṇāḥ pravrajanti” iti sarvakarmasannyāsaṃ vidhāya taccheṣeṇa – “kiṃ prajayā kariṣyāmo yeṣāṃ no'yamātmā'yaṃ lokaḥ” (bṛ.u.4.4.22) iti. tatraiva ca prāg dāraparigrahāt “puruṣaḥ” “ātmā” prākṛtaḥ dharmajijñāsottarakālaṃ lokatrayasādhanaṃ – putraṃ, dviprakāraṃ ca vittaṃ – “mānuṣaṃ”, “daivaṃ ca” nu tatra mānuṣaṃ karmarūpaṃ pitṛlokaprāptisādhanaṃ, vidyāṃ ca daivaṃ vittaṃ devalokaprāptisādhanaṃ “sokāmayata” iti avidyākāmavataḥ eva sarvāṇi karmāṇi śrautādīni darśitāni. tebhyaḥ (vyutthāya, pravrajanti iti) vyutthānam ātmānam eva lokam icchataḥ akāmasya vihitam, tadetadvibhāgavacanam anupapannaṃ syāt, yadi śrautakarmajñānayoḥ samuccayaḥ abhipretaḥ syāt bhagavataḥ.", "intro": True},
               {"text": "na ca arjunasya praśnaḥ upapannaḥ bhavati “jyāyasī cetkarmaṇaste” (3.1) ityādiḥ. eka puruṣānuṣṭheyatvāsambhavaṃ buddhikarmaṇoḥ bhagavatā pūrvaṃ anuktaṃ kathaṃ arjunaḥ aśrutaṃ buddheśca karmaṇaḥ jyāyastvaṃ bhagavati adhyāropayet mṛṣaiva “jyāyasī cetkarmaṇaste matā buddhiḥ” (3.1) iti.", "intro": True},
               {"text": "kiñca – yadi buddhikarmaṇoḥ sarveṣāṃ samuccayaḥ uktaḥ syāt, arjunasyāpi saḥ uktaḥ eva iti, “yacchreya etayorekaṃ tanme brūhi suniścitam” (5.1) iti kathamubhayoḥ upadeśe sati anyataraviṣayaḥ eva praśnaḥ syāt? na hi pittapraśamanārthinaḥ vaidyena madhuraṃ śītaṃ ca bhoktavyam iti upadiṣṭe “tayoranyataratpittapraśamanakāraṇaṃ brūhi” iti praśnaḥ sambhavati. atha arjunasya bhagavaduktavacanārthavivekānavadhāraṇanimittaḥ praśnaḥ kalpyate, tathāpi bhagavatā praśnānurūpaṃ prativacanaṃ deyaṃ, “mayā buddhikarmaṇoḥ samuccayaḥ uktaḥ, kimartham itthaṃ tvaṃ bhrānto'si” iti. na tu punaḥ prativacanamananurūpampṛṣṭāt anyat eva “dve niṣṭhe mayā purā prokte” (3.3) iti vaktuṃ yuktam.", "intro": True},
               {"text": "nāpi smārtenaiva karmaṇā buddheḥ samuccaye'bhiprete vibhāgavacanādi sarvam upapannam kiñca kṣatriyasya yuddhaṃ smārtaṃ karma svadharma iti jānataḥ “tat kiṃ karmaṇi ghore māṃ niyojayasi” (3.1) iti upālambhaḥ anupapannaḥ.", "intro": True},
               {"text": "tasmād gītāśāstre īṣanmātreṇāpi śrautena smārtena vā karmaṇā ātmajñānasya samuccayaḥ na kenaciddarśayituṃ śakyaḥ.", "intro": True},
               {"text": "yasya tu ajñānādrāgādi doṣato vā karmaṇi pravṛttasya yajñena, dānena, tapasā vā viśuddhasattvasya jñānam utpannaṃ paramārthatattva viṣayaṃ “ekamevedaṃ sarvaṃ brahma akartṛ ca” iti, tasya karmaṇi karmaprayojane ca nivṛtte'pi lokasaṅgrahārthaṃ yatnapūrvaṃ yathā pravṛttiḥ tathaiva karmaṇi pravṛttasya yatpravṛtti rūpaṃ dṛśyate na tat karma yena buddheḥ samuccayaḥ syāt, yathā bhagavataḥ vāsudevasya kṣātradharmaceṣṭitaṃ na jñānena samuccīyate puruṣārthasiddhayenu tadvat tatphalābhisandhyahaṅkārābhāvasya tulyatvāt viduṣaḥ. tattvavittu “nāhaṃ karomī”ti manyate, na ca tatphalam abhisandhatte. yathā ca svargādi kāmārthinaḥ agnihotrādi kāmasādhanānuṣṭhānāya āhitāgneḥ kāmye eva agnihotrādau pravṛttasya sāmikṛte vinaṣṭe'pi kāme tadeva agnihotrādi anutiṣṭhato'pi na tat kāmyam agnihotrādi bhavati. tathā ca darśayati bhagavān “kurvannapi na lipyate” (5.7), “na karoti na lipyate” (13.31) iti tatra tatra. yacca “pūrvaiḥ pūrvataraṃ kṛtam” (4.15), “karmaṇaiva hi saṃsiddhimāsthitā janakādayaḥ” (3.20) iti, tattu pravibhajya vijñeyam. tatkatham? yadi tāvatpūrve janakādayaḥ tattvavidaḥ api pravṛttakarmāṇaḥ syuḥ, te lokasaṅgrahārthaṃ “guṇā guṇeṣu vartante” (3.28) iti jñānenaiva saṃsiddhiṃ āsthitāḥ. karmasannyāse prāpte'pi karmaṇā sahaiva saṃsiddhim āsthitāḥ na karmasannyāsaṃ kṛtavantaḥ ityarthaḥ. atha na te tattvavidaḥ – īśvarasamarpitena karmaṇā sādhanabhūtena saṃsiddhiṃ, sattvaśuddhiṃ, jñānotpatti lakṣaṇāṃ vā saṃsiddhim āsthitāḥ janakādayaḥ iti vyākhyeyam. etameva artham vakṣyati bhagavān “sattvaśuddhaye karma kurvanti” (5.11) iti. “sva karmaṇā tamabhyarcya siddhiṃ vindati mānavaḥ”. (18.46) ityuktvā siddhiṃ prāptasya ca punaḥ jñānaniṣṭhāṃ vakṣyati “siddhiṃ prāpto yathā brahma” (18.50) ityādinā. tasmāt gītāśāstre kevalāt eva tattvajñānāt mokṣaprāptiḥ, na karma samuccitāt iti niścitaḥ arthaḥ. yathā ca ayamarthaḥ tathā prakaraṇaśaḥ vibhajya tatra tatra darśayiṣyāmaḥ.", "intro": True},
               {"text": "tatraivaṃ dharmasammūḍha cetasaḥ mithyājñānavataḥ mahati śokasāgare nimagnasya arjunasya anyatra ātmajñānāt uddharaṇam apaśyan bhagavān vāsudevaḥ tataḥ arjunam uddidhārayiṣuḥ ātmajñānāya avatārayan āha–", "intro": True},
               "aśocyān ityādi. na śocyāḥ aśocyāḥ, bhīṣmadroṇādayaḥ sadvṛttvāt paramārtha svarūpeṇa ca nityatvāt. tān aśocyān, anvaśocaḥ anuśocitavānasi, “te mriyante mannimittam. ahaṃ tairvinābhūtaḥ kiṃ kariṣyāmi rājyasukhādinā?” iti. tvaṃ prajñāvādān prajñāvatāṃ buddhimatāṃ vādāṃśca vacanāni ca bhāṣase. tadetat mauḍhyaṃ pāṇḍityaṃ ca virudthaṃ darśayasi ātmani, unmatta iva ityabhiprāyaḥ yasmāt gatāsūn gata prāṇān, mṛtān, agatāsūn, agata prāṇān jīvataśca nānuśocanti paṇḍitāḥ ātmajñāḥ. paṇḍā ātmaviṣayā buddhiḥ yeṣāṃ te hi paṇḍitāḥ “pāṇḍityaṃ nirvidya” (bṛ.u.3.5.1) iti śruteḥ. paramārthatastu tān nityān aśocyān anuśocasi, ataḥ mūḍhaḥ asi ityabhiprāyaḥ",
           ]),
        _v([
            "na tvevāhaṃ jātu nāsaṃ na tvaṃ neme janādhipāḥ |",
            "na caiva na bhaviṣyāmaḥ sarve vayamataḥ param",
        ], "|| 12 ||",
           "Never was there a time when I was not, nor you, nor these rulers of men; nor shall any of us ever cease to be hereafter.",
           bhashya=[
               {"text": "kutaḥ te aśocyāḥ? yataḥ nityāḥ. katham?", "intro": True},
               "na tu iti || na tu eva, jātu kadācit ahaṃ na āsam, kintu āsam eva. atīteṣu dehotpattivināśeṣu ghaṭādiṣu viyad iva nityaḥ eva ahaṃ āsaṃ iti abhiprāyaḥ. tathā – na tvaṃ na āsīḥ, kiṃ tu āsīḥ eva. tathā – na ime, janādhipāḥ na āsan, kiṃ tu āsan eva. tathā – na ca eva na bhaviṣyāmaḥ, kiṃ tu bhaviṣyāmaḥ eva sarve vayaṃ ataḥ asmāt dehavināśāt paraṃ uttarakāle'pi. triṣvapi kāleṣu nityāḥ ātma svarūpeṇa ityarthaḥ, dehabhedānuvṛttyā bahuvacanam, na ātma bhedābhiprāyeṇa.",
           ]),
        _v([
            "dehino'smin yathā dehe kaumāraṃ yauvanaṃ jarā |",
            "tathā dehāntaraprāptirdhīrastatra na muhyati",
        ], "|| 13 ||",
           "As the embodied one passes in this body through childhood, youth and old age, so it passes into another body. The steadfast are not bewildered by this.",
           bhashya=[
               {"text": "tatra kathamiva nityaḥ ātmā iti? dṛṣṭāntaṃ āha –", "intro": True},
               "dehinaḥ iti. dehaḥ asya asti iti dehī tasya dehinaḥ dehavataḥ ātmanaḥ asmin vartamāne dehe yathā yena prakāreṇa kaumāraṃ kumārabhāvaḥ bālyāvasthā, yauvanaṃ yūnaḥ bhāvaḥ madhyamāvasthā, jarā vayohāniḥ jīrṇāvasthā, iti etāḥ, tisraḥ avasthāḥ anyonyavilakṣaṇāḥ. tāsāṃ prathamāvasthānāśe na nāśaḥ, dvitīyāvasthopajanane na upajananaṃ ātmanaḥ. kiṃ tarhi? avikriyasya eva ekasya dvitīya tṛtīyāvasthāprāptiḥ ātmanaḥ dṛṣṭā. tathā tadvat eva dehāt anyaḥ dehaḥ dehāntaraṃ, tasya prāptiḥ dehāntara prāptiḥ avikriyasya eva ātmanaḥ ityarthaḥ. dhīraḥ dhīmān, tatra evaṃ sati, na muhyati na mohaṃ āpadyate.",
           ]),
        _v([
            "mātrāsparśāstu kaunteya śītoṣṇasukhaduḥkhadāḥ |",
            "āgamāpāyino'nityā stāṃstitikṣasva bhārata",
        ], "|| 14 ||",
           "The contacts of the senses with their objects, O son of Kuntī, give rise to cold and heat, pleasure and pain; they come and go and do not last. Endure them, O Bhārata.",
           bhashya=[
               {"text": "yadyapi ātmavināśanimittaḥ mohaḥ na sambhavati nityaḥ ātmā iti vijānataḥ tathāpi śītoṣṇasukhaduḥkhaprāptinimittaḥ mohaḥ laukikaḥ dṛśyate, sukhaviyoganimitto mohaḥ duḥkhasaṃyoganimittaśca śokaḥ. ityetat arjunasya vacanaṃ āśaṅkya bhagavān āha.", "intro": True},
               "mātrāsparśāḥ iti. mātrāḥ ābhiḥ, mīyante śabdādayaḥ iti śrotrādīni indriyāṇi. mātrāṇāṃ sparśāḥ śabdādibhiḥ saṃyogāḥ. te śītoṣṇasukhaduḥkhadāḥ śītaṃ uṣṇaṃ sukhaṃ duḥkhaṃ ca prayacchantīti. athavā – spṛśyante iti sparśāḥ viṣayāḥ śabdādayaḥ mātrāśca sparśāśca śītoṣṇasukhaduḥkhadāḥ – śītaṃ kadācit sukhaṃ, kadācit duḥkham. tathā uṣṇam api aniyatasvarūpam. sukhaduḥkhe punaḥ niyatarūpatāṃ na vyabhicarataḥ. ataḥ tābhyāṃ pṛthak śītoṣṇayoḥ grahaṇam. yasmāt te mātrāsparśādayaḥ āgamāpāyinaḥ āgamāpāyaśīlāḥ tasmāt anityāḥ. ataḥ tān śītoṣṇādīn titikṣasva prasahasva. teṣu harṣaṃ viṣādaṃ vā mā kārṣīḥ ityarthaḥ.",
           ]),
        _v([
            "yaṃ hi na vyathayantyete puruṣaṃ puruṣarṣabha |",
            "samaduḥkhasukhaṃ dhīraṃ so'mṛtatvāya kalpate",
        ], "|| 15 ||",
           "The steadfast man whom these do not disturb, O best of men, to whom pain and pleasure are alike — he is fit for immortality.",
           bhashya=[
               {"text": "śītoṣṇādīn sahataḥ kiṃ syāt iti? śṛṇu –", "intro": True},
               "yaṃ hi iti. yaṃ hi puruṣaṃ samaduḥkhasukhaṃ same duḥkhasukhe yasya taṃ samaduḥkhasukhaṃ sukhaduḥkhaprāptau harṣaviṣādarahitaṃ dhīraṃ dhīmantaṃ na vyathayanti na cālayanti nityātma darśanāt ete yathoktāḥ śītoṣṇādayaḥ, saḥ nityātmasvarūpadarśananiṣṭhaḥ dvandvasahiṣṇuḥ amṛtattvāya amṛtabhāvāya mokṣāya kalpate samarthaḥ bhavati.",
           ]),
        _v([
            "nā'sato vidyate bhāvo nā'bhāvo vidyate sataḥ |",
            "ubhayorapi dṛṣṭo'ntastvanayostattvadarśibhiḥ",
        ], "|| 16 ||",
           "The unreal has no being, and the real never ceases to be. The truth about both has been seen by those who see the essence of things.",
           bhashya=[
               {"text": "itaśca śokamohau akṛtvā śītoṣṇādisahanaṃ yuktaṃ, kartum, yasmāt–", "intro": True},
               "nāsataḥ iti – (na) asataḥ avidyamānasya śītoṣṇādeḥ sakāraṇasya na vidyate nāsti bhāvaḥ, bhāvanam, astitā. na hi śītoṣṇādi sakāraṇam pramāṇaiḥ nirūpyamāṇaṃ vastu sat bhavati. vikāro hi saḥ. vikāraśca vyabhicarati. yathā ghaṭādi saṃsthānaṃ cakṣuṣā nirūpyamāṇaṃ mṛdvyatirekeṇa anupalabdheḥ asat, tathā sarvo vikāraḥ kāraṇavyatirekeṇa anupalabdheḥ asan. janmapradhvaṃsābhyāṃ prāk ūrdhvaṃ ca anupalabdheḥ kāryasya ghaṭādeḥ mṛdādikāraṇasya ca tatkāraṇavyatirekeṇa anupalabdheḥ asattvam. tadasattve ca sarvābhāvaprasaṅgaḥ iti cet – nanu sarvatra buddhidvayopalabdheḥ – sadbuddhiḥ asadbuddhiḥ iti. yadviṣayā buddhiḥ na vyabhicarati, tat sat, yadviṣayā buddhiḥ vyabhicarati tat asat iti sadasadvibhāge buddhitantre sthite sarvatra dve buddhī sarvaiḥ upalabhyete sāmānādhikaraṇe – na nīlotpalavat, san ghaṭaḥ, san paṭaḥ, san hastī, iti. evaṃ sarvatra. tayoḥ buddhyoḥ ghaṭādibuddhiḥ vyabhicarati. tathā ca darśitam. na tu sadbuddhiḥ. tasmād ghaṭādibuddhiviṣayaḥ asan, vyabhicārāt, na tu sadbuddhiviṣayaḥ, avyabhicārāt.",
               "ghaṭe vinaṣṭe ghaṭabuddhau vyabhicarantyāṃ sadbuddhirapi vyabhicarati iti cet, nanu paṭādau api sadbuddhidarśanāt. viśeṣaṇaviṣayaiva sā sadbuddhiḥ. sadbuddhivat ghaṭabuddhirapi ghaṭāntare dṛśyate iti cet, nanu paṭādāvadarśanāt. sadbuddhirapi naṣṭe ghaṭe na dṛśyate iti cet na – viśeṣyābhāvāt. sadbuddhiḥ viśeṣaṇaviṣayāsatī viśeṣyābhāve viśeṣaṇānupapattau kiṃ viṣayā syāt, na tu punaḥ sadbuddheḥ viṣayābhāvāt.",
               "ekādhikaraṇatvaṃ ghaṭādi viśeṣyābhāve na yuktam iti cet – nanu “idam udakam” iti marīcyādau anyatarābhāve'pi sāmānādhikaraṇyadarśanāt. tasmāt dehādeḥ dvandvasya ca sakāraṇasya asato na vidyate bhāvaḥ iti. tathā sataḥ ca ātmanaḥ abhāvaḥ avidyamānatā na vidyate, sarvatra avyabhicārāt iti avocāma. evaṃ ātmānātmanoḥ sadasatoḥ ubhayoḥ api dṛṣṭaḥ upalabdhaḥ antaḥ nirṇayaḥ, sat sadeva asat asadeva iti tu anayoḥ yathoktayoḥ tattvadarśibhiḥ.",
               "tat iti sarvanāmanu sarvaṃ ca brahmanu tasya nāma tat iti tadbhāvaḥ tattvaṃ, brahmaṇaḥ yāthātmyam. tat draṣṭuṃ śīlaṃ yeṣāṃ te tattvadarśinaḥ taiḥ tattvadarśibhiḥ. tvamapi tattvadarśināṃ dṛṣṭiṃ āśritya śokaṃ mohaṃ ca hitvā śītoṣṇādīni niyatāniyatarūpāṇi dvandvāni, vikāro'yamasan eva marīci jalavat mithyā avabhāsate – iti manasi niścitya titikṣasva iti abhiprāyaḥ.",
           ]),
        _v([
            "avināśi tu tadviddhi yena sarvamidaṃ tatam |",
            "vināśamavyayasyāsya na kaścitkartumarhati",
        ], "|| 17 ||",
           "Know that to be indestructible by which all this is pervaded. No one can bring about the destruction of this imperishable one.",
           bhashya=[
               {"text": "kiṃ punaḥ tat yat sat eva sarvadā iti? ucyate –", "intro": True},
               "avināśi iti. avināśi na vinaṣṭuṃ śīlaṃ asya iti. tu śabdaḥ asataḥ viśeṣaṇārthaḥ, tat viddhi vijānīhi. kiṃ? yena sarvaṃ idaṃ jagat tatam vyāptaṃ sadākhyena brahmaṇā sākāśaṃ, ākāśena iva ghaṭādayaḥ. vināśaṃ adarśanaṃ abhāvam. avyayasya na vyeti upacayāpacayau na yāti iti avyayaṃ, tasya avyayasya. na etat sadākhyaṃ brahma svena rūpeṇa vyeti, vyabhicarati niravayavatvāt, dehādivat. nāpi ātmīyena, ātmīyābhāvāt. yathā devadattaḥ dhanahānyā vyeti, na tu evaṃ brahma vyeti. ataḥ avyayasya asya brahmaṇaḥ vināśaṃ na kaścit kartuṃ arhati, na kaścit ātmānaṃ vināśayituṃ śaknoti īśvaro'pi. ātmā hi brahmanu svātmani ca kriyāvirodhāt.",
           ]),
        _v([
            "antavanta ime dehā nityasyoktāḥ śarīriṇaḥ |",
            "anāśino'prameyasya tasmādyudhyasva bhārata",
        ], "|| 18 ||",
           "These bodies of the eternal, indestructible, immeasurable embodied one are said to have an end. Therefore fight, O Bhārata.",
           bhashya=[
               {"text": "kiṃ punaḥ tat asat yat svātmasattāṃ vyabhicarati iti? ucyate.", "intro": True},
               "antavantaḥ iti. antaḥ vināśaḥ vidyate yeṣāṃ te antavantaḥ. yathā mṛgatṛṣṇikādau sadbuddhiḥ anuvṛttā pramāṇanirūpaṇānte vicchidyate, sa tasya antaḥnu tathā ime dehāḥ svapnamāyā dehādivacca antavantaḥ nityasya śarīriṇaḥ śarīravataḥ anāśinaḥ aprameyasya ātmanaḥ antavantaḥ iti uktāḥ vivekibhiḥ ityarthaḥ. “nityasya” “anāśinaḥ” iti na punaruktamnu nityatvasya dvividhatvāt loke, nāśasya ca.yathā dehaḥ bhasmībhūtaḥ adarśanaṃ gataḥ naṣṭaḥ ucyate. vidyamāno'pi yathā anyathā pariṇataḥ vyādhyādiyuktaḥ jātaḥ naṣṭaḥ ucyate. tatra “nityasya” “anāśina”ḥ iti dvividhenāpi nāśena asambaddhasya ityarthaḥ. anyathā pṛthivyādivat api nityatvaṃ syāt ātmanaḥ, tat mā bhūt iti “nityasya” “anāśinaḥ” ityāha.",
               "aprameyasya sa prameyasya pratyakṣādi pramāṇaiḥ aparicchedyasya ityarthaḥ. nanu āgamena ātmā paricchidyate, pratyakṣādinā ca pūrvam. na, ātmanaḥ svataḥ siddhatvāt. siddhe hi ātmani pramātari pramitsoḥ pramāṇānveṣaṇā bhavati. na hi pūrvaṃ “itthaṃ ahaṃ” iti ātmānaṃ apramāya paścāt prameya paricchedāya pravartate. na hi ātmā nāma kasyacit aprasiddhaḥ bhavati. śāstraṃ tu antyaṃ pramāṇaṃ ataddharmāddhyāropaṇamātra nivartakatvena prāmāṇyaṃ ātmanaḥ pratipadyate, na tu ajñātārthajñāpakatvena. tathā ca śrutiḥ – “yat sākṣādaparokṣād brahma ya ātmā sarvāntaraḥ”. (bṛ.u.3.4.1) iti. yasmāt evaṃ nityaḥ avikriyaśca ātmā tasmāt yudhyasva, yuddhāt uparamaṃ mā kārṣīḥ ityarthaḥ. na hi atra yuddhakartavyatā vidhīyate, yuddhe pravṛttaḥ eva hi asau śokamoha pratibaddhaḥ tūṣṇīṃ āste. ataḥ tasya kartavya pratibandhāpanayanamātraṃ bhagavatā kriyate. tasmāt “yudhyasva” iti anuvādamātraṃ. na vidhiḥ.",
           ]),
        _v([
            "ya enaṃ vetti hantāraṃ yaścainaṃ manyate hatam |",
            "ubhau tau na vijānīto nāyaṃ hanti na hanyate",
        ], "|| 19 ||",
           "He who thinks this one a slayer, and he who thinks it slain — neither understands. It does not slay, nor is it slain.",
           bhashya=[
               {"text": "śokamohādi saṃsārakāraṇanivṛtyarthaṃ gītāśāstraṃ, na pravartakaṃ, iti etasya arthasya sākṣibhūte ṛcau (kaṭha.u.2.18.19) ānināya bhagavān. yattu manyase “yuddhe bhīṣmādayaḥ mayā hanyante, aham eva teṣāṃ hantā” iti eṣā buddhiḥ mṛṣaiva te. kathaṃ?", "intro": True},
               "ya enaṃ iti. yaḥ enaṃ prakṛtaṃ dehinaṃ vetti vijānāti hantāraṃ hanana kriyāyāḥ kartāraṃ, yaḥ ca enaṃ anyaḥ manyate hataṃ dehahananena “hataḥ aham.” iti hanana kriyāyāḥ karmabhūtaṃ, tau ubhau na vijānītaḥ na jñātavantau avivekena ātmānam. “hantā aham,” “hataḥ asmi aham” iti dehahananena ātmānaṃ ahaṃ pratyayaviṣayaṃ yau vijānītaḥ tau ātmasvarūpānabhijñau ityarthaḥ. yasmāt na ayaṃ ātmā hanti na hanana kriyāyāḥ kartā bhavati, na hanyate na ca karma bhavatītyarthaḥ, avikriyatvāt.",
           ]),
        _v([
            "na jāyate mriyate vā kadācinnāyaṃ bhūtvā'bhavitā vā na bhūyaḥ |",
            "ajo nityaḥ śāśvato'yaṃ purāṇo na hanyate hanyamāne śarīre",
        ], "|| 20 ||",
           "It is never born and never dies; nor, having been, will it ever cease to be. Unborn, eternal, constant and ancient, it is not slain when the body is slain.",
           bhashya=[
               {"text": "kathaṃ avikriyaḥ ātmā iti dvitīyaḥ mantraḥ–", "intro": True},
               "na jāyate iti. na jāyate na utpadyate, janilakṣaṇā vastuvikriyā na ātmanaḥ vidyate ityarthaḥ. tathā na mriyate vā. vā śabdaḥ cārthe. na mriyate ca iti antyā vināśalakṣaṇā vikriyā pratiṣiddhyate. kadācit śabdaḥ sarvavikriyā pratiṣedhaiḥ sambadhyate – na kadācit jāyate, na kadācit mriyate, ityevam. yasmāt ayaṃ ātmā bhūtvā bhavanakriyāṃ anubhūya paścāt abhavitā abhāvaṃ gantā na bhūyaḥ punaḥ, tasmāt na mriyate. yo hi bhūtvā na bhavitā sa mriyate iti ucyate loke. vā śabdāt na śabdācca ayaṃ ātmā abhūtvā vā bhavitā dehavat na bhūyaḥ punaḥ. tasmāt na jāyate. yo hi abhūtvā bhavitā sa jāyate iti ucyate. naivaṃ ātmā. ataḥ na jāyate. yasmāt evaṃ tasmāt ajaḥ. yasmāt na mriyate tasmāt nityaḥ ca.",
               "yadyapi ādyantayoḥ vikriyayoḥ pratiṣedhe sarvāḥ vikriyāḥ pratiṣiddhāḥ bhavanti, tathāpi madhyabhāvinīnāṃ vikriyāṇāṃ svaśabdaiḥ eva tadarthaiḥ pratiṣedhaḥ kartavyaḥ iti anuktānām api yauvanādi samasta vikriyāṇāṃ pratiṣedhaḥ yathā syāt ityāha – śāśvataḥ ityādinā. śāśvataḥ iti apakṣayalakṣaṇā vikriyā pratiṣidhyate. śaśvat bhavaḥ śāśvataḥ. nāpakṣīyate svarūpeṇa, niravayavatvāt. nirguṇatvācca nāpi guṇakṣayeṇa apakṣayaḥ. apakṣayaviparītā api vṛddhilakṣaṇā vikriyā pratiṣidhyate purāṇaḥ iti. yaḥ hi avayavāgamena upacīyate saḥ vardhate, abhinavaḥ iti ca ucyate. ayaṃ tu ātmā niravayavatvāt purāpi navaḥ eva iti purāṇaḥnu na vardhate ityarthaḥ. tathā – na hanyate na vipariṇamyate, ityarthaḥ hanyamāne vipariṇamyamāne'pi śarīre. hantiḥ atra vipariṇāmārthaḥ draṣṭavyaḥ apunaruktatāyai. asmin mantre ṣaṭ bhāvavikārāḥ laukika vastu vikriyāḥ ātmani pratiṣidhyante. sarvaprakāravikriyā rahitaḥ ātmā iti vākyārthaḥ. yasmāt evaṃ tasmāt “ubhau tau na vijānītaḥ” (2.19) iti pūrveṇa mantreṇa asya sambandhaḥ.",
           ]),
        _v([
            "vedāvināśinaṃ nityaṃ ya enamajamavyayam |",
            "kathaṃ sa puruṣaḥ pārtha kaṃ ghātayati hanti kam",
        ], "|| 21 ||",
           "One who knows it to be indestructible, eternal, unborn and unchanging — how can such a person slay, O Pārtha, or cause anyone to slay?",
           bhashya=[
               {"text": "“ya enaṃ vetti hantāram” (2.19) ityanena mantreṇa hananakriyāyāḥ kartā karma ca na bhavatīti pratijñāya “na jāyate” ityanena avikriyatve hetum uktvā pratijñātārtham upasaṃharati.", "intro": True},
               "vedāvināśinamiti : veda vijānāti, avināśinam antyabhāva vikārarahitaṃ, nityaṃ, vipariṇāmarahitaṃ “yaḥ veda” iti sambandhaḥ. enaṃ pūrveṇa mantreṇa uktalakṣaṇam ajaṃ, janmarahitam, avyayam, apakṣayarahitaṃ, kathaṃ kena prakāreṇa saḥ vidvān puruṣaḥ adhikṛtaḥ hanti, hanana kriyāṃ karoti? kathaṃ vā ghātayati hantāraṃ prayojayati? na kathaṃ cit hanti, na kathañcit kañcit ghātayati iti ubhayatra ākṣepaḥ, evārthaḥ praśnārthāsambhavāt. hetvarthasya avikriyatvasya tulyatvāt viduṣaḥ sarvakarmapratiṣedha eva prakaraṇārthaḥ abhipretaḥ bhagavataḥ. hantestu ākṣepaḥ udāharāṇārthatvena kathitaḥ.",
               "viduṣaḥ kaṃ karmāsambhave hetuviśeṣaṃ paśyan karmāṇi ākṣipati bhagavān “kathaṃ sa puruṣaḥ” iti. nanu uktaḥ eva ātmanaḥ avikriyatvaṃ sarvakarmāsambhavakāraṇaviśeṣaḥ. satyaṃ uktaḥ na tu saḥ kāraṇaviśeṣaḥ anyatvāt viduṣaḥ avikriyāt ātmanaḥ iti. na hi avikriyaṃ sthāṇuṃ viditavataḥ karma na sambhavati iti cet – nanu viduṣaḥ ātmatvāt. na dehādi saṅghātasya vidvattā. ataḥ pāriśeṣyāt asaṃhataḥ ātmā vidvān avikriyaḥ iti tasya viduṣaḥ karmāsambhavāt ākṣepaḥ yuktaḥ “kathaṃ sa puruṣaḥ” iti.",
               "yathā buddhyādyāhṛtasya śabdādyarthasya avikriyaḥ eva san buddhivṛttyavivekavijñānena avidyayā upalabdhā ātmā kalpyate. evaṃ eva ātmānātmavivekajñānena buddhivṛttyā vidyayā – asatyarūpayā eva paramārthataḥ avikriyaḥ eva ātmā vidvān ucyate. viduṣaḥ karmāsambhavavacanāt yāni karmāṇi śāstreṇa vidhīyante tāni aviduṣaḥ vihitāni iti bhagavataḥ niścayo'vagamyate.",
               "nanu vidyāpi aviduṣaḥ eva vidhīyate, viditavidyasya piṣṭapeṣaṇavat vidyāvidhānānarthakyāt, tatra aviduṣaḥ karmāṇi vidhīyante, na viduṣaḥ iti viśeṣaḥ nopapadyate. na, anuṣṭheyasya bhāvābhāvaviśeṣopapatteḥ. agnihotrādividhyarthajñānottarakālam agnihotrādikarma aneka sādhanopasaṃhārapūrvakam anuṣṭheyaṃ, “kartā aham mama kartavyam” ityevamprakārakavijñānavataḥ aviduṣaḥ yathā anuṣṭheyaṃ bhavati na tu tathā “na jāyate” ityādyātmasvarūpa vidhyarthajñānottara kālabhāvi kiñcit anuṣṭheyaṃ bhavati, (kintu) “na ahaṃ kartā” “na ahaṃ bhoktā” ityādyātmaikatvākartṛtvādi viṣayajñānāt anyat na utpadyata iti eṣaḥ viśeṣaḥ upapadyate. yaḥ punaḥ “kartā aham” iti vetti ātmānaṃ, tasya “mama idaṃ kartavyam” iti avaśyambhāvinī buddhiḥ syātnu tadapekṣayā saḥ adhikriyate iti taṃ prati karmāṇi, sambhavanti. sa ca avidvān “ubhau tau na vijānītaḥ” (2.19) iti vacanāt. viśeṣitasya ca viduṣaḥ karmākṣepa vacanāt – “kathaṃ sa puruṣaḥ” (2.21) iti. tasmāt viśeṣitasya avikriyātmadarśinaḥ viduṣaḥ mumukṣoḥ ca sarvakarmasannyāse eva adhikāraḥ. ata eva bhagavān nārāyaṇaḥ sāṅkhyān viduṣaḥ, aviduṣaḥ ca karmiṇaḥ pravibhajya dve niṣṭhe grāhayati – “jñānayogena sāṅkhyānāṃ karmayogena yoginām” (3.3) iti. tathā ca putrāya āha bhagavān vyāsaḥ – “dvāvimāvatha panthānau” (ma.bhā.śāṃ.240.6) ityādi. tathā ca “kriyāpathaścaiva purastāt paścāt sannyāsaśca” (tai.ā.10.62.12 arthatonuvādaṃ). iti etameva vibhāgaṃ punaḥ punaḥ darśayiṣyati bhagavān – “atattvavidahaṅkāra vimūḍhātmā kartāhamiti manyate”, “tattvavittu na ahaṃ karomi” (3.27–28) iti. tathā ca “sarva karmāṇi manasā sannyasyāste” (5.13) ityādi.",
               "tatra kecit paṇḍitammanyāḥ vadanti – janmādiṣaḍbhāvavikriyārahitaḥ, avikriyaḥ akartā, ekaḥ, aham ātmā iti na kasyacit jñānam utpadyate. yasmin sati sarvakarmasannyāsaḥ upadiśyate, iti. tat nanu “na jāyate” ityādi śāstropadeśānarthakyāt. yathā ca śāstropadeśa sāmarthyāt dharmādharmāstitva vijñānaṃ kartuśca dehāntara sambandhavijñānaṃ ca utpadyate, tathā śāstrāt tasyaiva ātmanaḥ avikriyatvākartṛtvaikatvādi vijñānaṃ kasmāt na utpadyate iti praṣṭavyāḥ te. karaṇāgocaratvāt iti cet – na, “manasaivānudraṣṭavyam” (bṛ.u.4.4.19) iti śruteḥ. śāstrācāryopadeśa śamadamādisaṃskṛtaṃ manaḥ ātmadarśane karaṇam. tathā ca tadadhigamāya anumāne āgame ca sati jñānaṃ notpadyate iti sāhasam etat.",
               "jñānaṃ ca utpadyamānaṃ tadviparītaṃ ajñānaṃ avaśyaṃ bādhate iti abhyupagantavyam. tat ca ajñānaṃ darśitaṃ “hantā ahaṃ, hataḥ asmi” iti, “ubhau tau na vijānītaḥ” (2.19) iti. atra ca ātmanaḥ hananakriyāyāḥ kartṛtvaṃ, karmatvaṃ, hetukartṛtvaṃ ca ajñānakṛtaṃ darśitam. tat ca sarvakriyāsu api samānaṃ kartṛtvādeḥ avidyākṛtatvaṃ, avikriyatvāt ātmanaḥ. vikriyāvān hi kartā ātmanaḥ karmabhūtaṃ anyaṃ prayojayati “kuru” iti – tat etat aviśeṣeṇa viduṣaḥ sarvakriyāsu kartṛtvaṃ hetukartṛtvaṃ ca pratiṣedhati bhagavān vāsudevaḥ viduṣaḥ karmādhikārābhāvapradarśanārthaṃ “vedāvināśinaṃ ... kathaṃ sa puruṣaḥ” ityādinā.",
               "kva punaḥ viduṣaḥ adhikāraḥ iti? etat uktaṃ pūrvameva “jñānayogena sāṅkhyānām” (3.3) iti. tathā ca sarvakarmasannyāsaṃ vakṣyati “sarvakarmāṇi manasā” (5.13) ityādinā. nanu “manasā” iti vacanāt na vācikānāṃ kāyikānāṃ ca sannyāsaḥ iti cet – na, sarvakarmāṇi iti viśeṣitatvāt. mānasānāṃ eva sarvakarmaṇāṃ iti cet – na, manovyāpāra pūrvakatvāt vākkāyavyāpārāṇāṃ, manovyāpārābhāve tadanupapatteḥ, śāstrīyāṇāṃ vākkāyakarmaṇāṃ kāraṇāni mānasāni karmāṇi varjayitvā anyāni sarvakarmāṇi manasā sannyasya iti cet–na, “naiva kurvannakārayan” (5.13) iti viśeṣaṇāt. sarvakarmasannyāsaḥ ayaṃ bhagavatā uktaḥ mariṣyataḥ, na jīvataḥ iti cet – na, “navadvāre pure dehī ... āste” (5.13) iti viśeṣaṇānupapatteḥ. na hi sarvakarmasannyāsena mṛtasya taddehe āsanaṃ sambhavati. akurvataḥ akārayataśca dehe sannyasya iti sambandhaḥ, na dehe āste iti cet – na, sarvatra ātmanaḥ avi– kriyatvāvadhāraṇāt, āsanakriyāyāḥ ca adhikaraṇāpekṣatvāt, tadanapekṣatvāt ca sannyāsasya. sampūrvastu nyāsaśabdaḥ atra tyāgārthaḥ, na nikṣepārthaḥ. tasmāt gītāśāstre ātmajñānavataḥ sannyāsa eva adhikāraḥ, na karmaṇi iti tatra tatra upariṣṭāt ātmajñāna prakaraṇe darśayiṣyāmaḥ.",
           ]),
        _v([
            "vāsāṃsi jīrṇāni yathā vihāya navāni gṛhṇāti naro'parāṇi |",
            "tathā śarīrāṇi vihāya jīrṇānyanyāni saṃyāti navāni dehī",
        ], "|| 22 ||",
           "As a man casts off worn-out garments and puts on others that are new, so the embodied one casts off worn-out bodies and enters others that are new.",
           bhashya=[
               {"text": "prakṛtaṃ tu vakṣyāmaḥ tatra ātmanaḥ avināśitvaṃ pratijñātam tat kimiva iti? ucyate –", "intro": True},
               "vāsāṃsi iti. vāsāṃsi vastrāṇi jīrṇāni durbalatāṃ gatāni yathā loke vihāya parityajya navāni abhinavāni gṛhṇāti upādatte naraḥ puruṣaḥ aparāṇi anyāni, tathā tadvat eva śarīrāṇi vihāya jīrṇāni anyāni saṃyāti saṅgacchati navāni dehī ātmā puruṣavat avikriyaḥ eva ityarthaḥ.",
           ]),
        _v([
            "nainaṃ chindanti śastrāṇi nainaṃ dahati pāvakaḥ |",
            "na cainaṃ kledayantyāpaḥ na śoṣayati mārutaḥ",
        ], "|| 23 ||",
           "Weapons do not cut it, fire does not burn it, water does not wet it, and wind does not dry it.",
           bhashya=[
               {"text": "kasmāt avikriya eveti? āha –", "intro": True},
               "nainaṃ chindanti iti. enaṃ prakṛtaṃ dehinaṃ na chindanti śastrāṇi, niravayavatvāt na avayavavibhāgaṃ kurvanti. śastrāṇi asyādīni.tathā na enaṃ dahati pāvakaḥ, agniḥ api na bhasmīkaroti. tathā – na ca enaṃ kledayanti āpaḥ. apāṃ hi sāvayavasya vastunaḥ ārdrībhāvakaraṇena avayavaviśleṣāpādane sāmarthyam. tat na niravayave ātmani sambhavati. tathā snehavat dravyaṃ snehaśoṣaṇena nāśayati vāyuḥ. enaṃ tu ātmānaṃ na śoṣayati mārutaḥ api. yataḥ evaṃ tasmāt –",
           ]),
        _v([
            "acchedyo'yamadāhyo'yamakledyo'śoṣya eva ca |",
            "nityaḥ sarvagataḥ sthāṇuracalo'yaṃ sanātanaḥ",
        ], "|| 24 ||",
           "It cannot be cut, burnt, wetted or dried. It is eternal, all-pervading, stable, unmoving and everlasting.",
           bhashya=[
               "acchedyo'yamiti – yasmāt anyonya nāśahetūni bhūtāni enam ātmānaṃ nāśayituṃ na utsahante tasmāt, nityaḥ nityatvāt sarvagataḥ, sarvagatatvāt sthāṇuḥ, sthāṇuḥ iva sthiraḥ, ityetat. sthiratvāt acalaḥ ayam ātmā, ataḥ sanātanaḥ cirantanaḥ, na kāraṇāt kutaścit niṣpannaḥ abhinavaḥ ityarthaḥ.",
               "na eteṣāṃ ślokānāṃ paunaruktyaṃ codanīyam – yata ekenaiva ślokena ātmanaḥ nityatvam avikriyatvaṃ ca uktam – “na jāyate mriyate vā” ityādinā, tatra yadeva ātma viṣayaṃ kiñcit ucyate tat etasmāt ślokārthāt na atiricyate. kiñcit śabdataḥ punaruktaṃ, kiñcit arthataḥ iti. durbodhatvāt ātmavastunaḥ punaḥpunaḥ prasaṅgam āpādya śabdāntareṇa tadeva vastu nirūpayati bhagavān vāsudevaḥ kathaṃ nu nāma avyaktaṃ saṃsāriṇām buddhigocaratām āpannaṃ sat saṃsāra nivṛttaye syāditi. kiñca –",
           ]),
        _v([
            "avyakto'yamacintyo'yamavikāryo'yamucyate |",
            "tasmādevaṃ viditvainaṃ nānuśocitumarhasi",
        ], "|| 25 ||",
           "It is called unmanifest, unthinkable and unchanging. Knowing it to be such, you should not grieve.",
           bhashya=[
               "avyakto'yamiti – avyaktaḥ sarvakaraṇāviṣayatvāt na vyajyate iti avyaktaḥ ayam ātmā. ata eva acintyaḥ ayam, yat hi indriyagocaraḥ vastu tat cintāviṣayatvam āpadyate. ayaṃ tu ātmā anindriyagocaratvāt acintyaḥ avikāryaḥ ayam. yathā kṣīraṃ dadhyātañcanādinā vikāri na tathā ayam ātmā. niravayavatvāt ca avikriyaḥ. na hi niravayavaṃ kiñcit vikriyātmakaṃ dṛṣṭam. avikriyatvāt avikāryaḥ ayam ātmā ucyate. tasmāt evaṃ yathokta prakāreṇa enam ātmānaṃ viditvā tvaṃ na anuśocitum arhasi – “hantā aham eṣām”, “mayā ete hanyante” iti.",
           ]),
        _v([
            "atha cainaṃ nityajātaṃ nityaṃ vā manyase mṛtam |",
            "tathāpi tvaṃ mahābāho naivaṃ śocitumarhasi",
        ], "|| 26 ||",
           "And even if you think of it as constantly born and constantly dying, even then, mighty-armed one, you should not grieve.",
           bhashya=[
               {"text": "ātmanaḥ anityatvaṃ abhyupagamya idaṃ ucyate –", "intro": True},
               "atha cainamiti – “atha ca iti abhyupagamārthaḥ. enaṃ prakṛtam ātmānaṃ, nityajātaṃ, loka prasiddhyā pratyanekaśarīrotpattiṃ jātaḥ jātaḥ iti vā manyase, tathā pratitattadvināśaṃ nityaṃ vā manyase mṛtaṃ, mṛtaḥ mṛtaḥ iti, tathāpi tathā abhāve api ātmani tvaṃ mahābāho na evaṃ śocitum arhasi. janmavataḥ nāśaḥ nāśavataḥ janma ca ityetau avaśyambhāvinau iti. yasmāt –",
           ]),
        _v([
            "jātasya hi dhruvo mṛtyuḥ dhruvaṃ janma mṛtasya ca |",
            "tasmādaparihārye'rthe na tvaṃ śocitumarhasi",
        ], "|| 27 ||",
           "For death is certain for the born, and birth is certain for the dead. Therefore you should not grieve over what cannot be avoided.",
           bhashya=[
               "jātasya iti. jātasya hi labdhajanmanaḥ, dhruvaḥ avyabhicārī, mṛtyuḥ maraṇam dhruvaṃ janma mṛtasya ca. tasmāt aparihāryaḥ ayaṃ janmamaraṇalakṣaṇaḥ arthaḥ, yasmāt tasmāt aparihārye arthe na tvaṃ śocitum arhasi. (janmavataḥ nāśaḥ, nāśavataḥ janma iti ca svābhāvikaḥ cet aparihāryārthaḥ tasmin aparihārye arthe na tvaṃ śocitum arhasi).",
           ]),
        _v([
            "avyaktādīni bhūtāni vyaktamadhyāni bhārata |",
            "avyaktanidhanānyeva tatra kā paridevanā",
        ], "|| 28 ||",
           "Beings are unmanifest in their beginning, manifest in their middle, and unmanifest again in their end, O Bhārata. What is there to lament in this?",
           bhashya=[
               {"text": "kāryakaraṇasaṅghātātmakāni api bhūtāni uddiśya śokaḥ na yuktaḥ kartuṃ, yataḥ –", "intro": True},
               "avyaktādīniti – avyaktādīni – avyaktam adarśanam, anupalabdhiḥ ādiḥ yeṣāṃ bhūtānāṃ putramitrādi kāryakāraṇasaṅghātātmakānāṃ tāni avyaktādīni bhūtāni prāk utpatteḥ, utpannāni ca prāk maraṇāt vyaktamadhyāni. avyaktanidhanānyeva – punaḥ avyaktam adarśanaṃ nidhanaṃ maraṇaṃ yeṣāṃ tāni avyaktanidhanāni. maraṇāt ūrdhvam avyaktatāmeva pratipadyante ityarthaḥ tathā coktam. “adarśanādāpatitaḥ punaścādarśanaṃ gataḥ, nāsau tava na tasya tvaṃ vṛthā kā paridevanā” (ma.bhā.strī.pa.2.13) iti tatra kā paridevanā, ko vā pralāpaḥ adṛṣṭadṛṣṭapraṇaṣṭabhrāntibhūteṣu bhūteṣu ityarthaḥ",
           ]),
        _v([
            "āścaryavatpaśyati kaścidenamāścaryavadvadati tathaiva cānyaḥ |",
            "āścaryavaccainamanyaḥ śṛṇoti śrutvāpyenaṃ veda na caiva kaścit",
        ], "|| 29 ||",
           "One sees it as a wonder; another speaks of it as a wonder; another hears of it as a wonder; yet even having heard, no one truly knows it.",
           bhashya=[
               {"text": "durvijñeyaḥ ayaṃ prakṛtaḥ ātmā, kiṃ tvāṃ eva ekaṃ upālabhe sādhāraṇe bhrāntinimitte? kathaṃ durvijñeyaḥ ayaṃ ātmā iti? ataḥ āha–", "intro": True},
               "āścaryavat iti. āścaryavat āścaryaṃ adṛṣṭapūrvaṃ adbhutaṃ akasmāt dṛśyamānaṃ tena tulyaṃ āścaryavat āścaryamiva enaṃ ātmānaṃ paśyati kaścit. āścaryavat enaṃ vadati tathaiva ca anyaḥ, āścaryavat ca enaṃ anyaḥ śruṇoti. śrutvā dṛṣṭvā uktvā api enaṃ ātmānaṃ veda na caiva kaścit.",
               "athavā – yaḥ ayaṃ ātmānaṃ paśyati sa āścaryatulyaḥ yaḥ vadati yaḥ ca śruṇoti, saḥ anekasahasreṣu kaścideva bhavati. ataḥ durbodhaḥ ātmā ityabhiprāyaḥ",
           ]),
        _v([
            "dehī nityamavadhyo'yaṃ dehe sarvasya bhārata |",
            "tasmātsarvāṇi bhūtāni na tvaṃ śocitumarhasi",
        ], "|| 30 ||",
           "This embodied one within the body of every being is ever beyond harm, O Bhārata. Therefore you should not grieve for any creature.",
           bhashya=[
               {"text": "atha idānīṃ prakaraṇārthaṃ upasaṃharati –", "intro": True},
               "dehī iti. dehī śarīrī nityaṃ sarvadā sarvāvasthāsu avadhyaḥ niravayavatvāt nityatvāt ca tatra avadhyo'yaṃ dehe śarīre sarvasya sarvagatatvāt sthāvarādiṣu sthito'pi. sarvasya prāṇijātasya dehe vadhyamāne'pi ayaṃ dehī na vadhyaḥ yasmāt tasmāt bhīṣmādīni sarvāṇi bhūtāni uddiśya na tvaṃ śocituṃ arhasi.",
           ]),
        _v([
            "svadharmamapi cāvekṣya na vikampitumarhasi |",
            "dharmyāddhi yuddhācchreyo'nyat kṣatriyasya na vidyate",
        ], "|| 31 ||",
           "Considering also your own dharma, you should not waver; for to a kṣatriya there is nothing better than a righteous battle.",
           bhashya=[
               {"text": "iha (2.30) paramārthatattvāpekṣāyāṃ śoko vā moho vā na sambhavati ityuktam. na kevalaṃ paramārthatattvāpekṣāyām eva kintu –", "intro": True},
               "svadharma iti. svadharmaṃ api svaḥ dharmaḥ kṣatriyasya dharmaḥ yuddhaṃ tamapi avekṣya tvaṃ na vikampituṃ pracalituṃ arhasi dharmyāt kṣatriyasya svābhāvikāt dharmāt ātmasvābhāvyāt ityabhiprāyaḥ. tacca yuddhaṃ pṛthivījayadvāreṇa dharmārthaṃ prajārakṣaṇārthaṃ ca paramaṃ dharmyam. dharmāt anapetaṃ dharmyam. tasmāt dharmyāt yuddhāt śreyaḥ anyat kṣatriyasya na vidyate hi yasmāt.",
           ]),
        _v([
            "yadṛcchayā copapannaṃ svargadvāramapāvṛtam |",
            "sukhinaḥ kṣatriyāḥ pārtha labhante yuddhamīdṛśam",
        ], "|| 32 ||",
           "Happy are the kṣatriyas, Pārtha, who meet such a battle, come of itself like an open door to heaven.",
           bhashya=[
               {"text": "kutaśca tat yuddhaṃ kartavyaṃ iti? ucyate –", "intro": True},
               "yadṛcchayā iti. yadṛcchayā ca aprārthitayā upapannaṃ āgataṃ svargadvāraṃ apāvṛtaṃ udghāṭitaṃ ye etat īdṛśaṃ yuddhaṃ labhante kṣatriyāḥ he pārtha! kiṃ na sukhinaḥ te?",
           ]),
        _v([
            "atha cettvamimaṃ dharmyaṃ saṅgrāmaṃ na kariṣyasi |",
            "tataḥ svadharmaṃ kīrtiṃ ca hitvā pāpamavāpsyasi",
        ], "|| 33 ||",
           "But if you will not fight this righteous battle, then, abandoning your own dharma and your honour, you will incur sin.",
           bhashya=[
               {"text": "evaṃ kartavyatā prāptam api –", "intro": True},
               "atha iti. ata cet tvaṃ imaṃ dharmyaṃ dharmādanapetaṃ vihitaṃ saṅgrāmaṃ yuddhaṃ na kariṣyasi cet, tataḥ tadakāraṇāt svadharmaṃ kīrtiṃ ca mahādevādi samāgamanimittāṃ hitvā kevalaṃ pāpaṃ avāpsyasi.",
           ]),
        _v([
            "akīrtiṃ cāpi bhūtāni kathayiṣyanti te'vyayām |",
            "sambhāvitasya cākīrtirmaraṇādatiricyate",
        ], "|| 34 ||",
           "People will speak of your unending disgrace; and for one who has been honoured, disgrace is worse than death.",
           bhashya=[
               {"text": "na kevalaṃ svadharmakīrtiparityāgaḥ –", "intro": True},
               "akīrtiṃ iti. akīrtiṃ ca api bhūtāni kathayiṣyanti te tava avyayāṃ dīrghakālām. dharmātmā śūraḥ ityevamādibhiḥ guṇaiḥ sambhāvitasya ca akīrtiḥ maraṇāt atiricyate, sambhāvitasya ca akīrteḥ varaṃ maraṇaṃ ityarthaḥ kiñca –",
           ]),
        _v([
            "bhayādraṇāduparataṃ maṃsyante tvāṃ mahārathāḥ |",
            "yeṣāṃ ca tvaṃ bahumato bhūtvā yāsyasi lāghavam",
        ], "|| 35 ||",
           "The great chariot-warriors will think you withdrew from the battle out of fear; and you, once highly esteemed by them, will be held light.",
           bhashya=[
               "bhayāt iti. bhayāt karṇādibhyaḥ raṇāt yuddhāt uparataṃ nivṛttaṃ maṃsyante cintayiṣyanti na kṛpayā iti tvāṃ mahārathāḥ duryodhanaprabhṛtayaḥ(ke maṃsyante? iti āha) yeṣāṃ ca tvaṃ duryodhanādīnāṃ bahumataḥ bahubhiḥ guṇaiḥ yuktaḥ ityevaṃ mataḥ bahumataḥ bhūtvā punaḥ tvaṃ yāsyasi lāghavaṃ laghubhāvam. kiñca.",
           ]),
        _v([
            "avācyavādāṃśca bahūnvadiṣyanti tavāhitāḥ |",
            "nindantastava sāmarthyaṃ tato duḥkhataraṃ nu kim",
        ], "|| 36 ||",
           "Your enemies will say many unspeakable things, deriding your strength. What could be more painful than that?",
           bhashya=[
               "avācyavādān iti. avācyavādān avaktavyān vādān ca bahūn aneka prakārān vadiṣyanti tava ahitāḥ śatravaḥ nindantaḥ kutsayantaḥ tava tvadīyaṃ sāmarthyam nivātakavacādi yuddhanimittam. tataḥ tasmāt nindāprāpteḥ duḥkhāt duḥkhataraṃ nu kiṃ? tataḥ kaṣṭataraṃ duḥkhaṃ nāsti ityarthaḥ.",
           ]),
        _v([
            "hato vā prāpsyasi svargaṃ jitvā vā bhokṣyase mahīm |",
            "tasmāduttiṣṭha kaunteya yuddhāya kṛtaniścayaḥ",
        ], "|| 37 ||",
           "Slain, you will gain heaven; victorious, you will enjoy the earth. So rise, son of Kuntī, resolved to fight.",
           bhashya=[
               {"text": "yuddhe punaḥ kriyamāṇe karṇādibhiḥ –", "intro": True},
               "hato vā iti. hataḥ vā prāpsyasi svargaṃ, hataḥ san svargaṃ prāpsyasi. jitvā vā karṇādīn śūrān bhokṣyase mahīm. ubhayathāpi tava lābhaḥ eva ityabhiprāyaḥ. yataḥ evaṃ tasmāt uttiṣṭha kaunteya! yuddhāya kṛtaniścayaḥ. “jeṣyāmi śatrūn, mariṣyāmi vā” iti niścayaṃ kṛtvā ityarthaḥ.",
           ]),
        _v([
            "sukhaduḥkhe same kṛtvā lābhālābhau jayājayau |",
            "tato yuddhāya yujyasva naivaṃ pāpamavāpsyasi",
        ], "|| 38 ||",
           "Treating alike pleasure and pain, gain and loss, victory and defeat, prepare for battle; so you will incur no sin.",
           bhashya=[
               {"text": "tatra yuddhaṃ svadharmaḥ ityevaṃ yuddhyamānasya upadeśam imaṃ śṛṇu –", "intro": True},
               "sukhaduḥkhe iti. sukhaduḥkhe same tulye kṛtvā, rāgadveṣau (api) akṛtvā ityetat. tathā lābhālābhau jayājayau ca samau kṛtvā tataḥ yuddhāya yujyasva ghaṭasva. na evaṃ yuddhaṃ kurvan pāpaṃ avāpsyasi (iti) eṣaḥ upadeśaḥ prāsaṅgikaḥ.",
           ]),
        _v([
            "eṣā te'bhihitā sāṅkhye buddhiryoge tvimāṃ śṛṇu |",
            "buddhyā yukto yayā pārtha karmabandhaṃ prahāsyasi",
        ], "|| 39 ||",
           "This understanding has been set out for you according to Sāṅkhya; now hear it according to Yoga. Endowed with this understanding, Pārtha, you will cast off the bondage of action.",
           bhashya=[
               {"text": "śokamohāpanaye (nayanāya) laukikaḥ nyāyaḥ “svadharmamapi cāvekṣya” ityādyaiḥ ślokaiḥ uktaḥ, na tu tātparyeṇa. paramārthadarśanaṃ tu iha prakṛtam. tacca uktaṃ upasaṃhriyate – eṣā te abhihitā iti śāstraviṣayavibhāga pradarśanāya. iha hi pradarśite punaḥ śāstraviṣayavibhāge upariṣṭāt “jñānayogena sāṅkhyānāṃ karmayogena yoginām” (3.3) iti. niṣṭhādvayaviṣayaṃ śāstraṃ sukhaṃ pravartiṣyate, śrotāraśca viṣayavibhāgena sukhaṃ grahiṣyanti iti – ataḥ āha –", "intro": True},
               "eṣā te iti. eṣā te tubhyaṃ abhihitā uktā sāṅkhye paramārthavastu vivekaviṣaye buddhiḥ jñānaṃ sākṣāt śokamohādisaṃsārahetudoṣanivṛtti kāraṇam, yoge tu tatprāptyupāye niḥsaṅgatayā dvandvaprahāṇapūrvakam īśvarārādhanārthe karmayoge karmānuṣṭhāne samādhiyoge ca imāṃ anantaram eva ucyamānāṃ buddhiṃ śṛṇu. tāṃ ca buddhiṃ stauti prarocanārtham. buddhyā yayā yogaviṣayayā yuktaḥ he pārtha! karmabandhaṃ karma eva dharmādharmākhyaḥ bandhaḥ karmabandhaḥ taṃ prahāsyasi īśvaraprasādanimittajñānaprāptyā eva ityabhiprāyaḥ. kiñca anyat –",
           ]),
        _v([
            "nehābhikramanāśo'sti pratyavāyo na vidyate |",
            "svalpamapyasya dharmasya trāyate mahato bhayāt",
        ], "|| 40 ||",
           "Here no effort is lost and no reverse is incurred. Even a little of this dharma protects one from great fear.",
           bhashya=[
               "neha iti. na iha mokṣamārge karmayoge abhikramanāśaḥ abhikramaṇaṃ abhikramaḥ prārambhaḥ tasya nāśaḥ na asti yathā kṛṣyādeḥ. yogaviṣaye prārambhasya na anaikāntikaphalatvaṃ ityarthaḥ. kiñca – na api cikitsāvat pratyavāyaḥ vidyate. kintu svalpam api asya dharmasya yogadharmasya anuṣṭhitaṃ trāyate rakṣati mahataḥ bhayāt saṃsārabhayāt janmamaraṇādilakṣaṇāt.",
           ]),
        _v([
            "vyavasāyātmikā buddhirekeha kurunandana |",
            "bahuśākhā hyanantāśca buddhayo'vyavasāyinām",
        ], "|| 41 ||",
           "Here, O joy of the Kurus, the resolute understanding is single; the thoughts of the irresolute are many-branched and endless.",
           bhashya=[
               {"text": "yā iyaṃ sāṅkhye buddhiḥ uktā yoge ca vakṣyamāṇalakṣaṇā sā –", "intro": True},
               "vyavasāyeti :– vyavasāyātmikā niścayasvabhāvā, ekaiva buddhiḥ itara viparītabuddhiḥ śākhābhedasya bādhikā samyak pramāṇajanitatvāt, iha śreyomārge, he kurunandana. yāḥ punaḥ itarāḥ buddhayaḥ, yāsāṃ śākhābhedapracāravaśāt anantaḥ apāraḥ anuparataḥ saṃsāraḥ nityapratataḥ vistīrṇaḥ bhavati, pramāṇajanita vivekabuddhinimittavaśācca uparatāsu anantabhedabuddhiṣu saṃsāraḥ api uparamate, tāḥ buddhayaḥ bahuśākhāḥ bahvyaḥ śākhāḥ yāsāṃ tāḥ bahuśākhāḥ bahubhedāḥ ityetat. pratiśākhābhedena ca anantāḥ buddhayaḥ keṣām? avyavasāyinām, pramāṇajanitavivekabuddhirahitānām ityarthaḥ.",
           ]),
        _v([
            "yāmimāṃ puṣpitāṃ vācaṃ pravadantyavipaścitaḥ |",
            "vedavādaratāḥ pārtha nānyadastīti vādinaḥ",
        ], "|| 42 ||",
           "The undiscerning, who delight in the words of the Veda, Pārtha, and declare that there is nothing else, speak flowery words —",
           bhashya=[
               {"text": "yeṣāṃ vyavasāyātmikā buddhiḥ nāsti te –", "intro": True},
               "yāmiti ḥ– yāmimāṃ vakṣyamāṇāṃ, puṣpitāṃ puṣpitavṛkṣa iva śobhamānāṃ śrūyamāṇa ramaṇīyāṃ, vācaṃ vākyalakṣaṇāṃ pravadanti, ke? avipaścitaḥ alpamedhasaḥ avivekinaḥ ityarthaḥ, vedavādaratāḥ bahvarthavādaphalasādhanaprakāśakeṣu vedavākyeṣu ratāḥ he! pārtha! na anyat svargapaśvādiphalasādhanebhyaḥ karmabhyaḥ asti ityevaṃ vādinaḥ vadanaśīlāḥ",
           ]),
        _v([
            "kāmātmānaḥ svargaparāḥ janmakarmaphalapradām |",
            "kriyāviśeṣabahulāṃ bhogaiśvaryagatiṃ prati",
        ], "|| 43 ||",
           "full of desire, intent on heaven, offering rebirth as the fruit of action, abounding in special rites aimed at enjoyment and power.",
           bhashya=[
               "kāmātmānaḥ iti kāmātmānaḥ kāmasvabhāvāḥ, kāmaparāḥ ityarthaḥ svargaparāḥ, svargaḥparaḥ puruṣārthaḥ eṣāṃ te svargaparāḥ svargapradhānāḥ janmakarmaphalapradāṃ, karmaṇaḥ phalaṃ karmaphalaṃ, janma eva karmaṇaḥ phalaṃ janma karma phalaṃ tat pradadāti iti janmakarmaphalapradā, tāṃ vācam – pravadanti iti anuṣajyate. kriyāviśeṣa bahulāṃ, kriyāṇāṃ viśeṣāḥ kriyāviśeṣāḥ, te bahulā yasyāṃ vāci tāṃ. svargapaśuputrādyarthāḥ yayā vācā bahulyena prakāśyante. bhogaiśvaryagatiṃ prati, bhogaśca aiśvaryaṃ ca bhogaiśvarye, tayoḥ gatiḥ prāptiḥ bhogaiśvarya– gatiḥ, tāṃ prati sādhanabhūtāḥ ye kriyāviśeṣāḥ, tadbahulāṃ tāṃ vācaṃ pravadantaḥ mūḍhāḥ saṃsāre parivartante ityabhiprāyaḥ teṣāṃ ca –",
           ]),
        _v([
            "bhogaiśvaryaprasaktānāṃ tayā'pahṛtacetasām |",
            "vyavasāyātmikā buddhiḥ samādhau na vidhīyate",
        ], "|| 44 ||",
           "For those attached to enjoyment and power, whose minds are carried away by that speech, no resolute understanding is established in samādhi.",
           bhashya=[
               "bhogeti ḥ– bhogaiśvaryaprasaktānāṃ – bhogaḥ kartavyam aiśvaryaṃ ca iti bhogaiśvaryayoḥ eva praṇayavatāṃ tadātmabhūtānāṃ, tayā kriyāviśeṣabahulayā vācā apahṛtacetasām ācchāditaviveka prajñānāṃ vyavasāyātmikā sāṅkhye yoge vā yā buddhiḥ, samādhau samādhīyate asmin puruṣopabhogāya sarvam iti samādhiḥ antaḥkaraṇam, buddhiḥ, tasmin samādhau, na vidhīyate na bhavatītyarthaḥ.",
           ]),
        _v([
            "traiguṇyaviṣayā vedā nistraiguṇyo bhavārjuna |",
            "nirdvandvo nityasattvastho niryogakṣema ātmavān",
        ], "|| 45 ||",
           "The Vedas deal with the three guṇas. Be free of the three guṇas, Arjuna — free of the pairs of opposites, ever grounded in goodness, free of getting and keeping, possessed of the Self.",
           bhashya=[
               {"text": "ye evaṃ vivekabuddhirahitāḥ teṣāṃ kāmātmanāṃ yat phalaṃ tat āha –", "intro": True},
               "traiguṇya iti. traiguṇyaviṣayāḥ – traiguṇyaṃ saṃsāraḥ viṣayaḥ prakāśayitavyaḥ yeṣāṃ te vedāḥ traiguṇyaviṣayāḥ tvaṃ tu nisraiguṇyaḥ bhava arjuna, niṣkāmaḥ bhava ityarthaḥ nirdvandvaḥ, sukhaduḥkhahetū satpratipakṣau padārthau dvandvaśabdavācyau, tataḥ nirgataḥ nirdvandaḥ bhava. nityasatvasthaḥ sadā satvaguṇāśritaḥ bhava. tathā niryogakṣemaḥ anupāttasya upādānaṃ yogaḥ, upāttasya rakṣaṇaṃ kṣemaḥ. yogakṣemapradhānasya śreyasi pravṛttiḥ duṣkarā iti ataḥ niryogakṣemaḥ bhava. ātmavān apramattaḥ ca bhava. eṣa tava upadeśaḥ svadharmaṃ anutiṣṭhataḥ.",
           ]),
        _v([
            "yāvānartha udapāne sarvataḥ samplutodake |",
            "tāvān sarveṣu vedeṣu brāhmaṇasya vijānataḥ",
        ], "|| 46 ||",
           "As much use as there is in a well when water floods on every side, so much is there in all the Vedas for the brāhmaṇa who knows.",
           bhashya=[
               {"text": "sarveṣu vedokteṣu karmasu yāni uktāni anantāni phalāni tāni na apekṣyante cet, kimarthaṃ tāni īśvarāya iti anuṣṭhīyante iti? ucyate, śṛṇu.", "intro": True},
               "yāvān iti. yathā loke kūpataḍāgādyanekasmin udapāne paricchinnodake yāvān yāvatparimāṇaḥ snānapānādiḥ arthaḥ phalaṃ prayojanaṃ saḥ sarvaḥ arthaḥ sarvataḥ samplutodake tāvān eva sampadyate, tatra antarbhavati ityardhaḥ. evaṃ tāvān tāvatparimāṇaḥ eva sampadyate sarveṣu vedeṣu vedokteṣu karmasu yaḥ arthaḥ yat karmaphalaṃ saḥ arthaḥ brāhmaṇasya sannyāsinaḥ paramārthatattvaṃ vijānataḥ yaḥ arthaḥ yat vijñānaphalaṃ sarvataḥ samplutodakasthānīyaṃ tasmin tāvān eva sampadyate – tatraiva antarbhavatītyarthaḥ. “sarvaṃ tat abhisameti yat kiñca prajāḥ sādhu kurvanti yastadveda yat sa veda” (chāṃ.u.4.1.4) iti śruteḥ. “sarvaṃ karmākhilaṃ” (4.33) iti ca vakṣyati. tasmāt prāk jñānaniṣṭhādhikāra prāpteḥ karmaṇi adhikṛtena kūpataḍāgādyartha sthānīyaṃ api karma kartavyam. tava ca –",
           ]),
        _v([
            "karmaṇyevādhikāraste mā phaleṣu kadācana |",
            "mā karmaphalaheturbhūrmā te saṅgo'stvakarmaṇi",
        ], "|| 47 ||",
           "Your right is to action alone, never to its fruits. Let not the fruit of action be your motive, nor let your attachment be to inaction.",
           bhashya=[
               "karmaṇi iti. karmaṇi eva adhikāraḥ, na jñānaniṣṭhāyāṃ te tava. tatra ca karma kurvataḥ mā phaleṣu adhikāraḥ astu, karmaphalatṛṣṇā mā bhūt kadācana kasyāñcit api avasthāyāṃ ityarthaḥ. yadā karmaphale tṛṣṇā te syāt tadā karmaphalaprāpteḥ hetuḥ syāḥ, evaṃ mā karmaphalaheturbhūḥ. yadā hi karmaphalatṛṣṇāprayuktaḥ karmaṇi pravartate tadā karmaphalasya eva janmanaḥ hetuḥ bhavet. yadi karmaphalaṃ na iṣyate, kiṃ karmaṇā duḥkharūpeṇa? iti mā te tava saṅgaḥ astu akarmaṇi akaraṇe prītiḥ mā bhūt.",
           ]),
        _v([
            "yogasthaḥ kuru karmāṇi saṅgaṃ tyaktvā dhanañjaya |",
            "siddhyasiddhyoḥ samo bhūtvā samatvaṃ yoga ucyate",
        ], "|| 48 ||",
           "Steadfast in yoga, perform actions, Dhanañjaya, abandoning attachment and remaining even in success and failure. This evenness is called yoga.",
           bhashya=[
               {"text": "yadi karmaphalaprayuktena na kartavyaṃ karma, kathaṃ tarhi kartavyaṃ iti? ucyate –", "intro": True},
               "yogasthaḥ iti. yogasthaḥ san kuru karmāṇi kevalaṃ īśvarārthaṃ, tatrāpi “īśvaro me tuṣyatu” iti saṅgaṃ tyaktvā dhanañjaya. phalatṛṣṇāśūnyena kriyamāṇe karmaṇi satvaśuddhijā, jñānaprāptilakṣaṇāsiddhiḥ, tadviparyayajā asiddhiḥ, tayoḥ siddhyasiddhyoḥ api samaḥ tulyaḥ bhūtvā kuru karmāṇi. ko'sau yogaḥ yatrasthaḥ kuru iti uktam? idaṃ eva tat – siddhyasiddhyoḥ samatvaṃ yogaḥ ucyate –",
           ]),
        _v([
            "dūreṇa hyavaraṃ karma buddhiyogāddhanañjaya |",
            "buddhau śaraṇamanviccha kṛpaṇāḥ phalahetavaḥ",
        ], "|| 49 ||",
           "Action is far inferior to the yoga of understanding, Dhanañjaya. Seek refuge in understanding; wretched are those whose motive is the fruit.",
           bhashya=[
               {"text": "yat punaḥ samatvabuddhiyuktaṃ īśvarārādhanārthaṃ karma (uktaṃ) etasmāt karmaṇaḥ –", "intro": True},
               "dūreṇa iti. dūreṇa atiprakarṣeṇa hi avaraṃ adhamaṃ nikṛṣṭaṃ karma phalārthinā kriyamāṇaṃ buddhiyogāt samatvabuddhiyuktāt karmaṇaḥ, janma maraṇādihetutvāt. he dhanañjaya, yataḥ evaṃ tataḥ yogaviṣayāyāṃ buddhau tatparipākajāyāṃ vā sāṅkhyabuddhau śaraṇaṃ āśrayaṃ abhayaprāptikāraṇaṃ anviccha prārthayasva. paramārthajñānaśaraṇaḥ bhava ityarthaḥ yataḥ avaraṃ karma kurvāṇāḥ kṛpaṇāḥ dīnāḥ phalahetavaḥ phalatṛṣṇāprayuktāḥ santaḥ “yo vā etadakṣaraṃ gārgyaviditvā'smāllokātpraiti sa kṛpaṇaḥ” (bṛ.3.8.10) iti śruteḥ.",
           ]),
        _v([
            "buddhiyukto jahātīha ubhe sukṛtaduṣkṛte |",
            "tasmādyogāya yujyasva yogaḥ karmasu kauśalam",
        ], "|| 50 ||",
           "One endowed with understanding casts off here both good and evil deeds. Therefore devote yourself to yoga; yoga is skill in action.",
           bhashya=[
               {"text": "samatvabuddhiyuktaḥ san svadharmaṃ anutiṣṭhan yat phalaṃ prāpnoti tat śṛṇu –", "intro": True},
               "buddhi iti. buddhiyuktaḥ samatvaviṣayayā buddhyā yuktaḥ buddhiyuktaḥ saḥ jahāti parityajati iha asmin loke ubhe sukṛtaduṣkṛte puṇyapāpe satvaśuddhijñānaprāptidvāreṇa yataḥ, tasmāt samatvabuddhiyogāya yujyasva ghaṭasva. yogaḥ hi karmasu kauśalaṃ svadharmākhyeṣu karmasu vartamānasya yā siddhyasiddhyoḥ samatvabuddhiḥ īśvarārpitacetastayā tat kauśalaṃ kuśala bhāvaḥ. taddhi kauśalaṃ yat bandhasvabhāvāni api karmaṇi samatvabuddhyā svabhāvāt nivartante. tasmāt samatvabuddhiyuktaḥ bhava tvam. yasmāt.",
           ]),
        _v([
            "karmajaṃ buddhiyuktā hi phalaṃ tyaktvā manīṣiṇaḥ |",
            "janmabandhavinirmuktāḥ padaṃ gacchantyanāmayam",
        ], "|| 51 ||",
           "The wise, endowed with understanding, having given up the fruit born of action and freed from the bondage of birth, go to the state beyond all ill.",
           bhashya=[
               "karmajamiti : karmajaṃ phalaṃ “tyaktvā” iti vyavahitena sambandhaḥ iṣṭāniṣṭadehaprāptiḥ karmajaṃ phalaṃ, karmabhyaḥ jātaṃ, buddhiyuktāḥ samatvabuddhiyuktāḥ, santaḥ hi yasmāt, phalaṃ tyaktvā parityajya manīṣiṇaḥ jñāninaḥ bhūtvā, janmabandhavinirmuktāḥ – janmaiva bandhaḥ janmabandhaḥ tena vinirmuktāḥ, jīvantaḥ eva janmabandhavinirmuktāḥ santaḥ, padaṃ paramaṃ viṣṇoḥ mokṣākhyaṃ, gacchanti, anāmayaṃ sarvopadravarahitamityarthaḥ.",
               "athavā – “buddhiyogāddhanañjaya” ityārabhya paramārthadarśanalakṣaṇaiva sarvataḥ samplutodaka sthānīyā karmayogajasattvaśuddhijanitā buddhiḥ darśitā, sākṣāt sukṛtaduṣkṛta prahāṇādi hetutvaśravaṇāt.",
           ]),
        _v([
            "yadā te mohakalilaṃ buddhirvyatitariṣyati |",
            "tadā gantāsi nirvedaṃ śrotavyasya śrutasya ca",
        ], "|| 52 ||",
           "When your understanding crosses beyond the thicket of delusion, then you will become indifferent to what has been heard and what is yet to be heard.",
           bhashya=[
               {"text": "yogānuṣṭhānajanitasattvaśuddhijā buddhiḥ kadā prāpyate iti. ucyate–", "intro": True},
               "yadeti. yasmin kāle, te tava, mohakalilaṃ mohātmakam avivekarūpaṃ kāluṣyaṃ, yena ātmānātmavivekabodhaṃ kaluṣīkṛtya viṣayaṃ pratyantaḥ karaṇaṃ pravartyate tat, tava buddhiḥ vyatitariṣyati vyatikramiṣyati, atiśuddhabhāvam āpatsyate ityarthaḥ. tadā tasmin kāle, gantāsi, prāpsyasi, nirvedaṃ, vairāgyaṃ, śrotavyasya ca śrutasya ca. tadā śrotavyaṃ śrutaṃ ca niṣphalaṃ pratipadyate (pratibhāti) ityabhiprāyaḥ.",
           ]),
        _v([
            "śrutivipratipannā te yadā sthāsyati niścalā |",
            "samādhāvacalā buddhistadā yogamavāpsyasi",
        ], "|| 53 ||",
           "When your understanding, bewildered by what you have heard, stands unmoving and steady in samādhi, then you will attain yoga.",
           bhashya=[
               {"text": "mohakalilātyayadvāreṇa labdhātmaviveka prajñaḥ kadā karmayogajaṃ phalaṃ paramārthayogam avāpsyāmi iti cet śṛṇu –", "intro": True},
               "śrutivipratipannā iti. śrutivipratipannā aneka sādhyasādhana sambandhaprakāśana śrutibhiḥ śravaṇaiḥ pravṛttinivṛttilakṣaṇaiḥ vipratipannā nānāpratipannā (śruti vipratipannā) vikṣiptā satī te tava buddhiḥ yadā yasmin kāle sthāsyati sthirībhūtā bhaviṣyati niścalā vikṣepacalanavarjitā satī samādhau – samādhīyate cittam asmin iti samādhiḥ ātmā, tasmin ātmani ityetat | (sā api) acalā, tatrāpi vikalpavarjitā ityetat. buddhiḥ antaḥkaraṇam. tadā tasmin kāle yogaṃ avāpsyasi vivekaprajñāṃ samādhiṃ prāpsyasi.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "sthitaprajñasya kā bhāṣā samādhisthasya keśava |",
            "sthitadhīḥ kiṃ prabhāṣeta kimāsīta vrajeta kim",
        ], "|| 54 ||",
           "Arjuna said: What is the description of one of steady wisdom, established in samādhi, O Keśava? How does one of steady mind speak, how does he sit, how does he walk?",
           bhashya=[
               {"text": "praśnabījaṃ pratilabhya arjunaḥ uvāca labdhasamādhiprajñasya lakṣaṇabubhutsayā–", "intro": True},
               "sthitaprajñasyetiḥ sthitā pratiṣṭhitā “aham asmi paraṃ brahma” iti prajñā yasya saḥ sthitaprajñaḥ, tasya kā bhāṣā? kiṃ tasya bhāṣaṇam, vacanaṃ katham asau paraiḥ bhāṣyate ityarthaḥ. samādhisthasya samādhau sthitasya, keśava, sthitadhīḥ sthitaprajñaḥ svayaṃ vā kiṃ prabhāṣeta? kim āsīta, vrajeta kim? āsanaṃ vrajanaṃ vā tasya katham ityarthaḥ. sthitaprajñasya lakṣaṇam anena ślokena pṛcchyate.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "prajahāti yadā kāmān sarvān pārtha manogatān |",
            "ātmanyevātmanā tuṣṭaḥ sthitaprajñastadocyate",
        ], "|| 55 ||",
           "The Blessed Lord said: When a man casts off all the desires that enter the mind, Pārtha, and is content in the Self by the Self, then he is called one of steady wisdom.",
           bhashya=[
               {"text": "yaḥ hi āditaḥ eva sannyasya karmāṇi jñānayoganiṣṭhāyāṃ pravṛttaḥ yaśca karmayogena tayoḥ “prajahāti” ityārabhya adhyāyasamāptiparyantaṃ sthitaprajñalakṣaṇaṃ sādhanaṃ ca upadiśyate, sarvatraiva hi adhyātmaśāstre kṛtārthalakṣaṇāni yāni tānyeva sādhanāni upadiśyante yatnasādhyatvāt. yāni yatnasādhyāni sādhanāni, lakṣaṇāni ca bhavanti tāni.", "intro": True},
               "prajahātīti – prajahāti prakarṣeṇa jahāti parityajati, yadā yasmin kāle, sarvān samastān, kāmān icchābhedān, he pārtha, manogatān manasi praviṣṭān hṛdi praviṣṭān. sarvakāmaparityāge tuṣṭikāraṇābhāvāt śarīradhāraṇanimittaśeṣe ca sati unmattapramattasyeva pravṛttiḥ prāptā ityataḥ ucyate – ātmani eva pratyagātma svarūpe eva, ātmanā svena eva, bāhyalābhanirapekṣaḥ tuṣṭaparamārtha darśanāmṛtarasalābhena anyasmāt alampratyayavān, sthita prajñaḥ, sthitā pratiṣṭhitā ātmānātmavivekajā prajñā yasya saḥ vidvān tadā ucyate. tyakta putra vittalokaiṣaṇaḥ, sannyāsī, ātmārāmaḥ ātmakrīḍaḥ sthitaprajñaḥ ityarthaḥ. kiñca –",
           ]),
        _v([
            "duḥkheṣvanudvignamanāḥ sukheṣu vigataspṛhaḥ |",
            "vītarāgabhayakrodhaḥ sthitadhīrmunirucyate",
        ], "|| 56 ||",
           "He whose mind is not shaken in sorrows, who has no craving for pleasures, from whom passion, fear and anger have gone — he is called a sage of steady mind.",
           bhashya=[
               "duḥkheṣu iti. duḥkheṣu ādhyātmikādiṣu prāpteṣu anudvignaṃ ca prakṣubhitaṃ duḥkhaprāptau manaḥ yasya so'yaṃ anudvignamanāḥ. tathā sukheṣu prāpteṣu vigatā spṛhā tṛṣṇā yasya, na agniḥ iva indhanādyādhāne, sukhāni anuvivardhate sa vigataspṛhaḥ. vītarāgabhayakrodhaḥ rāgaśca bhayaṃ ca krodhaśca vītāḥ vigatāḥ yasmāt saḥ vītarāgabhayakrodhaḥ sthitadhīḥ sthitaprajñaḥ muniḥ sannyāsī tadā ucyate. kiñca –",
           ]),
        _v([
            "yaḥ sarvatrānabhisnehastattatprāpya śubhāśubham |",
            "nābhinandati na dveṣṭi tasya prajñā pratiṣṭhitā",
        ], "|| 57 ||",
           "He who is without attachment anywhere, who neither rejoices nor hates on meeting good or evil — his wisdom is firmly established.",
           bhashya=[
               "yaḥ sarvatreti – yaḥ muniḥ, sarvatra dehajīvitādiṣvapi anabhisnehaḥ abhisnehavarjitaḥ, tat tat prāpya śubhāśubhaṃ tat tat śubham aśubhaṃ vā labdhvā na abhinandati, na dveṣṭi, śubhaṃ prāpya na tuṣyati na hṛṣyati aśubhaṃ ca prāpya na dveṣṭi ityarthaḥ. tasya evaṃ harṣaviṣādavarjitasya vivekaprajñā pratiṣṭhitā bhavati. kiñca –",
           ]),
        _v([
            "yadā saṃharate cāyaṃ kūrmo'ṅgānīva sarvaśaḥ |",
            "indriyāṇīndriyārthebhyastasya prajñā pratiṣṭhitā",
        ], "|| 58 ||",
           "When he draws back his senses from their objects on every side, as a tortoise draws in its limbs, his wisdom is firmly established.",
           bhashya=[
               "yadā saṃharate iti – yadā saṃharate samyak upasaṃharate, ca, ayaṃ jñānaniṣṭhāyāṃ pravṛttaḥ yatiḥ kūrmaḥ bhayāt svāni ajñāni upasaṃharati sarvaśaḥ sarvataḥ evaṃ jñānaniṣṭhaḥ, indriyāṇi, indriyārthebhyaḥ sarvaviṣayebhyaḥ upasaṃharate, tasya prajñā pratiṣṭhitā iti uktārthaṃ vākyam.",
           ]),
        _v([
            "viṣayā vinivartante nirāhārasya dehinaḥ |",
            "rasavarjaṃ raso'pyasya paraṃ dṛṣṭvā nivartate",
        ], "|| 59 ||",
           "Objects fall away from the embodied one who abstains from them, but the taste for them remains; even the taste falls away when the Supreme is seen.",
           bhashya=[
               {"text": "tatra viṣayān anāharataḥ āturasyāpi indriyāṇi nivartante, kūrmāṅgānīva saṃhriyante, na tu tadviṣayaḥ rāgaḥ saḥ kathaṃ saṃhriyate iti. ucyate –", "intro": True},
           ]),
        _v([
            "yatato hyapi kaunteya puruṣasya vipaścitaḥ |",
            "indriyāṇi pramāthīni haranti prasabhaṃ manaḥ",
        ], "|| 60 ||",
           "For the turbulent senses, son of Kuntī, forcibly carry away the mind even of a wise man who is striving.",
           bhashya=[
               {"text": "viṣayā iti – yadyapi – viṣayopalakṣitāni viṣayaśabdavācyāni indriyāṇi, athavā viṣayāḥ eva, nirāhārasya anāhriyamāṇaviṣayasya kaṣṭe tapasi sthitasya mūrkhasya api, vinivartante, dehinaḥ dehavataḥ rasavarjaṃ – rasaḥ rāgaḥ viṣayeṣu yaḥ taṃ varjayitvā rasaśabdo rāge prasiddhaḥ “svarasena pravṛttaḥ” “rasikaḥ”, “rasajñaḥ” ityādi darśanāt. saḥ api rasaḥ rañjanarūpaḥ sūkṣmaḥ asya yateḥ paraṃ paramārthatattvaṃ brahma, dṛṣṭvā upalabhya “ahameva tat” iti vartamānasya nivartate nirbījaṃ viṣayajñānaṃ sampadyate ityarthaḥ. na asati samyagdarśane rasasya ucchedaḥ. tasmāt samyagdarśanātmikāyāḥ prajñāyāḥ sthairyaṃ kartavyam iti abhiprāyaḥ.", "intro": True},
               {"text": "samyagdarśanalakṣaṇaprajñāsthairyaṃ cikīrṣatā ādau indriyāṇi svavaśe sthāpayitavyāni, yasmāt tadanavasthāpane doṣam āha –", "intro": True},
               "yatataḥ iti – yatataḥ prayatnaṃ kurvataḥ hi yasmāt kaunteya, puruṣasya, vipaścitaḥ medhāvinaḥ “apīti” vyavahitena sambandhaḥ, indriyāṇi pramāthīni pramathanaśīlāni viṣayābhimukhaṃ hi puruṣaṃ vikṣobhayanti ākulīkurvanti, ākulīkṛtya ca haranti prasabhaṃ prasahya prakāśameva paśyataḥ vivekavijñānayuktaṃ manaḥ yataḥ tasmāt.",
           ]),
        _v([
            "tāni sarvāṇi saṃyamya yukta āsīta matparaḥ |",
            "vaśe hi yasyendriyāṇi tasya prajñā pratiṣṭhitā",
        ], "|| 61 ||",
           "Restraining them all, let him sit in yoga, intent on me; for he whose senses are under control has wisdom firmly established.",
           bhashya=[
               "tānīti – tāni sarvāṇi saṃyamya saṃyamanaṃ vaśīkaraṇaṃ kṛtvā, yuktaḥ samāhitaḥ san, āsīta. matparaḥ ahaṃ vāsudevaḥ sarvapratyagātmā paraḥ yasya saḥ matparaḥ, “na anyaḥ ahaṃ tasmāt” iti āsīta ityarthaḥ evam āsīnasya yateḥ vaśe hi yasya indriyāṇi vartante abhyāsabalāt tasya prajñā pratiṣṭhitā.",
           ]),
        _v([
            "dhyāyato viṣayān puṃsaḥ saṅgasteṣūpajāyate |",
            "saṅgātsañjāyate kāmaḥ kāmāt krodho'bhijāyate",
        ], "|| 62 ||",
           "When a man dwells on objects, attachment to them is born; from attachment arises desire, and from desire, anger.",
           bhashya=[
               {"text": "atha idānīṃ parābhaviṣyataḥ sarvānarthamūlaṃ idaṃ ucyate –", "intro": True},
               "dhyāyata iti – dhyāyataḥ cintayataḥ, viṣayān śabdādiviṣaya viśeṣān ālocayataḥ, puṃsaḥ puruṣasya, saṅgaḥ āsaktiḥ, prītiḥ, teṣu viṣayeṣu upajāyate utpadyate. saṅgāt prīteḥ sañjāyate samutpadyate, kāmaḥ tṛṣṇā. kāmāt kutaścit pratihatāt, krodhaḥ abhijāyate.",
           ]),
        _v([
            "krodhādbhavati sammohaḥ sammohāt smṛtivibhramaḥ |",
            "smṛtibhraṃśād buddhināśo buddhināśātpraṇaśyati",
        ], "|| 63 ||",
           "From anger comes delusion, from delusion the loss of memory, from the loss of memory the ruin of understanding; and with the ruin of understanding he perishes.",
           bhashya=[
               "krodhāt iti. krodhāt bhavati sammohaḥ avivekaḥ kāryākārya viṣayaḥ. kruddhaḥ hi sammūḍhaḥ san gurum api ākrośati. sammohāt smṛtivibhramaḥ śāstrācāryopadeśāhita saṃskāra janitāyāḥ smṛteḥ syāt vibhramaḥ bhraṃśaḥ smṛtyutpattinimittaprāptau anutpattiḥ. tataḥ smṛtibhraṃśāt buddhināśaḥ buddhināśaḥ buddheḥ nāśaḥ. kāryākāryaviṣaya vivekāyogyatā antaḥkaraṇasya buddheḥ nāśaḥ ucyate. buddhināśāt praṇaśyati. tāvadeva hi puruṣaḥ yāvat antaḥkaraṇaṃ tadīyaṃ kāryākāryaviṣayavivekayogyam. tadayogyatve naṣṭa eva puruṣaḥ bhavati. ataḥ tasya antaḥkaraṇasya buddheḥ nāśāt praṇaśyati. puruṣārthāyogyaḥ bhavati ityarthaḥ.",
           ]),
        _v([
            "rāgadveṣaviyuktaistu viṣayānindriyaiścaran |",
            "ātmavaśyairvidheyātmā prasādamadhigacchati",
        ], "|| 64 ||",
           "But one who moves among objects with senses under control, free of attraction and aversion, governed by the Self, attains serenity.",
           bhashya=[
               {"text": "sarvānarthasya mūlaṃ uktaṃ viṣayābhidhyānam. atha idānīṃ mokṣakāraṇaṃ idaṃ ucyate –", "intro": True},
               "rāgadveṣa iti. rāgadveṣaviyuktaiḥ rāgaśca dveṣaśca rāgadveṣau, tatpurassarāḥ hi indriyāṇāṃ pravṛttiḥ svābhāvikī, tatra ca mumukṣuḥ bhavati saḥ tābhyāṃ viyuktaiḥ śrotrādibhiḥ indriyaiḥ viṣayān avarjanīyān caran upalabhamānaḥ ātmavaśyaiḥ ātmanaḥ vaśyāni vaśīkṛtāni indriyāṇi taiḥ ātmavaśyaiḥ vidheyātmā icchātaḥ ātmā antaḥkaraṇaṃ yasya saḥ ayaṃ prasādaṃ adhigaccati. prasādaḥ prasannatā, svāsthyam.",
           ]),
        _v([
            "prasāde sarvaduḥkhānāṃ hānirasyopajāyate |",
            "prasannacetaso hyāśu buddhiḥ paryavatiṣṭhate",
        ], "|| 65 ||",
           "In serenity all his sorrows come to an end; for the understanding of one whose mind is serene soon becomes firmly established.",
           bhashya=[
               {"text": "prasāde sati kiṃ syāt iti? ucyate –", "intro": True},
               "prasāda iti – prasāde sarvaduḥkhānām ādhyātmikādīnāṃ hāniḥ vināśaḥ asya yateḥ upajāyate. kiṃ ca prasannacetasaḥ svasthāntaḥkaraṇasya hi yasmāt āśu śīghraṃ buddhiḥ paryavatiṣṭhate, ākāśamiva parisamantāt, avatiṣṭhate, ātmasvarūpeṇaiva niścalībhavati ityarthaḥ. evaṃ prasannacetasaḥ avasthitabuddheḥ kṛtakṛtyatā yataḥ tasmāt rāgadveṣaviyuktaiḥ indriyaiḥ śāstrāviruddheṣu avarjanīyeṣu yuktaḥ samācaret ityarthaḥ.",
           ]),
        _v([
            "nāsti buddhirayuktasya na cāyuktasya bhāvanā |",
            "na cābhāvayataḥ śāntiraśāntasya kutaḥ sukham",
        ], "|| 66 ||",
           "For the undisciplined there is no understanding, and no contemplation; for one who does not contemplate there is no peace; and for one without peace, whence happiness?",
           bhashya=[
               {"text": "sā iyaṃ prasannatā stūyate –", "intro": True},
               "nāsti iti. na asti na vidyate na bhavati ityarthaḥ. buddhiḥ ātmasvarūpaviṣayā ayuktasya asamāhitāntaḥkaraṇasya. na ca asti ayuktasya bhāvanā ātmajñānābhiniveśaḥ. tathā na ca asti abhāvayataḥ ātmajñānābhiniveśam akurvataḥ śāntiḥ upaśamaḥ aśāntasya kutaḥ sukham. indriyāṇāṃ hi viṣayasevātṛṣṇātaḥ nivṛttiḥ yā tat sukhaṃ, na viṣayaviṣayā tṛṣṇā. duḥkham eva hi sā. na tṛṣṇāyāṃ satyāṃ sukhasya gandhamātram api utpa(papa)dyate ityarthaḥ.",
           ]),
        _v([
            "indriyāṇāṃ hi caratāṃ yanmano'nuvidhīyate |",
            "tadasya harati prajñāṃ vāyurnāvamivāmbhasi",
        ], "|| 67 ||",
           "For when the mind follows the roving senses, it carries away his wisdom, as the wind carries away a ship upon the waters.",
           bhashya=[
               {"text": "ayuktasya kasmāt buddhiḥ nāsti iti? ucyate –", "intro": True},
               "indriyāṇāmiti – indriyāṇāṃ, hi yasmāt, caratāṃ svasvaviṣayeṣu pravartamānānāṃ yat manaḥ, anuvidhīyate anupravartate, tat indriyaviṣayavikalpanena pravṛttaṃ manaḥ, asya yateḥ harati, prajñām ātmānātmavivekajāṃ nāśayati. katham? vāyuḥ nāvam iva, ambhasi udake. jigamiṣatāṃ sāṃyātrikāṇāṃ mārgāt uddhṛtya unmārge yathā vāyuḥ nāvaṃ pravartayati, evam ātmaviṣayāṃ prajñāṃ hṛtvā manaḥ anyaviṣayāṃ karoti.",
           ]),
        _v([
            "tasmādyasya mahābāho nigṛhītāni sarvaśaḥ |",
            "indriyāṇīndriyārthebhyastasya prajñā pratiṣṭhitā",
        ], "|| 68 ||",
           "Therefore, mighty-armed one, he whose senses are withdrawn from their objects on every side — his wisdom is firmly established.",
           bhashya=[
               {"text": "“yatato hyapi” (2.60) ityupanyastasya arthasya anekadhā upapattiṃ uktvā taṃ ca arthaṃ upapādya upasaṃharati –", "intro": True},
               "tasmāt iti || indriyāṇāṃ pravṛttau doṣaḥ upapāditaḥ yasmāt tasmāt yasya yateḥ he mahābāho! nigṛhītāni sarvaśaḥ sarvaprakāraiḥ mānasādibhedaiḥ indriyāṇi indriyārthebhyaḥ śabdādibhyaḥ tasya prajñā pratiṣṭhitā.",
           ]),
        _v([
            "yā niśā sarvabhūtānāṃ tasyāṃ jāgarti saṃyamī |",
            "yasyāṃ jāgrati bhūtāni sā niśā paśyato muneḥ",
        ], "|| 69 ||",
           "What is night for all beings, in that the self-controlled one is awake; and where beings are awake, that is night for the sage who sees.",
           bhashya=[
               {"text": "yo'yaṃ laukikaḥ vaidikaśca vyavahāraḥ saḥ utpannavivekajñānasya sthitaprajñasya avidyākāryatvāt avidyānivṛttau nivartate, avidyāyāḥ ca vidyāvirodhāt nivṛttiḥ ityetaṃ arthaṃ sphuṭīkurvan āha –", "intro": True},
               "yā niśā iti || yā niśā rātriḥ sarvapadārthānāṃ avivekakarī tamaḥ svabhāvatvāt sarvabhūtānāṃ sarveṣāṃ bhūtānām. kiṃ tat? paramārthatattvaṃ sthita prajñasya viṣayaḥ. yathā naktañcarāṇāṃ ahaḥ eva sat anyeṣāṃ niśā bhavati, tadvat naktañcarasthānīyānāṃ ajñā(ni)nāṃ sarvabhūtānāṃ niśā iva niśā paramārthatattvaṃ. agocaratvāt atadbuddhīnām. tasyāṃ paramārthatattvalakṣaṇāyāṃ ajñānanidrāyāḥ prabuddhaḥ jāgarti saṃyamī saṃyamavān, jitendriyaḥ yogī ityarthaḥ. yasyāṃ grāhyagrāhaka (bheda) lakṣaṇāyāṃ avidyānidrā(śā)yāṃ prasuptāni eva bhūtāni jāgrati iti ucyante(te), yasyāṃ niśāyāṃ prasuptā iva svapna dṛśaḥ, sā niśā avidyārūpatvāt paramārthatattvaṃ paśyataḥ muneḥ iti.",
               "ataḥ karmāṇi avidyāvasthāyāṃ eva codyante, na vidyāvasthāyām. vidyāyāṃ hi satyāṃ udite savitari śārvaraṃ iva tamaḥ praṇāśaṃ upagacchati avidyā. prāk vidyotpatteḥ avidyā pramāṇabuddhyā gṛhyamāṇā kriyākārakaphalabhedarūpā ca satī sarvakarma– hetutvaṃ pratipadyate. na apramāṇa buddhyā gṛhyamāṇāyāḥ karmahetutvopapattiḥ. “pramāṇa– bhūtena vedena mama coditaṃ kartavyaṃ karma”, iti hi karmaṇi kartā pravartate, na “avidyā mātramidaṃ sarvaṃ niśā iva” iti. yasya tu punaḥ “niśevāvidyāmātramidaṃ sarvaṃ bhedajātam” iti jñānaṃ tasyā''tmajñasya sarvakarmasannyāse evādhikāra, na pravṛttau. tathā ca darśayiṣyati “tadbuddhayastadātmānaḥ”(5.17) ityādinā jñānaniṣṭhāyāṃ eva tasya adhikāram.",
               "tatrāpi pravartakapramāṇābhāve pravṛttyanupapattiḥ iti cet na, svātmaviṣayatvāt ātmavijñānasya. na hi ātmanaḥ svātmani pravartakapramāṇāpekṣā, ātmattvāt eva tadantattvāt ca sarva pramāṇānāṃ pramāṇatvasya. na hi ātma svarūpādhigame sati punaḥ pramāṇaprameyavyavahāraḥ sambhavati.pramātṛttvaṃ hi ātmanaḥ nivartayati antyaṃ pramāṇam. nivartayat eva ca apramāṇībhavati svapnakālapramāṇam iva prabodhe. loke ca vastvadhigame pravṛtti hetuttvādarśanātpramāṇasya. tasmāt na ātmavidaḥ karmaṇi adhikāraḥ iti siddham.",
           ]),
        _v([
            "āpūryamāṇamacalapratiṣṭhaṃ samudramāpaḥ praviśanti yadvat |",
            "tadvatkāmā yaṃ praviśanti sarve sa śāntimāpnoti na kāmakāmī",
        ], "|| 70 ||",
           "As the waters enter the ocean, which is ever being filled yet stays unmoved in its place, so he into whom all desires enter attains peace — not the desirer of desires.",
           bhashya=[
               {"text": "viduṣaḥ tyaktaiṣaṇasya sthitaprajñasya yateḥ eva mokṣaprāptiḥ na tu asannyāsinaḥ kāmakāminaḥ ityetam arthaṃ dṛṣṭāntena pratipādayiṣyan āha –", "intro": True},
               "āpūrya iti. āpūryamāṇaṃ adbhiḥ acalapratiṣṭhaṃ acalatayā pratiṣṭhā avasthitiḥ yasya tam acalapratiṣṭhaṃ samudraṃ āpaḥ sarvato gatāḥ praviśanti svātmasthaṃ avikriyam eva santaṃ yadvat tadvatkāmāḥ viṣayasannidhau api sarvataḥ icchāviśeṣāḥ yaṃ puruṣaṃ (muniṃ), samudram iva āpaḥ, avikurvantaḥ praviśanti sarve ātmani eva pralīyante na svātmavaśaṃ kurvanti saḥ śāntiṃ mokṣaṃ āpnoti, na itaraḥ kāmakāmī kāmyante iti kāmāḥ viṣayāḥ tān kāmayituṃ śīlaṃ yasya sa kāmakāmī, saḥ naiva prāpnoti ityarthaḥ. yasmāt evaṃ tasmāt –",
           ]),
        _v([
            "vihāya kāmānyaḥ sarvān pumāṃścarati niḥspṛhaḥ |",
            "nirmamo nirahaṅkāraḥ sa śāntimadhigacchati",
        ], "|| 71 ||",
           "The man who gives up all desires and moves about free from longing, without the sense of 'mine', without the sense of 'I', attains peace.",
           bhashya=[
               "vihāya iti. vihāya parityajya kāmān yaḥ sannyāsī pumān sarvān aśeṣataḥ kārtsnyena carati jīvanamātraceṣṭāśeṣaḥ paryaṭati ityarthaḥ. nispṛhaḥ śarīrajīvana mātre'pi nirgatā spṛhā yasya saḥ nispṛhaḥ san nirmamaḥ śarīra jīvanamātrākṣiptaparigrahepi “mama idaṃ” iti abhiniveśavarjitaḥ, nirahaṅkāraḥ vidyāvatvādi nimittātmasambhāvanārahitaḥ ityetat. saḥ evambhūtaḥ sthitaprajñaḥ brahmavit śāntiṃ sarvasaṃsāraduḥkhoparamalakṣaṇāṃ nirvāṇākhyāṃ adhigacchati prāpnoti brahmabhūtaḥ bhavati ityarthaḥ. sā eṣā jñānaniṣṭhā stūyate –",
           ]),
        _v([
            "eṣā brāhmī sthitiḥ pārtha naināṃ prāpya vimuhyati |",
            "sthitvā'syāmantakāle'pi brahmanirvāṇamṛcchati",
        ], "|| 72 ||",
           "This is the Brāhmī state, Pārtha; attaining it, one is no longer deluded. Remaining in it even at the hour of death, one attains the peace of Brahman (brahmanirvāṇa).",
           bhashya=[
               "eṣā brāhmī iti. eṣā yathoktā brāhmī brahmaṇi bhavā iyaṃ sthitiḥ sarvaṃ karma sannyasya brahma svarūpeṇa eva avasthānaṃ ityetat. he pārtha! na enāṃ sthitiṃ prāpya labdhvā vimuhyati mohaṃ prāpnoti. sthitvā asyāṃ sthitau brāhmyāṃ yathoktāyāṃ antakālepi antye vayasyapi brahmanirvāṇaṃ brahmanirvṛtiṃ mokṣam ṛcchati gacchati. kimu vaktavyaṃ brahmacaryāt eva sannyasya yāvajjīvaṃ yaḥ brahmaṇi eva avatiṣṭhate saḥ brahmanirvāṇaṃ ṛcchati iti?",
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsu upaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjuna saṃvāde sāṅkhyayogo nāma dvitīyaḥ adhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the second chapter, Sāṅkhya Yoga."},
        {"colophon": "iti śrīmatparamahaṃsarivrājakācāryagovindabhagavatpūjyapādaśiṣya śrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye sāṅkhyayogo nāma dvitīyo'dhyāyaḥ", "gloss": "Thus ends the second chapter, Sāṅkhya Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
