# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 4 (Jñānakarmasannyāsa Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 4 · Jñānakarmasannyāsa Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 4",
    "h1": "Bhagavad Gītā · Chapter 4",
    "subtitle": "Jñānakarmasannyāsa Yoga · knowledge, action and renunciation · with Śaṅkara's bhāṣya",
    "note": "Kṛṣṇa reveals the ancient lineage of this yoga and the purpose of his own births, then teaches the seeing of inaction in action and action in inaction, the many forms of sacrifice, and the supremacy of knowledge, which burns all action to ashes.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 3', 'gita-bhashya-03-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 5 ›', 'gita-bhashya-05-iast.html')],
    "sections": [
        {"bhashya": [
            "yaḥ ayaṃ yogaḥ adhyāyadvayena uktaḥ jñānaniṣṭhālakṣaṇaḥ sasannyāsaḥ karmayogopāyaḥ, yasmin vedārthaḥ parisamāptaḥ pravṛttilakṣaṇaḥ, nivṛttilakṣaṇaśca gītāsu ca sarvāsu ayameva yogaḥ vivakṣitaḥ bhagavatā. ataḥ parisamāptaṃ vedārthaṃ manvānaḥ taṃ vaṃśakathanena stauti śrī bhagavān –",
        ], "summary": "bhāṣya · the chapter's opening"},
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "imaṃ vivasvate yogaṃ proktavānahamavyayam |",
            "vivasvānmanave prāha manurikṣvākave'bravīt",
        ], "|| 1 ||",
           "The Blessed Lord said: I taught this imperishable yoga to Vivasvān; Vivasvān taught it to Manu, and Manu told it to Ikṣvāku.",
           bhashya=[
               "imamiti. imam adhyāyadvayena uktaṃ yogaṃ vivasvate ādityāya, sargādau, proktavān ahaṃ jagatparipālayitṝṇāṃ kṣatriyāṇāṃ balādhānāya. tena yogabalena hi yuktāḥ samarthāḥ bhavanti brahma parirakṣitum. brahmakṣattre paripālayitum alam. avyayam avyayaphalatvāt. na hi asya yogasya samyagdarśananiṣṭhālakṣaṇasya mokṣākhyaṃ phalaṃ vyeti. sa ca vivasvān manave prāha. manuḥ ikṣvākave svaputrāya ādirājāya abravīt.",
           ]),
        _v([
            "evaṃ paramparāprāptamimaṃ rājarṣayo viduḥ |",
            "sa kāleneha mahatā yogo naṣṭaḥ parantapa",
        ], "|| 2 ||",
           "Thus received in succession, the royal sages knew it. Through long lapse of time here, O scorcher of foes, that yoga was lost.",
           bhashya=[
               "evamiti : evaṃ kṣatriya paramparāprāptam imaṃ, rājarṣayaḥ, rājānaḥ ca te ṛṣayaḥ ca iti te rājarṣayaḥ, viduḥ imaṃ yogam. saḥ yogaḥ kālena iha mahatā dīrgheṇa, naṣṭaḥ vicchinna sampradāyaḥ saṃvṛttaḥ, he parantapa, ātmanaḥ vipakṣabhūtāḥ parāḥ ucyante, tān śauryatejogabhastibhiḥ bhānuḥ iva tāpayati iti parantapaḥ, śatrutāpana ityarthaḥ.",
           ]),
        _v([
            "sa evāyaṃ mayā te'dya yogaḥ proktaḥ purātanaḥ |",
            "bhakto'si me sakhā ceti rahasyaṃ hyetaduttamam",
        ], "|| 3 ||",
           "That same ancient yoga I have taught you today, for you are my devotee and my friend; this is indeed the highest secret.",
           bhashya=[
               {"text": "durbalān ajitendriyān prāpya naṣṭaṃ yogam imam upalabhya, lokaṃ ca apuruṣārthasambandhinam –", "intro": True},
               "sa evāyam iti : saḥ eva ayaṃ mayā, te tubhyam, adya idānīm, yogaḥ proktaḥ purātanaḥ, bhaktaḥ asi, me sakhā ca asi iti. rahasyaṃ yasmāt hi etat uttamaṃ yogajñānam ityarthaḥ.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "aparaṃ bhavato janma paraṃ janma vivasvataḥ |",
            "kathametadvijānīyāṃ tvamādau proktavāniti",
        ], "|| 4 ||",
           "Arjuna said: Your birth was later, and the birth of Vivasvān earlier. How am I to understand that you taught it in the beginning?",
           bhashya=[
               {"text": "bhagavatā vipratiṣiddham uktam iti mā bhūt kasya cit buddhiḥ iti parihārārthaṃ codyam iva kurvan –", "intro": True},
               "aparamiti : aparam arvāk vasudevagṛhe bhavataḥ janma. paraṃ pūrvaṃ sargādau, janma utpattiḥ, vivasvataḥ ādityasya. tat katham etat vijānīyām aviruddhārthatayā, yaḥ tvam eva ādau proktavān imaṃ yogaṃ saḥ eva tvam idānīṃ mahyaṃ proktavān asi iti.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "bahūni me vyatītāni janmāni tava cārjuna |",
            "tānyahaṃ veda sarvāṇi na tvaṃ vettha parantapa",
        ], "|| 5 ||",
           "The Blessed Lord said: Many births of mine have passed, and of yours, Arjuna. I know them all; you do not know them, O scorcher of foes.",
           bhashya=[
               {"text": "yā vāsudeve anīśvarāsarvajñāśaṅkā mūrkhāṇāṃ tāṃ pariharan śrī bhagavānuvāca, yadarthaḥ hi arjunasya praśnaḥ–", "intro": True},
               "bahūnīti : bahūni, me mama, vyatītāni atikrāntāni, janmāni tava ca he arjuna. tāni ahaṃ, veda jāne, sarvāṇi, na tvaṃ, vettha na jānīṣe, dharmādharmādipratibaddhajñānaśaktitvāt. ahaṃ punaḥ nityaśuddhabuddhamuktasvabhāvatvāt anāvaraṇajñānaśaktiḥ iti veda, ahaṃ, he parantapa.",
           ]),
        _v([
            "ajo'pi sannavyayātmā bhūtānāmīśvaro'pi san |",
            "prakṛtiṃ svāmadhiṣṭhāya sambhavāmyātmamāyayā",
        ], "|| 6 ||",
           "Though I am unborn and my Self is imperishable, though I am the lord of beings, yet governing my own nature I come into being through my own māyā.",
           bhashya=[
               {"text": "kathaṃ tarhi tava nityeśvarasya dharmādharmābhāve'pi janma iti ucyate –", "intro": True},
               "ajo'pīti : ajaḥ api janmarahitaḥ api san, tathā, avyayātmā akṣīṇajñānaśaktisvabhāvaḥ api san, tathā, bhūtānāṃ brahmādistambaparyantānām, īśvaraḥ īśanaśīlaḥ api san, prakṛtiṃ svāṃ mama vaiṣṇavīṃ māyāṃ triguṇātmikāṃ, yasyāḥ vaśe sarvaṃ jagat vartate, yayā mohitaṃ jagat sat svam ātmānaṃ vāsudevaṃ na jānāti tāṃ prakṛtiṃ svām, adhiṣṭhāya vaśīkṛtya, sambhavāmi dehavān iva bhavāmi, jātaḥ iva, ātmamāyayā ātmanaḥ māyayā, na paramārthataḥ lokavat.",
           ]),
        _v([
            "yadā yadā hi dharmasya glānirbhavati bhārata |",
            "abhyutthānamadharmasya tadā''tmānaṃ sṛjāmyaham",
        ], "|| 7 ||",
           "Whenever dharma declines and adharma rises, O Bhārata, then I bring myself forth.",
           bhashya=[
               {"text": "tacca janma kadā, kimarthaṃ ca iti? ucyate –", "intro": True},
               "yadeti : yadā yadā hi dharmasya, glāniḥ hāniḥ varṇāśramādi lakṣaṇasya prāṇinām abhyudayaniḥśreyasasādhanasya, bhavati, bhārata, abhyutthānam udbhavaḥ adharmasya tadā ātmānaṃ sṛjāmi ahaṃ māyayā. kimarthaṃ?",
           ]),
        _v([
            "paritrāṇāya sādhūnāṃ vināśāya ca duṣkṛtām |",
            "dharmasaṃsthāpanārthāya sambhavāmi yuge yuge",
        ], "|| 8 ||",
           "For the protection of the good, for the destruction of evildoers, and to establish dharma firmly, I come into being age after age.",
           bhashya=[
               "paritrāṇāyeti : paritrāṇāya parirakṣaṇāya, sādhūnāṃ sanmārgasthānāṃ, vināśāya ca duṣkṛtāṃ pāpakāriṇāṃ, kiñca dharma saṃsthāpanārthāya dharmasya samyaksthāpanaṃ dharma saṃsthāpanaṃ tadarthaṃ sambhavāmi, yuge yuge pratiyugam.",
           ]),
        _v([
            "janma karma ca me divyamevaṃ yo vetti tattvataḥ |",
            "tyaktvā dehaṃ punarjanma naiti māmeti so'rjuna",
        ], "|| 9 ||",
           "He who truly knows my divine birth and action is not born again on leaving the body; he comes to me, Arjuna.",
           bhashya=[
               "janmeti : janma māyārūpaṃ, karma ca sādhuparitrāṇādi, me mama, divyam aprākṛtam aiśvaram, evaṃ yathoktaṃ, yaḥ vetti tattvataḥ tattvena yathāvat, tyaktvā deham imaṃ, punaḥ janma punaḥ utpattiṃ na eti na prāpnoti. mām eti āgacchati – saḥ mucyate, he arjuna.",
           ]),
        _v([
            "vītarāgabhayakrodhā manmayā māmupāśritāḥ |",
            "bahavo jñānatapasā pūtā madbhāvamāgatāḥ",
        ], "|| 10 ||",
           "Freed from passion, fear and anger, absorbed in me, taking refuge in me, many, purified by the austerity of knowledge, have attained my state.",
           bhashya=[
               {"text": "naiṣaḥ mokṣamārgaḥ idānīṃ pravṛttaḥ, kiṃ tarhi? pūrvamapi –", "intro": True},
               "vītarāgeti : vītarāgabhayakrodhā : rāgaśca bhayaṃ ca krodhaḥ ca vītāḥ vigatāḥ yebhyaḥ te vītarāgabhayakrodhāḥ, manmayāḥ brahmavidaḥ īśvarābhedadarśinaḥ, māmeva ca parameśvaram upāśritāḥ, kevalajñānaniṣṭhāḥ ityarthaḥ. bahavaḥ aneke, jñānatapasā jñānameva ca paramātma viṣayaṃ tapaḥ tena jñānatapasā, pūtāḥ parāṃ śuddhiṃ gatāḥ santaḥ madbhāvam īśvarabhāvaṃ mokṣam āgatāḥ samanuprāptāḥ. itara taponirapekṣajñānaniṣṭhāḥ ityasya liṅgaṃ “jñānatapasā” iti viśeṣaṇam.",
           ]),
        _v([
            "ye yathā māṃ prapadyante tāṃstathaiva bhajāmyaham |",
            "mama vartmānuvartante manuṣyāḥ pārtha sarvaśaḥ",
        ], "|| 11 ||",
           "In whatever way people approach me, in that same way I favour them; everywhere, Pārtha, people follow my path.",
           bhashya=[
               {"text": "“tava tarhi rāgadveṣau staḥ, yena kebhyaścideva ātmabhāvaṃ prayacchasi na sarvebhyaḥ iti?” ucyate –", "intro": True},
               "ye yatheti : ye yathā yena prakāreṇa, yena prayojanena, yatphalārthitayā māṃ prapadyante tān, tathaiva tatphaladānena, bhajāmi anugṛhṇāmi, aham ityetat. teṣāṃ mokṣaṃ prati anarthitvāt. na hi ekasya mumukṣutvaṃ phalārthitvaṃ ca yugapat sambhavati. ataḥ ye yat phalārthinaḥ tān tat phalapradānena, ye yathoktakāriṇaḥ tu aphalārthinaḥ mumukṣavaḥ ca tān jñānapradānena, ye jñāninaḥ sannyāsinaḥ mumukṣuvaḥ ca tān mokṣapradānena, tathā ārtān ārtiharaṇena ityevaṃ yathā prapadyante ye tān tathaiva bhajāmi ityarthaḥ. na punāḥ rāgadveṣanimittaṃ mohanimittaṃ vā kañcit bhajāmi. sarvathāpi sarvāvasthasya mama īśvarasya, vartma mārgam, anuvartante manuṣyāḥ yatphalārthitayā yasmin karmaṇi adhikṛtāḥ ye pravartante te manuṣyāḥ atra ucyante – he pārtha, sarvaśaḥ sarvaprakāraiḥ",
           ]),
        _v([
            "kāṅkṣantaḥ karmaṇāṃ siddhiṃ yajanta iha devatāḥ |",
            "kṣipraṃ hi mānuṣe loke siddhirbhavati karmajā",
        ], "|| 12 ||",
           "Desiring the success of their actions, people here worship the gods; for in the world of men success born of action comes quickly.",
           bhashya=[
               {"text": "yadi tava īśvarasya rāgādidoṣābhāvāt sarvaprāṇiṣu anujighṛkṣāyāṃ tulyāyāṃ, sarvaphalapradānasamarthe ca tvayi sati “vāsudevaḥ sarvam” (7.19) iti jñānenaiva mumukṣavaḥ santaḥ kasmāt tvāmeva sarve na pratipadyante iti? śṛṇu tatra kāraṇam –", "intro": True},
               "kāṅkṣantaḥ iti – kāṅkṣantaḥ abhīpsantaḥ karmaṇāṃ siddhiṃ phalaniṣpattiṃ yajante, iha asmin loke, devatāḥ indrāgnyādyāḥ “athayo'nyāṃ devatāmupāste'sāvanyohamasmīti na sa veda yathā paśurevaṃ sa devānām” (bṛ.u.1.4.10) iti śruteḥ. teṣāṃ hi bhinnadevatāyājināṃ phalākāṅkṣiṇāṃ, kṣipraṃ śīghraṃ, hi yasmāt, mānuṣe loke, manuṣyaloke hi śāstrādhikāraḥ “kṣipraṃ hi mānuṣe loke” iti viśeṣaṇāt anyeṣvapi karmaphalasiddhiṃ darśayati bhagavān. mānuṣe loke varṇāśramādikarmādhikāraḥ iti viśeṣaḥ. teṣāṃ varṇāśramādyadhikāriṇām karmaṇāṃ phalasiddhiḥ bhavati. karmajā karmaṇo jātā.",
           ]),
        _v([
            "cāturvarṇyaṃ mayā sṛṣṭaṃ guṇakarmavibhāgaśaḥ |",
            "tasya kartāramapi māṃ viddhyakartāramavyayam",
        ], "|| 13 ||",
           "The fourfold order of classes was created by me according to the division of guṇa and action. Though I am its author, know me as the non-doer, the imperishable.",
           bhashya=[
               {"text": "mānuṣe eva loke varṇāśramādi karmādhikāraḥ na anyeṣu lokeṣu iti niyamaḥ kiṃ nimittaḥ iti? athavā – varṇāśramādi pravibhāgopetāḥ manuṣyāḥ mama vartma anuvartante sarvaśaḥ iti uktam. kasmāt punaḥ kāraṇāt niyamena tavaiva vartma anuvartante na anyasya iti? ucyate –", "intro": True},
               "cāturvarṇyamiti – cāturvarṇyaṃ catvāraḥ eva varṇāḥ cāturvarṇyam, mayā īśvareṇa, sṛṣṭam utpāditam “brāhmaṇo'sya mukhamāsīt” (ṛ.saṃ.10.90.12, tai.ā.3.12.13) ityādi śruteḥ. guṇakarmavibhāgaśaḥ guṇavibhāgaśaḥ karmavibhāgaśaḥ ca. guṇāḥ sattvarajastamāṃsi. tatra sāttvikasya sattvapradhānasya brāhmaṇasya “śamaḥ damaḥ tapaḥ” (18.42) ityādīni karmāṇi. sattvopasarjana rajaḥ pradhānasya kṣatriyasya “śauryatejaḥ” prabhṛtīni karmāṇi (18.43) tama upasarjanarajaḥ pradhānasya vaiśyasya “kṛṣyādīni” karmāṇi (18.44) raja upasarjanatamaḥ pradhānasya śūdrasya śuśrūṣaiva karma (18.44) ityevaṃ guṇakarmavibhāgaśaḥ cāturvarṇyaṃ mayā sṛṣṭam ityarthaḥ. taccedaṃ cāturvarṇyaṃ na anyeṣu lokeṣu, ato “mānuṣe loke” iti viśeṣaṇam. hanta tarhi cāturvarṇyasya sargādeḥ karmaṇaḥ karmaṇaḥ kartṛtvāt tatphalena yujyase, ataḥ na tvaṃ nityamuktaḥ, nityeśvaraḥ iti? ucyate – yadyapi māyāsaṃvyavahāreṇa tasya karmaṇaḥ kartāram api santaṃ māṃ paramārthataḥ viddhi akartāram, ataḥ eva avyayam asaṃsāriṇaṃ ca māṃ viddhi.",
           ]),
        _v([
            "na māṃ karmāṇi limpanti na me karmaphale spṛhā |",
            "iti māṃ yo'bhijānāti karmabhirna sa badhyate",
        ], "|| 14 ||",
           "Actions do not taint me, nor do I long for their fruit. One who knows me thus is not bound by actions.",
           bhashya=[
               {"text": "yeṣāṃ tu karmaṇāṃ kartāraṃ māṃ manyase, paramārthataḥ teṣām akartaiva ahaṃ, yataḥ –", "intro": True},
               "neti – na, māṃ, tāni karmāṇi, limpanti dehādyārambhakatvena, ahaṅkārābhāvāt. na ca, teṣāṃ karmaṇāṃ, phaleṣu, me, spṛhā tṛṣṇā. yeṣāṃ tu saṃsāriṇām “ahaṃ kartā” ityabhimānaḥ, karmasu spṛhā tatphaleṣu ca, tān karmāṇi limpantīti yuktam. tadabhāvāt na māṃ karmāṇi limpanti. ityevaṃ yaḥ anyo'pi mām ātmatvena abhijānāti, na ahaṃ kartā na me karmaphale spṛhā iti, saḥ karmabhiḥ na badhyate. tasyāpi na dehādyārambhakāṇi karmāṇi bhavanti ityarthaḥ.",
           ]),
        _v([
            "evaṃ jñātvā kṛtaṃ karma pūrvairapi mumukṣubhiḥ |",
            "kuru karmaiva tasmāttvaṃ pūrvaiḥ pūrvataraṃ kṛtam",
        ], "|| 15 ||",
           "Knowing this, the seekers of liberation of old also performed action. Therefore you too should perform action, as the ancients did long ago.",
           bhashya=[
               {"text": "nāhaṃ kartā, na me karmaphale spṛhā iti–", "intro": True},
               "evamiti. evaṃ jñātvā kṛtaṃ karma pūrvaiḥ api atikrāntaiḥ mumukṣubhiḥ. kuru tena karmaiva tvaṃ, na tūṣṇīm āsanaṃ, na sannyāsaḥ kartavyaḥ tasmāt tvaṃ, pūrvairapi anuṣṭhitatvāt. yadi anātmajñastvaṃ tadā ātmaśuddhyarthaṃ, tattvavit cet lokasaṅgrahārthaṃ, pūrvaiḥ janakādibhiḥ, pūrvataraṃ kṛtaṃ, na adhunātanaṃ, kṛtam anuṣṭhitam.",
           ]),
        _v([
            "kiṃ karma kimakarmeti kavayo'pyatra mohitāḥ |",
            "tatte karma pravakṣyāmi yad jñātvā mokṣyase'śubhāt",
        ], "|| 16 ||",
           "What is action, what is inaction? Even the wise are bewildered here. I will explain to you that action, knowing which you will be freed from evil.",
           bhashya=[
               {"text": "tatra karma cet kartavyaṃ tvadvacanādeva karomi aham, kiṃ viśeṣitena “pūrvaiḥ pūrvataraṃ kṛtam” iti? ucyate – yasmāt mahat vaiṣamyaṃ karmaṇi, katham?–", "intro": True},
               "kiṃ karmeti : kiṃ karma kiṃ ca akarma iti, kavayaḥ medhāvinaḥ api atra asmin karmādi viṣaye, mohitāḥ mohaṃ gatāḥ. tat ataḥ te tubhyam, ahaṃ karma akarma ca pravakṣyāmi. yad jñātvā viditvā karmādi mokṣyase aśubhāt saṃsārāt.",
           ]),
        _v([
            "karmaṇo hyapi boddhavyaṃ boddhavyaṃ ca vikarmaṇaḥ |",
            "akarmaṇaśca boddhavyaṃ gahanā karmaṇo gatiḥ",
        ], "|| 17 ||",
           "For one must understand what action is, one must understand what wrong action is, and one must understand what inaction is; deep is the way of action.",
           bhashya=[
               {"text": "na ca etat tvayā mantavyam – karma nāma dehādi ceṣṭā. lokaprasiddham, akarma tadakriyā tūṣṇīm āsanaṃ, kiṃ tatra boddhavyam iti. kasmāt? ucyate–", "intro": True},
               "karmaṇaḥ iti – karmaṇaḥ śāstravihitasya hi yasmāt, api asti boddhavyaṃ, boddhavyaṃ ca asti eva, vikarmaṇaḥ pratiṣiddhasya, tathā akarmaṇaśca tūṣṇīmbhāvasya boddhavyam asti iti triṣvapi adhyāhāraḥ kartavyaḥ. yasmāt gahanā viṣamā durṅñeyā karmaṇaḥ iti upalakṣaṇārthaṃ karmādināṃ karmākarmavikarmaṇāṃ, gatiḥ yāthātmyam tattvamityarthaḥ",
           ]),
        _v([
            "karmaṇyakarma yaḥ paśyedakarmaṇi ca karma yaḥ |",
            "sa buddhimān manuṣyeṣu sa yuktaḥ kṛtsnakarmakṛt",
        ], "|| 18 ||",
           "He who sees inaction in action and action in inaction is wise among men; he is a yogin who has done all action.",
           bhashya=[
               {"text": "kiṃ punaḥ tattvaṃ karmādeḥ yat boddhavyaṃ vakṣyāmi iti pratijñātaṃ ? ucyate–", "intro": True},
               "karmaṇīti : karmaṇi – karma kriyate iti, vyāpāramātram. tasmin karmaṇi akarma karmābhāvaṃ, yaḥ paśyet, akarmaṇi ca karmābhāve – kartṛtantratvāt pravṛtti nivṛttyoḥ vastu aprāpyaiva hi sarva eva kriyākārakādi vyavahāraḥ avidyābhūmau eva – karma yaḥ paśyet paśyati, saḥ buddhimān manuṣyeṣu, saḥ yuktaḥ yogī, kṛtsna karmakṛt samasta karmakṛt ca saḥ iti stūyate karmākarmaṇoḥ itaretaradarśī.",
               "nanu, kimidaṃ viruddham ucyate “karmaṇi akarma yaḥ paśyet” iti “akarmaṇi ca karma” iti? na hi karma akarma syāt akarma vā karma? tatra viruddhaṃ kathaṃ paśyet draṣṭā? nanu akarmaiva paramārthataḥ sat karmavat avabhāsate mūḍhadṛṣṭeḥ lokasya, tathā karmaiva akarmavat. tatra yathābhūtadarśanārthamāha bhagavān “karmaṇyakarma yaḥ paśyet” ityādi. ato na viruddham. buddhimattvādyupapatteśca. “boddhavyam” iti ca yathābhūtadarśanam ucyate. na ca viparītajñānāt aśubhāt mokṣaṇaṃ syāt. “yad jñātvā mokṣyase'śubhāt” iti ca uktam. tasmāt karmākarmaṇī viparyayeṇa gṛhīte prāṇibhiḥ, tadviparyayagrahaṇanivṛttyarthaṃ bhagavato vacanaṃ “karmaṇyakarmayaḥ” ityādi.",
               "na ca atra karmādhikaraṇam akarma asti kuṇḍe badarāṇīva, nāpi akarmādhikaraṇaṃ karma asti, karmābhāvatvāt akarmaṇaḥ. ataḥ viparītagṛhīte eva karmākarmaṇī laukikaiḥ yathā mṛgatṛṣṇikāyām udakaṃ, śuktikāyāṃ vā rajatam.",
               "nanu karma karmaiva sarveṣām, na kvacidvyabhicarati? tat na, nausthasya nāvi gacchantyāṃ taṭastheṣu agatiṣu nageṣu pratikūlagatidarśanāt, dūreṣu cakṣuṣaḥ asannikṛṣṭeṣu gacchatsu gatyabhāvadarśanāt. evam ihāpi akarmaṇi “ahaṃ karomi” iti karma darśanaṃ, karmaṇi ca akarmadarśanaṃ viparīta darśanam, yena tannirākaraṇārthamucyate “karmaṇyakarma yaḥ paśyet” ityādi.",
               "tat etat uktaprativacanam api asakṛt atyantaviparītadarśanabhāvitatayā momuhyamānaḥ lokaḥ śrutamapi asakṛt tattvaṃ vismṛtya, mithyāprasaṅgam avatārya avatārya codayati iti punaḥ punaḥ uttaram āha bhagavān, durvijñeyatvaṃ ca ālakṣya vastunaḥ. “avyakto'yamacintyo'yam” (2.20), “na jāyate mriyate” (2.25) ityādinā ātmani karmābhāvaḥ śrutismṛtinyāyaprasiddhaḥ uktaḥ vakṣyamāṇaḥ ca. tasmin ātmani karmābhāve akarmaṇi karmaviparītadarśanam atyantanirūḍham, yataḥ “kiṃ karma kimakarmeti kavayopyatramohitāḥ” (4.16) dehādyāśrayaṃ ca karma ātmani adhyāropya “ahaṃ kartā, mama etat karma, mayā asya karmaṇaḥ phalaṃ bhoktavyam” iti ca, tathā “ahaṃ tūṣṇīṃ bhavāmi yena ahaṃ nirāyāsaḥ akarmā sukhī syām” iti kāryakaraṇāśrayaṃ vyāpāroparamaṃ, tatkṛtaṃ ca sukhitvam ātmani adhyāropya “na karomi kiñcit, tūṣṇīm sukhaṃ āse” iti abhimanyate lokaḥ, tatra idaṃ lokasya viparītadarśanāpanayanāya āha bhagavān “karmaṇyakarma yaḥ paśyet” ityādi.",
               "atra ca karma karmaiva sat kāryakaraṇāśrayaṃ karmarahite avikriye ātmani sarvaiḥ adhyastam, yataḥ paṇḍito'pi “ahaṃ karomi” iti manyate. ataḥ ātma samavetatayā sarvalokaprasiddhe karmaṇi, nadīkūlastheṣviva vṛkṣeṣu gatiḥ prātilomyena, akarma karmābhāvaṃ yathābhūtaṃ, gatyabhāvamiva vṛkṣeṣu, yaḥ paśyet, akarmaṇi ca kāryakaraṇa vyāpāroparame, karmavat ātmanyadhyāropite, “tūṣṇīm akurvan sukham āse” iti ahaṅkārābhisandhi hetutvāt, tasmin akarmaṇi ca karma yaḥ paśyet, yaḥ evaṃ karmākarma vibhāgajñaḥ saḥ buddhimān paṇḍitaḥ manuṣyeṣu, saḥ yuktaḥ yogī, kṛtsnakarmakṛcca, saḥ aśubhāt mokṣitaḥ kṛtakṛtyo bhavati ityarthaḥ.",
               "ayaṃ ślokaḥ anyathā vyākhyātaḥ kaiścit. katham? nityānāṃ kila karmaṇām īśvarārthatvena anuṣṭhīyamānānāṃ tatphalābhāvāt akarmāṇi tāni ucyante gauṇyā, vṛttyā. teṣāṃ ca akaraṇaṃ akarma, tacca pratyavāyaphalatvāt karma ucyate gauṇyā vṛttyā. tatra nitye karmaṇi akarma yaḥ paśyet phalābhāvāt, yathā dhenuḥ api gauḥ agauḥ ucyate kṣīrākhyaṃ phalaṃ na prayacchati iti, tadvat. tathā nityākaraṇe tu akarmaṇi karma yaḥ paśyet narakādipratyavāyaphalaṃ prayacchati iti.",
               "naitat yuktaṃ vyākhyānam, evaṃ jñānāt aśubhāt mokṣānupapatteḥ, “yad jñātvā mokṣyase'śubhāt” iti bhagavatā uktaṃ vacanaṃ bādhyeta. katham? nityānām anuṣṭhānāt aśubhāt syānnāma mokṣaṇaṃ, na tu teṣāṃ phalābhāvajñānāt. na hi nityānāṃ phalābhāvajñānaṃ aśubhamuktiphalatvena coditaṃ, nityakarmajñānaṃ vā. na ca bhagavatā ihaiva uktam. etena akarmaṇi karmadarśanaṃ pratyuktam. na hi akarmaṇi “karmeti” darśanaṃ kartavyatayā iha codyate, nityasya tu kartavyatāmātram. na ca “akaraṇāt nityasya pratyavāyo bhavati” iti vijñānāt kiñcit phalaṃ syāt. nāpi nityākaraṇaṃ jñeyatvena coditam. nāpi “karma akarma” iti mithyādarśanāt aśubhāt mokṣaṇam, buddhimattvam, yuktatā, kṛtsnakarmakṛttvādi ca phalam upapadyate, stutirvā. mithyājñānameva hi sākṣāt aśubhasvarūpaṃ, kutaḥ anyasmāt aśubhāt mokṣaṇam? na hi tamaḥ tamasaḥ nivartakaṃ bhavati.",
               "nanu karmaṇi yat akarmadarśanam akarmaṇi vā karmadarśanaṃ na tat mithyājñānam, kiṃ tarhi? gauṇaṃ phalabhāvābhāvanimittam – na, karmākarma vijñānādapi gauṇāt phalāśravaṇāt. nāpi śrutahānyaśrutakalpanāyāṃ kaścidviśeṣo'palabhyate. svaśabdenāpi śakyaṃ vaktuṃ “nityakarmaṇāṃ phalaṃ nāsti. akaraṇācca teṣāṃ narakapātaḥ syāt” iti. tatra vyājena paravyāmoharūpeṇa “karmaṇyakarma yaḥ paśyet” ityādinā kim? tatraivaṃ vyācakṣāṇena bhagavatoktaṃ vākyaṃ lokavyāmohārtham iti vyaktaṃ kalpitaṃ syāt. na ca etat chadmarūpeṇa vākyena rakṣaṇīyaṃ vastuḥ nāpi śabdāntareṇa punaḥ punaḥ ucyamānaṃ subodhaṃ syāt ityevaṃ vaktuṃ yuktam. “karmaṇyevādhikāraste” (2.47) ityatra hi sphuṭataraḥ uktaḥ arthaḥ na punaḥ vaktavyaḥ bhavati. sarvatra ca praśastaṃ boddhavyaṃ ca kartavyameva, na niṣprayojanaṃ boddhavyam ityucyate. na ca mithyājñānaṃ boddhavyaṃ bhavati, tatpratyupasthāpitaṃ vā vastvā bhāsam.",
               "nāpi nityānām akaraṇāt abhāvāt pratyavāyabhāvotpattiḥ,“nāsato vidyate bhāvaḥ” (2.16) iti, “kathamasataḥ sajjāyeta” (chāṃ.u.6.2.2) iti ca darśitam asataḥ sajjanmapratiṣedhāt. asataḥ sadutpattiṃ bruvatā asadeva sad bhavet sacca asadbhavet iti uktaṃ syāt. tacca ayuktam, sarvapramāṇavirodhāt. na ca niṣphalaṃ vidadhyāt karma śāstram, duḥkhasvarūpatvāt, duḥkhasya ca buddhipūrvakatayā, kāryatvānupapatteḥ. tadakaraṇe ca narakapātābhyupagamāt anarthāyaiva ubhayathāpi karaṇe akaraṇe ca śāstraṃ niṣphalaṃ kalpitaṃ syāt. svābhyupagamavirodhaśca – “nityaṃ niṣphalaṃ karme”ti abhyupagamya “mokṣaphalāya” iti bruvataḥ. tasmāt yathāśruta eva arthaḥ “karmaṇyakarma” ityādeḥ. tathā ca vyākhyātaḥ asmābhiḥ ślokaḥ.",
           ]),
        _v([
            "yasya sarve samārambhāḥ kāmasaṅkalpavarjitāḥ |",
            "jñānāgnidagdhakarmāṇaṃ tamāhuḥ paṇḍitaṃ budhāḥ",
        ], "|| 19 ||",
           "He whose undertakings are all free from desire and its intentions, whose actions are burnt up in the fire of knowledge — him the wise call learned.",
           bhashya=[
               {"text": "tadetat karmaṇi akarmādi darśanaṃ stūyate–", "intro": True},
               "yasyeti – yasya yathoktadarśinaḥ, sarve yāvantaḥ samārambhāḥ sarvāṇi, karmāṇi, samārabhyante iti samārambhāḥ, kāmasaṅkalpavarjitāḥ kāmaiḥ tatkāraṇaiḥ ca saṅkalpaiḥ varjitāḥ, mudhaiva ceṣṭāmātrāḥ anuṣṭhīyante, pravṛttena cet lokasaṅgrahārthaṃ, nivṛttena cet jīvanamātrārthaṃ, taṃ jñānāgnidagdhakarmāṇaṃ, karmādau akarmādidarśanaṃ jñānaṃ, tadeva agniḥ, tena jñānāgninā dagdhāni śubhāśubhalakṣaṇāni karmāṇi yasya tam, āhuḥ paramārthataḥ, paṇḍitaṃ, budhāḥ brahmavidaḥ.",
           ]),
        _v([
            "tyaktvā karmaphalāsaṅgaṃ nityatṛpto nirāśrayaḥ |",
            "karmaṇyabhipravṛtto'pi naiva kiñcitkaroti saḥ",
        ], "|| 20 ||",
           "Having given up attachment to the fruit of action, ever content and dependent on nothing, he does nothing at all, though fully engaged in action.",
           bhashya=[
               {"text": "yastu karmādau akarmādidarśī saḥ akarmādidarśanāt eva niṣkarmā sannyāsī jīvanamātrārtha ceṣṭaḥ san karmaṇi na pravartate. yadyapi prāk vivekataḥ pravṛttaḥ. yaḥ tu prārabdhakarmā san uttarakālam utpannātmasamyag darśanaḥ syāt saḥ sarvakarmaṇi prayojanam apaśyan sasādhanaṃ karma parityajatyeva. saḥ kutaścit nimittāt karma parityāgāsambhave sati karmaṇi tatphale ca saṅgarahitatayā, svaprayojanābhāvāt lokasaṅgrahārthaṃ pūrvavat karmaṇi pravṛttaḥ api naiva kiñcit karoti, jñānāgnidagdhakarmatvāt, tadīyaṃ karma akarmaiva sampadyate ityetam arthaṃ darśayan āha–", "intro": True},
               "tyaktveti : tyaktvā karmasu abhimānaṃ phalāsaṅgaṃ ca yathoktena jñānena, nityatṛptaḥ nirākāṅkṣaḥ viṣayeṣu ityarthaḥ – nirāśrayaḥ āśrayarahitaḥ āśrayaḥ nāma yat āśritya puruṣārthaṃ sisādhayiṣati. dṛṣṭādṛṣṭeṣṭaphalasādhanāśrayarahitaḥ ityarthaḥ. viduṣā kriyamāṇaṃ karma paramārthataḥ akarmaiva, tasya niṣkriyātmadarśanasampannatvāt. tena evambhūtena prayojanābhāvāt sasādhanaṃ karmaparityaktavyam eva iti prāpte tataḥ nirgamāsambhavāt, lokasaṅgrahacikīrṣayā, śiṣṭavigarhaṇāparijihīrṣayā vā pūrvavat karmaṇi abhipravṛttaḥ api niṣkriyātma darśanasampannatvāt naiva kiñcit karoti saḥ.",
           ]),
        _v([
            "nirāśīryatacittātmā tyaktasarvaparigrahaḥ |",
            "śārīraṃ kevalaṃ karma kurvannāpnoti kilbiṣam",
        ], "|| 21 ||",
           "Without craving, with mind and self restrained, giving up all possessions, doing only bodily action, he incurs no sin.",
           bhashya=[
               {"text": "yaḥ punaḥ pūrvokta viparītaḥ prāgeva karmārambhāt brahmaṇi sarvāntare pratyagātma niṣkriye sañjātātmadarśanaḥ saḥ dṛṣṭādṛṣṭeṣṭaviṣayāśīrvivarjitatayā dṛṣṭādṛṣṭārthe karmaṇi prayojanam apaśyan sasādhanaṃ karma sannyasya śarīrayātrāmātraceṣṭaḥ yatiḥ jñānaniṣṭhaḥ mucyate ityetam arthaṃ darśayitum āha–", "intro": True},
               "niriti : nirāśīḥ nirgatāḥ āśiṣaḥ yasmāt saḥ nirāśīḥ, yata cittātmā cittam antaḥkaraṇam, ātmā bāhyaḥ kāryakaraṇasaṅghātaḥ, tau, ubhau api yatau saṃyatau yena saḥ, yatacittātmā, tyaktasarvaparigrahaḥ – tyaktaḥ sarvaḥ parigrahaḥ yena saḥ tyakta sarvaḥ parigrahaḥ śārīram śarīrasthitimātraprayojanam, kevalam, tatrāpi abhimānavarjitam, karma kurvan na āpnoti na prāpnoti kilbiṣam pāpaṃ aniṣṭarūpaṃ dharmaṃ ca. dharmo'pi mumukṣoḥ kilbiṣameva, bandhāpādakatvāt, tasmāt tābhyāṃ muktaḥ bhavati saṃsāramuktaḥ bhavatītyarthaḥ.",
               "(kiñca) “śārīraṃ kevalaṃ karma” ityatra kiṃ śarīra nirvartyaṃ śārīraṃ karma abhipretam? āhosvit śarīrasthitimātraprayojanaṃ śārīraṃ karma iti? kiṃ cātaḥ yadi śarīra nirvartyaṃ śārīraṃ karma, yadi vā śarīra sthitimātraprayojanaṃ śārīram iti? ucyateyadā śarīra nirvartyaṃ karma śārīraṃ abhipretaṃ syāt tadā dṛṣṭādṛṣṭaprayojanaṃ karma pratiṣiddhamapi śarīreṇa kurvan na āpnoti kilbiṣam iti bruvataḥ viruddhābhidhānaṃ prasajyeta. śāstrīyaṃ ca karma dṛṣṭādṛṣṭa prayojanaṃ śarīreṇa kurvan iti viśeṣaṇāt kevala śabda prayogācca vāṅmanasanirvartyaṃ karma vidhipratiṣedhaviṣayaṃ dharmādharmaśabdavācyaṃ kurvan nāpnoti kilbiṣam ityapi bruvataḥ aprāpta pratiṣedhaprasaṅgaḥ “śārīraṃ karma kurvan” iti viśeṣaṇāt kevalaśabdaprayogāt ca vāṅmanasābhyāṃ nirvartya karma vidhipratiṣedhaviṣayaṃ dharmādharmaśabdavācyaṃ kurvan prāpnoti kilbiṣaṃ ityuktaṃ syāt. tatrāpi vāṅmanasābhyāṃ vihitānuṣṭhāna pakṣe kilbiṣa prāptivacanaṃ viruddham āpadyeta. pratiṣiddha sevāpakṣe'pi bhūtārthānuvādamātraṃ anarthakaṃ syāt. yadā tu śarīrasthitimātraprayojanaṃ śārīraṃ karma abhipretaṃ bhavet, tadā dṛṣṭādṛṣṭaprayojanaṃ karma vidhipratiṣedhagamyaṃ śarīra vāṅmano nirvartyam anyat akurvan taireva śarīrādibhiḥ śarīrasthitimātraprayojanaṃ kevalaśabda– prayogāt “ahaṃ karomi” iti abhimāna varjitaḥ śarīrādi ceṣṭāmātraṃ lokadṛṣṭyā kurvan na āpnoti kilbiṣam. evambhūtasya pāpaśabdavācya kilbiṣaprāptyasambhavāt, kilbiṣaṃ saṃsāraṃ na prāpnoti, jñānāgnidagdhasarvakarmatvāt, apratibandhena mucyate eva iti pūrvokta samyagdarśanaphalānuvādaḥ eva eṣaḥ. evaṃ “śārīraṃ kevalaṃ karma” ityasya arthaparigrahe niravadyaṃ bhavati.",
           ]),
        _v([
            "yadṛcchālābhasantuṣṭo dvandvātīto vimatsaraḥ |",
            "samaḥ siddhāvasiddhau ca kṛtvā'pi na nibadhyate",
        ], "|| 22 ||",
           "Content with what comes by chance, beyond the pairs of opposites, free from envy, even in success and failure, he is not bound even when he acts.",
           bhashya=[
               {"text": "tyaktasarvaparigrahasya yateḥ annādeḥ śarīrasthitihetoḥ parigrahasya abhāvāt yācanādinā śarīrasthitikartavyatāyāṃ prāptāyāṃ – “ayācitamasaṅkluptamupapannaṃ yadṛcchayā” (bau.dha.sū.21.8.12, anugītā, 45.19) ityādinā vacanena anujñātaṃ yateḥ śarīrasthitihetoḥ annādeḥ prāptidvāram āviṣkurvan āha–", "intro": True},
               "yadṛcchā iti. yadṛcchālābhasantuṣṭaḥ aprārthitopanataḥ lābhaḥ yadṛcchālābhaḥ tena santuṣṭaḥ sañjātālampratyayaḥ dvandvātītaḥ dvandvaiḥ śītoṣṇādibhiḥ hanyamāno'pi aviṣaṇṇacittaḥ dvandvātītaḥ ucyate. vimatsaraḥ vigatamatsaraḥ nirvairabuddhiḥ samaḥ tulyaḥ yadṛcchālābhasya siddhau asiddhau ca. yaḥ evambhūto yatiḥ annādeḥ śarīrasthitihetoḥ lābhālābhayoḥ samaḥ harṣaviṣādavarjitaḥ karmādau akarmādidarśī yathābhūtātmadarśananiṣṭhaḥ san śarīrasthitimātraprayojane bhikṣāṭanādikarmaṇi śarīrādinirvartye “naiva kiñcit karomyaham”, “guṇā guṇeṣu vartante” ityevaṃ sadā samparicakṣāṇaḥ ātmanaḥ kartṛtvābhāvaṃ paśyan naiva kiñcit bhikṣāṭanādikaṃ karma karoti, lokavyavahārasāmānyadarśanena tu laukikaiḥ āropitakartṛtve bhikṣāṭanādau karmaṇi kartā bhavati. svānubhavena tu śāstrapramāṇajanitena akartā eva. saḥ evaṃ parādhyāropita kartṛtvaḥ śarīrasthitimātraprayojanaṃ bhikṣāṭanādikaṃ karma kṛtvā api na nibadhyate bandhahetoḥ karmaṇaḥ sahetukasya jñānāgninā dagdhatvāt iti uktānuvādaḥ eva eṣaḥ.",
           ]),
        _v([
            "gatasaṅgasya muktasya jñānāvasthitacetasaḥ |",
            "yajñāyācarataḥ karma samagraṃ pravilīyate",
        ], "|| 23 ||",
           "For one whose attachment has gone, who is free, whose mind is established in knowledge, who acts for the sake of sacrifice, all action dissolves entirely.",
           bhashya=[
               {"text": "“tyaktvā karmaphalāsaṅgam” (4.20) ityanena ślokena yaḥ prārabdhakarmā san yadā niṣkriya brahmātmadarśanasampannaḥ syāt tadā tasya ātmanaḥ kartṛkarmaprayojanābhāvadarśinaḥ karmaparityāge prāpte kutaścinnimittāt tadasambhave sati pūrvavat, tasmin karmaṇi abhipravṛttaḥ api “naiva kiñcitkaroti saḥ” (4.20) iti karmābhāvaḥ pradarśitaḥ. yasyaivaṃ karmābhāvaḥ darśitaḥ tasyaiva.", "intro": True},
               "gatasaṅgasya iti. gatasaṅgasya sarvataḥ nivṛttāsakteḥ muktasya nivṛtta dharmādharmādibandhanasya, jñānāvasthita cetasaḥ jñāne eva avasthitaṃ cetaḥ yasya saḥ ayaṃ jñānāvasthitacetāḥ tasya, yajñāya yajñanivṛttyartham ācarataḥ nivartayataḥ karma, samagraṃ saha agreṇa phalena vartate iti samagraṃ karma, tat samagraṃ pravilīyate vinaśyati ityarthaḥ.",
           ]),
        _v([
            "brahmārpaṇaṃ brahma haviḥ brahmāgnau brahmaṇā hutam |",
            "brahmaiva tena gantavyaṃ brahmakarmasamādhinā",
        ], "|| 24 ||",
           "The offering is Brahman, the oblation is Brahman, poured by Brahman into the fire that is Brahman; Brahman alone is to be reached by one absorbed in action that is Brahman.",
           bhashya=[
               {"text": "kasmāt punaḥ kāraṇāt kriyamāṇaṃ karma svakāryārambham akurvan samagraṃ pravilīyate iti? ucyate, yataḥ –", "intro": True},
               "brahmeti : brahma arpaṇam – yena karaṇena brahmavit haviḥ agnau arpayati tat brahmaiva iti paśyati. tasya ātmavyatirekeṇābhāvaṃ paśyati, yathā śuktikāyāṃ rajatābhāvaṃ paśyati. tat ucyate brahmārpaṇam iti. yathā yat rajataṃ tat śuktikā eva iti. “brahma arpaṇam” iti asamaste pade. yadarpaṇabuddhyā gṛhyate loke tadasya brahmavidaḥ brahmaiva ityarthaḥ. brahma haviḥ – tathā yat havirbuddhyā gṛhyamāṇaṃ tat brahmaiva asya. tathā brahmāgnau iti samastaṃ padam. agniḥ api brahma eva, yatra hūyate brahmaṇā kartrā, brahmaiva kartā ityarthaḥ yat tena hutaṃ havanakriyā tat brahma eva. yat tena gantavyaṃ phalaṃ tadapi brahmaiva. brahmakarmasamādhinā – brahmaiva karma brahmakarma. tasmin samādhiḥ yasya saḥ brahmakarmasamādhiḥ, tena brahmakarmasamādhinā brahma eva gantavyam.",
               "evaṃ lokasaṅgrahacikīrṣuṇāpi kriyamāṇaṃ karma paramārthataḥ akarma, brahmabuddhyupamṛditatvāt. nivṛttakarmaṇo'pi sarvakarmasannyāsinaḥ samyagdarśanastutyarthaṃ yajñatvasampādanaṃ jñānasya sutarāmupapadyate – yat arpaṇādi adhiyajñe prasiddhaṃ tat asya adhyātmaṃ brahmaiva paramārthadarśinaḥ iti. anyathā sarvasya brahmatve arpaṇādīnāmeva viśeṣataḥ brahmatvābhidhānam anarthakaṃ syāt. tasmāt brahmaiva idaṃ sarvam iti jānataḥ viduṣaḥ karmābhāvaḥ, kārakabuddhyabhāvācca. na hi kārakabuddhirahitaṃ yajñākhyaṃ karma dṛṣṭaṃ. sarvaṃ eva agnihotrādikaṃ karma śabdasamarpitadevatāviśeṣa sampradānādikārakabuddhimat kartrabhimānaphalābhisandhimat ca dṛṣṭam, na upamṛditakriyākārakaphalabhedabuddhimat kartṛtvābhimāna phalābhisandhirahitaṃ vā.",
               "idaṃ tu brahma buddhyupamṛditārpaṇādikārakakriyāphalabhedabuddhikarma. ataḥ akarmaiva tat. tathā ca darśitam – “karmaṇyakarma yaḥ paśyet” (4.18) “karmaṇyabhipravṛttopi naiva kiñcit karoti saḥ” (4.20), “guṇā guṇeṣu vartante” (6.28) “naiva kiñcitkaromīti yukto manyeta tattvavit” (5.8) ityādibhiḥ. tathā ca darśayan tatra tatra kriyākāraka phalabhedabuddhyupamardanaṃ karoti. dṛṣṭā ca kāmyāgnihotrādau kāmopamardena kāmyāgnihotrādihāniḥ. tathā matipūrvakā'matipūrvakādīnāṃ karmaṇāṃ kāryaviśeṣasya ārambhakatvaṃ dṛṣṭam. tathā ihāpi brahma buddhyupamṛdi'tārpaṇādikārakakriyā phalabhedabuddheḥ. bāhyaceṣṭāmātreṇa karma api viduṣaḥ akarma sampadyate. ataḥ uktaṃ “samagraṃ pravilīyate” (4.23) iti.",
               "atra kecidāhuḥ– yat brahma tat arpaṇādīni. brahmaiva kila arpaṇādinā pañcavidhena kārakātmanā vyavasthitaṃ sat tadeva karma karoti. tatra na arpaṇādibuddhiḥ nivartyate, kiṃ tu arpaṇādiṣu brahmabuddhiḥ ādhīyate, yathā pratimādau viṣṇvādibuddhiḥ yathā vā nāmādau brahmabuddhiḥ evamiti. (chāṃ u. 7.1.5)",
               "satyam evam api syāt yadi jñānayajñastutyarthaṃ prakaraṇaṃ na syāt. atra tu samyagdarśanaṃ jñānayajñaśabditam, anekān yajñaśabditān kriyāviśeṣān upanyasya “śreyān dravyamayādyajñāt jñānayajñaḥ” (4.33) iti jñānaṃ stauti. atra ca samartham idaṃ vacanaṃ “brahmārpaṇam” ityādi jñānasya yajñatva sampādane ityuktam. ye tu arpaṇādiṣu, pratimāyāṃ viṣṇnudṛṣṭivat, brahmadṛṣṭiḥ kṣipyate nāmādiṣu iva ca iti bruvate na teṣāṃ brahmavidyā uktā iha vivakṣitā syāt, arpaṇādiviṣayatvāt jñānasya.",
               "na ca dṛṣṭisampādanajñānena mokṣaphalaṃ prāpyate – “brahmaiva tena gantavyam” iti ca ucyate. viruddhaṃ ca samyagdarśanaṃ antareṇa mokṣaphalaṃ prāpyate iti. prakṛtavirodhaśca. samyagdarśanaṃ ca prakṛtaṃ “karmaṇyakarma yaḥ paśyet” (4.18) ityatra. ante ca samyagdarśanaṃ, tasyaiva upasaṃhārāt. “śreyān dravyamayādyajñāt jñānayajñaḥ” (4.33), “jñānaṃ labdhvā parāṃ śāntim” (4.39) ityādinā samyag darśanastutimeva kurvan upakṣīṇaḥ adhyāyaḥ – tatra akasmāt arpaṇādau brahmadṛṣṭiḥ aprakaraṇe, pratimāyām iva viṣṇudṛṣṭiḥ, ucyate iti anupapannam, tasmāt yathāvyākhyātārthaḥ eva ayaṃ ślokaḥ.",
           ]),
        _v([
            "daivamevāpare yajñaṃ yoginaḥ paryupāsate |",
            "brahmāgnāvapare yajñaṃ yajñenaivopajuhvati",
        ], "|| 25 ||",
           "Some yogins offer sacrifice to the gods alone; others offer sacrifice by sacrifice itself into the fire of Brahman.",
           bhashya=[
               {"text": "tatrādhunā samyagdarśanasya yajñatvaṃ sampādya tat stutyartham anye'pi yajñā upakṣipyante daivamevetyādinā –", "intro": True},
               "daivamiti. daivam eva – devāḥ ijyante yena yajñena asau daivaḥ yajñaḥ. tam eva apare yajñaṃ, yoginaḥ karmiṇaḥ paryupāsate, kurvanti ityarthaḥ. brahmāgnau – “satyaṃ jñānamanantaṃ brahma” (tai.u. 2.1) “vijñānamānandaṃ brahma” (bṛ.u.3.9.28) “yatsākṣādaparokṣāt brahma ya ātmā sarvāntaraḥ (bṛ.u. 3.4.1) ityādivacanoktam, “aśanāyāpipāsādi sarvasaṃsāradharmavarjitam” (bṛ.u. 3.5.1) “neti neti” (bṛ.u.4.4.22) itara nirastāśeṣaviśeṣaṃ brahmaśabdena ucyate. brahma ca tat agniśca saḥ homādhikaraṇatvavivakṣayā brahma agniḥ tasmin brahmāgnau, apare anye brahmavidaḥ yajñam, yajñaśabdavācyaḥ ātmā ātmanāmasu yajñaśabdasya pāṭhāt, tam ātmānaṃ yajñaṃ, paramārthataḥ parameva brahma santaṃ buddhyādyupādhisaṃyuktam, adhyasta sarvopādhidharmakam, āhutirūpaṃ, yajñenaiva ātmanaiva uktalakṣaṇena, upajuhvati prakṣipanti, sopādhikasya ātmanaḥ nirupādhikena parabrahmasvarūpeṇaiva yat darśanaṃ saḥ tasmin homaḥ taṃ kurvanti brahmātmaikatva darśananiṣṭhāḥ sannyāsinaḥ ityarthaḥ.",
           ]),
        _v([
            "śrotrādīnīndriyāṇyanye saṃyamāgniṣu juhvati |",
            "śabdādīnviṣayānanya indriyāgniṣu juhvati",
        ], "|| 26 ||",
           "Some offer hearing and the other senses into the fires of restraint; others offer sound and the other objects into the fires of the senses.",
           bhashya=[
               {"text": "saḥ ayaṃ samyagdarśanalakṣaṇaḥ yajñaḥ daivayajñādiṣu yajñeṣu upakṣipyate “brahmārpaṇam” (4.24) ityādi ślokaiḥ prastutaḥ “śreyān dravyamayādyajñād jñānayajñaḥ parantapa” (4.33) ityādinā stutyartham –", "intro": True},
               "śrotrādīnīti – śrotrādīni indriyāṇi, anye yoginaḥ, saṃyamāgniṣu, pratīndriyaṃ saṃyamaḥ bhidyate iti bahuvacanam, saṃyamāḥ eva agnayaḥ, teṣu juhvati indriyasaṃyamam eva kurvanti ityarthaḥ. śabdādīnviṣayānanye indriyāgniṣu – indriyāṇyeva agnayaḥ teṣu indriyāgniṣu juhvati – śrotrādibhiḥ aviruddhaviṣayagrahaṇaṃ homaṃ manyante. kiñca –",
           ]),
        _v([
            "sarvāṇīndriyakarmāṇi prāṇakarmāṇi cāpare |",
            "ātmasaṃyamayogāgnau juhvati jñānadīpite",
        ], "|| 27 ||",
           "Others offer all the actions of the senses and the actions of the breath into the fire of the yoga of self-restraint, kindled by knowledge.",
           bhashya=[
               "sarvāṇīti – sarvāṇi indriyakarmāṇi indriyāṇāṃ karmāṇi, tathā prāṇakarmāṇi prāṇaḥ vāyuḥ ādhyātmikaḥ tatkarmāṇi akuñcana prasāraṇādīni tāni ca, apare, ātma saṃyamayogāgnau – ātmani saṃyamaḥ ātmasaṃyamaḥ sa eva yogāgniḥ, tasmin ātma saṃyamayogāgnau juhvati prakṣipanti, jñānadīpite, sneheneva pradīpe vivekavijñānena ujjvalabhāvam āpādite juhvati pravilāpayanti ityarthaḥ.",
           ]),
        _v([
            "dravyayajñāstapoyajñā yogayajñāstathā'pare |",
            "svādhyāyajñānayajñāśca yatayaḥ saṃśitavratāḥ",
        ], "|| 28 ||",
           "Some offer wealth, some austerity, some yoga as sacrifice; and others, ascetics of strict vows, offer study and knowledge.",
           bhashya=[
               "dravyeti – dravyayajñāḥ tīrtheṣu dravya viniyogaṃ yajñabuddhyā kurvanti ye te dravyayajñāḥ. tapoyajñāḥ tapaḥ yajñaḥ yeṣāṃ tapasvināṃ te tapoyajñāḥ. yogayajñāḥ – prāṇāyāma pratyāhārādilakṣaṇaḥ yogaḥ yajñaḥ yeṣāṃ te yogayajñāḥ. tathā apare svādhyāyajñānayajñāḥ ca – svādhyāyaḥ yathāvidhi ṛgādyabhyāsaḥ yajñaḥ yeṣāṃ te svādhyāyayajñāḥ. jñānayajñāḥ – jñānaṃ śāstrārthaparijñānaṃ yajñaḥ yeṣāṃ te jñānayajñāḥ ca, yatayaḥ yatanaśīlāḥ saṃśitavratāḥ samyak śitāni tanūkṛtāni, tīkṣīkṛtāni vratāni yeṣāṃ te saṃśitavratāḥ.",
           ]),
        _v([
            "apāne juhvati prāṇaṃ prāṇe'pānaṃ tathā'pare |",
            "prāṇāpānagatī ruddhvā prāṇāyāmaparāyaṇāḥ",
        ], "|| 29 ||",
           "Others, intent on control of the breath, offer the in-breath into the out-breath and the out-breath into the in-breath, restraining the course of both.",
           bhashya=[
               "apāne iti – apāne apānavṛttau – juhvati prakṣipanti. prāṇaṃ prāṇavṛttiṃ. pūrakākhyaṃ prāṇāyāmaṃ kurvanti ityarthaḥ. prāṇe apānaṃ tathā apare juhvati. recakākhyaṃ ca prāṇāyāmaṃ kurvanti ityetat. prāṇāpānagatī mukhanāsikābhyāṃ vāyoḥ nirgamanaṃ prāṇasya gatiḥ. tadviparyayeṇa adhaḥ gamanam apānasya gatiḥ prāṇāpānagatī ete (ke) ruddhvā nirudhya prāṇāyāmaparāyaṇāḥ prāṇāyāmatatparāḥ kumbhakākhyaṃ prāṇāyāmaṃ kurvanti ityarthaḥ.",
           ]),
        _v([
            "apare niyatāhārāḥ prāṇān prāṇeṣu juhvati |",
            "sarve'pyete yajñavido yajñakṣapitakalmaṣāḥ",
        ], "|| 30 ||",
           "Others, regulating their food, offer the breaths into the breaths. All of these know sacrifice, and their sins are destroyed by sacrifice.",
           bhashya=[
               "apare iti – apare niyatāhārāḥ, niyataḥ parimitaḥ āhāraḥ yeṣāṃ te niyatāhārāḥ santaḥ prāṇān vāyubhedān prāṇeṣu eva juhvati. yasya, yasya vāyoḥ jayaḥ kriyate itarān vāyubhedān tasmin tasmin juhvati. te tatra praviṣṭāḥ iva bhavanti. sarve'pi ete yajñavidaḥ yajñakṣapitakalmaṣāḥ – yajñaiḥ yathoktaiḥ kṣapitaḥ nāśitaḥ kalmaṣaḥ yeṣāṃ te yajñakṣapitakalmaṣāḥ. evaṃ yathoktān yajñān nirvartya –",
           ]),
        _v([
            "yajñaśiṣṭāmṛtabhujo yānti brahma sanātanam |",
            "nāyaṃ loko'styayajñasya kuto'nyaḥ kurusattama",
        ], "|| 31 ||",
           "Eating the nectar that remains from sacrifice, they reach the eternal Brahman. This world is not for one who does not sacrifice, still less the other, O best of the Kurus.",
           bhashya=[
               "yajña iti. yajñāśiṣṭāmṛtabhujaḥ – yajñānāṃ śiṣṭaṃ yajñaśiṣṭam. yajñaśiṣṭaṃ ca tat amṛtaṃ ca yajñaśiṣṭāmṛtam. tat bhuñjate iti yajñaśiṣṭāmṛtabhujaḥ. yathoktān yajñān kṛtvā tacchiṣṭena kālena yathāvidhicoditaṃ annam amṛtākhyaṃ bhuñjate iti yajñaśiṣṭāmṛtabhujaḥ. yānti gacchanti brahma sanātanaṃ cirantanaṃ mumukṣavaḥ cetnu kālātikramāpekṣayā iti sāmarthyāt gamyate. na ayaṃ lokaḥ sarvaprāṇisādhāraṇaḥ api asti yathoktānām yajñānāṃ ekaḥ api yajña yasya nāsti saḥ ayajñaḥ tasya, kutaḥ anyaḥ viśiṣṭasādhanasādhyaḥ, kurusattama.",
           ]),
        _v([
            "evaṃ bahuvidhā yajñā vitatā brahmaṇo mukhe |",
            "karmajān viddhi tān sarvānevaṃ jñātvā vimokṣyase",
        ], "|| 32 ||",
           "Thus sacrifices of many kinds are spread out in the mouth of the Veda. Know them all to be born of action; knowing this, you will be released.",
           bhashya=[
               "evamiti. evaṃ yathoktāḥ bahuvidhāḥ bahuprakārāḥ yajñāḥ vitatāḥ vistīrṇāḥ brahmaṇaḥ vedasya mukhe dvāre. vedadvāreṇa avagamyamānāḥ brahmaṇaḥ mukhe vitatāḥ ucyante. tadyathā “vāci hi prāṇān juhumaḥ” (ai.ā.3.2.6) ityādayaḥ. karmajān kāyikavācika mānasakarmodbhavān viddhitān sarvān anātmajān. nirvyāpāraḥ hi ātmā. ataḥ evaṃ jñātvā vimokṣyase aśubhāt. “na madvyāpārāḥ ete, nirvyāpāraḥ aham, udāsīnaḥ” ityevaṃ jñātvā asmāt samyagdarśanāt, mokṣyase aśubhāt saṃsārabandhanāt ityarthaḥ.",
           ]),
        _v([
            "śreyān dravyamayādyajñāt jñānayajñaḥ parantapa |",
            "sarvaṃ karmākhilaṃ pārtha jñāne parisamāpyate",
        ], "|| 33 ||",
           "Better than sacrifice with material things is the sacrifice of knowledge, O scorcher of foes; all action without exception, Pārtha, culminates in knowledge.",
           bhashya=[
               {"text": "“brahmārpaṇam” ityādi ślokena samyagdarśanasya yajñatvaṃ sampāditam, yajñāśca aneke upadiṣṭāḥ. taiḥ siddhapuruṣārthaprayojanaiḥ jñānaṃ stūyate. katham?", "intro": True},
               "śreyāniti – śreyān, dravyamayāt dravya sādhanasādhyāt yajñāt jñānayajñaḥ he parantapa. dravyamayo hi yajñaḥ phalasya ārambhakaḥ, jñānayajñaḥ na phalārambhakaḥ, ataḥ śreyān praśasyataraḥ. katham? yataḥ sarvaṃ karma samastam akhilam apratibaddhaṃ, pārtha, jñāne mokṣasādhane sarvataḥ samplutodakasthānīye parisamāpyate, antarbhavati ityarthaḥ. “yathā kṛtāya vijitāyādhareyāḥ saṃyantyevamenaṃ sarvaṃ tadabhisameti yatkiñcit prajāḥ sādhu kurvanti yastadveda yat sa veda” (chāṃ u. 4.1.4) iti śruteḥ.",
           ]),
        _v([
            "tadviddhi praṇipātena paripraśnena sevayā |",
            "upadekṣyanti te jñānaṃ jñāninastattvadarśinaḥ",
        ], "|| 34 ||",
           "Know it by prostrating, by questioning and by service. The wise who have seen the truth will teach you knowledge.",
           bhashya=[
               {"text": "tadetat viśiṣṭaṃ jñānaṃ kena prāpyate iti? ucyate–", "intro": True},
               "tadviddhīti – tat viddhi vijānīhi yena vidhinā prāpyate iti. ācāryān abhigamya, praṇipātena prakarṣeṇa nīcaiḥ patanaṃ praṇipātaḥ, dīrghanamaskāraḥ, tena “kathaṃ bandhaḥ?” “kathaṃ mokṣaḥ? kāvidyā? kā ca avidyā?” iti paripraśnena, sevayā guruśuśrūṣayā, evamādinā. praśrayeṇa āvarjitāḥ ācāryāḥ, upadekṣyanti kathayiṣyanti te jñānaṃ yathoktaviśeṣaṇam, jñāninaḥ. jñānavantaḥ api kecit yathāvat tattvadarśana śīlāḥ, apare nanu ataḥ viśinaṣṭi tattvadarśinaḥ iti. ye samyagdarśinaḥ taiḥ upadiṣṭaṃ jñānaṃ kāryakṣamaṃ bhavati, na itarat iti bhagavataḥ matam.",
           ]),
        _v([
            "yad jñātvā na punarmohamevaṃ yāsyasi pāṇḍava |",
            "yena bhūtānyaśeṣeṇa drakṣyasyātmanyatho mayi",
        ], "|| 35 ||",
           "Knowing it, you will not fall again into such delusion, Pāṇḍava; by it you will see all beings without remainder in the Self, and then in me.",
           bhashya=[
               {"text": "tathā ca sati idam api samarthaṃ vacanam –", "intro": True},
               "yaditi ḥ yat jñātvā, yat jñānaṃ taiḥ upadiṣṭam adhigamya prāpya, punaḥ bhūyaḥ moham, evam yathā idānīm mohaṃ gataḥ asi, punaḥ evaṃ na yāsyasi he pāṇḍava, kiṃ ca yena jñānena bhūtāni aśeṣeṇa, brahmādīni stambaparyantāni drakṣyasi sākṣāt ātmani pratyagātmani matsaṃsthāni. imāni bhūtāni iti, atho api mayi vāsudeve parameśvare ca imāni iti, kṣetrajñeśvaraikatvaṃ sarvopaniṣatprasiddhaṃ drakṣyasi ityarthaḥ",
           ]),
        _v([
            "api cedasi pāpebhyaḥ sarvebhyaḥ pāpakṛttamaḥ |",
            "sarvaṃ jñānaplavenaiva vṛjinaṃ santariṣyasi",
        ], "|| 36 ||",
           "Even if you are the most sinful of all sinners, you will cross over all wrongdoing by the raft of knowledge alone.",
           bhashya=[
               {"text": "kiṃ ca etasya jñānasya māhātmyam", "intro": True},
               "apīti – api cet asi, pāpebhyaḥ, pāpakṛdbhyaḥ, sarvebhyaḥ, atiśayena pāpakṛt pāpakṛttamaḥ, sarvaṃ, jñānaplavenaiva, jñānam eva plavaṃ kṛtvā, vṛjinaṃ vṛjinārṇavaṃ pāpaṃ, santariṣyasi. dharmaḥ api iha mumukṣoḥ pāpam ucyate.",
           ]),
        _v([
            "yathaidhāṃsi samiddho'gnirbhasmasātkuruterju'na |",
            "jñānāgniḥ sarvakarmāṇi bhasmasāt kurute tathā",
        ], "|| 37 ||",
           "As a kindled fire reduces its fuel to ashes, Arjuna, so the fire of knowledge reduces all actions to ashes.",
           bhashya=[
               {"text": "jñānaṃ kathaṃ nāśayati pāpam iti sadṛṣṭāntam ucyate –", "intro": True},
               "yatheti : yathā, edhāṃsi kāṣṭhāni, samiddhaḥ samyak iddhaḥ dīptaḥ, agniḥ, bhasmasāt bhasmībhāvaṃ, kurute arjuna, jñānameva agniḥ jñānāgniḥ sarvakarmāṇi bhasmasāt kurute tathā, nirbījīkaroti ityarthaḥ, na hi sākṣādeva jñānāgniḥ karmāṇi indhanavat bhasmīkartuṃ śaknoti. tasmāt samyagdarśanaṃ sarvakarmaṇāṃ nirbījatvakāraṇam ityabhiprāyaḥ. sāmarthyāt yena karmaṇā śarīraṃ ārabdhaṃ tat pravṛttaphalatvāt upabhogenaiva kṣīyate “tasya tāvadeva ciraṃ yāvanna vimokṣye'tha sampatsye” (chāṃ. u. 6.14.2) iti śruteḥ. ataḥ yāni apravṛttaphalāni jñānotpatteḥ prāk kṛtāni jñānasahabhāvīni ca atītāneka janmakṛtāni ca tānyeva bhasmasāt kurute.",
           ]),
        _v([
            "na hi jñānena sadṛśaṃ pavitramiha vidyate |",
            "tatsvayaṃ yogasaṃsiddhaḥ kālenātmani vindati",
        ], "|| 38 ||",
           "There is no purifier here equal to knowledge. One perfected in yoga finds it in himself in time.",
           bhashya=[
               "na hīti : na hi jñānena sadṛśaṃ tulyaṃ pavitraṃ pāvanaṃ śuddhikaram, iha vidyate. tat jñānaṃ svayameva yogasaṃsiddhaḥ yogena karmayogena samādhiyogena ca saṃsiddhaḥ saṃskṛtaḥ yogyatām āpannaḥ san mumukṣuḥ kālena mahatā ātmani vindati labhate ityarthaḥ.",
           ]),
        _v([
            "śraddhāvān labhate jñānaṃ tatparaḥ saṃyatendriyaḥ |",
            "jñānaṃ labdhvā parāṃ śāntimacireṇādhigacchati",
        ], "|| 39 ||",
           "The man of faith, devoted to it, with senses controlled, gains knowledge; having gained knowledge, he soon attains supreme peace.",
           bhashya=[
               {"text": "yena ekāntena jñānaprāptiḥ bhavati saḥ upāyaḥ upadiśyate –", "intro": True},
               "śraddhāvāniti : śraddhāvān śraddhāluḥ labhate jñānam. śraddhālutve'pi bhavati kaścit mandaprasthānaḥ, ataḥ āha – tatparaḥ gurūpasadanādau abhiyuktaḥ jñānalabdhyupāye śraddhāvān, tatparo'pi ajitendriyaḥ syāt ityataḥ āha–saṃyatendriyaḥ, saṃyatāni viṣayebhyaḥ nivartitāni yasya indriyāṇi saḥ saṃyatendriyaḥ. yaḥ evaṃ bhūtaḥ śraddhāvān tatparaḥ, saṃyatendriyaśca saḥ avaśyaṃ jñānaṃ labhate. praṇipātādistu bāhyaḥ anaikāntikaḥ api bhavati, māyāvitvādi sambhavāt. na tu tat śraddhāvattvādau, ita ekāntataḥ jñānalabdhyupāyaḥ.",
               "kiṃ punaḥ jñānalābhāt syāt iti ucyate – jñānaṃ labdhvā parāṃ mokṣākhyāṃ śāntim uparatiṃ acireṇa kṣiprameva adhigacchati. samyagdarśanāt kṣipram eva mokṣaḥ bhavati iti sarvaśāstranyāya prasiddhaḥ suniścitaḥ arthaḥ.",
           ]),
        _v([
            "ajñaścāśraddadhānaśca saṃśayātmā vinaśyati |",
            "nāyaṃ loko'sti na paro na sukhaṃ saṃśayātmanaḥ",
        ], "|| 40 ||",
           "The ignorant, the faithless and the doubting perish. For the doubting self there is neither this world, nor the next, nor happiness.",
           bhashya=[
               {"text": "atra saṃśayaḥ na kartavyaḥ, pāpiṣṭho hi saṃśayaḥ, katham? ucyate–", "intro": True},
               "ajñaśceti : ajñaḥ ca anātmajñaḥ, aśraddadhānaḥ, ca, guruvākya śāstreṣu aviśvāsavān ca saṃśayātmā ca, saṃśayacittaśca vinaśyati. ajñāśraddadhānau yadyapi vinaśyataḥ tathāpi na tathā yathā saṃśayātmā. sa tu pāpiṣṭhaḥ sarveṣām – katham? nāyaṃ sādhāraṇaḥ api lokaḥ asti. tathā na paraḥ lokaḥ. na sukham, tatrāpi saṃśayotpatteḥ, saṃśayātmanaḥ saṃśayacittasya. tasmāt saṃśayaḥ na kartavyaḥ kasmāt.",
           ]),
        _v([
            "yogasannyastakarmāṇaṃ jñānasañchinnasaṃśayam |",
            "ātmavantaṃ na karmāṇi nibadhnanti dhanañjaya",
        ], "|| 41 ||",
           "Actions do not bind one who has renounced actions through yoga, whose doubts are cut by knowledge, who is possessed of the Self, O Dhanañjaya.",
           bhashya=[
               "yogeti : yogasannyastakarmāṇam – paramārthadarśanalakṣaṇena yogena sannyastāni karmāṇi yena paramārthadarśinā dharmādharmākhyāni taṃ yogasannyastakarmāṇam. kathaṃ yogasannyastakarmā ityāha – jñānasañchinnasaṃśayaṃ jñānena ātmeśvaraikatvadarśanalakṣaṇena sañchinnaḥ saṃśayaḥ yasya saḥ jñānasañchinnasaṃśayaḥ, yaḥ evaṃ yogasannyastakarmā tam, ātmavantam apramattaṃ, guṇaceṣṭārūpeṇa dṛṣṭāni karmāṇi na nibadhnanti aniṣṭādirūpaṃ phalaṃ na ārabhante, he dhanañjaya.",
           ]),
        _v([
            "tasmādajñānasambhūtaṃ hṛtsthaṃ jñānāsinā'tmanaḥ |",
            "chittvainaṃ saṃśayaṃ yogamātiṣṭhottiṣṭha bhārata",
        ], "|| 42 ||",
           "Therefore, cutting with the sword of knowledge this doubt of yours, born of ignorance and lodged in the heart, resort to yoga; arise, O Bhārata!",
           bhashya=[
               {"text": "yasmāt karmayogānuṣṭhānāt aśuddhikṣayahetukajñānasañchinnasaṃśayaḥ na nibadhyate karmabhiḥ jñānāgnidagdhakarmatvāt eva, yasmāt ca jñānakarmānuṣṭhānaviṣaye saṃśayavān vinaśyati –", "intro": True},
               "tasmāditi : tasmāt pāpiṣṭham ajñānasambhūtam ajñānāt avivekato jātaṃ, hṛtsthaṃ hṛdi buddhau sthitaṃ, jñānāsinā – śokamohādidoṣaharaṃ samyagdarśanaṃ jñānaṃ, tadeva asiḥ khaḍgaḥ tena jñānāsinā, ātmanaḥ svasya, ātma viṣayatvāt saṃśayasya, na hi parasya saṃśayaḥ apareṇa chettavyatāṃ prāptaḥ, yena svasya iti viśeṣyate. ataḥ ātmaviṣayaḥ api svasya eva bhavati. chittvā enaṃ saṃśayaṃ svavināśahetubhūtaṃ, yogaṃ samyagdarśanopāyaṃ karmānuṣṭhānam ātiṣṭha kurvityarthaḥ, uttiṣṭha ca idānīṃ yuddhāya bhārata iti.",
           ]),
        "ornament",
        {"colophon": "iti śrī mahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītā– sūpaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjuna saṃvāde jñānakarmasannyāsayogo nāma caturtho'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the fourth chapter, Jñānakarmasannyāsa Yoga."},
        {"colophon": "iti śrīmatparamahaṃsa parivrājakācārya govindabhagavatpūjyapādaśiṣya śrīmacchajkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye jñānakarma sannyāsayogo nāma caturtho'dhyāyaḥ", "gloss": "Thus ends the fourth chapter, Jñānakarmasannyāsa Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
