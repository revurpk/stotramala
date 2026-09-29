# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 17 (Śraddhātrayavibhāga Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 17 · Śraddhātrayavibhāga Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 17",
    "h1": "Bhagavad Gītā · Chapter 17",
    "subtitle": "Śraddhātrayavibhāga Yoga · the three kinds of faith · with Śaṅkara's bhāṣya",
    "note": "The threefold faith, according to the guṇas, and the threefold forms of food, sacrifice, austerity and giving; the chapter ends with the formula oṃ tat sat, by which acts are consecrated.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 16', 'gita-bhashya-16-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 18 ›', 'gita-bhashya-18-iast.html')],
    "sections": [
        {"bhashya": [
            "“tasmācchāstraṃ pramāṇaṃ te” iti bhagavadvākyāt labdhapraśnabījaḥ arjuna uvāca –",
        ], "summary": "bhāṣya · the chapter's opening"},
        {"speaker": "arjuna uvāca"},
        _v([
            "ye śāstravidhimutsṛjya yajante śraddhayā'nvitāḥ |",
            "teṣāṃ niṣṭhā tu kā kṛṣṇa sattvamāhorajastamaḥ",
        ], "|| 1 ||",
           "Arjuna said: Those who set aside the injunctions of scripture yet sacrifice with faith — what is their standing, Kṛṣṇa? Is it sattva, rajas or tamas?",
           bhashya=[
               "ye iti. ye kecit aviśeṣitāḥ śāstravidhiṃ śāstravidhānaṃ śrutismṛti śāstra codanāṃ utsṛjya parityajya yajante devādīn pūjayanti śraddhayā anvitāḥ śraddhayā āstikyabuddhyā anvitāḥ saṃyuktāḥ santaḥ śrutilakṣaṇaṃ smṛtilakṣaṇaṃ vā kañcit śāstravidhiṃ apaśyantaḥ vṛddhavyavahāradarśanādeva śraddhānatayā ye devādīn pūjayanti te iha “ye śāstravidhimutsṛjya yajante śraddhayā'nvitāḥ” ityevaṃ gṛhyante. ye punaḥ kañcit śāstravidhiṃ upalabhamānā eva taṃ utsṛjya ayathāvidhi devādīn pūjayanti te iha “ye śāstravidhimutsṛjya yajante” iti na parigṛhyante. kasmāt? śraddhayā anvitatvaviśeṣaṇāt. devādipūjāvidhiparaṃ kiñcit śāstraṃ paśyanta eva tat utsṛjya aśraddhānatayā tadvihitāyāṃ devādipūjāyāṃ śraddhayā anvitāḥ pravartante iti na śakyaṃ kalpayituṃ yasmāt, tasmāt pūrvoktā eva “ye śāstravidhimutsṛjya yajante śraddhayā'nvitāḥ” ityatra gṛhyante. teṣāṃ evambhūtānāṃ niṣṭhā tu avasthānaṃ kā kṛṣṇa! sattvaṃ āho rajaḥ tamaḥ, kiṃ sattvaṃ niṣṭhā avasthānaṃ, āhosvit rajaḥ, athavā tamaḥ iti? etat uktaṃ bhavati – yā teṣāṃ devādiviṣayā pūjā, sā kiṃ sāttvikī āhosvit rājasī, uta tāmasī iti?",
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "trividhā bhavati śraddhā dehināṃ sā svabhāvajā |",
            "sāttvikī rājasī caiva tāmasī ceti tāṃ śṛṇu",
        ], "|| 2 ||",
           "The Blessed Lord said: The faith of embodied beings, born of their own nature, is threefold — sāttvika, rājasa and tāmasa. Hear of it.",
           bhashya=[
               {"text": "sāmānyaviṣayaḥ ayaṃ praśnaḥ na apravibhajya prativacanaṃ arhatīti śrī", "intro": True},
               "trividheti. trividhā triprakārā bhavati śraddhā, yasyāṃ niṣṭhāyāṃ tvaṃ pṛcchasi, dehināṃ śarīriṇāṃ sā svabhāvajā, janmāntarakṛtadharmādisaṃskārāḥ maraṇakāle abhivyaktaḥ “svabhāvaḥ” ucyate, tato jātā svabhāvajā, sāttvikī sattva nirvṛttā devapūjādiviṣayā. rājasī rajonirvṛttā yakṣarakṣaḥpūjādiviṣayā, tāmasī tamonirvṛttā preta piśācādi pūjādiviṣayā, evaṃ trividhāṃ tāmucyamānāṃ śraddhāṃ śṛṇu avadhāraya.",
           ]),
        _v([
            "sattvānurūpā sarvasya śraddhā bhavati bhārata |",
            "śraddhāmayo'yaṃ puruṣaḥ yo yacchraddhassa eva saḥ",
        ], "|| 3 ||",
           "The faith of each is in keeping with his inner being, O Bhārata. A person is made of faith; as his faith is, so is he.",
           bhashya=[
               {"text": "sā iyaṃ trividhā bhavati –", "intro": True},
               "sattvānurūpā viśiṣṭasaṃskāropetāntaḥkaraṇānurūpā sarvasya prāṇijātasya śraddhā bhavati, bhārata. yadyevaṃ tataḥ kiṃ syāditi, ucyate, śraddhāmayaḥ ayaṃ śraddhāprāyaḥ puruṣaḥ saṃsārī jīvaḥ, kathaṃ? yaḥ yacchraddhaḥ yā śraddhā yasya jīvasya, saḥ yacchraddhaḥ sa eva tacchraddhānurūpa eva saḥ jīvaḥ.",
           ]),
        _v([
            "yajante sāttvikā devān yakṣarakṣāṃsi rājasāḥ |",
            "pretān bhūtagaṇāṃścānye yajante tāmasā janāḥ",
        ], "|| 4 ||",
           "The sāttvika worship the gods; the rājasa worship yakṣas and rākṣasas; and the others, tāmasa people, worship ghosts and hosts of spirits.",
           bhashya=[
               {"text": "tataśca kāryeṇa liṅgena devādipūjayā sattvādi niṣṭhā anumeyā ityāha.", "intro": True},
               "yajante pūjayanti sāttvikāḥ sattvaniṣṭhāḥ devān, yakṣarakṣāṃsi rājasāḥ, pretān bhūtagaṇāṃśca saptamātṛkādīṃśca anye yajante tāmasāḥ janāḥ.",
           ]),
        _v([
            "aśāstravihitaṃ ghoraṃ tapyante ye tapo janāḥ |",
            "dambhāhaṅkārasaṃyuktāḥ kāmarāgabalānvitāḥ",
        ], "|| 5 ||",
           "Those people who practise terrible austerities not enjoined by scripture, given to hypocrisy and egoism, driven by the force of desire and passion,",
           bhashya=[
               {"text": "evaṃ kāryato nirṇītaḥ sattvādiniṣṭhāḥ śāstravidhyutsarge. tatra kaścideva sahasreṣu devapūjādiparaḥ. sattvaniṣṭho bhavati, bāhulyena tu rajoniṣṭhāḥ tamoniṣṭhāścaiva prāṇino bhavanti. kathaṃ?", "intro": True},
               "aśāstravihitanna śāstravihitaṃ ghoraṃ pīḍākaraṃ prāṇināmātmanaśca tapaḥ tapyante nirvartayanti ye tapo janāḥ, te ca dambhāhaṅkārasaṃyuktāḥ, dambhaśca ahaṅkāraśca dambhāhaṅkārau, tābhyāṃ saṃyuktāḥ dambhāhaṅkārasaṃyuktāḥ, kāmarāgabalānvitāḥ kāmaśca rāgaśca kāmarāgau tatkṛtaṃ balaṃ kāmarāgabalaṃ tena anvitāḥ kāmarāgabalānvitāḥ.",
           ]),
        _v([
            "karśayantaśśarīrasthaṃ bhūtagrāmamacetasaḥ |",
            "māṃ caivāntaḥ śarīrasthaṃ tān viddhyāsuraniścayān",
        ], "|| 6 ||",
           "senseless, tormenting the aggregate of elements in the body, and me too who dwell within the body — know them to be of demonic resolve.",
           bhashya=[
               "karśayantaḥ kṛśīkurvantaḥ, śarīrasthaṃ bhūtagrāmaṃ karaṇasamudāyaṃ, acetasaḥ avivekinaḥ, māṃ caiva tatkarmabuddhisākṣibhūtaṃ antaśśarīrasthaṃ nārāyaṇaṃ karśayantaḥ, madanuśāsanākaraṇameva matkarśanaṃ, tān viddhi āsuraniścayān, āsuro niścayo yeṣāṃ te āsuraniścayāḥ, tān pariharaṇārthaṃ viddhi iti upadeśaḥ.",
           ]),
        _v([
            "āhārastvapi sarvasya trividho bhavati priyaḥ |",
            "yajñastapastathā dānaṃ teṣāṃ bhedamimaṃ śṛṇu",
        ], "|| 7 ||",
           "Even the food that is dear to each is of three kinds, and so are sacrifice, austerity and giving. Hear the distinction between them.",
           bhashya=[
               {"text": "āhārādīnāṃ ca rasyasnigdhādivargatrayarūpeṇa bhinnānāṃ yathākramaṃ sāttvika rājasatāmasa puruṣapriyatvapradarśanaṃ iha kriyate – rasyasnigdhādiṣu āhāraviśeṣeṣu ātmanaḥ prītyatirekeṇa liṅgena sāttvikatvaṃ rājasatvaṃ ca buddhvā rajastamoliṅgānāmāhārāṇāṃ parivarjanārthaṃ sattvaliṅgānāṃ copādanārthaṃ. tathā yajñādīnāmapi sattvādiguṇabhedena trividhatva pratipādanaṃ iha “rājasatāmasān buddhvā kathaṃ nu nāma parityajet, sāttvikāneva anutiṣṭhet” ityevamarthaṃ āha.", "intro": True},
               "āhārastvapi sarvasya bhoktuḥ prāṇinaḥ trividho bhavati priyaḥ iṣṭaḥ, tathā yajñaḥ, tathā tapaḥ tathā dānaṃ. teṣāṃ āhārādīnāṃ bhedamimaṃ vakṣyamāṇaṃ śṛṇu.",
           ]),
        _v([
            "āyussattvabalārogyasukhaprītivivardhanāḥ |",
            "rasyāḥ snigdhāḥ sthirā hṛdyā āhārāssāttvikapriyāḥ",
        ], "|| 8 ||",
           "Foods that increase life, vigour, strength, health, happiness and cheerfulness, that are savoury, rich, nourishing and agreeable, are dear to the sāttvika.",
           bhashya=[
               "āyuśca sattvaṃ ca balaṃ ca ārogyaṃ ca sukhaṃ ca prītiśca āyussattvabalārogya sukhaprītayaḥ tāsāmāyussattvādīnāṃ vivardhanāḥ āyussattvabalārogyasukhaprīti vivardhanāḥ, te ca rasyāḥ rasopetāḥ, snigdhāḥ snehavantaḥ, sthirāḥ cirakālasthāyinaḥ dehe, hṛdyāḥ hṛdayapriyāḥ āhārāḥ sāttvikapriyāḥ sāttvikasya iṣṭāḥ.",
           ]),
        _v([
            "kaṭvamlalavaṇātyuṣṇatīkṣṇarūkṣavidāhinaḥ |",
            "āhārā rājasasyeṣṭā duḥkhaśokāmayapradāḥ",
        ], "|| 9 ||",
           "Foods that are bitter, sour, salty, very hot, pungent, dry and burning, which cause pain, grief and sickness, are dear to the rājasa.",
           bhashya=[
               "kaṭvamlalavaṇātyuṣṇa tīkṣa rūkṣa vidāhinaḥ ityatra ati śabdaḥ kaṭvādiṣu sarvatra yojyaḥ, ati kaṭuḥ atitīkṣaḥ ityevaṃ kaṭuśca amlaśca lavaṇaśca atyuṣṇaśca ati tīkṣaśca rūkṣaśca vidāhī ca te āhārāḥ rājasasyeṣṭāḥ duḥkhaśokāmayapradāḥ duḥkhaṃ ca śokaṃ ca āmayaṃ ca prayacchantīti duḥkhaśokāmayapradāḥ.",
           ]),
        _v([
            "yātayāmaṃ gatarasaṃ pūti paryuṣitaṃ ca yat |",
            "ucchiṣṭamapi cāmedhyaṃ bhojanaṃ tāmasapriyam",
        ], "|| 10 ||",
           "Food that is stale, tasteless, putrid and left overnight, leftovers and what is impure, is dear to the tāmasa.",
           bhashya=[
               "yātayāmaṃ mandapakvaṃ nirvīryasya gatarasaśabdenoktatvāt. gatarasaṃ rasaviyuktaṃ, pūti durgandhi, paryuṣitaṃ ca pakvaṃ sat rātryantaritaṃ ca yat, ucchiṣṭamapi bhuktaśiṣṭamucchiṣṭaṃ, amedhyaṃ ayajñārhaṃ, bhojanam īdṛśaṃ tāmasapriyam.",
           ]),
        _v([
            "aphalākāṅkṣibhiryajño vidhidṛṣṭo ya ijyate |",
            "yaṣṭavyameveti manaḥ samādhāya sa sāttvikaḥ",
        ], "|| 11 ||",
           "Sacrifice offered according to the rule by those who desire no fruit, with the mind fixed on the thought that it simply ought to be done, is sāttvika.",
           bhashya=[
               {"text": "adha idānīṃ yajñaḥ trividha ucyate –", "intro": True},
               "aphalākāṅkṣibhiḥ aphalārthibhiḥ yajñaḥ vidhidṛṣṭaḥ śāstracodanādṛṣṭaḥ yaḥ yajñaḥ ijyate nirvartyate, yaṣṭavyameveti yajñasvarūpanirvartanameva kāryamiti manassamādhāya, nānena puruṣārtho mama kartavya ityevaṃ niścitya, saḥ sāttviko yajña ucyate.",
           ]),
        _v([
            "abhisandhāya tu phalaṃ dambhārthamapi caiva yat |",
            "ijyate bharataśreṣṭha taṃ yajñaṃ viddhi rājasam",
        ], "|| 12 ||",
           "But know, O best of the Bhāratas, that sacrifice offered with an eye to its fruit, or for display, is rājasa.",
           bhashya=[
               "abhisandhāya tu uddiśya phalaṃ, dambhārthamapicaiva yadijyate, bharataśreṣṭha, taṃ yajñaṃ viddhi rājasam.",
           ]),
        _v([
            "vidhihīnamasṛṣṭānnaṃ mantrahīnamadakṣiṇam |",
            "śraddhāvirahitaṃ yajñaṃ tāmasaṃ paricakṣate",
        ], "|| 13 ||",
           "Sacrifice without regard to the rule, in which no food is distributed, without mantras, without gifts to the priests and without faith, is called tāmasa.",
           bhashya=[
               "vidhihīnaṃ yathācoditaviparītaṃ, asṛṣṭānnaṃ brāhmaṇebhyo na sṛṣṭaṃ na dattamannaṃ yasmin yajñe saḥ asṛṣṭānnaḥ taṃ asṛṣṭānnaṃ, mantrahīnaṃ mantrataḥ svarataḥ varṇato vā viyuktaṃ mantrahīnaṃ, adakṣiṇaṃ uktadakṣiṇārahitaṃ, śraddhāvirahitaṃ yajñaṃ tāmasaṃ paricakṣate tamonirvṛttaṃ kathayanti.",
           ]),
        _v([
            "devadvijaguruprājñapūjanaṃ śaucamārjavam |",
            "brahmacaryamahiṃsā ca śārīraṃ tapa ucyate",
        ], "|| 14 ||",
           "Worship of the gods, the twice-born, teachers and the wise; purity, uprightness, celibacy and non-violence — this is called austerity of the body.",
           bhashya=[
               {"text": "athedānīṃ tapaḥ trividhamucyate –", "intro": True},
               "devāśca dvijāśca guravaśca prāṅjāśca devadvijaguruprājñāḥ teṣāṃ pūjanaṃ devadvijaguru prājñapūjanaṃ, śaucaṃ, ārjavaṃ, ṛjutvaṃ brahmacaryamahiṃsā ca śarīranirvartyaṃ śārīraṃ śarīrapradhānaiḥ sarvaireva kāryakaraṇaiḥ kartrādibhiḥ sādhyaṃ śārīraṃ tapaḥ ucyate. “pañcaite tasya hetavaḥ” iti vakṣyati.",
           ]),
        _v([
            "anudvegakaraṃ vākyaṃ satyaṃ priyahitaṃ ca yat |",
            "svādhyāyābhyasanaṃ caiva vāṅmayaṃ tapa ucyate",
        ], "|| 15 ||",
           "Speech that causes no agitation, that is truthful, pleasant and beneficial, and the practice of study of scripture — this is called austerity of speech.",
           bhashya=[
               "anudvegakaraṃ prāṇināṃ aduḥkhakaraṃ vākyaṃ satyaṃ priyahitaṃ ca yat – priyahite dṛṣṭādṛṣṭārthe. anudvegakaratvādibhiḥ dharmaiḥ vākyaṃ viśeṣyate. viśeṣaṇadharmasamuccayārthaṃ caśabdaḥ. parapratyayārthaṃ prayuktasya vākyasya satyapriyahitānudvegakaratvānāṃ anyatamena dvābhyāṃ tribhirvāhīnatā syādyadi, na tat vāṅmayaṃ tapaḥ. tathā satyavākyasya itareṣāṃ anyatamena dvābhyāṃ tribhirvā vihīnatāyāṃ na vāṅmayatapastvam. tathā priyavākyasyāpi itareṣāṃ anyatamena dvābhyāṃ tribhirvā vihīnasya na vāṅmayatapastvam. tathā hitavākyasyāpi itareṣāṃ anyatamena dvābhyāṃ tribhirvā vihīnasya na vāṅmayatapastvam. kiṃ punaḥ tat tapaḥ? yat satyaṃ vākyaṃ anudvegakaraṃ priyaṃ hitaṃ ca tat tapaḥ vāṅmayaṃ, yathā “śāntobhava vatsa! svādhyāyaṃ yogaṃ ca anutiṣṭha. tathā te śreyo bhaviṣyati” iti. svādhyāyābhyasanaṃ ca eva yathāvidhi vāṅmayaṃ tapaḥ ucyate.",
           ]),
        _v([
            "manaḥprasādaḥ saumyatvaṃ maunamātma vinigrahaḥ |",
            "bhāvasaṃśuddhirityetattapo mānasamucyate",
        ], "|| 16 ||",
           "Serenity of mind, gentleness, silence, self-restraint and purity of disposition — this is called austerity of the mind.",
           bhashya=[
               "manaḥ prasādaḥ manasaḥ praśāntiḥ svacchatāpādanaṃ prasādaḥ, saumyatvaṃ yatsaumanasyamāhuḥ, mukhādiprasādādikāryonneyā antaḥkaraṇasya vṛttiḥ. maunaṃ vāksaṃyamo'pi manassaṃyamapūrvako bhavati iti kāryeṇa kāraṇaṃ ucyate manassaṃyamo maunamiti, ātmavinigrahaḥ manonirodhaḥ sarvataḥ sāmānyarūpaḥ ātmavinigrahaḥ, vāgviṣayasyaiva manasaḥ saṃyamaḥ maunaṃ, iti viśeṣaḥ. bhāvasaṃśuddhiḥ – paraiḥ vyavahārakāle amāyāvitvaṃ bhāvasaṃśuddhiḥ, ityetat tapaḥ mānasaṃ ucyate.",
           ]),
        _v([
            "śraddhayā parayā taptaṃ tapastattrividhaṃ naraiḥ |",
            "aphalākāṅkṣibhiryuktaiḥ sāttvikaṃ paricakṣate",
        ], "|| 17 ||",
           "This threefold austerity, practised with supreme faith by disciplined people who desire no fruit, is called sāttvika.",
           bhashya=[
               {"text": "yathoktaṃ kāyikaṃ vācikaṃ mānasaṃ ca tapaḥ taptaṃ naraiḥ sattvādiguṇabhedena kathaṃ trividhaṃ bhavatīti, ucyate –", "intro": True},
               "śraddhayā āstikyabuddhyā parayā prakṛṣṭayā taptaṃ anuṣṭhitaṃ tapaḥ tat prakṛtaṃ trividhaṃ triprakāraṃ tryadhiṣṭhānaṃ naraiḥ anuṣṭhātṛbhiḥ aphalākāṅkṣibhiḥ phalākāṅkṣārahitaiḥ yuktaiḥ samāhitaiḥ – yat īdṛśaṃ tapaḥ, tat sāttvikaṃ sattvanirvṛttaṃ paricakṣate kathayanti śiṣṭāḥ.",
           ]),
        _v([
            "satkāramānapūjārthaṃ tapo dambhena caiva yat |",
            "kriyate tadiha proktaṃ rājasaṃ calamadhruvam",
        ], "|| 18 ||",
           "Austerity practised for the sake of respect, honour and reverence, and with hypocrisy, is here called rājasa; it is unstable and fleeting.",
           bhashya=[
               "satkāraḥ sādhukāraḥ “sādhuḥ ayaṃ tapasvī brāhmaṇaḥ” ityevamarthaṃ, māno mānanaṃ pratyutthānābhivādanādiḥ tadarthaṃ pūjā pādaprakṣālanārcanāśayitṛtvādi tadarthaṃ ca tapaḥ satkāramānapūjārthaṃ, dambhena caiva yatkriyate tapaḥ tat iha proktaṃ kathitaṃ rājasaṃ calaṃ kādācitkaphalatvena adhruvam.",
           ]),
        _v([
            "mūḍhagrāheṇātmano yat pīḍayā kriyate tapaḥ |",
            "parasyotsādanārthaṃ vā tattāmasamudāhṛtam",
        ], "|| 19 ||",
           "Austerity practised out of a deluded notion, with self-torture, or for the purpose of harming another, is called tāmasa.",
           bhashya=[
               "mūḍhagrāheṇa aviveka niścayena ātmanaḥ pīḍayā yat kriyate tapaḥ parasya utsādanārthaṃ vināśārthaṃ vā tat tāmasaṃ tapaḥ udāhṛtam.",
           ]),
        _v([
            "dātavyamiti yaddānaṃ dīyate'nupakāriṇe |",
            "deśe kāle ca pātre ca taddānaṃ sāttvikaṃ smṛtam",
        ], "|| 20 ||",
           "A gift given because it ought to be given, to one who cannot return it, at the right place and time and to a worthy person, is held to be sāttvika.",
           bhashya=[
               {"text": "idānīṃ dānatraividhyaṃ ucyate –", "intro": True},
               "dātavyamityevaṃ manaḥ kṛtvā yaddānaṃ dīyate anupakāriṇe pratyupakārāsamarthāya, samarthāyāpi nirapekṣaṃ dīyate, deśe puṇyadeśe kurukṣetrādau, kāle saṅkrāntyādau, pātre ca ṣaḍaṅgavidvedapārage ityādau, taddānaṃ sāttvikaṃ smṛtam.",
           ]),
        _v([
            "yattu pratyupakārārthaṃ phalamuddiśya vā punaḥ |",
            "dīyate ca parikliṣṭaṃ taddānaṃ rājasaṃ smṛtam",
        ], "|| 21 ||",
           "But a gift given in expectation of a return, or with an eye to its fruit, or grudgingly, is held to be rājasa.",
           bhashya=[
               "yattu dānaṃ pratyupakārārthaṃ kāle tu ayaṃ māṃ pratyupakariṣyati ityevamarthaṃ, phalaṃ vā asya dānasya me bhaviṣyati adṛṣṭamiti, tat uddiśya punaḥ dīyate ca parikliṣṭaṃ khedasaṃyuktaṃ taddānaṃ rājasaṃ smṛtam.",
           ]),
        _v([
            "adeśakāle yaddānamapātrebhyaśca dīyate |",
            "asatkṛtamavajñātaṃ tattāmasamudāhṛtam",
        ], "|| 22 ||",
           "A gift given at the wrong place and time, to unworthy persons, without respect or with contempt, is called tāmasa.",
           bhashya=[
               "adeśakāle adeśe apuṇyadeśe mlecchā śucyādi saṅkīrṇe akāle puṇyahetutvena aprakhyāte saṅkrāntyādiviśeṣarahite apātrebhyaśca mūrkhataskarādibhyaḥ, deśādi sampattau vā asatkṛtaṃ priyavacana pādaprakṣālanapūjādirahitaṃ avajñātaṃ pātraparibhavayuktaṃ ca yat, taddānaṃ tāmasamudāhṛtam.",
           ]),
        _v([
            "ontatsaditi nirdeśo brahmaṇastrividhaḥ smṛtaḥ |",
            "brāhmaṇāstena vedāśca yajñāśca vihitāḥ purā",
        ], "|| 23 ||",
           "'Oṃ tat sat' — this is held to be the threefold designation of Brahman. By it the brāhmaṇas, the Vedas and sacrifices were ordained of old.",
           bhashya=[
               {"text": "yajñadānatapaḥ prabhṛtīnāṃ sādguṇyakaraṇāya ayamupadeśa ucyate–", "intro": True},
               "oṃ tatsat ityevaṃ nirdeśaḥ, nirdiśyate aneneti nirdeśaḥ, trividho nāmanirdeśaḥ brahmaṇaḥ smṛtaḥ cintitaḥ vedānteṣu brahmavidbhiḥ, brāhmaṇāḥ tena nirdeśena trividhena vedāśca yajñāśca vihitāḥ nirmitāḥ purā pūrvaṃ iti nirdeśastutyarthaṃ ucyate.",
           ]),
        _v([
            "tasmādomityudāhṛtya yajñadānatapaḥkriyāḥ |",
            "pravartante vidhānoktāḥ satataṃ brahmavādinām",
        ], "|| 24 ||",
           "Therefore the acts of sacrifice, giving and austerity prescribed by the rule are always begun by the expounders of Brahman after uttering 'Om'.",
           bhashya=[
               "tasmāt “om” iti udāhṛtya uccārya yajñadānatapaḥ kriyāḥ yajñādi svarūpāḥ kriyāḥ pravartante vidhānoktāḥ śāstracoditāḥ satataṃ sarvadā brahmavādināṃ brahmavadana śīlānām.",
           ]),
        _v([
            "tadityanabhisandhāya phalaṃ yajñatapaḥkriyāḥ |",
            "dānakriyāśca vividhāḥ kriyante mokṣakāṅkṣibhiḥ",
        ], "|| 25 ||",
           "With 'tat', and without aiming at fruit, acts of sacrifice and austerity and various acts of giving are performed by those who seek liberation.",
           bhashya=[
               "tat iti anabhisandhāya “tat iti brahmābhidhānamuccārya anabhisandhāya ca yajñādi karmaṇaḥ phalaṃ, yajñatapaḥ kriyāḥ yajñakriyāśca tapaḥkriyāśca yajñatapaḥ kriyāḥ dānakriyāśca vividhāḥ kṣetra hiraṇyapradānādi lakṣaṇāḥ kriyante nirvartyante mokṣakāṅkṣibhiḥ mokṣārthibhiḥ mumukṣubhiḥ.",
           ]),
        _v([
            "sadbhāve sādhubhāve ca sadityetatprayujyate |",
            "praśaste karmaṇi tathā sacchabdaḥ pārtha yujyate",
        ], "|| 26 ||",
           "'Sat' is used in the sense of reality and of goodness; and the word 'sat' is likewise used, Pārtha, of a praiseworthy act.",
           bhashya=[
               {"text": "oṃ tacchabdayoḥ viniyogaḥ uktaḥ. atha idānīṃ sacchabdasya viniyoga ucyate –", "intro": True},
               "sadbhāve, asataḥ sadbhāve yathā avidyamānasya putrasya janmani, tathā sādhubhāve ca asadvṛttasya asādhossadvṛttatā sādhubhāvaḥ tasmin sādhubhāve ca sat ityetadabhidhānaṃ brahmaṇaḥ prayujyate abhidhīyate. praśaste karmaṇi vivāhādau ca tathā sacchabdaḥ pārtha! yujyate prayujyate ityetat.",
           ]),
        _v([
            "yajñe tapasi dāne ca sthitiḥ saditi cocyate |",
            "karma caiva tadarthīyaṃ sadityevābhidhīyate",
        ], "|| 27 ||",
           "Steadfastness in sacrifice, austerity and giving is also called 'sat', and any action for such purposes is likewise called 'sat'.",
           bhashya=[
               "yajñe yajñakarmaṇi yā sthitiḥ, tapasi ca yā sthitiḥ dāne ca yā sthitiḥ, sā saditi cocyate vidvadbhiḥ. karmacaiva tadarthīyaṃ yajñadānatapo'rthīyaṃ athavā yasya abhidhānatrayaṃ prakṛtaṃ tadarthīyaṃ īśvarārthīyamityetat, sadityevābhidhīyate tadetadyajñadānatapa ādi karma asāttvikaṃ viguṇamapi śraddhāpūrvakaṃ brahmaṇaḥ abhidhānatrayaprayogeṇa saguṇaṃ sāttvikaṃ sampāditaṃ bhavati.",
           ]),
        _v([
            "aśraddhayā hutaṃ dattaṃ tapastaptaṃ kṛtaṃ ca yat |",
            "asadityucyate pārtha na ca tatpretya no iha",
        ], "|| 28 ||",
           "Whatever is offered, given, or done as austerity or as a rite without faith is called 'asat', Pārtha; it is of no avail here or hereafter.",
           bhashya=[
               {"text": "tatra ca sarvatra śraddhāpradhānatayā sarvaṃ sampādyate yasmāt, tasmāt.", "intro": True},
               "aśraddhayā hutaṃ havanaṃ kṛtaṃ, aśraddhayā dattaṃ brāhmaṇebhyaḥ, tathā aśraddhayā tapaḥ taptaṃ anuṣṭhitaṃ, tathā aśraddhayaiva kṛtaṃ ca yat stutinamaskārādi, tat sarvaṃ asadityucyate, matprāptisādhana mārgabāhyatvāt, he pārtha, na ca tat bahulāyāsamapi pretya phalāya no'pi ihārthaṃ, sādhubhiḥ ninditatvāditi.",
           ]),
        "ornament",
        {"colophon": "iti śrī mahābhārate śatasāhasryāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsūpaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjunasaṃvāde śraddhātrayavibhāgayogonāma saptadaśo– dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the seventeenth chapter, Śraddhātrayavibhāga Yoga."},
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryagovindabhagavatpūjyapādaśiṣyaśrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhagavadgītābhāṣye śraddhātrayavibhāgayogo nāma saptadaśo'dhyāyaḥ.", "gloss": "Thus ends the seventeenth chapter, Śraddhātrayavibhāga Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
