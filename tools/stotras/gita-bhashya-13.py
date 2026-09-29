# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 13 (Kṣetrakṣetrajñavibhāga Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 13 · Kṣetrakṣetrajñavibhāga Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 13",
    "h1": "Bhagavad Gītā · Chapter 13",
    "subtitle": "Kṣetrakṣetrajñavibhāga Yoga · the field and the knower of the field · with Śaṅkara's bhāṣya",
    "note": "The field (kṣetra) — the body with all it contains — and the knower of the field (kṣetrajña), whom Kṛṣṇa declares to be himself in all fields. The chapter sets out the qualities called knowledge, the object of knowledge (Brahman), and prakṛti and puruṣa. Śaṅkara's commentary on 13.2 is one of the longest and most closely argued passages of the bhāṣya. The book, like most editions of Śaṅkara's text, has 34 verses here (it does not include the extra opening verse some recensions carry).",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 12', 'gita-bhashya-12-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 14 ›', 'gita-bhashya-14-iast.html')],
    "sections": [
        {"bhashya": [
            "saptame adhyāye sūcite dve prakṛtī īśvarasya – triguṇātmikā aṣṭadhā bhinnā aparā saṃsārahetutvāt, parā ca anyā jīvabhūtā kṣetrajñalakṣaṇā īśvarātmikā, yābhyāṃ prakṛtibhyām īśvaraḥ jagadutpattisthitilayahetutvaṃ pratipadyate. tatra kṣetrakṣetrajñalakṣaṇaprakṛtidvaya nirūpaṇadvāreṇa tadvataḥ īśvarasya tattvanirdhāraṇārthaṃ kṣetrādhyāyaḥ ārabhyate. atītānantarādhyāye ca “adveṣṭā sarvabhūtānām” (12.13) ityādinā yāvadadhyāyaparisamāptiḥ tāvattattvajñānināṃ sannyāsināṃ niṣṭhā yathā te vartante ityetaduktam. kena punaḥ te tattvajñānena yuktāḥ yathoktadharmācaraṇād bhagavataḥ priyāḥ bhavanti ityevamarthaḥ ca ayam adhyāyaḥ ārabhyate – prakṛtiśca triguṇātmikā sarvakāryakaraṇaviṣayākāreṇa pariṇatā puruṣasya bhogāpavargārthakartavyatayā dehendriyādyākāreṇa saṃhanyate. so'yaṃ saṅghātaḥ idaṃ śarīram, tadetat śrī bhagavānuvāca.",
        ], "summary": "bhāṣya · the chapter's opening"},
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "idaṃ śarīraṃ kaunteya kṣetramityabhidhīyate |",
            "etadyo vetti taṃ prāhuḥ kṣetrajña iti tadvidaḥ",
        ], "|| 1 ||",
           "The Blessed Lord said: This body, son of Kuntī, is called the field; he who knows it is called the knower of the field by those who know them.",
           bhashya=[
               "idamiti – idamiti sarvanāmnā uktaṃ viśinaṣṭi “śarīram” iti. he kaunteya! kṣatatrāṇāt, kṣayāt, kṣaraṇāt, kṣetravadvā asmin karmaphalaniṣpatteḥ kṣetram iti. iti śabdaḥ evaṃ– śabdapadārthakaḥ. kṣetram iti evaṃ abhidhīyate, kathyate. etat śarīraṃ kṣetraṃ yaḥ vetti vijānāti āpādatalamastakaṃ jñānena viṣayīkaroti svābhāvikena aupadeśikena vā vedanena viṣayīkaroti vibhāgaśaḥ, taṃ veditāraṃ prāhuḥ kathayanti kṣetrajñaḥ iti. iti śabdaḥ evaṃśabdapadārthakaḥ eva pūrvavat. kṣetrajña iti evam āhuḥ. ke? tadvidaḥ tau kṣetrakṣetrajñau ye vidanti vijānanti te tadvidaḥ.",
           ]),
        _v([
            "kṣetrajñaṃ cāpi māṃ viddhi sarvakṣetreṣu bhārata |",
            "kṣetrakṣetrajñayorjñānaṃ yattad jñānaṃ mataṃ mama",
        ], "|| 2 ||",
           "Know me also as the knower of the field in all fields, O Bhārata. The knowledge of the field and of the knower of the field — that I hold to be knowledge.",
           bhashya=[
               {"text": "evaṃ kṣetrakṣetrajñau uktau. kim etāvanmātreṇa jñānena jñātavyau iti? na ityucyate –", "intro": True},
               "kṣetrajñamiti – kṣetrajñaṃ yathoktalakṣaṇaṃ cāpi māṃ parameśvaram asaṃsāriṇaṃ, viddhi jānīhi. sarvakṣetreṣu yaḥ kṣetrajñaḥ brahmādistambaparyantānekakṣetropādhipravibhaktaḥ taṃ nirastasarvopādhibhedaṃ sadasadādiśabdapratyayāgocaraṃ viddhi ityabhiprāyaḥ. he bhārata! yasmāt kṣetrakṣetrajñeśvara'yāthātmya vyatirekeṇa na jñānagocaram anyat avaśiṣṭam asti tasmāt kṣetrakṣetrajñayoḥ jñeyabhūtayoḥ yat jñānaṃ kṣetrakṣetrajñau yena jñānena viṣayīkriyete tad jñānaṃ, samyag jñānam iti matam abhiprāyaḥ mama īśvarasya viṣṇoḥ.",
               "nanu sarvakṣetreṣu eka eva īśvaraḥ na anyaḥ tadvyatiriktaḥ bhoktā vidyate cet, tataḥ īśvarasya saṃsāritvaṃ prāptamnu īśvaravyatirekeṇa vā saṃsāriṇaḥ anyasya abhāvāt saṃsārābhāvaprasaṅgaḥ, tacca ubhayam aniṣṭam, bandhamokṣataddhetuśāstrānarthakyaprasaṅgāt, pratyakṣādi pramāṇavirodhācca. pratyakṣeṇa tāvat sukhaduḥkhataddhetulakṣaṇaḥ saṃsāraḥ upalabhyate. jagadvaicitryopa labdheḥ dharmādharmanimittaḥ saṃsāraḥ anumīyate. sarvam etat anupapannam ātmeśvaraikatve.",
               "na, jñānājñānayoḥ anyatvena upapatteḥ – “dūramete viparīte viṣūcī avidyā yā ca vidyeti jñātā” (kaṭha.u.2.4). tathā ca tayoḥ vidyā'vidyayoḥ phalabhedopi viruddhaḥ nirdiṣṭaḥ – “śreyaśca preyaśca” (kaṭha.u.2.2) iti. vidyāviṣayaḥ śreyaḥ, preyastu avidyākāryam iti. tathā ca vyāsaḥ – “dvāvimāvatha panthānau” (śāṃ.pa.240.6) ityādi “imau dvāveva panthānau” ityādi ca. iha ca dve niṣṭhe ukte. avidyā ca kāryeṇa saha hātavyā iti śrutismṛtinyāyebhyaḥ avagamyate. śrutayaḥ tāvat – “iha cedavedīdatha satyamasti na cedihāvedīnmahatī vinaṣṭiḥ” (kena.u.2.5), “tamevaṃ vidvānamṛta iha bhavati nānyaḥ panthā vidyate'yanāya” (puruṣasūkte. tai.ā.3.12, śve.u.3.8), “vidvānna bibheti kutaścana” (tai.u.2.4) aviduṣaḥ tu – “atha tasya bhayaṃ bhavati” (tai.u.2.7), “avidyāyāmantare vartamānāḥ” (kaṭha.u.2.5), “brahma veda brahmaiva bhavati” (muṃ.u.3.2.9), “anyosāvanyo'hamasmīti na sa veda yathā paśurevaṃ sa devānām” (bṛha.u.1.4.10), ātmavit yaḥ – “saḥ idaṃ sarvaṃ bhavati”. (bṛ.u.1.4.10), “yadā carmavat” (śve.u.6.20) ityādyāḥ sahasraśaḥ. smṛtayaśca – “ajñānenāvṛtaṃ jñānaṃ tena muhyanti jantavaḥ” (5.15) “ihaiva tairjitaḥ sargo yeṣāṃ sāmye sthitaṃ manaḥ” (5.25), “samaṃ paśyan hi sarvatra” (13.28) ityādyāḥ.",
               "nyāyataśca – “sarpān kuśāgrāṇi tathodapānaṃ jñātvā manuṣyāḥ parivarjayanti | ajñānatastatra patanti kecid jñāne phalaṃ paśya yathā viśiṣṭam” (śāṃ.pa.201.16) tathā ca dehādiṣu ātmabuddhiḥ avidvān rāgadveṣādiprayuktaḥ dharmādharmānuṣṭhānakṛt “jāyate mriyate” ca ityavagamyate. dehādivyatiriktātmadarśinaḥ rāgadveṣādiprahāṇāt tadapekṣa dharmādharmapravṛttyupaśamanāt mucyante iti na kenacit pratyākhyātuṃ śakyaṃ nyāyataḥ. tatra evaṃ sati kṣetrajñasya īśvarasyaiva sataḥ avidyākṛtopādhibhedataḥ saṃsāritvamiva bhavati, yathā dehādyātmatvam ātmanaḥ. sarvajantūnāṃ hi prasiddhaḥ dehādiṣu anātmasu ātmabhāvaḥ niścitaḥ avidyākṛtaḥ, yathā sthāṇau puruṣaniścayaḥ. na ca etāvatā puruṣadharmaḥ sthāṇoḥ bhavati, sthāṇudharmo vā puruṣasyanu tathā na caitanyadharmaḥ dehasya, dehadharmo vā cetanasya, evaṃ sukhaduḥkhamohātmakatvādiḥ ātmanaḥ na yuktaḥ avidyākṛtatvāviśeṣāt, jarāmṛtyuvat.",
               "na, atulyatvāt iti cet – sthāṇupuruṣau jñeyau eva santau jñātrā anyonyasmin adhyastau avidyayānu dehātmanoḥ tu jñeyajñātroḥ eva itaretarādhyāsaḥ iti na samaḥ dṛṣṭāntaḥ, ataḥ dehadharmaḥ jñeyaḥ api jñātuḥ ātmanaḥ bhavati iti cet –",
               "na, acaitanyādiprasaṅgāt, yadi hi jñeyasya dehādeḥ kṣetrasya dharmāḥ sukhaduḥkha mohecchādveṣādayaḥ jñātuḥ ātmanaḥ bhavanti tadā jñeyasya kṣetrasya dharmāḥ kecit ātmanaḥ bhavanti avidyādhyāropitāḥ, jarāmaraṇādayastu na bhavanti iti viśeṣahetuḥ vaktavyaḥ. “na bhavanti” ityasti anumānam avidyādhyāropitatvāt, jarāmaraṇādivat iti, heyatvāt upādeyatvācca ityādi. tatraivaṃ sati kartṛtvabhoktṛtvalakṣaṇaḥ saṃsāraḥ jñeyasthaḥ jñātari avidyayā adhyāropitaḥ iti, na tena jñātuḥ kiñcidduṣyati. yathā bālaiḥ adhyāropitena ākāśasya talamalinatvādinā. evaṃ ca sati sarvakṣetreṣvapi sataḥ bhagavataḥ kṣetrajñasya īśvarasya saṃsāritvagandhamātram api na āśaṅkyam (na śakyaṃ vaktum). na hi kvacidapi loke avidyādhyastena dharmeṇa kasyacit upakāraḥ apakāro vā dṛṣṭaḥ.",
               "yattu uktaṃ “na samo dṛṣṭāntaḥ iti” tat asat. katham? avidyādhyāsamātraṃ hi dṛṣṭāntadārṣṭāntikayoḥ sādharmyaṃ vivakṣitamnu tat na vyabhicarati. “yattu jñātari vyabhicarati” iti manyase tasyāpi anaikāntikatvaṃ darśitaṃ jarādibhiḥ. avidyāvattvāt kṣetrajñasya saṃsāritvam iti cet, na avidyāyāḥ tāmasatvāt. tāmaso hi pratyayaḥ āvaraṇātmakatvāt avidyā, viparītagrāhakaḥ, saṃśayopasthāpakaḥ vā agrahaṇātmako vā. vivekaprakāśabhāve tadabhāvāt. tāmase ca āvaraṇātmake timirādidoṣe sati agrahaṇādeḥ avidyāmātrasya (avidyātrayasya) upalabdheḥ.",
               "atrāha – evaṃ tarhi jñātṛdharmaḥ avidyā? na, karaṇe cakṣuṣi taimirikatvādi doṣopalabdheḥ. yattu manyase jñātṛdharmaḥ avidyā, tadeva ca avidyādharmavattvaṃ kṣetrajñasya saṃsāritvamnu tatra yaduktam īśvara eva kṣetrajñaḥ na saṃsārī ityetat ayuktam iti – tat nanu yathā karaṇe cakṣuṣi viparītagrāhakādidoṣasya darśanāt. na viparītādigrahaṇaṃ tannimitto vā taimirikatvādidoṣaḥ grahītuḥ cakṣuṣaḥ saṃskāreṇa timire apanīte grahītuḥ adarśanāt na grahītuḥ adharmaḥ yathā, tathā sarvatraiva agrahaṇaviparītasaṃśayapratyayāḥ tannimittāḥ, karaṇasyaiva kasyacit bhavitum arhanti. na jñātuḥ kṣetrajñasya. saṃvedyatvācca teṣāṃ pradīpaprakāśavat na jñātṛdharmatvam. saṃvedyatvādeva svātmavyatiriktasaṃvedyatvam. sarvakaraṇaviyoge ca kaivalye sarvavādibhiḥ avidyādidoṣavattvānabhyu pagamāt. ātmanaḥ yadi kṣetrasya agnyuṣṇavat svaḥ dharmaḥ, tataḥ na kadācidapi tena viyogaḥ syāt. avikriyasya ca vyomavat sarvagatasya amūrtasya ātmanaḥ kenacit saṃyogaviyogānupapatteḥ siddhaṃ kṣetrajñasya nityam eva īśvaratvam. “anāditvānnirguṇatvāt” (13.31) iti īśvaravacanācca.",
               "nanvevaṃ sati saṃsārasaṃsāritvābhāve śāstrānarthakyādidoṣaḥ syāditi cet – na sarvaiḥ abhyupagatatvāt. sarvaiḥ hi ātmavādibhiḥ abhyupagataḥ doṣaḥ na ekena parihartavyaḥ bhavati. katham abhyupagataḥ iti? muktātmanāṃ hi saṃsārasaṃsāritvavyavahārābhāvaḥ sarvaireva ātmavādibhiḥ iṣyate. na ca teṣāṃ śāstrānarthakyādidoṣaprāptiḥ abhyupagatā. tathā naḥ, kṣetrajñānām īśvaraikatve sati śāstrānarthakyaṃ bhavatu, avidyāviṣaye ca arthavattvam, yathā dvaitavādināṃ sarveṣāṃ bandhāvasthāyām eva śāstrādyarthavatvaṃ na muktāvasthāyāṃ, evam.",
               "nanu ātmanaḥ bandhamuktāvasthe paramārthataḥ eva vastubhūte dvaitināṃ naḥ sarveṣām. ataḥ heyopādeyatatsādhanasadbhāve śāstrādyarthavattvaṃ syāt, advaitināṃ punaḥ dvaitasya aparamārthatvāt, avidyākṛtatvāt, bandhāvasthāyāśca ātmanaḥ aparamārthatve nirviṣayatvāt śāstrādyānarthakyam iti cet, na ātmanaḥ avasthābhedānupapatteḥ. yadi tāvat ātmanaḥ bandhamuktāvasthe yugapat syātāṃ krameṇa vā? yugapat tāvat virodhāt na sambhavataḥ, sthitigatī iva ekasmin. kramabhāvitve ca nirnimittatvaṃ sannimittatvaṃ vā? nirnimittatve anirmokṣaprasaṅgaḥ. sa nimittatve ca svataḥ abhāvāt aparamārthatvaprasaṅgaḥ. tathā ca sati abhyupagamahāniḥ.",
               "kiṃ ca – bandhamuktāvasthayoḥ paurvāparyānirūpaṇāyāṃ bandhāvasthā pūrvaṃ prakalpyā anādimatī, antavatī ca. tacca pramāṇaviruddham. tathā mokṣāvasthā sādimatī anantā ca pramāṇaviruddhā eva abhyupagamyate. na ca avasthāvataḥ avasthāntaraṃ gacchataḥ nityatvam upapādayituṃ śakyam. atha anityatvadoṣa parihārāya bandhamuktāvasthābhedaḥ na parikalpyate ataḥ dvaitināmapi śāstrānarthakyādidoṣaḥ aparihāryaḥ eva, iti samānatvāt na advaitavādinā parihartavyo doṣaḥ.",
               "na ca śāstrānarthakyam, yathāprasiddhāvidvatpuruṣaviṣayatvāt śāstrasya, aviduṣāṃ hi phalahetvoḥ anātmanoḥ ātmadarśanaṃ na viduṣām. viduṣāṃ hi phalahetubhyām ātmanaḥ anyatvadarśane sati tayoḥ ahamiti ātmadarśanānupapatteḥ. na hi atyantamūḍhaḥ unmattādiḥ api jalāgnyoḥ chāyāprakāśayoḥ vā aikātmyaṃ paśyati, kimuta vivekī. tasmāt na vidhipratiṣedhaśāstraṃ tāvat phalahetubhyām ātmanaḥ anyatvadarśinaḥ bhavati. na hi “devadatta tvam idaṃ kuru” iti kasmiṃścit karmaṇi niyukte viṣṇumitraḥ “ahaṃ niyuktaḥ” iti tatrasthaḥ niyogaṃ śṛṇvannapi pratipadyate. niyogaviṣayavivekāgrahaṇāttu upapadyate pratipattiḥ. tathā phalahetvoḥ api.",
               "nanu prākṛtasambandhāpekṣayā yuktāḥ eva pratipattiḥ śāstrārthaviṣayā phalahetubhyām anyātmadarśane'pi sati – iṣṭaphalahetau pravartitaḥ asmi, aniṣṭaphalahetoḥ ca nivartitaḥ asmi itinu yathā pitṛputrādīnām itaretarātmānyatvadarśane satyapi anyonyaniyoga pratiṣedhārthapratipattiḥ? (bṛ.u.1.5.17).",
               "na vyatiriktātmadarśana pratipatteḥ prāgena phalahetvo ātmābhimānasya siddhatvāt. pratipannaniyogapratiṣedhārthaḥ. hi phalahetubhyām anyatvaṃ pratipadyate, na pūrvam. tasmāt vidhipratiṣedha śāstram avidvadviṣayam iti siddham.",
               "nanu “svargakāmo yajeta” (āpa.śrau. 10.2.1) “kalañjaṃ na bhakṣayet” ityādau ātmavyatirekadarśinām apravṛttau kevaladehādyātmadṛṣṭīnāṃ ca – ataḥ kartuḥ abhāvāt śāstrānarthakyam iti cet?",
               "na, yathā prasiddhitaḥ eva pravṛttinivṛttyupapatteḥ. īśvarakṣetrajñai katvadarśī brahmavit tāvat na pravartate. tathā nairātma vādyapi “nāsti paralokaḥ” iti na pravartate. yathāprasiddhi tastu vidhipratiṣedhaśāstra śravaṇānyathā'nupa pattyā anumitātmastitvaḥ ātmaviśeṣānabhijñaḥ karmaphalaṃ sañjātatṛṣṇaḥ śraddadhānatayā ca pravartate iti sarveṣāṃ naḥ pratyakṣam, ataḥ na śāstrānarthakyam.",
               "vivekinām apravṛttidarśanāt tadanugāminām apravṛttau śāstrānarthakyam iti cet –",
               "na, kasyacideva vivekopapatteḥ. anekeṣu hi prāṇiṣu kaścideva vivekī syāt, yathā idānīm. na ca vivekinām anuvartante mūḍhāḥ, rāgādidoṣatantratvāt pravṛtteḥ, abhicaraṇādau ca pravṛttidarśanāt. svabhāvyācca pravṛtteḥ. “svabhāvastu pravartate” (5.14) iti hi uktam. tasmāt avidyāmātraṃ saṃsāraḥ yathādṛṣṭaviṣayaḥ eva, na kṣetrajñasya kevalasya avidyā tatkāryaṃ ca. na mithyājñānaṃ paramārthavastu dūṣayituṃ samartham. na hi ūṣaradeśaṃ snehena paṅkīkartuṃ śaknoti marīcyudakaṃ, tathā avidyā kṣetrajñasya na kiñcit kartuṃ śaknoti. ataśca idamuktaṃ “kṣetrajñaṃ cāpi māṃ viddhi” (13.2), “ajñānenāvṛtaṃ jñānam” (5.15) iti ca.",
               "atha kimidaṃ saṃsāriṇām iva “aham evam” “mamaiva idam” iti paṇḍitānām api?",
               "śṛṇunu idaṃ tatpāṇḍityaṃ, yat kṣetra eva ātmadarśanam. yadi punaḥ kṣetrajñam avikriyaṃ paśyeyuḥ, tataḥ na bhogaṃ karma vā ākāṅkṣeyuḥ “mama syāt” iti. vikriyaiva bhogakarmaṇī. atha evaṃ sati, phalārthitvāt avidvān pravartate. viduṣaḥ punaḥ avikriyātma darśinaḥ phalārthitvābhāvāt pravṛttyanupapattau kāryakāraṇasaṅghātavyāpāroparame nivṛttiḥ upacaryate. idaṃ ca anyat pāṇḍityaṃ kasya cit astu – kṣetrajñaḥ īśvaraḥ eva, kṣetraṃ ca anyat kṣetrajñasya eva viṣayaḥ. ahaṃ tu saṃsārī sukhī duḥkhī ca. saṃsāroparamaśca mama kartavyaḥ kṣetrakṣetrajñavijñānena dhyānena ca īśvaraṃ kṣetrajñaṃ sākṣātkṛtvā tatsvarūpa avasthānena iti. yaśca evaṃ budhyate, yaśca bodhayati, nāsau kṣetrajñaḥ iti. evaṃ manvānaḥ yaśca sa paṇḍitāpasadaḥ saṃsāramokṣayoḥ śāstrasya ca arthavattvaṃ karomi iti, ātmahā svayaṃ mūḍhaḥ, anyāṃśca vyāmohayati – śāstrārthasampradāyarahitatvāt śrutahānim aśrutakalpanāṃ ca kurvan. tasmāt asampradāyavit sarvaśāstravidapi mūrkhavadeva upekṣaṇīyaḥ.",
               "yaduktam – “īśvarasya kṣetrajñai katve saṃsāritvaṃ prāpnoti, kṣetrajñānāṃ ceśva raikatve saṃsāriṇaḥ “abhāvāt saṃsārābhāvaprasaṅgaḥ” iti – etau doṣau pratyuktau “vidyā'vidyayoḥ vailakṣaṇyābhyupagamāt” iti. katham? avidyāparikalpitadoṣeṇa tadviṣayaṃ vastu pāramārthikaṃ na duṣyati iti. tathā ca dṛṣṭāntaḥ darśitaḥ – marīcyambhasā ūṣaradeśaḥ na paṅkīkriyate iti. saṃsāriṇaḥ abhāvāt saṃsārabhāvaprasaṅgadoṣo'pi saṃsārasaṃsāriṇoḥ avidyākalpitatvopapattyā pratyuktaḥ.",
               "nanu avidyāvattvameva kṣetrajñasya saṃsāritvadoṣaḥ. tatkṛtaṃ ca sukhitva duḥ khitvādi pratyakṣam upalabhyate? iti cet –",
               "na, jñeyasya kṣetradharmatvāt, jñātuḥ kṣetrajñasya tatkṛtadoṣānupapatteḥ. yāvat kiñcit kṣetrajñasya doṣajātam avidyamānam āsañjayasi tasya jñeyatvopapatteḥ kṣetradharmatva meva na kṣetrajñadharmatvam. na ca tena kṣetrajñaḥ duṣyati, jñeyena jñātuḥ saṃsargānupapatteḥ. yadi hi saṃsargaḥ syāt jñeyatvameva na upapadyeta. yadi ātmanaḥ dharmaḥ avidyāvattvaṃ duḥkhitvādi ca kathaṃ bhoḥ pratyakṣam upalabhyate? kathaṃ vā kṣetrajñadharma? “jñeyaṃ ca tat sarvaṃ kṣetraṃ jñātaiva kṣetrajñaḥ” ityavadhārite, avidyāduḥkhitvādeḥ kṣetrajñaviśeṣaṇatvaṃ kṣetrajñadharmatvaṃ, tasya ca pratyakṣopa labhyatvam iti viruddham ucyate avidyāmātrāvaṣṭambhāt kevalam.",
               "atrāha – sā avidyā kasyeti. yasya dṛśyate tasyaiva. kasya dṛśyate iti? atrocyate – “avidyā kasya dṛśyate” iti praśnaḥ nirarthakaḥ. katham? dṛśyate cet avidyā, tadvantamapi paśyasi. na ca tadvati upalabhyamāne “sā kasyeti” praśnaḥ yuktaḥ. na hi gomati upalabhyamāne “gāvaḥ kasyeti” praśnaḥ arthavān bhavati. nanu viṣamaḥ dṛṣṭāntaḥ – gavāṃ tadvataśca pratyakṣatvāt sambandhaḥ api pratyakṣaḥ iti praśnaḥ nirarthakaḥ. na tathā avidyā tadvān ca pratyakṣau, yataḥ praśnaḥ nirarthakaḥ syāt. apratyakṣeṇa avidyāvatā avidyāsambandhe jñāte kiṃ tava syāt? avidyāyāḥ anarthahetutvāt parihartavyā syāt. yasya avidyā saḥ tāṃ parihariṣyati. nanu mamaiva avidyā? jānāsi tarhi avidyāṃ tadvantaṃ ca ātmānam. jānāmi, na tu pratyakṣeṇa. anumānena cet jānāsi kathaṃ sambandhagrahaṇam? na hi tava jñātuḥ jñeyabhūtayā avidyayā tatkāle sambandhaḥ grahītuṃ śakyate, avidyāyāḥ viṣayatvenaiva jñātuḥ upayuktatvāt. na ca jñātuḥ avidyāyāḥ ca sambandhasya yaḥ grahītā, jñānaṃ ca anyat tadviṣayaṃ sambhavati, anavasthā prāpteḥ. yadi jñātrā'pi jñeyasambandho jñāyeta anyaḥ jñātā kalpyaḥ syāt, tasyāpi anyaḥ tasyāpi anyaḥ iti anavasthā aparihāryā. yadi punaḥ avidyā jñeyā, anyadvā jñeyaṃ jñeyameva. tathā jñātā'pi jñātaiva, na jñeyaṃ bhavati. yadā ca evam avidyāduḥkhitvādyaiḥ na jñātuḥ kṣetrajñasya kiñcit duṣyati.",
               "nanu ayameva doṣaḥ yat doṣavat kṣetravijñātṛtvam? na. vijñāna svarūpasyaiva avikriyasya vijñātṛtvopacārāt. yathā uṣṇatāmātreṇa agneḥ taptakriyopacāraḥ tadvat. yathā ca atra bhagavatā kriyākārakaphalātmatvābhāvaḥ ātmani svata eva darśitaḥ avidyādhyāropitaḥ eva kriyākārakādiḥ ātmani upacaryate tathā tatra tatra “ya enaṃ vetti hantāram” (2.19), “prakṛteḥ kriyamāṇāni guṇaiḥ karmāṇi sarvaśaḥ” (3.27), “nādatte kasyacit pāpam” (5.15) ityādiprakaraṇeṣu darśitaḥ, tathaiva ca vyākhyātam asmābhiḥ. uttareṣu ca prakaraṇeṣu darśayiṣyāmaḥ.",
               "hanta! tarhi ātmani kriyākārakaphalātmatāyāḥ svataḥ abhāve avidyayā ca adhyāropitatve “karmāṇi avidvatkartavyānyeva, na viduṣām”, iti prāptam?",
               "satyam evaṃ prāptam. etadeva ca “na hi dehabhṛtā śakyam” (18.11) ityatra darśayiṣyāmaḥ. sarvaśāstropasaṃhāraprakaraṇe ca “samāsenaiva kaunteya! niṣṭhā jñānasya yā parā” (18.50) ityatra viśeṣataḥ darśayiṣyāmaḥ. alam atra bahuprapañceneti upasaṃhriyate.",
           ]),
        _v([
            "tatkṣetraṃ yacca yādṛkca yadvikāri yataśca yat |",
            "sa ca yo yatprabhāvaśca tatsamāsena me śṛṇu",
        ], "|| 3 ||",
           "Hear from me briefly what that field is, what it is like, what its modifications are and whence each arises; and who he is, and what his powers are.",
           bhashya=[
               {"text": "“idaṃ śarīraṃ (1) ityādi ślokopadiṣṭasya kṣetrādhyāyārthasya saṅgrahaślokaḥ ayamupanyasyate “tat kṣetraṃ yacca” (3) ityādi. vyācikhyāsitasya hi arthasya saṅgrahopanyāsaḥ nyāyyaḥ iti –", "intro": True},
               "tat yiti. yat nirdiṣṭam “idaṃ śarīram” iti tat tacchabdena parāmṛśati. yaccedaṃ nirdiṣṭaṃ kṣetraṃ tat, yādṛk yādṛśaṃ svakīyaiḥ dharmaiḥ, “ca” śabdaḥ samuccayārthaḥ. yadvikāri yaḥ vikāraḥ yasya tat yadvikāri, yataḥ yasmāt ca yat, “kāryam utpadyate” iti vākyaśeṣaḥ. saḥ ca yaḥ kṣetrajñaḥ nirdiṣṭaḥ saḥ yatprabhāvaḥ ye prabhāvāḥ upādhikṛtāḥ śaktayaḥ yasya saḥ yatprabhāvaḥ ca. tat kṣetrakṣetrajñayoḥ yāthātmyaṃ yathāviśeṣitaṃ samāsena saṅkṣepeṇa me mama vākyataḥ śṛṇu, śrutvā avadhāraya ityarthaḥ.",
           ]),
        _v([
            "ṛṣibhirbahudhā gītaṃ chandobhirvividhaiḥ pṛthak |",
            "brahmasūtrapadaiḥ caiva hetumadbhirviniścitaiḥ",
        ], "|| 4 ||",
           "It has been sung by seers in many ways, in distinct metres, and in the reasoned and decisive words of the Brahma-sūtras.",
           bhashya=[
               {"text": "tat kṣetrakṣetrajñayoḥ yāthātmyaṃ vivakṣitaṃ stauti śrotṛbuddhiprarocanārtham–", "intro": True},
               "ṛṣibhiriti – ṛṣibhiḥ vasiṣṭhādibhiḥ, bahudhā bahuprakāraṃ, gītaṃ kathitam, chandāṃsi ṛgādīni, taiḥ chandobhiḥ vividhaiḥ nānābhāvaiḥ nānāprakāraiḥ, pṛthak vivekataḥ, gītam. kiṃ ca – brahmasūtrapadaiḥ ca, eva brahmaṇaḥ sūcakāni vākyāni brahmasūtrāṇi, taiḥ padyate gamyate jñāyate brahmeti tāni padāni ucyante. taiḥ eva ca kṣetrakṣetrajñayoḥ yāthātmyaṃ “gītam” ityanuvartate – “ātmetyevopāsīta” (bṛ.u.1.4.7) ityevamādibhiḥ brahmasūtrapadaiḥ ātmā jñāyate. hetumadbhiḥ yuktiyuktaiḥ, viniścitaiḥ niḥsaṃśayarūpaiḥ. niścita pratyayotpādakaiḥ ityarthaḥ.",
           ]),
        _v([
            "mahābhūtānyahaṅkāro buddhiravyaktameva ca |",
            "indriyāṇi daśaikaṃ ca pañca cendriyagocarāḥ",
        ], "|| 5 ||",
           "The great elements, the ego, the understanding and the unmanifest, the ten senses and the one mind, and the five objects of the senses;",
           bhashya=[
               {"text": "stutyā abhimukhībhūtāya arjunāya āha bhagavān –", "intro": True},
               "mahābhūtāni iti – mahābhūtāni – mahānti ca tāni bhūtāni sarvavikāravyāpakatvāt. bhūtāni ca sūkṣmāṇi, (na sthūlāni). sthūlāni tu indriyagocaraśabdena abhidhāyiṣyante. ahaṅkāraḥ mahābhūtakāraṇam ahampratyayalakṣaṇaḥ. ahaṅkārakāraṇaṃ buddhiḥ adhyavasāyalakṣaṇā. tatkāraṇam avyaktameva ca, na vyaktam avyaktam, avyākṛtam, īśvaraśaktiḥ “mama māyā duratyayā” (7.14) ityuktam. evaśabdaḥ prakṛtyavadhāraṇārthaḥ . etāvat eva aṣṭadhā bhinnā prakṛtiḥ. “ca” śabdaḥ bhedasamuccayārthaḥ. indriyāṇi, daśaśrotrādīni pañca buddhyutpādakatvāt buddhīndriyāṇi, vākpāṇyādīni pañca karmanirvartakatvāt karmendriyāṇi, tāni daśa, ekaṃ ca, kiṃ tat? manaḥ ekādaśaṃ saṅkalpādyātmakam. pañca ca indriyagocarāḥ śabdādayaḥ viṣayāḥ. tānyetāni sāṅkhyāḥ caturviṃśatitattvāni ācakṣate.",
           ]),
        _v([
            "icchā dveṣaḥ sukhaṃ duḥkhaṃ saṅghātaścetanā dhṛtiḥ |",
            "etat kṣetraṃ samāsena savikāramudāhṛtam",
        ], "|| 6 ||",
           "desire, aversion, pleasure, pain, the aggregate, consciousness and steadfastness — this, in brief, is the field with its modifications.",
           bhashya=[
               {"text": "athedānīm ātmaguṇāḥ iti yān ācakṣate vaiśeṣikāḥ te'pi kṣetradharmāḥ eva, na tu kṣetrajñasya ityāha bhagavān –", "intro": True},
               "icchā iti – icchā yajjātīyaṃ sukhātmakam artham upalabdhavān pūrvaṃ, punaḥ tajjātīyam samupalabhamānaḥ tam arthaṃ ādātum icchati sukhahetuḥ itinu sā iyam icchā antaḥkaraṇasyadharmaḥ, jñeyatvāt kṣetram. tathā dveṣaḥ – yajjātīyam arthaṃ duḥ khahetutvena anubhūtavān, punaḥ tajjātīyam arthaṃ upalabhamānaḥ taṃ dveṣṭi, saḥ ayaṃ dveṣaḥ jñeyatvāt kṣetrameva. tathā sukham anukūlaṃ prasannasattvātmakaṃ jñeyatvāt kṣetrameva. duḥkhaṃ pratikūlātmakannu jñeyatvāt tadapi kṣetram. saṅghātaḥ dehendriyāṇāṃ saṃhatiḥ. tasyām abhivyaktā antaḥkaraṇavṛttiḥ, tapte iva lohapiṇḍe agniḥ ātmacaitanyābhāsarasaviddhā cetanā, sā ca kṣetraṃ, jñeyatvāt. dhṛtiḥ yayā avasādaprāptāni dehendriyāṇi dhriyante, sā ca jñeyatvāt kṣetram. sarvāntaḥkaraṇadharmopalakṣaṇārtham icchādigrahaṇam. yat uktaṃ tat upasaṃharati – etat kṣetraṃ samāsena, savikāraṃ saha vikāreṇa mahadādinā udāhṛtam uktam.",
           ]),
        _v([
            "amānitvamadambhitvamahiṃsā kṣāntirārjavam |",
            "ācāryopāsanaṃ śaucaṃ sthairyamātmavinigrahaḥ",
        ], "|| 7 ||",
           "Humility, unpretentiousness, non-violence, patience, uprightness, service of the teacher, purity, steadiness, self-restraint;",
           bhashya=[
               {"text": "yasya kṣetrabhedajātasya saṃhatiḥ “idaṃ śarīraṃ kṣetram” (1) ityuktaṃ tat kṣetraṃ vyākhyātaṃ mahābhūtādibhedabhinnaṃ dhṛtyantam (5.6) kṣetrajñaḥ vakṣyamāṇa viśeṣaṇaḥ, yasya saprabhāvasya kṣetrajñasya parijñānāt amṛtatvaṃ bhavati, taṃ “jñeyaṃ yattat pravakṣyāmi” (13.12) ityādinā saviśeṣaṇaṃ svayameva vakṣyati bhagavān. adhunā tu tadjñānasādhanagaṇam amānitvādi– lakṣaṇaṃ, yasmin sati tadjñeyavijñāne yogyaḥ adhikṛtaḥ bhavati, yatparaḥ sannyāsī jñānaniṣṭhaḥ ucyate, tam amānitvādigaṇaṃ, jñānasādhanatvāt jñānaśabdavācyaṃ vidadhāti bhagavān –", "intro": True},
               "avamānitvam iti. amānitvam – māninaḥ bhāvaḥ mānitvam, ātmanaḥ ślāghanam, tadabhāvaḥ amānitvam. adambhitvam – svadharmaprakaṭīkaraṇaṃ dambhitvaṃ. tadabhāvaḥ adambhitvam. ahiṃsā ahiṃsanam, prāṇinām apīḍanam. kṣāntiḥ parāparādhaprāptau avikriyā. ārjavam ṛju – bhāvaḥ, avakratvam. ācāryopāsanam – mokṣasādhanopadeṣṭuḥ ācāryasya śuśrūṣādiprayogeṇa sevanam. śaucam – kāyamalānāṃ mṛjjalābhyāṃ prakṣālanamnu antaśca manasaḥ pratipakṣabhāvanayā rāgādimalāpanayanaṃ śaucam. sthairyam sthirabhāvaḥ mokṣamārge eva kṛtādhyavasāyatvam. ātmavinigrahaḥ – ātmanaḥ apakārakasya ātmaśabdavācyasya kāryakaraṇasaṅghātasya, vinigrahaḥ svabhāvena sarvataḥ pravṛttasya sanmārge eva nirodhaḥ ātmavinigrahaḥ. kiṃ ca –",
           ]),
        _v([
            "indriyārtheṣu vairāgyamanahaṅkāra eva ca |",
            "janmamṛtyujarāvyādhiduḥkhadoṣānudarśanam",
        ], "|| 8 ||",
           "dispassion towards the objects of the senses, absence of egoism, and insight into the evil of birth, death, old age, sickness and pain;",
           bhashya=[
               "indriyārtheṣu iti – indriyārtheṣu śabdādiṣu dṛṣṭādṛṣṭeṣu bhogeṣu virāgabhāvaḥ vairāgyam. anahaṅkāraḥ ahaṅkārābhāvaḥ eva ca janmamṛtyujarāvyādhiduḥkhadoṣānudarśanam – janma ca mṛtyuḥ ca jarā ca vyādhayaḥ ca duḥkhāni ca teṣu janmādiduḥkhānteṣu pratyekaṃ doṣānudarśanam. janmani garbhavāsayonidvāraniḥsaraṇaṃ doṣaḥ, tasya anudarśanam ālocanam. tathā mṛtyau doṣānudarśanam. tathā jarāyāṃ prajñāśaktitejonirodhadoṣānudarśanaṃ paribhūtatā ca iti. tathā vyādhiṣu śirorogādiṣu doṣānudarśanam. tathā duḥkheṣu adhyātmādhibhūtādhi'daivanimitteṣu. athavā duḥkhānyeva doṣaḥ duḥkhadoṣaḥ tasya janmādiṣu pūrvavat anudarśanam. duḥkhaṃ janma, duḥkhaṃ mṛtyuḥ, duḥkhaṃ jarā, duḥkhaṃ vyādhayaḥ. duḥ khanimittatvāt janmādayaḥ duḥkhāni, na punaḥ svarūpeṇaiva duḥkhamiti. evaṃ janmādiṣu duḥ khadoṣānudarśanāt dehendriya'viṣayabhogeṣu vairāgyam upajāyate. tataḥ pratyagātmani pravṛttiḥ karaṇānām ātmadarśanāya. evaṃ jñānahetutvāt jñānamucyate janmādiduḥ khadoṣānudarśanam. kiñca –",
           ]),
        _v([
            "asaktiranabhiṣvaṅgaḥ putradāragṛhādiṣu |",
            "nityaṃ ca samacittatvamiṣṭāniṣṭopapattiṣu",
        ], "|| 9 ||",
           "non-attachment, absence of clinging to son, wife, home and the like, and constant evenness of mind in the face of the desired and the undesired;",
           bhashya=[
               "asaktiriti – asakti ḥ – saktiḥ saṅganimitteṣu viṣayeṣu prītimātram, tadabhāvaḥ asaktiḥ. anabhiṣvaṅgaḥ abhiṣvaṅgābhāvaḥ. abhiṣvaṅgaḥ nāma saktiviśeṣaḥ eva ananyātmabhāvanā lakṣaṇaḥ. yathā anyasmin sukhini duḥkhini vā “ahameva sukhī duḥkhī ca”, jīvati mṛte vā “ahameva jīvāmi mariṣyāmi” ca iti. kva ityāha – putradāragṛhādiṣu putreṣu dāreṣu gṛheṣu, “ādi” grahaṇāt anyeṣu api atyanteṣṭeṣu dāsavargādiṣu. tacca ubhayaṃ jñānārthatvāt jñānam ucyate. nityaṃ ca samacittatvaṃ tulyacittatā'kva? iṣṭāniṣṭopapattiṣu. iṣṭānām aniṣṭānāṃ ca, upapattayaḥ samprāptayaḥ, tāsu iṣṭāniṣṭopapattiṣu nityameva tulyacittatā. iṣṭopapattiṣu na hṛṣyati, na kupyati ca aniṣṭopapattiṣu. tacca etat nityaṃ samacittatvaṃ jñānam. kiṃ ca –",
           ]),
        _v([
            "mayi cānanyayogena bhaktiravyabhicāriṇī |",
            "viviktadeśasevitvamaratirjanasaṃsadi",
        ], "|| 10 ||",
           "unswerving devotion to me with undivided yoga, resort to solitary places, and distaste for the company of people;",
           bhashya=[
               "mayīti – mayi ca īśvare ananyayogena apṛthaksamādhinā, “na anyaḥ bhagavataḥ vāsudevāt paraḥ asti, ataḥ saḥ eva naḥ gatiḥ” ityevaṃ niścitā avyabhicāriṇī buddhiḥ ananya – yogaḥ. tena bhajanaṃ bhaktiḥ, na vyabhicaraṇaśīlā avyabhicāriṇī. sā ca jñānam. viviktadeśasevitvam – viviktaḥ svabhāvataḥ saṃskāreṇa vā aśucyādibhiḥ sarpacoravyāghrabhayādibhiḥ ca rahitaḥ araṇyanadīpulinadevagṛhādiḥ vivikto deśaḥ, taṃ sevituṃ śīlam asya iti vivikta deśasevī, tadbhāvaḥ viviktadeśasevitvam. vivikteṣu hi deśeṣu cittaṃ prasīdati yataḥ, tataḥ ātmādibhāvanā vivikte sañjāyate. ataḥ viviktadeśasevitvaṃ jñānam ucyate. aratiḥ aramaṇaṃ, janasaṃsadi – janānāṃ prākṛtānāṃ saṃskāraśūnyānām avinītānāṃ saṃsat samavāyaḥ janasaṃsat na saṃskāravatāṃ vinītānāṃ saṃsat, tasyāḥ jñānopakāritvāt. ataḥ prākṛtajanasaṃsadi aratiḥ jñānārthatvāt jñānam. kiñca –",
           ]),
        _v([
            "adhyātmajñānanityatvaṃ tattvajñānārthadarśanam |",
            "etad jñānamiti proktamajñānaṃ yadato'nyathā",
        ], "|| 11 ||",
           "constancy in the knowledge of the Self, and insight into the purpose of the knowledge of truth — this is called knowledge; what is contrary to it is ignorance.",
           bhashya=[
               "adhyātma iti – adhyātmajñānanityatvam – ātmādiviṣayajñānam adhyātmajñānam. tasmin nityabhāvaḥ nityatvam. amānitvādīnāṃ (7) jñānasādhanānām bhāvanāparipākanimittaṃ tattvajñānaṃ, tasya arthaḥ mokṣaḥ, saṃsāroparamaḥnu tasya ālocanaṃ tattvajñānārthadarśanamnu tattvajñānaphalālocane hi tatsādhanānuṣṭhāne pravṛttiḥ syāditi. etat amānitvādi tattvajñānārtha'darśanāntam uktaṃ jñānamiti proktam, jñānārthatvāt. ajñānaṃ yat ataḥ asmāt yathoktāt anyathā viparyayeṇa – mānitvam, dambhitvam, hiṃsā, akṣāntiḥ, anārjavam ityādi ajñānaṃ vijñeyaṃ pariharaṇāya, saṃsārapravṛttikāraṇatvāt iti.",
           ]),
        _v([
            "jñeyaṃ yattat pravakṣyāmi yad jñātvā'mṛtamaśnute |",
            "anādimatparaṃ brahma na sattannāsaducyate",
        ], "|| 12 ||",
           "I will declare that which is to be known, knowing which one gains immortality: the beginningless supreme Brahman, which is said to be neither being nor non-being.",
           bhashya=[
               {"text": "yathoktena jñānena jñātavyaṃ kimityākāṅkṣāyām āha – “jñeyaṃ yattat” ityādi. nanu yamāḥ niyamāśca amānitvādayaḥ, na taiḥ jñeyaṃ jñāyate. na hi amānitvādi kasyacit vastunaḥ paricchedakaṃ dṛṣṭam. sarvatraiva hi yadviṣayaṃ, jñānaṃ tadeva tasya jñeyasya paricchedakaṃ dṛśyate. na hi anyaviṣayeṇa jñānena anyat upalabhyate, yathā ghaṭaviṣayeṇa jñānena agniḥ. naiṣa doṣaḥ, jñānanimittatvāt jñānam ucyate iti hi avocāmanu jñānasahakāri kāraṇatvācca.", "intro": True},
               "jñeya jñātavyaṃ yat tat pravakṣyāmi prakarṣeṇa yathāvat vakṣyāmi. kiṃ phalaṃ taditi prarocanena śrotuḥ abhimukhīkaraṇāya āha – yat jñeyaṃ jñātvā amṛtaṃ amṛtatvaṃ aśnute, na punaḥ mriyate ityarthaḥ. anādimat – ādiḥ asya astīti ādimat. na ādimat. kiṃ tat? paraṃ niratiśayaṃ brahma “jñeyam” iti prakṛtam.",
               "atra kecit “anādimatparam” iti padaṃ chindanti, bahuvrīhiṇokte arthe matupaḥ ānarthakyam aniṣṭaṃ syāditi. arthaviśeṣaṃ ca darśayanti – ahaṃ vāsudevākhyā parā śaktiḥ yasya tat matparam iti. satyam evam apunaruktaṃ syāt arthaḥ cet sambhavati. na tu arthaḥ sambhavati, brahmaṇaḥ sarvaviśeṣapratiṣedhenaiva vijijñāpayiṣitatvāt “na sattannāsaducyate” iti. viśiṣṭaśaktimattvapradarśanaṃ viśeṣapratiṣedhaśceti vipratiṣiddham. tasmāt matupaḥ bahuvrīhiṇā samānārthatve'pi prayogaḥ ślokapūraṇārthaḥ.",
               "“amṛtattvaphalaṃ jñeyaṃ mayā ucyate” iti prarocanena abhimukhīkṛtya āha – na sat tad jñeyamucyate, nāpyasattaducyate. nanu mahatā parikarabandhena kaṇṭharaveṇa udghuṣya “jñeyaṃ pravakṣyāmi” iti, ananurūpam uktaṃ “na sattannāsaducyate” iti? na, anurūpameva uktam. katham? – sarvāsu hi upaniṣatsu jñeyaṃ brahma “neti neti” (bṛ.u.2.3.6), “asthūlam anaṇu” (bṛ.u.3.8.8) ityādi viśeṣapratiṣedhenaiva nirdiśyate, “na idaṃ tat” iti, vācaḥ agocaratvāt. nanu na tad asti yat vastu “asti” śabdena nocyate? atha “asti” śabdena nocyate nāsti tad jñeyam. vipratiṣiddhaṃ ca “jñeyaṃ tat” “astiśabdena nocyate” iti. na tāvat nāsti, nāstibuddhya viṣayatvāt. nanu sarvāḥ buddhayaḥ astināstibuddhyanugatā eva? tatraivaṃ sati jñeyamapi astibuddhyanugata pratyaya viṣayaṃ vā syāt nāstibuddhyanugatapratyayaviṣayaṃ vā syāt. na, atīndriyatvena ubhayabuddhyanugata pratyayāviṣayatvāt. yat hi indriyagamyaṃ vastu ghaṭādikaṃ, tat astibuddhyanugatapratyayaviṣayaṃ vā syāt, nāsti buddhyanugatapratyayaviṣayaṃ vā syāt. idaṃ tu jñeyam atīndriyatvena śabdaika pramāṇagamyatvāt na ghaṭādivat ubhayabuddhyanugata pratyayaviṣayam, ityataḥ “na sattannāsat” iti ucyate. yattūktaṃ viruddham ucyate, “jñeyaṃ tat” “na sattannāsaducyate” iti, na viruddham – “anyadeva tadviditādatho aviditādadhi” (ke.u.1.3) iti śruteḥ. śrutirapi viruddhārthā iti cet – yathā yajñāya śālāmārabhya “ko hi tadveda yadyamuṣmin loke'sti vā na veti” (tai.saṃ.6.1.1.) iti cet – na, viditāviditānyatvaśruteḥ avaśyavijñeyārthapratipādanaparatvāt. “yadyamuṣmin” ityādi tu vidhiśeṣaḥ arthavādaḥ.",
               "upapatteśca sadasadādiśabdaiḥ brahma nocyate iti. sarvo hi śabdaḥ arthaprakāśanāya pratyuktaḥ, śrūyamāṇaḥ ca śrotṛbhiḥ, jātikriyāguṇasambandhadvāreṇa saṅketagrahaṇa'savyapekṣaḥ arthaṃ pratyāyayati, na anyathā, adṛṣṭatvāt. tadyathā – “gauḥ” “aśvaḥ” iti vā jātitaḥ, “pacati”, “paṭhati” iti vā kriyātaḥ, “śuklaḥ” “kṛṣṇaḥ” iti vā guṇataḥ, “dhanī” “gomān” iti vā sambandhataḥ. na tu brahma jātimat, ataḥ na sadādiśabdavācyam – nāpi guṇavat. yena guṇaśabdena ucyeta – nirguṇatvāt, nāpi kriyāśabdavācyam, niṣkriyatvāt, “niṣkalaṃ niṣkriyaṃ śāntam” itiśruteḥ (śve.u.6.19). na ca sambandhī, ekatvāt. advayatvāt aviṣayatvāt, ātmatvāt ca na kenacit śabdena ucyate iti yuktamnu “yato vāco nivartante” (tai.u.2.9.9) ityādi śrutibhiḥ ca.",
           ]),
        _v([
            "sarvataḥ pāṇipādaṃ tatsarvato'kṣiśiromukham |",
            "sarvataḥ śrutimalloke sarvamāvṛtya tiṣṭhati",
        ], "|| 13 ||",
           "With hands and feet everywhere, with eyes, heads and faces everywhere, with ears everywhere, it abides in the world, enveloping all.",
           bhashya=[
               {"text": "sacchabdapratyayāviṣayatvāt asattvāśaṅkāyāṃ jñeyasya sarvaprāṇikaraṇopādhidvāreṇa tadastitvaṃ pratipādayan tadāśaṅkānivṛttyartham āha –", "intro": True},
               "sarvataḥ iti – sarvataḥ pāṇipādam – sarvataḥ pāṇayaḥ pādāḥ ca asya iti sarvataḥ pāṇipādaṃ tat jñeyam. sarvaprāṇikaraṇopādhibhiḥ kṣetrajñasyāstitvaṃ vibhāvyate. kṣetrajñaśca kṣetropādhitaḥ ucyate. kṣetraṃ ca pāṇipādādibhiḥ anekadhā bhinnam. kṣetropādhibhedakṛtaṃ viśeṣajātaṃ mithyaiva kṣetrajñasya, iti tadapanayanena jñeyatvam uktaṃ “na sattannāsaducyate” iti. upādhikṛtaṃ mithyārūpamapi astitvādhigamāya jñeyadharmavat parikalpya ucyate “sarvataḥ pāṇipādam” ityādi. tathā hi sampradāyavidāṃ vacanam – “adhyāropāpavādābhyāṃ niṣprapañcaṃ prapañcyate” iti. sarvatra sarvadehāvayavatvena gamyamānāḥ pāṇipādādayaḥ jñeyaśakti sadbhāvanimittasvakāryāḥ iti jñeyasadbhāve liṅgāni, “jñeyasya” iti upacārataḥ ucyante. tathā vyākhyeyamanyat. sarvataḥ pāṇipādaṃ tat jñeyaṃ, sarvataḥ akṣiśiromukhaṃ, sarvataḥ akṣīṇi śirāṃsi mukhāni ca yasya tat sarvato'kṣiśiromukhamnu sarvataḥ śrutimat śrutiḥ śravaṇendriyaṃ, tat yasya tat śrutimat loke prāṇinikāyenu sarvam āvṛtya sarvaṃ vyāpya tiṣṭhati sthitiṃ labhate.",
           ]),
        _v([
            "sarvendriyaguṇābhāsaṃ sarvendriyavivarjitam |",
            "asaktaṃ sarvabhṛccaiva nirguṇaṃ guṇabhoktṛ ca",
        ], "|| 14 ||",
           "Shining through the functions of all the senses, yet free of all the senses; unattached, yet sustaining all; free of the guṇas, yet the experiencer of the guṇas;",
           bhashya=[
               {"text": "upādhibhūtapāṇipādādīndriyādhyāropaṇāt jñeyasya tadvattāśaṅkā mā bhūt ityevamarthaḥ ślokārambha :", "intro": True},
               "sarvendriya iti – sarvendriyaguṇābhāsam – sarvāṇi ca tāni indriyāṇi śrotrādīni, buddhīndriya karmendriyākhyāni, antaḥkaraṇe ca buddhimanasī jñeyopādhitvasya tulyatvāt sarvendriya – grahaṇena gṛhyante. api ca, antaḥkaraṇopādhidvāreṇaiva śrotrādīnāmapi upādhitvam ityataḥ antaḥkaraṇabahiṣkaraṇopādhibhūtaiḥ sarvendriyaguṇaiḥ adhyavasāyasaṅkalpaśravaṇavacanādibhiḥ avabhāsate iti sarvendriyaguṇābhāsam, sarvendriyavyāpāraiḥ vyāpṛtamiva tad jñeyamityarthaḥ. “dhyāyatīva lelāyatīva” (bṛ.u.4.3.7) iti śruteḥ. kasmāt punaḥ kāraṇāt na vyāpṛtameva iti gṛhyate ityataḥ āha – sarvendriyavivarjitaṃ sarvakaraṇarahitam ityarthaḥ. ataḥ na karaṇavyāpāraiḥ vyāpṛtaṃ tad jñeyam. yastu ayaṃ mantraḥ “apāṇipādo javano grahītā paśyatyacakṣuḥ sa śṛṇotya 'karṇaḥ” (śve.u.3.19) ityādiḥ saḥ sarvendriyopādhi guṇānuguṇyabhajanaśaktimat tat jñeyam ityevaṃ pradarśanārthaḥnu na tu sākṣādeva jananādikriyāvattvapradarśanārthaḥ “andho maṇimavindat” (tai.ā.1.1) ityādimantrārthavat tasya mantrasya arthaḥ. yasmāt sarvakaraṇavarjitaṃ tat jñeyaṃ, tasmāt asaktaṃ sarvasaṃśleṣavarjitam. yadyapi evaṃ, tathāpi sarvabhṛt ca eva. sadāspadaṃ hi sarvaṃ, sarvatra sadbuddhyanugamāt. na hi mṛgatṛṣṇikādayaḥ api nirāspadā bhavanti. ataḥ sarvabhṛt sarvaṃ bibharti iti. syāt idaṃ ca anyat jñeyasya sattvādhigamadvāram – nirguṇaṃ – sattvarajastamāṃsi guṇāḥ taiḥ varjitaṃ tat jñeyaṃ, tathāpi guṇabhoktṛ ca – guṇānāṃ sattvarajastamasāṃ śabdādi dvāreṇa sukhaduḥkhamohākārapariṇatānāṃ, bhoktṛ ca upalabdhṛ ca tat jñeyam – ityarthaḥ – kiñca –",
           ]),
        _v([
            "bahirantaśca bhūtānāmacaraṃ carameva ca |",
            "sūkṣmatvāttadavijñeyaṃ dūrasthaṃ cāntike ca tat",
        ], "|| 15 ||",
           "outside and inside beings, unmoving and moving; too subtle to be known; far away and yet near is That.",
           bhashya=[
               "bahiḥ iti – bahiḥ – tvakparyantaṃ deham ātmatvena avidyākalpitam apekṣya tameva avadhiṃ kṛtvā bahiḥ ucyate. tathā pratyagātmānam apekṣya dehameva avadhiṃ kṛtvā antaḥ ucyate. “bahirantaśca” ityukte madhye abhāve prāpte idam ucyate – acaraṃ carameva ca, yat carācaraṃ, dehābhāsamapi, tadeva jñeyaṃ, yathā rajjuḥ sarpābhāsaḥ. yadi acaraṃ carameva ca syāt vyavahāraviṣayaṃ sarvaṃ jñeyaṃ kimartham “idam” iti sarvaiḥ na vijñeyam iti? ucyate – satyaṃ sarvābhāsaṃ tat, tathāpi vyomavat sūkṣmam. antaḥ sūkṣmatvāt svena rūpeṇa tat jñeyamapi avijñeyam aviduṣām. viduṣāṃ tu – “ātmaiva idaṃ sarvam” (bṛ.u.2.4.6) “brahmaivedaṃ sarvam” (bṛ.u.2.5.1) ityādipramāṇataḥ nityaṃ vijñātam. avijñātatayā dūrasthaṃ varṣasahasra koṭyā'pi aviduṣām aprāpyatvāt. antike ca tat ātmatvāt viduṣām. kiṃ ca –",
           ]),
        _v([
            "avibhaktaṃ ca bhūteṣu vibhaktamiva ca sthitam |",
            "bhūtabhartṛ ca tad jñeyaṃ grasiṣṇu prabhaviṣṇu ca",
        ], "|| 16 ||",
           "Undivided, it abides in beings as though divided. It is to be known as the sustainer of beings, their devourer and their creator.",
           bhashya=[
               "avibhaktaṃ iti – avibhaktaṃ ca, pratidehaṃ vyomavat tat ekam. bhūteṣu sarvaprāṇiṣu vibhaktamiva ca sthitaṃ, deheṣveva vibhāvyamānatvāt. bhūtabhartṛ ca – bhūtāni bibhartīti tat jñeyaṃ bhūtabhartṛ ca sthitikāle. pralayakāle ca grasiṣṇu grasanaśīlam. utpattikāle prabhaviṣṇu ca prabhavanaśīlaṃ, yathā rajjvādiḥ sarpādeḥ mithyākalpitasya.",
           ]),
        _v([
            "jyotiṣāmapi tajjyotistamasaḥ paramucyate |",
            "jñānaṃ jñeyaṃ jñānagamyaṃ hṛdi sarvasya viṣṭhitam",
        ], "|| 17 ||",
           "The light of lights, it is said to be beyond darkness. Knowledge, the object of knowledge, the goal of knowledge — it is seated in the hearts of all.",
           bhashya=[
               {"text": "kiṃ ca– sarvatra vidyamānamapi sat na upalabhyate cet jñeyaṃ tamaḥ tarhi? na. kiṃ tarhi –", "intro": True},
               "jyotiṣām iti – jyotiṣām ādityādīnām api, tat jñeyaṃ, jyotiḥ. ātmacaitanya jyotiṣā iddhāni hi ādityādīni jyotīṃṣi dīpyante. “yena sūryastapati tejaseddhaḥ” (tai.brā.3.12.9), “tasya bhāsā sarvamidaṃ vibhāti” (śve.u.6.14) ityādi mantrebhyaḥnu smṛteśca ihaiva “yadāditya gataṃ tejaḥ” (15.12.) ityādeḥ. tamasaḥ ajñānāt, param asaṃspṛṣṭam, ucyate. jñānādeḥ duḥkhasampādanabuddhyā prāptāvasādasya uttambhanārtham āha jñānam amānitvādi (13.7'11), jñeyaṃ “jñeyaṃ yattat pravakṣyāmi” (13.12'17) ityādinā uktam. jñānagamyam jñeyameva jñātaṃ sat jñānaphalam iti jñānagamyam ucyate. jñāyamānaṃ tu tad jñeyam. tat etat trayamapi hṛdi buddhau sarvasya prāṇijātasya, viṣṭhitaṃ viśeṣeṇa sthitam. tatraiva hi etat trayaṃ vibhāvyate.",
           ]),
        _v([
            "iti kṣetraṃ tathā jñānaṃ jñeyaṃ coktaṃ samāsataḥ |",
            "madbhakta etadvijñāya madbhāvāyopapadyate",
        ], "|| 18 ||",
           "Thus the field, knowledge and the object of knowledge have been briefly told. My devotee who understands this enters into my being.",
           bhashya=[
               {"text": "yathoktārthopasaṃhārārthaḥ ayaṃ ślokaḥ ārabhyate –", "intro": True},
               "iti kṣetraṃ iti – iti evam kṣetram mahābhūtādi dhṛtyantaṃ (13.5'6), tathā jñānam amānitvādi tattvajñānārthadarśanaparyantam (13.7'11), jñeyaṃ ca “jñeyaṃ yattat” (13.12) ityādi “tamasaḥ paramucyate” (13.17) ityevamantam, uktaṃ samāsataḥ saṅkṣepataḥ. etāvān hi sarvaḥ vedārthaḥ gītārthaśca upasaṃhṛtya uktaḥ. asmin samyagdarśane kaḥ adhikriyate iti ucyate – madbhaktaḥ mayi sarveśvare sarvajñe paramagurau vāsudeve samarpitasarvātmabhāvaḥ yat paśyati śṛṇoti spṛśati vā “sarvameva bhagavān vāsudevaḥ” ityevaṅgrahāviṣṭabuddhiḥ madbhaktaḥ saḥ etat yathoktaṃ samyagdarśanaṃ vijñāya, madbhāvāya – mama bhāvaḥ madbhāvaḥ, paramātmabhāvaḥ, tasmai madbhāvāya upapadyate ghaṭate, mokṣaṃ gacchati.",
           ]),
        _v([
            "prakṛtiṃ puruṣaṃ caiva viddhyanādī ubhāvapi |",
            "vikārāṃśca guṇāṃścaiva viddhi prakṛtisambhavān",
        ], "|| 19 ||",
           "Know that prakṛti and puruṣa are both beginningless; and know that the modifications and the guṇas arise from prakṛti.",
           bhashya=[
               {"text": "tatra saptamādhyāye īśvarasya dve prakṛtī upanyaste parāpare kṣetrakṣetrajña lakṣaṇe nu “etadyonīni bhūtāni” (7.6) iti coktam. kṣetrakṣetrajñaprakṛtidvayayonitvaṃ kathaṃ bhūtānām ityayam arthaḥ adhunā ucyate –", "intro": True},
               "prakṛtiṃ iti – prakṛtiṃ puruṣaṃ caiva īśvarasya prakṛtī, tau prakṛtipuruṣau ubhau api anādī viddhi. na vidyate ādiḥ yayoḥ tau anādī. nityeśvaratvādīśvarasya tatprakṛtyorapi yuktaṃ nityatvena bhavitum. prakṛtidvayavattvameva hi īśvarasya īśvaratvam. yābhyāṃ prakṛtibhyām īśvaraḥ jagadutpattisthitipralayahetuḥ. te dve prakṛtī anādī satyau saṃsārasya kāraṇam.",
               "“na ādī anādī” iti tatpuruṣasamāsaṃ kecit varṇayanti. tena hi kila īśvarasya kāraṇatvaṃ sidhyati. yadi punaḥ prakṛtipuruṣāveva nityau syātāṃ tatkṛtameva jagat, na īśvarasya jagataḥ kartṛtvam. tadasat – prāk prakṛtipuruṣayoḥ utpatteḥ īśitavyābhāvāt īśvarasya anīśvaratvaprasaṅgāt, saṃsārasya nirnimittatve anirmokṣaprasaṅgāt, śāstrānarthakya prasaṅgāt, bandhamokṣābhāvaprasaṅgācca. nityatve punaḥ īśvarasya prakṛtyoḥ sarvam etat upapannaṃ bhavet. katham? vikārān ca guṇān ca eva, vakṣyamāṇān vikārān buddhyādi dehendriyāntān, guṇān ca sukhaduḥkhamohapratyayākārapariṇatān vṛkṣyamāṇān viddhi jānīhi, prakṛtisambhavān, prakṛtiḥ īśvarasya vikārakāraṇaśaktiḥ triguṇātmikā māyā, sā sambhavaḥ yeṣāṃ vikārāṇāṃ guṇānāṃ ca tān vikārān guṇān ca viddhi jānīhi prakṛtisambhavān prakṛtipariṇāmān.",
           ]),
        _v([
            "kāryaka(kā)raṇakartṛtve hetuḥ prakṛtirucyate |",
            "puruṣaḥ sukhaduḥkhānāṃ bhoktṛtve heturucyate",
        ], "|| 20 ||",
           "Prakṛti is said to be the cause in the production of body and organs; puruṣa is said to be the cause in the experience of pleasure and pain.",
           bhashya=[
               {"text": "ke punaḥ te vikārāḥ guṇāḥ ca prakṛtisambhavāḥ?", "intro": True},
               "kārya iti – kāryaṃ śarīram. karaṇāni tatsthāni trayodaśa. dehasyārbhakāṇi bhūtāni, pañca viṣayāśca prakṛtisambhavāḥ vikārāḥ pūrvoktāḥ iha kāryagrahaṇena gṛhyante. guṇāśca prakṛtisambhavāḥ sukhaduḥkhamohātmakāḥ karaṇāśrayatvāt karaṇagrahaṇena gṛhyante. teṣāṃ kāryakaraṇānāṃ kartṛtvam utpādakatvaṃ yat tat kāryakaraṇakartṛtvam, tasmin kāryakaraṇakartṛtve hetuḥ kāraṇam, ārambhakatvena prakṛtiḥ ucyate. evaṃ kāryakaraṇakartṛtvena saṃsārasya kāraṇaṃ prakṛtiḥ. “kāryakāraṇakartṛtve” ityasmin api pāṭhe kāryaṃ – yadasya vipariṇāmaḥ tat tasya kāryam. vikāraḥ vikāri, kāraṇam. tayoḥ vikāravikāriṇoḥ kāryakāraṇayoḥ kartṛtve iti. tāni eva kāryakāraṇāni ucyante. athavā ṣoḍaśa vikārāḥ kāryam. sapta prakṛti vikṛtayaḥ kāraṇam. teṣāṃ kartṛtve hetuḥ prakṛtiḥ ucyate ārambhakatvenaiva. puruṣaśca saṃsārasya kāraṇaṃ yathā syāt tat ucyate – puruṣaḥ jīvaḥ kṣetrajñaḥ bhoktā iti paryāyaḥ. saḥ sukhaduḥkhānāṃ bhogyānāṃ, bhoktṛtve upalabdhṛtve hetuḥ ucyate. kathaṃ punaḥ anena kāryakaraṇakartṛtvena sukhaduḥkhabhoktṛtvena ca prakṛtipuruṣayoḥ saṃsārakāraṇatvam ucyate iti? atrocyate – kāryakaraṇasukhaduḥkharūpeṇa hetuphalātmanā prakṛteḥ pariṇāmābhāve puruṣasya ca cetanasya asati tadupalabdhṛtve kutaḥ saṃsāraḥ syāt? yadā punaḥ kāryakaraṇa sukhaduḥkharūpeṇa hetuphalātmanā pariṇatayā prakṛtyā bhogyayā puruṣasya tadviparītasya bhoktṛtvena avidyārūpaḥ saṃyogaḥ syāt tadā saṃsāraḥ syāt iti. ataḥ yat prakṛtipuruṣayoḥ kāryakaraṇakartṛtvena sukhaduḥkhabhoktṛtvena ca saṃsārakāraṇatvam uktaṃ. tat yuktam uktam. kaḥ punaḥ ayaṃ saṃsāraḥ nāma? sukhaduḥkhasambhogaḥ saṃsāraḥ. puruṣasya sukhaduḥkhānāṃ sambhoktṛtvaṃ saṃsāritvam iti.",
           ]),
        _v([
            "puruṣaḥ prakṛtistho hi bhuṅkte prakṛtijān guṇān |",
            "kāraṇaṃ guṇasaṅgo'sya sadasadyonijanmasu",
        ], "|| 21 ||",
           "For puruṣa, abiding in prakṛti, experiences the guṇas born of prakṛti; attachment to the guṇas is the cause of its births in good and evil wombs.",
           bhashya=[
               {"text": "yatpuruṣasya sukhaduḥkhānāṃ bhoktṛtvaṃ saṃsāritvam iti uktaṃ tasya tat kiṃ nimittamiti? ucyate –", "intro": True},
               "puruṣaḥ iti – puruṣaḥ bhoktā, prakṛtisthaḥ – prakṛtau avidyālakṣaṇāyāṃ kāryakaraṇarūpeṇa pariṇatāyāṃ sthitaḥ prakṛtisthaḥ, prakṛtim ātmatvena gataḥ ityetat. hi yasmāt tasmāt bhuṅkte upalabhate ityarthaḥ. prakṛtijān prakṛtitaḥ jātān sukhaduḥ khamohākārābhivyaktān guṇān “sukhī– duḥkhī, mūḍhaḥ paṇḍita aham” ityevam. satyāmapi avidyāyāṃ sukhaduḥkhamoheṣu guṇeṣu bhujyamāneṣu yaḥ saṅgaḥ ātmabhāvaḥ, saṃsārasya saḥ pradhānaṃ kāraṇaṃ asya puruṣasya janmanaḥ – “sa yathākāmo bhavati tatkraturbhavati” (bṛ.u.4.4.5) ityādi śruteḥ. tadetat āha – kāraṇaṃ hetuḥ guṇasaṅgaḥ guṇeṣu saṅgaḥ, asya puruṣasya bhoktuḥ, sadasadyonijanmasu – sat ca asat ca yonayaḥ sadasadyonayaḥ, tāsu sadasadyoniṣu janmāni sadasadyonijanmāni, teṣu sadasadyonijanmasu viṣayabhūteṣu kāraṇaṃ guṇasaṅgaḥ. athavā, sadasadyonijanmasu asya saṃsārasya kāraṇaṃ guṇasaṅgaḥ iti saṃsārapadam adhyāhāryam. sadyonayaḥ devādiyo'nayaḥ, asadyonayaḥ paśvādiyonayaḥ, sāmarthyāt sadasadyonayaḥ manuṣyayonayaḥ api aviruddhāḥ draṣṭavyāḥ. etat uktaṃ bhavati.",
               "prakṛtisthatvākhyā avidyā, guṇeṣu ca saṅgaḥ kāmaḥ saṃsārasya kāraṇam iti. tacca parivarjanāya ucyate. asya ca nivṛtti kāraṇaṃ jñānavairāgye sasannyāse gītāśāstre prasiddham. tacca jñānaṃ purastāt upanyastaṃ kṣetrakṣetrajñaviṣayam. “yad jñātvā'mṛtamaśnute” (13.12) iti. uktaṃ ca anyāpohena ataddharmādhyāropeṇa ca (13.13).",
           ]),
        _v([
            "upadraṣṭā'numantā ca bhartā bhoktā maheśvaraḥ |",
            "paramātmeti cāpyukto dehe'smin puruṣaḥ paraḥ",
        ], "|| 22 ||",
           "The supreme Person in this body is also called the witness, the consenter, the sustainer, the experiencer, the great lord, and the supreme Self.",
           bhashya=[
               {"text": "tasyaiva punaḥ sākṣāt nirdeśaḥ kriyate –", "intro": True},
               "upadraṣṭā – samīpasthaḥ san draṣṭā svayam avyāpṛtaḥ, yathā ṛtvigyaja – māneṣu yajñakarmavyāpṛteṣu taṭasthaḥ anyaḥ avyāpṛtaḥ yajñavidyākuśalaḥ ṛtvigyajamānavyāpāra – guṇadoṣāṇām īkṣitā, tadvat kāryakaraṇavyāpāreṣu avyāpṛtaḥ anyaḥ vilakṣaṇaḥ teṣāṃ kāryakaraṇānāṃ savyāpārāṇāṃ sāmīpyena draṣṭā upadraṣṭā. athavā dehacakṣurmanobuddhyātmānaḥ draṣṭāraḥ. teṣāṃ bāhyaḥ draṣṭā dehaḥ. tataḥ ārabhya antaratamaḥ ca pratyak samīpaḥ ātmā draṣṭā, yataḥ paraḥ antaraḥ nāsti saḥ atiśayasāmīpyena draṣṭṛtvāt upadraṣṭā. yajñopadraṣṭṛvadvā sarvaviṣayīkaraṇāt upadraṣṭā. anumantā ca – anumodanam anumananam. kurvatsu tatkriyāsu paritoṣaḥ. tatkartā anumantā ca. athavā, anumantā – kāryakaraṇapravṛttiṣu svayam apravṛttaḥ api pravṛttaḥ iva tadanukūlaḥ vibhāvyate, tena anumantā. athavā pravṛttān svavyāpāreṣu tatsākṣibhūtaḥ kadācidapi na nivārayati iti anumantā. bhartā – bharaṇaṃ nāma dehendriya manobuddhīnāṃ saṃhatānāṃ caitanyātmapārārthyena nimittabhūtena caitanyābhāsānāṃ yat svarūpadhāraṇaṃ tat caitanyātmakṛtameveti bhartā ātmā ucyate. bhoktā – agnyuṣṇavat nityacaitanya svarūpeṇa buddheḥ sukhaduḥkhamohātmakāḥ pratyayāḥ sarva viṣaya viṣayāḥ caitanyātmagrastāḥ iva jāyamānāḥ vibhaktāḥ vibhāvyante iti bhoktā ātmā ucyate. maheśvaraḥ – sarvātmatvāt svatantratvācca mahān ca asau īśvaraśca iti maheśvaraḥ. paramātmā dehādīnāṃ buddhyantānāṃ, pratyagātmatvena parikalpitānām avidyayā paramaḥ upadraṣṭṛtvādilakṣaṇaḥ ātmā iti paramātmā. saḥ antaḥ (taḥ) “paramātmā” ityanena śabdena cāpi uktaḥ kathitaḥ śrutau. kva asau? asmin dehe paraḥ avyaktāt, “uttamaḥ puruṣastvanyaḥ paramātmetyudāhṛtaḥ” (15.17) iti yo vakṣyamāṇaḥ “kṣetrajñaṃ cāpi māṃ viddhi” (13.2) iti upanyastaḥ vyākhyāya upasaṃhṛtaśca.",
           ]),
        _v([
            "ya evaṃ vetti puruṣaṃ prakṛtiṃ ca guṇaiḥ saha |",
            "sarvathā vartamāno'pi na sa bhūyo'bhijāyate",
        ], "|| 23 ||",
           "He who thus knows puruṣa and prakṛti with its guṇas is not born again, however he may live.",
           bhashya=[
               {"text": "tametaṃ yathoktalakṣaṇam ātmānam –", "intro": True},
               "ya evaṃ iti. yaḥ evaṃ yathoktaprakāreṇa vetti puruṣaṃ sākṣāt ātmabhāvena “ayaṃ ahaṃ asmi” iti, prakṛtiṃ ca yathoktām avidyālakṣaṇāṃ guṇaiḥ svavikāraiḥ saha, nivartitām abhāvam āpāditāṃ vidyayā, sarvathā sarvaprakāreṇa vartamānaḥ api saḥ bhūyaḥ punaḥ patite asmin vidvaccharīre, dehāntarāya na abhijāyate, na utpadyate. dehāntaraṃ na gṛhṇāti ityarthaḥ. api śabdāt kimu vaktavyaṃ svavṛttasthaḥ na jāyate iti abhiprāyaḥ.",
               "nanu yadyapi jñānotpattyanantaraṃ punarjanmābhāvaḥ uktaḥ, tathā'pi prāg jñānotpatteḥ kṛtānāṃ karmaṇām, uttara kālabhāvināṃ ca yāni ca atikrāntāneka janmakṛtāni teṣāṃ ca, phalam adattvā nāśo na yuktaḥ iti, syuḥ trīṇi janmāni, kṛtavipraṇāśo hi na yuktaḥ iti, yathā phale pravṛttānām ārabdhajanmanāṃ karmaṇām na ca karmaṇāṃ viśeṣaḥ avagamyate. tasmāt triprakārāṇyapi karmāṇi trīṇi janmāni ārabherannu saṃhatāni vā sarvāṇi ekaṃ janma ārabheran. anyathā kṛtavipraṇāśe sati sarvatra anāśvāsaprasaṅgaḥ, śāstrārthānarthakyaṃ ca syāt. ityataḥ idam ayuktaṃ uktaṃ “na sa bhūyo'bhijāyate” iti. nanu “kṣīyante cāsya karmāṇi” (mu.u.2.2.8), “brahma veda brahmaiva bhavati” (mu.3.2.9), “tasya tāvadeva ciram” (chāṃ.u.6.14.2), “iṣīkātūlavat sarvāṇi karmāṇi pradūyante” (chāṃ.u.5.24.3. arthatonuvādaṃ) ityādi śrutiśatebhyaḥ uktaḥ viduṣaḥ sarvakarmadāhaḥ. ihāpi ca uktaḥ “yathaidhāṃsi” (4.37) ityādinā sarvakarmadāhaḥ, vakṣyati ca (18.66) upapatteśca – avidyākāmakleśabījanimittāni hi karmāṇi janmāntarāṅkuram ārabhante. ihāpi ca “sāhaṅkārābhi – sandhīni karmāṇi phalārambhakāṇi, na itarāṇi” iti tatra tatra bhagavatā uktam. bījānyagnyupadagdhāni na rohanti yathā punaḥ jñānadagdhaistathā kleśairnātmā sampadyate punaḥ (vana.pa. 200.100) iti ca.",
               "astu tāvat jñānotpattyuttarakālakṛtānāṃ karmaṇāṃ jñānena dāhaḥ, jñānasahabhāvitvāt. na tu iha janmani jñānotpatteḥ prāk kṛtānām karmaṇāṃ atītānekajanmāntara kṛtānāṃ ca dāhaḥ yuktaḥ. nanu “sarvakarmāṇi” (4.37) iti viśeṣaṇāt. jñānottarakālabhāvināmeva sarvakarmaṇām iti cet – nanu saṅkoce kāraṇānupapatteḥ. yattu uktaṃ “yathā vartamānajanmārambhakāṇi karmāṇi na kṣīyante phaladānāya pravṛttānyeva satyapi jñāne, tathā anārabdhaphalānāmapi karmaṇāṃ kṣayaḥ na yuktaḥ” iti tadasat. katham? teṣāṃ mukteṣuvat pravṛttaphalatvāt. yathā pūrvaṃ lakṣyavedhāya muktaḥ iṣuḥ dhanuṣaḥ lakṣyavedhottarakālamapi ārabdhavegakṣayāt patanenaiva nivartate, evaṃ śarīrārambhakaṃ karma śarīrasthitiprayojane nivṛtte'pi ā saṃskāravegakṣayāt pūrvavat pravartate eva. sa eva iṣuḥ pravṛttinimittānārabdhavegaḥ tu amuktaḥ dhanuṣi prayuktaḥ api upasaṃhriyate, tathā anārabdhaphalāni karmāṇi svāśrayasthānyeva tattvajñānena nirbījīkriyante iti, patite asmin vidvaccharīre “na sa bhūyo'bhijāyate” iti, yuktameva uktam iti siddham.",
           ]),
        _v([
            "dhyānenātmani paśyanti kecidātmānamātmanā |",
            "anye sāṅkhyena yogena karmayogena cāpare",
        ], "|| 24 ||",
           "Some see the Self in the self by the self through meditation; others by the yoga of Sāṅkhya; others by the yoga of action.",
           bhashya=[
               {"text": "atra ātmadarśane upāyavikalpāḥ ime dhyānādayaḥ ucyante –", "intro": True},
               "dhyānena iti – dhyānena – dhyānaṃ nāma śabdādibhyo viṣayebhya śrotrādīni karaṇāni manasi upasaṃhṛtya, manaśca pratyakcetayitari, ekāgratayā yaccintanaṃ, tat dhyānam. tathā – dhyāyatīva bakaḥ, “dhyāyatīva pṛthivī ... dhyāyantīva parvatāḥ” (chāṃ.u.7.6.1) iti upamopādānāt tailadhārāvat santataḥ avicchinnapratyayaḥ dhyānam. tena dhyānena, ātmani buddhau, paśyanti ātmānaṃ pratyakcetanam, ātmanā svenaiva pratyakcetanena dhyānasaṃskṛtena antaḥkaraṇena, kecit yoginaḥ. anye sāṅkhyena yogena. sāṅkhyaṃ nāma – “ime sattvarajastamāṃsi guṇāḥ mayā dṛśyāḥ, ahaṃ tebhyaḥ anyaḥ, tadvyāpārasākṣibhūtaḥ nityaḥ guṇavilakṣaṇaḥ ātmā” iti cintanannu sāṅkhyaḥ yogaḥ, tena “paśyanti ātmānam ātmanā” iti vartate. karmayogena – karmaiva yogaḥ. īśvarārpaṇabuddhyā anuṣṭhīyamānaṃ ghaṭanarūpaṃ yogārthatvāt yoga ucyate guṇataḥ. tena sattvaśuddhijñānotpattidvāreṇa ca apare.",
           ]),
        _v([
            "anye tvevamajānantaḥ śrutvā'nyebhya upāsate |",
            "te'pi cātitarantyeva mṛtyuṃ śrutiparāyaṇāḥ",
        ], "|| 25 ||",
           "Others, not knowing this, worship on hearing it from others; they too, devoted to what they have heard, cross beyond death.",
           bhashya=[
               "anyetu iti – anye tu eteṣu vikalpeṣu anyatamenāpi evaṃ yathoktam ātmānam ajānantaḥ, anyebhyaḥ ācāryebhyaḥ śrutvā “idameva cintayata” iti uktāḥ upāsate śraddadhānāḥ santaḥ cintayanti. te'pi ca atitarantyeva atikrāmantyeva, mṛtyuṃ – mṛtyuyuktaṃ saṃsāram ityetat. śrutiparāyaṇāḥ – śrutiḥ śravaṇaṃ param ayanaṃ gamanaṃ mokṣamārgapravṛttau paraṃ sādhanaṃ yeṣāṃ te śrutiparāyaṇāḥ, kevalaṃ paropadeśa pramāṇāḥ, svayaṃ vivekarahitāḥ ityabhi prāyaḥ. kimuvaktavyaṃ pramāṇaṃ prati svatantrāḥ vivekinaḥ mṛtyum atikrāmanti ityabhiprāyaḥ.",
           ]),
        _v([
            "yāvatsañjāyate kiñcit sattvaṃ sthāvarajaṅgamam |",
            "kṣetrakṣetrajñasaṃyogāttadviddhi bharatarṣabha",
        ], "|| 26 ||",
           "Whatever being is born, moving or unmoving, know, O best of the Bhāratas, that it arises from the union of the field and the knower of the field.",
           bhashya=[
               {"text": "“kṣetrajñaṃ cāpi māṃ viddhi” (13.2) iti kṣetrajñeśvaraikatvaviṣayaṃ jñānaṃ mokṣasādhanaṃ “yad jñātvā'mṛtamaśnute” (13.12) ityuktam. tat kasmāt hetoḥ iti taddhetupradarśanāya ślokaḥ ārabhyate. yasmāt –", "intro": True},
               "yāvaditi – yāvat yat, kiñcit, sañjāyate samutpadyate, sattvaṃ vastu, kim aviśeṣeṇa? na ityāha – sthāvarajaṅgamam sthāvaraṃ jaṅgamaṃ ca, kṣetrakṣetrajñasaṃyogāt tat jāyate ityevaṃ, viddhi jānīhi, he bharatarṣabha. kaḥ punaḥ ayaṃ kṣetrakṣetrajñayoḥ saṃyogaḥ abhipretaḥ? na tāvat rajjvā iva ghaṭasya avayavasaṃśleṣadvārakaḥ sambandhaviśeṣaḥ saṃyogaḥ kṣetreṇa kṣetrajñasya sambhavati, ākāśavat niravayavatvāt. nāpi samavāyalakṣaṇaḥ tantupaṭayoriva kṣetrakṣetrajñayoḥ itaretara kāryakāraṇabhāvānabhyupagamāt iti. ucyate – kṣetrakṣetrajñayoḥ viṣayaviṣayiṇoḥ bhinnasvabhāvayoḥ itaretarataddharmādhyāsalakṣaṇaḥ saṃyogaḥ kṣetrakṣetrajñasvarūpavivekābhāvanibandhanaḥ, rajjuśuktikādīnāṃ tadvivekajñānābhāvāt adhyāropitasarparajatādi saṃyogavat. saḥ ayaṃ adhyāsasvarūpaḥ kṣetrakṣetrajñayoḥ saṃyogaḥ mithyājñānalakṣaṇaḥ. yathāśāstraṃ kṣetrakṣetrajña lakṣaṇabheda parijñānapūrvakaṃ prāk darśitarūpāt kṣetrāt, muñjādiva iṣīkāṃ, yathoktalakṣaṇaṃ kṣetrajñaṃ pravibhajya “na sattannāsaducyate (13.12) ityanena nirastasarvopādhiviśeṣaṃ jñeyaṃ brahmasvarūpeṇa yaḥ paśyati, kṣetraṃ ca māyānirmitahasti (harmyādivat) svapnadṛṣṭavastu (vat) gandharvanagarādivat “asadeva sadiva avabhāsate” iti evaṃ niścitavijñānaḥ yaḥ, tasya yathoktasamyagdarśanavirodhāt apagacchati mithyājñānam. tasya janmahetoḥ apagamāt “ya evaṃ vetti puruṣaṃ prakṛtiṃ ca guṇaiḥ saha” (13.23) ityanena “vidvān bhūyaḥ na abhijāyate” iti yat uktaṃ tat upapannaṃ uktam.",
           ]),
        _v([
            "samaṃ sarveṣu bhūteṣu tiṣṭhantaṃ parameśvaram |",
            "vinaśyatsvavinaśyantaṃ yaḥ paśyati sa paśyati",
        ], "|| 27 ||",
           "He who sees the supreme Lord abiding alike in all beings, not perishing when they perish — he sees.",
           bhashya=[
               {"text": "“na sa bhūyo'bhijāyate” (13.23) iti samyagdarśanaphalam avidyādisaṃsārabīja nivṛttidvāreṇa janmābhāvaḥ uktaḥ. janmakāraṇaṃ ca avidyānimittakaḥ kṣetrakṣetrajñasaṃyogaḥ uktaḥ. ataḥ tasyāḥ avidyāyāḥ nivartakaṃ samyagdarśanam uktam api punaḥ śabdāntareṇa ucyate –", "intro": True},
               "samamiti – samaṃ nirviśeṣaṃ, tiṣṭhantaṃ sthitiṃ kurvantaṃ, kva? sarveṣu samasteṣu bhūteṣu brahmādisthāvarānteṣu prāṇiṣu, kam? parameśvaraṃ, dehendriya manobuddhyavyaktātmanaḥ apekṣya parameśvaraḥ taṃ sarveṣu bhūteṣu samaṃ tiṣṭhantam. tāni viśinaṣṭi “vinaśyatsu” iti, taṃ ca parameśvaram “avinaśyantam” iti, bhūtānāṃ parameśvarasya ca atyantavailakṣaṇyapradarśanārtham. katham? sarveṣāṃ hi bhāvivikārāṇāṃ janilakṣaṇaḥ bhāvavikāraḥ mūlam, janmottarakālabhāvinaḥ anye sarve bhāvavikārāḥ vināśāntāḥnu vināśāt paraḥ na kaścit asti bhāvavikāraḥ, bhāvābhāvāt. sati hi dharmiṇi dharmāḥ bhavanti. ataḥ antyabhāva vikārābhāvānuvādena tat pūrvabhāvinaḥ sarve bhāvavikārāḥ pratiṣiddhāḥ bhavanti saha kāryaiḥ. tasmāt sarvabhūtavailakṣaṇyam, atyantameva parameśvarasya siddhaṃ, nirviśeṣatvam, ekatvaṃ ca. yaḥ evaṃ yathoktaṃ parameśvaraṃ paśyati, saḥ paśyati.",
               "nanu sarvo'pi lokaḥ paśyati, kiṃ viśeṣaṇena iti? satyam paśyatinu kiṃ tu viparītaṃ paśyati. ataḥ viśinaṣṭi – sa eva paśyatīti. yathā timiradoṣadṛṣṭiḥ anekaṃ candraṃ paśyati tamapekṣya ekacandradarśī viśiṣyate – sa eva paśyatītinu tathaiva ihāpi ekam avibhaktaṃ yathoktam ātmānaṃ yaḥ paśyati, saḥ vibhaktānekātmaviparītadarśibhyaḥ viśiṣyate – sa eva paśyatīti. itare paśyantaḥ api na paśyanti, viparītadarśitvāt – anekacandradarśivat ityarthaḥ",
           ]),
        _v([
            "samaṃ paśyan hi sarvatra samavasthitamīśvaram |",
            "na hinastyātmanā''tmānaṃ tato yāti parāṃ gatim",
        ], "|| 28 ||",
           "For, seeing the Lord established alike everywhere, he does not harm the Self by the self, and so he goes to the highest goal.",
           bhashya=[
               {"text": "yathoktasya samyagdarśanasya phalavacanena stutiḥ kartavyā, iti ślokaḥ ārabhyate –", "intro": True},
               "samamiti – samaṃ paśyan upalabhamānaḥ yasmāt sarvatra sarvabhūteṣu, samavasthitaṃ tulyatayā avasthitam īśvaram atītānantaraślokoktalakṣaṇamityarthaḥ. samaṃ paśyan. kim? na hinasti hiṃsāṃ na karoti ātmanā svenaiva svam ātmānam. tataḥ tadahiṃsanāt yāti parāṃ prakṛṣṭāṃ gatim mokṣākhyām. nanu naiva kaścit prāṇī svayaṃ svam ātmānaṃ hinasti, katham ucyate aprāptaṃ “na hinasti” iti? yathā “na pṛthivyām nāntarikṣe na divyagniḥ cetavyaḥ” (tai.saṃ. 5.2.7.1) ityādi. naiṣa doṣaḥ. ajñānām ātmatiraskaraṇopapatteḥ. sarvo hi ajñaḥ atyantaprasiddhaṃ sākṣāt aparokṣam ātmānaṃ tiraskṛtya anātmānam ātmatvena parigṛhya, tamapi dharmādharmau kṛtvā upāttam ātmānaṃ hatvā anyam ātmānam upādatte navam, taṃ caiva hatvā anyam, evaṃ tamapi hatvā anyam. ityevam upāttamupāttam ātmānaṃ hantīti ātmahā sarvaḥ ajñaḥ. yastu paramārthātmā, asāvapi sarvadā avidyayā hata iva, vidyamānaphalābhāvāt, iti sarve eva ātmahanaḥ eva avidvāṃsaḥ. yastu itaraḥ yathoktātmadarśī saḥ ubhaya'thāpi ātmanā ātmānaṃ na hinasti na hanti. tataḥ yāti parāṃ gatiṃ, yathoktaṃ phalaṃ tasya bhavatītyarthaḥ.",
           ]),
        _v([
            "prakṛtyaiva ca karmāṇi kriyamāṇāni sarvaśaḥ |",
            "yaḥ paśyati tathā''tmānamakartāraṃ sa paśyati",
        ], "|| 29 ||",
           "He who sees that all actions are done by prakṛti alone, and that the Self is not the doer — he sees.",
           bhashya=[
               {"text": "sarvabhūtastham īśaṃ samaṃ paśyan na hinasti ātmanā ātmānam ityuktam, tadanupapannaṃ, svaguṇakarmavailakṣaṇyabhedabhinneṣu ātmasu, ityetat āśaṅkya āha –", "intro": True},
               "prakṛtyā iti – prakṛtiḥ bhagavataḥ māyā triguṇātmikā, “māyāṃ tu prakṛtiṃ vidyāt” (śve.u.4.10) iti mantravarṇāt. tayā prakṛtyaiva na anyena, mahadādi kāryakaraṇākārapariṇatayā karmāṇi vāṅmanaḥkāyārabhyāṇi, kriyamāṇāni nirvartyamānāni, sarvaśaḥ sarvaprakāraiḥ yaḥ paśyati upalabhate, tathā ātmānaṃ kṣetrajñam, akartāraṃ sarvopādhivivarjitaṃ, sa paśyati saḥ paramārthadarśī ityabhiprāyaḥ nirguṇasya akartuḥ nirviśeṣasya ākāśasyeva bhede pramāṇānupapattiḥ ityarthaḥ.",
           ]),
        _v([
            "yadā bhūtapṛthagbhāvamekasthamanupaśyati |",
            "tata eva ca vistāraṃ brahma sampadyate tadā",
        ], "|| 30 ||",
           "When he sees the separate existence of beings as resting in the One, and their expansion from it alone, then he attains Brahman.",
           bhashya=[
               {"text": "punarapi tadeva samyagdarśanaṃ śabdāntareṇa prapañcayati –", "intro": True},
               "yadā iti – yadā yasminkāle, bhūtapṛthagbhāvam bhūtānāṃ pṛthagbhāvaṃ pṛthaktvam, ekasmin ātmani sthitam ekastham anupaśyati, śāstrocāryopadeśam anu ātmānaṃ pratyakṣatvena paśyati “ātmaivedaṃ sarvam” (bṛ.u.2.4.6) iti, tataḥ eva ca tasmādeva ca vistāram utpattiṃ vikāsam – “ātmataḥ prāṇaḥ, ātmataḥ āśā, ātmataḥ smaraḥ, ātmataḥ ākāśaḥ ātmataḥ tejaḥ ātmataḥ āpaḥ ātmataḥ āvirbhāvatirobhāvau, ātmataḥ annam” (chāṃ.u.7.26.1) ityevamādiprakāraiḥ vistāraṃ yadā paśyati, brahma sampadyate brahmaiva bhavati tadā tasmin kāle ityarthaḥ.",
           ]),
        _v([
            "anāditvānnirguṇatvātparamātmā'yamavyayaḥ |",
            "śarīrastho'pi kaunteya na karoti na lipyate",
        ], "|| 31 ||",
           "Being beginningless and without guṇas, this imperishable supreme Self, son of Kuntī, neither acts nor is tainted, though dwelling in the body.",
           bhashya=[
               {"text": "ekasya ātmanaḥ sarvadehātmatve taddoṣasambandhe prāpte idam ucyate –", "intro": True},
               "anāditvāt iti – anāditvāt – anādeḥ bhāvaḥ anāditvam, ādiḥ kāraṇam, tat yasya nāsti tat anādi. yat hi ādimat tat svena ātmanā vyetinu ayaṃ tu anāditvāt niravayavaḥ iti kṛtvā na vyeti. tathā nirguṇatvāt. saguṇo hi guṇavyayāt vyeti, ayaṃ tu nirguṇatvāt na vyetinu iti paramātmā ayam avyayaḥ, na asya vyayaḥ vidyate ityavyayaḥ. yataḥ evam ataḥ śarīrastho'pi, śarīreṣu ātmanaḥ upalabdhiḥ bhavatīti śarīrasthaḥ ucyate. tathāpi na karoti karma. tadakaraṇādeva tatphalena na lipyate. yaḥ hi kartā saḥ karmaphalena lipyate. ayaṃ tu akartā, ataḥ na phalena lipyate ityarthaḥ. kaḥ punaḥ deheṣu karoti lipyate ca? yadi tāvat anyaḥ paramātmanaḥ dehī karoti lipyate ca, tataḥ idam anupapannam uktaṃ kṣetrajñeśvaraikatvaṃ “kṣetrajñaṃ cāpi māṃ viddhi” (13.2) ityādi. atha nāsti īśvarāt anyaḥ dehī, kaḥ karoti kaḥ lipyate ca iti vācyam. paro vā nāstīti. sarvathā durvijñeyaṃ durvācyaṃ ceti bhagavatproktaṃ aupaniṣadaṃ darśanaṃ parityaktaṃ vaiśeṣikaiḥ sāṅkhyārhatabauddhaiśca.",
               "tatrāyaṃ parihāraḥ bhagavatā svenaiva uktaḥ “svabhāvastu pravartate” (5.14) iti. avidyāmātrasvabhāvo hi karoti lipyate iti vyavahāraḥ bhavati, na tu paramārthataḥ eva tasmin paramātmani tat asti. ataḥ eva etasmin paramārthasāṅkhyadarśane sthitānāṃ jñānaniṣṭhānāṃ paramahaṃsaparivrājakānāṃ tiraskṛtāvidyāvyavahārāṇāṃ karmādhikāraḥ nāsti iti tatra tatra darśitaṃ bhagavatā.",
           ]),
        _v([
            "yathā sarvagataṃ saukṣmyādākāśaṃ nopalipyate |",
            "sarvatrāvasthito dehe tathā''tmā nopalipyate",
        ], "|| 32 ||",
           "As all-pervading space is not tainted, because of its subtlety, so the Self, abiding everywhere in the body, is not tainted.",
           bhashya=[
               {"text": "kimiva na karoti na lipyate ityatra dṛṣṭāntam āha –", "intro": True},
               "yathā iti – yathā sarvagataṃ sarvavyāpyapi sat, saukṣmyāt sūkṣmabhāvāt, ākāśaṃ khaṃ, na upalipyate na sambadhyate, sarvatra avasthitaḥ dehe tathā ātmā na upalipyate. kiṃ ca –",
           ]),
        _v([
            "yathā prakāśayatyekaḥ kṛtsnaṃ lokamimaṃ raviḥ |",
            "kṣetraṃ kṣetrī tathā kṛtsnaṃ prakāśayati bhārata",
        ], "|| 33 ||",
           "As the one sun illumines this whole world, so the lord of the field illumines the whole field, O Bhārata.",
           bhashya=[
               "yathā iti – yathā, prakāśayati avabhāsayati, ekaḥ kṛtsnaṃ lokam imaṃ raviḥ savitā ādityaḥ, tathā tadvat, avyaktamahābhūtādi dhṛtyantaṃ kṣetraṃ ekaḥ san prakāśayati, kaḥ? kṣetrī, paramātmā ityarthaḥ, bhārata! ravidṛṣṭāntaḥ atra ātmanaḥ ubhayārthaḥ api bhavati, ravivat sarvakṣetreṣu ekaḥ eva ātmā alepakaśca iti.",
           ]),
        _v([
            "kṣetrakṣetrajñayorevamantaraṃ jñānacakṣuṣā |",
            "bhūtaprakṛtimokṣaṃ ca ye viduryānti te param",
        ], "|| 34 ||",
           "Those who know, with the eye of knowledge, the distinction between the field and the knower of the field, and the release of beings from prakṛti, go to the Supreme.",
           bhashya=[
               {"text": "samastādhyāyopasaṃhārārthaḥ ayaṃ ślokaḥ –", "intro": True},
               "kṣetrakṣetrayoḥ iti – kṣetrakṣetrajñayoḥ yathāvyākhyātayoḥ, evaṃ yathāpradarśitaprakāreṇa, antaram itaretaravailakṣaṇyaviśeṣaṃ, jñānacakṣuṣā śāstrācāryaprasādopadeśajanitam ātmapratyayikaṃ jñānaṃ cakṣuḥ, tena jñānacakṣuṣā, bhūtaprakṛtimokṣaṃ ca – bhūtānāṃ prakṛtiḥ avidyālakṣaṇā avyaktākhyā tasyāḥ bhūtaprakṛteḥ mokṣaṇam abhāvagamanaṃ ca, ye viduḥ jānanti, yānti gacchanti, te, paraṃ paramārthatattvaṃ brahma, na punaḥ deham ādadate ityarthaḥ.",
           ]),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsu upaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjunasaṃvāde kṣetrakṣetrajñayogo nāma trayodaśo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the thirteenth chapter, Kṣetrakṣetrajñavibhāga Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣyaśrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye kṣetrakṣetrajñayogo nāma trayodaśo'dhyāyaḥ", "gloss": "Thus ends the thirteenth chapter, Kṣetrakṣetrajñavibhāga Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
