# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 10 (Vibhūti Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 10 · Vibhūti Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 10",
    "h1": "Bhagavad Gītā · Chapter 10",
    "subtitle": "Vibhūti Yoga · the divine manifestations · with Śaṅkara's bhāṣya",
    "note": "Kṛṣṇa declares himself the source of all, and at Arjuna's request names his foremost manifestations (vibhūti) among gods, sages, beings and things — concluding that the whole universe is upheld by a single fragment of himself.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 9', 'gita-bhashya-09-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 11 ›', 'gita-bhashya-11-iast.html')],
    "sections": [
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "bhūya eva mahābāho śṛṇu me paramaṃ vacaḥ |",
            "yatte'haṃ prīyamāṇāya vakṣyāmi hitakāmyayā",
        ], "|| 1 ||",
           "The Blessed Lord said: Hear once more, mighty-armed one, my supreme word, which I will speak to you, who delight in it, out of desire for your good.",
           bhashya=[
               {"text": "saptame adhyāye bhagavataḥ tattvaṃ vibhūtayaśca prakāśitāḥ, navame ca. atha idānīṃ yeṣu yeṣu bhāveṣu cintyaḥ bhagavān te te bhāvāḥ vaktavyāḥ. tattvaṃ ca bhagavataḥ vaktavyam uktamapi, durvijñeyatvāt ityataḥ.", "intro": True},
               "bhūyaḥ iti – bhūyaḥ eva punaḥ, he mahābāho, śṛṇu, me madīyaṃ paramaṃ prakṛṣṭaṃ niratiśayavastunaḥ prakāśakaṃ, vacaḥ vākyaṃ, yat paramaṃ, te tubhyaṃ, prīyamāṇāya, madvacanāt prīyase tvam atīva amṛtamiva piban, tataḥ vakṣyāmi hitakāmyayā hitecchayā.",
           ]),
        _v([
            "na me viduḥ suragaṇāḥ prabhavaṃ na maharṣayaḥ |",
            "ahamādirhi devānāṃ maharṣīṇāṃ ca sarvaśaḥ",
        ], "|| 2 ||",
           "Neither the hosts of gods nor the great seers know my origin; for I am the source of the gods and of the great seers in every way.",
           bhashya=[
               {"text": "kimarthaṃ ahaṃ vakṣyāmi iti? ataḥ āha –", "intro": True},
               "na me viduḥ na jānanti suragaṇāḥ brahmādayaḥ, kiṃ te na viduḥ? mama prabhavaṃ prabhāvaṃ prabhuśaktyatiśayam, athavā prabhavaṃ prabhavanam utpattiṃ, nāpi maharṣayaḥ bhṛgvādayaḥ viduḥ. kasmāt te na viduḥ. kasmāt te na viduḥ. iti ucyate – aham ādiḥ kāraṇaṃ hi yasmāt devānāṃ maharṣīṇāṃ ca sarvaśaḥ sarvaprakāraiḥ –",
           ]),
        _v([
            "yo māmajamanādiṃ ca vetti lokamaheśvaram |",
            "asammūḍhaḥ sa martyeṣu sarvapāpaiḥ pramucyate",
        ], "|| 3 ||",
           "He who knows me as unborn and without beginning, the great lord of the worlds, is undeluded among mortals and is freed from all sins.",
           bhashya=[
               "yaḥ mām ajam anādiṃ ca, yasmāt aham ādiḥ devānāṃ maharṣīṇāṃ, na mama anyaḥ ādiḥ vidyate, ataḥ aham ajaḥ anādiḥ ca, anāditvam ajatve hetuḥ, taṃ mām ajam anādiṃ ca yaḥ vetti vijānāti lokamaheśvaraṃ lokānāṃ mahāntam īśvaraṃ (turīyam ajñānatatkāryavarjitam) asammūḍhaḥ sammohavarjitaḥ saḥ martyeṣu manuṣyeṣu sarvapāpaiḥ sarvaiḥ pāpaiḥ matipūrvāmatipūrvakṛtaiḥ pramucyate pramokṣyate.",
           ]),
        _v([
            "buddhirjñānamasammohaḥ kṣamā satyaṃ damaḥ śamaḥ |",
            "sukhaṃ duḥkhaṃ bhavo'bhāvo bhayaṃ cābhayameva ca",
        ], "|| 4 ||",
           "Understanding, knowledge, freedom from delusion, patience, truthfulness, self-restraint and calm; pleasure and pain, being and non-being, fear and fearlessness;",
           bhashya=[
               {"text": "itaśca ahaṃ maheśvaraḥ lokānām –", "intro": True},
               "buddhiḥ antaḥkaraṇasya sūkṣmādyarthāvabodhanasāmarthyam. tadvantaṃ buddhimāniti hi vadanti. jñānam ātmādipadārthānām avabodhaḥ. asammohaḥ pratyutpanneṣu boddhavyeṣu vivekapūrvikā pravṛttiḥ. kṣamā ākruṣṭasya tāḍitasya vā avikṛtacittatā. satyaṃ yathādṛṣṭasya yathāśrutasya vā ātmānubhavasya parabuddhi saṅkrāntaye tathaiva uccāryamāṇā vāk satyam ucyate. damaḥ bāhyendriyopaśamaḥ. śamaḥ antaḥkaraṇasya upaśamaḥ. sukham āhlādaḥ. duḥkhaṃ santāpaḥ. bhavaḥ udbhavaḥ. abhāvaḥ tadviparyayaḥ. bhayaṃ ca trāsaḥ abhayam eva ca tadviparītam.",
           ]),
        _v([
            "ahiṃsā samatā tuṣṭistapo dānaṃ yaśo'yaśaḥ |",
            "bhavanti bhāvā bhūtānāṃ matta eva pṛthagvidhāḥ",
        ], "|| 5 ||",
           "non-violence, equanimity, contentment, austerity, generosity, fame and infamy — these various states of beings arise from me alone.",
           bhashya=[
               "ahiṃseti – ahiṃsā apīḍā prāṇinām. samatā samacittatā. tuṣṭiḥ santoṣaḥ paryāptabuddhiḥ lābheṣu. tapaḥ indriyasaṃyamapūrvakaṃ śarīrapīḍanam. dānaṃ yathāśakti saṃvibhāgaḥ. yaśaḥ dharmanimittā kīrtiḥ. ayaśastu adharmanimittā akīrtiḥ. bhavanti bhāvāḥ yathoktāḥ buddhyādayaḥ, bhūtānāṃ prāṇināṃ, matta eva īśvarāt, pṛthagvidhāḥ nānāvidhāḥ svakarmānu rūpeṇa. kiñca –",
           ]),
        _v([
            "maharṣayaḥ sapta pūrve catvāro manavastathā |",
            "madbhāvā mānasā jātā yeṣāṃ loka imāḥ prajāḥ",
        ], "|| 6 ||",
           "The seven great seers of old and the four Manus, from whom these creatures in the world descend, were born of my mind and share my nature.",
           bhashya=[
               "maharṣayaḥ sapta bhṛgvādayaḥ, pūrve atītakālasambandhinaḥ, catvāraḥ manavaḥ tathā sāvarṇāḥ iti prasiddhāḥ. te ca, madbhāvāḥ madgatabhāvanāḥ, vaiṣṇavena sāmarthyena upetāḥ mānasāḥ manasaiva utpāditāḥ mayā jātāḥ utpannāḥ, yeṣāṃ manūnāṃ maharṣīṇāṃ ca sṛṣṭiḥ loke imāḥ sthāvarajaṅgamalakṣaṇāḥ prajāḥ.",
           ]),
        _v([
            "etāṃ vibhūtiṃ yogaṃ ca mama yo vetti tattvataḥ |",
            "so'vikampena yogena yujyate nātra saṃśayaḥ",
        ], "|| 7 ||",
           "He who knows in truth this glory and this yoga of mine is joined to me in unwavering yoga; of this there is no doubt.",
           bhashya=[
               "etāmiti – etāṃ yathoktāṃ, vibhūtiṃ vistāraṃ, yogaṃ ca yuktiṃ ca ātmanaḥ ghaṭanam, athavā yogaiśvarya sāmarthyaṃ, sarvajñatvaṃ yogajaṃ yogaḥ ityucyate. mama madīyaṃ, yaḥ vetti tattvataḥ tattvena, yathāvat ityetat. saḥ, avikampena apravicalitena, yogena samyagdarśana sthairyalakṣaṇena, yujyate sambadhyate. na atra saṃśayaḥ na asmin arthe saṃśayaḥ asti.",
           ]),
        _v([
            "ahaṃ sarvasya prabhavaḥ mattassarvaṃ pravartate |",
            "iti matvā bhajante māṃ budhā bhāvasamanvitāḥ",
        ], "|| 8 ||",
           "I am the origin of all; from me everything proceeds. Knowing this, the wise worship me, filled with devotion.",
           bhashya=[
               {"text": "kīdṛśena avikampena yogena yujyate iti? ucyate –", "intro": True},
               "ahaṃ paraṃ brahma vāsudevākhyaṃ, sarvasya jagataḥ prabhavaḥ utpattiḥ. mattaḥ eva sthitināśakriyāphalopabhogalakṣaṇaṃ vikriyārūpaṃ sarvaṃ jagat pravartate ityevaṃ matvā, bhajante, sevante, māṃ, budhāḥ avagataparamārthatattvāḥ bhāvasamanvitāḥ bhāvaḥ bhāvanā, paramārthatattvā bhiniveśaḥ, tena samanvitāḥ saṃyuktā ityarthaḥ. kiñca –",
           ]),
        _v([
            "maccittā madgataprāṇā bodhayantaḥ parasparam |",
            "kathayantaśca māṃ nityaṃ tuṣyanti ca ramanti ca",
        ], "|| 9 ||",
           "With their minds on me, their lives given to me, enlightening one another and always speaking of me, they are content and rejoice.",
           bhashya=[
               "maccittā iti – mayi cittaṃ yeṣāṃ te maccittāḥ, madgataprāṇāḥ māṃ gatāḥ prāptāḥ cakṣurādayaḥ prāṇāḥ yeṣāṃ te madgataprāṇāḥ, mayi upasaṃhṛtakaraṇāḥ ityarthaḥ. athavā – madgataprāṇāḥ madgatajīvanāḥ ityetat. bodhayantaḥ avagamayantaḥ, parasparam anyonyaṃ, kathayantaḥ jñānabalavīryādidharmaiḥ viśiṣṭaṃ māṃ, tuṣyanti ca paritoṣam upayānti, ramanti ca ratiṃ prāpnuvanti priyasaṅgatyeva.",
           ]),
        _v([
            "teṣāṃ satatayuktānāṃ bhajatāṃ prītipūrvakam |",
            "dadāmi buddhiyogaṃ taṃ yena māmupayānti te",
        ], "|| 10 ||",
           "To those who are ever disciplined and worship me with love, I give the yoga of understanding by which they come to me.",
           bhashya=[
               {"text": "ye yathoktaiḥ prakāraiḥ bhajante yāṃ bhaktāḥ santaḥ–", "intro": True},
               "teṣāṃ satatayuktānāṃ nityābhiyuktānāṃ, nivṛttasarvabāhyaiṣaṇānāṃ, bhajatāṃ sevamānānāṃ, kim arthitvādinā kāraṇena? na ityāha – prītipūrvakam – prītiḥ snehaḥ, tatpūrvakaṃ māṃ bhajatām ityarthaḥ, dadāmi prayacchāmi, buddhiyogaṃ – buddhiḥ samyagdarśanaṃ mattattvaviṣayaṃ, tena yogaḥ buddhiyogaḥ, taṃ buddhiyogam yena buddhiyogena samyagdarśanalakṣaṇena, māṃ parameśvaram ātmabhūtam, ātmatvena, upayānti pratipadyante. ke? te ye maccittatvādiprakāraiḥ māṃ bhajante.",
           ]),
        _v([
            "teṣāmevānukampārthamahamajñānajaṃ tamaḥ |",
            "nāśayāmyātmabhāvastho jñānadīpena bhāsvatā",
        ], "|| 11 ||",
           "Out of compassion for them, abiding in their hearts, I destroy the darkness born of ignorance with the shining lamp of knowledge.",
           bhashya=[
               {"text": "kimarthaṃ kasya vā tvatprāpti pratibandhahetoḥ nāśakaṃ buddhiyogaṃ teṣāṃ tvadbhaktānāṃ dadāsi? ityapekṣāyām āha.", "intro": True},
               "teṣāmeva kathaṃ nāma śreyaḥ syāt iti anukampārthaṃ dayāhetoḥ, aham ajñānajaṃ avivekataḥ jātaṃ mithyāpratyayalakṣaṇaṃ mohāndhakāraṃ tamaḥ nāśayāmi, ātmabhāvasthaḥ ātmanaḥ bhāvaḥ antaḥkaraṇāśayaḥ tasminneva sthitaḥ san, jñānadīpena viveka pratyayarūpeṇa bhaktiprasādasnehābhiṣiktena madbhāvanābhiniveśavāteritena brahmacaryādisādhanasaṃskāra vatprajñāvartinā, viraktāntaḥkaraṇādhāreṇa viṣayavyāvṛttacittarāgadveṣā kaluṣitanivātāpavarakasthena, nityapravṛttaigryadhyānajanitasamyagdarśanabhāsvatā jñānadīpenetyarthaḥ.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "paraṃ brahma paraṃ dhāma pavitraṃ paramaṃ bhavān |",
            "puruṣaṃ śāśvataṃ divyamādidevamajaṃ vibhum",
        ], "|| 12 ||",
           "Arjuna said: You are the supreme Brahman, the supreme abode, the supreme purifier — the eternal divine Person, the first of the gods, unborn and all-pervading.",
           bhashya=[
               {"text": "yathoktāṃ bhagavataḥ vibhūtiṃ yogaṃ ca śrutvā arjuna āha –", "intro": True},
               "paraṃ brahma paramātmā, paraṃ dhāma paraṃ tejaḥ, pavitraṃ pāvanaṃ paramaṃ prakṛṣṭaṃ bhavān. puruṣaṃ śāśvataṃ nityaṃ, divyaṃ divi bhavam, ādidevaṃ sarvadevānām ādau bhavaṃ devaṃ, ajaṃ, vibhuṃ vibhavanaśīlam īdṛśam",
           ]),
        _v([
            "āhustvāmṛṣayaḥ sarve devarṣirnāradastathā |",
            "asito devalo vyāsaḥ svayaṃ caiva bravīṣi me",
        ], "|| 13 ||",
           "So all the seers declare you, and the divine seer Nārada, Asita, Devala and Vyāsa; and you yourself tell me so.",
           bhashya=[
               "āhuḥ kathayanti, tvām ṛṣayaḥ vasiṣṭhādayaḥ, sarve, devarṣiḥ nāradaḥ tathā asitaḥ devalaḥ api evam āha vyāsaḥ ca svayaṃ caiva tvaṃ ca bravīṣi me.",
           ]),
        _v([
            "sarvametadṛtaṃ manye yanmāṃ vadasi keśava |",
            "na hi te bhagavan vyaktiṃ vidurdevā na dānavāḥ",
        ], "|| 14 ||",
           "All this that you tell me I hold to be true, Keśava; for neither the gods nor the demons, O Lord, know your manifestation.",
           bhashya=[
               "sarvamiti – sarvametat yathā uktam ṛṣibhiḥ, tvayā ca etat, ṛtaṃ satyameva, manye yat māṃ prati vadasi bhāṣase, he keśava. na hi, te tava, bhagavan, vyaktiṃ prabhavaṃ, viduḥ devāḥ, na dānavāḥ.",
           ]),
        _v([
            "svayamevātmanā''tmānaṃ vettha tvaṃ puruṣottama |",
            "bhūtabhāvana bhūteśa devadeva jagatpate",
        ], "|| 15 ||",
           "You alone know yourself by yourself, O supreme Person, source of beings, lord of beings, god of gods, lord of the world.",
           bhashya=[
               {"text": "yataḥ tvaṃ devādīnāṃ ādiḥ, ataḥ –", "intro": True},
               "svayameva ātmanā ātmānaṃ vettha jānāsi tvaṃ, niratiśayajñānaiśvaryabalādi śaktimantam, īśvaraṃ, puruṣottama, bhūtāni bhāvayatīti bhūtabhāvanaḥ, he bhūtabhāvana, bhūteśa bhūtānām īśaḥ, he devadeva, jagatpate.",
           ]),
        _v([
            "vaktumarhasyaśeṣeṇa divyā hyātmavibhūtayaḥ |",
            "yābhirvibhūtibhirlokānimāṃstvaṃ vyāpya tiṣṭhasi",
        ], "|| 16 ||",
           "You should tell me, without reserve, of your own divine manifestations, by which you pervade these worlds and abide in them.",
           bhashya=[
               "vaktumiti – vaktuṃ kathayitum, arhasi aśeṣeṇa, divyāḥ hi ātma vibhūtayaḥ ātmanaḥ vibhūtayaḥ yāḥ tāḥ vaktum arhasi. yābhiḥ vibhūtibhiḥ ātmanaḥ māhātmyavistaraiḥ imān lokān, tvaṃ vyāpya tiṣṭhasi.",
           ]),
        _v([
            "kathaṃ vidyāmahaṃ yogiṃstvāṃ sadā paricintayan |",
            "keṣu keṣu ca bhāveṣu cintyo'si bhagavan mayā",
        ], "|| 17 ||",
           "How shall I know you, O yogin, meditating on you always? In what aspects of being are you to be contemplated by me, O Lord?",
           bhashya=[
               "kathaṃ iti. kathaṃ vidyāṃ vijānīyāṃ ahaṃ he yogin! tvāṃ sadā paricintayan. keṣu keṣu ca bhāveṣu vastuṣu cintyaḥ asi dhyeyaḥ asi bhagavan! mayā",
           ]),
        _v([
            "vistareṇātmano yogaṃ vibhūtiṃ ca janārdana |",
            "bhūyaḥ kathaya tṛptirhi śṛṇvato nāsti me'mṛtam",
        ], "|| 18 ||",
           "Tell me again in detail of your yoga and your manifestations, Janārdana; for I never tire of hearing this nectar."),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "hanta te kathayiṣyāmi divyā hyātmavibhūtayaḥ |",
            "prādhānyataḥ kuruśreṣṭha nāstyanto vistarasya me",
        ], "|| 19 ||",
           "The Blessed Lord said: Very well, I will tell you of my divine manifestations — the foremost among them, O best of the Kurus, for there is no end to my extent.",
           bhashya=[
               {"text": "vistareṇeti – vistareṇa ātmanaḥ yogaṃ yogaiśvaryaśaktiviśeṣaṃ, vibhūtiṃ ca, vistaraṃ dhyeyapadārthānāṃ, he janārdana! ardate gatikarmaṇaḥ rūpam. asurāṇāṃ devapratipakṣa bhūtānāṃ janānāṃ narakādigamayitṛtvāt janārdana abhyudaya niḥ śreyasapuruṣārthaprayojanaṃ sarvaiḥ janaiḥ yācyate iti vā. bhūyaḥ pūrvam uktam api kathaya. tṛptiḥ hi paritoṣaḥ yasmāt nāsti me mama śṛṇvataḥ tvanmukhaniḥsṛtavākyāmṛtam.", "intro": True},
               "hanta te iti – hanta idānīṃ te tava divyāḥ divibhavāḥ, ātmavibhūtayaḥ ātmanaḥ mama vibhūtayaḥ yāḥ tāḥ kathayiṣyāmi ityetat. prādhānyataḥ yatra yatra pradhānā yā yā vibhūtiḥ tāṃ tāṃ pradhānāṃ prādhānyataḥ kathayiṣyāmi ahaṃ kuruśreṣṭha. aśeṣatastu varṣaśatenāpi na śakyāḥ vaktuṃ, yataḥ nāsti antaḥ vistarasya me mama vibhūtīnām ityarthaḥ.",
           ]),
        _v([
            "ahamātmā guḍākeśa sarvabhūtāśayasthitaḥ |",
            "ahamādiśca madhyaṃ ca bhūtānāmanta eva ca",
        ], "|| 20 ||",
           "I am the Self, Guḍākeśa, abiding in the heart of all beings; I am the beginning, the middle and the end of beings.",
           bhashya=[
               {"text": "tatra prathamameva tāvat śṛṇu –", "intro": True},
               "aham, ātmā pratyagātmā, guḍākeśa – guḍākā nidrā, tasyāḥ īśaḥ guḍākeśaḥ jitanidraḥ ityarthaḥ. ghanakeśaḥ iti vā. sarveṣāṃ bhūtānām, āśaye antaḥ hṛdi sthitaḥ aham ātmā pratyagātmā nityaṃ dhyeyaḥ. tadaśaktena ca uttareṣu bhāveṣu cintyaḥ ahaṃ. yasmāt ahameva ādiḥ bhūtānāṃ kāraṇaṃ, tathā madhyaṃ ca sthitiḥ, antaḥ pralayaḥ ca.",
           ]),
        _v([
            "ādityānāmahaṃ viṣṇurjyotiṣāṃ raviraṃśumān |",
            "marīcirmarutāmasmi nakṣatrāṇāmahaṃ śaśī",
        ], "|| 21 ||",
           "Of the Ādityas I am Viṣṇu; of lights, the radiant sun; of the Maruts I am Marīci; among the stars, I am the moon.",
           bhashya=[
               {"text": "evaṃ ca dhyeyaḥ aham –", "intro": True},
               "ādityānāṃ dvādaśānāṃ viṣṇuḥ nāma ādityaḥ aham, jyotiṣāṃ raviḥ prakāśayitṝṇām aṃśumān raśmimān. marīciḥ nāma marutāṃ maruddevatābhedānām asmi. nakṣatrāṇām ahaṃ, śaśī candramāḥ.",
           ]),
        _v([
            "vedānāṃ sāmavedo'smi devānāmasmi vāsavaḥ |",
            "indriyāṇāṃ manaścāsmi bhūtānāmasmi cetanā",
        ], "|| 22 ||",
           "Of the Vedas I am the Sāmaveda; of the gods I am Vāsava; of the senses I am the mind; in beings I am consciousness.",
           bhashya=[
               "vedānāmiti – vedānāṃ madhye sāmavedaḥ asmi. devānāṃ rudrādityādīnāṃ vāsavaḥ indraḥ, asmi, indriyāṇām ekādaśānāṃ cakṣurādīnāṃ, manaḥ ca asmi, saṅkalpa vikalpātmakaṃ manaśca asmi. bhūtānām asmi cetanā. kāryakaraṇasaṅghāte nityābhivyaktā buddhivṛttiḥ cetanā.",
           ]),
        _v([
            "rudrāṇāṃ śaṅkaraścāsmi vitteśo yakṣarakṣasām |",
            "vasūnāṃ pāvakaścāsmi meruḥ śikhariṇāmaham",
        ], "|| 23 ||",
           "Of the Rudras I am Śaṅkara; of yakṣas and rākṣasas, the lord of wealth; of the Vasus I am fire; of mountains, I am Meru.",
           bhashya=[
               "rudrāṇāmiti – rudrāṇām ekādaśānāṃ śaṅkaraḥ ca asmi. vitteśaḥ kuberaḥ yakṣarakṣasāṃ yakṣāṇāṃ rakṣasāṃ ca. vasūnām aṣṭānāṃ pāvakaḥ ca asmi agniḥ. meru śikhariṇāṃ śikharavatām, aham.",
           ]),
        _v([
            "purodhasāṃ ca mukhyaṃ māṃ viddhi pārtha bṛhaspatim |",
            "senānīnāmahaṃ skandaḥ sarasāmasmi sāgaraḥ",
        ], "|| 24 ||",
           "Know me, Pārtha, as the chief of household priests, Bṛhaspati; of generals I am Skanda; of bodies of water I am the ocean.",
           bhashya=[
               "purodhasāmiti – purodhasāṃ ca rājapurohitānāṃ, mukhyaṃ pradhānaṃ, māṃ, viddhi jānīhi, he pārtha! bṛhaspatim. sa hi indrasya iti mukhyaḥ syāt purodhasām. senānīnāṃ senāpatīnām, ahaṃ skandaḥ devasenāpatiḥ. sarasāṃ yāni devakhātāni sarāṃsi teṣāṃ sarasāṃ sāgaraḥ, asmi bhavāmi.",
           ]),
        _v([
            "maharṣīṇāṃ bhṛgurahaṃ girāmasmyekamakṣaram |",
            "yajñānāṃ japayajño'smi sthāvarāṇāṃ himālayaḥ",
        ], "|| 25 ||",
           "Of the great seers I am Bhṛgu; of utterances I am the single syllable; of sacrifices I am the sacrifice of silent repetition; of immovable things, the Himālaya.",
           bhashya=[
               "maharṣīṇāmiti – maharṣīṇāṃ bhṛguḥ aham. girāṃ vācāṃ padalakṣaṇānām ekam akṣaram oṅkāraḥ asmi. yajñānāṃ japayajñaḥ asmi. sthāvarāṇāṃ sthitimatāṃ himālayaḥ.",
           ]),
        _v([
            "aśvatthaḥ sarvavṛkṣāṇāṃ devarṣīṇāṃ ca nāradaḥ |",
            "gandharvāṇāṃ citrarathaḥ siddhānāṃ kapilo muniḥ",
        ], "|| 26 ||",
           "Of all trees I am the aśvattha; of divine seers, Nārada; of the gandharvas, Citraratha; of the perfected, the sage Kapila.",
           bhashya=[
               "aśvattha iti – aśvatthaḥ sarvavṛkṣāṇāṃ, devarṣīṇāṃ ca nāradaḥ – devā eva santaḥ ṛṣitvaṃ prāptāḥ mantradarśitvāt, te devarṣayaḥ, teṣāṃ nāradaḥ asmi. gandharvāṇāṃ citraratho nāma gandharvaḥ asmi. siddhānāṃ – janmanaiva dharmajñānavairāgyaiśvaryātiśayaṃ prāptānāṃ kapilaḥ muniḥ.",
           ]),
        _v([
            "uccaiḥśravasamaśvānāṃ viddhi māmamṛtodbhavam |",
            "airāvataṃ gajendrāṇāṃ narāṇāṃ ca narādhipam",
        ], "|| 27 ||",
           "Among horses know me as Uccaiḥśravas, born of the nectar; among lordly elephants, Airāvata; and among men, the king.",
           bhashya=[
               "uccairiti – uccaiḥ śravasam aśvānām uccaiḥśravāḥ nāma aśvaḥ taṃ māṃ, viddhi jānīhi, amṛtodbhavam amṛtanimittamathanodbhavam. airāvatam irāvatyāḥ apatyaṃ, gajendrāṇāṃ hastīśvarāṇāṃ taṃ “māṃ viddhi” ityanuvartate. narāṇāṃ ca manuṣyāṇāṃ ca narādhipaṃ rājānaṃ māṃ viddhi jānīhi.",
           ]),
        _v([
            "āyudhānāmahaṃ vajraṃ dhenūnāmasmi kāmadhuk |",
            "prajanaścāsmi kandarpaḥ sarpāṇāmasmi vāsukiḥ",
        ], "|| 28 ||",
           "Of weapons I am the thunderbolt; of cows, Kāmadhenu; I am Kandarpa, the begetter; of serpents I am Vāsuki.",
           bhashya=[
               "āyudhānām iti – āyudhānām ahaṃ vajraṃ dadhīcyasthisambhavam. dhenūnāṃ dogdhrīṇāṃ asmi kāmadhuk vasiṣṭhasya sarvakāmānāṃ dogdhrī, sāmānyā vā kāmadhuk. prajanaḥ prajanayitā asmi kandarpaḥ kāmaḥ. sarpāṇāṃ sarpabhedānām asmi vāsukiḥ sarparājaḥ.",
           ]),
        _v([
            "anantaścāsmi nāgānāṃ varuṇo yādasāmaham |",
            "pitṝṇāmaryamā cāsmi yamaḥ saṃyamatāmaham",
        ], "|| 29 ||",
           "Of nāgas I am Ananta; of water-beings, Varuṇa; of the ancestors I am Aryaman; of those who restrain, I am Yama.",
           bhashya=[
               "ananta iti – anantaḥ ca asmi nāgānāṃ nāgaviśeṣāṇāṃ nāgarājaḥ ca asmi. varuṇaḥ yādasām aham abdevatānāṃ rājā aham. pitṝṇām aryamā nāma pitṛrājaḥ ca asmi. yamaḥ saṃyamatāṃ saṃyamanaṃ kurvatām aham.",
           ]),
        _v([
            "prahlādaścāsmi daityānāṃ kālaḥ kalayatāmaham |",
            "mṛgāṇāṃ ca mṛgendro'haṃ vainateyaśca pakṣiṇām",
        ], "|| 30 ||",
           "Of the daityas I am Prahlāda; of reckoners, time; of beasts I am the lion; and of birds, the son of Vinatā.",
           bhashya=[
               "prahlāda iti – prahlādaḥ nāma ca asmi daityānāṃ ditivaṃśyānām, kālaḥ kalayatāṃ kalanaṃ gaṇanaṃ kurvatām aham. mṛgāṇāṃ ca mṛgendraḥ siṃhaḥ vyāghro vā aham. venateyaḥ ca garutmān vinatāsutaḥ pakṣiṇāṃ patatriṇām.",
           ]),
        _v([
            "pavanaḥ pavatāmasmi rāmaḥ śastrabhṛtāmaham |",
            "jhaṣāṇāṃ makaraścāsmi srotasāmasmi jāhnavī",
        ], "|| 31 ||",
           "Of purifiers I am the wind; of wielders of weapons, Rāma; of fishes I am the makara; of rivers, the Gaṅgā.",
           bhashya=[
               "pavana iti – pavanaḥ vāyuḥ, pavatāṃ pāvayitṝṇām asmi. rāmaḥ śastrabhṛtām ahaṃ śastrāṇāṃ dhārayitṝṇāṃ dāśarathiḥ rāmaḥ aham. jhaṣāṇāṃ matsyādīnāṃ makaro nāma jāti viśeṣaḥ aham. srotasām sravantīnāṃ asmi jāhnavī gaṅgā.",
           ]),
        _v([
            "sargāṇāmādirantaśca madhyaṃ caivāhamarjuna |",
            "adhyātmavidyā vidyānāṃ vādaḥ pravadatāmaham",
        ], "|| 32 ||",
           "Of creations I am the beginning, the end and the middle, Arjuna; of knowledge, the knowledge of the Self; of those who debate, I am the reasoning.",
           bhashya=[
               "sargāṇāmiti – sṛṣṭīnām ādiḥ antaḥ ca madhyaṃ ca eva aham utpatti sthitilayāḥ, aham arjuna. bhūtānāṃ jīvādhiṣṭhitānāmeva ādiḥ antaśca iti uktam upakrame. (20) iha tu sarvasyaiva sargamātrasya iti viśeṣaḥ adhyātmavidyā vidyānāṃ mokṣārthatvāt pradhānamasmi. vādaḥ arthanirṇaya hetutvāt, pravadatāṃ pradhānam, ataḥ saḥ aham asmi. pravaktṛdvāreṇa vādanabhedānāmeva vādajalpavitaṇḍānām iha grahaṇaṃ “pravadatām” iti.",
           ]),
        _v([
            "akṣarāṇāmakāro'smi dvandvaḥ sāmāsikasya ca |",
            "ahamevākṣayaḥ kālo dhātā'haṃ viśvatomukhaḥ",
        ], "|| 33 ||",
           "Of letters I am the letter a; of compounds, the dvandva; I am imperishable time itself; I am the ordainer whose face is everywhere.",
           bhashya=[
               "akṣarāṇāmiti – akṣarāṇāṃ varṇānām akāraḥ varṇaḥ asmi. dvandvaḥ samāsaḥ asmi sāmāsikasya samāsasamūhasya. kiṃ ca ahameva akṣayaḥ akṣīṇaḥ, kālaḥ prasiddhaḥ kṣaṇādyākhyaḥ, athavā parameśvaraḥ vā kālasyāpi kālaḥ, asmi. dhātā ahaṃ karmaphalasya vidhātā sarvajagataḥ, viśvatomukhaḥ sarvatomukhaḥ.",
           ]),
        _v([
            "mṛtyuḥ sarvaharaścāhamudbhavaśca bhaviṣyatām |",
            "kīrtiḥ śrīrvākca nārīṇāṃ smṛtirmedhā dhṛtiḥ kṣamā",
        ], "|| 34 ||",
           "I am all-seizing death and the origin of what is to be; among feminine powers I am fame, fortune, speech, memory, intelligence, steadfastness and patience.",
           bhashya=[
               "mṛtyuḥ dvividhaḥ dhanādiharaḥ prāṇaharaśca. tatra yaḥ prāṇaharaḥ saḥ sarvaharaḥ ityucyate. saḥ ahamityarthaḥ. athavā, paraḥ īśvaraḥ pralaye sarvaharaṇāt sarva haraḥ, saḥ aham. udbhavaḥ utkarṣaḥ abhyudayaḥ, tatprāptihetuśca ahaṃ, keṣām? bhaviṣyatāṃ bhāvikalyāṇānām utkarṣaprāpti yogyānām ityarthaḥ. kīrtiḥ, śrīḥ vāk ca, nārīṇāṃ, smṛtiḥ medhā, dhṛtiḥ kṣamā – ityetāḥ uttamāḥ strīṇām aham asmi, yāsāṃ ābhāsamātra sambandhenāpi lokaḥ kṛtārtham ātmānaṃ manyate.",
           ]),
        _v([
            "bṛhatsāma tathā sāmnāṃ gāyatrī chandasāmaham |",
            "māsānāṃ mārgaśīrṣo'hamṛtūnāṃ kusumākaraḥ",
        ], "|| 35 ||",
           "Of sāmans I am the Bṛhatsāman; of metres, the Gāyatrī; of months I am Mārgaśīrṣa; of seasons, the season of flowers.",
           bhashya=[
               "bṛhatsāmeti – bṛhatsāma tathā sāmnāṃ pradhānam asmi. “gāyatrī chandasāmaham gāyatryā”di chandoviśiṣṭānām ṛcāṃ gāyatrīṛk aham asmi ityarthaḥ. māsānāṃ mārgaśīrṣo'ham ṛtūnāṃ kusumākaraḥ. vasantaḥ.",
           ]),
        _v([
            "dyūtaṃ chalayatāmasmi tejastejasvināmaham |",
            "jayo'smi vyavasāyo'smi sattvaṃ sattvavatāmaham",
        ], "|| 36 ||",
           "I am the gambling of the deceitful, the splendour of the splendid; I am victory, I am resolve, I am the goodness of the good.",
           bhashya=[
               "dyūtamiti – dyūtam akṣadevanādilakṣaṇaṃ, chalayatāṃ chalasya kartṝṇām asmi. tejastejasvināmahaṃ, jayaḥ asmi jetṝṇāṃ, vyavasāyaḥ asmi vyavasāyinām sattvaṃ sattvavatāṃ sāttvikānām aham.",
           ]),
        _v([
            "vṛṣṇīnāṃ vāsudevo'smi pāṇḍavānāṃ dhanañjayaḥ |",
            "munīnāmapyahaṃ vyāsaḥ kavīnāmuśanā kaviḥ",
        ], "|| 37 ||",
           "Of the Vṛṣṇis I am Vāsudeva; of the Pāṇḍavas, Dhanañjaya; of sages I am Vyāsa; of poets, the poet Uśanas.",
           bhashya=[
               "vṛṣṇīnāmiti – vṛṣṇīnāṃ yādavānāṃ vāsudevaḥ asmi ayameva ahaṃ tvatsakhā. pāṇḍavānāṃ dhanañjayaḥ tvameva. munīnāṃ mananaśīlānāṃ sarvapadārthajñānināmapi ahaṃ vyāsaḥ. kavīnāṃ krāntadarśināṃ uśanā kaviḥ asmi.",
           ]),
        _v([
            "daṇḍo damayatāmasmi nītirasmi jigīṣatām |",
            "maunaṃ caivāsmi guhyānāṃ jñānaṃ jñānavatāmaham",
        ], "|| 38 ||",
           "Of those who punish I am the rod; of those who seek victory, statecraft; of secrets I am silence; and the knowledge of the knowers am I.",
           bhashya=[
               "daṇḍa iti – daṇḍaḥ damayatāṃ damayitṝṇām asmi, adāntānāṃ damanakāraṇam. nītiḥ asmi, jigīṣatāṃ jetum icchatām, maunaṃ ca eva asmi, guhyānāṃ gopyānām. jñānaṃ jñānavatāmaham.",
           ]),
        _v([
            "yaccāpi sarvabhūtānāṃ bījaṃ tadahamarjuna |",
            "na tadasti vinā yatsyānmayā bhūtaṃ carācaram",
        ], "|| 39 ||",
           "Whatever is the seed of all beings, that am I, Arjuna. There is no being, moving or unmoving, that could exist without me.",
           bhashya=[
               "yaccāpīti – yaccāpi sarvabhūtānāṃ, bījaṃ prarohakāraṇaṃ, tat aham arjuna. prakaraṇopasaṃhārārthaṃ vibhūti saṅkṣepam āha – na tat asti bhūtaṃ carācaraṃ caram acaraṃ vā, mayā vinā yat syāt bhavet, mayā aprakṛṣṭaṃ parityaktaṃ nirātmakaṃ śūnyaṃ hi tat syāt, ataḥ madātmakaṃ sarvam ityarthaḥ.",
           ]),
        _v([
            "nānto'sti mama divyānāṃ vibhūtīnāṃ parantapa |",
            "eṣa tūddeśataḥ prokto vibhūtervistaro mayā",
        ], "|| 40 ||",
           "There is no end to my divine manifestations, O scorcher of foes; what I have told is only an illustration of the extent of my glory.",
           bhashya=[
               "nāntostīti – nāntaḥ asti mama divyānāṃ vibhūtīnāṃ vistarāṇāṃ parantapa. na hi īśvarasya sarvātmanaḥ divyānāṃ vibhūtīnām iyattā śakyā vaktuṃ jñātuṃ vā kenacit. eṣaḥ tu uddeśataḥ ekadeśena proktaḥ vibhūteḥ vistaraḥ mayā.",
           ]),
        _v([
            "yadyadvibhūtimatsattvaṃ śrīmadūrjitameva vā |",
            "tattadevāvagaccha tvaṃ mama tejo'ṃśasambhavam",
        ], "|| 41 ||",
           "Whatever being has glory, splendour or might, know that it springs from a fragment of my radiance.",
           bhashya=[
               "yadyaditi – yadyat loke, vibhūtimat vibhūtiyuktaṃ, sattvaṃ vastu śrīmat ūrjitam eva vā, śrīḥ lakṣmīḥ, tayā sahitam utsāhopetaṃ vā, tat tat, eva avagaccha tvaṃ vijānīhi, mama īśvarasya tejoṃśasambhavaṃ, tejasaḥ aṃśaḥ ekadeśaḥ sambhavaḥ yasya tat tejoṃśasambhavam iti avagaccha tvam.",
           ]),
        _v([
            "athavā bahunaitena kiṃ jñātena tavārjuna |",
            "viṣṭabhyāhamidaṃ kṛtsnamekāṃśena sthito jagat",
        ], "|| 42 ||",
           "But what need have you, Arjuna, of this detailed knowledge? I stand supporting this whole universe with a single fragment of myself.",
           bhashya=[
               {"text": "athaveti – athavā bahunā etena evamādinā kiṃ jñātena tava arjuna. syāt sāvaśeṣeṇa. aśeṣataḥ tvam imam ucyamānam arthaṃ śṛṇu – viṣṭabhya viśeṣataḥ, stambhanaṃ dṛḍhaṃ kṛtvā idaṃ kṛtsnaṃ jagat ekāṃśena ekāvayavena ekapādena sarvabhūtasvarūpeṇa ityetat. tathā ca mantravarṇaḥ “pādo'sya viśvābhūtāni” (tai.ā.30.12, ṛ.saṃ.10.90.3) iti – sthitaḥ ahaṃ iti.", "intro": True},
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasahasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītā – sūpaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjunasaṃvāde vibhūtiyogo nāma daśamo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the tenth chapter, Vibhūti Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣyaśrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye vibhūtiyogo nāma daśamo'dhyāyaḥ.", "gloss": "Thus ends the tenth chapter, Vibhūti Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
