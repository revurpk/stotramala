# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 18 (Mokṣasannyāsa Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 18 · Mokṣasannyāsa Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 18",
    "h1": "Bhagavad Gītā · Chapter 18",
    "subtitle": "Mokṣasannyāsa Yoga · liberation through renunciation · with Śaṅkara's bhāṣya",
    "note": "The summation: renunciation and relinquishment, the five factors of action, the threefold knowledge, action, agent, understanding, steadfastness and happiness, the duties born of nature, the way to Brahman, and the final counsel — 'abandoning all dharmas, take refuge in me alone.' At 18.66 Śaṅkara sets out his concluding survey of the whole teaching (śāstrārthopasaṃhāra), the longest passage of the bhāṣya. Arjuna declares his delusion gone, and Sañjaya closes the dialogue.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 17', 'gita-bhashya-17-iast.html'), ('all chapters', '../../index.html#gita')],
    "sections": [
        {"bhashya": [
            "sarvasyaiva gītāśāstrasya arthaḥ asminnadhyāye upasaṃhṛtya sarvaśca vedārtho vaktavya ityevamarthaḥ ayamadhyāyaḥ ārabhyate. sarveṣu hi atīteṣvadhyāyeṣu uktaḥ arthaḥ asminnadhyāye avagamyate. arjunastu sannyāsatyāgaśabdārthayoreva viśeṣambubhutsuḥ",
        ], "summary": "bhāṣya · the chapter's opening"},
        {"speaker": "arjuna uvāca"},
        _v([
            "sannyāsasya mahābāho tattvamicchāmi veditum |",
            "tyāgasya ca hṛṣīkeśa pṛthakkeśiniṣūdana",
        ], "|| 1 ||",
           "Arjuna said: I wish to know the truth about renunciation, mighty-armed one, and about relinquishment, Hṛṣīkeśa, each distinctly, O slayer of Keśin.",
           bhashya=[
               "sannyāsasya iti. sannyāsa śabdārthasya ityetat, he mahābāho! tattvaṃ tasya bhāvastattvaṃ yāthātmyamityetat. icchāmi vedituṃ, jñātuṃ, tyāgasya ca tyāgaśabdārthasya ityetat, hṛṣīkeśa! pṛthak itaretara vibhāgataḥ keśiniṣūdana! keśināmā hayacchadmā kaścit asuraḥ taṃ niṣūditavān bhagavān vāsudevaḥ, tena tannāmnā sambodhyate arjunena.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "kāmyānāṃ karmaṇāṃ nyāsaṃ sannyāsaṃ kavayo viduḥ |",
            "sarvakarmaphalatyāgaṃ prāhustyāgaṃ vicakṣaṇāḥ",
        ], "|| 2 ||",
           "The Blessed Lord said: The sages understand renunciation to be the giving up of actions done from desire; the discerning declare relinquishment to be the giving up of the fruit of all actions.",
           bhashya=[
               {"text": "sannyāsa tyāga śabdau tatra tatra nirdiṣṭau, na nirluṭhitārthau pūrveṣu adhyāyeṣu. ataḥ arjunāya pṛṣṭavate tannirṇayāya.", "intro": True},
               "kāmyānāmiti. kāmyānāṃ aśvamedhādīnāṃ karmaṇāṃ nyāsaṃ parityāgaṃ sannyāsaṃ sannyāsaśabdārthaṃ, anuṣṭheyatvena prāptasya ananuṣṭhānaṃ kavayaḥ paṇḍitāḥ kecit viduḥ vijānanti. nityanaimittikānāṃ anuṣṭhīyamānānāṃ sarvakarmaṇāṃ ātmasambandhitayā prāptasya phalasya parityāgaḥ sarvakarmaphalatyāgaḥ taṃ prāhuḥ kathayanti tyāgaṃ tyāgaśabdārthaṃ vicakṣaṇāḥ paṇḍitāḥ. yadi kāmyakarmaparityāgaḥ phalaparityāgo vā arthaḥ vaktavyaḥ, sarvathā parityāgamātraṃ sannyāsatyāgaśabdayoḥ ekārthaḥ syāt, sa ghaṭapaṭaśabdāviva jātyantara – bhūtārthau.",
               "nanu nitya naimittikānāṃ karmaṇāṃ phalameva nāstītyāhuḥ kathamucyate. teṣāṃ phalatyāgaḥ, yathā vandhyāyāḥ putra tyāgaḥ.",
               "naiṣa doṣaḥ, nityānāmapi karmaṇāṃ bhagavatā phalavattvasya iṣṭatvāt. vakṣyati hi bhagavān “aniṣṭamiṣṭaṃ miśraṃ ca” iti “na taṃ sannyāsināmiti” ca, sannyāsināmeva kevalaṃ karmaphalānubandhaṃ darśayan asannyāsināṃ nityakarmaphalaprāptiṃ “bhavatyatyāgināṃ pretye”ti darśayati.",
           ]),
        _v([
            "tyājyaṃ doṣavadityeke karma prāhurmanīṣiṇaḥ |",
            "yajñadānatapaḥkarma na tyājyamiti cāpare",
        ], "|| 3 ||",
           "Some wise men say that action should be given up as an evil; others that acts of sacrifice, giving and austerity should not be given up.",
           bhashya=[
               "tyājyamiti. tyājyaṃ tyaktavyaṃ, doṣavat doṣaḥ asyāstīti doṣavat. kiṃ tat? karma bandhahetutvātsarva meva. athavā, doṣaḥ yathā rāgādiḥ tyajyate. tathā tyājyamityeke karma prāhuḥ manīṣiṇaḥ paṇḍitāḥ sāṅkhyādi dṛṣṭimāśritāḥ, adhikṛtānāṃ karmiṇāmapīti. tatraiva yajñadānatapaḥkarma na tyājyamiti cāpare.",
               "karmiṇa evādhikṛtāḥ, tān apekṣya ete vikalpāḥ na tu niṣṭhān vyutthāyinaḥ sannyāsinaḥ apekṣya. “jñānayogena sāṅkhyānāṃ niṣṭhā mayā purā prokte”ti (3.3) karmādhikārāt apoddhṛtāḥ ye na tānprati cintā. “nanu karmayogena yogināṃ” (3.3) iti adhikṛtāḥ pūrvaṃ vibhaktaniṣṭhāḥ api iha sarvaśāstrārthopasaṃhāra – prakaraṇe yathā vicāryante, tathā sāṅkhyā api jñānaniṣṭhāḥ vicāryantāṃ iti. na, teṣāṃ mohaduḥkhanimitta tyāganupapatteḥ. nā kāyakleśanimittaṃ duḥkhaṃ sāṅkhyāḥ ātmani paśyanti, icchādīnāṃ kṣetradharmatvena e darśitatvāt. ataḥ te na kāyakleśaduḥkhabhayāt karma parityajanti. nāpi te karmāṇi ātmani paśyanti, yena niyataṃ karma mohāt parityajeyuḥ. guṇānāṃ karma “naiva kiñcit karomi” (5.8) iti hi te sannyasyanti. “sarvakarmāṇi manasā sannyasya” (5.13) ityādibhiḥ tattvavidaḥ sannyāsaprakāraḥ uktaḥ. tasmāt ye anye adhikṛtāḥ karmaṇi anātmavidaḥ, yeṣāṃ ca mohanimittaḥ tyāgaḥ sambhavati kāyakleśabhayācca, te eva tāmasāḥ tyāginaḥ rājasāśca iti nindyante, karmiṇāṃ anātmajñānāṃ karmaphalatyāgastutyartham. “sarvārambha parityāgī ...”, “maunī santuṣṭo yena kenacit. aniketaḥ sthiramatiḥ” (12.16'19) iti guṇātītalakṣaṇe ca paramārthasannyāsinaḥ viśeṣitatvāt. vakṣyati ca “niṣṭhā jñānasya yā parā” iti. (18.50) tasmāt jñānaniṣṭhāḥ sannyāsinaḥ na iha vivakṣitāḥ. karmaphalatyāgaḥ eva sāttvikatvena guṇena tāmasatvādyapekṣayā sannyāsaḥ ucyate, na mukhyaḥ sarvakarmasannyāsaḥ.",
               "sarvakarmasannyāsāsambhave ca “na hi dehabhṛtā” (18.11) iti hetu vacanāt mukhya eva iti cet, na, hetuvacanasya stutyarthatvāt. yathā “tyāgācchāntiranantara” miti (12.12) karmaphalatyāga'stutireva yathoktāneka pakṣānuṣṭhānāśaktimantamarjunaṃ ajñaṃ prati vidhānāt, tathedamapi “na hi dehabhṛtā śakya” miti (18.11) karmaphalatyāga stutyarthaṃ na “sarvakarmāṇi manasā sannyasya naiva kurvannakārayannāste” (5.13) ityasya pakṣasya apavādaḥ kenaciddarśayituṃ śakyaḥ. tasmāt karmaṇyadhikṛtā npratyeva eṣa sannyāsatyāgavikalpaḥ. ye tu paramārthadarśinaḥ sāṅkhyāḥ teṣāṃ jñānaniṣṭhāyāmeva sarvakarmasannyāsalakṣaṇāyāṃ adhikāraḥ, nānyatreti na te vikalpārhāḥ. tacca upapāditamasmābhiḥ “vedāvināśinaṃ” (2.21) ityasmin pradeśe, tṛtīyādau ca.",
           ]),
        _v([
            "niścayaṃ śṛṇu me tatra tyāge bharatasattama |",
            "tyāgo hi puruṣavyāghra trividhassamprakīrtitaḥ",
        ], "|| 4 ||",
           "Hear my decision about relinquishment, O best of the Bhāratas; for relinquishment, O tiger among men, is declared to be of three kinds.",
           bhashya=[
               {"text": "tatra eteṣu vikalpabhedeṣu –", "intro": True},
               "niścayamiti. niścayaṃ śṛṇu avadhāraya, me mama, vacanāt, tatra tyāge tyāgasannyāsa vikalpe yathādarśite, bharatasattama! bharatānāṃ sādhutama! tyāgo hi tyāgasannyāsaśabdavācyo hi ya arthaḥ sa eka eveti abhipretyāha – “tyāgo hi” iti puruṣavyāghra. trividhaḥ triprakāraḥ tāmasādi prakāraiḥ samprakīrtitaḥ śāstreṣu samyak kathitaḥ. yasmāt tāmasādibhedena tyāgasannyāsa śabda vācyā'rtho adhikṛtasya karmiṇo'nātmajñasya trividhaḥ sambhavati na paramārthadarśinaḥ, ityayamartho durjñānaḥ tasmāt atra tattvaṃ nānyo vaktuṃ samarthaḥ. tasmānniściyaṃ paramārthaśāstrārtha viṣayaṃ adhyavasāyaṃ aiśvaraṃ me mattaḥ śṛṇu.",
           ]),
        _v([
            "yajñadānatapaḥkarma na tyājyaṃ kāryameva tat |",
            "yajño dānaṃ tapaścaiva pāvanāni manīṣiṇām",
        ], "|| 5 ||",
           "Acts of sacrifice, giving and austerity should not be given up; they should be performed. Sacrifice, giving and austerity are purifiers of the wise.",
           bhashya=[
               {"text": "kaḥ punaḥ asau niścaya iti, āha –", "intro": True},
               "yajña iti. yajñaḥ dānaṃ tapa ityetat trividhaṃ karma na tyājyaṃ na tyaktavyaṃ, kāryaṃ karaṇīyameva tat, kasmāt? yajñaḥ dānaṃ tapaścaiva pāvanāni viśuddhikarāṇi manīṣiṇāṃ phalānabhisandhīnāmityetat.",
           ]),
        _v([
            "etānyapi tu karmāṇi saṅgaṃ tyaktvā phalāni ca |",
            "kartavyānīti me pārtha niścitaṃ matamuttamam",
        ], "|| 6 ||",
           "But even these actions should be performed giving up attachment and fruits. This, Pārtha, is my decided and highest view.",
           bhashya=[
               "etānyapi iti. etānyapi tu karmāṇi yajñadānatapāṃsi pāvanāni uktāni, saṅgaṃ āsaktiṃ teṣu, tyaktvā phalāni ca teṣāṃ parityajya kartavyāni iti anuṣṭheyānīti, me mama, niścitaṃ matamuttamam. “niścayaṃ śṛṇu me tatra” (18.4) iti pratijñāya, pāvanatvaṃ ca hetumuktvā, “etānyapi tu karmāṇi kartavyāni” iti etat “niścitaṃ matamuttamam” yiti pratijñātārthopasaṃhāra eva. na apūrvārthaṃ vacanam “etānyapi” iti prakṛtasannikṛṣṭārthatvopapatteḥ sāsaṅgasya phalārthino bandhahetavaḥ. “etānyapi karmāṇi mumukṣoḥ kartavyāni” iti apiśabdasya arthaḥ. na tu anyāni karmāṇi apekṣya “etānyapi” iti ucyate. anye tu varṇayanti – nityānāṃ karmaṇāṃ phalābhāvāt “saṅgaṃ tyaktvā phalāni” iti nopapadyate. ataḥ “etānyapi” yiti yāni kāmyāni karmāṇi nityebhyaḥ anyāni, etānyapi kartavyāni, kimuta yajñadānatapāṃsi nityāni iti, tadasat, nityānāmapi karmaṇāṃ yiha phalavattvasya upapāditatvāt “yajño dānaṃ tapaścaiva pāvanāni, ityādinā vacanena. nityānyapi karmāṇi bandhahetutvāśaṅkayā jihāsoḥ mumukṣoḥ kuta kāmyeṣu prasaṅgaḥ? “dūreṇa hyavaraṃ karma” (2.49) iti ca ninditatvāt, yajñārthātkarmaṇo'nyatra (3.9) iti ca kāmyakarmaṇāṃ bandhahetutvasya niścitatvāt, “traiguṇyaviṣayā vedāḥ” (2.45) “traividyā māṃ somapāḥ” (9.20) “kṣīṇe puṇye martyalokaṃ viśanti” (9.21) iti ca, dūravyavahitatvācca, na kāmyeṣu “etānyapi” iti vyapadeśaḥ.",
           ]),
        _v([
            "niyatasya tu sannyāsaḥ karmaṇo nopapadyate |",
            "mohāttasya parityāgastāmasaḥ parikīrtitaḥ",
        ], "|| 7 ||",
           "The renunciation of obligatory action is not proper; giving it up out of delusion is declared to be tāmasa.",
           bhashya=[
               {"text": "tasmādajñasyādhikṛtasya mumukṣoḥ –", "intro": True},
               "niyatasya iti. niyatasya tu nityasya sannyāsaḥ parityāgaḥ karmaṇo, nopapadyate, tasya pāvanatvasya iṣṭatvāt. mohāt ajñānāt tasya niyatasya parityāgaḥ – niyataṃ ca avaśyaṃ kartavyaṃ, tyajyate ca, iti hi pratiṣiddhaṃ. ato mohanimittaḥ parityāgaḥ tāmasaḥ parikīrtitaḥ mohaśca tamaḥ iti. kiñca –",
           ]),
        _v([
            "duḥkhamityeva yatkarma kāyakleśa bhayāttyajet |",
            "sa kṛtvā rājasaṃ tyāgaṃ naiva tyāgaphalaṃ labhet",
        ], "|| 8 ||",
           "He who gives up an action because it is painful, out of fear of bodily hardship, performs a rājasa relinquishment and does not gain its fruit.",
           bhashya=[
               "duḥkhamiti. duḥkhamityeva yatkarma kāyakleśabhayāt śarīraduḥkhabhayāt tyajet, sa kṛtvā rājasaṃ rajo nirvartyaṃ tyāgaṃ naiva tyāgaphalaṃ jñānapūrvakasya sarvakarmatyāgasya phalaṃ mokṣākhyaṃ na labhet na labheta.",
           ]),
        _v([
            "kāryamityeva yatkarma niyataṃ kriyate'rjuna |",
            "saṅgaṃ tyaktvā phalaṃ caiva sa tyāgaḥ sāttviko mataḥ",
        ], "|| 9 ||",
           "When obligatory action is done because it ought to be done, Arjuna, giving up attachment and fruit, that relinquishment is held to be sāttvika.",
           bhashya=[
               {"text": "kaḥ punassāttvikastyāgaḥ iti āha –", "intro": True},
               "kāryamiti. kāryaṃ kartavyamityeva yatkarma niyataṃ nityaṃ kriyate nirvartyate, arjuna, saṅgaṃ tyaktvā phalaṃ caiva, etat nityānāṃ karmaṇāṃ phalavattve bhagavadvacanaṃ pramāṇamavocāma. atha vā, yadyapi phalaṃ na śrūyate nityasya karmaṇaḥ, tathā'pi nityaṃ karma kṛtaṃ ātmasaṃskāraṃ pratyavāyaparihāraṃ vā phalaṃ karoti ātmanaḥ iti kalpayatyevājñaḥ. tatra tāmapi kalpanāṃ nivārayati “phalaṃ tyaktvā” ityanena. ataḥ sādhu uktaṃ “saṅgaṃ tyaktvā phalaṃ ca” iti saḥ tyāgaḥ nitya karmasu saṅgaphalaparityāgaḥ sāttvikaḥ sattvaguṇanirvṛttomataḥ abhipretaḥ.",
               "ākṣepaṇa – nanu karma parityāgaḥ trividhaḥ sannyāsaḥ iti ca prakṛtaḥ. tatra tāmaso rājasaśca tyāgaḥ uktaḥ. kathamiha saṅgaphalatyāgaḥ tṛtīyatvenocyate? yathā trayo brāhmaṇāssamāgatāḥ, tatra ṣaḍaṅga vidau dvau, kṣatriyastṛtīya iti.",
               "tadvat naiṣa doṣaḥ. tyāga sāmānyena stutyarthatvāt. asti hi karma sannyāsasya phalābhisandhityāgasya ca tyāgatvasāmānyaṃ. tatra rājasatāmasatvena karmatyāganindayā karmaphalābhisandhityāgaḥ sāttvikatvena stūyate, “sa tyāgaḥ sāttviko mataḥ” iti.",
           ]),
        _v([
            "na dveṣṭyakuśalaṃ karma kuśale nānuṣajjate |",
            "tyāgī sattvasamāviṣṭo medhāvī chinnasaṃśayaḥ",
        ], "|| 10 ||",
           "The relinquisher pervaded by sattva, wise, with his doubts cut away, does not hate unpleasant action nor cling to pleasant action.",
           bhashya=[
               {"text": "yastu adhikṛtaḥ saṅgaṃ tyaktvā phalābhisandhiṃ ca karma nityaṃ karoti, tasya phalarāgādinā akaluṣīkriyamāṇamantaḥkaraṇa nityaiśca karmabhiḥ saṃskriyamāṇaṃ viśuddhyati. tadviśuddhaṃ prasannaṃ ātmālocanakṣamaṃ bhavati. tasyaiva nityakarmānuṣṭhānena viśuddhāntaḥ karaṇasya ātmajñānābhimukhasya krameṇa yathā tanniṣṭhā syāt, tadvaktavyamiti āha –", "intro": True},
               "na dveṣṭi iti. na dveṣṭyakuśalaṃ aśobhanaṃ kāmyaṃ karma, śarīrārambhadvāreṇa saṃsāra kāraṇaṃ “kimanena” ityevam. kuśale śobhane nitye karmaṇi sattvaśuddhi jñānotpattitanniṣṭhāhetutvena “mokṣakāraṇamidaṃ” ityevaṃ nānuṣajjate. anuṣaṅgaṃ prītiṃ na karoti ityetat. kaḥ punarasau? tyāgī pūrvoktena saṅgaphalatyāgena tadvān tyāgī yaḥ karmaṇi saṅgaṃ tyaktvā tatphalaṃ ca nityakarmānuṣṭhāyī saḥ tyāgī, kadā punarasau akuśalaṃ karma na dveṣṭi, kuśale ca nānuṣajjate iti, ucyate – sattvasamāviṣṭaḥ yadā sattvena ātmānātma vivekajñānahetunā samāviṣṭaḥ saṃvyāptaḥ, sattva saṃyukta ityetat. ata eva ca medhāvī medhayā ātmajñāna lakṣaṇayā prajñayā saṃyuktaḥ tadvān medhāvī, medhā vitvādeva chinna saṃśayaḥ chinnaḥ avidyākṛtaḥ saṃśayaḥ yasya, “ātma svarūpāvasthānameva paraṃ niśśreyasasādhanaṃ, na anyat kiñcit” ityevaṃ niścayena chinna saṃśayaḥ. yaḥ adhikṛtaḥ puruṣaḥ pūrvoktena prakāreṇa karmayogānuṣṭhānena krameṇa saṃskṛtātmā san janmādivikriyā rahitatvena niṣkriyamātmānamātmatvena sambuddhaḥ, saḥ sarvakarmāṇi manasā sannyasya naiva kurvannakārayannāsīno naiṣkarmyalakṣaṇāṃ jñānaniṣṭhāmaśnute ityetat. pūrvoktasya karmayogasya prayojanamanenaiva ślokena uktam.",
           ]),
        _v([
            "na hi dehabhṛtā śakyaṃ tyaktuṃ karmāṇyaśeṣataḥ |",
            "yastu karmaphalatyāgī sa tyāgītyabhidhīyate",
        ], "|| 11 ||",
           "For it is not possible for an embodied being to give up actions entirely; but he who gives up the fruit of action is called a relinquisher.",
           bhashya=[
               {"text": "yaḥ punaradhikṛtassan dehātmābhimānitvena dehabhṛdajñaḥ abādhitātmakartṛtva vijñānatayā “ahaṃ kartā” iti niścitabuddhiḥ, tasya aśeṣakarma parityāgasyāśakyatvāt karmaphalatyāgena codita karmānuṣṭhāne eva adhikāraḥ, na tattyāge ityetamarthaṃ darśayitumāha –", "intro": True},
               "na hi iti. na hi yasmāddehabhṛtā, dehaṃ bibhartīti dehabhṛt, dehātmābhimānavān dehabhṛdityucyate, na vivekī, sa hi “vedāvināśina” (2.21) mityādinā kartṛtvādhikārānnivartitaḥ. ataḥ tena dehabhṛtā ajñena na śakyaṃ tyaktuṃ sannyasituṃ karmāṇi aśeṣataḥ niśśeṣeṇa. tasmādyastvajño'dhikṛto nityāni karmāṇi kurvan karmaphalatyāgī karmaphalābhisandhimātrasannyāsī sa tyāgītyabhidhīyate, karmyapi sanniti stutyabhiprāyeṇa. tasmātparamārthadarśitvenaiva adehabhṛtā dehātmabhāvarahitenaivāśeṣakarmasannyāsaśśakyate kartum.",
           ]),
        _v([
            "aniṣṭamiṣṭaṃ miśraṃ ca trividhaṃ karmaṇaḥ phalam |",
            "bhavatyatyāgināṃ pretya na tu sannyāsināṃ kvacit",
        ], "|| 12 ||",
           "The fruit of action is threefold — undesired, desired and mixed — for those who have not relinquished, after death; but never for the renouncers.",
           bhashya=[
               {"text": "kiṃ punastatprayojanaṃ yatsarvakarmasannyāsātsyāditi ucyate –", "intro": True},
               "aniṣṭamiti. aniṣṭaṃ narakatiryagādilakṣaṇaṃ, iṣṭaṃ devādilakṣaṇaṃ, miśraṃ iṣṭāniṣṭasaṃyuktaṃ manuṣyalakṣaṇaṃ ca tattrividhaṃ triprakāraṃ karmaṇaḥ dharmādharmādi lakṣaṇasya phalaṃ bāhyānekakārakavyāpāra niṣpannaṃ sadavidyākṛtamindrajālamāyopamaṃ mahāmohakaraṃ pratyagātmopasarpi iva – phalgutayā layamadarśanaṃ gacchatīti phalanirvacanam – tadeva lakṣaṇaṃ phalaṃ bhavati atyāgināṃ ajñānāṃ karmiṇāṃ aparamārtha sannyāsināṃ pretya śarīrapātādūrdhvaṃ. na tu sannyāsināṃ paramārthasannyāsināṃ paramahaṃsa – parivrājakānāṃ kevalajñānaniṣṭhānāṃ kvacit. na hi kevala samyagdarśananiṣṭhā avidyādisaṃsārabījaṃ nonmūlayati kadācidityarthaḥ. ataḥ paramārthadarśina eva aśeṣakarmasannyāsitvaṃ sambhavati, avidyādhyāropitatvādātmani kriyākāraka phalānāṃ, na tvajñasyādhiṣṭhānādīni kriyākartṛkārakāṇyātmatvena paśyataḥ aśeṣakarma sannyāsassambhavati.",
           ]),
        _v([
            "pañcaitāni mahābāho kāraṇāni nibodha me |",
            "sāṅkhye kṛtānte proktāni siddhaye sarvakarmaṇām",
        ], "|| 13 ||",
           "Learn from me, mighty-armed one, these five factors for the accomplishment of all actions, as declared in the Sāṅkhya doctrine:",
           bhashya=[
               {"text": "tat etat uttaraiḥ ślokaiḥ darśayati –", "intro": True},
               "pañca iti. pañcaitāni vakṣyamāṇāni mahābāho, kāraṇāni nirvartakāni. nibodha mama ityuttaratra cetassamādhānārthaṃ vastuvaiṣamya pradarśanārthaṃ ca. tāni ca kāraṇāni jñātavyatayā stauti – sāṅkhye, jñātavyāḥ padārthāssaṅkhyāyante yasmin śāstre tatsāṅkhyaṃ vedāntaḥ, kṛtānta iti tasyaiva viśeṣaṇaṃ. kṛtamiti karmocyate, tasyāntaḥ parisamāptiryatra sa kṛtāntaḥ, karmānta ityetat “yāvānartha udapāne” (2.46) “sarvaṃ karmākhilaṃ pārtha jñāne parisamāpyate” (4.33) ityātmajñāne sañjāte sarvakarmaṇāṃ nivṛttiṃ darśayati. atastasminnātmajñānārthe sāṅkhye kṛtānte vedānte, proktāni kathitāni siddhaye niṣpatyarthaṃ sarvakarmaṇām.",
           ]),
        _v([
            "adhiṣṭhānaṃ tathā kartā karaṇaṃ ca pṛthagvidham |",
            "vividhāḥ ca pṛthakceṣṭā daivaṃ caivātra pañcamam",
        ], "|| 14 ||",
           "the body, the agent, the various instruments, the many distinct activities, and the divine, the fifth among them.",
           bhashya=[
               {"text": "kāni tānīti ucyate –", "intro": True},
               "adhiṣṭhānamiti. adhiṣṭhānaṃ icchādveṣasukhaduḥkhajñānādīnā'mabhivyakterāśrayodhiṣṭhānaṃ śarīraṃ, tathā kartā upādhilakṣaṇo bhoktā, karaṇaṃ ca śrotrādi śabdādyupalabdhaye pṛthagvidhaṃ nānā prakāraṃ tadvādaśasaṅkhyaṃ, vividhāśca pṛthakceṣṭāḥ vāyavīyāḥ prāṇāpānādyāḥ daivaṃ caiva daivameva ca atra eteṣu caturṣu pañcamaṃ pañcānāṃ pūraṇaṃ ādityādi cakṣurādyanugrāhakam.",
           ]),
        _v([
            "śarīravāṅmanobhiryat karma prārabhate naraḥ |",
            "nyāyyaṃ vā viparītaṃ vā pañcaite tasya hetavaḥ",
        ], "|| 15 ||",
           "Whatever action a man undertakes with body, speech or mind, whether right or wrong, these five are its factors.",
           bhashya=[
               "śarīra iti. śarīravāṅmanobhiḥ yat karma tribhiretaiḥ prārabhate nirvartayati naraḥ, nyāyyaṃ vā dharmyaṃ śāstrīyaṃ viparītaṃ vā adharmyamaśāstrīyaṃ yaccāpi nimeṣādikaṃ ceṣṭitādi jīvanahetuḥ tadapi pūrvakṛta dharmādharmayoreva kāryamiti nyāyyaviparītayoreva grahaṇena gṛhītaṃ, pañcaite yathoktāstasya sarvasyaiva karmaṇohetavaḥ kāraṇāni. nanu etānyadhiṣṭhānādīni sarvakarmaṇāṃ nirvartakāni. kathaṃ ucyate “śarīra vāṅmanobhiryatkarma prārabhata” iti? naiṣa doṣaḥ, vidhipratiṣedhalakṣaṇaṃ sarvaṃ karma śarīrāditrayapradhānaṃ tadaṅgatayā darśanaśravaṇādi ca jīvanalakṣaṇaṃ tridhaiva rāśīkṛtamucyate śarīrādibhirārabhyata iti. phala kāle'pi tatpradhānaissādhanairbhujyate iti pañcānāmeva hetutvaṃ na virudhyate iti.",
           ]),
        _v([
            "tatraivaṃ sati kartāramātmānaṃ kevalaṃ tu yaḥ |",
            "paśyatyakṛtabuddhitvānna sa paśyati durmatiḥ",
        ], "|| 16 ||",
           "This being so, he who, through an untrained understanding, sees himself, the pure Self, as the agent does not see, being of perverted mind.",
           bhashya=[
               "tatra iti. tatreti prakṛtena sambadhyate, evaṃ sati evaṃ yathoktaiḥ pañcabhirhetubhirnirvartye sati karmaṇi. “tatraivaṃ satī” ti durmatitvasya hetutvena sambadhyate. tatra eteṣu ātmā ananyatvena avidyayā parikalpitaiḥ kriyamāṇasya karmaṇaḥ “ahameva kartā” iti kartāramātmānaṃ kevalaṃ śuddhaṃ tu yaḥ paśyatyavidvān, kasmāt? vedāntācāryopadeśanyāyaiḥ akṛtabuddhitvāt asaṃskṛta buddhitvāt, yo'pi dehādivyatiriktātmavādī ātmānameva kevalaṃ kartāraṃ paśyati. asāvapyakṛta buddhireva ataḥ akṛtabuddhitvāt na saḥ paśyatyātmanastattvaṃ karmaṇo vā ityarthaḥ. ato durmatiḥ kutsitā viparītā duṣṭā ajasraṃ jananamaraṇa pratipattihetubhūtā matiḥ asya iti durmatiḥ. saḥ paśyannapi na paśyati, yathā taimirikaḥ anekacandraṃ, yathā vā abhreṣu dhāvatsu candraṃ dhāvantaṃ, yathā vāhane upaviṣṭaḥ anyeṣu dhāvatsu ātmānaṃ dhāvantam.",
           ]),
        _v([
            "yasya nāhaṅkṛto bhāvo buddhiryasya na lipyate |",
            "hatvā'pi sa imān lokān na hanti na nibadhyate",
        ], "|| 17 ||",
           "He who is free from the sense of 'I am the doer', whose understanding is not tainted — though he slays these people, he does not slay and is not bound.",
           bhashya=[
               {"text": "kaḥ punassumatiḥ yassamyakpaśyatītyucyate –", "intro": True},
               "yasya iti. yasya śāstrācāryopadeśa nyāyasaṃskṛtātmanaḥ na bhavati ahaṃ kṛtaḥ “ahaṃ kartā” ityevaṃlakṣaṇaṃ bhāvaḥ bhāvanā pratyayaḥ – ete eva pañca adhiṣṭhānādayaḥ avidyayā ātmani kalpitāḥ sarvakarmaṇāṃ kartāraḥ, na ahaṃ ahaṃ tu tadvyāpārāṇāṃ sākṣibhūtaḥ “aprāṇo hyamanāḥ śubhro hyakṣarātparataḥ paraḥ” (muṃ.u.2.12) kevalaḥ avikriyaḥ ityevaṃ paśyati iti etat – buddhi antaḥkaraṇaṃ yasya ātmanaḥ upādhibhūtā na lipyate na anuśayinī bhavati – “idaṃ ahaṃ akārṣaṃ, tena ahaṃ narakaṃ gamiṣyāmi”, ityevaṃ yasya buddhiḥ na lipyate – saḥ sumatiḥ, saḥ paśyati. hatvā api saḥ imān lokān, sarvān imān prāṇinaḥ ityarthaḥ, na hanti hananakriyāṃ na karoti, na nibadhyate nāpi tatkāryeṇa adharmaphalena sambadhyate.",
               "nanu hatvā'pi na hanti iti vipratiṣiddhaṃ ucyate yadyapi stutiḥ? naiṣa doṣaḥ laukika pāramārthikadṛṣṭyapekṣayā tadupapatteḥ. dehādyātmabuddhyā hantā ahaṃ iti laukikīṃ dṛṣṭiṃ āśritya “hatvā'pi” iti āha, yathādarśitāṃ pāramārthikī dṛṣṭiṃ āśritya “na hanti na nibadhyate” iti etat ubhayaṃ upapadyate eva. nanu adhiṣṭhānādibhiḥ sambhūya karoti eva ātmā, “kartāramātmānaṃ kevalaṃ tu” (18.16) iti “kevala” śabdaprayogāt. naiṣa doṣaḥ ātmanaḥ avikriyasvabhāvatve adhiṣṭhānādibhiḥ saṃhatatvānupapatteḥ. vikriyāvataḥ hi anyaiḥ saṃhananaṃ sambhavati, saṃhatya vā kartṛtvaṃ syāt. na tu avikriyasya ātmanaḥ kenacit saṃhananaṃ asti iti na sambhūya kartṛtvaṃ upapadyate. ataḥ kevalatvaṃ ātmanaḥ svābhāvikam iti kevalaśabdaḥ anuvādamātram. avakriyatvaṃ ca ātmanaḥ śrutismṛtinyāya prasiddham. “avikāryo'yamucyate”, (2.25) “guṇaireva karmāṇi kriyante”, (3.27) “śarīra stho'pi na karoti”, (13.31) ityādi asakṛt upapāditaṃ gītāsu eva tāvat. śrutiṣu ca dhyāyatīva lelāyatīva (bṛ.u.43.7) ityevamādyāsu. nyāyataśca niravayavaṃ, aparatantraṃ, avikriyaṃ ātmatattvaṃ iti rājamārgaḥ. vikriyāvattvābhyupagame'pi ātmanaḥ svakīyā eva vikriyā svasya bhavituṃ arhati, na adhiṣṭhānādīnāṃ karmāṇi ātmakartṛkāṇi syuḥ na hi parasya karma pareṇa akṛtaṃ āgantuṃ arhati. yattu avidyayā gamitaṃ, na tat tasya, yathā rajatatvaṃ na śuktikāyāḥ, yathā vā talamalinatvaṃ bālaiḥ gamitaṃ avidyayā na ākāśasya tathā adhiṣṭhānādi vikriyā'pi teṣāṃ eva, na ātmanaḥ. tasmāt yuktaṃ uktam “ahaṅkṛtatatvabuddhi lepābhāvāt vidvān na hanti na nibadhyate” iti.",
               "“nāyaṃ hanti na hanyate” iti pratijñāya “na jāyate” ityādi hetuvacanena avikriyatvaṃ ātmanaḥ uktvā, “vedāvināśinaṃ” iti viduṣaḥ karmādhikāranivṛttiṃ śāstrādau saṅkṣepataḥ uktvā madhyaprasāritāṃ, tatra tatra prasaṅgaṃ kṛtvā iha upasaṃharati śāstrārtha piṇḍikaraṇāya “vidvān na hanti na nibadhyate” iti. evaṃ ca sati dehabhṛttvābhimānāpapattau avidyākṛtāśeṣakarma sannyāsopapatteḥ sannyāsināṃ aniṣṭādi trividhaṃ karmaṇaḥ phalaṃ na bhavati iti upapannaṃ, tadviparyayāt ca itareṣāṃ bhavati iti etat ca aparihāryaṃ iti eṣaḥ gītāśāstrārthaḥ upasaṃhṛtaḥ. sa eṣaḥ sarvavedārthasāraḥ nipuṇamatibhiḥ paṇḍitaiḥ vicārya pratipattavyaḥ iti tatra tatra prakaraṇavibhāgena darśitaḥ asmābhiḥ śāstranyāyānusāreṇa.",
           ]),
        _v([
            "jñānaṃ jñeyaṃ parijñātā trividhā karmacodanā |",
            "karaṇaṃ karma karteti trividhaḥ karmasaṅgrahaḥ",
        ], "|| 18 ||",
           "Knowledge, the known and the knower make up the threefold impulse to action; the instrument, the action and the agent make up the threefold basis of action.",
           bhashya=[
               {"text": "atha idānīṃ karmaṇāṃ pravartaka mucyate –", "intro": True},
               "jñānamiti. jñānaṃ jñāyate'neneti sarva viṣayaṃ jñānamaviśeṣeṇocyate tathā jñeyaṃ jñātavyaṃ tadapi sāmānyenaiva sarvamucyate, tathā parijñātā upādhi lakṣaṇaḥ avidyā kalpito bhoktā – iti etattrayamaviśeṣeṇa sarvakarmaṇāṃ pravartikā trividhā triprakārā karmacodanā. jñānādīnāṃ hi trayāṇāṃ sannipāte hānopādānopekṣā prayojanaḥ sarvakarmārambhassyāt. tataḥ pañcabhiradhiṣṭhānādibhirārabdhaṃ vāṅñmanaḥ kāyāśrayabhedena tridhā rāśībhūtaṃ triṣu karaṇādiṣu saṅgṛhyate ityetaducyate – karaṇaṃ kriyate'neneti bāhyaṃ śrotrādi antasthaṃ buddhyādi, karma īpsitatamaṃ kartuḥ kriyayā vyāpyamānaṃ kartā karaṇānāṃ vyāpārayitopādhi lakṣaṇaḥ iti trividhastriprakāraḥ karma saṅgrahaḥ, saṅgṛhyate'sminniti saṅgrahaḥ karmaṇassaṅgrahaḥ karma saṅgrahaḥ, karma eṣu triṣu samavaiti, tenāyaṃ trividhaḥ karma saṅgrahaḥ",
           ]),
        _v([
            "jñānaṃ karma ca kartā ca tridhaiva guṇabhedataḥ |",
            "procyate guṇasaṅkhyāne yathāvacchṛṇu tānyapi",
        ], "|| 19 ||",
           "Knowledge, action and the agent are declared in the doctrine of the guṇas to be of three kinds each, according to the distinction of the guṇas. Hear of these as they are.",
           bhashya=[
               {"text": "atha idānīṃ kriyākāraka phalānāṃ sarveṣāṃ guṇātmakatvāt sattvarajastamo guṇabhedataḥ trividhaḥ bhedaḥ vaktavya iti ārabhyate –", "intro": True},
               "jñānamiti. jñānaṃ karma ca karma kriyā, na kārakaṃ pāribhāṣikaṃ īpsitatamaṃ karma, kartā ca nirvartakaḥ kriyāṇāṃ tridhaiva, avadhāraṇaṃ guṇavyatiriktajātyantarābhāva pradarśanārthaṃ guṇabhedassatvādi bhedenetyarthaḥ, procyate kathyate guṇa saṅkhyāne kāpile śāstre tadapi guṇasaṅkhyāna śāstraṃ guṇabhoktṛviṣaye pramāṇameva, paramārtha brahmaikatva viṣaye yadyapi virudhyate, tathāpi te hi kāpilāḥ guṇagauṇavyāpāranirūpaṇe abhiyuktāḥ iti tacchāstramapi vakṣyamāṇārtha stutyarthatvena upādīyate iti na virodhaḥ. yathāvat yathānyāyaṃ yathāśāstraṃ śṛṇu tānyapi jñānādīni tadbhedajātāni ca guṇabheda kṛtāni śṛṇu, vakṣyamāṇe arthe manassamādhiṃ kuru ityarthaḥ.",
           ]),
        _v([
            "sarvabhūteṣu yenaikaṃ bhāvamavyayamīkṣate |",
            "avibhaktaṃ vibhakteṣu tad jñānaṃ viddhi sāttvikam",
        ], "|| 20 ||",
           "Know that knowledge to be sāttvika by which one sees the one imperishable being in all beings, undivided in the divided.",
           bhashya=[
               {"text": "jñānasya tāvat trividhatvaṃ ucyate –", "intro": True},
               "sarvabhūteṣu iti. sarvabhūteṣu avyaktādi sthāvarānteṣu bhūteṣu yena jñānena ekaṃ bhāvaṃ vastu bhāva śabdaḥ vastuvācī, ekaṃ ātma vastu ityarthaḥ avyayaṃ na vyeti svātmanā svadharmeṇa vā, kūṭasthaṃ ityarthaḥ, īkṣate paśyati yena jñānena. taṃ ca bhāvaṃ avibhaktaṃ pratidehaṃ vibhakteṣu dehabhedeṣu na vibhaktaṃ tat ātma vastu vyomavat nirantaramityarthaḥ, tat jñānaṃ sākṣāt samyagdarśanaṃ advaitātma viṣayaṃ sāttvikaṃ viddhi iti. yāni dvaita darśanāni tāni asamyagbhūtāni rājasāni tāmasāni ca iti na sākṣāt saṃsārocchittaye bhavanti.",
           ]),
        _v([
            "pṛthaktvena tu yad jñānaṃ nānābhāvān pṛthagvidhān |",
            "vetti sarveṣu bhūteṣu tad jñānaṃ viddhi rājasam",
        ], "|| 21 ||",
           "But know that knowledge to be rājasa which, through separateness, sees in all beings various entities of different kinds.",
           bhashya=[
               "pṛthaktvena iti. pṛthaktvena tu bhedena prati śarīra manyatvena yad jñānaṃ nānābhāvān bhinnān ātmanaḥ pṛthagvidhān pṛthakprakārān bhinnalakṣaṇānityarthaḥ. vetti vijānāti yat jñānaṃ sarveṣu bhūteṣu jñānasya kartṛtvāsambhavāt yena jñānena vettītyarthaḥ, tat jñānaṃ viddhi rājasaṃ rajoguṇa nirvṛttam.",
           ]),
        _v([
            "yattu kṛtsnavadekasmin kārye saktamahaitukam |",
            "atattvārthavadalpaṃ ca tattāmasamudāhṛtam",
        ], "|| 22 ||",
           "And that which clings to one single effect as if it were the whole, without reason, without grasp of truth, and trivial, is declared to be tāmasa.",
           bhashya=[
               "yattu iti. yat jñānaṃ kṛtsnavat samastavat sarva viṣayamiva ekasmin kārye dehe bahirvā pratimādau saktaṃ “etāvāneva ātmā īśvaro vā, nātaḥ paramasti” iti, yathā nagnakṣapaṇakādīnāṃ śarīrāntarvartī dehaparimāṇo jīvaḥ, īśvaro vā pāṣāṇa dārvādimātraṃ, ityevamekasmin kārye saktaṃ ahaitukaṃ hetuvarjitaṃ niryuktikaṃ, atattvārthavat ayathābhūtārthavat, yathābhūtārthastattvārthaḥ, so'syajñeyabhūtaḥ astīti tattvārthavat, na tattvārthavadatattvārthavat, ahaitukatvādeva alpaṃ ca, alpa viṣayatvāt alpaphalatvādvā. tat tāmasamudāhṛtaṃ. tāmasānāṃ hi prāṇināṃ avivekināṃ jñānamīdṛśaṃ dṛśyate.",
           ]),
        _v([
            "niyataṃ saṅgarahitamarāgadveṣataḥ kṛtam |",
            "aphalaprepsunā karma yattatsāttvikamucyate",
        ], "|| 23 ||",
           "Obligatory action done without attachment, without desire or aversion, by one who seeks no fruit, is called sāttvika.",
           bhashya=[
               {"text": "atha idānīṃ karmaṇaḥ traividhyamucyate –", "intro": True},
               "niyatamiti. niyataṃ nityaṃ saṅgarahitaṃ āsaktivarjitaṃ arāgadveṣataḥ kṛtaṃ rāgaprayuktena dveṣa prayuktena ca kṛtaṃ rāgadveṣataḥ kṛtam, tadviparītamarāgadveṣataḥ kṛtam, aphalaprepsunā phalaṃ prāptumicchatīti phalaprepsuḥ phalatṛṣṇaḥ tadviparītena aphalaprepsunā kartrā kṛtaṃ karma yat, tat sāttvikamucyate.",
           ]),
        _v([
            "yattu kāmepsunā karma sāhaṅkāreṇa vā punaḥ |",
            "kriyate bahulāyāsaṃ tadrājasamudāhṛtam",
        ], "|| 24 ||",
           "But action done by one who longs for desires, or with egoism, and with much strain, is declared to be rājasa.",
           bhashya=[
               "yattu iti. yattu kāmepsunā karmaphalaprepsunetyarthaḥ. karma sāhaṅkāreṇa iti na tattvajñānāpekṣayā kiṃ tarhi? laukika śrotriya nirahaṅkārāpekṣayā. yo hi paramārtha nirahaṅkāraḥ ātmavit. na tasya kāmepsutva – bahulāyāsa kartṛtva prāptiḥ asti sāttvikasyāpi karmaṇaḥ anātmavit sāhaṅkāraḥ kartā, kimuta rājasa tāmasayoḥ. loke anātmavidapi śrotriyo nirahaṅkāraḥ ucyate “nirahaṅkāraḥ ayaṃ brāhmaṇaḥ” iti tasmāt tadapekṣayaiva “sāhaṅkāreṇa” vetyuktam. punaśśabdaḥ pādapūraṇārthaḥ. kriyate bahulāyāsaṃ kartrā mahatā āyāsena nirvartyate, tat karma rājasamudāhṛtam.",
           ]),
        _v([
            "anubandhaṃ kṣayaṃ hiṃsāmanapekṣya ca pauruṣam |",
            "mohādārabhyate karma yattattāmasamucyate",
        ], "|| 25 ||",
           "Action undertaken out of delusion, without regard to consequence, loss, injury to others or one's own capacity, is called tāmasa.",
           bhashya=[
               "anubandhamiti. anubandhaṃ paścādbhāvi yadvastu saḥ anubandhaḥ ucyate taṃ ca anubandhaṃ, kṣayaṃ yasmin karmaṇi kriyamāṇe śakti kṣayaḥ arthakṣayo vā syāt taṃ kṣayaṃ, hiṃsāṃ prāṇibādhāṃ ca, anapekṣya ca nirapekṣya ca pauruṣaṃ puruṣakāraṃ “śaknomi idaṃ karma samāpayituṃ” ityevamātmasāmarthyaṃ, ityetāni anubandhādīnyanapekṣya pauruṣāntāni mohāt avivekataḥ ārabhyate karma yat, tat tāmasaṃ tamo nirvṛttamucyate.",
           ]),
        _v([
            "muktasaṅgo'nahaṃvādī dhṛtyutsāhasamanvitaḥ |",
            "siddhyasiddhyornirvikāraḥ kartā sāttvika ucyate",
        ], "|| 26 ||",
           "An agent free from attachment, without egoism, endowed with steadfastness and zeal, unchanged in success and failure, is called sāttvika.",
           bhashya=[
               {"text": "idānīṃ kartṛbheda ucyate –", "intro": True},
               "mukta iti. muktasaṅgaḥ muktaḥ parityaktaḥ saṅgaḥ yena saḥ muktasaṅgaḥ, anahaṃvādī nāhaṃvadanaśīlaḥ, dhṛtyutsāha samanvitaḥ dhṛtiḥ dhāraṇaṃ utsāhaḥ udyamaḥ tābhyāṃ samanvitaḥ saṃyuktaḥ dhṛtyutsāha samanvitaḥ, siddhyasiddhyoḥ kriyamāṇasya karmaṇaḥ phalasiddhau asiddhau ca siddhyasiddhyornirvikāraḥ, kevalaṃ śāstra pramāṇena prayukto na phalarāgādinā yaḥ saḥ nirvikāraḥ ucyate. evambhūtaḥ kartā yaḥ saḥ sāttvikaḥ ucyate.",
           ]),
        _v([
            "rāgī karmaphalaprepsurlubdho hiṃsātmako'śuciḥ |",
            "harṣaśokānvitaḥ kartā rājasaḥ parikīrtitaḥ",
        ], "|| 27 ||",
           "An agent who is passionate, who longs for the fruit of action, greedy, violent by nature, impure, and subject to joy and sorrow, is called rājasa.",
           bhashya=[
               "rāgī iti. rāgī rāgaḥ asyāstīti rāgī karma phalaprepsuḥ karma phalārthī ityarthaḥ. lubdhaḥ paradravyeṣu sañjāta tṛṣṇaḥ, tīrthādau svadravyāparityāgī vā hiṃsātmakaḥ parapīḍākara svabhāvaḥ aśuciḥ bāhyābhyantara śaucavarjitaḥ harṣaśokānvitaḥ iṣṭa prāptau harṣaḥ aniṣṭa prāptāviṣṭaviyoge ca śokaḥ tābhyāṃ harṣa śokābhyāṃ samanvitaḥ saṃyuktaḥ, tasyaiva ca karmaṇaḥ sampatti vipattibhyāṃ harṣaśokau syātāṃ tābhyāṃ saṃyukto yaḥ kartā saḥ rājasaḥ parikīrtitaḥ.",
           ]),
        _v([
            "ayuktaḥ prākṛtaḥ stabdhaḥ śaṭho naiṣkṛtiko'lasaḥ |",
            "viṣādī dīrghasūtrī ca kartā tāmasa ucyate",
        ], "|| 28 ||",
           "An agent who is undisciplined, vulgar, obstinate, deceitful, malicious, lazy, despondent and procrastinating is called tāmasa.",
           bhashya=[
               "ayukta iti. ayuktaḥ na yuktaḥ na samāhitaḥ, prākṛtaḥ atyantāsaṃskṛta buddhiḥ bālasamaḥ, stabdhaḥ daṇḍavat. na namati kasmaicit, śaṭhaḥ māyāvī śakti gūhanakārī, naiṣkṛtikaḥ para vibhedanaparaḥ, alasaḥ apravṛtti śīlaḥ kartavyeṣvapi viṣādī viṣādavān sarvadā avasanna svabhāvaḥ, dīrghasūtrī ca kartavyādīnāṃ dīrghaprasāraṇaḥ sarvadā mandasvabhāvaḥ yadadya śvo vā kartavyaṃ tanmāsenāpi na karoti, yaścaivaṃ bhūtaḥ kartā saḥ tāmasaḥ ucyate.",
           ]),
        _v([
            "buddherbhedaṃ dhṛteścaiva guṇatastrividhaṃ śṛṇu |",
            "procyamānamaśeṣeṇa pṛthaktvena dhanañjaya",
        ], "|| 29 ||",
           "Hear now, Dhanañjaya, the threefold distinction of understanding and of steadfastness according to the guṇas, set out fully and distinctly.",
           bhashya=[
               "buddherbhedamiti. buddheḥ bhedaṃ dhṛteḥ ca evaṃ bhedaṃ, guṇataḥ sattvādiguṇataḥ trividhaṃ śṛṇviti sūtropanyāsaḥ. procyamānaṃ kathyamānaṃ aśeṣeṇa niravaśeṣataḥ yathāvat pṛthaktvena vivekataḥ dhanañjaya! digvijaye mānuṣaṃ daivaṃ ca prabhūtaṃ dhanaṃ jitavān tena asau dhanañjayaḥ tasya sambuddhiḥ he dhanañjaya arjuna.",
           ]),
        _v([
            "pravṛttiṃ ca nivṛttiṃ ca kāryākārye bhayābhaye |",
            "bandhaṃ mokṣaṃ ca yā vetti buddhiḥ sā pārtha sāttvikī",
        ], "|| 30 ||",
           "That understanding which knows action and cessation, what ought and ought not to be done, fear and fearlessness, bondage and liberation, is sāttvika, Pārtha.",
           bhashya=[
               "pravṛttimiti. pravṛttiṃ ca pravṛttiḥ pravartanaṃ bandhahetuḥ karmamārgaḥ śāstravihitaviṣayaḥ nivṛttiṃ ca nivṛttiḥ mokṣahetuḥ sannyāsamārgaḥ – bandhamokṣa samānavākyatvāt pravṛtti nivṛttī karma sannyāsa mārgāvityavagamyate – kāryākārye vihita pratiṣiddhe laukike vaidike vā śāstrabuddheḥ kartavyākartavye karaṇākaraṇe ityetat kasya? deśakālādyapekṣayā dṛṣṭādṛṣṭārthānāṃ karmaṇāṃ. bhayābhaye bibhetyasmāditi bhayaṃ coravyāghrādi, na bhayaṃ abhayaṃ, bhayaṃ ca abhayaṃ ca bhayābhaye, dṛṣṭādṛṣṭaviṣayayoḥ bhayābhayayoḥ kāraṇe ityarthaḥ. bandhaṃ sahetukaṃ mokṣaṃ ca sahetukaṃ yā vetti vijānāti buddhiḥ, sā pārtha! sāttvikī. tatra jñānaṃ buddheḥ vṛttiḥ buddhistu vṛttimatī. dhṛtirapi vṛttiviśeṣa eva. buddheḥ",
           ]),
        _v([
            "yayā dharmamadharmaṃ ca kāryaṃ cākāryameva ca |",
            "ayathāvatprajānāti buddhiḥ sā pārtha rājasī",
        ], "|| 31 ||",
           "That understanding by which one wrongly grasps dharma and adharma, what ought and ought not to be done, is rājasa, Pārtha.",
           bhashya=[
               "yayā iti. yayā dharmaṃ śāstra coditaṃ adharmaṃ ca tatpratiṣiddhaṃ kāryaṃ ca akāryameva ca pūrvokte eva kāryākārye ayathāvat na yathāvat sarvataḥ nirṇayena na prajānāti buddhiḥ sā pārtha rājasī.",
           ]),
        _v([
            "adharmaṃ dharmamiti yā manyate tamasā''vṛtā |",
            "sarvārthānviparītāṃśca buddhiḥ sā pārtha tāmasī",
        ], "|| 32 ||",
           "That understanding which, covered by darkness, thinks adharma to be dharma and sees all things perversely, is tāmasa, Pārtha.",
           bhashya=[
               "adharmamiti. adharmaṃ pratiṣiddhaṃ vihitaṃ dharmamiti yā manyate jānāti tamasā āvṛtā satī, sarvārthān sarvāneva jñeyapadārthān viparītāṃśca viparītāneva vijānāti, buddhissā pārtha tāmasī.",
           ]),
        _v([
            "dhṛtyā yayā dhārayate manaḥ prāṇendriyakriyāḥ |",
            "yogenāvyabhicāriṇyā dhṛtiḥ sā pārtha sāttvikī",
        ], "|| 33 ||",
           "The unwavering steadfastness by which, through yoga, one holds the workings of the mind, the breath and the senses, is sāttvika, Pārtha.",
           bhashya=[
               "dhṛtyā iti. dhṛtyā yayā – avyabhicāriṇyā iti vyavahitena sambandhaḥ, dhārayate kiṃ? manaḥ prāṇendriya kriyāḥ manaśca prāṇāśca indriyāṇi ca manaḥ prāṇendriyāṇi teṣāṃ kriyāḥ ceṣṭāḥ tāḥ ucchāstramārgapravṛtteḥ dhārayate dhārayati – dhṛtyā hi dhāryamāṇāḥ ucchāstramārgaviṣayāḥ na bhavanti – yogena samādhinā avyabhicāriṇyā nityasamādhyanugatayā ityarthaḥ etaduktaṃ bhavati – avyabhicāriṇyā dhṛtyā manaḥ prāṇendriyakriyāḥ dhāryamāṇāḥ yogena dhārayatīti yā evaṃ lakṣaṇā dhṛtiḥ sā pārtha, sāttvikī.",
           ]),
        _v([
            "yayā tu dharmakāmārthān dhṛtyā dhārayate'rjuna |",
            "prasaṅgena phalākāṅkṣī dhṛtiḥ sā pārtha rājasī",
        ], "|| 34 ||",
           "But the steadfastness by which one holds to dharma, desire and wealth, craving their fruits through attachment, Arjuna, is rājasa, Pārtha.",
           bhashya=[
               "yayā iti. yayā tu dharmakāmārthān dharmaśca kāmaścārthaśca dharmakāmārthāḥ tān dharmakāmārthān dhṛtyā yayā dhārayate manasi nityameva kartavyarūpān avadhārayati he arjuna, prasaṅgena yasya yasya dharmāderdhāraṇa prasaṅgaḥ tena tena prasaṅgena phalākāṅkṣī ca bhavati yaḥ puruṣaḥ, tasya yā dhṛtiḥ, sā pārtha, rājasī bhavati.",
           ]),
        _v([
            "yayā svapnaṃ bhayaṃ śokaṃ viṣādaṃ madameva ca |",
            "na vimuñcati durmedhā dhṛtiḥ sā pārtha tāmasī",
        ], "|| 35 ||",
           "The steadfastness by which a dull-witted man does not let go of sleep, fear, grief, despondency and conceit is tāmasa, Pārtha.",
           bhashya=[
               "yayā iti. yayā svapnaṃ nidrāṃ bhayaṃ trāsaṃ śokaṃ viṣādaṃ viṣaṇṇatāṃ madaṃ viṣayasevāṃ ātmanaḥ bahumanyamānaḥ matta iva madameva ca manasi nityameva kartavyarūpatayā kurvanna vimuñcati dhārayatyeva durmedhāḥ kutsitamedhāḥ puruṣaḥ yaḥ tasya dhṛtiḥ yā, sā tāmasī matā.",
           ]),
        _v([
            "sukhaṃ tvidānīṃ trividhaṃ śṛṇu me bharatarṣabha |",
            "abhyāsādramate yatra duḥkhāntaṃ ca nigacchati",
        ], "|| 36 ||",
           "And now hear from me, O best of the Bhāratas, of the threefold happiness, in which one delights through practice and comes to the end of sorrow.",
           bhashya=[
               {"text": "guṇabhedena kriyāṇāṃ kārakāṇāṃ ca trividho bheda uktaḥ atha idānīṃ sukhasya ca phalasya ca trividho bhedaḥ ucyate –", "intro": True},
               "sukhamiti. sukhaṃ tvidānīṃ trividhaṃ śṛṇu, samādhānaṃ kurvityetat, me mama bharatarṣabha. abhyāsāt paricayāt āvṛtteḥ, ramate ratiṃ pratipadyate, yatra yasmin sukhānubhave duḥkhāntaṃ ca duḥkhāvasānaṃ duḥkhopaśamaṃ ca nigacchati niścayena prāpnoti.",
           ]),
        _v([
            "yattadagre viṣamiva pariṇāme'mṛtopamam |",
            "tatsukhaṃ sāttvikaṃ proktamātmabuddhiprasādajam",
        ], "|| 37 ||",
           "That which is like poison at first but like nectar in the end, born of the serenity of one's own understanding, is declared to be sāttvika happiness.",
           bhashya=[
               "yaditi. yattatsukhaṃ agre pūrvaṃ prathamasannipāte jñānavairāgyadhyānasamādhyārambhe atyantāyāsapūrvakatvāt viṣamiva duḥkhātmakaṃ bhavati, pariṇāme jñānavairāgyādiparipākajaṃ sukhaṃ amṛtopamaṃ, tatsukhaṃ sāttvikaṃ proktaṃ vidvadbhiḥ, ātmano buddhirātmabuddhiḥ, ātmabuddheḥ prasādaḥ nairmalyaṃ salilasya iva svacchatā, tataḥ jātamātmabuddhi prasādajaṃ. ātmaviṣayā vā ātmāvalambanā vā buddhiḥ ātmabuddhiḥ tatprasādaprakarṣādvā jātamityetat. tasmātsāttvikaṃ tat.",
           ]),
        _v([
            "viṣayendriyasaṃyogādyattadagre'mṛtopamam |",
            "pariṇāme viṣamiva tatsukhaṃ rājasaṃ smṛtam",
        ], "|| 38 ||",
           "That which arises from the contact of the senses with their objects, like nectar at first but like poison in the end, is held to be rājasa.",
           bhashya=[
               "viṣaya iti. viṣayendriya saṃyogājjāyate yatsukhaṃ tatsukhamagre prathamakṣaṇe amṛtopamaṃ amṛtasamaṃ, pariṇāme viṣamiva, balavīryarūpaprajñāmedhā dhanotsāhahānihetutvāt adharmatajjanitanarakādi hetutvācca pariṇāme tadupabhogapariṇāmānte viṣamiva, tatsukhaṃ rājasam smṛtam.",
           ]),
        _v([
            "yadagre cānubandhe ca sukhaṃ mohanamātmanaḥ |",
            "nidrā''lasyapramādotthaṃ tattāmasamudāhṛtam",
        ], "|| 39 ||",
           "That happiness which deludes the self both at the beginning and in its consequence, arising from sleep, sloth and heedlessness, is declared to be tāmasa.",
           bhashya=[
               "yadagre iti. yadagre cānubandhe ca avasāne cottarakāle sukhaṃ mohanaṃ mohakaramātmanaḥ, nidrā''lasyapramādotthaṃ nidrā ca ālasyaṃ ca pramādaśceti etebhyassamuttiṣṭhatīti nidrā''lasyapramādotthaṃ, tat tāmasamudāhṛtam.",
           ]),
        _v([
            "na tadasti pṛthivyāṃ vā divi deveṣu vā punaḥ |",
            "sattvaṃ prakṛtijairmuktaṃ yadebhiḥ syāttribhirguṇaiḥ",
        ], "|| 40 ||",
           "There is no being on earth, nor again in heaven among the gods, that is free from these three guṇas born of prakṛti.",
           bhashya=[
               {"text": "atha idānīṃ prakaraṇopasaṃhārārthaḥ śloka ārabhyate –", "intro": True},
               "na tat iti. na tat asti tat nāsti pṛthivyāṃ vā manuṣyādiṣu sattvaṃ prāṇijātaṃ anyadvā aprāṇijātaṃ, divi deveṣu vā punaḥ sattvaṃ prakṛtijaiḥ prakṛtitaḥ jātaiḥ ebhistribhirguṇaiḥ sattvābhirmuktaṃ parityaktaṃ yat syāt bhavet “na tadastī” ti pūrveṇa sambandhaḥ.",
           ]),
        _v([
            "brāhmaṇakṣatriyaviśāṃ śūdrāṇāṃ ca parantapa |",
            "karmāṇi pravibhaktāni svabhāvaprabhavairguṇaiḥ",
        ], "|| 41 ||",
           "The duties of brāhmaṇas, kṣatriyas and vaiśyas, and of śūdras, O scorcher of foes, are distributed according to the guṇas arising from their own nature.",
           bhashya=[
               {"text": "sarvaḥ saṃsāraḥ kriyākārakaphalalakṣaṇaḥ sattvarajastamoguṇātmako avidyāparikalpitaḥ samūlaḥ anarthaḥ uktaḥ vṛkṣarūpakalpanayā ca “ūrdhvamūla” (15.1) mityādinā. “taṃ cāsaṅga śastreṇa dhṛḍhena chitvā tataḥ padaṃ tatparimārgitavyaṃ” (14.3,4) iti ca uktaṃ. tatra ca sarvasya triguṇātmakatvāt saṃsārakāraṇa nivṛttyanupapattau prāptāyāṃ, yathā tannivṛttissyāt tathā vaktavyaṃ, sarvaśca gītāśāstrārthaḥ upasaṃhartavyaḥ, etāvāneva ca sarvavedasmṛtyarthaḥ puruṣārthamicchadbhiranuṣṭheyaḥ ityevamarthaṃ ca “brāhmaṇakṣatriyaviśāṃ” ityādiḥ ārabhyate –", "intro": True},
               "brāhmaṇa iti. brāhmaṇāśca kṣatriyāśca viśaśca brāhmaṇakṣatriyaviśaḥ teṣāṃ brāhmaṇakṣatriyaviśāṃ, śūdrāṇāṃ ca – śūdrāṇāmasamāsakaraṇamekajātitve sati vedānadhikārāt – he parantapa, karmāṇi pravibhaktāni itaretaravibhāgena vyavasthāpitāni. kena? svabhāvaprabhavairguṇaiḥ svabhāvaḥ īśvarasya prakṛtiḥ triguṇātmikā māyā sā prabhavaḥ yeṣāṃ guṇānāṃ te svabhāvaprabhavāḥ taiḥ, śamādīni karmāṇi pravibhaktāni brāhmaṇādīnām.",
               "athavā brāhmaṇasvabhāvasya sattvaguṇaḥ prabhavaḥ kāraṇaṃ, tathā kṣatriyasvabhāvasya sattvopasarjanaṃ rajaḥprabhavaḥ, vaiśyasvabhāvasya tama upasarjanaṃ rajaḥ prabhavaḥ, śūdrasvabhāvasya rajaḥupasarjanaṃ tamaḥ prabhavaḥ praśāntyaiśvaryehāmūḍhatāsvabhāvadarśanāt caturṇāṃ.",
               "athavā janmāntarakṛtasaṃskāraḥ prāṇināṃ vartamāna janmanisvakāryābhimukhatvenābhivyaktasvabhāvaḥ sa prabhavo yeṣāṃ guṇānāṃ te svabhāvaprabhavāḥ, guṇāḥ, guṇaprādurbhāvasya niṣkāraṇatvānupapatteḥ “svabhāvaḥ kāraṇaṃ” iti ca kāraṇa viśeṣopādānāṃ evaṃsvabhāva prakṛtabhavaiḥ sattvarajastamobhirguṇaiḥ svakāryānurūpeṇa śamādīni karmāṇi pravibhaktāni.",
               "nanu śāstrapravibhaktāni śāstreṇa vihitāni brāhmaṇādīnāṃ śamādīni karmāṇi, kathamucyate sattvādiguṇa pravibhaktāni iti? naiṣa doṣaḥ, śāstreṇāpi brāhmaṇādīnāṃ sattvādi guṇa viśeṣāpekṣayaiva śamādīni karmāṇi pravibhaktāni, na guṇānapekṣayā, iti śāstra pravibhaktānyapi karmāṇi guṇa pravibhaktānītyucyate.",
           ]),
        _v([
            "śamo damastapaḥ śaucaṃ kṣāntirārjavameva ca |",
            "jñānaṃ vijñānamāstikyaṃ brahmakarma svabhāvajam",
        ], "|| 42 ||",
           "Calm, self-restraint, austerity, purity, forbearance and uprightness, knowledge, realisation and faith in the hereafter are the duties of the brāhmaṇa, born of his nature.",
           bhashya=[
               {"text": "kāni punastāni karmāṇi iti ucyate –", "intro": True},
               "śama iti. śamaḥ damaśca yathāvyākhyātārthau, tapaḥ yathoktaṃ śārīrādi, (17.14'16) śaucaṃ vyākhyātaṃ (16.3) kṣāntiḥ kṣamā ārjavaṃ ṛjutaiva ca jñānaṃ vijñānaṃ āstikyaṃ āstikabhāvaḥ śraddadhānatā āgamārtheṣu, brahmakarma brāhmaṇajāteḥ karma karma svabhāvajam – yaduktaṃ “svabhāvaprabhavairguṇaiḥ pravibhaktānī”ti tadevoktaṃ svabhāvajamiti.",
           ]),
        _v([
            "śauryaṃ tejo dhṛtirdākṣyaṃ yuddhe cāpyapalāyanam |",
            "dānamīśvarabhāvaśca kṣattrakarma svabhāvajam",
        ], "|| 43 ||",
           "Valour, vigour, steadfastness, skill, not fleeing in battle, generosity and lordliness are the duties of the kṣatriya, born of his nature.",
           bhashya=[
               "śauryamiti. śauryaṃ śūrasya bhāvaḥ, tejaḥ prāgalbhyaṃ, dhṛtiḥ dhāraṇaṃ, sarvāvasthāsu anavasādaḥ bhavati yayā dhṛtyā uttambhitasya dākṣyaṃ dakṣasya bhāvaḥ sahasā pratyutpanneṣu kāryeṣu avyāmohena pravṛttiḥ, yuddhe cāpyapalāyanaṃ aparāṅmukhī bhāvaḥ śatrubhyaḥ, dānaṃ deyadravyeṣu muktahastatā, īśvarabhāvaśca īśvarasya bhāvaḥ, prabhuśakti prakaṭīkaraṇaṃ īśitavyān prati, kṣātraṃ karma kṣatrajāteḥ vihitaṃ karma kṣātraṃ karma svabhāvajam.",
           ]),
        _v([
            "kṛṣigaurakṣyavāṇijyaṃ vaiśyakarma svabhāvajam |",
            "paricaryātmakaṃ karma śūdrasyāpi svabhāvajam",
        ], "|| 44 ||",
           "Agriculture, cattle-keeping and trade are the duties of the vaiśya, born of his nature; work of the nature of service is the duty of the śūdra, born of his nature.",
           bhashya=[
               "kṛṣi iti. kṛṣigaurakṣyavāṇijyaṃ kṛṣiśca gaurakṣyaṃ ca vāṇijyaṃ ca kṛṣigaurakṣyavāṇijyaṃ, kṛṣiḥ bhūmeḥ vilekhanaṃ, gaurakṣyaṃ gāḥ rakṣatīti gorakṣaḥ tasya bhāvaḥ gaurakṣyaṃ, paśupālyamityarthaḥ, vāṇijyaṃ vaṇikkarma krayavikrayādilakṣaṇaṃ vaiśyakarma vaiśyajāteḥ karma vaiśyakarma svabhāvajam. paricaryātmakaṃ śuśrūṣāsvabhāvaṃ karma śūdrasyāpi svabhāvajam.",
           ]),
        _v([
            "sve sve karmaṇyabhiratassaṃsiddhiṃ labhate naraḥ |",
            "svakarmanirataḥ siddhiṃ yathā vindati tacchṛṇu",
        ], "|| 45 ||",
           "Devoted each to his own duty, a man attains perfection. Hear how one devoted to his own duty finds perfection.",
           bhashya=[
               {"text": "eteṣāṃ jātivihitānāṃ karmaṇāṃ samyaganuṣṭhitānāṃ svargaprāptiḥ phalaṃ svabhāvataḥ, “varṇāḥ āśramāśca svakarmaniṣṭhā pretya karmaphalamanubhūyā tataśśeṣeṇa viśiṣṭadeśa jātikuladharmāyuśśruta – vṛttavittaḥ sukhamedhaso janma pratipadyante” ityādi smṛtibhyaḥ, purāṇe ca varṇināmāśramiṇāṃ ca lokaphalabhedaviśeṣa – smaraṇāt. kāraṇāntarāttu idaṃ vakṣyamāṇaṃ phalamucyate –", "intro": True},
               "svesve iti. svesve yathoktalakṣaṇabhede karmaṇi abhirataḥ tatparaḥ, saṃsiddhiṃ svakarmānuṣṭhānāt aśuddhi kṣaye sati kāyendriyāṇāṃ jñāniṣṭhāyogyatālakṣaṇāṃ saṃsiddhiṃ labhate prāpnoti naraḥ adhikṛtaḥ puruṣaḥ, kiṃ svakarmānuṣṭhānata eva sākṣāt saṃsiddhiḥ? na. kathaṃ tarhi? svakarmanirataḥ siddhiṃ yathā yena prakāreṇa vindati, tacchṛṇu.",
           ]),
        _v([
            "yataḥ pravṛttirbhūtānāṃ yena sarvamidaṃ tatam |",
            "svakarmaṇā tamabhyarcya siddhiṃ vindati mānavaḥ",
        ], "|| 46 ||",
           "By worshipping, through his own duty, him from whom beings arise and by whom all this is pervaded, a man attains perfection.",
           bhashya=[
               "yata iti. yataḥ yasmāt pravṛttiḥ utpattiḥ ceṣṭā vā yasmāt antaryāmiṇaḥ īśvarāt bhūtānāṃ prāṇināṃ syāt, yena īśvareṇa sarvaṃ idaṃ jagat tataṃ vyāptaṃ svakarmaṇā pūrvoktena prativarṇaṃ taṃ īśvaramabhyarcya pūjayitvā ārādhya kevalaṃ jñānaniṣṭhāyogyatā lakṣaṇāṃ siddhiṃ vindati mānavaḥ manuṣyaḥ.",
           ]),
        _v([
            "śreyān svadharmo viguṇaḥ paradharmātsvanuṣṭhitāt |",
            "svabhāvaniyataṃ karma kurvannāpnoti kilbiṣam",
        ], "|| 47 ||",
           "Better one's own dharma, though imperfect, than the dharma of another well performed. Doing the action prescribed by his own nature, one incurs no sin.",
           bhashya=[
               {"text": "yataḥ evaṃ, ataḥ –", "intro": True},
               "śreyān iti. śreyān praśasyataraḥ svodharmaḥ svadharmaḥ viguṇo'pi iti api śabdo draṣṭavyaḥ, paradharmāt svanuṣṭhitvāt. svabhāva niyataṃ svabhāvena niyataṃ, yaduktaṃ svabhāvajamiti, tadevoktaṃ svabhāvaṃ niyatamiti, yathā viṣajātasya kṛmeḥ viṣaṃ na doṣakaraṃ, tathā svabhāvaniyataṃ karma kurvannāpnoti kilbiṣaṃ pāpam.",
           ]),
        _v([
            "sahajaṃ karma kaunteya sadoṣamapi na tyajet |",
            "sarvārambhā hi doṣeṇa dhūmenāgnirivāvṛtāḥ",
        ], "|| 48 ||",
           "One should not give up the duty one is born to, son of Kuntī, even if it has defects; for all undertakings are enveloped by defects, as fire by smoke.",
           bhashya=[
               {"text": "svabhāvaniyataṃ karma kurvāṇo viṣaja iva kṛmiḥ kilbiṣaṃ nāpnotītyuktaṃ, paradharmaśca bhayāvahaḥ iti, anātmajñaśca “na hi kaścit kṣaṇamapi akarmakṛttiṣṭhati” iti ataḥ –", "intro": True},
               "sahajamiti. sahajaṃ saha janmanaiva utpannaṃ. kiṃ tat? karma, kaunteya, sadoṣamapi triguṇātmakatvāt na tyajet, sarvārambhāḥ ārabhyanta ityārambhāḥ sarvakarmāṇītyetat, prakaraṇāt ye kecit ārambhāḥ svadharmāḥ paradharmāśca, te sarve hi yasmāt – triguṇātmakatvaṃ atra hetuḥ – triguṇātmakatvāt doṣeṇa dhūmena sahajena agniriva, āvṛtāḥ. sahajasya karmaṇaḥ svadharmākhyasya parityāgena paradharmānuṣṭhāne'pi doṣānnaiva mucyate, bhayāvahaśca paradharmaḥ. na ca śakyate aśeṣataḥ tyaktuṃ ajñena karma yataḥ, tasmāt na tyajet ityarthaḥ.",
               "kimaśeṣataḥ tyaktuṃ aśakyaṃ karma iti na tyajet? kiṃ vā sahajasya karmaṇaḥ tyāge doṣo bhavatīti? kiṃ cātaḥ, yadi tāvat aśeṣataḥ tyaktuṃ aśakyaṃ iti na tyājyaṃ sahajaṃ karma, evaṃ tarhyaśeṣatastyāge guṇa eva syāditi siddhaṃ bhavati. satyamevaṃ, aśeṣatastyāga eva nopapadyata iti cet, kiṃ nityapracalitātmakaḥ puruṣaḥ? yathā sāṅkhyānāṃ guṇāḥ, kiṃ vā kriyaiva kārakaṃ yathā bauddhānāṃ skandhāḥ kṣaṇapradhvaṃsinaḥ, ubhayathā'pi, karmaṇaḥ aśeṣataḥ tyāgaḥ na sambhavati, atha tṛtīyo'pi pakṣaḥ – yadā karoti tadā sakriyaṃ vastu. yadā na karoti, tadā sakriyaṃ vastu. yadā na karoti, tadā niṣkriyaṃ tadeva. tatraivaṃ sati śakyaṃ karmāśeṣatastyaktuṃ. ayaṃ tvasmin tṛtīye pakṣe viśeṣaḥ – na nityapracalitaṃ vastu, nāpi kriyaiva kārakaṃ kiṃ tarhi? vyavasthite dravye avidyamānā kriyā utpadyate vidyamānā ca vinaśyati, śuddhaṃ taddravyaṃ śaktimadavatiṣṭhate. ityevamāhuḥ kāṇādāḥ, tadeva ca kārakamiti asmin pakṣe ko doṣaḥ iti.",
               "ayameva tu doṣaḥ – yatastvabhāgavataṃ matamidaṃ, kathaṃ jñāyate? yataḥ āha bhagavān “nāsato vidyate bhāvaḥ” (2.16) ityādi. kāṇādānāṃ hi asataḥ bhāvaḥ, sataścābhāvaḥ. iti, idaṃ matamabhāgavataṃ, abhāgavatamapi nyāyavaccet ko doṣaḥ iti cet, ucyate – doṣavattvidaṃ sarvapramāṇavirodhāt. kathaṃ? yadi tāvaddvyaṇukādi dravyaṃ prāgutpatteḥ atyantameva asat, utpannaṃ ca sthitaṃ kañcitkālaṃ punaḥ atyantameva asattvamāpadyate, tathā ca satyasadeva sat jāyate, sadeva asattvaṃ āpadyate, abhāvaḥ bhāvo bhavati, bhāvaścābhāvo bhavatīti, tatrābhāvo jāyamānaḥ prāgutpatteśśaśaviṣāṇakalpaḥ samavāyyasamavāyinimittākhyaṃ kāraṇamapekṣya jāyate iti, na caivamabhāva utpadyate, kāraṇaṃ cāpekṣate iti śakyaṃ vaktuṃ, asatāṃ śaśaviṣāṇādīnāmadarśanāt, bhāvātmakāścet ghaṭādayaḥ utpādyamānāḥ, kiñcit abhivyaktimātre kāraṇaṃ apekṣya utpadyante iti śakyaṃ pratipattuṃ. kiṃ ca, asataśca sadbhāve sataścāsadbhāve na kvacit pramāṇaprameyavyavahāreṣu viśvāsaḥ kasyacitsyāt, “satsadevāsadeveti” niścayānupapatteḥ. kiñca – utpadyate iti dvyaṇukādeḥ dravyasya svakāraṇasattāsambandhaṃ āhuḥ. prāk utpatteśca asat, paścāt kāraṇavyāpāraṃ apekṣya svakāraṇaiḥ paramāṇubhiḥ sattayā ca samavāyalakṣaṇena sambandhena sambadhyate. sambaddhaṃ sat kāraṇasamavetaṃ sat bhavati. tatra vaktavyaṃ kathaṃ asataḥ svaṃ kāraṇaṃ bhavet, sambandhaḥ vā kenacit syāt? na hi vandhyāputrasya svaṃ kāraṇaṃ, sambandhaḥ vā kenacit pramāṇataḥ kalpayituṃ śakyate.",
               "nanu naivaṃ vaiśeṣikaiḥ abhāvasya sambandhaḥ kalpyate. dvyaṇukādīnāṃ hi dravyāṇāṃ svakāraṇasamavāyalakṣaṇaḥ sambandhaḥ satāmeva ucyate iti. nanu sambandhāt. prāk sattvānabhyupagamāt. na hi vaiśeṣikaiḥ kulāladaṇḍa cakrādivyāpārāt prāk ghaṭādīnāmastitvaṃ iṣyate. na ca mṛda eva ghaṭādyākāraprāpti – micchanti. tataśca asata eva sambandhaḥ pāriśeṣyādiṣṭo bhavati.",
               "nanu asato'pi samavāyalakṣaṇaḥ sambandhaḥ na viruddhaḥ. na, vandhyāputrādīnāmadarśanāt. ghaṭādereva prāgabhāvasya svakāraṇa sambandho bhavatīti na vandhyāputrādeḥ, abhāvasya tulyatve'pi iti viśeṣaḥ abhāvasya vaktavyaḥ, ekasya abhāvaḥ, dvayoḥ abhāvaḥ sarvasyābhāvaḥ, prāgabhāvaḥ pradhvaṃsābhāvaḥ, itaretarābhāvaḥ, atyantābhāvaḥ iti ca lakṣaṇato na kenacidviśeṣo darśayituṃ śakyaḥ. asati ca viśeṣe ghaṭasya prāgabhāva eva kulālādibhirghaṭabhāvamāpadyate sambadhyate ca, bhāvena, kapālākhyena, svakāraṇena sambaddhaśca sarvavyavahārayogyaśca bhavati, na tu ghaṭasyaiva pradhvaṃsādyabhāvaḥ abhāvatve satyapi iti pradhvaṃsā bhāvānāṃ na kvacit vyavahārayogyatvam prāgabhāvasyaiva dvyaṇukādidravyākhyasya utpattyādi – vyavahārārhatvaṃ ityedasamañjasaṃ, abhāvatvāviśeṣāt atyantapradhvaṃsābhāvayoriva. nanu naiva asmābhiḥ prāgabhāvasya bhāvāpattiḥ ucyate. bhāvasyaiva tarhi bhāvāpattiḥ, yathā ghaṭasya ghaṭāpattiḥ paṭasya vā paṭāpattiḥ etadapi abhāvasya bhāvāpatti vadeva pramāṇa viruddhaṃ.",
               "sāṅkhyasyāpi yaḥ pariṇāmapakṣaḥ so'pi apūrvadharmotpattivināśāṅgī karaṇāt vaiśeṣika – pakṣānna viśiṣyate, abhivyaktitirobhāvāṅgīkaraṇe'pi abhivyaktitirobhāvayoḥ vidyamānatvāvidyamānatvanirūpaṇe pūrvavadeva pramāṇavirodhaḥ. etena kāraṇasyaiva saṃsthāna mutpattyādi ityetadapi pratyuktam. pāriśeṣyāt – sat ekameva vastvavidyayotpattivināśādidharmaiḥ anekadhā naṭavat vikalpyate iti. idaṃ bhāgavataṃ mataṃ uktaṃ, “nāsato vidyate bhāvaḥ” (2.16) ityasmin śloke, satpratyayasya avyabhicārāt vyabhicārācca itareṣāmiti.",
               "kathaṃ tarhyātmano avikriyatve aśeṣataḥ karmaṇastyāgo nopapadyata iti? yadi vastubhūtāḥ guṇāḥ. yadi vā avidyā kalpitāḥ taddharmaḥ karma, tadātmanyavidyayādhyāropitamevetyavidvān) “na hi kaścit kṣaṇamapi aśeṣatastyaktuṃ śaknoti” (3.5) ityuktam. vidvāṃstu punaḥ vidyayā avidyāyāṃ nivṛttāyāṃ śaknotyevāśeṣataḥ karma parityaktuṃ avidyā'dhyāropitasya śeṣānupapatteḥ. na hi taimirikadṛṣṭyā adhyāropitasya dvicandrādestimirāpagame'pi śeṣaḥ avatiṣṭhate, evaṃ ca sati idaṃ vacanamupapannaṃ “sarva karmāṇi” manasā” (5.13) ityādi, “sve sve karmaṇyabhiratassaṃsiddhiṃ labhate naraḥ”, (18.45) “sakarmaṇā tamabhyarcya siddhiṃ vindati mānavaḥ” (18.46) iti ca.",
           ]),
        _v([
            "asaktabuddhi ssarvatra jitātmā vigataspṛhaḥ |",
            "naiṣkarmyasiddhiṃ paramāṃ sannyāsenādhigacchati",
        ], "|| 49 ||",
           "He whose understanding is unattached everywhere, who has conquered himself and from whom longing has gone, attains through renunciation the supreme perfection of freedom from action.",
           bhashya=[
               {"text": "yā karmajā siddhiḥ uktā jñānaniṣṭhāyogyatālakṣaṇā, tasyāḥ phalabhūtā naiṣkarmyasiddhiḥ jñānaniṣṭhālakṣaṇā ca vyaktavyeti ślokaḥ ārabhyate –", "intro": True},
               "asaktabuddhiḥ iti. asaktabuddhiḥ asaktā saṅgarahitā buddhiḥ antaḥkaraṇaṃ yasya saḥ asaktabuddhiḥ sarvatra putradārādiṣu āsaktinimitteṣu jitātmā, jito vaśīkṛtaḥ ātmā antaḥkaraṇaṃ yasya sa jitātmā, vigataspṛhaḥ vigatā spṛhā tṛṣṇā tadevajīvitabhogeṣu yasmāt saḥ vigataspṛhaḥ ya evambhūtaḥ ātmajñaḥ saḥ naiṣmaryasiddhiṃ nirgatāni karmāṇi yasmāt niṣkriyabrahmātma sambodhāt sa niṣkarmā tasya bhāvo naiṣkarmyaṃ, naiṣkarmyaṃ ca tat siddhiśca sā naiṣkarmyasiddhiḥ niṣkarmatvasya vā niṣkriyātma svarūpāvasthānalakṣaṇasya siddhiḥ niṣpattiḥ, tāṃ naiṣkarmya siddhiṃ paramāṃ prakṛṣṭāṃ karmajasiddhi vilakṣaṇāṃ sadyomuktyavasthāna rūpāṃ, sannyāsena samyagdarśanena tatpūrvakena vā sarvakarma sannyāsena, adhigacchati prāpnoti. tathācoktaṃ – sarvakarmāṇi manasā sannyasya, naiva kurvanna kārayannāste” (5.13) iti.",
           ]),
        _v([
            "siddhiṃ prāpto yathā brahma tathā'pnoti nibodha me |",
            "samāsenaiva kaunteya niṣṭhā jñānasya yā parā",
        ], "|| 50 ||",
           "Learn from me in brief, son of Kuntī, how, having attained perfection, he attains Brahman — that highest consummation of knowledge.",
           bhashya=[
               {"text": "pūrvoktena svakarmānuṣṭhānena īśvarābhyarcanarūpeṇa janitāṃ prāguktalakṣaṇāṃ siddhiṃ prāptasyotpannātmavivekajñānasya kevalātmajñānaniṣṭhārūpā naiṣkarmyalakṣaṇā siddhiḥ yena krameṇa bhavati, tadvaktavyamityāha –", "intro": True},
               "siddhimiti. siddhiṃ prāptaḥ svakarmaṇeśvaraṃ samabhyarcya tatprasādajāṃ kāyendriyāṇāṃ jñānaniṣṭhāyogyatālakṣaṇāṃ siddhiṃ prāptaḥ – siddhiṃ prāptaḥ iti tadanuvāda uttarārthaḥ. kiṃ taduttaraṃ yadarthaḥ anuvādaḥ iti ucyate – yathā yena prakāreṇa jñāniniṣṭhārūpeṇa brahma paramātmānaṃ āpnoti. tathā taṃ prakāraṃ jñānaniṣṭhāprāptikramaṃ me mama vacanāt nibodha tvaṃ niścayena avadhāraya ityetat, kiṃ vistareṇa? na ityāha – samāsenaiva saṅkṣepeṇaiva, he kaunteya, yathā brahma prāpnoti tathā nibodheti anena yā pratijñatā brahmaprāptiḥ tāṃ idantayā darśayitumāha – “niṣṭhā jñānasya yā parā” iti. niṣṭhā paryavasānaṃ parisamāptiḥ ityetat, kasya brahmajñānasya, yā parā, sā kīdṛśī? yādṛśaṃ ātma jñānaṃ kīdṛk tat? yādṛśaḥ ātmā? kīdṛśa saḥ? yādṛśo bhagavatā uktaḥ, (18.17) upaniṣadvā kyaiśca nyāyataśca.",
               "nanu viṣayākāraṃ jñānaṃ. na jñānaviṣayaḥ nāpyākāravān ātmeṣyate kvacit. nanuḥ “ādityavarṇaṃ” (śve.u.3.8) “bhārūpaḥ” (chāṃ.u.3.14.2) “svayañjyotiḥ” (bṛ.u. 4.3.9) ityākāra vattvamātmanaḥ śrūyate. nanu tamorūpatva pratiṣedhārthatvāt teṣāṃ vākyānām – dravyaguṇādyākārapratiṣedhe ātmanaḥ tamorūpatve prāpte tatpratiṣedhārthāni “ādityavarṇaṃ” ityādīni vākyāni. “arūpaṃ” (kaṭha. 3.15) iti ca viśeṣataḥ rūpa pratiṣedhāt. aviṣayatvāccha – “na sandṛśe tiṣṭhati rūpamasya na cakṣuṣā paśyati kaścanainaṃ. (śve.u.4.20) “aśabdamasparśaṃ” (kaṭha.u. 3.15) ityādeḥ, tasmāt ātmākāraṃ jñānamityanupapannam. kathaṃ tarhi ātmanaḥ jñānaṃ? sarvaṃ hi yadviṣayaṃ yat jñānaṃ tattadākāraṃ bhavati, nirākāraśca ātmā ityuktaṃ. jñānātmanoścobhayornirākāratve kathaṃ tadbhāvanā niṣṭheti. na atyanta nirmalatvātisvacchatvātisūkṣmatvopapatteḥ ātmanaḥ. buddheścātmavannairalyādupapatteḥ ātmacaitanyākāra bhāsatvopapattiḥ. buddhyābhāsaṃ manaḥ tadābhāsāni indriyāṇi, indriyābhāsaśca dehaḥ. ataḥ laukikaiḥ dehamātre eva ātmadṛṣṭi kriyate.",
               "dehacaitanyavādinaśca lokāyatikāḥ “caitanyaviśiṣṭaḥ kāyaḥ puruṣaḥ” ityāhuḥ. tathā cānye indriyacaitanyavādinaḥ, anye manaścaitanyavādinaḥ, anye buddhicaitanyavādinaḥ tato'pyāntaramavyaktamavyākṛtākhyaṃ avidyāvasthamātmatvena pratipannāḥ kecit. sarvatra buddhyādidehānte ātmacaitanyā bhāsatā ātmabhrāntikāraṇamityataśca ātmaviṣayaṃ jñānaṃ na vidhātavyaṃ, kiṃ tarhi? nāmarūpādya nātmādhyāropaṇa nivṛttirevakāryā. nātmacaitanyavijñānaṃ kāryaṃ avidyā'dhyāropitasarvapadārthākāraiḥ eva viśiṣṭatayā dṛśyamānatvāt iti. ata eva hi vijñānavādino bauddhāḥ vijñānavyatirekeṇa vastvenāstīti pratipannāḥ, pramāṇāntara nirapekṣatāṃ ca svasaṃviditatvābhyupagamena. tasmādavidyā'dhyāropita nirākaraṇamātraṃ brahmaṇi kartavyaṃ, na tu brahmavijñāne yatnaḥ, atyantaprasiddhatvāt. avidyākalpitanāmarūpaviśeṣākārapahṛtabuddhīnāṃ atyantaprasiddhaṃ suvijñeyaṃ āsannataramātmabhūtamapyaprasiddhaṃ durvijñeyamatidūramanyadiva ca pratibhāti avivekināṃ. bāhyākāranivṛtta buddhīnāṃ tu labdhagurvātmaprasādānāṃ nātaḥ paraṃ sukhaṃ suprasiddhaṃ suvijñeyaṃ svāsannataramasti, tathācoktaṃ – “pratyakṣāvagamaṃ dharmya” (9.2) mityādi.",
               "kecittu paṇḍitammanyāḥ “nirākāratvāt ātmavastu na upaitibuddhiḥ. ataḥ dussādhyāsamyak jñānaniṣṭhā” ityāhuḥ, satyam, evaṃ gurusampradāyarahitānāṃ aśruta vedāntānāṃ atyanta bahirviṣayāsakta buddhīnāṃ samyakpramāṇeṣu akṛtaśramāṇāṃ. tadviparītānāṃ tu laukikagrāhyagrāhakadvaitavastuni sadbuddhiḥ nitarāṃ dussampādyā, ātmacaitanya vyatirekeṇa vastvantarasyānupalabdheḥ, yathā ca “etadevameva, nānyathā” iti avocāma, uktaṃ ca bhagavatā “yasyāṃ jāgrati bhūtāni sā niśā paśyato muneḥ” (2.69) iti. tasmāt bāhyākārabheda buddhiḥ nivṛttireva ātmasvarūpāvalambanakāraṇaṃ, na hi ātmā nāma kasyacit kadācidaprasiddhaḥ prāpyaḥ, heyaḥ. upādeyo vā, aprasiddhe hi tasmin ātmani svārthāḥ sarvāḥ pravṛttayaḥ vyarthāḥ prasajyeran, na ca dehādyacetanārthatvaṃ śakyaṃ kalpayituṃ, na ca sukhārthaṃ sukhaṃ duḥkhārthaṃ duḥkhaṃ. ātmāvagatyavasānārthatvācca sarvavyavahārasya, (bra.sū.3.4.26.27) tasmāt yathā svadehasya paricchedāya na pramāṇāntarāpekṣā tato'pi ātmanaḥ antaratamatvāt tadavagatiṃ prati na pramāṇāntarāpekṣā. iti ātmajñānaniṣṭhā vivekināṃ suprasiddheti siddham.",
               "yeṣāmapi nirākāraṃ jñānaṃ apratyakṣaṃ teṣāmapi jñānavaśenaiva jñeyāvagatiriti jñānamatyanta prasiddhaṃ sukhādidevetyabhyupaṅgatavyaṃ. jijñāsānupapatteśca aprasiddhaṃ cet, jñānaṃ jñeyavat jijñāsyeta. yathā jñeyaṃ ghaṭādilakṣaṇaṃ jñānena jñātā vyāptumicchati tathā jñānamapi jñānāntareṇa jñātā vyāptumicchet. na caitadasti, ataḥ atyantaprasiddhaṃ jñānaṃ, jñātā'pi ata eva prasiddhaḥ iti. tasmād jñāne yatno na kartavyaḥ, kiṃ tu anātmani ātmabuddhi nivṛttāneva. tasmāt jñānaniṣṭhā susampādyā.",
           ]),
        _v([
            "buddhyā viśuddhayā yukto dhṛtyā'tmānaṃ niyamya ca |",
            "śabdādīn viṣayāṃstyaktvā rāgadveṣau vyudasya ca",
        ], "|| 51 ||",
           "Endowed with a purified understanding, restraining the self with steadfastness, giving up sound and the other objects, and setting aside attraction and aversion;",
           bhashya=[
               {"text": "sā iyaṃ jñānasya parā niṣṭhā ucyate, kathaṃ kāryā iti –", "intro": True},
               "buddhyā iti. buddhyā adhyavasāyalakṣaṇayā viśuddhayā māyārahitayā yuktaḥ sampannaḥ, dhṛtyā dhairyeṇa ātmānaṃ kāryakaraṇasaṅghātaṃ niyamya ca niyamanaṃ kṛtvā vaśīkṛtya, śabdādīn śabdaḥ ādiḥ eṣāṃ tān viṣayān tyaktvā sāmarthyāt śarīrasthitimātrahetu– bhūtān kevalān muktvā tataḥ adhikān sukhārthān tyaktvā ityarthaḥ, śarīrasthityarthatvena prāpteṣu rāgadveṣau vyudasya ca parityajya ca. tataḥ –",
           ]),
        _v([
            "viviktasevī laghvāśī yatavākkāyamānasaḥ |",
            "dhyānayogaparo nityaṃ vairāgyaṃ samupāśritaḥ",
        ], "|| 52 ||",
           "resorting to solitude, eating lightly, with speech, body and mind controlled, ever intent on the yoga of meditation, taking refuge in dispassion;",
           bhashya=[
               "vivikta iti. viviktasevī araṇyanadīpulinagiriguhādīn viviktān deśān sevituṃ śīlamasya iti viviktasevī, laghvāśī laghvaśanaśīlaḥ viviktasevālaghvaśanayoḥ nidrādidoṣanivartakatvena cittaprasādahetutvāt grahaṇaṃ yatavākkāyamānasaḥ vākca kāyaśca mānasaṃ ca yatāni saṃyatāni yasya jñānaniṣṭhasya sa jñānaniṣṭhaḥ yatiḥ yatavākkāyamānasaḥ syāt, evamuparata sarvakaraṇassan dhyānayogaparaḥ dhyānamātmasvarūpacintanaṃ yogaḥ ātmaviṣaye ekāgrīkaraṇaṃ tau dhyānayogau paratvena kartavyau yasya saḥ dhyānayogaparaḥ, nityaṃ nityagrahaṇaṃ mantrajapādya nyakartavyābhāvadarśanārthaṃ, vairāgyaṃ virāgasya bhāvo vairāgyaṃ dṛṣṭādṛṣṭeṣu viṣayeṣu vaitṛṣṇyaṃ samupāśritaḥ nityameva ityarthaḥ, kiñca.",
           ]),
        _v([
            "ahaṅkāraṃ balaṃ darpaṃ kāmaṃ krodhaṃ parigraham |",
            "vimucya nirmamaḥ śānto brahmabhūyāya kalpate",
        ], "|| 53 ||",
           "casting off egoism, force, arrogance, desire, anger and possession, free from the sense of 'mine' and at peace — he is fit to become Brahman.",
           bhashya=[
               "ahaṅkāramiti. ahaṅkāramahaṅkaraṇaṃ ahaṅkāraḥ dehādiṣu taṃ balaṃ sāmarthyaṃ kāmarāga – saṃyuktaṃ – na itarat śarīrādi sāmarthyaṃ, svābhāvikatvena tattvāgasyāśakyatvāt – darpaṃ, darpo nāma harṣānantarabhāvī dharmātikramahetuḥ, hṛṣṭo dṛpyati dṛpto dharmamatikrāmati (āpa.dha.1.13.4) iti smaraṇāt, taṃ ca kāmaṃ icchāṃ krodhaṃ dveṣaṃ, parigrahaṃ indriyamanogata doṣaparityāge'pi śarīradhāraṇa prasaṅgena dharmānuṣṭhānanimittena vā bāhyaḥ parigrahaḥ prāptaḥ taṃ ca vimucya parityajya paramahaṃsa parivrājakobhūtvā, dehajīvanamātre'pi nirgatamamabhāvaḥ nirmamaḥ ata eva śāntaḥ uparataḥ yassaṃhṛta harṣāyāsaḥ yatiḥ jñānaniṣṭhaḥ brahmabhūyāya brahmabhavanāya kalpate samartho bhavati. anena krameṇa –",
           ]),
        _v([
            "brahmabhūtaḥ prasannātmā na śocati na kāṅkṣati |",
            "samassarveṣu bhūteṣu madbhaktiṃ labhate parām",
        ], "|| 54 ||",
           "Having become Brahman, serene in the Self, he neither grieves nor desires; the same towards all beings, he attains supreme devotion to me.",
           bhashya=[
               "brahmabhūta iti. brahmabhūtaḥ brahmaprāptaḥ, prasannātmā labdhādhyātma prasādabhāvaḥ na śocati kiñcidartha – vaikalyamātmanaḥ vaiguṇyaṃ voddiśya na śocati na santapyate. na kāṅkṣati na hyaprāptaviṣayākāṅkṣā brahmavidaḥ upapadyate ataḥ brahmabhūtasyāyaṃ svabhāvaḥ anūdyate. “na śocati nakāṅkṣatīti”. “na hṛṣyatī” ti vā pāṭhāntaraṃ samassarveṣu bhūteṣu, ātmaupamyeva sarvabhūteṣu sukhaṃ duḥkhaṃ vā samameva paśyati ityarthaḥ, na ātma samadarśanaṃ iha, tasya vakṣyamāṇatvāt “bhaktyā māmabhijānāti” (18.55) iti. evambhūtaḥ jñānaniṣṭhaḥ madbhaktiṃ mayi parameśvare bhaktiṃ bhajanaṃ parameśvare bhaktiṃ bhajanaṃ parāmuttamāṃ jñānalakṣaṇāṃ caturthīṃ labhate “caturvidhā bhajante māṃ” ityuktam.",
           ]),
        _v([
            "bhaktyā māmabhijānāti yāvānyaścāsmi tattvataḥ |",
            "tato māṃ tattvato jñātvā viśate tadanantaram",
        ], "|| 55 ||",
           "Through devotion he knows me in truth — what and who I am; then, knowing me in truth, he enters into me at once.",
           bhashya=[
               {"text": "tataḥ jñānalakṣaṇayā –", "intro": True},
               "bhaktyā iti. bhaktyā māmabhijānāti, yāvān ahaṃ upādhikṛtavistarabhedaḥ, yaśca ahaṃ asmi vidhvastasarvopādhibhedaḥ, uttamaḥ puruṣaḥ ākāśakalpaḥ taṃ māmadvaitaṃ caitanyamātraikarasaṃ ajaraṃ amaraṃ abhayamanidhanaṃ tattvataḥ abhijānāti. tataḥ māṃ evaṃ tattvataḥ jñātvā viśate tadanantaraṃ māmeva jñānānantaraṃ, nātra jñānāntarapraveśakriye bhinne vivakṣite “jñātvā viśate tadanantaraṃ” iti, kiṃ tarhi? phalāntarābhāvāt jñānamātrameva. “kṣetrajñaṃ cāpi māṃ viddhi” (13.2) iti uktatvāt.",
               "nanu viruddhamidamuktaṃ, “jñānasya yā parā kāṣṭhā tayā māṃ abhijānāti” iti. kathaṃ viruddhamiti cet, ucyate – yadaiva yasmin viṣaye jñānamutpadyate jñātuḥ, tadaivaṃ taṃ viṣayamabhijānāti jñātā iti na jñānaniṣṭhāṃ jñānāvṛttilakṣaṇāṃ apekṣate iti, ataśca jñānena na abhijānāti, jñānāvṛttyā tu jñānaniṣṭhayā abhijānātīti. naiṣa doṣaḥ, jñānasya svātmotpattiparipākahetuyuktasya pratipakṣa vihīnasya yat, ātmānubhavaniśca yāvasānatvaṃ tasya niṣṭhāśabdābhilāpāt. śāstrācāryopadeśena jñānotpatti paripākahetuṃ sahakāri kāraṇaṃ buddhi viśuddhatvādyamānitvādi guṇaṃ (13.7) cāpekṣya janitasya kṣetrajñaparamātmaikatva jñānasya kartṛtvādikārakabhedabuddhinibandhanasarvakarmasannyāsasahitasya svātmānubhavaniścayarūpeṇa yadavasthānaṃ sā parā jñānaniṣṭhā ityucyate. seyaṃ jñānaniṣṭhā ārtādibhaktitrayāpekṣayā parā caturthī bhaktirityuktā. (7.17) tayā parayā bhaktyā bhagavantaṃ tattvataḥ abhijānāti, yadanantarameva īśvarakṣetrajñabhedabuddhiḥ aśeṣataḥ nivartate. ataḥ jñānaniṣṭhālakṣaṇayā bhaktyā māmabhijānātīti vacanaṃ na virudhyate, tatra ca sarvaṃ nivṛttividhāyi śāstraṃ vedāntetihāsapurāṇasmṛtilakṣaṇaṃ nyāyaprasiddhaṃ arthavat bhavati – “viditvā ... vyutthāyātha bhikṣācaryaṃ caranti (bṛ.u.3.5.1), tasmānnyāsameṣāṃ tapasāmatiriktamā huḥ” (mahā.nā.u.24.1), “nyāsa evātyarecayat” (mahā.nā.u.21.2) iti. “sannyāsaḥ karmaṇāṃ nyāsaḥ” (18.2) “vedānimaṃ lokamamuṃ ca parityajya”, (āpa. da.2.23.13) “tyaja dharmamadharmaṃ ca” (śāṃ.pa.329.40nu 331.44) ityādi. iha ca (5.13) pradarśitāni vākyāni, na ca teṣāṃ vākyānāṃ ānarthakyaṃ yuktaṃ, na ca arthavādatvaṃ, svaprakaraṇasthatvāt, pratyagātma – vikriyasvarūpaniṣṭhatvācca mokṣasya, na hi pūrvasamudraṃ jigamiṣoḥ prātilomyena pratyaksamudrajigamiṣuṇā samānamārgatvaṃ sambhavati. pratyagātmaviṣaya pratyayasantānakaraṇābhiniveśaśca jñānaniṣṭhā sā ca pratyaksamudra gamanavat karmaṇā sahabhāvitvena virudhyate. parvatasarṣapamoriva antaravān virodhaḥ pramāṇavidāṃ niścitaḥ. tasmāt sarvakarmasannyāsenaiva jñāninaṣṭhā kāryā iti siddham.",
           ]),
        _v([
            "sarvakarmāṇyapi sadā kurvāṇo madvyapāśrayaḥ |",
            "matprasādādavāpnoti śāśvataṃ padamavyayam",
        ], "|| 56 ||",
           "Though always performing all actions, taking refuge in me, by my grace he attains the eternal, imperishable abode.",
           bhashya=[
               {"text": "svakarmaṇā bhagavataḥ abhyarcanabhaktiyogasya siddhiprāptiḥ phalaṃ jñānaniṣṭhāyogyatā, yannimittā jñānaniṣṭhā mokṣaphalāvasānā. saḥ bhagavadbhaktiyogaḥ adhunā stūyate śāstrārthopasaṃhāraprakaraṇe śāstrārtha niścayadārḍhyāya –", "intro": True},
               "sarvakarmāṇi iti. sarvakarmāṇyapi pratiṣiddhānyapi sadā kurvāṇaḥ anutiṣṭhan, madvyapāśrayaḥ ahaṃ vāsudevaḥ īśvaraḥ vyapāśrayo vyapāśrayaṇaṃ yasya saḥ madvyapāśrayaḥ, mayyarpita sarvātma bhāvaḥ ityarthaḥ so'pi matprasādāt mama parameśvarasya prasādāt avāpnoti śāśvataṃ nityaṃ vaiṣṇavapadamavyayam yasmādevaṃ tasmāt–",
           ]),
        _v([
            "cetasā sarvakarmāṇi mayi sannyasya matparaḥ |",
            "buddhiyogamupāśritya maccittaḥ satataṃ bhava",
        ], "|| 57 ||",
           "Mentally renouncing all actions in me, holding me supreme, resorting to the yoga of understanding, fix your mind on me always.",
           bhashya=[
               "cetasā iti. cetasā vivekabuddhyā, sarvakarmāṇi dṛṣṭādṛṣṭārthāni mayi īśvare sannyasya “yatkaroṣi yadaśnāsi” ityuktanyāyena matparaḥ ahaṃ vāsudevaḥ paro yasya tava saḥ tvaṃ matparaḥ san mayyarpita sarvātmabhāvaḥ buddhiyogaṃ samāhitabuddhitvaṃ buddhiyogaḥ taṃ buddhiyogaṃ apāśritya apāśrayaḥ ananya – śaraṇatvaṃ maccittaḥ mayyeva cittaṃ yasya tava saḥ tvaṃ maccittaḥ satataṃ sarvadā bhava.",
           ]),
        _v([
            "maccittaḥ sarvadurgāṇi matprasādāttariṣyasi |",
            "atha cettvamahaṅkārānna śroṣyasi vinaṅkṣyasi",
        ], "|| 58 ||",
           "With your mind on me, you will cross over all difficulties by my grace; but if out of egoism you will not listen, you will perish.",
           bhashya=[
               "maccittaḥ iti. maccittaḥ sarvadurgāṇi sarvāṇi dustarāṇi saṃsāra hetujātāni matprasādāt tariṣyasi atikramiṣyasi. atha cet yadi tvaṃ maduktaṃ ahaṅkārāt “paṇḍitaḥ ahaṃ” iti na śroṣyasi na grahīṣyasi, tataḥ tvaṃ vinaṅkṣyasi vināśaṃ gamiṣyasi.",
           ]),
        _v([
            "yadahaṅkāramāśritya na yotsya iti manyase |",
            "mithyaiṣa vyavasāyaste prakṛtistvāṃ niyokṣyati",
        ], "|| 59 ||",
           "If, relying on egoism, you think, 'I will not fight', your resolve is in vain; your nature will compel you.",
           bhashya=[
               {"text": "idaṃ ca tvayā na mantavyaṃ svatantraḥ ahaṃ, kimarthaṃ paroktaṃ kariṣyāmi?", "intro": True},
               "yadyahaṅkāraṃ iti. yadi cet tvaṃ ahaṅkāraṃ āśritya na yotsye iti na yuddhaṃ kariṣyāmi iti manyase cintayasi niścayaṃ karoṣi, mithyā eṣaḥ vyavasāyaḥ niścayaḥ te tava, yasmāt prakṛtiḥ kṣatriyasvabhāvaḥ tvāṃ niyokṣyati. yasmācca–",
           ]),
        _v([
            "svabhāvajena kaunteya nibaddhaḥ svena karmaṇā |",
            "kartuṃ necchasi yanmohāt kariṣyasyavaśo'pi tat",
        ], "|| 60 ||",
           "Bound by your own action born of your nature, son of Kuntī, what out of delusion you do not wish to do, you will do even against your will.",
           bhashya=[
               "svabhāvajena iti. svabhāvajena śauryādinā yathoktena kaunteya! nibaddhaḥ niścayena baddhaḥ svena ātmīyena karmaṇā kartuṃ na icchasi yat karma mohāt avivekataḥ kariṣyasi avaśaḥ api paravaśaḥ eva tat karma. yasmāt –",
           ]),
        _v([
            "īśvaraḥ sarvabhūtānāṃ hṛddeśe'rjuna tiṣṭhati |",
            "bhrāmayan sarvabhūtāni yantrārūḍhāni māyayā",
        ], "|| 61 ||",
           "The Lord dwells in the hearts of all beings, Arjuna, causing all beings, as if mounted on a machine, to revolve by his māyā.",
           bhashya=[
               "īśvaraḥ iti. īśvaraḥ īśanaśīlaḥ nārāyaṇaḥ sarvabhūtānāṃ sarvaprāṇināṃ hṛddeśe hṛdayadeśe arjuna śuklāntarātmasvabhāva! viśuddhāntaḥkaraṇa – “ahaśca kṛṣṇamahararjunaṃ ca” (ṛ.saṃ.6.9.1) iti darśanāt – tiṣṭhati sthitiṃ labhate. teṣu saḥ kathaṃ tiṣṭhatīti? āha – bhrāmayan bhramaṇaṃ kārayan sarvabhūtāni yantrārūḍhāni yantrāṇi ārūḍhāni adhiṣṭhitāni iva – iti ivaśabdaḥ atra draṣṭavyaḥ – yathā dārukṛtapuruṣādīni yantrārūḍhāni. māyayā chadmanā bhrāmayan tiṣṭhati iti sambandhaḥ.",
           ]),
        _v([
            "tameva śaraṇaṃ gaccha sarvabhāvena bhārata |",
            "tatprasādātparāṃ śāntiṃ sthānaṃ prāpsyasi śāśvatam",
        ], "|| 62 ||",
           "Take refuge in him alone with your whole being, O Bhārata. By his grace you will attain supreme peace and the eternal abode.",
           bhashya=[
               "tameva iti. tam eva īśvaraṃ śaraṇaṃ āśrayaṃ saṃsārārtiharaṇārthaṃ gaccha āśraya sarvabhāvena sarvātmanā he bhārata! tataḥ tatprasādāt īśvarānugrahāt parāṃ prakṛṣṭāṃ śānti uparatiṃ sthānaṃ ca mama viṣṇoḥ paramaṃ padaṃ prāpsyasi śāśvataṃ nityam.",
           ]),
        _v([
            "iti te jñānamākhyātaṃ guhyādguhyataraṃ mayā |",
            "vimṛśyaitadaśeṣeṇa yathecchasi tathā kuru",
        ], "|| 63 ||",
           "Thus I have declared to you knowledge more secret than all secrets. Reflect on it fully, and then do as you wish.",
           bhashya=[
               "iti iti. iti etat te tubhyaṃ jñānaṃ ākhyātaṃ kathitaṃ guhyāt gopyāt guhyataraṃ atiśeyana guhyaṃ rahasyaṃ ityarthaḥ, mayā sarvajñena īśvareṇa. vimṛśya vimarśanaṃ ālocanaṃ kṛtvā etat yathoktaṃ śāstraṃ aśeṣeṇa samastaṃ yathoktaṃ ca arthajātaṃ yathā icchasi tathā kuru.",
           ]),
        _v([
            "sarvaguhyatamaṃ bhūyaḥ śṛṇu me paramaṃ vacaḥ |",
            "iṣṭo'si me dṛḍhamiti tato vakṣyāmi te hitam",
        ], "|| 64 ||",
           "Hear again my supreme word, the most secret of all. You are dearly loved by me; therefore I will tell you what is for your good.",
           bhashya=[
               {"text": "bhūyo'pi mayā ucyamānaṃ śṛṇu –", "intro": True},
               "sarvaguhyatamaṃ iti. sarvaguhyatamaṃ sarvebhyaḥ guhyebhyaḥ atyanta guhyatamaṃ atyantarahasyaṃ uktam api asakṛt bhūyaḥ punaḥ śṛṇu me mama paramaṃ prakṛṣṭaṃ vacaḥ vākyam. na bhūyāt nāpi arthakāraṇāt vā vakṣyāmi, kiṃ tarhi? iṣṭaḥ priyaḥ asi me mama dṛḍhaṃ avyabhicāreṇa iti kṛtvā tataḥ tena kāraṇena vakṣyāmi kathayiṣyāmi te tava hitaṃ paramaṃ jñānaprāptisādhanam, tat hi sarvahitānāṃ hitatamam.",
           ]),
        _v([
            "manmanā bhava madbhakto madyājī māṃ namaskuru |",
            "māmevaiṣyasi satyaṃ te pratijāne priyo'si me",
        ], "|| 65 ||",
           "Fix your mind on me, be devoted to me, sacrifice to me, bow down to me. You will come to me; I promise you truly, for you are dear to me.",
           bhashya=[
               {"text": "kiṃ tat iti? āha –", "intro": True},
               "manmanāḥ iti. manmanāḥ bhava maccitaḥ bhava. madbhaktaḥ bhava madbhajanaḥ bhava. madyājī madyajana śīlaḥ bhava. māṃ namaskuru. namaskāraṃ api mamaiva kuru. tatra evaṃ vartamānaḥ vāsudeve eva samarpita sādhya sādhanaprayojanaḥ māṃ eva eṣyasi āgamiṣyasi. satyaṃ te tava pratijāne, satyāṃ pratijñāṃ karomi etasmin vastuni ityarthaḥ, yataḥ priyaḥ asi me. evaṃ bhagavataḥ satyapratijñatvaṃ buddhvā bhagavadbhakteḥ avaśya sambhāvi mokṣaphalaṃ avadhārya bhagavaccharaṇaikaparāyaṇaḥ bhavet iti vākyārthaḥ.",
           ]),
        _v([
            "sarvadharmān parityajya māmekaṃ śaraṇaṃ vraja |",
            "ahaṃ tvā sarvapāpebhyo mokṣayiṣyāmi mā śucaḥ",
        ], "|| 66 ||",
           "Abandoning all dharmas, take refuge in me alone. I will release you from all sins; do not grieve.",
           bhashya=[
               {"text": "karmayoganiṣṭhāyāḥ paramarahasyaṃ īśvaraśaraṇatāṃ upasaṃhṛtya atha idānīṃ karmayoganiṣṭhāphalaṃ samyagdarśanaṃ sarvavedāntasāravihitaṃ vaktavyam ityāha–", "intro": True},
               "sarvadharmān iti. sarvadharmān sarve ca te dharmāśca sarvadharmāḥ tān – dharmaśabdena atra adharmaḥ api gṛhyate, naiṣkarmyasya vivakṣitatvāt, “nāvirato duścaritāt”, (kaṭha.u. 2.24), “tyaja dharmamadharmaṃ ca” (śāṃ.pa.329.331.44) ityādi śrutismṛtibhyaḥ – sarvadharmān parityajya sannyasya sarvakarmāṇi ityetat. māṃ ekaṃ sarvātmānaṃ samaṃ sarvabhūtasthitaṃ īśvaraṃ (acyutaṃ garbhajanma jarāmaraṇavivarjitaṃ) “ahameva” ityevaṃ ekaṃ śaraṇaṃ vraja, na mattaḥ anyat asti iti avadhāraya ityarthaḥ. ahaṃ tvā tvāṃ evanniścitabuddhiṃ sarvapāpebhyaḥ sarvadharmādharmabandhanarūpebhyaḥ mokṣayiṣyāmi svātmabhāva – prakāśīkaraṇena. uktaṃ ca “nāśayāmyātma bhāvastho jñānadīpena bhāsvatā” (10.11) ityataḥ mā śucaḥ śokaṃ mā kārṣīḥ ityarthaḥ.",
               "kiṃ asmin gītāśāstre paraṃ niḥśreyasasādhanaṃ niścitam? – kiṃ jñānaṃ karma vā āhosvit ubhayam iti? kutaḥ saṃśaya? “yat jñātvā'mṛtamaśnute” (13.12) tato māṃ tattvato jñātvā viśate tadanantaraṃ (18.55) yityādīni vākyāni kevalajñānāt niśśreyasaprāptiṃ darśayanti. “karmaṇyevādhikāraste” (2.47) “kuru karmaiva” (4.15) ityevamādīni karmaṇāṃ avaśyakartavyatāṃ darśayanti. evaṃ jñānakarmaṇoḥ kartavyatvopadeśāt samuccitayo api niḥśreyasahetutvaṃ syāt iti bhavet saṃśayaḥ.",
               "kiṃ punaḥ atra mīmāṃsāphalam? nanu etat eva – eṣāṃ anyatamasya paramaniḥśreyasa sādhanatvāvadhāraṇaṃ, ataḥ vistīrṇataraṃ mīmāṃsya etat. ātmajñānasya tu kevalasya niḥśreyasa hetutvaṃ, bhedapratyayanivartakatvena kaivalyaphalāva sāyitvāt. kriyākārakaphalabhedabuddhiḥ avidyayā ātmani nityapravṛttā – “mama karma, ahaṃ kartā, amuṣmai phalāya yidaṃ karma kariṣyāmi” iti iyaṃ avidyāṃ anādikālapravṛttā. asyāḥ avidyāyāḥ nivartakaṃ – “ayaṃ ahaṃ asmi kevalaḥ akartā akriyaḥ aphalaḥ, na mattaḥ anyaḥ asti kaścit” – ityevaṃrūpaṃ ātmaviṣayaṃ jñānaṃ utpadyamānaṃ karmapravṛttihetu bhūtāyāḥ bhedabuddheḥ nivartakatvāt. tuśabdaḥ pakṣadvayavyāvṛttyarthaḥ – na kevalebhyaḥ karmabhyaḥ, na ca jñānakarmabhyāṃ samuccitābhyāṃ niḥ śśreyasaprāptiḥ iti pakṣadvayaṃ nivartayati. akāryatvācca niḥśreyasasya karmasādhanatvānupapattiḥ. na hi nityaṃ vastu karmaṇā jñānena vā kriyate.",
               "kevalajñānam api anarthakaṃ tarhi? na, avidyā nivartakatve sati dṛṣṭakaivalya phalāvasānatvāt. avidyā tamo nivartakasya jñānasya dṛṣṭaṃ kaivalyaphalāvasānatvaṃ, rajjvādiviṣaye sarpādyajñānatamonivartakapradīpaprakāśavat. vinivṛttasarpādivikalparajjukaivalyāvasānaṃ hi prakāśaphalam, tathā jñānam. dṛṣṭārthānāṃ ca chidikriyāgnimanthanādīnāṃ vyāpṛtakartrādikārakāṇāṃ dvaidhībhāvāgnidarśanādiphalāt anyaphale karmāntare vā vyāpārānupapattiḥ yathā, tathā dṛṣṭārthāyāṃ jñānaniṣṭhākriyāyāṃ (niṣkriyāyāṃ jñānaniṣṭhā kriyāyāṃ) iti, “niṣkriyāyāṃ jñānaniṣṭhāyāṃ” iti ca pāṭhau vyāpṛtasya jñātrādikārakasya ātmakaivalyaphalāt karmāntare pravṛttiḥ anupapannā iti na jñānaniṣṭhā karmasahitā upapadyate. bhujyagnihotrādikriyāvat syāt iti cet – na, kaivalyaphale jñāne kriyāphalārthitvānupapatteḥ. kaivalyaphale hi jñāne prāpte, sarvataḥ samplutodakaphale kūpataḍāgādi kriyāphalārthittvābhāvatat, phalāntare tatsādhanabhūtāyāṃ vā kriyāyāṃ arthitvānupapattiḥ. na hi rājyaprāpti phale karmaṇi, vyāpṛtasya kṣetramātraprāptiphale vyāpāra upapadyate, tadviṣayaṃ vā arthitvam. tasmāt na karmaṇaḥ asti niḥśreyasasādhanatvām. na ca jñānakarmaṇoḥ samuccitayoḥ. nāpi jñānasya kaivalyaphalasya karmasāhāyyāpekṣā, avidyā nivartakatvena virodhāt. na hi tamaḥ tamasaḥ nivartakam. ataḥ kevalam eva jñānaṃ niḥśreyasa sādhanaṃ iti.",
               "na – nityākaraṇe pratyayavāyaprāpteḥ, kaivalyasya ca nityatvāt, yat tāvat kevalajñānāt kaivalyaprāptiḥ ityetat, tat asat, yataḥ nityānāṃ karmaṇāṃ śrutyāktānāṃ akaraṇe pratyavāyaḥ narakādiprāpti – lakṣaṇaḥ syāt – nanu evaṃ tarhi karmabhyaḥ mokṣaḥ nāsti iti anirmokṣaḥ eva. naiṣa doṣaḥ, nityatvāt mokṣasya. nityānāṃ karmaṇāṃ anuṣṭhānāt pratyavāyasya aprāptiḥ pratiṣiddhasya ca akaraṇāt aniṣṭaśarīrānupapattiḥ kāmyānāṃ ca varjanāt iṣṭaśarīrānupapattiḥ, vartamānaśarīrābhakasya ca karmaṇaḥ phalopabhogakṣaye patite asmin śarīre dehāntarotpattau ca kāraṇābhāvāt ātmanaḥ rāgādīnāṃ ca akaraṇe svarūpāvasthānaṃ kaivalyam iti ayatnasiddhaṃ kaivalyaṃ iti. atikrāntānekajanmāntarakṛtasya svarganarakādiprāptiphalasya anārabdhakāryasya upabhogānupapatteḥ kṣayābhāvaḥ iti cet – na, nityakarmānuṣṭhānāyāsaduḥkhopabhogasya tatphalopabhogatvopapatteḥ. prāyaścittavadvā'pūrvopa citaduritakṣayārthaṃ nityaṃ karma. ārabdhānāṃ ca karmaṇāṃ upabhogena eva kṣīṇatvāt apūrvāṇāṃ ca karmaṇāṃ anārambhe ayatnasiddhaṃ kaivalyam iti.",
               "na, “tameva viditvā'timṛtyumeti nānyaḥ panthā vidyate'yanāya” (śve.u.3.8) iti vidyāyā anyaḥ panthāḥ mokṣāya na vidyate iti śruteḥ, carmavadākāśaveṣṭanā sambhavavat aviduṣaḥ mokṣāsambhavaśruteḥ (śve.u.6.20), “jñānāt kaivalyamāpnoti” iti ca purāṇasmṛteḥ anārabdhaphalānāṃ puṇyānāṃ karmaṇāṃ kṣayānupapatteśca. yathā pūrvopāttānāṃ duritānāṃ anārabdhaphalānāṃ syāt sambhavaḥ, tathā puṇyānāṃ anārabdha phalānāṃ syāt sambhavaḥ. teṣāṃ ca dehāntaraṃ akṛtvā kṣayānupapattau mokṣānupapattiḥ, dharmādharmahetūnāṃ ca rāgadveṣamohānāṃ anyatra ātmajñānāt ucchedānupapatteḥ dharmādharmocchedānupapattiḥ. nityānāṃ ca karmaṇāṃ puṇyaphalatvaśruteḥ, “varṇāḥ āśramāśca svakarmaniṣṭhāḥ (gau.dha.sū.11.29) ityādismṛteśca karmakṣayānupapattiḥ.",
               "ye tu āhuḥ – nityāni karmāṇi duḥkharūpatvāt pūrvakṛtadurita karmaṇāṃ phalameva, na tu teṣāṃ svarūpa vyatirekeṇa anyat phalaṃ asti, aśrutattvāt, jīvanādinimitte ca vidhānāt iti. nanu apravṛttānāṃ karmaṇāṃ phaladānāsambhavāt, duḥkhaphalaviśeṣānupapattiśca syāt. yat uktam – pūrvajanma kṛtaduritānāṃ karmaṇāṃ phalaṃ nityakarmānuṣṭhānāyāsaduḥkhaṃ bhujyate iti – tat asat. na hi maraṇakāle phaladānāya anaṅkurībhūtasya karmaṇaḥ phalaṃ anyakarmārabdhe janmani upabhujyate iti upapattiḥ. anyathā svargaphalopabhogāya agnihotrādikarmārabdhe janmani narakaphalopabhogānupapattiḥ na syāt. tasya durita duḥkhaviśeṣaphalatvānupapatteśca – anekeṣu hi duriteṣu sambhavatsu bhinnaduḥkhasādhanaphaleṣu nityakarmānuṣṭhānāyāsa – duḥkhamātraphaleṣu kalpyamāneṣu dvandvarogādibādhanaṃ, nirnimittaṃ na hi śakyate kalpayituṃ, nityakarmānuṣṭhānāyāsaduḥkham eva pūrvopātta – duritaphalaṃ na śirasāpāṣāṇavahanādi duḥkham iti. aprakṛtaṃ ca idaṃ ucyate – nityakarmānuṣṭhānāyāsa duḥkhaṃ pūrvakṛtaduritakarmaphalaṃ iti. katham – aprasūtaphalasya hi pūrvakṛtaduritasya kṣayaḥ na upapadyate iti prakṛtam. tatra prasūtaphalasya karmaṇaḥ phalaṃ nityakarmānuṣṭhānāyāsa duḥkhaṃ āha bhavān, na aprasūtaphalasya iti. atha sarvameva pūrvakṛtaṃ duritaṃ prasūtaphalam eva iti manyate bhavān – tataḥ nityakarmānuṣṭhānāyāsa duḥkham eva phalaṃ iti viśeṣeṇaṃ ayuktam. nityakarmavidhyānarthakyaprasaṅgaśca, upabhogenaiva prasūtaphalasya duritakarmaṇaḥ kṣamopapatteḥ. kiñca – śrutasya nityasya duḥkhaṃ cet phalaṃ, nityakarmānuṣṭhānāyāsāt eva tat dṛśyate vyāyāmādivat, tat anyasya iti kalpanānupapattiḥ. jīvanādinimitte ca vidhānāt, nityānāṃ karmaṇāṃ prāyaścittavat pūrvakṛtadurita – phalatvānupapattiḥ. yasmin pāpakarmaṇi nimitte yat vihitaṃ prāyaścittaṃ na tu tasya pāpasya tat phalam. atha tasya eva pāpasya nimittasya prāyaścittaduḥkhaṃ phalaṃ, jīvanādinimitte'pi nityakarmānuṣṭhānāyāsa duḥkhaṃ jīvanādinimittasya eva phalaṃ prasajyeta, nityaprāyaścittayoḥ naimittikatvāviśeṣāt. kiñca anyat – nityasya kāmyasya ca agnihotrādeḥ anuṣṭhānāyāsaduḥkhasya tulyatvāt nityānuṣṭhānāyāsa'duḥkham eva pūrvakṛta – duritasya phalam, na tu kāmyānuṣṭhānāyāsa duḥkhaṃ iti viśeṣaḥ na astīti tadapi pūrvakṛtaduritaphalaṃ prasajyeta. tathā ca sati nityānāṃ phalāśravaṇāt tadvidhānānyathā – nupapatteśca nityānuṣṭhānāyāsaduḥkhaṃ pūrvakṛtaduritaphalaṃ iti arthāpattikalpanā ca anupapannā. evaṃ vidhānānyathānupapatteḥ anuṣṭhānāyāsaduḥkha – vyatiriktaphalatvānumānācca nityānām. virodhācca, viruddhaṃ ca idaṃ ucyate – nityakarmaṇā anuṣṭhīyamānena anyasya karmaṇaḥ phalaṃ bhujyate iti abhyupagamyamāne sa eva upabhogaḥ nityasya karmaṇaḥ phalaṃ iti, nityasya karmaṇaḥ phalābhāvaḥ iti viruddhaṃ ucyate. kiñca – kāmyāgnihotrādau anuṣṭhīyamāne nityam api agnihotrādi tantreṇa eva anuṣṭhitaṃ bhavatīti tadāyāsaduḥkhena eva kāmyāgnihotrādiphalaṃ upakṣīṇaṃ syāt, tattantratvāt. atha kāmyāgnihotrādi phalaṃ anyat eva svargāditadanuṣṭhānāyā saduḥkham api bhinnaṃ prasajyeta. na ca tat asti, dṛṣṭavirodhāt. na hi kāmyānuṣṭhānāyāsa'duḥkhāt kevalanityānuṣṭhānāyāsaduḥkhaṃ bhinnaṃ dṛśyate. kiñca anyat – avihitaṃ, apratiṣiddhaṃ ca karma tatkālaphalaṃ, na tu śāstracoditaṃ pratiṣiddhaṃ vā tatkālaphalaṃ bhavet. tadā svargādiṣu api adṛṣṭaphalaśāsanena udyamaḥ na syāt – agnihotrādīnām eva karmasvarūpāviśeṣe anuṣṭhānāyāsa duḥkhamātreṇa upakṣayaḥ nityānāṃ, svargādimahāphalatvaṃ kāmyānāṃ – aṅgetikartavyatādyādhikye tu asati – phalakāmitvamātreṇa iti. tasmācca na nityānāṃ karmaṇāṃ adṛṣṭaphalabhāvaḥ kadācit api upapadyate.",
               "ataśca avidyāpūrvakasya karmaṇaḥ vidyā eva śubhasya aśubhasya vā kṣaya kāraṇaṃ āśeṣataḥ, na nityakarmānuṣṭhānam, avidyākāmabījaṃ hi sarvameva karma. tathā upapāditaṃ avidvadviṣayaṃ karma, vidvadviṣayā sarvakarmasannyāsapūrvikā jñāniṣṭhā “ubhau tau na vijānītaḥ” (2.19) “vedāvināśinaṃ nityaṃ” (2.21) “jñānayogena sāṅkhyānāṃ karmayogena yogināṃ” (3.3) “ajñānāṃ karmasaṅgināṃ” (3.26), “tattvavit mahābāho ... guṇā guṇeṣu vartante iti matvā na sajjate” (3.28), “sarvakarmāṇi manasā sannyasyāste” (5.13), “naiva kiñcit karomīti yukto manyeta tattvavit” (5.7), arthāt ajñaḥ “karomi” iti, ārurukṣoḥ karma kāraṇaṃ, ārūḍhasya yogasthasya śama eva kāraṇaṃ” (6.3)nu “udārāḥ” trayo'pi ajñāḥ “jñānī tvātmaiva me mataṃ” (7.18), “ajñāḥ karmiṇaḥ gatāgataṃ kāmakāmāḥ labhante” (9.21)nu “ananyāścintayanto māṃ nityayuktāḥ yathoktaṃ ātmānaṃ ākāśakalpaṃ akalmaṣam upāsate” (9.22) nu “dadāmi buddhiyogaṃ taṃ ena māmupayānti te” (10.10) – arthāt na karmiṇaḥ ajñāḥ upayānti. bhagavatkarmaṇa kāriṇaḥ ye yuktatamāḥ api karmiṇaḥ ajñāḥ te uttarottarahīnaphalatyāgāvasānasādhanāḥ. (12.6.11). anirdeśyākṣaropāsakāstu “adveṣṭā sarvabhūtānām” (12.13'20) iti ā adhyāyaparisamāpti uktasādhanāḥ kṣetrādhyāyādyadhyāyoktajñāna sādhanāśca (13.7'11nu 14.22'26nu 15.3'5) – adhiṣṭhānādi pañcakahetuka sarvakarmasannyāsināṃ (18.14) ātmaikatvā kartṛtvajñānavatāṃ parasyāṃ jñānaniṣṭhāyāṃ vartamānānāṃ bhagavattattvavidāṃ aniṣṭādikarmaphalatrayaṃ (18.12) paramahaṃsa parivrājakānām eva labdhabhagavatsvarūpātmaikatva śaraṇānāṃ na bhavati, bhavati eva anyeṣāṃ ajñānāṃ karmiṇāṃ asannyāsināṃ ityeṣaḥ gītāśāstroktakartavyārthasya vibhāgaḥ.",
               "avidyāpūrvakṛtaṃ sarvasya karmaṇaḥ asiddham iti cet – nanu brahmahatyādivat. yadyapi śāstrāvagataṃ nityaṃ karmanu tathā'pi avidyāvataḥ eva bhavati. yathā pratiṣedhaśāstrāvagatam api brahmahatyādilakṣaṇaṃ karma anarthakāraṇaṃ avidyākāmādi doṣavataḥ bhavati – anyathā pravṛtyanupapatteḥ – tathā nityanaimittikakāmyāni api iti. dehavyatiriktātmani ajñāne pravṛttiḥ nityādikarmasu anupapannā iti cet – na calanātmakasya karmaṇaḥ anātmakartṛkasya “ahaṃ karomi” iti pravṛttidarśanāt. dehādisaṅghāte ahampratyayaḥ gauṇaḥ, na mithyā iti cet – na, tatkārveṣvapi gauṇatvopapatteḥ. ātmīye dehādisaṅghāte ahampratyayaḥ gauṇaḥ, yathā ātmīye putre “ātmā vai putranāmā'si” (tai.saṃ.2.11) iti, loke ca mama prāṇa eva ayaṃ gauḥ iti, tadvat. naivaṃ mithyāpratyayaḥ. mithyāpratyayastu sthāṇupuruṣayoḥ agṛhyamāṇa viśeṣayoḥ. na gauṇapratyayasya mukhyakāryārthatā, adhikaraṇastutyarthatvāt luptopamāśabdena. “yathā siṃho devadattaḥ” “agniḥ māṇavakaḥ” iti siṃha iva, agniriva krauryapaiṅgalyādi sāmānyavattvāt devadattamāṇavakādhikaraṇastutyartham eva, na tu siṃhakāryāṃ agnikāryaṃ vā gauṇaśabdapratyaya nimittaṃ kiñcit sādhyate, mithyāpratyayakāryaṃ tu anarthaṃ anubhavati iti. gauṇapratyayaviṣayaṃ jānāti “naiṣa siṃhaḥ devadattaḥ”, “nāyaṃ agniḥ māṇavakaḥ” iti. tathā gauṇena dehādisaṅghātena ātmanā kṛtaṃ karma na mukhyena ahampratyayaviṣayeṇa ātmanā kṛtaṃ syāt. na hi gauṇasiṃhāgnibhyāṃ kṛtaṃ karma mukhyasiṃhāgnibhyāṃ kṛtaṃ syāt. na ca krauryeṇa paiṅgalyena vā mukhyasiṃhāgnyoḥ kāryaṃ kiñcit kriyate, stutyarthatvena upakṣīṇatvāt. stūyāmānau ca jānītaḥ “na ahaṃ siṃhaḥ na ahaṃ agniḥ” itinu na hi “siṃhasya karma mama, agneśca” iti. tathā “na saṅghātasya karma mama mukhyasya ātmanaḥ iti pratyayaḥ yuktataraḥ syāt, na punaḥ “ahaṃ kartā mama karma” iti. yacca āhuḥ “ātmīyaiḥ smṛtīcchāprayatnaiḥ karmahetubhiḥ ātmā karma karoti” iti. na, teṣāṃ mithyāpratyayapūrvakatvāt. mithyāpratyayanimitteṣṭāniṣṭānubhūtakriyāphalajanita saṃskārapūrvakāḥ hi smṛtīcchāprayatnādayaḥ. yathā asmin janmani dehādisaṅghātābhimānarāga dveṣādikṛtau dharmādharmau tatphalānubhavaśca tathā atīte atītetarepi janmani iti anādiḥ avidyākṛtaḥ saṃsāraḥ atītaḥ anāgataśca anumeyaḥ. tataśca sarvakarmasannyāsasahita – jñānaniṣṭhayā ātyantikaḥ saṃsāroparamaḥ iti siddham. avidyātmakatvācca dehābhimānasya tannivṛttau dehānupapatteḥ saṃsārānupapattiḥ. dehādisaṅghāte ātmābhimānaḥ avidyātmakaḥ. na hi loke “gavādibhyaḥ anyaḥ ahaṃ, mattaśca anye gavādayaḥ” iti jānan tān “ahaṃ” iti manyate kaścit. ajānaṃstu sthāṇau puruṣa vijñānavat avivekataḥ dehādisaṅghāte kuryāt “ahaṃ” iti pratyayaṃ, na vivekataḥ jānan. yastu “ātmā vai putranāmā'si” (tai.saṃ.2.11) iti putre “ahaṃ” pratyayuḥ, sa tu janyajanakasambandhanimittaḥ gauṇaḥ. gauṇena ca ātmanā bhojanādivat paramārthakāryaṃ na śakyate kartuṃ, gauṇasiṃhāgnibhyāṃ mukhyasiṃhāgnikāryavat.",
               "adṛṣṭaviṣayacodanāprāmāṇyāt ātmakartavyaṃ gauṇaiḥ dehendriyātmabhiḥ kriyate eva iti cet. na nu avidyākṛta ātmakatvāt teṣām. na gauṇāḥ ātmanaḥ dehendriyādayaḥ kiṃ tarhi? mithyāpratyayena eva anātmanaḥ santaḥ ātmatvaṃ āpādyante, tadbhāve bhāvāt, tadabhāve ca abhāvāt. avivekināṃ hi ajñānakāle bālānaṃ dṛśyate “dīrghaḥ ahaṃ” “gauraḥ ahaṃ” iti dehādisaṅghāte ahampratyayaḥ. na tu vivekināṃ anyaḥ ahaṃ dehādisaṅghātāt iti. jānatāṃ tatkāle dehādisaṅghāte ahampratyayaḥ bhavati. tasmāt mithyāpratyayābhāve abhāvāt tatkṛtaḥ eva, na gauṇaḥ. pṛthaggṛhyamāṇa – viśeṣasāmānyayoḥ hi siṃhadevadattayoḥ agnimāṇavakayoḥ vā gauṇaḥ pratyayaḥ śabdaprayogaḥ vā syāt, na agṛhyamāṇa viśeṣasāmānyayoḥ. yattu uktaṃ “śrutiprāmāṇyāt” iti – tat na, tatprāmāṇasya adṛṣṭa – viṣayatvāt. pratyakṣādipramāṇānupalabdhe hi viṣaye agnihotrādi sādhyasādhanasambandhe śruteḥ prāmāṇyaṃ, na pratyakṣādiviṣaye adṛṣṭadarśanārthaviṣayatvāt pramāṇasya. tasmāt na dṛṣṭamithyā'jñānanimittasya ahampratyayasya dehādisaṅghāte gauṇatvaṃ kalpayituṃ śakyam. na hi śrutiśatamapi “śītaḥ agniḥ, aprakāśo vā” iti bruvat prāmāṇyaṃ upaiti. yadi brūyāt “śītaḥ agniḥ, aprakāśo vā” iti, tathā'pi arthāntaraṃ śruteḥ vivakṣitaṃ kalpyam, prāmāṇyānyathā'nu'papatteḥ, na tu pramāṇāntaraviruddhaṃ svavacanaviruddhaṃ vā kalpyam.",
               "karmaṇaḥ mithyāpratyayavatka rtṛkatvāt kartuḥ abhāve śruteḥ aprāmāṇyam iti cet – na nu brahmavidyāyāṃ arthavattvopapatteḥ. karmavidhiśrutivat brahmavidyāvidhiśruteḥ api aprāmāṇya prasaṅgaḥ iti cet – – nanu bādhaka pratyayānupapatteḥ. yathā brahmavidyāvidhiśrutyā ātmani avagate dehādi saṅghāte ahampratyayaḥ bādhyate tathā ātmani eva ātmāvagatiḥ na kadācit kenacit kathañcit api bādhituṃ śakyā, phalāvyatirekāt avagateḥ yathā agniḥ uṣṇaḥ prakāśaśca iti, na ca evaṃ karmavidhiśṛteḥ aprāmāṇyaṃ, pūrvapūrvapravṛttinirodhena uttarottarāpūrvapravṛtti jananasya pratyagātmabhimukhyena pravṛttyutpādanārthatvāt. mithyātve'pi upāyasya upeyasatyatayā satyatvam eva syāt, yathā arthavādānāṃ vidhiśeṣāṇām, loke'pi bālonmattādīnāṃ paya ādau pāyayitavye cūḍāvardhanādi vacanam. prakārāntarasthānaṃ ca sākṣāt eva prāmāṇyaṃ siddhaṃ, prāk ātmajñānāt dehābhimānanimittapratyakṣādiprāmāṇyavat.",
               "yattu manyase svayamavyāpriyamāṇo'pi ātmā sannidhimātreṇa karoti, tadeva mukhyaṃ kartṛtvamātmanaḥ yathā rājā yudhyamāneṣu yodheṣu yudhyata iti prasiddhaṃ svayamayudhya – māno'pi sannidhānādeva jitaḥ parājitaśceti, tathā senāpatiḥ vācaiva karoti, kriyāphalasambandhaśca rājñaḥ senāpateśca dṛṣṭaḥ. yathā ca ṛtvikkarma yajamānasya, tathā dehādīnāṃ karma ātmakṛtaṃ syāt, phalasya ātmagāmitvāt, yathā vā bhrāmakasya lohabhrāma– yitṛtvāt, avyāpṛtasyaiva mukhyameva kartṛtvaṃ, tathā cātmāna iti. tadasat akurvataḥ kārakatva prasaṅgāt. kārakamaneka prakāramiti cet – na, rājaprabhṛtīnāṃ mukhyasyāpi kartṛtvasya darśanāt. rājā tāvat svavyāpāreṇāpi yudhyate yodhānāṃ ca yodhayitṛtve dhanādāne ca mukhya kartṛtvaṃ tathā jayaparājaya phalopabhoge, yajamānasyāpi pradhānatyāge dakṣiṇādāne ca mukhyameva kartṛtvaṃ. tasmāt avyāpṛtasya kartṛtvopacāro yaḥ, saḥ gauṇaḥ iti avagamyate. yadi mukhyaṃ anyata kartṛtvaṃ svavyāpāralakṣaṇaṃ nopalabhyeta rājayajamānaprabhṛtīnāṃ, tadā sannidhi mātreṇāpi kartṛtvaṃ mukhyaṃ parikalpyeta, yathā bhrāmakasya lohabhramaṇena, na tathā rājayajamānādīnāṃ svavyāpāro nopalabhyate, tasmātsannidhimātreṇa kartṛtvaṃ gauṇameva tathā ca sati tatphalasambandhopi gauṇa eva syāt, na gauṇena mukhyaṃ kāryaṃ nirvartyate, tasmātsannidhimātreṇa kartṛtvaṃ gauṇameva. tathā ca sati tatphalasambandho'pi gauṇa eva syāt, na gauṇena mukhyaṃ kāryaṃ nirvartṛte, tasmādasadeva etat gīyate “dehādīnāṃ vyāpāreṇa avyāpṛta evātmā kartā bhoktā ca syāt” iti. bhrāntinimittaṃ tu sarvamupapadyate, yathā svapne, māyāyāṃ ca evaṃ, na ca dehādyātmapratyayabhrānti santānavicchedeṣu suṣuptisamādhyādiṣu kartṛtvabhoktṛtvādyanarthaḥ upalabhyate. tasmāt bhrāntipratyaya nimittaevāyaṃ saṃsārabhramaḥ, na tu paramārthataḥ iti samyagdarśanāt atyantoparama iti siddham.",
           ]),
        _v([
            "idaṃ te nātapaskāya nābhaktāya kadā cana |",
            "na cāśuśrūṣave vācyaṃ na ca māṃ yo'bhyasūyati",
        ], "|| 67 ||",
           "This is never to be told by you to one who is without austerity or devotion, nor to one who does not wish to hear, nor to one who speaks ill of me.",
           bhashya=[
               {"text": "sarvagītāśāstrārthaṃ upasaṃhṛtya asmin adhyāye, viśeṣataśca ante iha śāstrārtha dārḍhyāya saṅkṣepataḥ upasaṃhāraṃ kṛtvā, atha idānīṃ śāstra sampradāyavidhim āha.", "intro": True},
               "idaṃ iti. idaṃ śāstraṃ te tava hitāya mayā uktaṃ saṃsāravicchittaye atapaskāya taporahitāya na vācyaṃ iti vyavahitena sambadhyate. tapasvine'pi abhaktāya gurau deve ca bhaktirahitāya kadācana kasyāñcit api avasthāyāṃ na vācyam. bhaktaḥ tapasvī api san aśuśrūṣuḥ yaḥ bhavati tasmai api na vācyam. na ca yaḥ māṃ vāsudevaṃ prākṛtaṃ manuṣyaṃ matvā abhyasūyati ātmapraśaṃsādi doṣādhyāropaṇena īśvaratvaṃ mama ajānan na sahate. asau api ayogyaḥ, tasmai api na vācyam. bhagavati anasūyāyuktāya tapasvine bhaktāya śuśrūṣave vācyaṃ śāstraṃ iti sāmarthyam gamyate. tatra “medhāvine tapasvine vā” iti anayoḥ vikalpadarśanāt śuśrūṣābhaktiyuktāya tapasvine tadyuktāya medhāvine vā vācyam. śuśrūṣābhakti viyuktāya na tapasvine nāpi medhāvine vācyam. bhagavati asūyāyuktāya samastaguṇavate'pi na vācyam. guruśuśrūṣābhaktimate ca vācyaṃ ityeṣaḥ śāstrasampradāya vidhiḥ.",
           ]),
        _v([
            "ya imaṃ paramaṃ guhyaṃ madbhakteṣvabhidhāsyati |",
            "bhaktiṃ mayi parāṃ kṛtvā māmevaiṣyatyasaṃśayaḥ",
        ], "|| 68 ||",
           "He who, with supreme devotion to me, teaches this supreme secret to my devotees will without doubt come to me.",
           bhashya=[
               {"text": "sampradāyasya kartuḥ phalaṃ idānīṃ āha –", "intro": True},
               "ya imaṃ iti. yaḥ imaṃ yathoktaṃ paramaṃ paramaniḥśreyasārthaṃ keśavārjunayoḥ saṃvādarūpaṃ granthaṃ guhyaṃ gopyatamaṃ madbhakteṣu mayi bhaktimatsu abhidhāsyati vakṣyati, granthaḥ arthataḥ ca sthāpayiṣyati ityarthaḥ, yathā tvayi mayā. bhakteḥ punargrahaṇāt bhaktimātreṇa kevalena śāstrasampradāne pātraṃ bhavati iti gamyate. kathaṃ abhidhāsyati iti? ucyate bhaktiṃ mayi parāṃ kṛtvā “bhagavataḥ paramaguroḥ acyutasya śuśrūṣā mayā kriyate” ityevaṃ kṛtvā ityarthaḥ. tasya idaṃ phalam – māṃ eva eṣyati mucyate eva. asaṃśayaḥ atra saṃśayaḥ na kartavya. kiñca –",
           ]),
        _v([
            "na ca tasmānmanuṣyeṣu kaścinme priyakṛttamaḥ |",
            "bhavitā na ca me tasmādanyaḥ priyataro bhuvi",
        ], "|| 69 ||",
           "No one among men does me dearer service than he, and no one on earth shall be dearer to me than he.",
           bhashya=[
               "na ca iti. na ca tasmāt śāstrasampradāyakṛtaḥ manuṣyeṣu manuṣyāṇāṃ madhye kaścit me mama priyakṛttamaḥ atiśayena priyakaraḥ, anyaḥ priyakṛttamaḥ, nāstevyaṃ ityarthaḥ vartamāneṣu. na ca bhavitā bhaviṣyatyapi kāle tasmāt dvitīyaḥ anyaḥ priyataraḥ priyakṛttaraḥ bhuvi loke'smin na bhavitā. yo'pi.",
           ]),
        _v([
            "adhyeṣyate ca ya imaṃ dharmyaṃ saṃvādamāvayoḥ |",
            "jñānayajñena tenāhamiṣṭaḥ syāmiti me matiḥ",
        ], "|| 70 ||",
           "And he who studies this sacred dialogue of ours — by him I shall have been worshipped with the sacrifice of knowledge; such is my view.",
           bhashya=[
               "adhyeṣyate iti. adhyeṣyate ca paṭhiṣyati yaḥ imaṃ dharmyaṃ dharmādanapetaṃ saṃvādarūpaṃ granthaṃ āvayoḥ, tena idaṃ kṛtaṃ syāt. jñānayajñena vidhijapopāṃśumānasānāṃ yajñānāṃ jñānayajñaḥ mānasatvāt viśiṣṭatamaḥ ityataḥ tena jñānayajñena gītāśāstrasya adhyayanaṃ stūyate, phalavidhiḥ eva vā, devatādiviṣayajñānaphalatulyaṃ asya phalaṃ bhavatīti – tena adhyayanena ahaṃ iṣṭaḥ pūjitaḥ syāṃ bhaveyaṃ iti me mama matiḥ niścayaḥ.",
           ]),
        _v([
            "śraddhāvānanasūyaśca śṛṇuyādapi yo naraḥ |",
            "so'pi muktaḥ śubhān lokān prāpnuyātpuṇyakarmaṇām",
        ], "|| 71 ||",
           "And the man who, full of faith and free from cavilling, merely hears it — he too, released, shall attain the happy worlds of those who do good.",
           bhashya=[
               {"text": "atha śrotuḥ idaṃ phalam –", "intro": True},
               "śraddhāvān iti. śraddhāvān śraddhānaḥ anasūyaḥ ca asūyāvarjitaḥ san imaṃ granthaṃ śṛṇuyāt api yaḥ naraḥ apiśabdāt kimuta arthajñānavān? saḥ api pāpāt muktaḥ śubhān praśastān lokān prāpnuyāt puṇyakarmaṇāṃ agnihotrādi karmavatām.",
           ]),
        _v([
            "kaccidetat śrutaṃ pārtha tvayaikāgreṇa cetasā |",
            "kaccidajñānasammohaḥ pranaṣṭaste dhanañjaya",
        ], "|| 72 ||",
           "Have you heard this, Pārtha, with a one-pointed mind? Has your delusion born of ignorance been destroyed, Dhanañjaya?",
           bhashya=[
               {"text": "śiṣyasya śāstrārthagrahaṇāgrahaṇavivekabubhutsayā pṛcchati. tadgrahaṇe jñāte punaḥ grāhayiṣyāmi upāyāntareṇa api iti praṣṭuḥ abhiprāyaḥ yatnāntaraṃ ca āsthāya śiṣyasya kṛtārthatā kartavyā iti ācāryadharmaḥ pradarśitaḥ bhavati.", "intro": True},
               "kaccit iti. kaccit kiṃ etat mayā uktaṃ śrutaṃ śravaṇena avadhāritaṃ pārtha! tvayā ekāgreṇa cetasā cittena? kiṃ vā apramādataḥ? kaccit ajñānasammohaḥ ajñānanimittaḥ sammohaḥ aviviktabhāvaḥ (vicittabhāvaḥ) avivekaḥ svābhāvikaḥ kiṃ pranaṣṭaḥ? yadarthaḥ ayaṃ śāstraśravaṇāyāsaḥ tava, mama ca upadeṣṭṛtvāyāsaḥ pravṛttaḥ – te tava he dhanañjaya.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "naṣṭo mohaḥ smṛtirlabdhā tvatprasādānmayā'cyuta |",
            "sthito'smi gatasandehaḥ kariṣye vacanaṃ tava",
        ], "|| 73 ||",
           "Arjuna said: My delusion is destroyed, and by your grace I have regained my memory, Acyuta. I stand firm, my doubts gone. I will do as you say.",
           bhashya=[
               "naṣṭaḥ iti. naṣṭaḥ mohaḥ ajñānajaḥ samastasaṃsārānarthahetuḥ, sāgaraḥ iva dustaraḥ. smṛtiḥ ca ātmatattvaviṣayā labdhā – yasyāḥ lābhāt sarvahṛdayagranthīnāṃ vipramokṣaḥ tvatprasādāt tava prasādāt mayā tvatprasādaṃ āśritena acyuta. aneka mohanāśapraśna prativacanena sarvaśāstrārthajñānaphalaṃ etāvat eva iti niścitaṃ darśitaṃ bhavati, yataḥ jñānāt mohanāśaḥ ātmasmṛtilābhaḥ ca iti. tathā ca śrutau “anātmavit śocāmi” iti upanyasya ātmajñānena sarvagranthīnāṃ vipramokṣaḥ uktaḥ (chāṃ.u.7.1.3.26.2) “bhidyate hṛdayagranthi” (muṃ.u.2.2.8) “tatra ko mohaḥ kaḥ śokaḥ ekatvamanupaśyataḥ” (ī.u.7) iti ca mantravarṇaḥ. atha idānīṃ tvacchāsane sthitaḥ asmi gatasandehaḥ muktasaṃśayaḥ kariṣye vacanaṃ tava. ahaṃ tvatprasādāt kṛtārthaḥ, na me kartavyaṃ asti ityabhiprāyaḥ.",
           ]),
        {"speaker": "sañjaya uvāca"},
        _v([
            "ityahaṃ vāsudevasya pārthasya ca mahātmanaḥ |",
            "saṃvādamimamaśrauṣamadbhutaṃ romaharṣaṇam",
        ], "|| 74 ||",
           "Sañjaya said: Thus I heard this wondrous dialogue between Vāsudeva and the great-souled Pārtha, which makes my hair stand on end.",
           bhashya=[
               {"text": "parisamāptaḥ śāstrārthaḥ atha idānīṃ kathāsambandhapradarśanārthaṃ sañjayaḥ", "intro": True},
               "ityahaṃ iti. iti evaṃ ahaṃ vāsudevasya pārthasya ca mahātmanaḥ saṃvādaṃ imaṃ yathoktaṃ aśrauṣaṃ śrutavān asmi adbhutaṃ atyantavismayakaraṃ romaharṣaṇaṃ romāñcakaram. taṃ ca imam.",
           ]),
        _v([
            "vyāsaprasādācchrutavānimaṃ guhyatamaṃ param |",
            "yogaṃ yogeśvarāt kṛṣṇātsākṣātkathayataḥ svayam",
        ], "|| 75 ||",
           "By the grace of Vyāsa I heard this supreme secret, this yoga, from Kṛṣṇa, the lord of yoga, himself declaring it directly.",
           bhashya=[
               "vyāsa iti. vyāsaprasādāt tataḥ divyacakṣurlābhāt śrutavān imaṃ saṃvādaṃ guhyatamaṃ paraṃ yogaṃ – yogārthatvāt grantho'pi yogaḥ – saṃvādaṃ imaṃ yogam eva vā yogeśvarāt kṛṣṇāt sākṣāt kathayataḥ svayaṃ, na paramparayā.",
           ]),
        _v([
            "rājan saṃsmṛtya saṃsmṛtya saṃvādamimamadbhutam |",
            "keśavārjunayoḥ puṇyaṃ hṛṣyāmi ca muhurmuhuḥ",
        ], "|| 76 ||",
           "O king, as I remember again and again this wondrous and holy dialogue between Keśava and Arjuna, I rejoice again and again.",
           bhashya=[
               "rājan iti. he rājan dhṛtarāṣṭra, saṃsmṛtya saṃsmṛtya pratikṣaṇaṃ saṃvādaṃ imaṃ adbhutaṃ keśavārjunayoḥ puṇyaṃ imaṃ śravaṇena api pāpaharaṃ śrutvā hṛṣyāmi ca muhurmuhuḥ pratikṣaṇam.",
           ]),
        _v([
            "tacca saṃsmṛtya saṃsmṛtya rūpamatyadbhutaṃ hareḥ |",
            "vismayo me mahān rājan hṛṣyāmi ca punaḥ punaḥ",
        ], "|| 77 ||",
           "And as I remember again and again that most wondrous form of Hari, great is my astonishment, O king, and I rejoice again and again.",
           bhashya=[
               "tacca iti. tat ca saṃsmṛtya rūpaṃ atyadbhutaṃ hareḥ viśvarūpaṃ vismayaḥ me mahān rājan! hṛṣyāmi ca punaḥ punaḥ. kiṃ bahunā –",
           ]),
        _v([
            "yatra yogeśvaraḥ kṛṣṇo yatra pārtho dhanurdharaḥ |",
            "tatra śrīrvijayo bhūtirdhruvā nītirmatirmama",
        ], "|| 78 ||",
           "Wherever there is Kṛṣṇa, the lord of yoga, and wherever there is Pārtha, the archer, there, I believe, are fortune, victory, prosperity and sound policy.",
           bhashya=[
               "yatra iti. yatra yasmin pakṣe yogeśvaraḥ sarvayogānāṃ īśvaraḥ tatprabhavatvāt sarvayogabījasya – kṛṣṇaḥ, yatra pārthaḥ yasmin pakṣe dhanurtharaḥ gāṇḍivadhanvā tatra śrīḥ tasmin pāṇḍavānāṃ pakṣe śrīḥ vijayaḥ, tatraiva bhūtiḥ śriyaḥ viśeṣaḥ vistāraḥ bhūtiḥ dhruvā avyabhicāriṇī nītiḥ nayaḥ, ityevaṃ matiḥ mama iti.",
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi yogaśāstre śrī kṛṣṇārjuna saṃvāde mokṣa sannyāsayogo nāma aṣṭādaśo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the eighteenth chapter, Mokṣasannyāsa Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣya śrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye mokṣasannyāsayogo nāma aṣṭādaśo'dhyāyaḥ.", "gloss": "Thus ends the eighteenth chapter, Mokṣasannyāsa Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
