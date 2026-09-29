# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 7 (Jñānavijñāna Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 7 · Jñānavijñāna Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 7",
    "h1": "Bhagavad Gītā · Chapter 7",
    "subtitle": "Jñānavijñāna Yoga · knowledge and realisation · with Śaṅkara's bhāṣya",
    "note": "Kṛṣṇa speaks of his two natures, the lower eightfold prakṛti and the higher, the life-principle; of himself as the essence in all things; of māyā, hard to cross; and of the four kinds of devotees, among whom the knower is his very Self.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 6', 'gita-bhashya-06-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 8 ›', 'gita-bhashya-08-iast.html')],
    "sections": [
        {"bhashya": [
            "“yogināmapi sarveṣāṃ madgatenāntarātmanā. śraddhāvān bhajate yo māṃ sa me yuktatamo mataḥ” (6.47) iti praśnabījaṃ upanyasya svayameva “īdṛśaṃ madīyaṃ tattvaṃ, evaṃ madgatāntarātmā syāt” ityetat vivakṣuḥ śrībhagavān uvāca–",
        ], "summary": "bhāṣya · the chapter's opening"},
        _v([
            "mayyāsaktamanāḥ pārtha yogaṃ yuñjan madāśrayaḥ |",
            "asaṃśayaṃ samagraṃ māṃ yathā jñāsyasi tacchṛṇu",
        ], "|| 1 ||",
           "The Blessed Lord said: Hear, Pārtha, how, with your mind attached to me, practising yoga and taking refuge in me, you will know me fully and without doubt.",
           bhashya=[
               "mayyāsaktamanā iti. mayi vakṣyamāṇa viśeṣaṇe parameśvare āsaktaṃ mano yasya sa mayyāsaktamanāḥ, he pārtha! yogaṃ yuñjan manaḥ samādhānaṃ kurvan madāśrayaḥ ahameva parameśvaraḥ āśrayaḥ yasya sa madāśrayaḥ. yo hi kaścit puruṣārthena kenacit, arthī bhavati sa tatsādhanaṃ karma agnihotrādi tapaḥ dānaṃ vā kiñcit āśrayaṃ pratipadyate, ayaṃ tu yogī māmeva āśrayaṃ pratipadyate, hitvā anyat sādhanāntaraṃ mayyeva āsaktamanāḥ bhavati. yaḥ tvaṃ evambhūtaḥ san asaṃśayaṃ samagraṃ samasta vibhūti balaśakyaiśvaryādi guṇasampannaṃ māṃ yathā yena prakāreṇa jñāsyasi saṃśayamantareṇa “evameva bhagavān” iti tat śṛṇu ucyamānaṃ mayā.",
           ]),
        _v([
            "jñānaṃ te'haṃ savijñānamidaṃ vakṣyāmyaśeṣataḥ |",
            "yad jñātvā neha bhūyo'nyat jñātavyamavaśiṣyate",
        ], "|| 2 ||",
           "I will teach you this knowledge together with realisation, without remainder; knowing it, nothing further remains here to be known.",
           bhashya=[
               {"text": "tacca madviṣayam–", "intro": True},
               "jñānaṃ iti. jñānaṃ te tubhyaṃ ahaṃ savijñānaṃ vijñānasahitaṃ svānubhavayuktaṃ idaṃ vakṣyāmi kathayiṣyāmi aśeṣataḥ kārtsnyena. tat jñānaṃ vivakṣitaṃ stauti śrotuḥ abhimukhīkaraṇāya– yat jñātvā yat jñānaṃ jñātvā na iha bhūyaḥ punaḥ anyat jñātavyaṃ puruṣārthasādhanaṃ avaśiṣyate na avaśiṣṭaṃ bhavati – iti mattattvajño yaḥ, sa sarvajño bhavatītyarthaḥ. ato viśiṣṭaphalatvāt durlabhataraṃ jñānam.",
           ]),
        _v([
            "manuṣyāṇāṃ sahasreṣu kaścidyatati siddhaye |",
            "yatatāmapi siddhānāṃ kaścinmāṃ vetti tattvataḥ",
        ], "|| 3 ||",
           "Among thousands of men, hardly one strives for perfection; and among those who strive and are perfected, hardly one knows me in truth.",
           bhashya=[
               {"text": "kathaṃ iti? ucyate –", "intro": True},
               "manuṣyāṇāṃ iti. manuṣyāṇāṃ madhye sahasreṣu anekeṣu kaścit yatati prayatnaṃ karoti siddhaye siddhyartham. teṣāṃ yatatām api siddhānāṃ – siddhāḥ eva hi te ye mokṣāya yatante, teṣāṃ – kaścit eva hi māṃ vetti tattvataḥ yathāvat.",
           ]),
        _v([
            "bhūmirāpo'nalo vāyuḥ khaṃ mano buddhireva ca |",
            "ahaṅkāra itīyaṃ me bhinnā prakṛtiraṣṭadhā",
        ], "|| 4 ||",
           "Earth, water, fire, air, space, mind, understanding and ego — this is my nature, divided eightfold.",
           bhashya=[
               {"text": "śrotāraṃ prarocanena abhimukhīkṛtyāha –", "intro": True},
               "bhūmiḥ iti. “bhūmiḥ” iti pṛthivī tanmātraṃ ucyate. na sthūlā, “bhinnā prakṛtiraṣṭadhā” iti vacanāt. tathā abādayo'pi tanmātrāṇyeva ucyante – āpaḥ, analaḥ, vāyuḥ, kham. manaḥ iti manasaḥ kāraṇaṃ ahaṅkāro gṛhyate. buddhiḥ iti ahaṅkārakāraṇam mahattattvam. ahaṅkāraḥ iti avidyā saṃyuktaṃ avyaktam. yathā viṣasaṃyuktaṃ annaṃ viṣam iti ucyate, evaṃ ahaṅkāravāsanāvat avyaktaṃ mūlakāraṇaṃ ahaṅkāraḥ ityucyate, pravartakatvāt ahaṅkārasya. ahaṅkāraḥ eva hi sarvasva pravṛttibījaṃ dṛṣṭaṃ loke. itīyaṃ yathoktā prakṛtiḥ me mama aiśvarī māyāśaktiḥ aṣṭadhā bhinnā bhedaṃ āgatā.",
           ]),
        _v([
            "apareyamitastvanyāṃ prakṛtiṃ viddhi me parām |",
            "jīvabhūtāṃ mahābāho yayedaṃ dhāryate jagat",
        ], "|| 5 ||",
           "This is my lower nature. But know my other, higher nature, mighty-armed one: the life-principle by which this world is sustained.",
           bhashya=[
               "aparā iti. aparā na parā nikṛṣṭā aśuddhā anarthakarī saṃsāra bandhanātmikā iyam. itaḥ asyāḥ yathoktāyāḥ tu anyāṃ viśuddhāṃ prakṛtiṃ mama ātmabhūtāṃ viddhi me parāṃ prakṛṣṭāṃ jīvabhūtāṃ kṣetrajñalakṣaṇāṃ prāṇadhāraṇanimittabhūtāṃ he mahābāho yayā prakṛtyā idaṃ dhāryate jagat antaḥ praviṣṭayā.",
           ]),
        _v([
            "etadyonīni bhūtāni sarvāṇītyupadhāraya |",
            "ahaṃ kṛtsnasya jagataḥ prabhavaḥ pralayastathā",
        ], "|| 6 ||",
           "Know that all beings have these two as their womb. I am the origin and the dissolution of the whole world.",
           bhashya=[
               "etat iti. etadyonīni ete parāpare kṣetrakṣetrajña lakṣaṇe prakṛtī yoniḥ yeṣāṃ bhūtānāṃ tāni etadyonīni bhūtāni sarvāṇi iti evaṃ upadhāraya jānīhi. yasmāt mama prakṛtī yoniḥ kāraṇaṃ sarvabhūtānāṃ, ataḥ ahaṃ kṛtsnasya samastasya jagataḥ prabhavaḥ utpattiḥ, pralayaḥ vināśaḥ tathā. prakṛtidvayadvāreṇa ahaṃ sarvajñaḥ īśvaraḥ jagataḥ kāraṇaṃ ityarthaḥ. yasmāt evaṃ tasmāt–",
           ]),
        _v([
            "mattaḥ parataraṃ nānyatkiñcidasti dhanañjaya |",
            "mayi sarvamidaṃ protaṃ sūtre maṇigaṇā iva",
        ], "|| 7 ||",
           "There is nothing whatever higher than I, Dhanañjaya. All this is strung on me like clusters of pearls on a thread.",
           bhashya=[
               "mattaḥ iti. mattaḥ parameśvarāt parataraṃ anyat kāraṇāntaraṃ kiñcit na asti na vidyate, ahameva jagatkāraṇaṃ ityarthaḥ, he dhanañjaya, yasmāt evaṃ tasmāt mayi parameśvare sarvāṇi bhūtāni sarvaṃ idaṃ jagat protaṃ anusyūtaṃ anugataṃ (anuviddhaṃ) grathitaṃ ityarthaḥ, dīrghatantuṣu paṭavat, sūtre ca maṇigaṇāḥ iva.",
           ]),
        _v([
            "raso'hamapsu kaunteya prabhā'smi śaśisūryayoḥ |",
            "praṇavaḥ sarvavedeṣu śabdaḥ khe pauruṣaṃ nṛṣu",
        ], "|| 8 ||",
           "I am the taste in water, son of Kuntī; I am the light in the moon and the sun; the syllable Om in all the Vedas, sound in space, and manhood in men.",
           bhashya=[
               {"text": "kena kena dharmeṇa viśiṣṭe tvayi sarvamidaṃ protaṃ ityucyate?–", "intro": True},
               "rasaḥ iti. rasaḥ ahaṃ apāṃ yaḥ sāraḥ saḥ rasaḥ, tasmin rasabhūte mayi āpaḥ protāḥ ityarthaḥ. evaṃ sarvatra. yathā ahaṃ apsu rasaḥ, evaṃ prabhā asmi śaśisūryayoḥ.praṇavaḥ oṅkāraḥ sarvavedeṣu, tasmin praṇavabhūte mayi sarve vedāḥ protāḥ. tathā khe ākāśe śabdaḥ sārabhūtaḥ, tasmin mayi khaṃ protam. tathā pauruṣaṃ puruṣasya bhāvaḥ pauruṣaṃ – yataḥ pumbuddhiḥ – nṛṣu tasmin mayi puruṣāḥ protāḥ–",
           ]),
        _v([
            "puṇyo gandhaḥ pṛthivyāṃ ca tejaścāsmi vibhāvasau |",
            "jīvanaṃ sarvabhūteṣu tapaścāsmi tapasviṣu",
        ], "|| 9 ||",
           "I am the pure fragrance in the earth and the brilliance in fire; I am the life in all beings and the austerity in ascetics.",
           bhashya=[
               "puṇyaḥ iti – puṇyaḥ surabhiḥ gandhaḥ pṛthivyāṃ ca aham, tasmin mayi gandhabhūte pṛthivī protā. puṇyatvaṃ gandhasya svabhāvataḥ eva pṛthivyāṃ darśitaṃ abādiṣu rasādeḥ puṇyatvopalakṣaṇārtham. apuṇyatvaṃ tu gandhādīnāṃ avidyādharmādyapekṣaṃ saṃsāriṇāṃ bhūtaviśeṣasaṃsarganimittaṃ bhavati. tejaḥ dīptiḥ ca asmi vibhāvasau agnau. tathā jīvanaṃ sarvabhūteṣu, yena jīvanti sarvāṇi bhūtāni tat jīvanam. tapaḥ ca asmi tapasviṣu, tasmin tapasi mayi tapasvinaḥ protāḥ–",
           ]),
        _v([
            "bījaṃ māṃ sarvabhūtānāṃ viddhi pārtha sanātanam |",
            "buddhirbuddhimatāmasmi tejastejasvināmaham",
        ], "|| 10 ||",
           "Know me, Pārtha, as the eternal seed of all beings. I am the understanding of the intelligent and the splendour of the splendid.",
           bhashya=[
               "bījaṃ iti. bījaṃ prarohakāraṇaṃ māṃ viddhi sarvabhūtānāṃ he pārtha sanātanaṃ cirantanam. kiñca – buddhiḥ vivekaśaktiḥ antaḥkaraṇasya buddhimatāṃ vivekaśaktimatāṃ asmi, tejaḥ prāgalbhyaṃ tadvatāṃ tejasvināṃ aham.",
           ]),
        _v([
            "balaṃ balavatāṃ cāhaṃ kāmarāgavivarjitam |",
            "dharmāviruddho bhūteṣu kāmo'smi bharatarṣabha",
        ], "|| 11 ||",
           "Of the strong I am the strength that is free from desire and passion; in beings I am desire that is not contrary to dharma, O best of the Bhāratas.",
           bhashya=[
               "balaṃ iti. balaṃ sāmarthyaṃ ojaḥ balavatāṃ ahaṃ, tat ca balaṃ kāmarāga vivarjitaṃ, kāmaśca rāgaśca kāmarāgau – kāmaḥ tṛṣṇā asannikṛṣṭeṣu viṣayeṣu, rāgaḥ rañjanā prāpteṣu viṣayeṣu – tābhyāṃ kāmarāgābhyāṃ vivarjitaṃ dehādidhāraṇamātrārthaṃ balaṃ sattvaṃ ahaṃ asmi, na tu saṃsāriṇāṃ tṛṣṇārāga kāraṇam. kiñca – dharmāviruddhaḥ dharmeṇa śāstrerthena aviruddhaḥ yaḥ prāṇiṣu bhūteṣu kāmaḥ, yathā dehadhāraṇamātrādyarthaḥ aśanapānādi viṣayaḥ, saḥ kāmaḥ asmi he bharatarṣabha! kiñca–",
           ]),
        _v([
            "ye caiva sāttvikā bhāvā rājasāstāmasāśca ye |",
            "matta eveti tānviddhi na tvahaṃ teṣu te mayi",
        ], "|| 12 ||",
           "And whatever states there are of sattva, rajas and tamas, know that they come from me alone; yet I am not in them — they are in me.",
           bhashya=[
               "ye iti. ye ca eva sāttvikāḥ sattvanirvṛttāḥ bhāvāḥ padārthāḥ, rājasāḥ rajonirvṛttāḥ, tāmasāḥ tamo nirvṛttāśca, ye kecit prāṇināṃ svakarmavaśāt jāyante bhāvāḥ tān mattaḥ eva jāyamānān iti evaṃ viddhi sarvān samastān eva. yadyapi te mattaḥ jāyante tathāpi na tu ahaṃ teṣu tadadhīnaḥ tadvaśaḥ, yathā saṃsāriṇaḥ. te punaḥ mayi madvaśāḥ madadhīnāḥ.",
           ]),
        _v([
            "tribhirguṇamayairbhāvairebhiḥ sarvamidaṃ jagat |",
            "mohitaṃ nābhijānāti māmebhyaḥ paramavyayam",
        ], "|| 13 ||",
           "Deluded by these states made of the three guṇas, this whole world does not recognise me, who am beyond them and imperishable.",
           bhashya=[
               {"text": "evambhūtamapi parameśvaraṃ nityaśuddhabuddhamuktasvabhāvaṃ sarvabhūtātmānaṃ nirguṇaṃ saṃsāradoṣabījapradāhakāraṇaṃ māṃ nābhijānāti jagat iti anukrośaṃ darśayati bhagavān. tacca kiṃ nimittaṃ jagataḥ ajñānamiti? ucyate –", "intro": True},
               "tribhiḥ iti. tribhiḥ guṇamayaiḥ guṇavikāraiḥ rāgadveṣamohādi prakāraiḥ bhāvaiḥ padārthaiḥ ebhiḥ yathoktaiḥ idaṃ prāṇijātaṃ jagat mohitaṃ avivekitāṃ āpāditaṃ sat na abhijānāti māṃ ebhyaḥ yathoktebhyaḥ guṇebhyaḥ paraṃ vyatiriktaṃ vilakṣaṇaṃ ca avyayaṃ vyayarahitaṃ janmādisarvabhāvavikāravarjitaṃ ityarthaḥ.",
           ]),
        _v([
            "daivī hyeṣā guṇamayī mama māyā duratyayā |",
            "māmeva ye prapadyante māyāmetāṃ taranti te",
        ], "|| 14 ||",
           "For this divine māyā of mine, made of the guṇas, is hard to cross; those who take refuge in me alone cross over this māyā.",
           bhashya=[
               {"text": "kathaṃ punaḥ daivīṃ etāṃ triguṇātmikāṃ vaiṣṇavīṃ māyāṃ atikrāmanti iti? ucyate–", "intro": True},
               "daivī iti. daivī devasya mama īśvarasya viṣṇoḥ svabhāvabhūtā hi yasmāt eṣā yathoktā guṇamayī mama māyā duratyayā duḥkhena atyayaḥ atikramaṇaṃ yasyāḥ sā duratyayā. tatra evaṃ sati sarvadharmān parityajya māṃ eva māyāvinaṃ svātmabhūtaṃ sarvātmanā ye prapadyante te māyāṃ etāṃ sarvabhūtamohinīṃ taranti atikrāmanti, te saṃsāra bandhanāt mucyante ityarthaḥ.",
           ]),
        _v([
            "na māṃ duṣkṛtino mūḍhāḥ prapadyante narādhamāḥ |",
            "māyayā'pahṛtajñānā āsuraṃ bhāvamāśritāḥ",
        ], "|| 15 ||",
           "Evildoers, deluded and the lowest of men, do not take refuge in me — their knowledge carried away by māyā, resorting to the demonic state.",
           bhashya=[
               {"text": "yadi tvāṃ prapannāḥ māyāṃ etāṃ taranti, kasmāt tvām eva sarve na prapadyante iti? ucyate–", "intro": True},
               "na māṃ iti. na māṃ parameśvaraṃ nārāyaṇaṃ duṣkṛtinaḥ pāpakāriṇaḥ mūḍhāḥ prapadyante narādhamāḥ narāṇāṃ madhye adhamāḥ nikṛṣṭāḥ te ca māyayā apahṛtajñānāḥ sammuṣitajñānāḥ āsuraṃ bhāvaṃ hiṃsānṛtādilakṣaṇaṃ āśritāḥ",
           ]),
        _v([
            "caturvidhā bhajante māṃ janāḥ sukṛtino'rjuna |",
            "ārto jijñāsurarthārthī jñānī ca bharatarṣabha",
        ], "|| 16 ||",
           "Four kinds of virtuous people worship me, Arjuna: the distressed, the seeker of knowledge, the seeker of gain, and the one who knows, O best of the Bhāratas.",
           bhashya=[
               {"text": "ye punaḥ narottamāḥ puṇyakarmāṇaḥ", "intro": True},
               "caturvidhā iti. caturvidhāḥ catuḥ prakārāḥ bhajante sevante māṃ janāḥ sukṛtinaḥ puṇyakarmāṇaḥ. he arjuna, ārtaḥ ārtiparigṛhītaḥ taskaravyāghrarogādinā abhibhūtaḥ āpannaḥ, jijñāsuḥ bhagavattattvaṃ jñātuṃ icchanti yaḥ. arthārthī dhanakāmaḥ, jñānī viṣṇoḥ tattvavit, ca he bharatarṣabha.",
           ]),
        _v([
            "teṣāṃ jñānī nityayukta ekabhaktirviśiṣyate |",
            "priyo hi jñānino'tyarthamahaṃ sa ca mama priyaḥ",
        ], "|| 17 ||",
           "Of these the knower, ever disciplined and devoted to the One, excels; for I am exceedingly dear to the knower, and he is dear to me.",
           bhashya=[
               "teṣāṃ iti. teṣāṃ caturṇāṃ madhye jñānī tattvavit tattvavittvāt nityayuktaḥ bhavati ekabhaktiśca, anyasya bhajanīyasya adarśanāt, ataḥ saḥ ekabhaktiḥ viśiṣyate viśeṣaṃ ādhikyaṃ āpadyate, atiricyate ityarthaḥ (18.55 bhāṣye). priyaḥ hi yasmāt ahaṃ ātmā jñāninaḥ, ataḥ tasya ahaṃ atyarthaṃ priyaḥ, prasiddhaṃ hi loke “ātmā priyaḥ bhavati” iti. tasmāt jñāninaḥ ātmattvāt vāsudevaḥ priyaḥ bhavatītyarthaḥ. sa ca jñānī mama vāsudevasya ātmā eva iti mama atyarthaṃ priyaḥ.",
           ]),
        _v([
            "udārāḥ sarva evaite jñānī tvātmaiva me matam |",
            "āsthitaḥ sa hi yuktātmā māmevānuttamāṃ gatim",
        ], "|| 18 ||",
           "All these are noble; but the knower I regard as my very Self. For, with disciplined self, he abides in me alone as the highest goal.",
           bhashya=[
               {"text": "na tarhi ārtādayaḥ trayaḥ vāsudevasya priyāḥ? na, kiṃ tarhi?", "intro": True},
               "udārāḥ iti. udārāḥ utkṛṣṭāḥ sarva eva ete, trayo'pi mama priyāḥ evetyarthaḥ na hi kaścit madbhaktaḥ mama vāsudevasya apriyaḥ bhavati. jñānī tu atyarthaṃ priyaḥ bhavatīti viśeṣaḥ. tat kasmāt iti? ataḥ āha– jñānī tu ātmā eva, na anyaḥ mattaḥ iti me mama mataṃ niścayaḥ. āsthitaḥ āroḍhuṃ pravṛttaḥ saḥ jñānī hi yasmāt “ahameva bhagavān vāsudevaḥ na anyaḥ asmi” ityevaṃ yuktātmā samāhitacittaḥ san mām eva paraṃ brahma gantavyaṃ anuttamāṃ gatiṃ gantuṃ pravṛttaḥ ityarthaḥ.",
           ]),
        _v([
            "bahūnāṃ janmanāmante jñānavānmāṃ prapadyate |",
            "vāsudevaḥ sarvamiti sa mahātmā sudurlabhaḥ",
        ], "|| 19 ||",
           "At the end of many births the man of knowledge takes refuge in me, knowing 'Vāsudeva is all'. Such a great soul is very rare.",
           bhashya=[
               {"text": "jñānī punarapi stūyate–", "intro": True},
               "bahūnāṃ iti. bahūnāṃ janmanāṃ jñānārthasaṃskārāśrayāṇāṃ ante samāptau jñānavān prāptaparipākajñānaḥ māṃ vāsudeva pratyagātmānaṃ pratyakṣataḥ prapadyate – katham? vāsudevaḥ sarvaṃ iti. ya evaṃ sarvātmānaṃ māṃ nārāyaṇaṃ pratipadyate, saḥ mahātmā, na tatsamaḥ anyaḥ asti, adhikaḥ vā. ataḥ sudurlabhaḥ, manuṣyāṇāṃ sahasreṣu (7.3) iti hi uktam.",
           ]),
        _v([
            "kāmaistaistairhṛtajñānāḥ prapadyante'nyadevatāḥ |",
            "taṃ taṃ niyamamāsthāya prakṛtyā niyatāḥ svayā",
        ], "|| 20 ||",
           "Those whose knowledge is carried away by this desire or that resort to other gods, observing this rule or that, constrained by their own nature.",
           bhashya=[
               {"text": "ātmaiva sarvaḥ vāsudevaḥ ityevaṃ apratipattau kāraṇaṃ ucyate–", "intro": True},
               "kāmaiḥ iti. kāmaiḥ taiḥ taiḥ putrapaśusvargādi viṣayaiḥ hṛtajñānāḥ apahṛtavivekavijñānāḥ prapadyante anyadevatāḥ prāpnuvanti vāsudevāt ātmanaḥ anyāḥ devatāḥ, taṃ taṃ niyamaṃ devatārādhane prasiddhaḥ yaḥ yaḥ niyamaḥ taṃ taṃ āsthāya āśritya prakṛtyā svabhāvena janmāntarārjita saṃskāraviśeṣeṇa niyatāḥ niyamitāḥ svayā ātmīyayā.",
           ]),
        _v([
            "yo yo yāṃ yāṃ tanuṃ bhaktaḥ śraddhayā'rcitumicchati |",
            "tasya tasyācalāṃ śraddhāṃ tāmeva vidadhāmyaham",
        ], "|| 21 ||",
           "Whatever form any devotee wishes to worship with faith, that same faith of his I make steady.",
           bhashya=[
               {"text": "teṣāṃ ca kāminām–", "intro": True},
               "yo yaḥ iti. yaḥ yaḥ kāmī yāṃ yāṃ devatātanuṃ śraddhayā saṃyuktaḥ bhaktaḥ ca san arcituṃ pūjayituṃ icchati, tasya tasya kāminaḥ acalāṃ sthirāṃ śraddhāṃ tām eva vidadhāmi sthirīkaromi (yayaiva pūrvaṃ pravṛttaḥ). svabhāvataḥ yaḥ yaḥ yāṃ yāṃ devatātanuṃ śraddhayā arcituṃ icchati–",
           ]),
        _v([
            "sa tayā śraddhayā yuktastasyārādhanamīhate |",
            "labhate ca tataḥ kāmān mayaiva vihitān hitān",
        ], "|| 22 ||",
           "Endowed with that faith, he seeks to worship that form, and from it he obtains his desires — granted in truth by me alone.",
           bhashya=[
               "sa tayā iti. saḥ tayā madvihitayā śraddhayā yuktaḥ san tasyāḥ devatātanvāḥrādhanaṃ ārādhanaṃ īhate ceṣṭate. labhate ca tataḥ tasyāḥ ārādhitāyāḥ devatātanvāḥ kāmān īpsitān mayā eva parameśvareṇa sarvajñena karmaphalavibhāgajñatayā vihitān nirmitān, tān hi yasmāt te bhagavatā vihitāḥ kāmāḥ tasmāt tān avaśyaṃ labhate ityarthaḥ. “hitān” iti padacchede hitattvaṃ kāmānāṃ upacaritaṃ kalpyam, na hi kāmāḥ hitāḥ kasyacit.",
           ]),
        _v([
            "antavattu phalaṃ teṣāṃ tadbhavatyalpamedhasām |",
            "devān devayajo yānti madbhaktā yānti māmapi",
        ], "|| 23 ||",
           "But finite is the fruit that comes to those of little understanding. Worshippers of the gods go to the gods; my devotees come to me.",
           bhashya=[
               {"text": "yasmāt antavatsādhanavyāpārāḥ avivekinaḥ kāminaścate, ataḥ–", "intro": True},
               "antavat iti. antavat vināśi tu phalaṃ teṣāṃ tat bhavati alpamedhasāṃ alpaprajñānām. devān devayajaḥ yānti devān yajante iti devayajaḥ, te devān yānti, madbhaktāḥ yānti māṃ api. evaṃ samāne api āyāse mām eva na prapadyante anantaphalāya, aho khalu kaṣṭataraṃ vartate, ityanukrośaṃ darśayati bhagavān.",
           ]),
        _v([
            "avyaktaṃ vyaktimāpannaṃ manyante māmabuddhayaḥ |",
            "paraṃ bhāvamajānanto mamāvyayamanuttamam",
        ], "|| 24 ||",
           "The undiscerning think of me, the unmanifest, as having become manifest, not knowing my higher being, imperishable and supreme.",
           bhashya=[
               {"text": "kiṃ nimittaṃ eva na prapadyante iti? ucyate–", "intro": True},
               "avyaktaṃ iti. avyaktaṃ aprakāśaṃ vyaktiṃ āpannaṃ prakāśaṃ gataṃ idānīṃ manyante māṃ nityaprasiddhaṃ īśvaraṃ api santaṃ abuddhayaḥ avivekinaḥ parambhāvaṃ paramātmasvarūpaṃ ajānantaḥ avivekinaḥ mama avyayaṃ vyayarahitaṃ anuttamaṃ niratiśayaṃ, madīyaṃ bhāvaṃ ajānantaḥ manyante ityarthaḥ.",
           ]),
        _v([
            "nāhaṃ prakāśaḥ sarvasya yogamāyāsamāvṛtaḥ |",
            "mūḍho'yaṃ nābhijānāti loko māmajamavyayam",
        ], "|| 25 ||",
           "Veiled by my yogamāyā, I am not manifest to all. This deluded world does not know me, the unborn and imperishable.",
           bhashya=[
               {"text": "tadajñānaṃ kiṃ nimittaṃ iti? ucyate–", "intro": True},
               "nāhaṃ iti. na ahaṃ prakāśaḥ sarvasya lokasya, keṣāñcit eva madbhaktānāṃ prakāśaḥ ahaṃ ityabhiprāyaḥ. yogamāyāsamāvṛtaḥ yogaḥ guṇānāṃ yuktiḥ ghaṭanaṃ, saiva māyā yogamāyā – athavā, bhagavataḥ cittasamādhānayogaḥ, tatkṛtā māyā yogamāyā tayā yogamāyayā samāvṛtaḥ, sañcchannaḥ ityarthaḥ. ata eva mūḍhaḥ lokaḥ ayaṃ na abhijānāti māṃ ajaṃ avyayam.",
           ]),
        _v([
            "vedāhaṃ samatītāni vartamānāni cārjuna |",
            "bhaviṣyāṇi ca bhūtāni māṃ tu veda na kaścana",
        ], "|| 26 ||",
           "I know the beings that are past, that are present, and that are yet to come, Arjuna; but no one knows me.",
           bhashya=[
               {"text": "yayā yogamāyayā samāvṛtaṃ māṃ lokaḥ nābhijānāti, na asau yogamāyā madīyā satī mama īśvarasya māyāvinaḥ jñānaṃ pratibadhnāti yathā anyasyāpi māyāvinaḥ māyājñānaṃ tadvat. yataḥ evaṃ ataḥ–", "intro": True},
               "veda iti. ahaṃ tu veda jāne samatītāni samatikrāntāni bhūtāni, tathā vartamānāni ca arjuna bhaviṣyāṇi ca bhūtāni veda ahaṃ, māṃ tu veda na kaścana madbhaktaṃ maccharaṇaṃ ekaṃ muktvā, mattattva vedanābhāvādeva na māṃ bhajate.",
           ]),
        _v([
            "icchādveṣasamutthena dvandvamohena bhārata |",
            "sarvabhūtāni sammohaṃ sarge yānti parantapa",
        ], "|| 27 ||",
           "Through the delusion of the pairs of opposites, arising from desire and aversion, O Bhārata, all beings fall into bewilderment at birth, O scorcher of foes.",
           bhashya=[
               {"text": "kena punaḥ mattattva vedanapratibandhane pratibaddhāni santi jāyamānāni sarvabhūtāni māṃ na vidanti ityapekṣāyāṃ idaṃ āha–", "intro": True},
               "icchā iti. icchādveṣasamutthena icchā ca dveṣaśca icchādveṣau tābhyāṃ samuttiṣṭhatīti icchādveṣasamutthaḥ. keneti viśeṣāpekṣāyāṃ idaṃ āha– dvandvamohena iti. dvandvanimittaḥ mohaḥ dvandvamohaḥ tena. tau eva icchādveṣau śītoṣṇavat parasparaviruddhau sukhaduḥkhataddhetu viṣayau yathākālaṃ sarvabhūtaiḥ sambadhyamānau dvandvaśabdena abhidhīyete. tatra yadā icchādveṣau sukhaduḥkhataddhetusamprāptau labdhātmakau bhavataḥ, tadā tau sarvabhūtānāṃ prajñāyāḥ svavaśāpādanadvāreṇa paramārthatattvaviṣayajñānotpatti pratibandhakāraṇaṃ mohaṃ janayataḥ. na hi icchādveṣadoṣaparavaśīkṛtacittasya yathābhūtārthaviṣayajñānaṃ utpadyate bahirapi, kimu vaktavyaṃ tābhyāṃ āviṣṭabuddheḥ sammūḍhasya pratyagātmani bahupratibandhe jñānaṃ notpadyate iti. ataḥ tena icchādveṣasamutthena dvandvamohena, bhārata bharatānvayaja, sarvabhūtāni sammohitāni santi sammohaṃ sammūḍhatāṃ sarge janmani utpattikāle ityetat yānti gacchanti he parantapa. mohavaśāni eva sarvabhūtāni jāyamānāni jāyante ityabhiprāyaḥ. yataḥ evaṃ ataḥ tena dvandvamohena pratibaddhaprajñānāni sarvabhūtāni sammohitāni māṃ ātmabhūtaṃ na jānanti, ataḥ evaṃ ātmabhāvena māṃ na bhajante.",
           ]),
        _v([
            "yeṣāṃ tvantagataṃ pāpaṃ janānāṃ puṇyakarmaṇām |",
            "te dvandvamohanirmuktā bhajante māṃ dṛḍhavratāḥ",
        ], "|| 28 ||",
           "But those people of pure deeds whose sin has come to an end, freed from the delusion of opposites, worship me, firm in their vows.",
           bhashya=[
               {"text": "ke punaḥ anena dvandva mohena nirmuktāḥ santaḥ tvāṃ viditvā yathāśāstraṃ ātmabhāvena bhajante ityapekṣitaṃ arthaṃ darśayituṃ āha.", "intro": True},
               "yeṣāṃ iti. yeṣāṃ tu punaḥ antagataṃ samāptaprāyaṃ kṣīṇaṃ pāpaṃ janānāṃ puṇyakarmaṇāṃ puṇyaṃ karma yeṣāṃ sattvaśuddhikāraṇaṃ vidyate te puṇyakarmāṇaḥ teṣāṃ puṇyakarmaṇāṃ te dvandvamohanirmuktāḥ yathoktena dvandvamohena nirmuktāḥ bhajante māṃ paramātmānaṃ dṛḍhavratāḥ. “evameva paramārthatattvaṃ, nānyathā” ityevaṃ sarvaparityāgavratena niścitavijñānāḥ dṛḍhavratāḥ ucyante.",
           ]),
        _v([
            "jarāmaraṇamokṣāya māmāśritya yatanti ye |",
            "te brahma tadviduḥ kṛtsnamadhyātmaṃ karma cākhilam",
        ], "|| 29 ||",
           "Those who strive for release from old age and death, taking refuge in me, know that Brahman, the whole of the inner Self, and all action.",
           bhashya=[
               {"text": "te kimarthaṃ bhajante iti? ucyate.", "intro": True},
               "jarā iti. jarāmaraṇamokṣāya jarāmaraṇayoḥ mokṣārthaṃ māṃ parameśvaraṃ āśritya matsamāhitacittāḥ santaḥ yatanti prayatante ye, te yat brahma paraṃ tat viduḥ kṛtsnaṃ samastaṃ, adhyātmaṃ pratyagātmaviṣayaṃ vastu tat viduḥ, karma ca akhilaṃ samastaṃ viduḥ.",
           ]),
        _v([
            "sādhibhūtādhidaivaṃ māṃ sādhiyajñaṃ ca ye viduḥ |",
            "prayāṇakāle'pi ca māṃ te viduryuktacetasaḥ",
        ], "|| 30 ||",
           "Those who know me together with the elemental, the divine and the sacrificial, with disciplined minds, know me even at the hour of death.",
           bhashya=[
               "sādhi iti sādhibhūtādhidaivaṃ adhibhūtaṃ ca adhidaivaṃ ca adhibhūtādhidaivaṃ saha adhibhūtādhidaivena vartate iti sādhibhūtādhidaivaṃ ca māṃ ye viduḥ, sādhiyajñaṃ ca saha adhiyajñena sādhiyajñaṃ ye viduḥ, prayāṇakāle maraṇakāle api ca māṃ te viduḥ. yuktacetasaḥ samāhitacittāḥ iti.",
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsūpaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjuna saṃvāde jñānavijñānayogo nāma saptamo'dhyāyaḥ", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the seventh chapter, Jñānavijñāna Yoga."},
        {"colophon": "iti śrī matparamahaṃsa parivrājakācāryagovindabhagavatpūjyapādaśiṣya śrīmacchaṅkarabhagavataḥ kṛtau, śrīmadbhagavadgītābhāṣye jñānavijñānayogo nāma saptamo'dhyāyaḥ", "gloss": "Thus ends the seventh chapter, Jñānavijñāna Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
