# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 8 (Akṣarabrahma Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 8 · Akṣarabrahma Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 8",
    "h1": "Bhagavad Gītā · Chapter 8",
    "subtitle": "Akṣarabrahma Yoga · the imperishable Brahman · with Śaṅkara's bhāṣya",
    "note": "Arjuna asks the meaning of the terms left at the end of chapter 7 — Brahman, adhyātma, karma, adhibhūta, adhidaiva, adhiyajña. Kṛṣṇa explains them, teaches remembrance of him at the hour of death, meditation on Om, the day and night of Brahmā, and the two paths of departure.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 7', 'gita-bhashya-07-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 9 ›', 'gita-bhashya-09-iast.html')],
    "sections": [
        {"bhashya": [
            "“te brahma tadviduḥ kṛtsnam” (7.29) ityādinā bhagavatā arjunasya praśnabījāni upadiṣṭāni ataḥ tatpraśnārthaṃ arjunaḥ uvāca.",
        ], "summary": "bhāṣya · the chapter's opening"},
        {"speaker": "arjuna uvāca"},
        _v([
            "kiṃ tad brahma kimadhyātmaṃ kiṃ karma puruṣottama |",
            "adhibhūtaṃ ca kiṃ proktaṃ adhidaivaṃ kimucyate",
        ], "|| 1 ||",
           "Arjuna said: What is that Brahman, what is the inner Self, what is action, O best of persons? What is called the elemental, and what is said to be the divine?"),
        _v([
            "adhiyajñaḥ kathaṃ ko'tra dehe'sminmadhusūdana |",
            "prayāṇakāle ca kathaṃ jñeyo'si niyatātmabhiḥ",
        ], "|| 2 ||",
           "Who is the lord of sacrifice here in this body, and how, O slayer of Madhu? And how are you to be known at the time of death by the self-controlled?"),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "akṣaraṃ brahma paramaṃ svabhāvo'dhyātmamucyate |",
            "bhūtabhāvodbhavakaro visargaḥ karmasañjñitaḥ",
        ], "|| 3 ||",
           "The Blessed Lord said: Brahman is the supreme Imperishable; its own being is called the inner Self; the offering that brings beings into existence is called action.",
           bhashya=[
               {"text": "eṣāṃ praśnānāṃ yathākramaṃ nirṇayāya śrī bhagavān uvāca.", "intro": True},
           ]),
        _v([
            "adhibhūtaṃ kṣaro bhāvaḥ puruṣaścādhidaivatam |",
            "adhiyajño'hamevātra dehe dehabhṛtāṃ vara",
        ], "|| 4 ||",
           "The elemental is perishable being; the divine is the Person; and I myself am the lord of sacrifice here in the body, O best of the embodied.",
           bhashya=[
               {"text": "akṣaraṃ iti. akṣaraṃ na kṣaratīti akṣaraṃ paramātmā “etasya vā akṣarasya praśāsane gārgi” (bṛ.u. 3.8.9) iti śruteḥ. oṅkārasya ca “omityekākṣaraṃ brahma” (8.13) iti pareṇa viśeṣaṇāt agrahaṇam. paramam iti niratiśaye brahmaṇi akṣare upapannataraṃ viśeṣaṇam. tasyaiva parasya brahmaṇaḥ pratidehaṃ pratyagātmabhāvaḥ svabhāvaḥ, svaḥ bhāvaḥ svabhāvaḥ adhyātmaṃ ucyate. ātmānaṃ dehaṃ adhikṛtya pratyagātmatayā pravṛttaṃ paramārthabrahmāvasānaṃ vastu svabhāvaḥ adhyātmaṃ ucyate – adhyātmaśabdena abhidhīyate. bhūtabhavodbhavakaraḥ bhūtānāṃ bhāvaḥ bhūtabhāvaḥ tasya udbhavaḥ bhūtabhāvodbhavaḥ taṃ karoti iti bhūtabhāvodbhavakaraḥ, bhūtavastūtpattikaraḥ ityarthaḥ. visargaḥ visarjanaṃ devatoddeśena carupuroḍāśādeḥ dravyasya parityāgaḥ, sa eṣa visargalakṣaṇaḥ yajñaḥ karmasañjñitaḥ karmaśabditaḥ ityetat. etasmāt hi bījabhūtāt vṛṣṭyādikrameṇa sthāvarajaṅgamāni bhūtāni udbhavanti.", "intro": True},
           ]),
        _v([
            "antakāle ca māmeva smaran muktvā kalevaram |",
            "yaḥ prayāti sa madbhāvaṃ yāti nāstyatra saṃśayaḥ",
        ], "|| 5 ||",
           "And whoever, at the time of death, leaves the body remembering me alone, and departs, attains my being; of this there is no doubt.",
           bhashya=[
               {"text": "adhibhūtaṃ iti. adhibhūtaṃ prāṇijātaṃ adhi (kṛtya) bhavatīti. ko'sau? kṣaraḥ kṣaratīti kṣaraḥ vināśī, yat kiñcit janimat vastu ityarthaḥ, puruṣaḥ pūrṇaḥ anena sarvam iti, puri śayanāt vā puruṣaḥ ādityāntargataḥ hiraṇyagarbhaḥ, sarvaprāṇikaraṇānāṃ anugrāhakaḥ, saḥ adhidaivatam. adhiyajñaḥ sarvayajñābhimāninī viṣṇvākhyā devatā, “yajño vai viṣṇuḥ” (tai.saṃ. 1.7.4) iti śruteḥ, sa hi viṣṇuḥ aham eva, atra asmin deha yaḥ yajñaḥ tasya ahaṃ adhiyajñaḥ, yajñaḥ hi dehanirvartyatvena dehasamavāyī iti dehādhikaraṇaḥ bhavati, dehabhṛtāṃ vara.", "intro": True},
               "antakāle iti. antakāle maraṇakāle ca mām eva parameśvaraṃ viṣṇuṃ smaran muktvā parityajya kalevaraṃ śarīraṃ yaḥ prayāti gacchati, saḥ madbhāvaṃ vaiṣṇavaṃ tattvaṃ yāti. na asti na vidyate atra asmin arthe saṃśayaḥ, yāti vā na vā iti.",
           ]),
        _v([
            "yaṃ yaṃ vā'pi smaran bhāvaṃ tyajatyante kalevaram |",
            "taṃ tamevaiti kaunteya sadā tadbhāva bhāvitaḥ",
        ], "|| 6 ||",
           "Whatever state one remembers when leaving the body at the end, to that very state one goes, son of Kuntī, being always absorbed in it.",
           bhashya=[
               {"text": "na madviṣayaḥ eva ayaṃ niyamaḥ kiṃ tarhi –", "intro": True},
               "yaṃ iti. yaṃ yaṃ vā'pi yaṃ yaṃ bhāvaṃ devatāviśeṣaṃ smaran cintayan tyajati parityajati ante antakāle prāṇaviyogakāle kalebaraṃ śarīraṃ taṃ tam eva smṛtaṃ bhāvaṃ eva eti na anyaṃ kaunteya! sadā sarvadā tadbhāvabhāvitaḥ tasmin bhāvaḥ saḥ bhāvitaḥ smaryamāṇatayā abhyastaḥ yena saḥ tadbhāvabhāvitaḥ san.",
           ]),
        _v([
            "tasmātsarveṣu kāleṣu māmanusmara yudhya ca |",
            "mayyarpitamanobuddhirmāmevaiṣyasyasaṃśayaḥ",
        ], "|| 7 ||",
           "Therefore at all times remember me, and fight. With mind and understanding offered to me, you will surely come to me.",
           bhashya=[
               {"text": "yasmāt evaṃ antyā bhāvanā dehāntaraprāptau kāraṇam.", "intro": True},
               "tasmāt iti. tasmāt sarveṣu kāleṣu māṃ anusmara. yathāśāstram yuddhya ca yuddhaṃ ca svadharmaṃ kuru. mayi vāsudeve arpite manobuddhī yasya tava saḥ tvaṃ mayi arpitamanobuddhiḥ san mām eva yathāsmṛtaṃ eṣyasi āgamiṣyasi, asaṃśayaḥ na saṃśayaḥ atra vidyate. kiñca.",
           ]),
        _v([
            "abhyāsayogayuktena cetasā nānyagāminā |",
            "paramaṃ puruṣaṃ divyaṃ yāti pārthānucintayan",
        ], "|| 8 ||",
           "With a mind disciplined by the yoga of practice and not straying elsewhere, meditating, one reaches the supreme divine Person, Pārtha.",
           bhashya=[
               "abhyāsa iti. abhyāsayogayuktena – mayi cittasamarpaṇaviṣayabhūte ekasmin tulyapratyayāvṛttilakṣaṇaḥ vilakṣaṇapratyayānantaritaḥ abhyāsaḥ, sa cāsau yogaḥ tena yuktaṃ tatraiva vyāpṛtaṃ yoginaḥ cetaḥ, tena cetasā nānyagāminā na anyatra viṣayāntare gantuṃ śīlaṃ asyeti nānyagāmi tena nānyagāminā, paramaṃ niratiśayaṃ puruṣaṃ divyaṃ divi sūryamaṇḍale bhavaṃ yāti gacchati he pārtha! anucintayan śāstrācāryopadeśaṃ anudhyāyan ityetat.",
           ]),
        _v([
            "kaviṃ purāṇamanuśāsitāramaṇoraṇīyāṃ samanusmaredyaḥ |",
            "sarvasya dhātāramacintyarūpamādityavarṇaṃ tamasaḥ parastāt",
        ], "|| 9 ||",
           "He who meditates on the seer, the ancient, the ruler, subtler than the subtle, the sustainer of all, of unthinkable form, sun-coloured, beyond darkness —",
           bhashya=[
               {"text": "9.0. kiṃ viśiṣṭaṃ ca puruṣaṃ yāti iti? ucyate", "intro": True},
               "kaviṃ iti. kaviṃ krāntadarśinaṃ sarvajñaṃ, purāṇaṃ cirantanaṃ, anuśāsitāraṃ sarvasya jagataḥ praśāsitāraṃ, aṇoḥ sūkṣmāt api aṇīyāṃsaṃ sūkṣmataraṃ anusmaret anucintayet yaḥ kaścit, sarvasya karmaphalajātasya dhātāraṃ vidhātāraṃ vicitratayā prāṇibhyaḥ vibhaktāraṃ, (vibhajya dhātāraṃ) acintyarūpaṃ na asya rūpaṃ niyataṃ vidyamānam api kenacit cintayituṃ śakyate iti acintyarūpaḥ taṃ ādityavarṇam ādityasya iva nityacaitanyaprakāśaḥ varṇaḥ yasya taṃ ādityavarṇam tamasaḥ parastāt ajñānalakṣaṇāt mohāndhakārāt paraṃ taṃ “anucintayan yāti” iti pūrveṇa sambandhaḥ. kiñca –",
           ]),
        _v([
            "prayāṇakāle manasā'calena bhaktyā yukto yogabalena caiva |",
            "bhruvormadhye prāṇamāveśya samyak sa taṃ paraṃ puruṣamupaiti divyam",
        ], "|| 10 ||",
           "at the time of departure, with unmoving mind, joined in devotion and by the power of yoga, fixing the breath between the brows, he reaches that supreme divine Person.",
           bhashya=[
               "prayāṇa iti. prayāṇakāle maraṇakāle manasā acalena calanavarjitena bhaktyā yuktaḥ bhajanaṃ bhaktiḥ tayā yuktaḥ yogabalena ca eva yogasya balaṃ yogabalaṃ samādhijasaṃskāra pracayajanitacittasthairyalakṣaṇaṃ yogabalaṃ tena ca yuktaḥ ityarthaḥ pūrvaṃ hṛdayapuṇḍarīke vaśīkṛtya cittaṃ tataḥ ūrdhvagāminyā nāḍyā bhūmijayakrameṇa bhruvoḥ madhye prāṇaṃ āveśya sthāpayitvā samyak apramattaḥ san, saḥ evaṃ vidvān yogī “kaviṃ purāṇam” (8.9) ityādi lakṣaṇaṃ taṃ paraṃ (parataraṃ) puruṣaṃ upaiti pratipadyate divyaṃ dyotanātmakam.",
           ]),
        _v([
            "yadakṣaraṃ vedavido vadanti viśanti yadyatayo vītarāgāḥ |",
            "yadicchanto brahmacaryaṃ caranti tatte padaṃ saṅgraheṇa pravakṣye",
        ], "|| 11 ||",
           "That which knowers of the Veda call the Imperishable, which ascetics free from passion enter, desiring which they live the celibate life — that goal I will tell you briefly.",
           bhashya=[
               {"text": "punarapi vakṣyamāṇena upāyena pratipitsitasya brahmaṇaḥ vedavidvadanādi viśeṣaṇa viśeṣyasya abhidhānaṃ karoti bhagavān –", "intro": True},
           ]),
        _v([
            "sarvadvārāṇi saṃyamya mano hṛdi nirudhya ca |",
            "mūrdhnyādhāyātmanaḥ prāṇamāsthito yogadhāraṇām",
        ], "|| 12 ||",
           "Closing all the gates, confining the mind in the heart, placing the breath in the head, established in the concentration of yoga,",
           bhashya=[
               {"text": "yat iti. yat akṣaraṃ na kṣaratīti akṣaraṃ avināśi vedavidaḥ vedārthajñāḥvadanti, “etadvai tadakṣaraṃ gārgi brāhmaṇā abhivadanti” iti śruteḥ, sarvaviśeṣanivartakatvena abhivadanti “asthūlamanaṇu” (bṛ.u.3.8.8) ityādi. kiñca viśanti praviśanti samyagdarśanaprāptau satyāṃ yat yatayaḥ yatanaśīlāḥ sannyāsinaḥ vītarāgāḥ vītaḥ vigataḥ rāgaḥ yebhyaḥ te vītarāgāḥ. yat ca akṣaraṃ icchantaḥ – “jñātuṃ” iti vākyaśeṣaḥ – brahmacaryaṃ gurau caranti ācaranti, tat te padaṃ tat akṣarākhyaṃ padaṃ padanīyaṃ te tubhyaṃ saṅgraheṇa saṅgrahaḥ saṅkṣepaḥ tena saṅkṣepeṇa pravakṣye kathayiṣyāmi.", "intro": True},
               {"text": "“sa yoha vai tadbhagavan manuṣyeṣu prāṇayāntamoṅkāra mabhidhyāyīta katamaṃ vāva sa tena lokaṃ jayatīti. tasmai sa hovāca etadvai satyakāma paraṃ cāparaṃ ca brahma yadoṅkāraḥ” ityupakramya “yaḥ punaretaṃ trimātreṇomityetenaivākṣareṇa paraṃ puruṣa mabhidhyāyīta... sa sāmabhirunnīyate brahmalokam (pra.u.5.1.2.5) ityādinā vacanena “anyatra dharmādanyatrādharmāt” iti ca upakramya “sarve vedā yatpadamāmananti. tapāṃsi sarvāṇi ca yadvadanti. yadicchanto brahmacaryaṃ caranti. tatte padaṃ saṅgraheṇa bravīmyomityet”. (kaṭha.u.2.14.15) ityādibhiśca vacanaiḥ parasya brahmaṇaḥ vācakarūpeṇa, pratimāvat pratīkarūpeṇa vā, parabrahmapratipattisādhanatvena mandamadhyamabuddhīnāṃ vivakṣitasya oṅkārasya upāsanaṃ kālāntare muktiphalaṃ uktaṃ yat, tadeva ihāpi “kaviṃ purāṇamanuśāsitāraṃ”, “yadakṣaraṃ vedavido vadanti” iti ca upanyastasya parasya brahmaṇaḥ pūrvoktarūpeṇa pratipattyupāyabhūtasya oṅkārasya kālāntaramuktiphalaṃ upāsanaṃ yogadhāraṇāsahitaṃ vaktavyaṃ prasaktānuprasaktaṃ ca yatkiñcit, ityevamarthaḥ uttaraḥ granthaḥ ārabhyate.", "intro": True},
               "sarva iti. sarvadvārāṇi sarvāṇi ca tāni dvārāṇi ca sarvadvārāṇi upalabdhau, tāni sarvāṇi saṃyamya saṃyamanaṃ kṛtvā manaḥ hṛdi hṛdayapuṇḍarīke nirudhya nirodhaṃ kṛtvā niṣpracāraṃ āpādya, tatra vaśīkṛtena manasā hṛdayāt ūrdhvagāminyā nāḍyā ūrdhvaṃ āruhya mūrthni ādhāya ātmanaḥ prāṇaṃ āsthitaḥ pravṛttaḥ yogadhāraṇāṃ dhārayitum. tatraiva ca dhārayan –",
           ]),
        _v([
            "omityekākṣaraṃ brahma vyāharan māmanusmaran |",
            "yaḥ prayāti tyajan dehaṃ sa yāti paramāṃ gatim",
        ], "|| 13 ||",
           "uttering the one syllable Om, which is Brahman, and remembering me — he who departs, leaving the body, reaches the highest goal.",
           bhashya=[
               "om iti. oṃ iti ekākṣaraṃ brahma brahmaṇaḥ abhidhānabhūtaṃ oṅkāraṃ vyāharan uccārayan, tadarthabhūtaṃ māṃ īśvaraṃ anusmaran anucintayan yaḥ prayāti mriyate saḥ tyajan parityajan dehaṃ śarīraṃ “tyajan dehaṃ” iti prayāṇaviśeṣaṇārthaṃ, dehatyāgena prayāṇaṃ ātmanaḥ na svarūpanāśena ityarthaḥ saḥ evaṃ tyajan yāti gacchati paramāṃ prakṛṣṭāṃ gatim.",
           ]),
        _v([
            "ananyacetāḥ satataṃ yo māṃ smarati nityaśaḥ |",
            "tasyāhaṃ sulabhaḥ pārtha nityayuktasya yoginaḥ",
        ], "|| 14 ||",
           "For the yogin who remembers me constantly, with a mind that never strays elsewhere, I am easy to reach, Pārtha, ever disciplined as he is.",
           bhashya=[
               "ananyacetāḥ iti. ananyacetāḥ na anyaviṣaye cetaḥ yasya saḥ ayaṃ ananyacetāḥ yogī satataṃ sarvadā yaḥ māṃ parameśvaraṃ smarati nityaśaḥ “satataṃ” iti nairantaryaṃ ucyate, “nityaśaḥ” iti dīrghakālaṃ ucyate”. na ṣaṇmāsaṃ saṃvatsaraṃ vā kiṃ tarhi? yāvajjīvaṃ nairantaryeṇa yaḥ māṃ smarati ityarthaḥ. tasya yoginaḥ ahaṃ sulabhaḥ sukhena labhyaḥ he pārtha, nityayuktasya sadā samāhitacittasya yoginaḥ. yataḥ evaṃ, ataḥ ananyacetāḥ san mayi sadā samāhitaḥ bhavet.",
           ]),
        _v([
            "māmupetya punarjanma duḥkhālayamaśāśvatam |",
            "nāpnuvanti mahātmānaḥ saṃsiddhiṃ paramāṃ gatāḥ",
        ], "|| 15 ||",
           "Having come to me, the great souls do not come again to birth, that transient home of sorrow, for they have reached the highest perfection.",
           bhashya=[
               {"text": "tava saulabhyena kiṃ syāt iti? ucyate, śṛṇu tat mama saulabhyena yat bhavati.", "intro": True},
               "māṃ upetya iti. māṃ īśvaraṃ upetya madbhāvaṃ āpadya punarjanma punarutpattiṃ na āpnuvanti na prāpnuvanti. kiṃ viśiṣṭaṃ punarjanma na prāpnuvanti iti? tadviśeṣaṇaṃ āha – duḥkhālayaṃ duḥkhānāṃ ādhyātmikādīnāṃ ālayaṃ āśrayaṃ, ālīyante yasmin duḥkhāni iti duḥkhālayaṃ janma. na kevalaṃ duḥkhālayaṃ aśāśvataṃ anavasthitasvarūpaṃ ca. nāpnuvanti īdṛśaṃ punarjanma mahātmānaḥ yatayaḥ saṃsiddhiṃ mokṣākhyāṃ paramāṃ prakṛṣṭāṃ gatāḥ prāptāḥ. ye punaḥ māṃ na prāpnuvanti te punaḥ āvartante.",
           ]),
        _v([
            "ābrahmabhuvanāllokāḥ punarāvartino'rjuna |",
            "māmupetya tu kaunteya punarjanma na vidyate",
        ], "|| 16 ||",
           "All the worlds up to the realm of Brahmā return again, Arjuna; but for one who reaches me, son of Kuntī, there is no rebirth.",
           bhashya=[
               {"text": "kiṃ punaḥ tvattaḥ anyat prāptāḥ punaḥ āvartante iti? ucyate –", "intro": True},
               "ābrahmabhuvanāt iti. ābrahmabhuvanāt bhavanti asmin bhūtāni iti bhuvanaṃ. brahmaṇo bhuvanaṃ brahmabhuvanaṃ, brahmalokaḥ ityarthaḥ, ābrahmabhuvanāt saha brahmabhuvanena lokāḥ sarve punarāvartinaḥ punarāvartasvabhāvāḥ he arjuna, māṃ ekaṃ upetya tu kaunteya punarjanma punarutpattiḥ na vidyate.",
           ]),
        _v([
            "sahasrayugaparyantamaharyadbrahmaṇo viduḥ |",
            "rātriṃ yugasahasrāntāṃ te'horātravido janāḥ",
        ], "|| 17 ||",
           "Those who know that a day of Brahmā lasts a thousand ages, and that his night ends after a thousand ages, are knowers of day and night.",
           bhashya=[
               {"text": "brahmalokasahitāḥ lokāḥ kasmāt punarāvartinaḥ? kālaparicchinnatvāt. katham?", "intro": True},
           ]),
        _v([
            "avyaktād vyaktayaḥ sarvāḥ prabhavantyaharāgame |",
            "rātryāgame pralīyante tatraivāvyaktasañjñake",
        ], "|| 18 ||",
           "At the coming of that day all manifest things spring from the unmanifest; at the coming of that night they dissolve into that very thing called the unmanifest.",
           bhashya=[
               {"text": "sahasra iti. sahasrayuga paryantaṃ sahasrāṇi yugāni paryantaṃ paryavasānaṃ yasya ahnaḥ tat ahaḥ sahasrayugaparyantaṃ brahmaṇaḥ prajāpateḥ virājaḥ viduḥ, rātriṃ api yugasahasrāntāṃ ahaḥ parimāṇāṃ eva. ke viduriti? āha – te ahorātravidaḥ kālasaṅkhyāvidaḥ janāḥ ityarthaḥ. yataḥ evaṃ kālaparicchinnāḥ te, ataḥ punarāvartinaḥ lokāḥ.", "intro": True},
               {"text": "prajāpateḥ ahani yat bhavati rātrau ca, tat ucyate.", "intro": True},
               "avyaktāt iti. avyaktāt avyaktaṃ prajāpateḥ svāpāvasthā, tasmāt avyaktāt vyaktayaḥ vyajyante iti vyaktayaḥ sthāvarajaṅgamalakṣaṇāḥ, sarvāḥ prajāḥ prabhavanti abhivyajyante, ahnaḥ āgamaḥ aharāgamaḥ tasmin aharāgame kāle brahmaṇaḥ prabodhakāle. tathā rātryāgame brahmaṇaḥ svāpakāle pralīyante sarvāḥ vyaktayaḥ tatra eva pūrvokte avyakta sañjñake.",
           ]),
        _v([
            "bhūtagrāmaḥ sa evāyaṃ bhūtvā bhūtvā pralīyate |",
            "rātryāgame'vaśaḥ pārtha prabhavatyaharāgame",
        ], "|| 19 ||",
           "This same multitude of beings, coming into being again and again, dissolves helplessly at the coming of night, Pārtha, and springs forth at the coming of day.",
           bhashya=[
               {"text": "akṛtābhyāgamakṛtavipraṇāśadoṣaparihārārthaṃ, bandhamokṣaśāstra pravṛttisāphalya pradarśanārthaṃ, avidyādikleśamūlakarmāśayavaśācca avaśaḥ bhūtagrāmaḥ bhūtvā bhūtvā pralīyate ityataḥ saṃsāre vairāgyadarśanārthaṃ ca idam āha.", "intro": True},
               "bhūtagrāmaḥ iti. bhūtagrāmaḥ sthāvarajaṅgamalakṣaṇaḥ yaḥ pūrvasmin kalpe āsīt sa eva ayaṃ nānyaḥ bhūtvā bhūtvā aharāgame, pralīyate punaḥ punaḥ rātryāgame ahnaḥ kṣaye avaśaḥ asvatantraḥ eva, he pārtha! prabhavati jāyate avaśaḥ eva aharāgame.",
           ]),
        _v([
            "parastasmāttu bhāvo'nyo'vyakto'vyaktātsanātanaḥ |",
            "yaḥ sa sarveṣu bhūteṣu naśyatsu na vinaśyati",
        ], "|| 20 ||",
           "But beyond that unmanifest there is another, eternal, unmanifest Being, which does not perish when all beings perish.",
           bhashya=[
               {"text": "yat upanyastaṃ akṣaraṃ tasya prāptyupāyo nirdiṣṭaḥ “omityekākṣaraṃ brahma” (8.13) ityādinā. atha idānīṃ akṣarasyaiva svarūpanirdidikṣayā idaṃ ucyate, anena yogamārgeṇa idaṃ gantavyaṃ iti.", "intro": True},
               "paraḥ iti. paraḥ vyatiriktaḥ bhinnaḥ – kutaḥ? tasmāt pūrvoktāt. “tu” śabdaḥ akṣarasya vivakṣitasya avyaktāt vailakṣaṇyaviśeṣaṇārthaḥ. bhāvaḥ akṣarākhyaṃ paraṃ brahma. vyatiriktatve satyapi sālakṣaṇyaprasaṅgo'stīti tadvinivṛttyarthaṃ āha – anyaḥ iti. anyaḥ vilakṣaṇaḥ. sa ca avyaktaḥ anindriyagocaraḥ “parastasmāt” ityuktaṃ, kasmāt punaḥ paraḥ? pūrvoktāt bhūtagrāmabījabhūtāt avidyālakṣaṇāt avyaktāt anyaḥ vilakṣaṇaḥ bhāvaḥ ityabhiprāyaḥ. sanātanaḥ cirantanaḥ yaḥ saḥ bhāvaḥ sarveṣu bhūteṣu brahmādiṣu naśyatsu na vinaśyati.",
           ]),
        _v([
            "avyakto'kṣara ityuktastamāhuḥ paramāṃ gatim |",
            "yaṃ prāpya na nivartante taddhāma paramaṃ mama",
        ], "|| 21 ||",
           "That unmanifest is called the Imperishable; they call it the highest goal, reaching which none return. That is my supreme abode.",
           bhashya=[
               "avyaktaḥ iti. yo'sau avyaktaḥ akṣaraḥ ityuktaḥ taṃ eva akṣarasañjñakaṃ avyaktaṃ bhāvaṃ āhuḥ paramāṃ prakṛṣṭāṃ gatim. yaṃ paraṃ bhāvaṃ prāpya gatvā na nivartante saṃsārāya, tat dhāma sthānaṃ paramaṃ prakṛṣṭaṃ mama, “viṣṇoḥ paramaṃ padam” (nṛ.pu.5.10) ityarthaḥ.",
           ]),
        _v([
            "puruṣaḥ sa paraḥ pārtha bhaktyā labhyastvananyayā |",
            "yasyāntaḥsthāni bhūtāni yena sarvamidaṃ tatam",
        ], "|| 22 ||",
           "That supreme Person, Pārtha, within whom beings dwell and by whom all this is pervaded, is to be won by undivided devotion.",
           bhashya=[
               {"text": "tallabdheḥ upāyaḥ ucyate –", "intro": True},
               "puruṣaḥ iti. puruṣaḥ puri śayanāt pūrṇatvādvā, saḥ paraḥ pārthaḥ, paraḥ niratiśayaḥ, yasmāt puruṣāt na paraṃ kiñcit. saḥ bhaktyā labhyastu jñānalakṣaṇayā ananyayā ātmaviṣayayā (7.17) yasya puruṣasya antaḥsthāni madhyasthāni bhūtāni kāryabhūtāni, kāryaṃ hi kāraṇasya antarvarti bhavati. yena puruṣeṇa sarva idaṃ jagat tataṃ vyāptam ākāśeneva ghaṭādi.",
           ]),
        _v([
            "yatra kāle tvanāvṛttimāvṛttiṃ caiva yoginaḥ |",
            "prayātā yānti taṃ kālaṃ vakṣyāmi bharatarṣabha",
        ], "|| 23 ||",
           "Now I will tell you, O best of the Bhāratas, the times at which yogins who depart do not return, and at which they return.",
           bhashya=[
               {"text": "prakṛtānāṃ yogināṃ praṇavāveśitabrahmabuddhīnāṃ kālāntaramuktibhājāṃ brahmapratipattaye uttaro mārgo vaktavyaḥ iti “yatra kāle” ityādi vivakṣitārthasamarpaṇārthaṃ ucyate āvṛttimārgopanyāsaḥ itaramārgastutyarthaḥ –", "intro": True},
               "yatra iti. yatra kāle prayātāḥ iti vyavahitena sambandhaḥ. yatra yasmin kāle tu anāvṛttiṃ apunarjanma āvṛttiṃ tadviparītāṃ caiva. “yoginaḥ” iti yoginaḥ karmiṇaśca ucyante, karmiṇastu guṇataḥ “karmayogena yoginām” (3.3) iti viśeṣaṇāt – yoginaḥ yatra kāle prayātāḥ mṛtāḥ yoginaḥ anāvṛttiṃ yānti, yatra kāle ca prayātāḥ āvṛttiṃ yānti, taṃ kālaṃ vakṣyāmi bharatarṣabha.",
           ]),
        _v([
            "agnirjyotirahaḥ śuklaḥ ṣaṇmāsā uttarāyaṇam |",
            "tatra prayātā gacchanti brahma brahmavido janāḥ",
        ], "|| 24 ||",
           "Fire, light, day, the bright fortnight, the six months of the sun's northern course — departing by these, knowers of Brahman go to Brahman.",
           bhashya=[
               {"text": "taṃ kālaṃ āha –", "intro": True},
               "agniḥ iti. agniḥ kālābhimāninī devatā. tathā – jyotiḥ api devataiva kālābhimāninī. athavā agnijyotiṣī yathāśrute eva devate. bhūyasā tu nirdeśo “yatra kāle” “taṃ kālaṃ” iti, āmravanavat. tathā ahaḥ devatā aharabhimāninī, śuklaḥ śuklapakṣadevatā, ṣaṇmāsā uttarāyaṇaṃ, tatrāpi devatā eva mārgabhūtā iti sthitaḥ anyatra (bra.sū.bhāṣye.4.3.4) ayaṃ nyāyaḥ. tatra tasmin mārge prayātāḥ mṛtāḥ gacchanti brahma brahmavidaḥ brahmopāsakāḥ brahmopāsana parāḥ janāḥ. “krameṇa” iti vākyaśeṣaḥ, na hi sadyomuktibhājāṃ samyagdarśana niṣṭhānāṃ gatiḥ āgatirvā kvacit asti. “na tasya prāṇāḥ utkrāmanti” (bṛ.u.4.4.6) iti śruteḥ. brahmasaṃlīna prāṇāḥ eva te brahmamayāḥ brahmabhūtāḥ eva te.",
           ]),
        _v([
            "dhūmo rātristathā kṛṣṇaḥ ṣaṇmāsā dakṣiṇāyanam |",
            "tatra cāndramasaṃ jyotiryogī prāpya nivartate",
        ], "|| 25 ||",
           "Smoke, night, the dark fortnight, the six months of the southern course — by these the yogin reaches the light of the moon and returns.",
           bhashya=[
               "dhūmaḥ iti. dhūmaḥ rātriḥ dhūmābhimāninī rātryabhimāninī ca devatā. tathā kṛṣṇaḥ kṛṣṇapakṣadevatā. ṣaṇmāsā dakṣiṇāyānaṃ iti ca pūrvavat devatā eva. tatra candramasi bhavaṃ cāndramasaṃ jyotiḥ phalaṃ iṣṭādikārī yogī karmī prāpya bhuktvā tatkṣayāt iha punaḥ nivartate.",
           ]),
        _v([
            "śuklakṛṣṇe gatī hyete jagataḥ śāśvate mate |",
            "ekayā yātyanāvṛttimanyayā''vartate punaḥ",
        ], "|| 26 ||",
           "These two paths of the world, the bright and the dark, are held to be eternal. By the one a man goes and does not return; by the other he returns again.",
           bhashya=[
               "śukla iti. śuklakṛṣṇe śuklā ca kṛṣṇā ca śuklakṛṣṇe, jñānaprakāśakatvāt śuklā, tadabhāvāt kṛṣṇā, ete śuklakṛṣṇe hi gatī – jagataḥ iti adhikṛtānāṃ jñānakarmaṇoḥ, na jagataḥ sarvasya eva ete gatī sambhavataḥ śāśvate nitye, saṃsārasya nityatvāt, mate abhiprete. tatra ekayā śuklayā yāti anāvṛttiṃ, anyayā itarayā āvartate punaḥ bhūyaḥ.",
           ]),
        _v([
            "naite sṛtī pārtha jānan yogī muhyati kaścana |",
            "tasmātsarveṣu kāleṣu yogayukto bhavārjuna",
        ], "|| 27 ||",
           "Knowing these two paths, Pārtha, no yogin is deluded. Therefore at all times be disciplined in yoga, Arjuna.",
           bhashya=[
               "naite iti. na ete yathokte sṛtī mārgau pārtha! jānan “saṃsārāya ekā, anyā mokṣāya ca” iti, yogī na muhyati kaścana kaścidapi, tasmāt sarveṣu kāleṣu yogayuktaḥ samāhitaḥ bhava arjuna, śṛṇu tasya yogasya māhātmyam –",
           ]),
        _v([
            "vedeṣu yajñeṣu tapassu caiva dāneṣu yatpuṇyaphalaṃ pradiṣṭam |",
            "atyeti tatsarvamidaṃ viditvā yogī paraṃ sthānamupaiti cādyam",
        ], "|| 28 ||",
           "Whatever fruit of merit is declared for the Vedas, for sacrifices, austerities and gifts — the yogin who knows this passes beyond it all and reaches the supreme, primal abode.",
           bhashya=[
               "vedeṣviti. vedeṣu samyagadhīteṣu yajñeṣu ca sādguṇyena anuṣṭhiteṣu tapaḥsu ca sutapteṣu dāneṣu ca samyagdatteṣu, eteṣu yat puṇyaphalaṃ pradiṣṭaṃ śāstreṇa, atyeti atītya gacchati tat sarvaṃ phalajātam, idaṃ viditvā saptapraśnanirṇayadvāreṇa uktaṃ arthaṃ samyak avadhārya anuṣṭhāya yogī, paraṃ utkṛṣṭaṃ aiśvaryaṃ sthānaṃ upaiti ca pratipadyate ādyaṃ ādau bhavaṃ, kāraṇaṃ brahma ityarthaḥ.",
           ]),
        "ornament",
        {"colophon": "iti śrī mahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītā – sūpaniṣatsu brahmavidyāyāṃ – yogaśāstre śrīkṛṣṇārjuna saṃvāde dhāraṇāyogo akṣaraparabrahmayogaḥ nāma aṣṭamo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the eighth chapter, Akṣarabrahma Yoga."},
        {"colophon": "iti śrī matparamahaṃsa parivrājakācāryagovindabhagavatpūjyapādaśiṣya śrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye dhāraṇāyogo akṣaraparabrahmayogaḥ nāma aṣṭamo'dhyāyaḥ.", "gloss": "Thus ends the eighth chapter, Akṣarabrahma Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
