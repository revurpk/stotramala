# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 6 (Dhyāna Yoga), with Śaṅkara's bhāṣya. The Sanskrit
# (mūla and bhāṣya, both public domain) is converted from the text layer of
# the Ramakrishna Math, Hyderabad edition (2013), whose legacy Telugu font was
# mapped to Unicode glyph by glyph; its Telugu translation is not used. Collated
# against Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; every
# correction is logged in SOURCES §7.4. The English of the verses and of the
# bhāṣya is original, made from the Sanskrit. Generated from the collated text — edit here, not
# upstream.


def _v(padas, num, gloss, bhashya=None):
    d = {"padas": padas, "num": num, "gloss": gloss}
    if bhashya:
        d["bhashya"] = bhashya
    return d


STOTRA = {
    "deity": "gita",
    "doc_title": "Bhagavad Gītā 6 · Dhyāna Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 6",
    "h1": "Bhagavad Gītā · Chapter 6",
    "subtitle": "Dhyāna Yoga · the yoga of meditation · with Śaṅkara's bhāṣya",
    "note": "The discipline of meditation: the true renouncer, the self as one's own friend or foe, the seat, posture and mind of the meditator, the steady flame in a windless place, and the fate of one who falls from yoga — for whom, Kṛṣṇa promises, there is no ruin.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('‹ chapter 5', 'gita-bhashya-05-iast.html'), ('all chapters', '../../index.html#gita'), ('chapter 7 ›', 'gita-bhashya-07-iast.html')],
    "sections": [
        {"bhashya": [
            {"text": "atītānantarādhyāyānte dhyānayogasya samyag darśanaṃ prati antaraṅgasya sūtrabhūtāḥ ślokāḥ “sparśān kṛtvā bahiḥ” (5.27.29) ityādayaḥ upadiṣṭāḥ, teṣāṃ vṛttisthānīyaḥ ayaṃ ṣaṣṭho'dhyāyaḥ ārabhyate. tatra dhyānayogasya bahiraṅgaṃ karma iti, yāvat dhyānayogārohaṇāsamarthaḥ tāvat gṛhasthena adhikṛtena kartavyaṃ karma ityataḥ tat stauti anāśritaḥ iti.", "tr": "At the end of the preceding chapter, verses such as 'shutting out external contacts' (5.27–29) were taught as aphorisms of the yoga of meditation, the inner discipline of right vision; this sixth chapter begins as their gloss. Since action is the outer discipline of the yoga of meditation, and must be done by a householder who is qualified for it as long as he is unable to ascend to the yoga of meditation, he praises it with 'not depending'."},
            {"text": "nanu kimarthaṃ dhyānayogārohaṇa sīmākaraṇam yāvatā anuṣṭheyameva vihitaṃ karma yāvajjīvam?– na, “ārurukṣormuneryogaṃ karma kāraṇamucyate” (6.3) iti viśeṣaṇāt, ārūḍhasya ca śamena eva sambandhakaraṇāt. ārurukṣoḥ ārūḍhasya ca śamaḥ karma ca ubhayaṃ kartavyatvena abhipretaṃ cet syāt tadā “ārurukṣoḥ”, “ārūḍhasya” ca iti śamakarma viṣayabhedena viśeṣaṇaṃ vibhāgakaraṇaṃ ca anarthakaṃ syāt. tatra āśramiṇāṃ kaścit yogam ārurukṣuḥ bhavati, ārūḍhaḥ ca kaścit, anye na ārurukṣavaḥ, na ārūḍhāḥ – tān pekṣya “ārurukṣoḥ” “ārūḍhasya” ca iti viśeṣaṇaṃ vibhāgakaraṇaṃ ca upapadyate eva iti cet – na, “tasyaiva” iti vacanāt punaḥ yogagrahaṇācca “yogārūḍhasya” iti; yaḥ āsīt pūrvaṃ yogam ārurukṣuḥ tasyaiva ārūḍhasya śamaḥ eva kartavyaḥ kāraṇaṃ yogaphalaṃ prati ucyate iti. ataḥ na yāvajjīvaṃ kartavyatvaprāptiḥ kasya cidapi karmaṇaḥ", "tr": "Objection: why set ascent to the yoga of meditation as a limit, when enjoined action must be done as long as one lives? No: because of the qualification 'for the sage who wishes to ascend to yoga, action is said to be the means' (6.3), and because calm alone is linked with one who has ascended. If both calm and action were meant as duties for both the one wishing to ascend and the one who has ascended, the qualifications 'of one wishing to ascend' and 'of one who has ascended', and the division of calm and action by their spheres, would be pointless. Objection: among those in the stages of life, some wish to ascend to yoga, some have ascended, and others neither wish to ascend nor have ascended; with reference to these, the qualifications and the division do make sense. No: because of the words 'of that same one', and because yoga is mentioned again in 'of one who has ascended to yoga'; it is said that for that same person who earlier wished to ascend to yoga, once he has ascended, calm alone is to be practised, the means to the fruit of yoga. Therefore no action whatever becomes a duty for as long as one lives."},
            {"text": "yogavibhraṣṭa vacanācca, gṛhasthasya cet karmiṇaḥ yogaḥ vihitaḥ ṣaṣṭhe adhyāye, saḥ yoga vibhraṣṭaḥ api karmagatiṃ, karmaphalaṃ prāpnoti iti tasya nāśāśaṅkā anupapannā syāt avaśyaṃ hi kṛtaṃ karma, kāmyaṃ nityaṃ vā mokṣasya nityatvāt anārabhyatve, svaṃ phalaṃ ārabhate eva. nityasya ca karmaṇaḥ veda pramāṇāvabuddhattvāt phalena bhavitavyam iti avocāma. (4.18) – anyathā vedasya anarthārthatva prasaṅgāt iti. na ca karmaṇi sati ubhayavibhraṣṭa vacanam arthavat. karmaṇaḥ vibhraṃśakāraṇānupapatteḥ. karma kṛtam īśvare sannyasya (sannyastam) ityataḥ kartari karma phalaṃ nārabhate iti cet – na, īśvare sannyāsasya adhikatara phalahetutvopapatteḥ mokṣāya eva iti cet – svakarmaṇāṃ kṛtānām īśvare nyāsaḥ mokṣāyaiva, na phalāntarāya yogasahitaḥ, yogācca vibhraṣṭaḥ, ityataḥ taṃ prati nāśāśaṅkā yuktaiva iti cet – na, “ekākī yata cittātmā nirāśīraparigrahaḥ” (6.10), “brahmacārivrate sthitaḥ” (6.14) iti ca karmasannyāsa'vidhānāt. na ca atra dhyānakāle strī sahāyakatvāśaṅkā yena ekākitvaṃ vidhīyate. na ca gṛhasthasya “nirāśīraparigrahaḥ” (6.10) ityādivacanam anukūlam. ubhayavibhraṣṭa praśnānu'papatteḥ ca (6.38).", "tr": "And from the mention of one who has fallen from yoga: if yoga were enjoined in the sixth chapter for a householder engaged in action, then even if he fell from yoga he would gain the course of action, the fruit of action, and the fear of his ruin would be groundless; for action done, desire-prompted or obligatory, necessarily produces its own fruit — liberation, being eternal, cannot be produced. And we have said that obligatory action, being known through the authority of the Veda, must have a fruit (4.18); otherwise the Veda would have to be useless. Nor, where there is action, does the phrase 'fallen from both' make sense, since there is no reason for action to be lost. Objection: action done is resigned to the Lord, so it does not produce its fruit for the doer. No: resigning it to the Lord would rather be a cause of a greater fruit. Objection: the resigning of one's own actions to the Lord is for liberation alone, not for another fruit, and is joined with yoga; and he has fallen from yoga — so the fear for his ruin is quite proper. No: because the renunciation of action is enjoined in 'alone, with mind and self restrained, without hope, without possessions' (6.10) and 'established in the vow of celibacy' (6.14). Nor is it to be suspected that at the time of meditation a wife would be his companion, so that being alone had to be enjoined; nor do words such as 'without hope, without possessions' (6.10) suit a householder. And the question about one fallen from both (6.38) would make no sense."},
            {"text": "“anāśritaḥ” ityanena karmiṇaḥ eva sannyāsitvaṃ yogitvaṃ ca uktaṃ, pratiṣiddhaṃ ca niragneḥ akriyasya ca sannyāsitvaṃ yogitvaṃ iti cet – na, dhyānayogaṃ prati bahiraṅgasya sataḥ karmaṇaḥ phalākāṅkṣāsannyāsa stutiparatvāt. na kevalaṃ niragniḥ akriyaḥ eva sannyāsī yogī ca. kiṃ tarhi karmī api – karmaphalāsaṅgaṃ sannyasya karmayogam anutiṣṭhan sattvaśuddhyarthaṃ, “saḥ sannyāsī ca yogī ca” bhavati. (6.1) iti stūyate na caikena vākyena karmaphalāsaṅgasannyāsastutiḥ caturthāśrama pratiṣedhaśca upapadyate. na ca prasiddhaṃ niragneḥ akriyasya paramārtha sannyāsinaḥ śrutismṛti purāṇetihāsa yogaśāstra vihitaṃ sannyāsitvaṃ yogitvaṃ ca pratiṣedhati bhagavān. svavacana virodhācca – “sarva karmāṇi manasā sannyasya... naiva kurvan na kārayan āste” (5.13), “maunī santuṣṭo yena kenacit, aniketaḥ sthiramatiḥ” (12.19), “vihāya kāmānyaḥ sarvān pumāṃścarati niḥspṛhaḥ” (2.71), “sarvārambhaparityāgī” (12.16) iti ca tatra bhagavatā svavacanāni darśitāni; taiḥ virudhyeta caturthāśrama pratiṣedhaḥ, tasmāt muneḥ yogam ārurukṣoḥ pratipannagārhasthyasya agnihotrādi karma phalanirapekṣam anuṣṭhīyamānaṃ dhyānayogārohaṇa sādhanatvaṃ sattvaśuddhidvāreṇa pratipadyatu iti “saḥ sannyāsī ca yogī ca” iti stūyate.", "tr": "Objection: by 'not depending' renunciation and yoga are said to belong to the man of action alone, and they are denied to one without fires and without rites. No: because the passage aims at praising the renunciation of craving for the fruit of action that is the outer discipline for the yoga of meditation. It is praised thus: not only is the one without fires and without rites a renouncer and a yogin; the man of action too, renouncing attachment to the fruit of action and practising the yoga of action for the purification of his mind, 'is a renouncer and a yogin' (6.1). Nor can one and the same sentence both praise the renunciation of attachment to fruit and deny the fourth stage of life. Nor does the Lord deny the renunciation and yoga of the true renouncer, without fires and without rites, which are well known and enjoined in śruti, smṛti, Purāṇa, Itihāsa and the yoga scriptures. And it would contradict his own words: 'renouncing all actions with the mind… neither acting nor causing action, he dwells' (5.13), 'silent, content with whatever comes, homeless, steady of mind' (12.19), 'the man who gives up all desires and moves about free of longing' (2.71), 'renouncing all undertakings' (12.16) — these words of the Lord himself would be contradicted by a denial of the fourth stage. Therefore the agnihotra and other actions, performed without regard to their fruit by a sage wishing to ascend to yoga who has taken up the householder's life, are praised as 'he is a renouncer and a yogin' so that he may understand them to be, through purification of the mind, a means of ascending to the yoga of meditation."},
        ], "summary": "bhāṣya · the chapter's opening"},
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "anāśritaḥ karmaphalaṃ kāryaṃ karma karoti yaḥ |",
            "sa sannyāsī ca yogī ca na niragnirna cākriyaḥ",
        ], "|| 1 ||",
           "The Blessed Lord said: He who does the action that ought to be done, without depending on its fruit, is a renouncer and a yogin — not one who merely gives up the sacred fire and ritual acts.",
           bhashya=[
               {"text": "anāśrita iti. anāśritaḥ – na āśritaḥ, kim? karmaphalaṃ – karmaṇaḥ phalaṃ karmaphalaṃ yat tat anāśritaḥ, karmaphala tṛṣṇārahitaḥ ityarthaḥ. yo hi karmaphale tṛṣṇāvān saḥ karmaphalam ataḥ āśritaḥ bhavati, ayaṃ tu tadviparītaḥ, ataḥ anāśritaḥ karmaphalam. evambhūtaḥ san kāryaṃ kartavyaṃ, nityaṃ kāmyaviparītam agnihotrādikaṃ, karma karoti nirvartayati, yaḥ kaścit īdṛśaḥ karmī saḥ karmyantarebhyaḥ viśiṣyate ityevamartham āha – saḥ sannyāsī ca yogī ca iti. sannyāsaḥ parityāgaḥ, saḥ yasya asti saḥ sannyāsī ca yogī ca – yogaḥ cittasamādhānaṃ, sa yasya asti saḥ yogī ca ityevaṃ guṇa sampannaḥ ayaṃ mantavyaḥ, na kevalaṃ niragniḥ akriya eva sannyāsī yogī ca – iti mantavyaḥ. nirgatāḥ agnayaḥ karmāṅgabhūtāḥ yasmāt saḥ niragniḥ, akriyaśca anagnisādhanā api avidyamānāḥ kriyāḥ tapodānādikāḥ yasya asau akriyaḥ.", "tr": "'Not depending…' Not depending — on what? On the fruit of action: free of thirst for the fruit of action, that is. He who thirsts for the fruit of action depends on it; this one is the opposite, so he does not depend on the fruit of action. Being so, whoever performs action that ought to be done — the obligatory, the opposite of desire-prompted, such as the agnihotra — such a man of action is superior to other men of action; to say this he says: 'he is a renouncer and a yogin'. Renunciation is giving up; he who has it is a renouncer; yoga is collectedness of mind; he who has it is a yogin. He is to be regarded as endowed with these qualities; it should not be thought that only one without fires and without rites is a renouncer and a yogin. Without fires: one from whom the fires that are auxiliaries of ritual have gone; without rites: one who has no rites, even those not requiring fire, such as austerity and charity."},
           ]),
        _v([
            "yaṃ sannyāsamiti prāhuryogaṃ taṃ viddhi pāṇḍava |",
            "na hyasannyastasaṅkalpo yogī bhavati kaścana",
        ], "|| 2 ||",
           "What they call renunciation, know that to be yoga, Pāṇḍava; for no one becomes a yogin without renouncing intention.",
           bhashya=[
               {"text": "nanu ca niragneḥ akriyasyaiva śrutismṛti yogaśāstreṣu sannyāsitvaṃ yogitvaṃ ca prasiddham. kathamiha sāgneḥ sakriyasya sannyāsitvaṃ yogitvaṃ ca aprasiddham ucyate iti? – naiṣa doṣaḥ, kayācit guṇavṛttyā ubhayasya sampipādayiṣitatvāt. tat katham? karmaphala saṅkalpa sannyāsāt sannyāsitvaṃ, yogāṅgatvena ca karmānuṣṭhānāt karmaphalasaṅkalpasya vā cittavikṣepahetoḥ parityāgāt yogitvaṃ ca iti gauṇam ubhayam; na punaḥ mukhyaṃ sannyāsitvaṃ yogitvaṃ ca abhipretam ityetam arthaṃ darśayitumāha –", "intro": True, "tr": "Objection: in śruti, smṛti and the yoga scriptures renunciation and yoga are well known to belong only to one without fires and without rites. How then are renunciation and yoga, which are not known to belong to one who keeps the fires and performs rites, ascribed to him here? This is no fault, for both are meant to be established in a secondary sense. How? Renunciation, because of the renunciation of the intention for the fruit of action; and yoga, because action is performed as an auxiliary of yoga, or because the intention for the fruit, which distracts the mind, has been given up — so both are secondary; primary renunciation and yoga are not meant. To show this he says:"},
               {"text": "yamiti. yaṃ sarvakarma tatphalaparityāgalakṣaṇaṃ paramārthasannyāsam sannyāsam iti prāhuḥ śrutismṛtividaḥ, yogaṃ karmānuṣṭhānalakṣaṇaṃ taṃ paramārthasannyāsaṃ viddhi jānīhi, he pāṇḍava, karmayogasya pravṛtti lakṣaṇasya tadviparītena nivṛttilakṣaṇena paramārthasannyāsena kīdṛśaṃ sāmānyam aṅgīkṛtya tadbhāvaḥ ucyate ityapekṣāyām idamucyate. asti paramārthasannyāsena sādṛśyaṃ kartṛdvārakaṃ karmayogasya. yaḥ hi paramārthasannyāsī saḥ tyaktasarvakarma sādhanatayā sarvakarmatatphalaviṣayaṃ saṅkalpaṃ pravṛtti hetukāmakāraṇaṃ sannyasyati. ayamapi karmayogī karma kurvāṇaḥ eva phalaviṣayaṃ saṅkalpaṃ sannyasyati ityevam arthaṃ darśayiṣyan āha – na, hi yasmāt asannyasta saṅkalpaḥ asannyasta aparityaktaḥ phalaviṣayaḥ saṅkalpaḥ abhisandhiḥ yena saḥ asannyastasaṅkalpaḥ, kaścana kaścidapi, karmī, yogī samādhānavān bhavati, na sambhavatītyarthaḥ, phalasaṅkalpasya cittavikṣepa hetutvāt. tasmāt yaḥ kaścana karmī sannyasta phalasaṅkalpaḥ bhavet, saḥ yogī samādhānavān avikṣiptacittaḥ bhavet, cittavikṣepahetoḥ phalasaṅkalpasya sannyastatvāt ityabhiprāyaḥ. evaṃ paramārtha sannyāsa karmayogayoḥ kartṛdvārakaṃ sannyā'sasāmānyam apekṣya “yaṃ sannyāsamiti prāhuryogaṃ taṃ viddhi pāṇḍava” iti karmayogasya stutyarthaṃ sannyāsatvam uktam.", "tr": "'What they call renunciation…' What the knowers of śruti and smṛti call renunciation — true renunciation, giving up all actions and their fruits — know that to be yoga, the performance of action, Pāṇḍava. If it is asked what common feature of the yoga of action, marked by activity, with its opposite, true renunciation, marked by withdrawal, is relied on in calling the one the other, it is said: the yoga of action has a resemblance to true renunciation through the agent. For the true renouncer, having given up all means of action, renounces the intention concerning all actions and their fruits, which is the cause of the desire that leads to activity; and the man of the yoga of action too, while doing action, renounces the intention concerning its fruit. To show this he says: for no one, no man of action whatever, who has not renounced intention — by whom the intention, the purpose, regarding the fruit has not been renounced, given up — becomes a yogin, collected; it is not possible, that is, because the intention for the fruit causes distraction of mind. Therefore whatever man of action has renounced the intention for the fruit would be a yogin, collected, with undistracted mind, since the intention for the fruit that causes distraction has been renounced — that is the purport. Thus, having regard to the common feature of renunciation through the agent in true renunciation and the yoga of action, the yoga of action is called renunciation in order to praise it: 'what they call renunciation, know that to be yoga, Pāṇḍava'."},
           ]),
        _v([
            "ārurukṣormuneryogaṃ karma kāraṇamucyate |",
            "yogārūḍhasya tasyaiva śamaḥ kāraṇamucyate",
        ], "|| 3 ||",
           "For the sage who wishes to ascend to yoga, action is said to be the means; for the same sage, once he has ascended, stillness is said to be the means.",
           bhashya=[
               {"text": "dhyānayogasya phalanirapekṣaḥ karmayogaḥ bahiraṅga sādhanam iti taṃ sannyāsatvena stutvā adhunā karmayogasya dhyānayogasādhanatvaṃ darśayati –", "intro": True, "tr": "Having praised the yoga of action, done without regard to fruit, as renunciation, since it is the outer means of the yoga of meditation, he now shows that the yoga of action is a means to the yoga of meditation:"},
               {"text": "ārurukṣoriti. ārurukṣoḥ āroḍhum icchataḥ – anārūḍhasya, dhyānayoge avasthātum aśaktasyaiva ityarthaḥ. kasya tasya ārurukṣoḥ? muneḥ, karmaphalasannyāsinaḥ ityarthaḥ. kim ārurukṣoḥ? yogaṃ, karmakāraṇaṃ sādhanam ucyate. yogārūḍhasya punaḥ tasyaiva, śamaḥ upaśamaḥ, sarvakarmabhyaḥ, nivṛttiḥ kāraṇaṃ, yogārūḍhasya sādhanam ucyate ityarthaḥ. yāvat yāvat karmabhyaḥ uparamate, tāvat tāvat nirāyāsasya jitendriyasya cittaṃ samādhīyate. tathā sati saḥ jhaṭiti yogārūḍho bhavati. tathā ca uktaṃ vyāsena – “naitādṛśaṃ brāhmaṇasyāsti vittaṃ yathaikatā samatā satyatā ca | śīlaṃ sthitirdaṇḍa nidhānamārjavaṃ tatastataścoparamaḥ kriyābhyaḥ || (śāṃ.pa. 175.38) iti.", "tr": "'For the sage who wishes to ascend…' For one who wishes to ascend — who has not ascended, who is not yet able to remain in the yoga of meditation, that is. Who is this one wishing to ascend? A sage: one who has renounced the fruit of action, that is. Wishing to ascend to what? To yoga; for him action is said to be the means. But for that same one, once he has ascended to yoga, calm — quiescence, withdrawal from all actions — is said to be the means for the one who has ascended to yoga. The more he withdraws from actions, the more the mind of the one free from toil and master of his senses becomes collected; and when that is so, he quickly becomes one who has ascended to yoga. And so Vyāsa has said: 'There is no wealth for a brāhmaṇa like oneness, sameness, truthfulness, good conduct, steadiness, laying aside the rod, straightforwardness, and withdrawal from rites step by step' (Śāntiparvan 175.38)."},
           ]),
        _v([
            "yadā hi nendriyārtheṣu na karmasvanuṣajjate |",
            "sarvasaṅkalpasannyāsī yogārūḍhastadocyate",
        ], "|| 4 ||",
           "When one is attached neither to the objects of the senses nor to actions, and has renounced all intention, then he is said to have ascended to yoga.",
           bhashya=[
               {"text": "atha idānīṃ kadā yogārūḍhaḥ bhavati iti ucyate –", "intro": True, "tr": "Now it is said when he becomes one who has ascended to yoga:"},
               {"text": "idi yadā – samādhīyamānacittaḥ yogī hi indriyārtheṣu indriyāṇām arthāḥ śabdādayaḥ teṣu indriyārtheṣu, karmasu ca nitya naimittika kāmyapratiṣiddheṣu, prayojanābhāvabuddhyā, na anuṣajjate anuṣaṅgaṃ kartavyatābuddhiṃ na karoti ityarthaḥ. sarvasaṅkalpasannyāsī sarvān saṅkalpān ihāmutrārthakāmahetūn sannyasituṃ śīlam asya iti sa sarvasaṅkalpasannyāsī, yogārūḍhaḥ, prāptayogaḥ ityetat, tadā tasminkāle, ucyate. “sarvasaṅkalpasannyāsī” iti vacanāt sarvāṃśca kāmān sarvāṇi ca karmāṇi sannyaset ityarthaḥ. saṅkalpamūlāḥ hi sarve kāmāḥ – “saṅkalpamūlaḥ kāmo vai yajñāḥ saṅkalpasambhavāḥ” (manu.smṛ. 2.3.) “kāma jānāmi te mūlaṃ saṅkalpāt kila jāyase” | “na tvāṃ saṅkalpayiṣyāmi samūlo na bhaviṣyasi” || (śāṃ.pa. 177.25) ityādismṛte:. sarvakāmaparityāge ca sarvakarmasannyāsaḥ siddho bhavati – “sa yathākāmo bhavati – tatkraturbhavati, yatkraturbhavati tatkarma kurute” (bṛ.u.4.4.5) ityādi śrutibhyaḥ”, “yadyat hi kurute jantuḥ tattatkāmasya ceṣṭitam” (mama.smṛ.2.4) ityādi smṛtibhyaśca. nyāyācca – na hi sarvasaṅkalpa sannyāse kaścit spanditum api śaktaḥ. tasmāt “sarvasaṅkalpa sannyāsī” iti vacanāt sarvān kāmān sarvāṇi karmāṇi ca tyājayati bhagavān.", "tr": "'When one is not attached to sense-objects…' When the yogin whose mind is being collected is not attached to the objects of the senses — sound and the rest — nor to actions, obligatory, occasional, desire-prompted or forbidden, because he sees no purpose in them — does not form the attachment of thinking them his duty, that is; renouncing all intentions — one whose nature is to renounce all intentions, which are the causes of desires for things of this world and the next — then, at that time, he is said to have ascended to yoga, to have attained yoga. From the words 'renouncing all intentions' the meaning is that one should renounce all desires and all actions. For all desires are rooted in intention, according to the smṛtis 'desire is rooted in intention; sacrifices arise from intention' (Manusmṛti 2.3) and 'Desire, I know your root: you are born of intention; I shall not form intentions of you, and you will be no more, with your root' (Śāntiparvan 177.25). And when all desires are given up, the renunciation of all actions is accomplished, according to the śrutis 'as is his desire, so is his will; as is his will, so is the action he does' (Bṛhadāraṇyaka 4.4.5) and the smṛtis 'whatever a creature does is the work of desire' (Manusmṛti 2.4). And by reasoning too: when all intentions are renounced no one can so much as stir. Therefore by the words 'renouncing all intentions' the Lord makes one give up all desires and all actions."},
           ]),
        _v([
            "uddharedātmanā''tmānaṃ nā'tmānamavasādayet |",
            "ātmaivahyātmano bandhurātmaiva ripurātmanaḥ",
        ], "|| 5 ||",
           "Let one raise the self by the self and not let the self sink; for the self alone is the friend of the self, and the self alone is its enemy.",
           bhashya=[
               {"text": "yadā evaṃ yogārūḍhaḥ tadā tena ātmā ātmanā uddhṛtaḥ bhavati saṃsārāt anarthajātāt, ataḥ –", "intro": True, "tr": "When he has thus ascended to yoga, the self is lifted up by the self out of saṃsāra, the mass of misfortune. Therefore —"},
               {"text": "uddharediti : uddharet, saṃsāra sāgare nimagnam, ātmanā, ātmānaṃ, tataḥ ut ūrdhvaṃ haret uddharet, yogarūḍhatāmāpādayet ityarthaḥ. na ātmānam, avasādayet, na adhaḥ nayet, na adhaḥ gamayet. ātmā eva, hi yasmāt, ātmanaḥ bandhuḥ, na hi anyaḥ kaścit bandhuḥ yaḥ saṃsāramuktaye bhavati. bandhuḥ api tāvat mokṣaṃ prati pratikūlaḥ eva, snehādi bandhanāyatanatvāt. tasmāt yuktam avadhāraṇam “ātmaiva hyātmano bandhuḥ” iti. ātmaiva ripuḥ śatruḥ. yaḥ anyaḥ apakārī bāhyaḥ śatruḥ saḥ api ātmaprayuktaḥ eva iti yuktam eva avadhāraṇam. “ātmaiva ripuḥ ātmanaḥ” iti.", "tr": "'Let one lift up the self by the self…' Let one lift up the self, sunk in the ocean of saṃsāra, by the self — raise it up out of it, bring it to the state of having ascended to yoga, that is. Let one not cast the self down, not lead it downward. For the self alone is the friend of the self; there is no other friend who can bring release from saṃsāra. Even a friend is in fact an obstacle to liberation, being a source of bondage through affection and the like. So the restriction 'the self alone is the friend of the self' is apt. The self alone is the enemy, the foe; any other, outer enemy who does harm is also prompted by the self; so the restriction 'the self alone is the enemy of the self' is apt too."},
           ]),
        _v([
            "bandhurātmā''tmanastasya yenātmaivātmanā jitaḥ |",
            "anātmanastu śatrutve vartetātmaiva śatruvat",
        ], "|| 6 ||",
           "The self is the friend of the self for one who has conquered himself by the self; but for one who has not conquered himself, the self acts like an enemy in hostility.",
           bhashya=[
               {"text": "ātmaiva bandhuḥ ātmaiva ripuḥ, ātmanaḥ ityuktam. tatra kiṃ lakṣaṇaḥ ātmā ātmanaḥ bandhuḥ, kiṃ lakṣaṇaḥ vā ātmā ātmanaḥ ripuḥ iti ucyate –", "intro": True, "tr": "It was said that the self alone is the friend and the self alone the enemy of the self. What kind of self is the friend of the self, and what kind is its enemy? It is said:"},
               {"text": "bandhuriti. bandhuḥ ātmā ātmanaḥ tasya – tasya ātmanaḥ saḥ ātmā bandhuḥ yena ātmanā ātmaiva jitaḥ. ātmā kāryakāraṇa saṅghātaḥ yena vaśīkṛtaḥ, jitendriyaḥ ityarthaḥ. anātmanaḥ tu ajitātmanaḥ tu, śatrutve śatrubhāve, varteta ātmaiva śatruvat, yathā anātmā śatruḥ ātmanaḥ apakārī, tathā ātmā ātmanaḥ apakāre varteta ityarthaḥ.", "tr": "'The self is the friend of the self…' The self is the friend of that self by which the self itself has been conquered — by which the self, the aggregate of body and senses, has been brought under control: one who has mastered the senses, that is. But for one who has not mastered himself, the self itself would act in enmity, like an enemy: as an outer enemy harms oneself, so the self would act to harm the self — that is the meaning."},
           ]),
        _v([
            "jitātmanaḥ praśāntasya paramātmā samāhitaḥ |",
            "śītoṣṇasukhaduḥkheṣu tathā mānāpamānayoḥ",
        ], "|| 7 ||",
           "The supreme Self of one who has conquered himself and is at peace remains composed in cold and heat, pleasure and pain, honour and dishonour.",
           bhashya=[
               {"text": "jitātmana iti :– jitātmanaḥ – kāryakaraṇasaṅghātaḥ ātmā jitaḥ yena saḥ jitātmā tasya jitātmanaḥ, praśāntasya prasannāntaḥ karaṇasya sataḥ sannyāsinaḥ, paramātmā samāhitaḥ sākṣāt ātmabhāvena vartate ityarthaḥ. kiñca śītoṣṇasukhaduḥkheṣu, tathā māne apamāne ca mānāpamānayoḥ pūjāparibhavayoḥ samaḥ syāt.", "tr": "'Of one who has mastered himself…' Of one who has mastered himself — by whom the self, the aggregate of body and senses, has been mastered — and is calm, the renouncer whose inner organ is serene, the supreme Self is collected: it abides directly as his own Self, that is. Moreover, he should be the same in cold and heat, pleasure and pain, and in honour and dishonour, in worship and contempt."},
           ]),
        _v([
            "jñānavijñānatṛptātmā kūṭastho vijitendriyaḥ |",
            "yukta ityucyate yogī samaloṣṭāśmakāñcanaḥ",
        ], "|| 8 ||",
           "The yogin who is content with knowledge and realisation, unshakeable, with senses conquered, to whom a clod, a stone and gold are alike, is called disciplined.",
           bhashya=[
               {"text": "jñāneti : – jñānavijñānatṛptātmā – jñānaṃ śāstroktapadārthānāṃ parijñānaṃ, vijñānaṃ tu śāstrataḥ jñātānāṃ tathaiva svānubhavakaraṇaṃ, tābhyāṃ jñānavijñānābhyāṃ, tṛptaḥ sañjātālampratyayaḥ ātmā antaḥkaraṇaṃ yasya saḥ jñānavijñānatṛptātmā kūṭasthaḥ aprakampyaḥ bhavati ityarthaḥ, vijitendriyaḥ ca. yaḥ īdṛśaḥ, yuktaḥ samāhitaḥ iti saḥ ucyate kathyate saḥ yogī. samaloṣṭāśmakāñcanaḥ loṣṭāśmakāñcanāni samāni yasya saḥ samaloṣṭāśmakāñcanaḥ. kiñca–", "tr": "'Content in knowledge and realisation…' Knowledge is the thorough understanding of the matters taught in scripture; realisation is making what is known from scripture one's own experience in just that way. He whose self, inner organ, is content with knowledge and realisation, in whom the sense 'enough' has arisen, is unshakeable — immovable, that is — and has conquered the senses. Such a one is said to be disciplined, collected; he is called a yogin. To whom a clod, a stone and gold are the same. Moreover —"},
           ]),
        _v([
            "suhṛnmitrāryudāsīnamadhyasthadveṣyabandhuṣu |",
            "sādhuṣvapi ca pāpeṣu samabuddhirviśiṣyate",
        ], "|| 9 ||",
           "He excels who is of even mind towards well-wishers, friends and foes, the indifferent and the neutral, the hateful and kinsmen, the good and the wicked.",
           bhashya=[
               {"text": "suhṛdityādi ślokārdham ekaṃ padam. suhṛt iti pratyupakāram anapekṣya upakartā. mitraṃ snehavān. ariḥ śatruḥ udāsīnaḥ na kasyacit pakṣaṃ bhajate. madhyasthaḥ yaḥ viruddhayoḥ ubhayoḥ hitaiṣī, dveṣyaḥ ātmanaḥ apriyaḥ bandhuḥ sambandhī. ityeteṣu, sādhuṣu śāstrānuvartiṣu, api ca, pāpeṣu pratiṣiddhakāriṣu sarveṣu eteṣu samabuddhiḥ “kaḥ kartā, kiṃ karma (kaḥ kiṅkarmā) iti avyāpṛtabuddhiḥ ityarthaḥ. viśiṣyate, vimucyate iti vā pāṭhāntaram. yogārūḍhānām sarveṣāṃ ayam uttamaḥ ityarthaḥ.", "tr": "'Towards well-wishers, friends, enemies…' The half-verse 'towards well-wishers…' is one compound. A well-wisher is one who helps without expecting a return; a friend, one who is affectionate; an enemy, a foe; the indifferent, one who takes no one's side; the neutral, one who wishes well to both of two opposed parties; the hateful, one disliked by oneself; a kinsman, a relative. Towards these, towards the good who follow the scriptures, and even towards sinners who do what is forbidden — towards all of these, one whose understanding is the same, whose understanding is not occupied with 'who is the doer, what is the deed', excels. 'Is freed' is another reading. Among all who have ascended to yoga he is the best, that is."},
           ]),
        _v([
            "yogī yuñjīta satatamātmānaṃ rahasi sthitaḥ |",
            "ekākī yatacittātmā nirāśīraparigrahaḥ",
        ], "|| 10 ||",
           "The yogin should constantly concentrate his mind, remaining in solitude, alone, with mind and body controlled, without hope and without possessions.",
           bhashya=[
               {"text": "ataḥ evam uttamaphalaprāptaye –", "intro": True, "tr": "Therefore, to attain this highest fruit —"},
               {"text": "yogīti. yogī dhyāyī, yuñjīta samādadhyāt, satataṃ sarvadā, ātmānam antaḥkaraṇam, rahasi ekānte giri guhādau sthitaḥ san, ekākī asahāyaḥ, “rahasi sthitaḥ ekākī ca” iti viśeṣaṇāt sannyāsaṃ kṛtvā ityarthaḥ. yata cittātmā – cittam antaḥkaraṇaṃ ātmā dehaśca saṃyatau yasya saḥ yatacittātmā, nirāśīḥ vītatṛṣṇaḥ aparigrahaḥ ca parigraharahitaḥ ityarthaḥ sannyāsitve'pi tyaktasarvaparigrahaḥ san yuñjīta ityarthaḥ.", "tr": "'The yogin should constantly discipline himself…' The yogin, the meditator, should discipline, collect, the self, the inner organ, constantly, at all times, staying in solitude, in a secluded place such as a mountain cave, alone, without a companion. From the qualifications 'staying in solitude' and 'alone', the meaning is 'having taken renunciation'. With mind and self restrained — the mind, the inner organ, and the self, the body, are restrained; without hope, free from thirst; and without possessions. Even as a renouncer, having given up all possessions, he should discipline himself — that is the meaning."},
           ]),
        _v([
            "śucau deśe pratiṣṭhāpya sthiramāsanamātmanaḥ |",
            "nātyucchritaṃ nātinīcaṃ cailājinakuśottaram",
        ], "|| 11 ||",
           "In a clean place, setting up for himself a firm seat, neither too high nor too low, covered with cloth, deer-skin and kuśa grass,",
           bhashya=[
               {"text": "atha idānīṃ yogaṃ yuñjānasya āsanāhāra vihārādīnāṃ yogasādhanatvena niyamaḥ vaktavyaḥ, prāptayogasya lakṣaṇaṃ tatphalādi ca ityataḥ ārabhyate. tatra āsanameva tāvat prathamam ucyate.", "intro": True, "tr": "Now the rules for one who practises yoga — about seat, food, recreation and the rest — are to be stated as means of yoga, together with the marks of one who has attained yoga and its fruit; hence this begins. First of all the seat is described."},
               {"text": "śucau iti. śucau śuddhe, vivikte svabhāvataḥ saṃskārataḥ vā, deśe sthāne, pratiṣṭhāpya, sthiram acalam, āsanam ātmanaḥ, āsanaṃ, nātyucchritam, na atīva ucchritam nāpi atinīcaṃ, tacca cailājinakuśottaram – cailam ajinaṃ kuśāśca uttare yasmin āsane tat āsanaṃ cailājinakuśottaram, pāṭhakramāt viparītaḥ atra kramaḥ cailādīnām.", "tr": "'In a clean place…' In a clean place — pure, secluded, by nature or by preparation — having set up firm, steady, his own seat, not too high and not too low, with cloth, a deer-skin and kuśa grass laid upon it: a seat on which cloth, skin and kuśa grass are spread. Here the order of cloth and the rest is the reverse of the order in the text."},
           ]),
        _v([
            "tatraikāgraṃ manaḥ kṛtvā yatacittendriya kriyaḥ |",
            "upaviśyāsane yuñjyādyogamātmaviśuddhaye",
        ], "|| 12 ||",
           "sitting there on the seat, making the mind one-pointed, with the workings of mind and senses restrained, let him practise yoga for the purification of the self.",
           bhashya=[
               {"text": "pratiṣṭhāpya kim?", "intro": True, "tr": "Having set it up, what then?"},
               {"text": "tatra iti. tatra tasmin āsane upaviśya yogaṃ yuñjyātkatham? sarva viṣayebhyaḥ upasaṃhṛtya ekāgraṃ manaḥ kṛtvā. yatacittendriyakriyaḥ – cittaṃ ca indriyāṇi ca cittendriyāṇi, teṣāṃ kriyāḥ saṃyatāḥ yasya saḥ yatacittendriya kriyaḥ, saḥ kimarthaṃ yogaṃ yuñjyāt ityāha – ātmaviśuddhaye – antaḥkaraṇasya viśuddhyartham ityetat.", "tr": "'There…' There, seated on that seat, he should practise yoga. How? Making the mind one-pointed, withdrawing it from all objects; with the activity of mind and senses restrained — one whose activities of mind and senses are controlled. For what purpose should he practise yoga? He says: for the purification of the self, for the purification of the inner organ, that is."},
           ]),
        _v([
            "samaṃ kāyaśirogrīvaṃ dhārayannacalaṃ sthiraḥ |",
            "samprekṣya nāsikāgraṃ svaṃ diśaścānavalokayan",
        ], "|| 13 ||",
           "Holding body, head and neck erect and still, steady, gazing at the tip of his nose and not looking around,",
           bhashya=[
               {"text": "bāhyam āsanam uktam, adhunā śarīradhāraṇaṃ katham ityucyate.", "intro": True, "tr": "The outer seat has been described; now it is told how the body is to be held."},
               {"text": "samamiti. samaṃ kāyaśirogrīvam – kāyaśca śiraśca grīvā ca kāyaśirogrīvam, tat samaṃ dhārayan, acalaṃ ca, samaṃ dhārayataḥ calanaṃ sambhavatiḥ ataḥ viśinaṣṭi acalam iti. sthiraḥ, sthiraḥ bhūtvā ityarthaḥ, svaṃ nāsikāgraṃ samprekṣya samyak prekṣaṇaṃ darśanaṃ kṛtvā iva iti; iva śabdaḥ luptaḥ draṣṭavyaḥ, na hi svanāsikāgra samprekṣaṇam iha vidhitsitaṃ, kiṃ tarhi? cakṣuṣoḥ dṛṣṭi sannipātaḥ; sa ca antaḥ karaṇasamādhānāpekṣaḥ vivakṣitaḥ. svanāsikāgra samprekṣaṇam eva cet vivakṣitaṃ manaḥ tatraiva samādhīyeta na ātmani – ātmani hi manasaḥ samādhānaṃ vakṣyati. “ātmasaṃsthaṃ manaḥ kṛtvā” (6.25) iti. tasmāt ivaśabdalopena akṣṇoḥ dṛṣṭi sannipātaḥ eva samprekṣya ityucyate. diśaḥ ca anavalokayan, diśāṃ ca avalokanam antarā akurvan ityetat. kiñca –", "tr": "'Holding body, head and neck erect…' Body, head and neck — holding these erect and motionless; since one holding them erect may still move, he specifies 'motionless'. Steady: becoming steady, that is. Gazing at the tip of his own nose — as if gazing, looking well; the word 'as if' is to be understood as dropped. For gazing at the tip of one's own nose is not what is enjoined here; rather, the meeting of the gaze of the two eyes, and that as required for the collecting of the inner organ, is what is meant. If gazing at the tip of one's own nose were what was meant, the mind would be collected there and not in the Self; but he will speak of collecting the mind in the Self: 'making the mind abide in the Self' (6.25). So by the dropping of 'as if', only the meeting of the gaze of the eyes is meant by 'gazing'. And not looking about at the directions — not looking at the directions in between, that is. Moreover —"},
           ]),
        _v([
            "praśāntātmā vigatabhīrbrahmacārivrate sthitaḥ |",
            "manaḥ saṃyamya maccitto yukta āsīta matparaḥ",
        ], "|| 14 ||",
           "serene, fearless, firm in the vow of celibacy, restraining the mind, thinking of me, let him sit disciplined, intent on me.",
           bhashya=[
               {"text": "praśāntātmeti. praśāntātmā – prakarṣeṇa śāntaḥ ātmā antaḥkaraṇaṃ yasya saḥ ayaṃ praśāntātmā, vigatabhīḥ vigatabhayaḥ brahmacārivrate sthitaḥ brahmacāriṇaḥ vrataṃ brahmacaryaṃ guru śuśrūṣā bhikṣānnabhuktyādi, tasmin sthitaḥ tadanuṣṭhātā bhavet ityarthaḥ. kiṃ ca manaḥ saṃyamya, manasaḥ vṛttīḥ upasaṃhṛtya ityetat, maccittaḥ mayi parameśvare cittaṃ yasya saḥ ayaṃ maccittaḥ, yuktaḥ samāhitaḥ san, āsīt upaviśet. matparaḥ ahaṃ paraḥ yasya saḥ ayaṃ matparaḥ bhavati kaścidrāgī strī cittaḥ, na tu striyameva paratvena gṛhṇāti, kiṃ tarhi? rājānaṃ mahādevaṃ vā, ayaṃ tu maccittaḥ matparaśca.", "tr": "'Serene of self…' Serene of self: one whose self, the inner organ, is deeply calm. Fearless, with fear gone. Established in the vow of celibacy: the vow of the brahmacārin — continence, service of the teacher, living on alms and the rest; he should abide in it, practise it, that is. Moreover, restraining the mind — withdrawing the activities of the mind, that is — with his mind on me, whose mind is on me, the supreme Lord, disciplined, collected, he should sit. Intent on me, for whom I am the highest. A passionate man may have his mind on a woman, yet he does not take the woman herself as the highest — rather the king or Mahādeva; but this one both has his mind on me and is intent on me."},
           ]),
        _v([
            "yuñjannevaṃ sadā''tmānaṃ yogī niyatamānasaḥ |",
            "śāntiṃ nirvāṇaparamāṃ matsaṃsthāmadhigacchati",
        ], "|| 15 ||",
           "Thus always disciplining himself, the yogin of restrained mind attains the peace that culminates in nirvāṇa and abides in me.",
           bhashya=[
               {"text": "atha idānīṃ yogaphalam ucyate –", "intro": True, "tr": "Now the fruit of yoga is told:"},
               {"text": "yuñjan iti. yuñjan samādhānaṃ kurvan, evaṃ yathoktena vidhānena, sadā ātmānaṃ sarvadā yogī niyatamānasaḥ, niyataṃ saṃyataṃ mānasaṃ manaḥ yasya saḥ ayaṃ niyata mānasaḥ śāntim uparatiṃ, nirvāṇaparamām nirvāṇaṃ mokṣaḥ, tat paramā niṣṭhā yasyāḥ śānteḥ sā nirvāṇa paramā, tāṃ nirvāṇa paramāṃ, matsaṃsthāṃ madadhīnām adhigacchati prāpnoti.", "tr": "'Thus always disciplining himself…' Thus disciplining, collecting, himself always, by the method described, the yogin with mind controlled — whose mind is controlled, restrained — attains, reaches, peace, cessation, whose culmination is nirvāṇa — nirvāṇa is liberation, and the peace that has it as its highest end is called 'culminating in nirvāṇa' — and which abides in me, depends on me."},
           ]),
        _v([
            "nātyaśnatastu yogo'sti na caikāntamanaśnataḥ |",
            "na cātisvapnaśīlasya jāgrato naiva cārjuna",
        ], "|| 16 ||",
           "Yoga is not for one who eats too much, nor for one who does not eat at all, nor for one who sleeps too much or keeps awake too long, Arjuna.",
           bhashya=[
               {"text": "idānīṃ yoginaḥ āhārādi niyamaḥ ucyate –", "intro": True, "tr": "Now the rules about food and the rest for the yogin are told:"},
               {"text": "na iti. nātyaśnataḥ ātmasammitam annaparimāṇam atītya aśnataḥ na yogaḥasti, na ca ekāntam anaśnataḥ yogaḥ asti. “yadu ha vā ātmasammitamannaṃ tadavati, tanna hinasti, yadbhūyo hinasti, tadyatkanīyo'nnaṃ na tadavati” (śata.brāha.9.2.1.2) iti śruteḥ. tasmādyogī na ātmasammitāt annāt adhikaṃ nyūnaṃ vā aśnīyāt. athavā yoginaḥ yogaśāstre paripaṭhitāt annaparimāṇāt atimātram aśnataḥ yogaḥ nāsti. uktaṃ hi – “ardhaṃ savyañjanānnasya tṛtīyamudakasya tu, vāyoḥ sañcaraṇārthaṃ tu caturthamavaśeṣayet”. ityādiparimāṇam, tathā – na cātisvapnaśīlasya yogaḥ bhavati, naiva ca atimātraṃ jāgrataḥ yogaḥ bhavati ca arjuna.", "tr": "'Yoga is not for one who eats too much…' There is no yoga for one who eats too much, beyond the measure of food suited to himself; nor is there yoga for one who does not eat at all. According to the śruti, 'The food that is suited to oneself protects; it does no harm. What is more harms; what is less does not protect' (Śatapatha Brāhmaṇa 9.2.1.2). So the yogin should not eat more or less than the food suited to himself. Or else: there is no yoga for the yogin who eats beyond the measure of food stated in the yoga scriptures; for it is said, 'Half the stomach for food with relishes, a third for water, and a fourth should be left for the movement of air' — such is the measure. Likewise there is no yoga for one given to sleeping too much, nor for one who keeps awake too much, Arjuna."},
           ]),
        _v([
            "yuktāhāravihārasya yuktaceṣṭasya karmasu |",
            "yuktasvapnāvabodhasya yogo bhavati duḥkhahā",
        ], "|| 17 ||",
           "For one who is moderate in food and recreation, disciplined in the movements of action, moderate in sleep and waking, yoga becomes the destroyer of sorrow.",
           bhashya=[
               {"text": "kathaṃ punaḥ yogaḥ bhavati ityucyate –", "intro": True, "tr": "How, then, does yoga come about? It is said:"},
               {"text": "yukta iti. yuktāhāra vihārasya – āhriyate iti āhāraḥ annam, viharaṇaṃ vihāraḥ pādakramaḥ, tau yuktau niyata parimāṇau yasya, saḥ yuktāhāra vihāraḥ tasya; tathā yuktaceṣṭasya – yuktā niyatā ceṣṭā yasya karmasu, tasya; tathā, yuktasvapnāvabodhasya – yuktau svapnaśca avabodhaśca tau niyatakālau yasya tasya; yuktāhāravihārasya yukta ceṣṭasya karmasu, yukta svapnāvabodhasya yoginaḥ yogaḥ bhavati, duḥkhahā – duḥkhāni sarvāṇi hantīti duḥkhahā sarva saṃsāra duḥkhakṣayakṛt yogaḥ bhavatītyarthaḥ.", "tr": "'For one disciplined in food and recreation…' Food is what is taken in; recreation is moving about, walking. One whose food and recreation are disciplined, of fixed measure; likewise one whose effort in actions is disciplined, regulated; likewise one whose sleep and waking are disciplined, kept to fixed times — for the yogin who is disciplined in food and recreation, disciplined in effort in actions, and disciplined in sleep and waking, there comes yoga that destroys sorrow: yoga that destroys all sorrows, that brings about the end of all the sorrow of saṃsāra, that is."},
           ]),
        _v([
            "yadā viniyataṃ cittamātmanyevāvatiṣṭhate |",
            "niḥspṛhaḥ sarvakāmebhyo yukta ityucyate tadā",
        ], "|| 18 ||",
           "When the controlled mind rests in the Self alone, free from longing for all desires, then one is said to be disciplined.",
           bhashya=[
               {"text": "atha adhunā kadā yuktaḥ bhavati ityucyate –", "intro": True, "tr": "Now it is told when one is disciplined:"},
               {"text": "yadā iti. yadā viniyataṃ cittaṃ viśeṣeṇa niyataṃ saṃyatam ekāgratām āpannaṃ cittaṃ hitvā bāhyārthacintām ātmanyeva kevale avatiṣṭhate, svātmani sthitiṃ labhate ityarthaḥ. niḥspṛhaḥ sarvakāmebhyaḥ – nirgatā dṛṣṭādṛṣṭa viṣayebhyaḥ spṛhā tṛṣṇā yasya yoginaḥ saḥ yuktaḥ samāhitaḥ iti ucyate, tadā tasmin kāle.", "tr": "'When the controlled mind…' When the controlled mind — especially controlled, restrained, become one-pointed — giving up thought of outer things, rests in the Self alone, finds its abiding in its own Self, that is; free from longing for all desires — the yogin from whom longing, thirst, for all objects seen and unseen has gone — then, at that time, he is called disciplined, collected."},
           ]),
        _v([
            "yathā dīpo nivātastho neṅgate sopamā smṛtā |",
            "yogino yatacittasya yuñjato yogamātmanaḥ",
        ], "|| 19 ||",
           "'As a lamp in a windless place does not flicker' — that is the simile used for the yogin of controlled mind practising the yoga of the Self.",
           bhashya=[
               {"text": "tasya yoginaḥ samāhitaṃ yaccittaṃ tasya upamā ucyate –", "intro": True, "tr": "A simile is given for the collected mind of that yogin:"},
               {"text": "yadhā iti. yathā, dīpaḥ pradīpaḥ, nivātasthaḥ nivāte vātavarjite deśe sthitaḥ, na iṅgate na calati, sā upamā upamīyate anayā iti upamā, yogajñaiḥ citta pracāradarśibhiḥ, smṛtā cintitā, yoginaḥ yatacittasya saṃyatāntaḥ karaṇasya, yuñjataḥ yogam anutiṣṭhataḥ, ātmanaḥ samādhim anutiṣṭhataḥ ityarthaḥ.", "tr": "'As a lamp in a windless place…' As a lamp standing in a windless place, a place free of wind, does not flicker, does not move — that simile — a simile is that by which something is compared — is thought of by those who know yoga, who see the workings of the mind, for the yogin with mind restrained, whose inner organ is controlled, practising yoga of the self — practising samādhi, that is."},
           ]),
        _v([
            "yatroparamate cittaṃ niruddhaṃ yogasevayā |",
            "yatra caivātmanā''tmānaṃ paśyannātmani tuṣyati",
        ], "|| 20 ||",
           "Where the mind, restrained by the practice of yoga, comes to rest; where, seeing the Self by the self, one is content in the Self;",
           bhashya=[
               {"text": "evaṃ yogābhyāsabalāt ekāgrībhūtaṃ nivātapradīpakalpaṃ sat –", "intro": True, "tr": "Thus, by the power of the practice of yoga, become one-pointed, like a lamp in a windless place —"},
               {"text": "yatra iti. yatra yasmin kāle uparamate, cittam, uparatiṃ gacchati, niruddhaṃ sarvataḥ nivāritapracāraṃ, yogasevayā yogānuṣṭhānena, yatracaiva yasmin ca kāle, ātmanā samādhipariśuddhena antaḥkaraṇena, ātmānaṃ paraṃ caitanyaṃ jyotiḥ svarūpaṃ, paśyan upalabhamānaḥ, sve eva ātmani, tuṣyati tuṣṭiṃ bhajate. kiñca", "tr": "'Where the mind comes to rest…' Where — at which time — the mind comes to rest, attains cessation, restrained — its movement checked on every side — by the practice of yoga; and where, at which time, seeing, perceiving, the Self — the supreme consciousness, light by nature — by the self, by the inner organ purified by samādhi, he is content in his own Self, finds contentment. Moreover —"},
           ]),
        _v([
            "sukhamātyantikaṃ yattadbuddhigrāhyamatīndriyam |",
            "vetti yatra na caivāyaṃ sthitaścalati tattvataḥ",
        ], "|| 21 ||",
           "where one knows that boundless happiness which is grasped by the understanding and lies beyond the senses, and, established there, never moves from the truth;",
           bhashya=[
               {"text": "sukhamiti. sukham ātyantikam atyantam eva bhavati iti ātyantikam, anantam ityarthaḥ. yat, tat, buddhigrāhyaṃ buddhyaiva indriya nirapekṣayā gṛhyate iti buddhigrāhyam, atīndriyam indriya gocarātītam, aviṣayajanitam ityarthaḥ, vetti tat īdṛśaṃ sukham anubhavati, yatra yasmin kāle, na ca, eva, ayaṃ vidvān ātmasvarūpe sthitaḥ, tasmāt, naiva calati tattvataḥ, tattvasvarūpāt na pracyavate ityarthaḥ. kiñca–", "tr": "'That utmost happiness…' Utmost happiness: that which is absolutely so, endless, that is. That which is grasped by the understanding — grasped by the understanding alone, independently of the senses — and beyond the senses, beyond the range of the senses, not produced by objects, that is. He knows, experiences, such happiness; where — at which time — established in the nature of the Self, this wise man never moves from the truth, does not fall away from his true nature, that is. Moreover —"},
           ]),
        _v([
            "yaṃ labdhvā cāparaṃ lābhaṃ manyate nādhikaṃ tataḥ |",
            "yasmin sthito na duḥkhena guruṇā'pi vicālyate",
        ], "|| 22 ||",
           "having gained which one thinks no other gain greater, and established in which one is not shaken even by heavy sorrow —",
           bhashya=[
               {"text": "ya miti. yaṃ labdhvā – yam ātmalābhaṃ, labdhvā prāpya, ca, aparam anyat, lābhāntaraṃ tataḥ adhikam astīti na manyate cintayati kiṃ ca yasmin ātmatattve, sthitaḥ, duḥkhena śastranipātādi lakṣaṇena guruṇā mahatāpi na vicālyate.", "tr": "'Having gained which…' Having gained, attained, which — the gain of the Self — he does not think, consider, any other gain to be greater than it; and established in which — in the reality of the Self — he is not shaken even by heavy, great sorrow, such as the falling of weapons upon him."},
           ]),
        _v([
            "taṃ vidyādduḥkhasaṃyogaviyogaṃ yogasañjñitam |",
            "sa niścayena yoktavyo yogo'nirviṇṇacetasā",
        ], "|| 23 ||",
           "let that be known as yoga: the unyoking from union with sorrow. That yoga should be practised with resolve and an undespairing mind.",
           bhashya=[
               {"text": "“yatroparamate” (6.20) ityārabhya yāvadbhiḥ viśeṣaṇaiḥ viśiṣṭaḥ ātmāvasthā viśeṣaḥ yogaḥ uktaḥ –", "intro": True, "tr": "Beginning with 'where the mind comes to rest' (6.20), yoga has been described as a particular state of the self qualified by these several attributes —"},
               {"text": "tamiti. taṃ vidyāt vijānīyāt, duḥkhasaṃyogaviyogaṃ, duḥkhaiḥ saṃyogaḥ duḥkhasaṃyogaḥ, tena viyogaḥ duḥkhasaṃyogaviyogaḥ, taṃ duḥkhasaṃyogaviyogaṃ, yogaḥ ityeva sañjñitaṃ viparīta lakṣaṇena vidyāt vijānīyāt ityarthaḥ. yogaphalam upasaṃhṛtya punaḥ anvārambheṇa yogasya kartavyatā ucyate niścayā'nirvedayoḥ yogasādhanatva vidhānārthaṃ. saḥ yathoktaphalaḥ yogaḥ niścayena adhyavasāyena yoktavyaḥ anirviṇṇacetasā, na nirviṇṇam anirviṇṇam, anirviṇṇaṃ kiṃ tat? cetaḥ tena, nirveda rahitena cetasā cittena ityarthaḥ. kiñca–", "tr": "'Let that be known…' Let one know, understand, that — disjunction from union with sorrow: union with sorrows is union with sorrow, and separation from that is disjunction from union with sorrow — as what is called yoga; let one understand it as named by the contrary description, that is. Having concluded the fruit of yoga, he begins again and tells that yoga is to be practised, in order to enjoin resolve and freedom from despondency as means of yoga. That yoga, with its fruit as described, is to be practised with resolve, with determination, with an undespondent mind — a mind, a heart, free from despondency, that is. Moreover —"},
           ]),
        _v([
            "saṅkalpaprabhavān kāmāṃstyaktvā sarvānaśeṣataḥ |",
            "manasaivendriyagrāmaṃ viniyamya samantataḥ",
        ], "|| 24 ||",
           "Giving up entirely all desires born of intention, restraining the whole group of the senses on every side with the mind alone,",
           bhashya=[
               {"text": "saṅkalpa iti. saṅkalpa prabhavān – saṅkalpaḥ prabhavaḥ yeṣāṃ kāmānāṃ te saṅkalpa prabhavāḥ kāmāḥ, tān, tyaktvā parityajya, sarvān aśeṣaṇa nirlepena, kiṃ ca – manasaiva vivekayuktena, indriyagrāmam indriya samudāyaṃ viniyamya niyamanaṃ kṛtvā samantataḥ samantāt.", "tr": "'Abandoning all desires born of intention…' Abandoning, giving up, desires born of intention — desires whose source is intention — all of them without remainder, without a trace; and with the mind alone, endowed with discrimination, restraining the host of the senses on every side —"},
           ]),
        _v([
            "śanaiḥ śanairuparamedbuddhyā dhṛtigṛhītayā |",
            "ātmasaṃsthaṃ manaḥ kṛtvā na kiñcidapi cintayet",
        ], "|| 25 ||",
           "little by little let him come to rest, with the understanding held firm; having fixed the mind in the Self, let him think of nothing at all.",
           bhashya=[
               {"text": "śanairiti. śanaiḥ śanaiḥ, na sahasā, uparamet uparatiṃ kuryāt, kayā? buddhyā, kiṃ viśiṣṭayā? dhṛti gṛhītayā'dhṛtyā dhairyeṇa gṛhītayā dhṛti gṛhītayā, dhairyeṇa yuktayā ityarthaḥ. ātmasaṃstham ātmani saṃsthitam, “ātmaiva sarvaṃ, na tataḥ anyat kiñcit asti” ityevam ātmasaṃsthaṃ, manaḥ kṛtvā na kiñcidapi cintayet. eṣa yogasya paramaḥ vidhiḥ.", "tr": "'Little by little let him come to rest…' Little by little, not suddenly, let him come to rest, bring about cessation. By what? By the understanding. Of what kind? Held by firmness: held by steadiness, endowed with fortitude, that is. Making the mind abide in the Self — 'the Self alone is all; there is nothing other than it' — thus making the mind abide in the Self, let him think of nothing at all. This is the highest rule of yoga."},
           ]),
        _v([
            "yato yato niścarati manaścañcalamasthiram |",
            "tatastato niyamyaitadātmanyeva vaśaṃ nayet",
        ], "|| 26 ||",
           "Wherever the restless, unsteady mind wanders off, from there let him restrain it and bring it back under the control of the Self alone.",
           bhashya=[
               {"text": "tatraivam ātmasaṃsthaṃ manaḥ kartuṃ pravṛttaḥ yogī–", "intro": True, "tr": "The yogin who has thus set about making the mind abide in the Self —"},
               {"text": "yato iti. yataḥ yataḥ yasmāt yasmāt nimittāt śabdādeḥ, niścarati nirgacchati, svābhāvika doṣāt, manaḥ, cañcalam atyarthaṃ calam, ata eva asthiraṃ, tataḥ tataḥ tasmāt tasmāt śabdādeḥ nimittāt, niyamya, tattat nimittaṃ yāthātmyanirūpaṇena ābhāsīkṛtya vairāgyabhāvanayā ca, etat manaḥ ātmanyeva vaśaṃ nayet ātmavaśyatām āpādayet. evaṃ yogābhyāsabalāt yoginaḥ ātmanyeva praśāmyati manaḥ.", "tr": "'Whenever the mind wanders…' From whatever cause — sound and the rest — the mind, fickle, exceedingly restless, and therefore unsteady, wanders, goes out, through its natural fault, from that cause, sound or whatever, let him restrain it — reducing each cause to a mere appearance by determining its true nature, and by cultivating dispassion — and bring this mind under control in the Self alone, make it subject to the Self. Thus, by the power of the practice of yoga, the yogin's mind comes to peace in the Self alone."},
           ]),
        _v([
            "praśāntamanasaṃ hyenaṃ yoginaṃ sukhamuttamam |",
            "upaiti śāntarajasaṃ brahmabhūtamakalmaṣam",
        ], "|| 27 ||",
           "For supreme happiness comes to the yogin whose mind is at peace, whose passion is stilled, who has become Brahman and is free from stain.",
           bhashya=[
               {"text": "praśānta iti. praśāntamanasaṃ prakarṣeṇa śāntaṃ manaḥ yasya saḥ praśāntamanāḥ, taṃ praśāntamanasam, hi enaṃ yoginaṃ, sukham, uttamaṃ niratiśayam, upaiti upagacchati. śāntarajasaṃ prakṣīṇamohādi kleśarajasam ityarthaḥ. brahmabhūtaṃ jīvanmuktaṃ, “brahmaiva sarvam” ityevaṃ niścayavantaṃ brahma bhūtam, akalmaṣaṃ adharmādivarjitam.", "tr": "'For this yogin, whose mind is serene…' For this yogin of serene mind — whose mind is deeply calm — comes, approaches, the highest, unsurpassed, happiness; to him whose rajas is stilled, in whom the rajas of the afflictions, delusion and the rest, has dwindled away, that is; who has become Brahman — liberated while living, with the certainty 'all is Brahman alone'; and who is stainless, free from demerit and the rest."},
           ]),
        _v([
            "yuñjannevaṃ sadā''tmānaṃ yogī vigatakalmaṣaḥ |",
            "sukhena brahmasaṃsparśamatyantaṃ sukhamaśnute",
        ], "|| 28 ||",
           "Thus always disciplining himself, the yogin freed from stain easily enjoys the boundless happiness of contact with Brahman.",
           bhashya=[
               {"text": "yuñjanniti. yuñjan evaṃ yathoktena krameṇa, yogī, yogāntarāyavarjitaḥ sadā sarvadā ātmānaṃ, vigatakalmaṣaḥ ca vigatapāpaḥ, sukhena anāyāsena, brahmasaṃsparśaṃ brahmaṇā pareṇa saṃsparśaḥ yasya tat brahmasaṃsparśaṃ, sukham, atyantam antam atītya vartate iti atyantam, utkṛṣṭaṃ, niratiśayam, sukhaṃ aśnute vyāpnoti.", "tr": "'Thus always disciplining himself…' Thus disciplining himself always, by the method described, the yogin, free from obstacles to yoga, his stain gone — his sin gone — easily, without toil, attains, pervades, the happiness of contact with Brahman — happiness in which there is contact with the supreme Brahman — that is endless: that which goes beyond any end, the highest, unsurpassed happiness."},
           ]),
        _v([
            "sarvabhūtasthamātmānaṃ sarvabhūtāni cātmani |",
            "īkṣate yogayuktātmā sarvatra samadarśanaḥ",
        ], "|| 29 ||",
           "With the self disciplined in yoga, seeing the same everywhere, he sees the Self abiding in all beings and all beings in the Self.",
           bhashya=[
               {"text": "idānīṃ yogasya yatphalaṃ brahmaikatvadarśanaṃ sarvasaṃsāravicchedakāraṇaṃ tat pradarśyate.", "intro": True, "tr": "Now the fruit of yoga — the vision of oneness with Brahman, the cause that cuts off all saṃsāra — is shown."},
               {"text": "sarva iti. sarvabhūtasthaṃ sarveṣu bhūteṣu sthitaṃ svam ātmānam, sarvabhūtāni ca ātmani brahmādīni stambaparyantāni ca sarvabhūtāni ātmani ekatāṃ gatāni īkṣate paśyati, yogayuktātmā samāhitāntaḥkaraṇaḥ, san sarvatra samadarśanaḥ sarveṣu brahmādisthāvarānteṣu viṣameṣu sarvabhūteṣu, samaṃ nirviśeṣaṃ brahmātmaikatva viṣayaṃ darśanaṃ jñānaṃ yasya saḥ sarvatra samadarśanaḥ.", "tr": "'He sees the Self abiding in all beings…' He sees his own Self abiding in all beings, and all beings, from Brahmā down to a clump of grass, in the Self, become one with it — he whose self is disciplined in yoga, whose inner organ is collected — seeing the same everywhere: one whose vision, whose knowledge, is the same, without distinction, having as its object the oneness of Brahman and the Self, in all beings, however unequal, from Brahmā down to the immovable."},
           ]),
        _v([
            "yo māṃ paśyati sarvatra sarvaṃ ca mayi paśyati |",
            "tasyā'haṃ na praṇaśyāmi sa ca me na praṇaśyati",
        ], "|| 30 ||",
           "He who sees me everywhere and sees everything in me — I am not lost to him, nor is he lost to me.",
           bhashya=[
               {"text": "etasyaiva ātmaikatvadarśanasya phalam ucyate –", "intro": True, "tr": "The fruit of this very vision of the oneness of the Self is told:"},
               {"text": "ya iti. yaḥ māṃ paśyati vāsudevaṃ, sarvasya ātmānaṃ, sarvatra sarveṣu bhūteṣu, sarvaṃ ca brahmādi bhūtajātaṃ mayi sarvātmani paśyati tasya evam ātmaikatvadarśinaḥ, aham īśvaraḥ, na praṇaśyāmi na parokṣatāṃ gamiṣyāmi. sa ca me na praṇaśyati, sa ca vidvān mama vāsudevasya na praṇaśyati na parokṣībhavati, tasya ca mama ca ekātmatvāt. svātmā hi nāma ātmanaḥ prakāśaḥ eva (priyaḥ) bhavati, yasmācca ahameva sarvātmaikatvadarśī ityetat.", "tr": "'He who sees me everywhere…' He who sees me, Vāsudeva, the Self of all, everywhere, in all beings, and sees everything, the whole multitude of beings from Brahmā onwards, in me, the Self of all — to him who thus sees the oneness of the Self, I, the Lord, am not lost, do not become remote. And he is not lost to me: that wise man is not lost to me, Vāsudeva, does not become remote, because he and I are one Self. For one's own Self is surely manifest (dear) to oneself; and because I alone am he who sees the oneness of the Self of all."},
           ]),
        _v([
            "sarvabhūtasthitaṃ yo māṃ bhajatyekatvamāsthitaḥ |",
            "sarvathā vartamāno'pi sa yogī mayi vartate",
        ], "|| 31 ||",
           "The yogin who, established in oneness, worships me as dwelling in all beings, abides in me, however he may live.",
           bhashya=[
               {"text": "pūrva ślokārthaṃ samyagdarśanamanūdya tatphalaṃ mokṣaḥ abhidhīyate–", "intro": True, "tr": "Restating right vision, the meaning of the previous verse, its fruit, liberation, is declared:"},
               {"text": "sarva iti. sarvathā sarvaprakāraiḥ vartamānaḥ api samyagdarśī yogī mayi vaiṣṇave parame pade, vartate, nityamuktaḥ eva saḥ na mokṣaṃ prati kenacit pratibadhyate ityarthaḥ.", "tr": "'He who, established in oneness…' He who, established in oneness, worships me abiding in all beings — that yogin with right vision, however he may live, in whatever way, abides in me, in the supreme abode of Viṣṇu; he is ever free; he is not obstructed by anything from liberation, that is."},
           ]),
        _v([
            "ātmaupamyena sarvatra samaṃ paśyati yo'rjuna |",
            "sukhaṃ vā yadi vā duḥkhaṃ sa yogī paramo mataḥ",
        ], "|| 32 ||",
           "He who, by comparison with himself, sees the same everywhere, Arjuna, whether in pleasure or in pain — he is deemed the highest yogin.",
           bhashya=[
               {"text": "kiṃ cānyat –", "intro": True, "tr": "And further —"},
               {"text": "ātmaupamyeneti. ātmaupamyena – ātmā svayam eva upamīyate (anayā) iti upamā. tasyāḥ upamāyāḥ bhāvaḥ aupamyam. tena ātmaupamyena, sarvatra sarvabhūteṣu, samaṃ tulyam, paśyati yaḥ arjuna, saḥ ca kiṃ samaṃ paśyatīti? ucyate – yathā mama sukham iṣṭaṃ tathā sarvaprāṇināṃ sukham anukūlam. vāśabdaḥ cārthe. yadi vā yacca duḥ khaṃ mama pratikūlam aniṣṭaṃ yathā, tathā sarvaprāṇināṃ duḥkhaṃ aniṣṭaṃ pratikūlam. ityevam, ātmaupamyena sukhaduḥkhe anukūla pratikūle tulyatayā sarvabhūteṣu samaṃ paśyati, na kasyacit pratikūlam ācarati ahiṃsakaḥ ityarthaḥ. yaḥ evam ahiṃsakaḥ samyagdarśananiṣṭhaḥ saḥ yogī paramaḥ utkṛṣṭaḥ, mataḥ, abhipretaḥ sarvayogināṃ madhye.", "tr": "'By the likeness to himself…' By the likeness to himself: that by which oneself is compared is a likeness, and its being so is 'likeness'; by that likeness to himself, he who sees the same, the equal, everywhere, in all beings, Arjuna — what does he see as the same? It is said: as pleasure is desired by me, so pleasure is welcome to all living beings — the word 'vā' has the sense of 'and' — and as pain is unwelcome, undesired, by me, so pain is undesired and unwelcome to all living beings. He who thus, by likeness to himself, sees pleasure and pain, the welcome and the unwelcome, as equal in all beings, does nothing unwelcome to anyone — is harmless, that is. He who is thus harmless and steadfast in right vision is held to be the supreme, the highest, yogin among all yogins."},
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "yo'yaṃ yogastvayā proktaḥ sāmyena madhusūdana |",
            "etasyāhaṃ na paśyāmi cañcalatvāt sthitiṃ sthirām",
        ], "|| 33 ||",
           "Arjuna said: This yoga of sameness that you have taught, Madhusūdana — I do not see how it can stand firm, because the mind is restless.",
           bhashya=[
               {"text": "etasya yathoktasya samyagdarśana lakṣaṇasya yogasya duḥkhasampādyatāṃ ālakṣya śuśrūṣuḥ (dhṛvam) tat prāptyupāyam arjunaḥ uvāca,", "intro": True, "tr": "Noticing that this yoga, consisting in right vision as described, is hard to achieve, Arjuna, wishing to hear the means to attain it, said:"},
               {"text": "yo'yamiti. yaḥ ayaṃ yogaḥ tvayā proktaḥ sāmyena samatvena, he! madhusūdana ! etasya yogasya, ahaṃ, na paśyāmi na upalabhe cañcalatvāt manasaḥ, kim? sthirām acalāṃ, sthitim.", "tr": "'This yoga that you have declared…' This yoga that you have declared as sameness, as equanimity, O Madhusūdana — of this yoga I do not see, do not find, a steady, unmoving, continuance, because of the restlessness of the mind."},
           ]),
        _v([
            "cañcalaṃ hi manaḥ kṛṣṇa pramāthi balavaddṛḍham |",
            "tasyāhaṃ nigrahaṃ manye vāyoriva suduṣkaram",
        ], "|| 34 ||",
           "For the mind is restless, Kṛṣṇa, turbulent, strong and obstinate. I think it as hard to restrain as the wind.",
           bhashya=[
               {"text": "prasiddhaṃ etat–", "intro": True, "tr": "This is well known:"},
               {"text": "cañcalamiti – cañcalaṃ hi manaḥ “kṛṣṇe”ti kṛṣateḥ vilekhanārthasya rūpam, bhaktajanapāpādi doṣākarṣaṇāt kṛṣṇaḥ. tasya sambuddhiḥ he kṛṣṇa. hi yasmāt manaḥ cañcalaṃ na kevalam atyarthaṃ cañcalaṃ, pramāthi ca pramathanaśīlaṃ, pramathnāti śarīram indriyāṇi ca vikṣipati, sat paravaśī karoti. kiṃ ca balavat, na kena cit niyantuṃ śakyam. durnivāratvāt kiṃ ca dṛḍhaṃ tantunāgavat acchedyaṃ, tasya evambhūtasya manasaḥ, ahaṃ, nigrahaṃ nirodhaṃ, manye, vāyoriva – yathā vāyoḥ duṣkaraḥ nirodhaḥ tato'pi manasaḥ duṣkaraṃ manye ityabhiprāyaḥ", "tr": "'For the mind is restless, Kṛṣṇa…' For the mind is restless. 'Kṛṣṇa' is a form of the root kṛṣ, meaning to scrape: he is Kṛṣṇa because he draws away the sins and other faults of his devotees; the vocative is 'O Kṛṣṇa'. For the mind is not only exceedingly restless; it is also turbulent, given to agitating — it agitates the body and the senses, distracts them and puts them in another's power. Moreover it is strong, not to be controlled by anyone, being hard to check; and firm, uncuttable like a tantunāga, a water snare. Of a mind such as this I think the restraint, the checking, as of the wind: as checking the wind is hard, I think that of the mind is harder still — that is the purport."},
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "asaṃśayaṃ mahābāho mano durnigrahaṃ calam |",
            "abhyāsena tu kaunteya vairāgyeṇa ca gṛhyate",
        ], "|| 35 ||",
           "The Blessed Lord said: Without doubt, mighty-armed one, the mind is restless and hard to control; but by practice and dispassion, son of Kuntī, it is held.",
           bhashya=[
               {"text": "śrī bhagavānuvāca – evaṃ etat yathā bravīṣi–", "intro": True, "tr": "The Blessed Lord said: It is just as you say —"},
               {"text": "asaṃśayamiti. asaṃśayaṃ nāsti saṃśayaḥ manaḥ durnigrahaṃ calam ityatra. he, mahābāho! kintu, abhyāsena tu abhyāso nāma cittabhūmau kasyāṃ cit samāna pratyayā vṛttiḥ cittasya. vairāgyaṃ nāma dṛṣṭādṛṣṭa bhogeṣu doṣadarśanābhyāsāt vaitṛṣṇyaṃ, tena ca vairāgyeṇa gṛhyate vikṣeparūpaḥ pracāraḥ cittasya. evaṃ tat manaḥ gṛhyate nigṛhyate, nirudhyate ityarthaḥ.", "tr": "'Without doubt, mighty-armed…' Without doubt — there is no doubt that the mind is hard to restrain and restless, mighty-armed. But by practice: practice is the repeated activity of the mind of the same kind in regard to some chosen ground of thought. Dispassion is freedom from thirst for enjoyments, seen and unseen, through repeatedly seeing their faults. By that dispassion the distracting movement of the mind is checked. Thus that mind is grasped, restrained, checked, that is."},
           ]),
        _v([
            "asaṃyatātmanā yogo duṣprāpa iti me matiḥ |",
            "vaśyātmanā tu yatatā śakyo'vāptumupāyataḥ",
        ], "|| 36 ||",
           "Yoga is hard to attain for one who is not self-controlled, I agree; but it can be attained by the right means by one who is self-controlled and strives.",
           bhashya=[
               {"text": "yaḥ punaḥ asaṃyatātmā, tena –", "intro": True, "tr": "But for one whose self is not restrained —"},
               {"text": "asaṃyatātmanā iti. asaṃyatātmanā abhyāsa vairāgyābhyām asaṃyataḥ ātmā antaḥkaraṇaṃ yasya saḥ ayam asaṃyatātmā, tena asaṃyatātmanā yogaḥ duṣprāpaḥ duḥkhena prāpyate iti me matiḥ. yaḥ tu punaḥ vaśyātmā abhyāsa vairāgyābhyāṃ vaśyatvam āpāditaḥ ātmā manaḥ yasya saḥ ayaṃ vaśyātmā. tena vaśyātmanā tu yatatā bhūyopi prayatnaṃ kurvatā, śakyaḥ avāptuṃ yogaḥ, upāyataḥ yathoktāt upāyāt.", "tr": "'For one whose self is unrestrained…' For one whose self, inner organ, has not been restrained by practice and dispassion, yoga is hard to attain, is attained with difficulty: this is my view. But by one whose self is controlled — whose self, the mind, has been brought under control by practice and dispassion — and who strives, makes effort again and again, yoga can be attained through the means, through the means described."},
           ]),
        {"speaker": "arjuna uvāca"},
        _v([
            "ayatiḥ śraddhayopeto yogāccalitamānasaḥ |",
            "aprāpya yogasaṃsiddhiṃ kāṃ gatiṃ kṛṣṇa gacchati",
        ], "|| 37 ||",
           "Arjuna said: One who has faith but does not strive, whose mind has strayed from yoga without attaining perfection in it — what end does he reach, Kṛṣṇa?",
           bhashya=[
               {"text": "tatra yogābhyāsāṅgīkaraṇena ihaloka paralokaprāptinimittāni karmāṇi sannyastāni yogasiddhi phalaṃ ca mokṣasādhanaṃ samyagdarśanaṃ na prāptam iti, yogī yogamārgāt maraṇakāle calitacittaḥ iti tasya nāśam āśaṅkya –", "intro": True, "tr": "Here, by taking up the practice of yoga, the actions that are the means of attaining this world and the next have been renounced; and the fruit of success in yoga, right vision, the means of liberation, has not been attained; and the yogin's mind has strayed from the path of yoga at the time of death. Fearing his ruin, [Arjuna asks]:"},
               {"text": "ayatiriti. ayatiḥ aprayatnavān yogamārge, śraddhayā āstikyabuddhyā ca upetaḥ, yogāt antakāle'pi calitaṃ mānasaṃ manaḥ yasya saḥ calitamānasaḥ bhraṣṭasmṛtiḥ saḥ aprāpya yogasaṃsiddhiṃ yogaphalaṃ samyagdarśanaṃ kāṃ gatiṃ he kṛṣṇa gacchati?", "tr": "'One who is not a striver, though endowed with faith…' One who does not strive, does not make effort, on the path of yoga, though endowed with faith, with belief in the unseen; whose mind has strayed from yoga even at the time of death, whose memory has failed — not having attained the perfection of yoga, its fruit, right vision, to what end does he go, O Kṛṣṇa?"},
           ]),
        _v([
            "kaccinnobhayavibhraṣṭaśchinnābhramiva naśyati |",
            "apratiṣṭho mahābāho vimūḍho brahmaṇaḥ pathi",
        ], "|| 38 ||",
           "Fallen from both, does he not perish like a scattered cloud, mighty-armed one, without support and bewildered on the path to Brahman?",
           bhashya=[
               {"text": "kaccit iti– kaccit kim, na ubhayavibhraṣṭaḥ karmamārgāt yogamārgācca vibhraṣṭaḥ san, chinnābhram iva, naśyati, kiṃ vā na naśyati, apratiṣṭhaḥ nirāśrayaḥ he mahābāho! vimūḍhaḥ san, brahmaṇaḥ pathi brahma prāpti mārge.", "tr": "'Does he not, fallen from both…' Does he not, fallen from both — from the path of action and from the path of yoga — perish like a broken cloud? Or does he not perish? Without support, without a refuge, mighty-armed, deluded on the path of Brahman, on the path to the attainment of Brahman."},
           ]),
        _v([
            "etanme saṃśayaṃ kṛṣṇa chettumarhasyaśeṣataḥ |",
            "tvadanyaḥ saṃśayasyāsya cchettā na hyupapadyate",
        ], "|| 39 ||",
           "You must dispel this doubt of mine completely, Kṛṣṇa; for there is no one but you who can dispel it.",
           bhashya=[
               {"text": "etaditi : etat me mama saṃśayaṃ, kṛṣṇa, chettum apanetum, arhasi, aśeṣataḥ, tvadanyaḥ, tvattaḥ anyaḥ ṛṣiḥ devaḥ vā, chettā nāśayitā saṃśayasya asya na hi yasmāt, upapadyate na sambhavati. ataḥ tvameva chettum arhasi ityarthaḥ.", "tr": "'This doubt of mine, Kṛṣṇa…' This doubt of mine, Kṛṣṇa, you should cut, remove, entirely; for other than you — any sage or god other than you — no destroyer of this doubt is possible. So you alone should cut it — that is the meaning."},
           ]),
        {"speaker": "śrī bhagavānuvāca"},
        _v([
            "pārtha naiveha nāmutra vināśastasya vidyate |",
            "na hi kalyāṇakṛtkaściddurgatiṃ tāta gacchati",
        ], "|| 40 ||",
           "The Blessed Lord said: Neither here nor hereafter is there ruin for him, Pārtha; for no one who does good, my friend, comes to an evil end.",
           bhashya=[
               {"text": "pārtheti – he pārtha! na eva, iha loke, na amutra parasmin vā loke, vināśaḥ tasya vidyate nāsti. nāśaḥ nāma pūrvasmāt hīnajanmaprāptiḥ. saḥ tasya yogabhraṣṭasya nāsti. na hi yasmāt, kalyāṇakṛt śubhakṛt, kaścit, durgatiṃ kutsitāṃ gatiṃ, he tāta! tanotyātmānaṃ putrarūpeṇa iti pitā tātaḥ ucyate, pitaiva putraḥ iti putro'pi tātaḥ ucyate; śiṣyo'pi putravat iti aputro'pi tātaḥ ucyate. yataḥ na gacchati.", "tr": "'Pārtha, neither here nor hereafter…' Pārtha, neither in this world nor in the other world is there ruin for him. Ruin means attaining a birth lower than the previous one; that does not happen to him who has fallen from yoga. For no one who does good goes to a bad, contemptible, end, dear one. 'Tāta' is the father, because he extends himself in the form of a son; and since the father is the son, the son too is called tāta; and since a disciple is like a son, even one who is not a son is called tāta. For he does not go [to a bad end]."},
           ]),
        _v([
            "prāpya puṇyakṛtāṃ lokānuṣitvā śāśvatīḥ samāḥ |",
            "śucīnāṃ śrīmatāṃ gehe yogabhraṣṭo'bhijāyate",
        ], "|| 41 ||",
           "Having reached the worlds of the doers of merit and dwelt there for countless years, one who has fallen from yoga is born in the house of the pure and prosperous.",
           bhashya=[
               {"text": "kiṃ tu asya bhavati?", "intro": True, "tr": "What, then, becomes of him?"},
               {"text": "prāpya iti. yogamārge pravṛttaḥ sannyāsī, sāmarthyāt, prāpya gatvā, puṇyakṛtām aśvamedhādi yājināṃ lokān, tatra ca, uṣitvā vāsam anubhūya, śāśvatīḥ nityāḥ samāḥ saṃvatsarān, tadbhogakṣaye śucīnām yathoktakāriṇāṃ śrīmatāṃ vibhūtimatāṃ gehe gṛhe yogabhraṣṭaḥ abhijāyate.", "tr": "'Having reached the worlds of the righteous…' The renouncer who had set out on the path of yoga — this is implied — having reached, gone to, the worlds of the righteous, of those who perform the horse sacrifice and the like, and having dwelt there, enjoyed his stay, for endless, perpetual years, at the end of that enjoyment is born, the one fallen from yoga, in the home of the pure — of those who act as enjoined — and the prosperous, the wealthy."},
           ]),
        _v([
            "athavā yogināmeva kule bhavati dhīmatām |",
            "etaddhi durlabhataraṃ loke janma yadīdṛśam",
        ], "|| 42 ||",
           "Or he is born in a family of wise yogins; but a birth such as this is harder to obtain in the world.",
           bhashya=[
               {"text": "athaveti – athavā śrīmatāṃ kulāt anyasmin yogināmeva daridrāṇāṃ kule bhavati jāyate, dhīmatāṃ buddhimatām. etat hi janma, yat daridrāṇāṃ yogināṃ kule, durlabhataraṃ duḥkhalabhyataraṃ, pūrvam apekṣya, loke janma yat īdṛśaṃ yathokta viśeṣaṇe kule.", "tr": "'Or else he is born in a family of yogins…' Or else, in a family other than that of the prosperous, he is born in a family of poor yogins, wise, intelligent. For this birth, in a family of poor yogins, is harder to gain, more difficult to obtain, than the former; such a birth in the world, in a family with the qualities described."},
           ]),
        _v([
            "tatra taṃ buddhisaṃyogaṃ labhate paurvadehikam |",
            "yatate ca tato bhūyaḥ saṃsiddhau kurunandana",
        ], "|| 43 ||",
           "There he regains the understanding cultivated in his former body, and strives on from there once more towards perfection, O joy of the Kurus.",
           bhashya=[
               {"text": "yasmāt ca –", "intro": True, "tr": "And because —"},
               {"text": "tatra iti. tatra yogināṃ kule taṃ, buddhisaṃyogaṃ buddhyā saṃyogaṃ buddhisaṃyogaṃ, labhate paurvadehikaṃ pūrvasmin dehe bhavaṃ paurvadehikaṃ. yatate ca prayatnaṃ karoti, ca tataḥ tasmāt pūrvakṛtāt saṃskārāt bhūyaḥ bahutaraṃ, saṃsiddhau saṃsiddhi nimittaṃ he kurunandana!", "tr": "'There he regains that union of understanding…' There, in the family of yogins, he gains that union of understanding — union with the understanding — from his former body, belonging to the former body; and from then on, from that impression formed before, he strives, makes effort, still more, for perfection, for the sake of perfection, joy of the Kurus."},
           ]),
        _v([
            "pūrvābhyāsena tenaiva hriyate hyavaśo'pi saḥ |",
            "jijñāsurapi yogasya śabdabrahmātivartate",
        ], "|| 44 ||",
           "By that former practice he is carried on even against his will. Even one who merely wishes to know yoga passes beyond the word-Brahman of the Veda.",
           bhashya=[
               {"text": "kathaṃ pūrvadeha buddhisaṃyogaḥ iti? tat ucyate–", "intro": True, "tr": "How is there union with the understanding of the former body? That is told:"},
               {"text": "pūrvābhyāsena iti. yaḥ pūrvajanmani kṛtaḥ abhyāsaḥ saḥ pūrvā'bhyāsaḥ, tenaiva balavatā hriyate, saṃsiddhau hi yasmāt, avaśaḥ api, saḥ yogabhraṣṭaḥ; tena kṛtaṃ cet yogābhyāsajāt saṃskārāt balavattaram dharmādilakṣaṇaṃ karma, tadā yogābhyāsajanitena saṃskāreṇāhriyate; adharmaścedbalavattaraḥ kṛtaḥ, tena yogajaḥ api saṃskāraḥ abhibhūyate eva, tat kṣaye tu yogajaḥ saṃskāraḥ svayameva kāryam ārabhate. na dīrghakālasthasyāpi vināśaḥ tasya asti ityarthaḥ. ataḥ jijñāsuḥ api yogasya svarūpaṃ jñātum icchan yogamārge pravṛttaḥ – sannyāsī yogabhraṣṭaḥ, sāmarthyāt, saḥ api, śabdabrahma vedoktakarmānuṣṭhānaphalam ativartate, atikrāmati apākariṣyati, kimuta buddhvā yaḥ yogaṃ tanniṣṭhaḥ abhyāsaṃ kuryāt.", "tr": "'By that same former practice…' The practice done in a former birth is former practice; by that powerful practice he is carried along to perfection, even against his will — he who has fallen from yoga. If action marked by merit and the rest, stronger than the impression born of the practice of yoga, has been done by him, he is not carried along by the impression born of the practice of yoga; if stronger demerit has been done, even the impression born of yoga is overpowered; but when that is exhausted, the impression born of yoga by itself begins its effect. There is no destruction of it, even if it lasts a long time — that is the meaning. Therefore even one who wishes to know yoga — desiring to know its nature, having set out on the path of yoga — the renouncer fallen from yoga, this is implied — even he passes beyond, surpasses, sets aside, the word-Brahman, the fruit of performing the actions taught in the Veda; how much more one who, having understood yoga, is steadfast in it and practises it."},
           ]),
        _v([
            "prayatnādyatamānastu yogī saṃśuddhakilbiṣaḥ |",
            "anekajanmasaṃsiddhastato yāti parāṃ gatim",
        ], "|| 45 ||",
           "But the yogin who strives with effort, cleansed of sin, perfected through many births, then reaches the highest goal.",
           bhashya=[
               {"text": "kutaśca yogitvaṃ śreyaḥ iti?", "intro": True, "tr": "And why is being a yogin better?"},
               {"text": "prayatnāditi. prayatnāt yatamānaḥ adhikataraṃ yatamānaḥ ityarthaḥ. tatra “yogī” vidvān saṃśuddhakilbiṣaḥ viśuddha kilbiṣaḥ saṃśuddhapāpaḥ aneka janmasaṃsiddhaḥ anekeṣu janmasu kiñcit kiñcit saṃskārajātam upacitya tena upacitena anekajanmakṛtena, saṃsiddhaḥ aneka janma saṃsiddhaḥ tataḥ labdha samyagdarśanaḥ san yāti, parāṃ prakṛṣṭāṃ gatim.", "tr": "'But the yogin striving with effort…' Striving with effort: striving more and more, that is. Then the yogin, the wise one, his sins cleansed, his evil purified, perfected through many births — having gathered a little of the store of impressions in each of many births, perfected by that store gathered over many births — and then having gained right vision, goes to the supreme, the highest, goal."},
           ]),
        _v([
            "tapasvibhyo'dhiko yogī jñānibhyo'pi mato'dhikaḥ |",
            "karmibhyaścādhiko yogī tasmādyogī bhavārjuna",
        ], "|| 46 ||",
           "The yogin is greater than the ascetics, and deemed greater even than the learned; the yogin is greater than those devoted to ritual action. Therefore be a yogin, Arjuna.",
           bhashya=[
               {"text": "yasmāt evaṃ tasmāt –", "intro": True, "tr": "Since it is so, therefore —"},
               {"text": "tapasvibhya iti. tapasvibhyaḥ adhikaḥ yogī, jñānibhyaḥ api, jñānam atra śāstrārthapāṇḍityaṃ, tadvadbhyo'pi mataḥ jñātaḥ, adhikaḥ śreṣṭhaḥ iti. karmibhyaḥ, agnihotrādi karma, tadvadbhyaḥ adhikaḥ yogī viśiṣṭaḥ. yasmāt tasmāt yogī bhava arjuna.", "tr": "'The yogin is greater than ascetics…' The yogin is greater than ascetics; greater even than men of knowledge — knowledge here is learning in the meaning of the scriptures — even than those who have it he is held, known, to be greater, superior; than men of action — action such as the agnihotra — than those who have it the yogin is greater, superior. Since it is so, become a yogin, Arjuna."},
           ]),
        _v([
            "yogināmapi sarveṣāṃ madgatenāntarātmanā |",
            "śraddhāvān bhajate yo māṃ sa me yuktatamo mataḥ",
        ], "|| 47 ||",
           "And of all yogins, he who worships me with faith, his inmost self absorbed in me, I hold to be the most disciplined.",
           bhashya=[
               {"text": "yogināmiti – yogināmapi sarveṣāṃ rudrādityādi dhyānaparāṇāṃ madhye, madgatena – mayi vāsudeve samāhitena, antarātmanā, antaḥkaraṇena, śraddhāvān śraddadhānaḥ san bhajate sevate yaḥ māṃ, saḥ me mama yuktatamaḥ atiśayena yuktaḥ mataḥ abhipretaḥ iti.", "tr": "'And of all yogins…' And of all yogins — among those devoted to meditation on Rudra, the Ādityas and the rest — he who, full of faith, having faith, worships, serves, me with his inner self gone to me, with his inner organ collected in me, Vāsudeva — him I hold, consider, the most disciplined, disciplined beyond all."},
           ]),
        "ornament",
        {"colophon": "iti śrī mahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītā– sūpaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjuna saṃvāde dhyānayogo nāma ṣaṣṭho– dhyāyaḥ", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the sixth chapter, Dhyāna Yoga."},
        {"colophon": "iti śrīmatparamahaṃsa parivrājakācāryagovindabhagavatpūjyapādaśiṣya śrīmacchaṅkarabhagavataḥ kṛtau śrīmadbhavadgītābhāṣye dhyānayogo nāma ṣaṣṭho'dhyāyaḥ.", "gloss": "Thus ends the sixth chapter, Dhyāna Yoga, of the commentary on the Bhagavad Gītā composed by Śrī Śaṅkara Bhagavat, wandering ascetic of the highest order and disciple of Śrī Govinda Bhagavatpāda."},
    ],
}
