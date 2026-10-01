# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhagavad Gītā, chapter 1 (Arjunaviṣāda Yoga), with Śaṅkara's bhāṣya. The Sanskrit
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
    "doc_title": "Bhagavad Gītā 1 · Arjunaviṣāda Yoga · Śaṅkara Bhāṣya",
    "app_title": "Gītā 1",
    "h1": "Bhagavad Gītā · Chapter 1",
    "subtitle": "Arjunaviṣāda Yoga · Arjuna's despondency · with Śaṅkara's bhāṣya",
    "note": "The Gītā opens on the field of Kurukṣetra, where Sañjaya describes the two armies to the blind king Dhṛtarāṣṭra and Arjuna, seeing his own kin arrayed for battle, sinks into grief. The page opens with the traditional preamble to a recitation — the viniyoga and nyāsa, the Gītā dhyāna, the guru stuti and the phalaśruti from the Mahābhārata. Śaṅkara does not comment on this chapter; his introduction to the whole work (upodghāta) stands at the head of the page, and his commentary proper begins at 2.10. The bhāṣya folds hold the Sanskrit commentary with an English rendering under each paragraph; the verse and commentary translations are original, made from the Sanskrit.",
    "footer": "Source: Śrīmad Bhagavadgītā Śaṅkarabhāṣyamu (Ramakrishna Math, Hyderabad, 2013), Sanskrit mūla and bhāṣya only, collated with Sanskrit Wikisource and the Pullela Śrīrāmacandruḍu edition; translations original. See SOURCES §7.4.",
    "nav": [('all chapters', '../../index.html#gita'), ('chapter 2 ›', 'gita-bhashya-02-iast.html')],
    "sections": [
        {"heading": "Pūrvāṅga · viniyoga and nyāsa"},
        dict(_v(["oṃ asya śrībhagavadgītāśāstramahāmantrasya bhagavān vedavyāsaḥ ṛṣiḥ, anuṣṭup chandaḥ, śrīkṛṣṇaparamātmā devatā, “aśocyānanvaśocastvaṃ prajñāvādāṃśca bhāṣase” iti bījam, “sarvadharmān parityajya māmekaṃ śaraṇaṃ vraja” iti śaktiḥ, “ahaṃ tvā sarvapāpebhyo mokṣayiṣyāmi māśucaḥ” iti kīlakam |"], "", "Oṃ. Of this great mantra, the scripture of the sacred Bhagavad Gītā, the seer is the blessed Vedavyāsa, the metre anuṣṭubh, and the deity Śrī Kṛṣṇa, the supreme Self. 'You grieve for those who should not be grieved for, yet speak words of wisdom' (2.11) is its seed; 'Abandoning all dharmas, take refuge in me alone' (18.66) is its power; 'I will release you from all sins; do not grieve' (18.66) is its pin, which holds it fast."), prose=True),
        dict(_v(["“nainaṃ chindanti śastrāṇi nainaṃ dahati pāvakaḥ” ityaṅguṣṭhābhyāṃ namaḥ | “na cainaṃ kledayantyāpo na śoṣayati mārutaḥ” iti tarjanībhyāṃ namaḥ | “acchedyo'yamadāhyo'yamakledyo'śoṣya eva ca” iti madhyamābhyāṃ namaḥ | “nityaḥ sarvagataḥ sthāṇuracalo'yaṃ sanātanaḥ” ityanāmikābhyāṃ namaḥ | “paśya me pārtha rūpāṇi śataśo'tha sahasraśaḥ” iti kaniṣṭhikābhyāṃ namaḥ | “nānāvidhāni divyāni nānāvarṇākṛtīni ca” iti karatalakarapṛṣṭhābhyāṃ namaḥ | iti karanyāsaḥ ||"], "", "The placing on the hands: with 'Weapons do not cut it, fire does not burn it' (2.23), salutation to the thumbs; with 'water does not wet it, wind does not dry it', to the forefingers; with 'It cannot be cut, burnt, wetted or dried' (2.24), to the middle fingers; with 'It is eternal, all-pervading, stable, unmoving, everlasting', to the ring fingers; with 'Behold, Pārtha, my forms by hundreds and thousands' (11.5), to the little fingers; with 'various and divine, of many colours and shapes', to the palms and the backs of the hands."), prose=True),
        dict(_v(["“nainaṃ chindanti śastrāṇi nainaṃ dahati pāvakaḥ” iti hṛdayāya namaḥ | “na cainaṃ kledayantyāpo na śoṣayati mārutaḥ” iti śirase svāhā | “acchedyo'yamadāhyo'yamakledyo'śoṣya eva ca” iti śikhāyai vaṣaṭ | “nityaḥ sarvagataḥ sthāṇuracalo'yaṃ sanātanaḥ” iti kavacāya hum | “paśya me pārtha rūpāṇi śataśo'tha sahasraśaḥ” iti netratrayāya vauṣaṭ | “nānāvidhāni divyāni nānāvarṇākṛtīni ca” iti astrāya phaṭ | “bhūrbhuvassuvarom” iti digbandhaḥ ||"], "", "The placing on the limbs, with the same six lines: to the heart, namaḥ; to the head, svāhā; to the tuft of hair, vaṣaṭ; to the armour, hum; to the three eyes, vauṣaṭ; to the weapon, phaṭ. With 'bhūr bhuvas suvar om' the quarters are sealed."), prose=True),
        dict(_v(["oṃ śrīkṛṣṇaprītyarthe gītāpārāyaṇe (jape vā) viniyogaḥ ||"], "", "Oṃ. This is undertaken in the recitation of the Gītā — or in its silent repetition — for the pleasure of Śrī Kṛṣṇa."), prose=True),
        {"heading": "Gītā dhyānam"},
        _v([
            "pārthāya pratibodhitāṃ bhagavatā nārāyaṇena svayaṃ",
            "vyāsena grathitāṃ purāṇamuninā madhye mahābhāratam |",
            "advaitāmṛtavarṣiṇīṃ bhagavatīmaṣṭādaśādhyāyinīṃ",
            "amba tvāmanusandadhāmi bhagavadgīte bhavadveṣiṇīm",
        ], "|| 1 ||",
           "O Mother, O Bhagavad Gītā — taught to Pārtha by the Lord Nārāyaṇa himself, woven by the ancient sage Vyāsa into the midst of the Mahābhārata, showering the nectar of non-duality, divine, in eighteen chapters, the destroyer of rebirth — on you I meditate."),
        _v([
            "namo'stu te vyāsa viśālabuddhe",
            "phullāravindāyatapatranetra |",
            "yena tvayā bhāratatailapūrṇaḥ",
            "prajvālito jñānamayaḥ pradīpaḥ",
        ], "|| 2 ||",
           "Salutation to you, Vyāsa of vast understanding, whose eyes are long as the petals of a full-blown lotus, by whom the lamp of knowledge, filled with the oil of the Bhārata, was kindled."),
        _v([
            "prapannapārijātāya totravetraikapāṇaye |",
            "jñānamudrāya kṛṣṇāya gītāmṛtaduhe namaḥ",
        ], "|| 3 ||",
           "Salutation to Kṛṣṇa — the wish-granting tree of those who take refuge in him, who holds the cowherd's goad in one hand and shows the sign of knowledge with the other — the milker of the nectar of the Gītā."),
        _v([
            "sarvopaniṣado gāvo dogdhā gopālanandanaḥ |",
            "pārtho vatsaḥ sudhīrbhoktā dugdhaṃ gītāmṛtaṃ mahat",
        ], "|| 4 ||",
           "The Upaniṣads are the cows; the milker is the son of the cowherd; Pārtha is the calf; the wise one is the drinker; and the milk is the great nectar of the Gītā."),
        {"heading": "Guru stuti"},
        _v([
            "vasudevasutaṃ devaṃ kaṃsacāṇūramardanam |",
            "devakīparamānandaṃ kṛṣṇaṃ vande jagadgurum",
        ], "|| 1 ||",
           "I bow to Kṛṣṇa, the teacher of the world — the divine son of Vasudeva, the slayer of Kaṃsa and Cāṇūra, the supreme joy of Devakī."),
        _v([
            "kṛṣṇadvaipāyanaṃ vyāsaṃ sarvalokahite ratam |",
            "vedābjabhāskaraṃ vande śamādinilayaṃ munim",
        ], "|| 2 ||",
           "I bow to Vyāsa, Kṛṣṇa Dvaipāyana, the sage devoted to the good of all the worlds, the sun that opens the lotus of the Veda, the dwelling-place of calm and the other virtues."),
        _v([
            "śrutismṛti purāṇānāmālayaṃ karuṇālayam |",
            "namāmi bhagavatpādaṃ śaṅkaraṃ lokaśaṅkaram",
        ], "|| 3 ||",
           "I bow to Śaṅkara Bhagavatpāda, the home of the Veda, the smṛtis and the Purāṇas, the home of compassion, who brings blessing to the world."),
        _v([
            "gururbrahmā gururviṣṇuḥ gururdevo maheśvaraḥ |",
            "gurussākṣāt parabrahma tasmai śrīgurave namaḥ",
        ], "|| 4 ||",
           "The guru is Brahmā, the guru is Viṣṇu, the guru is the god Maheśvara; the guru is the supreme Brahman itself. Salutation to that revered guru."),
        _v([
            "ajñānatimirāndhasya jñānāñjanaśalākayā |",
            "cakṣurunmīlitaṃ yena tasmai śrīgurave namaḥ",
        ], "|| 5 ||",
           "Salutation to that revered guru who, with the salve-stick of knowledge, opened the eyes of one blinded by the darkness of ignorance."),
        {"heading": "Gītā māhātmyam · phalaśruti (Mahābhārata 6.43.1–5)"},
        {"speaker": "vaiśampāyana uvāca"},
        _v([
            "gītā sugītā kartavyā kimanyaiḥ śāstrasaṃgrahaiḥ |",
            "yā svayaṃ padmanābhasya mukhapadmādviniḥsṛtā",
        ], "|| 1 ||",
           "Vaiśampāyana said: The Gītā should be well sung — what need of other compendia of scripture? For it came forth from the lotus-mouth of Padmanābha himself."),
        _v([
            "sarvaśāstramayī gītā sarvadevamayo hariḥ |",
            "sarvatīrthamayī gaṅgā sarvadevamayo manuḥ",
        ], "|| 2 ||",
           "The Gītā holds all the scriptures, as Hari holds all the gods, as the Gaṅgā holds all the holy fords, and as Manu holds all the gods."),
        _v([
            "gītā gaṅgā ca gāyatrī govindeti hṛdi sthite |",
            "caturgakārasaṃyukte punarjanma na vidyate",
        ], "|| 3 ||",
           "When the four words that begin with g — Gītā, Gaṅgā, Gāyatrī and Govinda — dwell in the heart, there is no rebirth."),
        _v([
            "ṣaṭśatāni saviṃśāni ślokānāṃ prāha keśavaḥ |",
            "arjunaḥ saptapañcāśat saptaṣaṣṭiṃ tu sañjayaḥ",
        ], "|| 4 ||",
           "Six hundred and twenty ślokas Keśava spoke; Arjuna fifty-seven; Sañjaya sixty-seven;"),
        _v([
            "dhṛtarāṣṭraḥ ślokamekaṃ gītāyā mānamucyate |",
            "bhāratāmṛtasarvasvagītāyā mathitasya ca |",
            "sāramuddhṛtya kṛṣṇena arjunasya mukhe hutam",
        ], "|| 5 ||",
           "and Dhṛtarāṣṭra one: this is said to be the measure of the Gītā. Churning the Gītā, the whole wealth of the nectar of the Bhārata, Kṛṣṇa drew out its essence and poured it into Arjuna's mouth as an offering."),
        "ornament",
        {"heading": "Śaṅkara's introduction"},
        {"bhashya": [
            {"text": "nārāyaṇaḥ paro'vyaktāt aṇḍamavyakta sambhavam | aṇḍasyāntastvime lokāḥ saptadvīpā ca medinī ||", "tr": "Nārāyaṇa is beyond the Unmanifest; from the Unmanifest the cosmic egg is born. Within the egg are these worlds, and the earth with its seven continents."},
            {"text": "sa bhagavān sṛṣṭvedaṃ jagat tasya ca sthitiṃ cikīrṣuḥ, marīcyādīn agre sṛṣṭvā prajāpatīn, pravṛttilakṣaṇaṃ dharmaṃ grāhayāmāsa vedoktam. tataḥ anyān ca sanakasanandanādīn utpādya, nivṛttilakṣaṇaṃ dharmaṃ jñānavairāgyalakṣaṇaṃ grāhayāmāsa. dvividho hi vedoktodharmaḥ, pravṛttilakṣaṇaḥ nivṛttilakṣaṇaśca, jagataḥ sthitikāraṇam. prāṇināṃ sākṣāt abhyudaya niśśreyasahetuḥ yaḥ sa dharmaḥ brāhmaṇādyaiḥ varṇibhiḥ āśramibhiḥ śreyorthibhiḥ anuṣṭhīyamānaḥ. dīrgheṇa kālena anuṣṭhātṝṇāṃ kāmodbhavāt hīyamānavivekavijñānahetukena adharmeṇa abhibhūyamāne dharme pravarthamāne ca adharme, jagataḥ sthitiṃ paripipālayiṣuḥ saḥ ādikartā nārāyaṇākhyaḥ viṣṇuḥ bhaumasya brahmaṇaḥ brāhmaṇatvasya rakṣaṇārthaṃ devakyāṃ vasudevāt aṃśena kṛṣṇaḥ kila sambabhūva. brāhmaṇatvasya hi rakṣaṇe rakṣitaḥ syāt vaidiko dharmaḥ tadadhīnatvāt varṇāśramabhedānām.", "tr": "That Lord, having created this world and wishing to maintain it, first created Marīci and the other lords of creatures and had them take up the dharma of engagement (pravṛtti) taught in the Veda. Then he brought forth others — Sanaka, Sanandana and the rest — and had them take up the dharma of withdrawal (nivṛtti), marked by knowledge and dispassion. For the dharma taught in the Veda is twofold, marked by engagement and by withdrawal, and it is the cause of the world's stability. That dharma, which is directly the cause of both worldly prosperity and the highest good for living beings, is practised by brāhmaṇas and the other classes and by those in the stages of life who seek the good. Over a long time, as desire arose in those who practised it, their discrimination and understanding declined; adharma, so caused, overpowered dharma and adharma increased. Then the first creator, Viṣṇu called Nārāyaṇa, wishing to preserve the stability of the world, was born — as is well known — as Kṛṣṇa, a portion of himself, of Vasudeva through Devakī, to protect the Brahman on earth, that is, brāhmaṇahood. For by protecting brāhmaṇahood the Vedic dharma is protected, since the distinctions of class and stage of life depend on it."},
            {"text": "sa ca bhagavān jñānaiśvaryaśaktibalavīryatejobhiḥ sadā sampannaḥ triguṇātmikāṃ vaiṣṇavīṃ svāṃ māyāṃ mūlaprakṛtiṃ vaśīkṛtya, ajaḥ, avyayaḥ bhūtānāṃ īśvaraḥ nityaḥ śuddhabuddhamuktasvabhāvaḥ api san, svamāyayā dehavān iva jātaḥ iva ca lokānugrahaṃ kurvanniva lakṣyate. svaprayojanā'bhāve'pi bhūtānugrahajighṛkṣayā vaidikaṃ dharmadvayaṃ arjunāya śokamohamahodadhau nimagnāya upadideśa, guṇādhikaiḥ hi gṛhītaḥ anuṣṭhīyamānaśca dharmaḥ pracayaṃ gamiṣyatīti. taṃ dharmaṃ bhagavatā yathopadiṣṭaṃ vedavyāsaḥ sarvajñaḥ bhagavān gītākhyaiḥ saptabhiḥ ślokaśataiḥ upanibabandha.", "tr": "That Lord, ever endowed with knowledge, sovereignty, power, strength, vigour and splendour, having brought under his control his own Vaiṣṇavī māyā, made of the three guṇas — primal nature — is seen, though unborn, imperishable, the lord of beings, eternally pure, awake and free by nature, as if embodied and as if born through his own māyā, as if to show favour to the world. Though he had no purpose of his own, wishing only to help beings, he taught this twofold Vedic dharma to Arjuna, who was sunk in a great ocean of grief and delusion — for a dharma taken up and practised by those of excellent qualities will spread. That dharma, as the Lord taught it, the omniscient and venerable Vedavyāsa set down in the seven hundred verses called the Gītā."},
            {"text": "tat idaṃ gītāśāstraṃ samasta vedārthasāra saṅgrahabhūtaṃ durvijñeyārthaṃ tadarthāviṣkaraṇāya anekaiḥ vivṛtapadapadārthavākyārthanyāyam api atyantaviruddhānekārthatvena laukikaiḥ gṛhyamāṇaṃ upalabhya ahaṃ vivekataḥ arthanirthāraṇārthaṃ saṅkṣepataḥ vivaraṇaṃ kariṣyāmi.", "tr": "This scripture, the Gītā, is a compendium of the essence of the meaning of the whole Veda, and its meaning is hard to grasp. Many have explained its words, their meanings, its sentences, their import and its reasoning, in order to bring out that meaning; yet I find that people take it to have many meanings that are entirely at odds with one another. So I shall write a brief explanation, in order to determine its meaning with discernment."},
            {"text": "tasya asya gītāśāstrasya saṅkṣepataḥ prayojanaṃ paraṃ niśśreyasaṃ sahetukasya saṃsārasya atyantoparamalakṣaṇam tacca sarvakarmasannyāsapūrvakāt ātmajñānaniṣṭhārūpāt dharmāt bhavati. tathā imaṃ evaṃ gītārthaṃ dharmaṃ uddiśya bhagavatā eva uktam – “sa hi dharmaḥ suparyāpto brahmaṇaḥ padavedane” (ma.bhā.aśva. 16.12) iti anugītāsu. tatraiva ca uktam. “naiva dharmī na cādharmī na caiva hi śubhāśubhī” (ma.bhā. aśva.19.7) “yaḥ syādekāsane līnaḥ tūṣṇīṃ kiñcadacintayan” (ma.bhā.aśva.19.1) “jñānaṃ sannyāsalakṣaṇam” (ma.bhā.aśva.43.25) iti ca. ihāpi ante uktaṃ arjunāya“sarvadharmān parityajya māmekaṃ śaraṇaṃ vraja” (18.66) iti.", "tr": "The purpose of this scripture, in brief, is the highest good: the complete cessation of transmigratory existence together with its cause. And that comes from the dharma that consists in steadfastness in the knowledge of the Self, preceded by the renunciation of all action. With this very dharma, the meaning of the Gītā, in view, the Lord himself said in the Anugītā: 'That dharma is fully sufficient for reaching the state of Brahman' (Mahābhārata, Aśvamedha 16.12). And there too he said: 'He is neither virtuous nor unvirtuous, nor subject to good and evil' (19.7), 'he who, absorbed on a single seat, remains silent, thinking of nothing' (19.1), and 'knowledge is marked by renunciation' (43.25). Here too, at the end, he tells Arjuna: 'Abandoning all dharmas, take refuge in me alone' (18.66)."},
            {"text": "abhyudayārtho'pi yaḥ pravṛttilakṣaṇaḥ dharmaḥ varṇān āśramāṃśca uddiśya vihitaḥ sa devādisthānaprāptihetuḥ api san, īśvarārpaṇabuddhyā anuṣṭhīyamānaḥ sattvaśuddhaye bhavati phalābhisandhivarjitaḥ. śuddhasattvasya ca jñānaniṣṭhāyogyatāprāptidvāreṇa jñānotpattihetutvena ca niśśreyasahetutvam api pratipadyate. tathā cemam eva artham abhisandhāya vakṣyati – “brahmaṇyādhāya karmāṇi” (5.10) “yoginaḥ karma kurvanti saṅgaṃ tyaktvātmaśuddhaye” (5.11) iti.", "tr": "The dharma of engagement, too, which aims at prosperity and is enjoined with reference to the classes and stages of life, though it is a cause of attaining the station of the gods and the like, leads to purity of mind when it is practised in the spirit of an offering to the Lord, without regard to its fruits. And for one whose mind is pure it becomes a cause of the highest good as well, by bringing fitness for steadfastness in knowledge and so giving rise to knowledge. With this very meaning in mind he will say: 'offering actions to Brahman' (5.10) and 'yogins perform action, giving up attachment, for the purification of the self' (5.11)."},
            {"text": "imaṃ dviprakāraṃ dharmaṃ niśśreyasaprayojanaṃ paramārthatattvaṃ ca vāsudevākhyaṃ parabrahmābhidheyabhūtaṃ viśeṣataḥ abhivyañjayat viśiṣṭaprayojanasambandhābhidheyavat gītāśāstram. yataḥ tadarthavijñāne samastapuruṣārthasiddhiḥ, ataḥ tadvivaraṇe yatnaḥ kriyate mayā.", "tr": "The Gītā-scripture sets forth in particular this twofold dharma, whose purpose is the highest good, and the supreme truth called Vāsudeva, the supreme Brahman, which is its subject; so it has a specific purpose, a specific relation and a specific subject. Since through understanding its meaning all the aims of human life are achieved, I undertake the effort of explaining it."},
        ], "summary": "Śaṅkara's introduction (upodghāta)"},
        {"heading": "Chapter 1 · Arjunaviṣāda Yoga"},
        {"speaker": "dhṛtarāṣṭra uvāca"},
        _v([
            "dharmakṣetre kurukṣetre samavetā yuyutsavaḥ |",
            "māmakāḥ pāṇḍavāścaiva kimakurvata sañjaya",
        ], "|| 1 ||",
           "Dhṛtarāṣṭra said: On the field of dharma, the field of the Kurus, gathered together and eager to fight — what did my sons and the sons of Pāṇḍu do, O Sañjaya?"),
        {"speaker": "sañjaya uvāca"},
        _v([
            "dṛṣṭvā tu pāṇḍavānīkaṃ vyūḍhaṃ duryodhanastadā |",
            "ācāryamupasaṅgamya rājā vacanamabravīt",
        ], "|| 2 ||",
           "Sañjaya said: Then King Duryodhana, seeing the army of the Pāṇḍavas drawn up in array, approached his teacher Droṇa and spoke these words."),
        _v([
            "paśyaitāṃ pāṇḍuputrāṇāmācārya mahatīṃ camūm |",
            "vyūḍhāṃ drupadaputreṇa tava śiṣyeṇa dhīmatā",
        ], "|| 3 ||",
           "Behold, O teacher, this mighty host of the sons of Pāṇḍu, marshalled by the son of Drupada, your own gifted pupil."),
        _v([
            "atra śūrā maheṣvāsā bhīmārjunasamā yudhi |",
            "yuyudhāno virāṭaśca drupadaśca mahārathaḥ",
        ], "|| 4 ||",
           "Here are heroes, great archers equal in battle to Bhīma and Arjuna — Yuyudhāna, Virāṭa, and Drupada, the mighty chariot-warrior;"),
        _v([
            "dhṛṣṭaketuścekitānaḥ kāśirājaśca vīryavān |",
            "purujit kuntibhojaśca śaibyaśca narapuṅgavaḥ",
        ], "|| 5 ||",
           "Dhṛṣṭaketu, Cekitāna and the valiant king of Kāśī; Purujit, Kuntibhoja, and Śaibya, a bull among men;"),
        _v([
            "yudhāmanyuśca vikrānta uttamaujāśca vīryavān |",
            "saubhadro draupadeyāśca sarva eva mahārathāḥ",
        ], "|| 6 ||",
           "valiant Yudhāmanyu and valiant Uttamaujas, the son of Subhadrā and the sons of Draupadī — all of them great chariot-warriors."),
        _v([
            "asmākaṃ tu viśiṣṭā ye tānnibodha dvijottama |",
            "nāyakā mama sainyasya sañjñārthaṃ tān bravīmi te",
        ], "|| 7 ||",
           "But know also the foremost among us, O best of the twice-born, the leaders of my army; I name them for your notice."),
        _v([
            "bhavān bhīṣmaśca karṇaśca kṛpaśca samitiñjayaḥ |",
            "aśvatthāmā vikarṇaśca saumadattirjayadrathaḥ",
        ], "|| 8 ||",
           "Yourself and Bhīṣma, Karṇa and Kṛpa, victorious in battle; Aśvatthāman, Vikarṇa, and the son of Somadatta too;"),
        _v([
            "anye ca bahavaḥ śūrāḥ madarthe tyaktajīvitāḥ |",
            "nānāśastrapraharaṇāḥ sarve yuddhaviśāradāḥ",
        ], "|| 9 ||",
           "and many other heroes, ready to give their lives for my sake, bearing many kinds of weapons, all of them skilled in war."),
        _v([
            "aparyāptaṃ tadasmākaṃ balaṃ bhīṣmābhirakṣitam |",
            "paryāptaṃ tvidameteṣāṃ balaṃ bhīmābhirakṣitam",
        ], "|| 10 ||",
           "This army of ours, guarded by Bhīṣma, is unbounded; but their army, guarded by Bhīma, is limited."),
        _v([
            "ayaneṣu ca sarveṣu yathābhāgamavasthitāḥ |",
            "bhīṣmamevābhirakṣantu bhavantaḥ sarva eva hi",
        ], "|| 11 ||",
           "So all of you, stationed at your posts at every point of entry, must above all protect Bhīṣma."),
        _v([
            "tasya sañjanayan harṣaṃ kuruvṛddhaḥ pitāmahaḥ |",
            "siṃhanādaṃ vinadyoccaiḥ śaṅkhaṃ dadhmau pratāpavān",
        ], "|| 12 ||",
           "Then, gladdening him, the mighty old Kuru, the grandsire, roared a lion's roar and blew his conch."),
        _v([
            "tataḥ śaṅkhāśca bheryaśca paṇavānakagomukhāḥ |",
            "sahasaivābhyahanyanta sa śabdastumulo'bhavat",
        ], "|| 13 ||",
           "Then conches, kettledrums, tabors, drums and horns sounded all at once, and the uproar was tremendous."),
        _v([
            "tataḥ śvetairhayairyukte mahati syandane sthitau |",
            "mādhavaḥ pāṇḍavaścaiva divyau śaṅkhau pradadhmatuḥ",
        ], "|| 14 ||",
           "Then, standing in their great chariot yoked with white horses, Mādhava and the son of Pāṇḍu blew their divine conches."),
        _v([
            "pāñcajanyaṃ hṛṣīkeśo devadattaṃ dhanañjayaḥ |",
            "pauṇḍraṃ dadhmau mahāśaṅkhaṃ bhīmakarmā vṛkodaraḥ",
        ], "|| 15 ||",
           "Hṛṣīkeśa blew Pāñcajanya, Dhanañjaya blew Devadatta, and Vṛkodara of terrible deeds blew the great conch Pauṇḍra."),
        _v([
            "anantavijayaṃ rājā kuntīputro yudhiṣṭhiraḥ |",
            "nakulaḥ sahadevaśca sughoṣamaṇipuṣpakau",
        ], "|| 16 ||",
           "King Yudhiṣṭhira, son of Kuntī, blew Anantavijaya; Nakula and Sahadeva blew Sughoṣa and Maṇipuṣpaka."),
        _v([
            "kāśyaśca parameṣvāsaḥ śikhaṇḍī ca mahārathaḥ |",
            "dhṛṣṭadyumno virāṭaśca sātyakiścāparājitaḥ",
        ], "|| 17 ||",
           "And the king of Kāśī, supreme archer, and Śikhaṇḍin the great chariot-warrior, Dhṛṣṭadyumna and Virāṭa, and the unconquered Sātyaki;"),
        _v([
            "drupado draupadeyāśca sarvaśaḥ pṛthivīpate |",
            "saubhadraśca mahābāhuḥ śaṅkhān dadhmuḥ pṛthak pṛthak",
        ], "|| 18 ||",
           "Drupada and the sons of Draupadī, O lord of the earth, and the mighty-armed son of Subhadrā — each blew his own conch on every side."),
        _v([
            "sa ghoṣo dhārtarāṣṭrāṇāṃ hṛdayāni vyadārayat |",
            "nabhaśca pṛthivīṃ caiva tumulo vyanunādayan",
        ], "|| 19 ||",
           "That tumult rent the hearts of Dhṛtarāṣṭra's sons, making sky and earth resound."),
        _v([
            "atha vyavasthitān dṛṣṭvā dhārtarāṣṭrān kapidhvajaḥ |",
            "pravṛtte śastrasampāte dhanurudyamya pāṇḍavaḥ",
        ], "|| 20 ||",
           "Then the son of Pāṇḍu, whose banner bears the monkey, seeing Dhṛtarāṣṭra's men drawn up, raised his bow as the clash of weapons was about to begin."),
        _v([
            "hṛṣīkeśaṃ tadā vākyamidamāha mahīpate |",
            "(arjuna uvāca)",
            "senayorubhayormadhye rathaṃ sthāpaya me'cyuta",
        ], "|| 21 ||",
           "And, O lord of the earth, he spoke these words to Hṛṣīkeśa. Arjuna said: Station my chariot between the two armies, O Acyuta,"),
        _v([
            "yāvadetānnirīkṣe'haṃ yoddhukāmānavasthitān |",
            "kairmayā saha yoddhavyamasmin raṇasamudyame",
        ], "|| 22 ||",
           "so that I may look upon these men standing eager for battle, and see with whom I must fight in this undertaking of war."),
        _v([
            "yotsyamānānavekṣe'haṃ ya ete'tra samāgatāḥ |",
            "dhārtarāṣṭrasya durbuddheryuddhe priyacikīrṣavaḥ",
        ], "|| 23 ||",
           "I would see those who have assembled here to fight, wishing to please in battle the evil-minded son of Dhṛtarāṣṭra."),
        {"speaker": "sañjaya uvāca"},
        _v([
            "evamukto hṛṣīkeśo guḍākeśena bhārata |",
            "senayorubhayormadhye sthāpayitvā rathottamam",
        ], "|| 24 ||",
           "Sañjaya said: Thus addressed by Guḍākeśa, O Bhārata, Hṛṣīkeśa stationed that finest of chariots between the two armies,"),
        _v([
            "bhīṣmadroṇapramukhataḥ sarveṣāṃ ca mahīkṣitām |",
            "uvāca pārtha paśyaitān samavetān kurūniti",
        ], "|| 25 ||",
           "before Bhīṣma and Droṇa and all the rulers of the earth, and said: Pārtha, behold these Kurus gathered together."),
        _v([
            "tatrāpaśyat sthitān pārthaḥ pitṝnatha pitāmahān |",
            "ācāryān mātulān bhrātṝn putrān pautrānsakhīṃstathā",
        ], "|| 26 ||",
           "There Pārtha saw, standing in both armies, fathers and grandfathers, teachers, maternal uncles, brothers, sons, grandsons and friends,"),
        _v([
            "śvaśurān suhṛdaścaiva senayorubhayorapi |",
            "tān samīkṣya sa kaunteyaḥ sarvān bandhūnavasthitān",
        ], "|| 27 ||",
           "fathers-in-law and well-wishers too. Seeing all these kinsmen so arrayed, the son of Kuntī,"),
        _v([
            "kṛpayā parayā''viṣṭo viṣīdannidamabravīt |",
            "dṛṣṭvemaṃ svajanaṃ kṛṣṇa yuyutsuṃ samupasthitam",
        ], "|| 28 ||",
           "overcome by deep pity, spoke in sorrow. Arjuna said: Seeing my own people, O Kṛṣṇa, drawn up and eager to fight,"),
        {"speaker": "arjuna uvāca"},
        _v([
            "sīdanti mama gātrāṇi mukhaṃ ca pariśuṣyati |",
            "vepathuśca śarīre me romaharṣaśca jāyate",
        ], "|| 29 ||",
           "my limbs give way, my mouth is parched, my body trembles and my hair stands on end."),
        _v([
            "gāṇḍīvaṃ sraṃsate hastāt tvakcaiva paridahyate |",
            "na ca śaknomyavasthātuṃ bhramatīva ca me manaḥ",
        ], "|| 30 ||",
           "Gāṇḍīva slips from my hand, my skin is burning; I cannot stand steady, and my mind seems to whirl."),
        _v([
            "nimittāni ca paśyāmi viparītāni keśava |",
            "na ca śreyo'nupaśyāmi hatvā svajanamāhave",
        ], "|| 31 ||",
           "I see ill omens, O Keśava, and I foresee no good in killing my own people in battle."),
        _v([
            "na kāṅkṣe vijayaṃ kṛṣṇa na ca rājyaṃ sukhāni ca |",
            "kiṃ no rājyena govinda kiṃ bhogairjīvitena vā",
        ], "|| 32 ||",
           "I do not want victory, Kṛṣṇa, nor kingdom nor pleasures. What use is a kingdom to us, Govinda, or enjoyments, or life itself?"),
        _v([
            "yeṣāmarthe kāṅkṣitaṃ no rājyaṃ bhogāḥ sukhāni ca |",
            "ta ime'vasthitā yuddhe prāṇāṃstyaktvā dhanāni ca",
        ], "|| 33 ||",
           "Those for whose sake we desire kingdom, enjoyments and pleasures stand here in battle, having given up life and wealth —"),
        _v([
            "ācāryāḥ pitaraḥ putrāstathaiva ca pitāmahāḥ |",
            "mātulāḥ śvaśurāḥ pautrāḥ śyālāḥ sambandhinastathā",
        ], "|| 34 ||",
           "teachers, fathers, sons and grandfathers, maternal uncles, fathers-in-law, grandsons, brothers-in-law and other kin."),
        _v([
            "etānna hantumicchāmi ghnato'pi madhusūdana |",
            "api trailokyarājyasya hetoḥ kiṃ nu mahīkṛte",
        ], "|| 35 ||",
           "These I would not wish to kill, O slayer of Madhu, even if they kill me — not for the kingship of the three worlds, let alone for the earth."),
        _v([
            "nihatya dhārtarāṣṭrānnaḥ kā prītiḥ syājjanārdana |",
            "pāpamevāśrayedasmān hatvaitānātatāyinaḥ",
        ], "|| 36 ||",
           "What joy could be ours, Janārdana, in slaying the sons of Dhṛtarāṣṭra? Only sin would cling to us for killing these aggressors."),
        _v([
            "tasmānnārhā vayaṃ hantuṃ dhārtarāṣṭrān svabāndhavān |",
            "svajanaṃ hi kathaṃ hatvā sukhinaḥ syāma mādhava",
        ], "|| 37 ||",
           "So we ought not to kill the sons of Dhṛtarāṣṭra, our own kinsmen. How could we be happy, Mādhava, after killing our own people?"),
        _v([
            "yadyapyete na paśyanti lobhopahatacetasaḥ |",
            "kulakṣayakṛtaṃ doṣaṃ mitradrohe ca pātakam",
        ], "|| 38 ||",
           "Even if these men, their minds overcome by greed, see no wrong in destroying a family and no crime in betraying friends,"),
        _v([
            "kathaṃ na jñeyamasmābhiḥ pāpādasmānnivartitum |",
            "kulakṣayakṛtaṃ doṣaṃ prapaśyadbhirjanārdana",
        ], "|| 39 ||",
           "why should not we, who clearly see the evil of destroying a family, learn to turn away from this sin, O Janārdana?"),
        _v([
            "kulakṣaye praṇaśyanti kuladharmāḥ sanātanāḥ |",
            "dharme naṣṭe kulaṃ kṛtsnamadharmo'bhibhavatyuta",
        ], "|| 40 ||",
           "When a family is destroyed, its ancient family dharmas perish; when dharma perishes, lawlessness overwhelms the whole family."),
        _v([
            "adharmābhibhavāt kṛṣṇa praduṣyanti kulastriyaḥ |",
            "strīṣu duṣṭāsu vārṣṇeya jāyate varṇasaṅkaraḥ",
        ], "|| 41 ||",
           "When lawlessness prevails, Kṛṣṇa, the women of the family are corrupted; and when the women are corrupted, O Vārṣṇeya, the mixing of classes arises."),
        _v([
            "saṅkaro narakāyaiva kulaghnānāṃ kulasya ca |",
            "patanti pitaro hyeṣāṃ luptapiṇḍodakakriyāḥ",
        ], "|| 42 ||",
           "This mixing leads to hell both the destroyers of the family and the family itself, for their ancestors fall, deprived of the offerings of rice-ball and water."),
        _v([
            "doṣairetaiḥ kulaghnānāṃ varṇasaṅkarakārakaiḥ |",
            "utsādyante jātidharmāḥ kuladharmāśca śāśvatāḥ",
        ], "|| 43 ||",
           "By these misdeeds of the destroyers of families, which bring about the mixing of classes, the eternal dharmas of caste and family are uprooted."),
        _v([
            "utsannakuladharmāṇāṃ manuṣyāṇāṃ janārdana |",
            "narake niyataṃ vāso bhavatītyanuśuśruma",
        ], "|| 44 ||",
           "We have heard, Janārdana, that men whose family dharmas are uprooted dwell in hell for an unending time."),
        _v([
            "aho bata mahatpāpaṃ kartuṃ vyavasitā vayam |",
            "yadrājyasukhalobhena hantuṃ svajanamudyatāḥ",
        ], "|| 45 ||",
           "Alas, what a great sin we have resolved to commit, ready to kill our own people out of greed for the pleasures of a kingdom!"),
        _v([
            "yadi māmapratīkāramaśastraṃ śastrapāṇayaḥ |",
            "dhārtarāṣṭrā raṇe hanyustanme kṣemataraṃ bhavet",
        ], "|| 46 ||",
           "Better for me if the sons of Dhṛtarāṣṭra, weapons in hand, were to kill me in battle, unresisting and unarmed."),
        {"speaker": "sañjaya uvāca"},
        _v([
            "evamuktvārjunaḥ saṅkhye rathopastha upāviśat |",
            "visṛjya saśaraṃ cāpaṃ śokasaṃvignamānasaḥ",
        ], "|| 47 ||",
           "Sañjaya said: Having spoken thus on the battlefield, Arjuna sank down on the seat of the chariot, casting away his bow and arrows, his mind overwhelmed by sorrow."),
        "ornament",
        {"colophon": "iti śrīmahābhārate śatasāhasryāṃ saṃhitāyāṃ vaiyāsikyāṃ bhīṣmaparvaṇi śrīmadbhagavadgītāsu upaniṣatsu brahmavidyāyāṃ yogaśāstre śrīkṛṣṇārjuna saṃvāde arjunaviṣādayogo nāma prathamo'dhyāyaḥ.", "gloss": "Thus, in the Bhagavad Gītā — the Upaniṣad, the knowledge of Brahman, the scripture of yoga, the dialogue of Śrī Kṛṣṇa and Arjuna — within the Bhīṣma Parva of the Mahābhārata, the collection of a hundred thousand verses by Vyāsa, ends the first chapter, Arjunaviṣāda Yoga."},
    ],
}
