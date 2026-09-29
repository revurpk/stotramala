# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 11 (Viśvarūpadarśana Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 11 · Viśvarūpadarśana Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 11",
    "h1": "Bhagavad Gītā · Chapter 11",
    "subtitle": "Viśvarūpadarśana Yoga · the vision of the cosmic form · with Śaṅkara's bhāṣya",
    "note": "Given divine sight, Arjuna beholds the cosmic form: the universe gathered in one body, then Time devouring the warriors. Terrified, he praises and begs forgiveness, and Kṛṣṇa returns to his gentle human form, declaring that only undivided devotion can see him so.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 10', 'gita-bhashya-10-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 12 ›', 'gita-bhashya-12-iast.html')],
    "sections": [
        {"speaker": "arjuna uvāca"},
        _v([
            "madanugrahāya paramaṃ guhyamadhyātmasañjñitam |",
            "yattvayoktaṃ vacastena moho'yaṃ vigato mama",
        ], "|| 1 ||",
           "Arjuna said: Out of grace to me you have spoken the supreme secret called the inner Self, and by those words this delusion of mine is gone.",
           bhashya=[
               {"text": "bhagavataḥ vibhūtayaḥ uktāḥ. tatra ca “viṣṭabhyāhamidaṃ kṛtsnamekāṃśena sthito jagat” (10.42) iti bhagavatā abhihitaṃ śrutvā yat jagat ātmarūpam ādyam aiśvaryaṃ tatsākṣātkartumicchan –", "intro": True},
               "madanugrahāya mama anugrahārthaṃ, paramaṃ niratiśayaṃ, guhyaṃ gopyam adhyātma sañjñitam ātmānātma vivekaviṣayaṃ yat tvayā uktaṃ vacaḥ vākyaṃ, tena te vacasā mohaḥ ayaṃ vigataḥ mama avivekabuddhiḥ apagatā ityarthaḥ. kiñca",
           ]),
        _v([
            "bhavāpyayau hi bhūtānāṃ śrutau vistaraśo mayā |",
            "tvattaḥ kamalapatrākṣa māhātmyamapi cāvyayam",
        ], "|| 2 ||",
           "For I have heard from you at length of the origin and dissolution of beings, O lotus-eyed one, and of your imperishable greatness.",
           bhashya=[
               "udbhavaḥ – utpatti, apyayaḥ pralayo tau bhavāpyayau hi bhūtānāṃ śṛte vistaraśaḥ na saṅkṣepataḥ mayā tvattaḥ tvatsakāśāt kamalapratākṣa. kamalasya patraṃ kamalapatraṃ tadvat akṣiṇī yasya tava sa tvaṃ kamalapratākṣaḥ, me kamalapatrākṣa mahātmanaḥ bhāvaḥ mahātmyamapi ca avyayaṃ akṣayaṃ “śṛtaṃ” iti anuvartate.",
           ]),
        _v([
            "evametadyathā'ttha tvamātmānaṃ parameśvara |",
            "draṣṭumicchāmi te rūpamaiśvaraṃ puruṣottama",
        ], "|| 3 ||",
           "As you have declared yourself to be, O supreme Lord, so it is. Yet I wish to see your sovereign form, O supreme Person.",
           bhashya=[
               "evamiti – evam etat, na anyathā,yathā yena prakāreṇa, āttha kathayasi, tvam ātmānaṃ parameśvara, tathāpi draṣṭum icchāmi, te tava, jñānaiśvarya balaśaktivīrya tejobhiḥ sampannam, aiśvaraṃ vaiṣṇavaṃ rūpaṃ puruṣottama.",
           ]),
        _v([
            "manyase yadi tacchakyaṃ mayā draṣṭumiti prabho |",
            "yogeśvara tato me tvaṃ darśayātmānamavyayam",
        ], "|| 4 ||",
           "If you think it possible for me to see it, Lord, master of yoga, then show me your imperishable Self.",
           bhashya=[
               "manyase cintayasi yadi mayā arjunena tat śakyaṃ draṣṭuṃ iti prabho! svāmin! yogino yogāḥ, teṣāṃ īśvaraḥ yogeśvaraḥ, he yogeśvara, yasmāt ahaṃ atīva arthī draṣṭuṃ, tataḥ tasmāt me madarthaṃ darśaya. tvaṃ ātmānaṃ avyayam.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "paśya me pārtha rūpāṇi śataśo'tha sahasraśaḥ |",
            "nānāvidhāni divyāni nānāvarṇākṛtīni ca",
        ], "|| 5 ||",
           "The Blessed Lord said: Behold, Pārtha, my forms by hundreds and thousands, various and divine, of many colours and shapes.",
           bhashya=[
               {"text": "evaṃ coditaḥ arjunena –", "intro": True},
               "paśya iti. paśya me pārtha! rūpāṇi śataśaḥ atha sahasraśaḥ, anekaśaḥ ityarthaḥ. tāni ca nānāvidhāni, divi bhavāni divyāni aprākṛtāni, nānāvarṇākṛtīni ca nānā vilakṣaṇāḥ nīlapītādiprakārāḥ varṇāḥ tathā ākṛtayaśca avayavasaṃsthāviśeṣāḥ yeṣāṃ rūpāṇāṃ tāni nānāvarṇākṛtīni ca.",
           ]),
        _v([
            "paśyādityān vasūn rudrānaśvinau marutastathā |",
            "bahūnyadṛṣṭapūrvāṇi paśyāścaryāṇi bhārata",
        ], "|| 6 ||",
           "Behold the Ādityas, the Vasus, the Rudras, the two Aśvins and the Maruts; behold many wonders never seen before, O Bhārata.",
           bhashya=[
               "paśyādityāniti – paśya ādityān dvādaśa, vasūn aṣṭau, rudrān ekādaśa, aśvinau dvau, marutaḥ sapta saptagaṇāḥ ye tān, tathā, bahūni anyānyapi adṛṣṭapūrvāṇi manuṣyaloke tvayā tvattaḥ anyena vā kenacit, paśya āścaryāṇi adbhutāni bhārata. na kevalaṃ etāvadeva –",
           ]),
        _v([
            "ihaikasthaṃ jagat kṛtsnaṃ paśyādya sacarācaram |",
            "mama dehe guḍākeśa yaccānyaddraṣṭumicchasi",
        ], "|| 7 ||",
           "Behold here today the whole universe, moving and unmoving, gathered as one in my body, Guḍākeśa, and whatever else you wish to see.",
           bhashya=[
               "iha ekastham ekasmin sthitaṃ jagat, kṛtsnaṃ samastaṃ, paśya, adya, idānīṃ sacarācaraṃ saha careṇa acareṇa ca vartate, mama dehe, guḍākeśa, yat ca anyat jayaparājayādi yat śaṅkase “yadvā jayema yadi vā no jayeyuḥ” (2.6) iti yat avocaḥ tadapi draṣṭuṃ yadi icchasi. kintu –",
           ]),
        _v([
            "na tu māṃ śakyase draṣṭumanenaiva svacakṣuṣā |",
            "divyaṃ dadāmi te cakṣuḥ paśya me yogamaiśvaram",
        ], "|| 8 ||",
           "But you cannot see me with this eye of yours. I give you a divine eye: behold my sovereign yoga!",
           bhashya=[
               "na tu, māṃ viśvarūpadharaṃ, śakyase draṣṭum anenaiva prākṛtena svacakṣuṣā, svakīyena cakṣuṣā. yena tu śakyase draṣṭuṃ divyena, tat divyaṃ dadāmi, te tubhyam cakṣuḥ. tena paśya me yogam aiśvaram īśvarasya mama aiśvaraṃ yogaṃ, yogaśaktyatiśayam ityarthaḥ.",
           ]),
        {"speaker": "sañjaya uvāca"},
        _v([
            "evamuktvā tato rājan mahāyogeśvaro hariḥ |",
            "darśayāmāsa pārthāya paramaṃ rūpamaiśvaram",
        ], "|| 9 ||",
           "Sañjaya said: Having spoken thus, O king, Hari, the great lord of yoga, then showed Pārtha his supreme sovereign form —",
           bhashya=[
               "evaṃ yathokta prakāreṇa, uktvā tataḥ anantaraṃ rājan dhṛtarāṣṭra, mahāyogeśvaraḥ mahāṃścāsau yogeśvaraśca, mahāyogeśvaraḥ hariḥ nārāyaṇaḥ darśayāmāsa darśitavān, pārthāya pṛthāsutāya, paramaṃ rūpaṃ viśvarūpam aiśvaram.",
           ]),
        _v([
            "anekavaktranayanamanekādbhutadarśanam |",
            "anekadivyābharaṇaṃ divyānekodyatāyudham",
        ], "|| 10 ||",
           "with many mouths and eyes, many wondrous sights, many divine ornaments, many divine weapons raised;",
           bhashya=[
               "aneketi – anekavaktranayanam – anekāni vaktrāṇi nayanāni ca yasmin rūpe tat aneka vaktranayanam. anekādbhutadarśanam – anekāni adbhutāni vismāpakāni darśanāni yasmin rūpe tat anekādbhutadarśanaṃ, tathā anekadivyābharaṇam – anekāni divyāni ābharaṇāni yasmin tat aneka divyābharaṇam, tathā divyānekodyatāyudham divyāni anekāni asyādīni udyatāni āyudhāni yasmin tat divyānekodyatāyudhaṃ, “darśayāmāseti” pūrveṇa sambandhaḥ. kiñca –",
           ]),
        _v([
            "divyamālyāmbaradharaṃ divyagandhānulepanam |",
            "sarvāścaryamayaṃ devamanantaṃ viśvatomukham",
        ], "|| 11 ||",
           "wearing divine garlands and garments, anointed with divine perfumes, all-wonderful, resplendent, infinite, facing every way.",
           bhashya=[
               "divyamālyāmbaradharam divyāni mālyāni puṣpāṇi ambarāṇi vastrāṇi ca dhriyante yena īśvareṇa taṃ divyamālyāmbaradharaṃ, divyagandhānulepam – divyaṃ gandhānulepanaṃ yasya taṃ divyagandhānulepanaṃ, sarvāścaryamayaṃ sarvāścaryaprāyam, devaṃ anantaṃ na asya antaḥ asti iti anantaḥ taṃ, viśvatomukhaṃ sarvatomukhaṃ sarvabhūtātmabhūtatvāt, “taṃ darśayāmāsa”, “arjunaḥ dadarśa” iti vā adhyāhriyate.",
           ]),
        _v([
            "divi sūryasahasrasya bhavedyugapadutthitā |",
            "yadi bhāḥ sadṛśī sā syādbhāsastasya mahātmanaḥ",
        ], "|| 12 ||",
           "If the light of a thousand suns were to blaze forth at once in the sky, it might resemble the splendour of that great being.",
           bhashya=[
               {"text": "yā punaḥ bhagavataḥ viśvarūpasya bhāḥ tasyāḥ upamā ucyate –", "intro": True},
               "divi antarikṣe, tṛtīyasyāṃ vā divi, sūryāṇāṃ sahasraṃ sūryasahasraṃ, tasya yugapat utthitasya sūryasahasrasya yā yugapat utthitā bhāḥ sā yadi, sadṛśī syāt tasya mahātmanaḥ viśvarūpasyaiva bhāsaḥ, yadi vā na syāt, tato'pi viśvarūpasyaiva bhāḥ atiricyate ityabhiprāyaḥ. kiñca",
           ]),
        _v([
            "tatraikasthaṃ jagatkṛtsnaṃ pravibhaktamanekadhā |",
            "apaśyaddevadevasya śarīre pāṇḍavastadā",
        ], "|| 13 ||",
           "There the son of Pāṇḍu saw the whole universe, divided in many ways, gathered as one in the body of the God of gods.",
           bhashya=[
               "tatra tasmin viśvarūpe, ekasmin sthitam ekasthaṃ jagat kṛtsnaṃ pravibhaktam anekadhā devapitṛmanuṣyādibhedaiḥ, apaśyat dṛṣṭavān, devadevasya hareḥ, śarīre, pāṇḍavaḥ arjunaḥ tadā.",
           ]),
        _v([
            "tataḥ sa vismayāviṣṭo hṛṣṭaromā dhanañjayaḥ |",
            "praṇamya śirasā devaṃ kṛtāñjalirabhāṣata",
        ], "|| 14 ||",
           "Then Dhanañjaya, filled with wonder, his hair standing on end, bowed his head to the God and spoke with joined palms.",
           bhashya=[
               "tata iti – tataḥ taṃ dṛṣṭvā saḥ vismayena āviṣṭaḥ vismayāviṣṭaḥ, hṛṣṭāni romāṇi yasya saḥ ayaṃ hṛṣṭaromā ca abhavat dhanañjayaḥ. praṇamya prakarṣeṇa namanaṃ kṛtvā prahvībhūtaḥ san śirasā, devaṃ viśvarūpadharaṃ, kṛtāñjaliḥ namaskārārthaṃ sampuṭīkṛtahastaḥ san abhāṣata uktavān.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "paśyāmi devāṃstava deva dehe sarvāṃstathā bhūtaviśeṣasaṅghān |",
            "brahmāṇamīśaṃ kamalāsanasthaṃ ṛṣīṃśca sarvānuragāṃśca divyān",
        ], "|| 15 ||",
           "Arjuna said: I see in your body, O God, all the gods and the hosts of different beings — Brahmā the lord seated on the lotus, all the seers and the divine serpents.",
           bhashya=[
               {"text": "katham. yattvayā darśitaṃ viśvarūpaṃ tadahaṃ paśyāmi iti svānubhavam āviṣkurvan –", "intro": True},
               "paśyāmi upalabhe, he deva, tava dehe, devān sarvān tathā bhūtaviśeṣasaṅghān – bhūta viśeṣāṇāṃ sthāvarajaṅgamānāṃ nānāsaṃsthānaviśeṣāṇāṃ saṅghāḥ bhūtaviśeṣasaṅghāḥ tān, kiñca brahmāṇaṃ caturmukham īśaṃ īśitāraṃ prajānāṃ, kamalāsanasthaṃ pṛthivīpadmamadhye merukarṇikāsanastham ityarthaḥ. ṛṣīn ca vaśiṣṭhādīn, sarvān uragān ca vāsuki prabhṛtīn, divyān divi bhavān.",
           ]),
        _v([
            "anekabāhūdaravaktranetraṃ paśyāmi tvāṃ sarvato'nantarūpam |",
            "nāntaṃ na madhyaṃ na punastavādiṃ paśyāmi viśveśvara viśvarūpa",
        ], "|| 16 ||",
           "I see you with countless arms, bellies, mouths and eyes, of infinite form on every side; I see no end, no middle and no beginning of you, O lord of the universe, O universal form.",
           bhashya=[
               "aneka bāhūdaravaktranetram – aneka bāhavaḥ udarāṇi vaktrāṇi netrāṇi ca yasya tava saḥ tvaṃ anekabāhūdaravaktranetraḥ, tam anekabāhūdaravaktranetraṃ. paśyāmi tvāṃ sarvataḥ sarvatra, anantarūpam anantāni rūpāṇi asya iti anantarūpaḥ, taṃ anantarūpaṃ. na antaḥ, avasānaṃ, na madhyaṃ, madhyaṃ nāma dvayoḥ koṭyoḥ antaraṃ, na punaḥ tava ādiṃ, tava devasya na antaṃ paśyāmi, na madhyaṃ paśyāmi na punaḥ ādiṃ paśyāmi, he viśveśvara, he viśvarūpa. kiñca",
           ]),
        _v([
            "kirīṭinaṃ gadinaṃ cakriṇaṃ ca tejorāśiṃ sarvatodīptimantam |",
            "paśyāmi tvāṃ durnirīkṣyaṃ samantāddīptānalārkadyutimaprameyam",
        ], "|| 17 ||",
           "I see you with crown, mace and discus, a mass of radiance shining everywhere, hard to look upon, blazing all around like fire and sun, immeasurable.",
           bhashya=[
               "kirīṭaṃ nāma śirobhūṣaṇa viśeṣaḥ, tat yasya asti saḥ kirīṭī taṃ kirīṭinaṃ, tathā gadinaṃ gadā asya vidyate iti gadī taṃ gadinaṃ, tathā cakriṇam cakram asya astīti cakrī, taṃ cakriṇam, tejorāśiṃ tejaḥ puñjaṃ. sarvatodīptimantaṃ sarvataḥ dīptiḥ asya asti saḥ sarvatodīptimān taṃ sarvatodīptimantaṃ, paśyāmi tvāṃ, durnirīkṣyam duḥkhena nirīkṣyaḥ durnirīkṣyaḥ, taṃ durnirīkṣyaṃ, samantāt samantataḥ, dīptānalkāradyutiṃ analaśca arkaśca analārkau tayoḥ dīptānalārkayoḥ dyutiḥ iva dyutiḥ tejaḥ yasya tava sa tvaṃ dīptānalārka dyutiḥ, taṃ dīptānalārkadyutim, aprameyaṃ na prameyam aprameyaṃ, aśakyaparicchedam ityarthaḥ.",
           ]),
        _v([
            "tvamakṣaraṃ paramaṃ veditavyaṃ tvamasya viśvasya paraṃ nidhānam |",
            "tvamavyayaḥ śāśvatadharmagoptā sanātanastvaṃ puruṣo mato me",
        ], "|| 18 ||",
           "You are the Imperishable, the supreme one to be known; you are the ultimate resting-place of this universe; you are the undying guardian of eternal dharma; you are, I hold, the primeval Person.",
           bhashya=[
               {"text": "ita eva te yogaśaktidarśanāt anuminomi –", "intro": True},
               "tvam, akṣaram – na kṣaratīti, akṣaraṃ paramaṃ brahma, veditavyaṃ jñātavyaṃ mumukṣubhiḥ. tvam asya viśvasya samastasya jagataḥ parama prakṛṣṭaṃ nidhānaṃ – nidhīyate asmin iti nidhānam, paraḥ āśrayaḥ ityarthaḥ. kiṃ ca tvam avyayaḥ. na tava vyayaḥ vidyate iti avyayaḥ. śāśvata dharmagoptā – śaśvat bhavaḥ śāśvataḥ, nityaḥ dharmaḥ, tasya goptā śāśvatadharmagoptā, sanātanaḥ cirantanaḥ tvaṃ puruṣaḥ paramaḥ mataḥ abhipretaḥ me mama. kiñca",
           ]),
        _v([
            "anādimadhyāntamanantavīryam anantabāhuṃ śaśisūryanetram |",
            "paśyāmi tvāṃ dīptahutāśavaktraṃ svatejasā viśvamidaṃ tapantam",
        ], "|| 19 ||",
           "I see you without beginning, middle or end, of infinite power, with countless arms, the moon and sun your eyes, your mouth a blazing fire, scorching this universe with your radiance.",
           bhashya=[
               "anādimadhyāntam ādiśca madhyaṃ ca antaśca na vidyate yasya saḥ ayam anādimadhyāntaḥ, tam – tvām anādimadhyāntam, anantavīryam – na tava vīryasya antaḥ asti iti anantavīryaḥ, taṃ tvām anantavīryaṃ, tathā anantabāhum – anantāḥ bāhavaḥ yasya tava saḥ tvam anantabāhuḥ, taṃ tvām anantabāhuṃ śaśisūryanetram – śaśisūryau netre yasya tava saḥ tvaṃ śaśisūryanetraḥ, taṃ tvāṃ śaśisūryanetraṃ, candrādityanayanaṃ paśyāmi tvāṃ, dīptahutāśavaktram – dīptaścāsau hutāśaśca saḥ vaktraṃ yasya tava saḥ tva dīptahutāśavaktraḥ, taṃ tvāṃ dīptahutāśavaktram svatejasā viśvam idaṃ tapantaṃ tāpayantam.",
           ]),
        _v([
            "dyāvāpṛthivyoridamantaraṃ hi vyāptaṃ tvayaikena diśaśca sarvāḥ |",
            "dṛṣṭvā'dbhutaṃ rūpamidaṃ tavograṃ lokatrayaṃ pravyathitaṃ mahātman",
        ], "|| 20 ||",
           "The space between heaven and earth and all the quarters are filled by you alone. Seeing this wondrous, terrible form of yours, great soul, the three worlds tremble.",
           bhashya=[
               "dvāvāpṛthivyoḥ, idam antaraṃ hi antarikṣam vyāptaṃ, tvayā ekena viśvarūpa dhareṇa, diśaḥ ca sarvāḥ vyāptāḥ, dṛṣṭvā upalabhya, adbhutam vismāpakaṃ, rūpam idaṃ, tava, ugraṃ, krūraṃ, lokānāṃ trayaṃ lokatrayaṃ, pravyathitaṃ bhītaṃ, pracalitaṃ vā, mahātman akṣudrasvabhāva",
           ]),
        _v([
            "amī hi tvāṃ surasaṅghā viśanti kecidbhītāḥ prāñjalayo gṛṇanti |",
            "svastītyuktvā maharṣisiddhasaṅghāḥ stuvanti tvāṃ stutibhiḥ puṣkalābhiḥ",
        ], "|| 21 ||",
           "These hosts of gods enter you; some, afraid, praise you with joined palms; hosts of great seers and perfected ones cry 'Hail!' and praise you with abundant hymns.",
           bhashya=[
               {"text": "atha adhunā purā “yadvā jayema yadi vā no jayeyu” (2.6) iti arjunasya yaḥ saṃśayaḥ āsīt, tannirṇayāya pāṇḍavavijayam aikāntikaṃ darśayāmi iti pravṛttaḥ bhagavān. taṃ paśyan āha, kiñca –", "intro": True},
               "amī hi yudhyamānāḥ yoddhāraḥ tvāṃ tvāṃ, surasaṅghāḥ ye atra bhūbhārāvatārāya avatīrṇāḥ vasvādidevasaṅghāḥ manuṣyasaṃsthānāḥ tvāṃ viśanti praviśantaḥ dṛśyante, tatra kecid bhītāḥ prājñalayaḥ santaḥ, gṛṇanti stuvanti tvām, anye palāyanepyaśaktāḥ santaḥ. yuddhe pratyupasthite utpātādinimittānyupalakṣya svastyastu jagataḥ ityuktvā, maharṣisidda saṅghāḥ, maharṣīṇāṃ siddhānāṃ ca saṅghāḥ stuvanti tvāṃ stutibhiḥ, puṣkalābhiḥ sampūrṇābhiḥ.",
           ]),
        _v([
            "rudrādityā vasavo ye ca sādhyā viśve'śvinau marutaścoṣmapāśca |",
            "gandharvayakṣāsurasiddhasaṅghā vīkṣante tvāṃ vismitāścaiva sarve",
        ], "|| 22 ||",
           "The Rudras, Ādityas, Vasus and Sādhyas, the Viśvedevas, the two Aśvins, the Maruts and the ancestors, the hosts of gandharvas, yakṣas, demons and the perfected — all gaze at you in amazement.",
           bhashya=[
               "rudrādityāḥ vasavaḥ ye ca sādhyāḥ – rudrādayaḥ gaṇāḥ viśve, aśvinau ca devau, marutaśca, ūṣmapāśca pitaraḥ, gandharvayakṣāsura siddhasaṅghāḥ – gandharvāḥ hāhāhūhū prabhṛtayaḥ, yakṣāḥ, kuberaprabhṛtayaḥ, asurāḥ virocanaprabhṛtayaḥ, siddhāḥ kapilādayaḥ teṣāṃ saṅghāḥ gandharvayakṣāsurasiddhasaṅghāḥ te, vīkṣante paśyanti, tvā tvāṃ, vismitāḥ vismayam āpannāḥ santaḥ ta eva sarve. yasmācca –",
           ]),
        _v([
            "rūpaṃ mahatte bahuvaktranetraṃ mahābāho bahubāhūrupādam |",
            "bahūdaraṃ bahudaṃṣṭrākarālaṃ dṛṣṭvā lokāḥ pravyathitāstathā'ham",
        ], "|| 23 ||",
           "Seeing your great form, mighty-armed one, with many mouths and eyes, many arms, thighs and feet, many bellies, terrible with many tusks, the worlds tremble, and so do I.",
           bhashya=[
               "rūpaṃ, mahat atipramāṇaṃ, te tava, bahuvaktranetraṃ bahūni vaktrāṇi mukhāni, netrāṇi cakṣūṃṣi ca yasmin rūpe tat bahuvaktranetraṃ, he mahābāho! bahubāhūrupādaṃ – bahavaḥ ūravaḥ pādāḥ ca yasmin tat rūpe bahubāhūrupādaṃ, kiṃ ca, bahūdaraṃ bahūni udarāṇi asmin iti bahūdaraṃ, bahudaṃṣṭrākarālaṃ – bahvībhiḥ daṃṣṭrābhiḥ karālaṃ vikṛtaṃ tat bahudaṃṣṭrākarālaṃ, dṛṣṭvā rūpam īdṛśaṃ lokāḥ laukikāḥ, prāṇinaḥ, pravyathitāḥ pracalitāḥ bhayena, tathā ahamapi. tattredaṃ kāraṇam –",
           ]),
        _v([
            "nabhaḥ spṛśaṃ dīptamanekavarṇaṃ vyāttānanaṃ dīptaviśālanetram |",
            "dṛṣṭvā hi tvāṃ pravyathitāntarātmā dhṛtiṃ na vindāmi śamaṃ ca viṣṇo",
        ], "|| 24 ||",
           "Seeing you touching the sky, blazing, many-coloured, with gaping mouths and huge flaming eyes, my inmost self trembles, and I find neither courage nor peace, O Viṣṇu.",
           bhashya=[
               "nabhaḥ spṛśam dyusparśamityarthaḥ, dīptaṃ prajvalitam, anekavarṇam aneke varṇāḥ bhayaṅkarāḥ nānā saṃsthānāḥ yasmin tvayi taṃ tvām anekavarṇaṃ, vyāttānanaṃ vyāttāni vivṛtāni ānanāni mukhāni yasmin tvayi taṃ tvāṃ vyāttānanaṃ, dīptaviśālanetraṃ dīptāni prajvalitāni viśālāni vistīrṇāni netrāṇi yasmin tvayi taṃ tvāṃ dīptaviśālanetraṃ, dṛṣṭvā hi tvāṃ pravyathitāntarātmā – pravyathitaḥ prabhītaḥ antarātmā manaḥ yasya mama saḥ ahaṃ pravyathitāntarātmā san dhṛtiṃ dhairyaṃ na vindāmi na labhe, śamaṃ ca upaśamaṃ manastuṣṭiṃ he viṣṇo! kasmāt?",
           ]),
        _v([
            "daṃṣṭrākarālāni ca te mukhāni dṛṣṭvaiva kālānalasannibhāni |",
            "diśo na jāne na labhe ca śarma prasīda deveśa jagannivāsa",
        ], "|| 25 ||",
           "Seeing your mouths, terrible with tusks, like the fires of the world's end, I know not the directions and find no refuge. Be gracious, Lord of gods, abode of the universe!",
           bhashya=[
               "daṃṣṭrākarālāni daṃṣṭrābhiḥ karālāni vikṛtāni, te tava, mukhāni, dṛṣṭvā eva upalabhya kālānalasannibhāni pralayakāle lokānāṃ dāhakaḥ agniḥ kālānalaḥ tatsannibhāni kālānalasadṛśāni dṛṣṭvā ityetat diśaḥ pūrvāparavivekena na jāne, dijñmūḍhaḥ jātaḥ asmi, ataḥ na labhe nopalabhe ca śarma sukham, ataḥ prasīda prasannaḥ bhava, he deveśa, jagannivāsa.",
           ]),
        _v([
            "amī ca tvāṃ dhṛtarāṣṭrasya putrāḥ sarve sahaivāvanipālasaṅghaiḥ |",
            "bhīṣmo droṇaḥ sūtaputrastathā'sau sahāsmadīyairapi yodhamukhyaiḥ",
        ], "|| 26 ||",
           "All these sons of Dhṛtarāṣṭra, together with the hosts of kings — Bhīṣma, Droṇa, and that son of the charioteer, with our own chief warriors too —",
           bhashya=[
               {"text": "yebhyaḥ mama parājayaśaṅkā āsīt sā ca apagatā, yataḥ –", "intro": True},
               "amī ca tvāṃ dhṛtarāṣṭrasya putrāḥ duryodhanaprabhṛtayaḥ – “tvaramāṇāḥ tvā viśanti” (27) iti vyavahitena sambandhaḥ sarve sahaiva sahitāḥ avanipālasaṅghaiḥ avaniṃ pṛthvīṃ pālayantīti avanipālāḥ teṣāṃ saṅghaiḥ, kiṃ ca bhīṣmaḥ droṇaḥ, sūtaputraḥ karṇaḥ tathā asau, saha asmadīyairapi dhṛṣṭadyumna prabhṛtibhiḥ yodhamukhyaiḥ yodhānāṃ pradhānaiḥ saha –",
           ]),
        _v([
            "vaktrāṇi te tvaramāṇā viśanti daṃṣṭrākarālāni bhayānakāni |",
            "kecidvilagnā daśanāntareṣu sandṛśyante cūrṇitairuttamāṅgaiḥ",
        ], "|| 27 ||",
           "rush headlong into your terrible mouths with their fearsome tusks; some are seen caught between your teeth, their heads crushed to powder.",
           bhashya=[
               "vaktrāṇi mukhāni, te tava, tvaramāṇāḥ tvarāyuktāḥ santaḥ viśanti – kiṃ viśiṣṭāni mukhāni? daṃṣṭrākarālāni, bhayānakāni bhayaṅkarāṇi, kiṃ ca kecit mukhāni praviṣṭānāṃ madhye vilagnāḥ daśanāntareṣu dantāntareṣu, māṃsamiva bhakṣitaṃ sandṛśyante upalabhyante cūrṇitaiḥ cūrṇīkṛtaiḥ, uttamājñaiḥ śirobhiḥ.",
           ]),
        _v([
            "yathā nadīnāṃ bahavo'mbuvegāḥ samudramevābhimukhā dravanti |",
            "tathā tavāmī naralokavīrā viśanti vaktrāṇyabhivijvalanti",
        ], "|| 28 ||",
           "As the many torrents of rivers rush towards the ocean, so these heroes of the world of men enter your flaming mouths.",
           bhashya=[
               {"text": "kathaṃ praviśanti mukhānītyāha –", "intro": True},
               "yathā iti. yathā nadīnāṃ sravantīnāṃ bahavaḥ aneke ambūnāṃ vegāḥ ambuvegāḥ tvarāviśeṣāḥ samudrameva abhimukhāḥ pratimukhāḥ dravanti praviśanti, tathā tadvat tava amī bhīṣmādayaḥ naralokavīrāḥ manuṣyaloke śūrāḥ viśanti vaktrāṇi abhivijjvalanti prakāśamānāni.",
           ]),
        _v([
            "yathā pradīptaṃ jvalanaṃ pataṅgā viśanti nāśāya samṛddhavegāḥ |",
            "tathaiva nāśāya viśanti lokāstavāpi vaktrāṇi samṛddhavegāḥ",
        ], "|| 29 ||",
           "As moths rush swiftly into a blazing fire to their destruction, so these worlds rush swiftly into your mouths to their destruction.",
           bhashya=[
               {"text": "te kimarthaṃ praviśanti kathaṃ ca ityāha –", "intro": True},
               "yathā pradīptaṃ jvalanam agniṃ pataṅgāḥ pakṣiṇaḥ viśanti, nāśāya vināśāya, samṛddhavegāḥ samṛddhaḥ udbhūtaḥ vegaḥ gatiḥ yeṣāṃ te samṛddhavegāḥ tathaiva nāśāya viśanti, lokāḥ prāṇinaḥ tava api vaktrāṇi samṛddhavegāḥ. tvaṃ punaḥ –",
           ]),
        _v([
            "lelihyase grasamānaḥ samantāllokān samagrān vadanairjvaladbhiḥ |",
            "tejobhirāpūrya jagatsamagraṃ bhāsastavogrāḥ pratapanti viṣṇo",
        ], "|| 30 ||",
           "Devouring all the worlds on every side with your flaming mouths, you lick your lips; your fierce rays fill the whole universe with brilliance and scorch it, O Viṣṇu.",
           bhashya=[
               "lelihyase āsvādayasi, grasamānaḥ antaḥ praveśayan, samantāt samantataḥ lokān, samagrān samastān, vadanaiḥ, vaktraiḥ, jvaladbhiḥ dīpyamānaiḥ tejobhiḥ āpūrva sampūrya, jagat samagraṃ samastam ityetat. kiṃ ca bhāsaḥ dīptayaḥ tava ugrāḥ krūrāḥ pratapanti santāpaṃ kurvanti, he! viṣṇo! vyāpanaśīla.",
           ]),
        _v([
            "ākhyāhi me ko bhavānugrarūpo namo'stu te devavara prasīda |",
            "vijñātumicchāmi bhavantamādyaṃ na hi prajānāmi tava pravṛttim",
        ], "|| 31 ||",
           "Tell me who you are, of such terrible form. Salutation to you, O best of gods; be gracious! I wish to know you, the primal one, for I do not understand what you are doing.",
           bhashya=[
               {"text": "yataḥ evam ugrasvabhāvaḥ ataḥ –", "intro": True},
               "ākhyāhi kathaya, me mahyaṃ, kaḥ bhavān ugrarūpaḥ krūrākāraḥ. namaḥ astu te tubhyaṃ, he devavara devānāṃ pradhāna, prasīda prasādaṃ kuru, vijñātuṃ viśeṣaṇa jñātum icchāmi bhavantam, ādyam ādau bhavam ādyam. na hi yasmāt prajānāmi tava tvadīyāṃ pravṛttiṃ ceṣṭām.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "kālo'smi lokakṣayakṛt pravṛddho lokānsamāhartumiha pravṛttaḥ |",
            "ṛte'pi tvāṃ na bhaviṣyanti sarve ye'vasthitāḥ pratyanīkeṣu yodhāḥ",
        ], "|| 32 ||",
           "The Blessed Lord said: I am Time, grown mature, the destroyer of worlds, engaged here in subduing the worlds. Even without you, none of these warriors arrayed in the opposing armies shall survive.",
           bhashya=[
               "kālosmīti – kālaḥ asmi lokakṣayakṛt – lokānāṃ kṣayaṃ karotīti lokakṣayakṛt, pravṛddhaḥ vṛddhiṃ gataḥ, yadarthaṃ pravṛddhaḥ tat śṛṇu – lokān samāhartuṃ, saṃhartum, iha asmin kāle, pravṛttaḥ. ṛte'pi vināpi, tvā tvāṃ, na bhaviṣyanti bhīṣmadroṇa karṇaprabhṛtayaḥ sarve, yebhyaḥ tava āśaṅkā, ye avasthitāḥ, pratyanīkeṣu anīkamanīkaṃ prati pratyanīkeṣu pratipakṣabhūteṣu anīkeṣu, yodhāḥ yoddhāraḥ.",
           ]),
        _v([
            "tasmāttvamuttiṣṭha yaśo labhasva jitvā śatrūn bhuṅkṣva rājyaṃ samṛddham |",
            "mayaivaite nihatāḥ pūrvameva nimittamātraṃ bhava savyasācin",
        ], "|| 33 ||",
           "Therefore rise up and win glory; conquer your enemies and enjoy a prosperous kingdom. By me they have already been slain; be merely the instrument, O ambidextrous archer.",
           bhashya=[
               "tasmāt tvam uttiṣṭha “bhīṣmadroṇaprabhṛtayaḥ atirathāḥ avasthitāḥ ajeyāḥ devairapi, arjunena jitāḥ” iti yaśaḥ labhasva. kevalaṃ puṇyaiḥ hi tat prāpyate. jitvā śatrūn duryodhanaprabhṛtīn. bhuṅkṣva rājyaṃ samṛddham asapatnam akaṇṭakam. mayaiva ete nihatāḥ niścayena hatāḥ prāṇaiḥ viyojitāḥ pūrvameva. nimittamātraṃ bhava tvaṃ, he savyasācin. savyena vāmenāpi hastena śarāṇāṃ kṣepāt savyasācīti ucyate arjunaḥ.",
           ]),
        _v([
            "droṇaṃ ca bhīṣmaṃ ca jayadrathaṃ ca karṇaṃ tathānyānapi yodhavīrān |",
            "mayā hatāṃstvaṃ jahi mā vyathiṣṭhā yudhyasva jetāsi raṇe sapatnān",
        ], "|| 34 ||",
           "Slay Droṇa and Bhīṣma, Jayadratha and Karṇa, and the other heroic warriors, already slain by me. Do not waver; fight! You will conquer your rivals in battle.",
           bhashya=[
               "droṇañceti : droṇaṃ ca – yeṣu yodheṣu arjunasya āśaṅkā tāṃstān vyapadiśati bhagavān mayā hatān iti. tatra droṇabhīṣmayostāvat prasiddham āśaṅkā kāraṇam. droṇaḥ dhanurvedācāryāḥ divyāstrasampannaḥ ātmanaśca viśeṣataḥ guruḥ gariṣṭhaḥ. bhīṣmaḥ svacchandamṛtyuḥ divyāstrasampannaśca paraśurāmeṇa dvandvayuddham agamat, na ca parājitaḥ. tathā jayadrathaḥ yasya pitā tapaḥ carati “mama putrasya śiraḥ bhūmau nipātayiṣyati yaḥ tasyāpi śiraḥ patiṣyatī”ti. karṇo'pi vāsavadattāyā śaktyā tu amoghayā sampannaḥ sūryaputraḥ kānīnaḥ yataḥ ataḥ tannāmnaiva nirdeśaḥ. mayā hatān tvaṃ jahi nimittamātreṇa, mā vyathiṣṭhāḥ, tebhyo bhayaṃ mā kārṣīḥ. yudhyasva. jetāsi duryodhanaprabhṛtīn, raṇe yuddhe sapatnān śatrūn.",
           ]),
        {"speaker": "sañjaya uvāca"},
        _v([
            "etacchrutvā vacanaṃ keśavasya kṛtāñjalirvepamānaḥ kirīṭī |",
            "namaskṛtvā bhūya evāha kṛṣṇaṃ sagadgadaṃ bhītabhītaḥ praṇamya",
        ], "|| 35 ||",
           "Sañjaya said: Hearing these words of Keśava, the crowned one, trembling, with joined palms, bowed down and, prostrating in great fear, spoke again to Kṛṣṇa in a faltering voice.",
           bhashya=[
               "etacchrutveti – etat śrutvā vacanaṃ keśavasya pūrvoktaṃ kṛtāñjaliḥ san, vepamānaḥ, kampamānaḥ, kirīṭī, namaskṛtvā, bhūyaḥ punaḥ eva, āha uktavān, kṛṣṇaṃ sagadgadaṃ, bhayāviṣṭasya duḥkhābhighātāt, snehāviṣṭasya ca harṣodbhavāt, aśrupūrṇanetratve sati śleṣmaṇā kaṇṭhāvarodhaḥ tenaḥ vācaḥ apāṭavaṃ mandaśabdatvaṃ yat saḥ gadgadaḥ, tena saha vartate iti. “sagadgadaṃ vacanam āhe”ti vacana kriyā viśeṣaṇam. bhītabhītaḥ. punaḥ punaḥ bhayāviṣṭacetāḥ san praṇamya prahvaḥ bhūtvā “āha” iti vyavahitena sambandhaḥ.",
               "atrāvasare sañjayavacanaṃ sābhiprāyam. katham? droṇādiṣu arjunena nihateṣu ajeyeṣu caturṣu nirāśrayaḥ duryodhanaḥ nihataḥ eveti matvā dhṛtarāṣṭraḥ jayaṃ prati nirāśaḥ san sandhiṃ kariṣyati, tataḥ śānntiḥ ubhayeṣāṃ bhaviṣyati iti. tadapi na aśrauṣīt dhṛtarāṣṭraḥ bhavitavyavaśāt.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "sthāne hṛṣīkeśa tava prakīrtyā jagatprahṛṣyatyanurajyate ca |",
            "rakṣāṃsi bhītāni diśo dravanti sarve namasyanti ca siddhasaṅghāḥ",
        ], "|| 36 ||",
           "Arjuna said: It is fitting, Hṛṣīkeśa, that the world rejoices and delights in your praise; the demons flee in terror to every quarter, and all the hosts of the perfected bow to you.",
           bhashya=[
               "sthāne iti – sthāne yuktam. kiṃ tat. tava prakīrtyā tvanmāhātmyakīrtanena śrutena, he! hṛṣīkeśa! yat jagat prahṛṣyati, praharṣam upaiti, tat sthāne yuktam ityarthaḥ. athavā viṣayaviśeṣaṇaṃ sthāne iti. yuktaḥ harṣādiviṣayaḥ bhagavān, yataḥ īśvaraḥ sarvātmā sarvabhūtasuhṛt ca iti. tathā anurajyate anurāgaṃ ca upaiti, tacca viṣaye iti vyākhyeyam. kiṃ ca rakṣāṃsi, bhītāni bhayāviṣṭāni diśaḥ dravanti gacchanti, tacca sthāne viṣaye, sarve namasyanti namaskurvanti ca siddhasaṅghāḥ siddhānāṃ samudāyāḥ kapilādīnāṃ, tacca sthāne.",
           ]),
        _v([
            "kasmācca te na nameran mahātman garīyase brahmaṇo'pyādikartre |",
            "ananta deveśa jagannivāsa tvamakṣaraṃ sadasattatparaṃ yat",
        ], "|| 37 ||",
           "And why should they not bow to you, great soul, who are greater even than Brahmā, the first creator? O infinite one, Lord of gods, abode of the universe, you are the Imperishable, being and non-being, and what lies beyond them.",
           bhashya=[
               {"text": "bhagavataḥ harṣādiviṣayatve hetuṃ darśayati –", "intro": True},
               "kasmācca hetoḥ, te tubhyaṃ na nameran na namaskuryuḥ mahātman! garīyase gurutarāya, yataḥ brahmaṇaḥ hiraṇyagarbhasyāpi, ādikartā kāraṇam, tasmāt ādikartre, katham ete na namaskuryuḥ. ataḥ harṣādīnāṃ namaskārasya ca sthānaṃ tvam arhaḥ viṣayaḥ ityarthaḥ, he ananta! deveśa jagannivāsa! tvam akṣaraṃ tat paraṃ yat vedānteṣu śrūyate. kiṃ tat? sadasat iti sat vidyamānam. asacca yat nāsti iti buddhiḥ. te upadhānabhūte (upādhibhūte) sadasatī yasya akṣarasya, yaddvāreṇa sat asat iti upacaryate. paramārthataḥ tu sadasataḥ paraṃ tat akṣaraṃ yat vedavidaḥ vadanti. tat tvameva na anyat ityabhiprāyaḥ punarapi stauti –",
           ]),
        _v([
            "tvamādidevaḥ puruṣaḥ purāṇa stvamasya viśvasya paraṃ nidhānam |",
            "vettā'si vedyaṃ ca paraṃ ca dhāma tvayā tataṃ viśvamanantarūpa",
        ], "|| 38 ||",
           "You are the first of the gods, the ancient Person; you are the supreme resting-place of this universe; you are the knower and what is to be known, the highest abode. By you the universe is pervaded, O one of infinite form.",
           bhashya=[
               "tvam ādidevaḥ, jagataḥ sraṣṭṛtvāt, puruṣaḥ puri śayanāt. purāṇaḥ cirantanaḥ tvameva asya viśvasya paraṃ prakṛṣṭaṃ, nidhānam nidhīyate asmin jagat sarvaṃ mahāpralayādau iti. kiñca vettā asi, veditā asi, sarvasyaiva vedyajātasya. yacca vedyaṃ vedanārhaṃ tacca asi. paraṃ ca dhāma paramaṃ padaṃ vaiṣṇavam. tvayā tataṃ vyāptaṃ viśvaṃ samastam, anantarūpa! antaḥ na vidyate tava rūpāṇām. kiñca",
           ]),
        _v([
            "vāyuryamo'gnirvaruṇaḥ śaśāṅkaḥ prajāpatistvaṃ prapitāmahaśca |",
            "namo namaste'stu sahasrakṛtvaḥ punaśca bhūyo'pi namo namaste",
        ], "|| 39 ||",
           "You are Vāyu, Yama, Agni, Varuṇa, the moon, Prajāpati, and the great-grandsire. Salutation, salutation to you a thousand times, and again and yet again salutation to you!",
           bhashya=[
               "vāyuḥ tvaṃ yamaśca agniḥ, varuṇaḥ apāmpatiḥ śaśāṅkaḥ candramāḥ prajāpatiḥ tvaṃ kaśyapādiḥ, prapitāmahaḥ ca pitāmahasyāpi pitā prapitāmahaḥ, brahmaṇaḥ api pitā ityarthaḥ. namaḥ namaḥ, te tubhyam astu sahasrakṛtvaḥ punaḥ ca bhūyaḥ api namaḥ namaḥ te. bahuśaḥ namaskāra kriyābhyāsāvṛttigaṇanaṃ kṛtvasucā ucyate, “punaśca” “bhūyopī”ti śraddhābhaktyatiśayāt aparitoṣam ātmanaḥ darśayati.",
           ]),
        _v([
            "namaḥ purastādatha pṛṣṭhataste namo'stu te sarvata eva sarva |",
            "anantavīryāmitavikramastvaṃ sarvaṃ samāpnoṣi tato'si sarvaḥ",
        ], "|| 40 ||",
           "Salutation to you in front and behind; salutation to you on every side, O All! Infinite in power, immeasurable in might, you pervade all, and so you are all.",
           bhashya=[
               "namaḥ purastāt pūrvasyāṃ diśi, tubhyam atha pṛṣṭhataḥ te pṛṣṭhataḥ api ca te namaḥ astu. sarvataḥ eva sarvāsu dikṣu sarvatra sthitāya, he sarva! anantavīryāmitavikramaḥ anantaṃ vīryam asya, amitaḥ vikramaḥ asya, vīryaṃ sāmarthyam, vikramaḥ parākramaḥ. vīryavānapi kaścit śatruvadhādi viṣaye na parākramate, mandaparākramo vā. tvaṃ tu anantavīryaḥ amitavikramaḥ ca iti anantavīryāmitavikramaḥ. sarvaṃ samastaṃ jagat samāpnoṣi samyak ekena ātmanā vyāṣnoṣi yataḥ tataḥ tasmāt asi bhavasi sarvaḥ. tvayā vinābhūtaṃ na kiñcidastītyarthaḥ.",
           ]),
        _v([
            "sakheti matvā prasabhaṃ yaduktaṃ he kṛṣṇa he yādava he sakheti |",
            "ajānatā mahimānaṃ tavedaṃ mayā pramādātpraṇayena vāpi",
        ], "|| 41 ||",
           "Whatever I said rashly, thinking you a friend — 'O Kṛṣṇa, O Yādava, O friend' — not knowing this greatness of yours, out of carelessness or even affection;",
           bhashya=[
               {"text": "yataḥ ahaṃ tvānmāhātmyāparijñānāparādhī ataḥ –", "intro": True},
               "sakhā samānavayā : iti matvā jñātvā viparītabuddhyā, prasabham abhibhūya, yat uktaṃ he kṛṣṇa he yādava he sakheti ca ajānatā ajñāninā, mūḍhena, kim ajānatā ityāha mahimānaṃ māhātmyaṃ tava idam īśvarasya viśvarūpaṃ, “tava idaṃ mahimānam ajānatā” iti vaiyadhikaraṇyena sambandhaḥ. “tavema” miti pāṭho yadyasti tadā sāmānādhikaraṇyameva. mayā pramādāt vikṣipta cittatayā praṇayena vā api praṇayaḥ nāma snehanimittaḥ visrambhaḥ tenāpi kāraṇena yat uktavānasmi.",
           ]),
        _v([
            "yaccāpahāsārthamasatkṛto'si vihāraśayyāsanabhojaneṣu |",
            "eko'thavāpyacyuta tatsamakṣaṃ tat kṣāmaye tvāmahamaprameyam",
        ], "|| 42 ||",
           "and whatever disrespect I showed you in jest, at play, in bed, at rest or at meals, alone or in company, O Acyuta — for that I beg forgiveness of you, the immeasurable.",
           bhashya=[
               "yacca apahāsārthaṃ parihāsaprayojanāya, asatkṛtaḥ paribhūtaḥ, asi bhavasi, kva? vihāraśayyāsanabhojaneṣu – viharaṇaṃ vihāraḥ, pādavyāyāmaḥ. śayanaṃ śayyā, āsanam āsthāyikā, bhojanam aśanam, ityeteṣu vihāraśayyāsanabhojaneṣu, ekaḥ parokṣaḥ san, asatkṛtaḥ asi paribhūtaḥ asi, athavā'pi he acyuta! tat samakṣam, tacchabdaḥ kriyāviśeṣaṇārthaḥ pratyakṣaṃ vā asatkṛtaḥ asi, tat sarvam aparādhajātaṃ, kṣāmaye kṣamāṃ kāraye, tvām, aham, aprameyaṃ pramāṇātītam. yataḥ tvam –",
           ]),
        _v([
            "pitā'si lokasya carācarasya tvamasya pūjyaśca gururgarīyān |",
            "na tvatsamo'styabhyadhikaḥ kuto'nyo lokatraye'pyapratimaprabhāva",
        ], "|| 43 ||",
           "You are the father of the world, of the moving and the unmoving, its worshipful and most venerable teacher. There is none equal to you in the three worlds; how could there be one greater, O one of incomparable power?",
           bhashya=[
               "pitā asi janayitā asi, lokasya prāṇijātasya, carācarasya sthāvarajaṅgamasya. na kevalaṃ tvam asya jagataḥ pitā, pūjyaḥ ca pūjārhaḥ, yataḥ guruḥ garīyān gurutaraḥ . kasmādgurutarastvam ityāha – na ca tvatsamaḥ tvattulyaḥ anyaḥ asti. na hi īśvaradvayaṃ sambhavati, anekeśvaratve vyavahārānupapatteḥ. tvatsamaḥ eva tāvat anyaḥ na sambhavati, kutaḥ eva anyaḥ abhyadhikaḥ syāt? lokatraye'pi apratimaprabhāva – pratimīyate yayā sā pratimā, na vidyate pratimā yasya tava prabhāvasya saḥ tvam apratimaprabhāvaḥ he! apratimaprabhāva niratiśayaprabhāva ityarthaḥ.",
           ]),
        _v([
            "tasmātpraṇamya praṇidhāya kāyaṃ prasādaye tvāmahamīśamīḍyam |",
            "piteva putrasya sakheva sakhyuḥ priyaḥ priyāyārhasi deva soḍhum",
        ], "|| 44 ||",
           "Therefore, bowing down and prostrating my body, I seek your grace, adorable Lord. As a father with a son, a friend with a friend, a lover with the beloved, bear with me, O God.",
           bhashya=[
               "tasmāt, praṇamya namaskṛtya, praṇidhāya prakarṣeṇa nīcaiḥ dhṛtvā, kāyaṃ śarīram, prasādaye prasādaṃ kāraye, tvām, aham, īśitāraṃ, īḍyaṃ stutyam, tvaṃ punaḥ putrasya aparādhaṃ pitā yathā kṣamate sarvaṃ, sakheva ca sakhyuḥ aparādhaṃ, yathā vā priyaḥ priyāyāḥ aparādhaṃ kṣamate evam arhasi, he! deva! soḍhuṃ prasahituṃ, kṣantum ityarthaḥ.",
           ]),
        _v([
            "adṛṣṭapūrvaṃ hṛṣito'smi dṛṣṭvā bhayena ca pravyathitaṃ mano me |",
            "tadeva me darśaya deva rūpaṃ prasīda deveśa jagannivāsa",
        ], "|| 45 ||",
           "I rejoice at having seen what was never seen before, yet my mind is shaken with fear. Show me that other form of yours, O God; be gracious, Lord of gods, abode of the universe.",
           bhashya=[
               "adṛṣṭapūrvamiti : adṛṣṭapūrvaṃ na kadācidapi dṛṣṭapūrvam idaṃ viśvarūpaṃ tava mayā anyairvā tadahaṃ dṛṣṭvā, hṛṣitaḥ, asmi. bhayena ca pravyathitaṃ manaḥ me, ataḥ tadeva me mama, darśaya, he deva! rūpaṃ yat matsakham, prasīda deveśa, jagannivāsa jagataḥ nivāsaḥ jagannivāsaḥ, he jagannivāsa.",
           ]),
        _v([
            "kirīṭinaṃ gadinaṃ cakrahastamicchāmi tvāṃ draṣṭumahaṃ tathaiva |",
            "tenaiva rūpeṇa caturbhujena sahasrabāho bhava viśvamūrte",
        ], "|| 46 ||",
           "I wish to see you as before, crowned, with mace and discus in hand. Take on that four-armed form, O thousand-armed one of universal form.",
           bhashya=[
               "kirīṭinamiti : kirīṭinaṃ kirīṭavantaṃ, tathā gadinaṃ gadāvantaṃ, cakrahastam icchāmi tvāṃ prārthaye tvāṃ draṣṭum ahaṃ, tathaiva pūrvavat ityarthaḥ. yataḥ evaṃ tasmāt, tenaiva rūpeṇa vasudevaputrarūpeṇa, caturbhujena, sahasrabāho vārtamānikena viśvarūpeṇa, bhava, viśvamūrte! upasaṃhṛtya viśvarūpaṃ tenaiva rūpeṇa vasudevaputrarūpeṇa bhava ityarthaḥ.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "mayā prasannena tavārjunedaṃ rūpaṃ paraṃ darśitamātmayogāt |",
            "tejomayaṃ viśvamanantamādyaṃ yanme tvadanyena na dṛṣṭapūrvam",
        ], "|| 47 ||",
           "The Blessed Lord said: Out of grace, Arjuna, I have shown you by my own yoga this supreme form — radiant, universal, infinite and primal — which no one but you has seen before.",
           bhashya=[
               {"text": "arjunaṃ bhītam upalabhya upasaṃhṛtya viśvarūpaṃ priyavacanena āśvāsayan –", "intro": True},
               "mayā prasannena, prasādaḥ nāma tvayi anugrahabuddhiḥ, tadvatā prasannena mayā tava he! arjuna! paraṃ rūpaṃ viśvarūpaṃ, darśitam ātmayogāt ātmanaḥ aiśvaryasya sāmarthyāt, tejomayaṃ tejaḥprāyaṃ, viśvaṃ samastam, anantam antarahitam, ādau bhavam ādyam, yadrūpaṃ, me mama tvadanyena tvattaḥ anyena kenacit na dṛṣṭapūrvam.",
           ]),
        _v([
            "na vedayajñādhyayanairnadānairna ca kriyābhirnatapobhirugraiḥ |",
            "evaṃrūpaḥ śakya ahaṃ nṛloke draṣṭuṃ tvadanyena kurupravīra",
        ], "|| 48 ||",
           "Not by the Vedas, sacrifices or study, not by gifts, rituals or severe austerities can I be seen in such a form in the world of men by anyone but you, O great hero of the Kurus.",
           bhashya=[
               {"text": "ātmanaḥ mama rūpadarśanena kṛtārthaḥ eva tvaṃ saṃvṛttaḥ iti tat stauti–", "intro": True},
               "na vedayajñādhyayanaiḥ na caturṇāmapi vedānām adhyayanaiḥ yathāvat yajñādhyayanaiśca. vedādhyayanaireva yajñādhyayanasya siddhatvāt pṛthak yajñādhyayanagrahaṇaṃ yajñavijñānopalakṣaṇārtham. tathā na dānaiḥ tulāpuruṣādibhiḥ, na ca, kriyābhiḥ agnihotrādibhiḥ śrautādibhiḥ, nāpi tapobhiḥ, ugraiḥ cāndrāyaṇādibhiḥ ugraiḥ ghoraiḥ, evaṃrūpaḥ yathādarśitaṃ viśvarūpaṃ yasya saḥ aham evaṃrūpaḥ, na śakyaḥ ahaṃ, nṛloke manuṣyaloke, draṣṭuṃ tvadanyena tvattaḥ anyena kurupravīra.",
           ]),
        _v([
            "mā te vyathā mā ca vimūḍhabhāvo dṛṣṭvā rūpaṃ ghoramīdṛk mamedam |",
            "vyapetabhīḥ prītamanāḥ punastvaṃ tadeva me rūpamidaṃ prapaśya",
        ], "|| 49 ||",
           "Be not afraid, be not bewildered, at seeing this terrible form of mine. Freed from fear and glad at heart, behold again this other form of mine.",
           bhashya=[
               "mā te vyatheti – mā te vyathā – mā bhūt te bhayam, mā ca vimūḍhabhāvaḥ vimūḍhacittatā, dṛṣṭvā upalabhya, rūpaṃ ghoram īdṛk yathādarśitaṃ mama idaṃ. vyapetabhīḥ vigatabhayaḥ prītamanāḥ ca san punaḥ bhūyaḥ tvaṃ tadeva caturbhujaṃ śaṅkhacakragadādharaṃ tava iṣṭaṃ rūpam idaṃ prapaśya.",
           ]),
        {"speaker": "sañjaya uvāca"},
        _v([
            "ityarjunaṃ vāsudevastathoktvā svakaṃ rūpaṃ darśayāmāsa bhūyaḥ |",
            "āśvāsayāmāsa ca bhītamenaṃ bhūtvā punaḥ saumyavapurmahātmā",
        ], "|| 50 ||",
           "Sañjaya said: Having spoken thus to Arjuna, Vāsudeva showed him again his own form; and the great soul, becoming gentle in form once more, comforted him in his terror.",
           bhashya=[
               "ityarjunamiti – iti evam, arjunaṃ vāsudevaḥ tathābhūtāṃ vacanam uktvā, svakaṃ vasudeva gṛhe jātaṃ rūpaṃ, darśayāmāsa darśitavān bhūyaḥ punaḥ āśvāsayāmāsa ca āśvāsitavān ca, bhītam enaṃ bhūtvā punaḥ saumyavapuḥ prasannadehaḥ mahātmā.",
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "dṛṣṭvedaṃ mānuṣaṃ rūpaṃ tava saumyaṃ janārdana |",
            "idānīmasmi saṃvṛttaḥ sacetāḥ prakṛtiṃ gataḥ",
        ], "|| 51 ||",
           "Arjuna said: Seeing this gentle human form of yours, Janārdana, I have now come to myself and am restored to my own nature.",
           bhashya=[
               "dṛṣṭvedamiti – dṛṣṭvā idaṃ mānuṣaṃ rūpaṃ matsakhaṃ prasannaṃ tava saumyaṃ janārdana, idānīm adhunā, asmi saṃvṛttaḥ sañjātaḥ, kim? sacetāḥ prasannacittaḥ prakṛtiṃ svabhāvaṃ gataśca asmi.",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "sudurdarśamidaṃ rūpaṃ dṛṣṭavānasi yanmama |",
            "devā apyasya rūpasya nityaṃ darśanakāṅkṣiṇaḥ",
        ], "|| 52 ||",
           "The Blessed Lord said: This form of mine that you have seen is very hard to see; even the gods ever long to see it.",
           bhashya=[
               "sudurdarśamiti – sudurdarśaṃ suṣṭhu duḥkhena darśanam asya iti sudurdarśam, idaṃ rūpaṃ dṛṣṭavān asi yat, mama devāḥ api, asya mama rūpasya nityaṃ sarvadā darśanakāṅkṣiṇaḥ darśanepsavaḥ api na tvamiva dṛṣṭavantaḥ na drakṣyanti ca ityabhiprāyaḥ. kasmāt –",
           ]),
        _v([
            "nāhaṃ vedairna tapasā na dānena na cejyayā |",
            "śakya evaṃvidho draṣṭuṃ dṛṣṭavānasi māṃ yathā",
        ], "|| 53 ||",
           "Not by the Vedas, nor by austerity, nor by gifts, nor by sacrifice can I be seen as you have seen me.",
           bhashya=[
               "na ahaṃ vedaiḥ ṛgyajuḥsāmātharvavedaiḥ caturbhirapi, na tapasā ugreṇa cāndrāyaṇādinā, na dānena gobhūhiraṇyādinā, na ca ijyayā yajñena pūjayā vā śakyaḥ, evaṃvidhaḥ yathādarśitaprakāraḥ draṣṭuṃ dṛṣṭavānasi māṃ yathā tvam.",
           ]),
        _v([
            "bhaktyā tvananyayā śakyaḥ ahamevaṃ vidho'rjuna |",
            "jñātuṃ draṣṭuṃ ca tattvena praveṣṭuṃ ca parantapa",
        ], "|| 54 ||",
           "But by undivided devotion, Arjuna, I can be known and seen in truth, and entered into, O scorcher of foes.",
           bhashya=[
               {"text": "kathaṃ punaḥ śakyaḥ iti?ucyate", "intro": True},
               "bhaktyā tu, kiṃ viśiṣṭayā ityāha ananyayā apṛthagbhūtayā, bhagavataḥ anyatra pṛthak na kadācidapi (yā) bhavati (sā tu ananyā bhaktiḥ). sarvaiḥ api karaṇaiḥ vāsudevāt anyat na upalabhyate yayā sā ananyā bhaktiḥ tayā bhaktyā śakyaḥ aham, evaṃvidhaḥ viśvarūpaprakāraḥ, he arjuna, jñātuṃ śāstrataḥ, na kevalaṃ jñātuṃ śāstrataḥ draṣṭuṃ ca sākṣātkartuṃ tattvataḥ tattvena praveṣṭuṃ ca mokṣaṃ ca gantuṃ parantapa.",
           ]),
        _v([
            "matkarmakṛnmatparamo madbhaktaḥ saṅgavarjitaḥ |",
            "nirvairaḥ sarvabhūteṣu yaḥ sa māmeti pāṇḍava",
        ], "|| 55 ||",
           "He who does my work, who holds me supreme, who is devoted to me, free from attachment and without enmity towards any being — he comes to me, Pāṇḍava.",
           bhashya=[
               {"text": "adhunā sarvasya gītāśāstrasya sārabhūtaḥ arthaḥ niḥśreyasārthaḥ, anuṣṭheyatvena samuccitya ucyate –", "intro": True},
               "matkarmakṛt – madarthaṃ karma matkarma. tat karotīti matkarmakṛt matparamaḥ – karoti bhṛtyaḥ svāmikarma, na tu ātmanaḥ paramā pretya gantavyā gatiḥ iti svāminaṃ pratipadyate. ayaṃ tu matkarmakṛt māmeva paramāṃ gatiṃ pratipadyate iti matparamaḥ, ahaṃ paramaḥ parā gatiḥ yasya saḥ ayam matparamaḥ tathā, madbhaktaḥ māmeva sarvaprakāraiḥ sarvātmanā sarvotsāhena bhajate iti madbhaktaḥ. saṅgavarjitaḥ dhanaputramitrakalatrabandhuvargeṣu saṅgavarjitaḥ saṅgaḥ prītiḥ snehaḥ, tadvarjitaḥ, nirvairaḥ nirgatavairaḥ sarvabhūteṣu śatru bhāvarahitaḥ ātmanaḥ atyantāpakārapravṛtteṣvapi, yaḥ īdṛśaḥ madbhaktaḥ, saḥ mām eti, ahameva tasya parā gatiḥ, na anyā gatiḥ kācit bhavati. ayaṃ tava upadeśaḥ iṣṭaḥ mayā upadiṣṭaḥ, he! pāṇḍava! iti.",
           ]),
        "ornament",
        {"colophon": "iti śrī mahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsu upaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjunasaṃvāde viśvarūpadarśanayogo nāma ekādaśo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the eleventh chapter, Viśvarūpadarśana Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovinda bhagavatpūjya pāda śiṣya śrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye viśvarūpadarśanaṃ yogo nāma ekādaśo'dhyāyaḥ", "gloss": "Thus ends the eleventh chapter, Viśvarūpadarśana Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
