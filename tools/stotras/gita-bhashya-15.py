# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 15 (Puruṣottama Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 15 · Puruṣottama Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 15",
    "h1": "Bhagavad Gītā · Chapter 15",
    "subtitle": "Puruṣottama Yoga · the supreme Person · with Śaṅkara's bhāṣya",
    "note": "The world as an inverted aśvattha tree, rooted above, to be cut down with the axe of detachment; the individual self as a fragment of the Lord; and the Supreme Person (puruṣottama), beyond both the perishable and the imperishable.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 14', 'gita-bhashya-14-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 16 ›', 'gita-bhashya-16-iast.html')],
    "sections": [
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "ūrdhvamūlamadhaḥśākhamaśvatthaṃ prāhuravyayam |",
            "chandāṃsi yasya parṇāni yastaṃ veda sa vedavit",
        ], "|| 1 ||",
           "The Blessed Lord said: They speak of the imperishable aśvattha tree with its roots above and its branches below; its leaves are the Vedic hymns. He who knows it knows the Veda.",
           bhashya=[
               {"text": "yasmāt madadhīnaṃ karmiṇāṃ karmaphalaṃ jñānināṃ ca jñānaphalam ataḥ bhaktiyogena māṃ ye sevante te matprasādāt jñānaprāptikrameṇa guṇātītāḥ mokṣaṃ gacchanti, kimu vaktavyam ātmanaḥ tattvameva samyak vijānantaḥ ityataḥ bhagavān arjunena apṛṣṭamapi ātmanaḥ tattvaṃ vivakṣuḥ uvāca – “ūrdhvamūlam” ityādinā. tatra tāvat vṛkṣarūpakalpanayā vairāgyahetoḥ saṃsārasvarūpaṃ varṇayati. viraktasya hi saṃsārāt bhagavattattvajñāne adhikāraḥ na anyasya iti.", "intro": True},
               "ūrdhvamūlaṃ kālataḥ sūkṣmatvāt, kāraṇatvāt, nityatvāt, mahattvāt ca “ūrdhvam ucyate brahma avyaktaṃ māyāśaktimat, tat mūlam asya iti so'yaṃ saṃsāravṛkṣaḥ ūrdhvamūlaḥ. śruteśca “ūrdhvamūlo'vākśākhaḥ eṣo'śvatthaḥ sanātanaḥ” (ka.u.6.1) iti, purāṇe ca avyaktamūlaprabhavastasyaivānugrahocchritaḥ | buddhiskandhamayaścaiva indriyāntara koṭaraḥ || mahābhūtaviśākhaśca viṣayaiḥ patravāṃstathā | dharmādharma supuṣpaśca sukhaduḥkhaphalodayaḥ || ājīvyaḥ sarvabhūtānāṃ brahmavṛkṣaḥ sanātanaḥ | etad brahmavanaṃ caiva brahmavṛkṣasya tasya tat || etacchittvā ca bhittvā ca jñānena paramāsinā | tataścātmaratiṃ prāpya tasmānnāvartate punaḥ || (aśva.parva. 35.20'22,47.12'15) ityādi taṃ ūrdhvamūlaṃ saṃsāraṃ māyāmayaṃ vṛkṣaṃ āhuḥ. mahadahaṅkāra tanmātrādayaḥ śākhāḥ iva asya adhaḥ bhavantīti so'yaṃ adhaḥśākhaḥ, taṃ adhaḥ śākham. na śvo'pi sthātā iti aśvatthaḥ taṃ kṣaṇapradhvaṃsinaṃ aśvatthaṃ prāhuḥ kathayanti. avyayaṃ – saṃsāramāyāyāḥ anādikālapravṛttatvāt so'yaṃ saṃsāravṛkṣaḥ avyayaḥ anādyanantadehādisantānāśrayaḥ hi suprasiddhaḥ – taṃ avyayam. tasyaiva saṃsāravṛkṣasya idaṃ anyat viśeṣaṇam – chandāṃsi yasya parṇāni chandāṃsi chādanāt ṛgyajuḥ sāmalakṣaṇāni yasya saṃsāravṛkṣa parṇānīva parṇāni. yathā vṛkṣasya parirakṣaṇārthāni parṇāni, tathā vedāḥ saṃsāravṛkṣa parirakṣaṇārthāḥ, dharmādharma taddhetuphalapradarśanārthatvāt. yathāvyākhyātaṃ saṃsāravṛkṣaṃ samūlaṃ yaḥ taṃ veda saḥ vedavit, vedārthavit ityarthaḥ. na hi samūlāt saṃsāravṛkṣāt asmāt jñeyaḥ anyaḥ aṇumātro'pi avaśiṣṭaḥ asti ityataḥ sarvajñaḥ sarvavedārthaviditi samūlasaṃsāravṛkṣajñānaṃ stauti –",
           ]),
        _v([
            "adhaścordhvaṃ prasṛtāstasya śākhā guṇapravṛddhā viṣayapravālāḥ |",
            "adhaśca mūlānyanusantatāni karmānubandhīni manuṣyaloke",
        ], "|| 2 ||",
           "Its branches spread below and above, nourished by the guṇas, with sense-objects for their shoots; and below, its roots stretch out, binding to action in the world of men.",
           bhashya=[
               {"text": "tasya etasya saṃsāravṛkṣasya aparā avayava kalpanā ucyate", "intro": True},
               "adhaḥ manuṣyādibhyaḥ yāvat sthāvaram, ūrdhvaṃ ca yāvat brāhmaṇaḥ viśvasṛjaḥ dhāma ityetadantaṃ yathākarma yathāśrutaṃ jñānakarmaphalāni tasya vṛkṣasya śākhāḥ prasṛtāḥ pragatāḥ, guṇapravṛddhāḥ – guṇaiḥ sattvarajastamobhiḥ pravṛddhāḥ sthūlīkṛtāḥ upādānabhūtaiḥ, viṣayapravālāḥ viṣayāḥ śabdādayaḥ, pravālāḥ iva dehādi karmaphalebhyaḥ śākhādibhyaḥ aṅkurībhavantīva, tena viṣayapravālāḥ śākhāḥ. saṃsāra vṛkṣasya paramamūlam upādānakāraṇaṃ pūrvam uktam. atha idānīṃ karmaphalajanitarāgadveṣādivāsanāḥ mūlānīva dharmādharmapravṛtti kāraṇāni avāntarabhāvīni, tāni adhaḥ ca dehādyapekṣayā mūlāni, anusantatāni anupraviṣṭāni, karmānubandhīni– karma dharmādharmalakṣaṇam, anubandhaḥ paścādbhāvi yeṣām udbhūtim anu udbhavatīti tāni karmānubandhīni, manuṣyaloke viśeṣataḥ. atra hi manuṣyāṇāṃ karmādhikāraḥ prasiddhaḥ.",
           ]),
        _v([
            "na rūpamasyeha tathopalabhyate nānto nacādirna ca sampratiṣṭhā |",
            "aśvatthamenaṃ suvirūḍhamūlamasaṅgaśastreṇa dṛḍhena chittvā",
        ], "|| 3 ||",
           "Its form is not perceived here as such, nor its end, nor its beginning, nor its foundation. Having cut down this firmly rooted aśvattha with the strong axe of non-attachment,",
           bhashya=[
               {"text": "yastu ayaṃ varṇitaḥ saṃsāravṛkṣaḥ –", "intro": True},
               "na rūpam asya iha yathā varṇitaṃ tathā naiva upalabhyate, svapnamarīcyudakamāyāgandharvanagarasamatvāt, dṛṣṭanaṣṭasvarūpaḥ hi saḥ ityataḥ, antaḥ paryantaḥ niṣṭhā parisamāptirvā, vidyate. tathā na ca ādiḥ – “itaḥ ārabhya ayaṃ pravṛttaḥ” iti na kenacit avagamyate. na ca sampratiṣṭhā sthitiḥ, madhyam asya kenacit upalabhyate. aśvattham enaṃ yathoktaṃ, suvirūḍhamūlaṃ suṣṭu virūḍhāni1 virohaṃ gatāni sudṛḍhāni mūlāni yasya tam enaṃ yathoktaṃ, suvirūḍha– mūlam asaṅgaśastreṇa – asaṅgaḥ putravittalokaiṣaṇābhyaḥ vyutthānaṃ, tena asaṅgaśastreṇa, dṛḍhena paramātmābhimukhyaniścaya dṛḍhikṛtena, punaḥ punaḥ vivekābhyāsāśmaniśitena, chittvā saṃsāravṛkṣaṃ sabījam uddhṛtya.",
           ]),
        _v([
            "tataḥ padaṃ tatparimārgitavyaṃ yasmin gatā na nivartanti bhūyaḥ |",
            "tameva cādyaṃ puruṣaṃ prapadye yataḥ pravṛttiḥ prasṛtā purāṇī",
        ], "|| 4 ||",
           "then one should seek that state from which, once reached, none return, thinking: 'I take refuge in that primal Person from whom the ancient stream of activity has flowed.'",
           bhashya=[
               "tataḥ iti – tataḥ paścāt yat padaṃ vaiṣṇavaṃ, tat parimārgitavyam. parimārgaṇam anveṣaṇam. jñātavyam ityarthaḥ. yasmin pade gatāḥ praviṣṭāḥ. na nivartanti na āvartante, bhūyaḥ punaḥ, saṃsārāya. kathaṃ parimārgitavyam ityāha – tameva ca yaḥ padaśabdena uktaḥ, ādyam ādau bhavaṃ puruṣaṃ prapadye ityevaṃ parimārgitavyaṃ taccharaṇatayā ityarthaḥ. kaḥ asau puruṣaḥ iti ucyate – yataḥ yasmāt puruṣāt. saṃsāramāyā vṛkṣa pravṛttiḥ, prasṛtā niḥsṛtā, aindrajālikādiva māyā, purāṇī cirantanī.",
           ]),
        _v([
            "nirmānamohā jitasaṅgadoṣā adhyātmanityā vinivṛttakāmāḥ |",
            "dvandvairvimuktāḥ sukhaduḥkhasañjñaiḥ gacchantyamūḍhāḥ padamavyayaṃ tat",
        ], "|| 5 ||",
           "Free from pride and delusion, having conquered the fault of attachment, ever devoted to the Self, with desires turned away, released from the pairs called pleasure and pain, the undeluded reach that imperishable state.",
           bhashya=[
               {"text": "kathaṃ bhūtāḥ tat padaṃ gacchantīti? ucyate –", "intro": True},
               "nirmānamohāḥ mānaśca mohaśca mānamohau, tau nirgatau yebhyaḥ te nirmānamohāḥ, māna mohavarjitāḥ jitasaṅgadoṣāḥ saṅga eva doṣaḥ saṅgadoṣaḥ jitaḥ saṅgadoṣaḥ yaiḥ te jitasaṅgadoṣāḥ. adhyātma nityāḥ paramātmasvarūpālocane nityāḥ tatparāḥ. vinivṛttakāmāḥ viśeṣeṇa nirlepena nivṛttāḥ kāmāḥ yeṣāṃ te vinivṛtta kāmāḥ, yatayaḥ sannyāsinaḥ, dvandvaiḥ priyāpriyādibhiḥ vimuktāḥ sukhaduḥkhañjñaiḥ parityaktāḥ gacchanti, amūḍhāḥ mohavarjitāḥ padam avyayam tat yathoktam.",
           ]),
        _v([
            "na tadbhāsayate sūryo na śaśāṅko na pāvakaḥ |",
            "yadgatvā na nivartante taddhāma paramaṃ mama",
        ], "|| 6 ||",
           "Neither the sun nor the moon nor fire illumines it; having gone there, none return. That is my supreme abode.",
           bhashya=[
               {"text": "tadeva padaṃ punaḥ viśiṣyate –", "intro": True},
               "tat dhāma iti vyavahitena dhāmnā sambandhaḥ. dhāma tejorūpaṃ padaṃ, na bhāsayate sūryaḥ ādityaḥ, sarvāvabhāsanaśaktimattve'pi sati. tathā na śaśāṅkaḥ candraḥ, na pāvakaḥ na agniḥ api. yat dhāma vaiṣṇavaṃ padaṃ gatvā prāpya na nivartante. yacca sūryādiḥ na bhāsayate tat dhāma padaṃ paramaṃ viṣṇoḥ mama padam.",
           ]),
        _v([
            "mamaivāṃśo jīvaloke jīvabhūtaḥ sanātanaḥ |",
            "manaḥṣaṣṭhānīndriyāṇi prakṛtisthāni karṣati",
        ], "|| 7 ||",
           "An eternal fragment of me, having become the living self in the world of living beings, draws to itself the senses, with the mind as the sixth, which rest in prakṛti.",
           bhashya=[
               {"text": "yat gatvā na nivartante ityuktam. nanu sarvā hi gatiḥ āgatyantā, “saṃyogāḥ viprayogāntāḥ” (strī. parva 2.3, mokṣa. parva 27.31, 330.20, vā.rā. ayo 105.16 ityādau) iti prasiddham. kathaṃ ucyate. “tat dhāma gatānāṃ nāsti nivṛttiḥ” iti? śṛṇu tatra kāraṇam –", "intro": True},
               "mamaiva paramātmanaḥ nārāyaṇasya, aṃśaḥ bhāgaḥ avayavaḥ ekadeśaḥ iti anarthāntaram. jīvaloke jīvānāṃ loke saṃsāre, jīvabhūtaḥ bhoktā kartā iti prasiddhaḥ sanātanaḥ cirantanaḥ, yathā jalasūryakaḥ sūryāṃśaḥ jalanimittāpāye sūryameva gattvā na nivartate – tenaiva ātmanā saṅgacchati, evameva. yathā vā ghaṭādyupādhiparicchinnaḥ ghaṭādyākāśaḥ ākāśāṃśaḥ san ghaṭādinimittāpāye ākāśaṃ prāpya na nivartate ityevam, ataḥ upapannam uktaṃ “yad gatvā na nivartante” iti. nanu niravayavasya paramātmanaḥ kutaḥ avayavaḥ ekadeśaḥ aṃśaḥ iti? sāvayavatve ca vināśaprasaṅgaḥ avayavavibhāgāt. naiṣaḥ doṣaḥ. avidyākṛtopādhiparicchinnaḥ ekadeśaḥ aṃśaḥ iva kalpitaḥ yataḥ. darśitaśca ayam arthaḥ kṣetrādhyāye (13) vistaraśaḥ. saḥ ca jīvaḥ madaṃśatvena kalpitaḥ kathaṃ saṃsarati utkrāmati ca iti? ucyate – manaḥ ṣaṣṭhāni indriyāṇi śrotrādīni prakṛtisthāni svasthāne karṇaśaṣkulyādau prakṛtau sthitāni karṣati ākarṣati. kasmin kāle.",
           ]),
        _v([
            "śarīraṃ yadavāpnoti yaccāpyutkrāmatīśvaraḥ |",
            "gṛhītvaitāni saṃyāti vāyurgandhānivāśayāt",
        ], "|| 8 ||",
           "When the lord acquires a body and when he leaves it, he takes these with him and goes, as the wind carries scents from their sources.",
           bhashya=[
               "yaccāpi yadā cāpi utkrāmati, īśvaraḥ dehādisaṅghātasvāmī jīvaḥ “tadā karṣati” iti ślokasya dvitīyapādaḥ arthavaśāt prāthamyena sambadhyate. yadā ca pūrvasmāt śarīrāt śarīrāntaram āpnoti tadā gṛhītvā etāni manaḥ ṣaṣṭhāni indriyāṇi saṃyāti samyak yāti gacchati. kimiva ityāha vāyuḥ pavanaḥ gandhān iva, āśayāt puṣpādeḥ. kāni punaḥ tāni iti? –",
           ]),
        _v([
            "śrotraṃ cakṣuḥ sparśanaṃ ca rasanaṃ ghrāṇameva ca |",
            "adhiṣṭhāya manaścāyaṃ viṣayānupasevate",
        ], "|| 9 ||",
           "Presiding over the ear, the eye, touch, taste and smell, and the mind, he enjoys the objects of the senses.",
           bhashya=[
               "śrotraṃ cakṣuḥ sparśanaṃ ca tvagindriyaṃ rasanaṃ jihvā ghrāṇam eva ca, manaḥ ṣaṣṭham, pratyekam indriyeṇa saha adhiṣṭhāya dehasthaḥ viṣayān śabdādīn upasevate.",
           ]),
        _v([
            "utkrāmantaṃ sthitaṃ vāpi bhuñjānaṃ vā guṇānvitam |",
            "vimūḍhā nānupaśyanti paśyanti jñānacakṣuṣaḥ",
        ], "|| 10 ||",
           "The deluded do not see him as he departs or stays or enjoys, joined with the guṇas; those with the eye of knowledge see him.",
           bhashya=[
               {"text": "evaṃ dehagataṃ dehāt –", "intro": True},
               "utkrāmantaṃ, parityajantaṃ dehaṃ pūrvopāttaṃ, sthitaṃ vā dehe tiṣṭhantaṃ, bhuñjānaṃ vā śabdādīn ca upalabhamānaṃ, guṇānvitaṃ sukhaduḥkhamohākhyaiḥ guṇaiḥ anvitam anugataṃ, saṃyuktamityarthaḥ. evaṃ bhūtam api enam, atyantadarśanagocaraprāptaṃ, vimūḍhāḥ dṛṣṭādṛṣṭaviṣayabhogabalākṛṣṭacetastayā, anekadhā mūḍhāḥ, na anupaśyanti – aho! kaṣṭaṃ vartate iti anukrośati ca bhagavān. ye tu punaḥ pramāṇajanitajñānacakṣuṣaḥ te enaṃ paśyanti jñāna cakṣuṣaḥ viviktadṛṣṭayaḥ ityarthaḥ. kecittu –",
           ]),
        _v([
            "yatanto yoginaścainaṃ paśyantyātmanyavasthitam |",
            "yatanto'pyakṛtātmāno nainaṃ paśyantyacetasaḥ",
        ], "|| 11 ||",
           "Yogins who strive see him established in themselves; but the unwise, whose selves are unrefined, do not see him even though they strive.",
           bhashya=[
               "yatantaḥ prayatnaṃ kurvantaḥ yoginaḥ ca samāhitacittāḥ, enaṃ prakṛtam ātmānaṃ paśyanti – “ayamaham asmi” iti upalabhante. ātmani svasyāṃ buddhau avasthitaṃ. yatantaḥ api śāstrādipramāṇaiḥ, akṛtātmānaḥ asaṃskṛtātmānaḥ tapasā indriyajayena ca, duścaritāt anuparatāḥ, aśāntadarpāḥ, prayatnaṃ kurvantaḥ api, na enaṃ paśyanti, acetasaḥ avivekinaḥ.",
           ]),
        _v([
            "yadādityagataṃ tejo jagadbhāsayate'khilam |",
            "yaccandramasi yaccāgnau tattejo viddhi māmakam",
        ], "|| 12 ||",
           "The radiance of the sun that illumines the whole world, the radiance in the moon and in fire — know that radiance to be mine.",
           bhashya=[
               {"text": "yat padaṃ sarvasya avabhāsakam api agnyādityādikaṃ jyotiḥ na avabhāsayate. yatprāptāśca mumukṣavaḥ punaḥ saṃsārābhimukhāḥ na nivartante, yasya ca padasya upādhibhedamanuvidhīyamānāḥ jīvāḥ ghaṭākāśādayaḥ iva ākāśasya aṃśāḥ tasya padasya sarvātmatvaṃ sarvavyavahārāspadatvaṃ ca vivakṣuḥ caturbhiḥ ślokaiḥ vibhūtisaṅkṣepaṃ āha bhagavān–", "intro": True},
               "yat, ādityagatam ādityāśrayaṃ, kiṃ, tat? tejaḥ dīptiḥ, prakāśaḥ, jagat bhāsayate prakāśayati akhilaṃ samastaṃ, yat, candramasi, tejaḥ avabhāsakaṃ vartate, yat ca agnau hutavahe, tat tejaḥ viddhi vijānīhi, māmakaṃ madīyaṃ, mama viṣṇoḥ tat jyotiḥ. athavā – yat ādityagataṃ tejaḥ caitanyātmakaṃ jyotiḥ, yat candramasi, yacca agnau vartate tat tejaḥ viddhi māmakaṃ madīyaṃ, mama viṣṇoḥ tat jyotiḥ. nanu sthāvareṣu jaṅgameṣu ca tat samānaṃ caitanyātmakaṃ jyotiḥ, tatra katham idaṃ viśeṣaṇaṃ “yadādityagatam” ityādi. naiṣa doṣaḥ, sattvādhikyāt āvistaratvopapatteḥ. ādityādiṣu hi sattvam atyantaprakāśam atyanta bhāsvaram ataḥ tatraiva āvistaraṃ jyotiḥ iti tat viśiṣyate, na tu tatraiva tat adhikam iti. yathā hi loke tulye'pi mukha saṃsthāne na kāṣṭhakuḍyādau mukham āvirbhavati, ādarśādau tu svacche svacchatare ca tāratamyena āvirbhavati tadvat. kiñca",
           ]),
        _v([
            "gāmāviśya ca bhūtāni dhārayāmyahamojasā |",
            "puṣṇāmi cauṣadhīḥ sarvāḥ somo bhūtvā rasātmakaḥ",
        ], "|| 13 ||",
           "Entering the earth, I sustain beings by my energy; and becoming the watery soma, I nourish all plants.",
           bhashya=[
               "gāṃ pṛthivīm, āviśya praviśya, dhārayāmi, bhūtāni jagat, aham, ojasā balena, yat balaṃ kāmarāgavivarjitam aiśvaraṃ rūpaṃ jagadvidhāraṇāya pṛthivyāṃ āviṣṭaṃ, yena gurvī pṛthivī na adhaḥ patati na vidīryate ca, tathā ca mantravarṇaḥ – “yena dyaurugrā pṛthivī ca dṛḍhā” (tai.saṃ. 4.1.8) iti, “sa dādhāra pṛthivīm” (tai.saṃ. 4.1.8) ityādiśca. ataḥ gām āviśya ca bhūtāni carācarāṇi dhārayāmi iti yuktam uktam. kiṃ ca pṛthivyāṃ jātāḥ oṣadhīḥ sarvāḥ vrīhiyavādyāḥ puṣṇāmi puṣṭimatīḥ rasasvādumatīśca karomi, somaḥ bhūtvā, rasātmakaḥ somaḥ san sarvarasātmakaḥ rasasvabhāvaḥ sarvarasānām ākaraḥ somaḥ. sa hi sarvarasātmakaḥ sarvāḥ oṣadhīḥ svātmarasānanupraveśayan puṣṇāti. kiñca –",
           ]),
        _v([
            "ahaṃ vaiśvānaro bhūtvā prāṇināṃ dehamāśritaḥ |",
            "prāṇāpānasamāyuktaḥ pacāmyannaṃ caturvidham",
        ], "|| 14 ||",
           "Becoming the digestive fire, I abide in the bodies of living beings, and joined with the in-breath and out-breath, I digest the four kinds of food.",
           bhashya=[
               "ahameva vaiśvānaraḥ udarasthaḥ agniḥ bhūtvā “ayamagni rvaiśvānaro yoyamantaḥpuruṣe, yenedamannaṃ pacyate” (bṛ.u.5.9.1) ityādiśruteḥ, vaiśvānaraḥ san, prāṇināṃ prāṇavatām, deham āśritaḥ praviṣṭaḥ prāṇāpānasamāyuktaḥ prāṇāpānābhyāṃ samāyuktaḥ saṃyuktaḥ, pacāmi paktiṃ karomi, caturvidhaṃ catuṣprakāram, annam aśanaṃ, bhojyaṃ, bhakṣyaṃ, coṣyaṃ, lehyaṃ ca. bhoktā vaiśvānaraḥ agniḥ, bhojyam annaṃ somaḥ, tat etat ubhayam agnīṣomau sarvam iti paśyataḥ annadoṣalopaḥ na bhavati. kiñca –",
           ]),
        _v([
            "sarvasya cāhaṃ hṛdi sanniviṣṭo mattaḥ smṛtirjñānamapohanaṃ ca |",
            "vedaiśca sarvairahameva vedyo vedāntakṛdvedavideva cāham",
        ], "|| 15 ||",
           "I am seated in the hearts of all; from me come memory, knowledge and their loss. I alone am to be known by all the Vedas; I am the author of Vedānta and the knower of the Veda.",
           bhashya=[
               "sarvasya prāṇijātasya aham ātmā san, hṛdi buddhau, sanniviṣṭaḥ, ataḥ mattaḥ ātmanaḥ sarvaprāṇināṃ smṛtiḥ jñānaṃ tadapohanaṃ apagamanaṃ ca. yeṣāṃ yathā puṇyakarmaṇāṃ puṇyakarmānurodhena jñāna smṛtī bhavataḥ tathā pāpakarmiṇāṃ pāpakarmānurūpeṇa smṛtijñānayoḥ, apohanaṃ ca apāyanam apagamanaṃ ca, vedaiḥ ca sarvaiḥ, ahameva paramātmā, vedyaḥ veditavyaḥ, vedāntakṛt, vedāntārthasampradāyakṛt ityarthaḥ. vedavit vedārthavideva ca aham.",
           ]),
        _v([
            "dvāvimau puruṣau loke kṣaraścākṣara eva ca |",
            "kṣaraḥ sarvāṇi bhūtāni kūṭastho'kṣara ucyate",
        ], "|| 16 ||",
           "There are two persons in the world, the perishable and the imperishable. The perishable is all beings; the unchanging one is called the imperishable.",
           bhashya=[
               {"text": "bhagavataḥ īśvarasya nārāyaṇākhyasya vibhūtisaṅkṣepaḥ uktaḥ viśiṣṭopādhikṛtaḥ “yadādityagataṃ tejaḥ” (15.12) ityādinā. atha adhunā tasyaiva kṣarākṣaropādhipravibhaktatayā nirupādhikasya kevalasya tattva (svarūpa) nirdidhārayiṣayā uttare ślokāḥ ārabhyante tatra sarvameva atītānāgatādhyāyārtha jātaṃ tridhā rāśīkṛtya āha –", "intro": True},
               "dvau imau pṛthak rāśīkṛtau puruṣāviti ucyete, loke saṃsāre. kṣaraḥ ca kṣaratīti kṣaraḥ, vināśī iti ekaḥ rāśiḥ aparaḥ puruṣaḥ akṣaraḥ tadviparītaḥ bhagavataḥ māyāśaktiḥ, kṣarākhyasya puruṣasya utpattibījam, aneka saṃsāri jantukāmakarmādisaṃskārāśrayaḥ, akṣaraḥ puruṣaḥ ucyate. kau tau puruṣau ityāha svayameva bhagavān – kṣaraḥ sarvāṇi bhūtāni, samastaṃ vikārajātam ityarthaḥ. kūṭasthaḥ kūṭaḥ rāśiḥ rāśiriva sthitaḥ, athavā kūṭaḥ māyā vañcanā jihmatā kuṭilatā iti paryāyāḥ, anekamāyā vañcanādi prakāreṇa sthitaḥ kūṭasthaḥ, saṃsārabījānantyāt na kṣaratīti akṣaraḥ ucyate.",
           ]),
        _v([
            "uttamaḥ puruṣastvanyaḥ paramātmetyudāhṛtaḥ |",
            "yo lokatrayamāviśya bibhartyavyaya īśvaraḥ",
        ], "|| 17 ||",
           "But the highest Person is another, called the supreme Self, who, entering the three worlds as the imperishable Lord, sustains them.",
           bhashya=[
               {"text": "ābhyāṃ kṣarākṣarābhyāṃ anyaḥ vilakṣaṇaḥ kṣarākṣaropādhidvaya doṣeṇa aspṛṣṭaḥ nityaśuddha buddhamukta svabhāvaḥ.", "intro": True},
               "uttamaḥ utkṛṣṭatamaḥ puruṣaḥ tu, anyaḥ atyantavilakṣaṇaḥ ābhyāṃ paramātmā iti – paramaḥ ca asau dehādyavidyākṛtātmabhyaḥ ātmā ca sarvabhūtānāṃ pratyakcetanaḥ. ityataḥ paramātmā iti – udāhṛtaḥ uktaḥ vedānteṣu. saḥ eva viśiṣyate – yaḥ lokatrayaṃ bhūrbhuvaḥ svarākhyaṃ svakīyayā caitanyabalaśaktyā āviśya praviśya, bibharti – svarūpasadbhāvamātreṇa bibharti dhārayati, avyayaḥ na asya vyayaḥ vidyate iti avyayaḥ kaḥ? īśvaraḥ sarvajñaḥ nārāyaṇākhyaḥ īśanaśīlaḥ.",
           ]),
        _v([
            "yasmāt kṣaramatīto'hamakṣarādapi cottamaḥ |",
            "ato'smi loke vede ca prathitaḥ puruṣottamaḥ",
        ], "|| 18 ||",
           "Since I transcend the perishable and am higher even than the imperishable, I am celebrated in the world and in the Veda as the Supreme Person.",
           bhashya=[
               {"text": "yathāvyākhyātasya īśvarasya “puruṣottamaḥ” ityetat nāma prasiddham. tasya nāmanirvacanaprasiddhyā arthavattvaṃ nāmno darśayan “niratiśayaḥ ahaṃ īśvaraḥ” iti ātmānaṃ darśayati bhagavān –", "intro": True},
               "yasmāditi – yasmāt kṣaram atītaḥ ahaṃ saṃsāramāyāvṛkṣam aśvatthākhyam atikrāntaḥ aham, akṣarādapi saṃsāramāyāvṛkṣabījabhūtāt api ca uttamaḥ utkṛṣṭatamaḥ ūrdhvatamaḥ vā, ataḥ tābhyāṃ kṣarākṣarābhyām uttamatvāt, asmi bhavāmi, loke vede ca prathitaḥ prakhyātaḥ, puruṣottamaḥ ityevaṃ māṃ bhaktajanāḥ viduḥ, kavayaḥ kāvyādiṣu ca idaṃ nāma nibadhnanti, puruṣottamaḥ ityanena abhidhānena abhigṛṇanti.",
           ]),
        _v([
            "yo māmevamasammūḍho jānāti puruṣottamam |",
            "sa sarvavidbhajati māṃ sarvabhāvena bhārata",
        ], "|| 19 ||",
           "He who, undeluded, knows me thus as the Supreme Person knows all, and worships me with his whole being, O Bhārata.",
           bhashya=[
               {"text": "atha idānīṃ yathāniruktaṃ ātmānaṃ yo veda, tasya idaṃ phalaṃ ucyate –", "intro": True},
               "yaḥ mām īśvaraṃ yathoktaviśeṣaṇam, evaṃ yathoktena prakāreṇa, asammūḍhaḥ sammohavarjitaḥ san, jānāti “ayam aham asmi” iti puruṣottamam. saḥ sarvavit sarvātmanā sarvaṃ vettīti sarvajñaḥ sarvabhūtasthaṃ bhajati māṃ sarvabhāvena sarvātmacittatayā, he bhārata.",
           ]),
        _v([
            "iti guhyatamaṃ śāstramidamuktaṃ mayā'nagha |",
            "etadbuddhvā buddhimānsyāt kṛtakṛtyaśca bhārata",
        ], "|| 20 ||",
           "Thus, sinless one, I have taught you this most secret teaching. Knowing it, one becomes wise and has done all that is to be done, O Bhārata.",
           bhashya=[
               {"text": "asmin adhyāye bhagavattattvajñānaṃ mokṣaphalaṃ uktvā atha idānīṃ tat stauti.", "intro": True},
               "iti etat guhyatamaṃ gopyatamaṃ, atyantarahasyaṃ, ityetat. kiṃ tat śāstram. yadyapi gītākhyaṃ samastaṃ śāstraṃ ucyate. tathā ayameva adhyāyaḥ iha “śāstraṃ” iti ucyate stutyarthaṃ, prakaraṇāt. sarvo hi gītāśāstrārthaḥ asmin adhyāye samāsena uktaḥ na kevalaṃ gītāśāstrārtha eva, kintu sarvaśca vedārthaḥ iha parisamāptaḥ, “yastaṃ veda sa vedavit” (15.1) “vedaiśca sarvairahameva vedyaḥ” (15.15) iti ca uktam. idaṃ uktaṃ kathitaṃ mayā he anagha! apāpa! etat śāstraṃ yathā darśitārthaṃ buddhvā buddhimān syāt bhavet – na anyathā – kṛtakṛtyaśca bhārata! kṛtaṃ kṛtyaṃ kartavyaṃ yena saḥ kṛtakṛtyaḥ, viśiṣṭajanma prasūtena brāhmaṇena yat kartavyaṃ tat sarvaṃ bhagavattattve vidite kṛtaṃ bhavet ityarthaḥ. na ca anyathā kartavyaṃ parisamāpyate kasya cit ityabhiprāyaḥ. “sarvaṃ karmākhilaṃ pārtha! jñāne parisamāpyate” (4.33) iti ca uktam. etaddhi janma sāmagryaṃ (sāphalyaṃ) brāhmaṇasya viśeṣataḥ prāpyaitat kṛtakṛtyo hi dvijo bhavati nānyathā (manu.12.93) iti ca mānavaṃ vacanam. yataḥ etat paramārthatattvaṃ mattaḥ śrutavān asi, ataḥ kṛtārthaḥ tvaṃ bhārata! iti.",
           ]),
        "ornament",
        {"colophon": "iti śrī mahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītā – sūpaniṣatsu brahmavidyāyāṃ yogaśāstre śrī kṛṣṇārjunasaṃvāde puruṣottamayogo nāma pañcadaśo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the fifteenth chapter, Puruṣottama Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣya śrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye puruṣottamayogo nāma pañcadaśo'dhyāyaḥ.", "gloss": "Thus ends the fifteenth chapter, Puruṣottama Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
