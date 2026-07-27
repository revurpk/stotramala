# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Vedānta Ḍiṇḍima, attributed to Śrī Śaṅkarācārya (verses public domain).
# IAST transcribed by hand from a scanned edition and cross-checked verse by
# verse against the printed Devanāgarī; the digital source is a copyrighted
# modern compilation, so ONLY the public-domain verses are used and every
# translation here is original. See SOURCES.md §7 for the copyright caveat.

_R = " — so resounds the drum of Vedānta."


def _v(l1, l2, n, gloss):
    return {"padas": [l1 + " |", l2], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "advaita",
    "doc_title": "Vedānta Ḍiṇḍima",
    "app_title": "Vedānta Ḍiṇḍima",
    "h1": "Vedānta Ḍiṇḍima",
    "subtitle": "The Kettledrum of Vedānta · attributed to Śaṅkara",
    "note": "Ninety-four verses proclaiming Advaita, each (but for the opening "
            "invocation and the closing two) ending in the refrain iti "
            "vedāntaḍiṇḍimaḥ — ‘thus beats the ḍiṇḍima, the kettledrum of "
            "Vedānta.’ The work is traditionally ascribed to Śrī "
            "Śaṅkarācārya and opens by invoking Dakṣiṇāmūrti, the silent teacher. "
            "Notice: the verses are public domain, but this text was transcribed "
            "from a copyrighted edition and is NOT cleared for commercial "
            "redistribution — see SOURCES.md §7. Non-commercial personal use is "
            "unaffected.",
    "footer": "Source: Vedānta Ḍiṇḍima, attributed to Śrī Śaṅkarācārya — verses "
              "public domain, but keyed from a copyrighted edition; not for "
              "commercial redistribution (see SOURCES.md §7)",
    "sections": [
        _v("vedāntaḍiṇḍimāstattvamekamudghoṣayanti yat",
           "āstāṃ purastāttattejo dakṣiṇāmūrtisañjñitam", 1,
           "May that Light named Dakṣiṇāmūrti — the one Reality which the "
           "kettledrums of Vedānta loudly proclaim — stand ever before us."),
        _v("ātmā'nātmā padārthau dvau bhoktṛbhogyatvalakṣaṇau",
           "brahmaivātmā na dehādiriti vedāntaḍiṇḍimaḥ", 2,
           "Self and non-self are the two categories, marked as the enjoyer and "
           "the enjoyed. The Self alone is Brahman, not the body and the rest"
           + _R),
        _v("jñānā'jñāne padārthau dvau ātmano muktibandhadau",
           "jñānānmuktirnibandho'nyāt iti vedāntaḍiṇḍimaḥ", 3,
           "Knowledge and ignorance are the two categories, bestowing on the "
           "Self release and bondage. From knowledge comes liberation, from the "
           "other bondage" + _R),
        _v("jñātṛjñeyapadārthau dvau bhāsyabhāsakalakṣaṇau",
           "jñātā brahma jagat jñeyam iti vedāntaḍiṇḍimaḥ", 4,
           "Knower and known are the two categories, marked as the revealer and "
           "the revealed. The knower is Brahman, the known is the world" + _R),
        _v("sukhaduḥkhe padārthau dvau priyavipriyakārakau",
           "sukhaṃ brahma jagadduḥkham iti vedāntaḍiṇḍimaḥ", 5,
           "Pleasure and pain are the two categories, the one welcome, the other "
           "unwelcome. Pleasure is Brahman; the world is pain" + _R),
        _v("samaṣṭivyaṣṭirūpau dvau padārthau sarvasammatau",
           "samaṣṭirīśvaro vyaṣṭirjīvo vedāntaḍiṇḍimaḥ", 6,
           "The collective and the individual are the two categories, admitted "
           "by all. The collective is Īśvara, the individual is the jīva" + _R),
        _v("jñānakarmapadārthau dvau vastukartrātmatantrakau",
           "jñānānmokṣo na karmabhya iti vedāntaḍiṇḍimaḥ", 7,
           "Knowledge and action are the two categories, the one resting on the "
           "Reality, the other on the doer. Liberation comes from knowledge, not "
           "from actions" + _R),
        _v("śrotavyāśrāvyarūpau dvau padārthau sukhaduḥkhadau",
           "śrotavyaṃ brahma naivānyat iti vedāntaḍiṇḍimaḥ", 8,
           "What is worth hearing and what is not are the two categories, giving "
           "pleasure and pain. What is worth hearing is Brahman, nothing else"
           + _R),
        _v("cintyācintyapadārthau dvau viśrāntiśrāntidāyakau",
           "cintyaṃ brahma paraṃ nānyat iti vedāntaḍiṇḍimaḥ", 9,
           "The worth-pondering and the not-worth-pondering are the two "
           "categories, granting repose and fatigue. The supreme Brahman alone "
           "is worth pondering, nothing else" + _R),
        _v("dhyeyādhyeyapadārthau dvau dhīsamādhyasamādhidau",
           "dhyātavyaṃ brahma naivānyat iti vedāntaḍiṇḍimaḥ", 10,
           "What deserves and what does not deserve meditation are the two "
           "categories, giving the mind stillness and distraction. Brahman alone "
           "is to be meditated on, nothing else" + _R),
        _v("yogino bhogino vā'pi tyāgino rāgiṇo'pi ca",
           "jñānānmokṣo na sandeha iti vedāntaḍiṇḍimaḥ", 11,
           "Be one a yogī or a pleasure-seeker, a renunciate or a lover of the "
           "world — liberation comes through knowledge, beyond doubt" + _R),
        _v("na varṇāśramasaṅketairna karmopāsanādibhiḥ",
           "brahmajñānaṃ vinā mokṣa iti vedāntaḍiṇḍimaḥ", 12,
           "Not by the marks of class or stage of life, not by rites or worship "
           "and the like — without the knowledge of Brahman there is no "
           "liberation" + _R),
        _v("asatyassarvasaṃsāro rasābhāsādidūṣitaḥ",
           "upekṣyo brahma vijñeyam iti vedāntaḍiṇḍimaḥ", 13,
           "The whole round of becoming is unreal, tainted by mere semblances of "
           "savour; holding it in disregard, one should know Brahman" + _R),
        _v("vṛthā kriyā vṛthā'lāpān vṛthā vādān manorathān",
           "tyaktvaikaṃ brahma vijñeyam iti vedāntaḍiṇḍimaḥ", 14,
           "Abandoning vain action, vain chatter, vain disputes and daydreams, "
           "one should know the one Brahman" + _R),
        _v("sthito brahmātmanā jīvo brahma jīvātmanā sthitam",
           "iti sampaśyatāṃ muktiriti vedāntaḍiṇḍimaḥ", 15,
           "The jīva abides as the Brahman-self, and Brahman abides as the "
           "jīva-self: for those who clearly see this, there is liberation" + _R),
        _v("jīvo brahmātmanā jñeyo jñeyaṃ jīvātmanā param",
           "muktistadaikyavijñānāditi vedāntaḍiṇḍimaḥ", 16,
           "The jīva is to be known as the Brahman-self, and the supreme Brahman "
           "as the jīva-self; liberation lies in knowing their oneness" + _R),
        _v("sarvātmanā paraṃ brahma śroturātmatayā sthitam",
           "nāyāsastattvavijñaptau iti vedāntaḍiṇḍimaḥ", 17,
           "The supreme Brahman abides as all, and as the very self of the "
           "listener; there is no toil in realizing that Reality" + _R),
        _v("aihikaṃ cāmuṣmikaṃ ca tāpāntaṃ karmasañcayam",
           "tyaktvā brahmaiva vijñeyamiti vedāntaḍiṇḍimaḥ", 18,
           "Renouncing the whole heap of action — of this world and the next, "
           "ending in pain — one should know Brahman alone" + _R),
        _v("advaitadvaitavādau dvau sūkṣmasthūladaśāṃ gatau",
           "advaitavādānmokṣassyāt iti vedāntaḍiṇḍimaḥ", 19,
           "The doctrines of non-duality and duality are the two, reaching the "
           "subtle and the gross states; liberation comes from the doctrine of "
           "non-duality" + _R),
        _v("karmiṇo vinivartante nivartante upāsakāḥ",
           "jñānino na nivartante iti vedāntaḍiṇḍimaḥ", 20,
           "The performers of rites return, and the worshippers return; the "
           "knowers alone do not return" + _R),
        _v("parokṣāsatphalaṃ karma jñānaṃ pratyakṣasatphalam",
           "jñānamevābhyasettasmāt iti vedāntaḍiṇḍimaḥ", 21,
           "Action has a fruit mediate and unreal; knowledge a fruit immediate "
           "and real; therefore one should practise knowledge alone" + _R),
        _v("vṛthā śramo'yaṃ viduṣāṃ vṛthā'yaṃ karmiṇāṃ śramaḥ",
           "yadi na brahmavijñānam iti vedāntaḍiṇḍimaḥ", 22,
           "Vain is this toil of the learned, vain this toil of the ritualists, "
           "if the knowledge of Brahman is not gained" + _R),
        _v("alaṃ yāgairalaṃ yogairalaṃ bhuktairalaṃ dhanaiḥ",
           "parasmin brahmaṇi jñāte iti vedāntaḍiṇḍimaḥ", 23,
           "Enough of sacrifices, enough of yogas, enough of enjoyments, enough "
           "of riches, once the supreme Brahman is known" + _R),
        _v("alaṃ vedairalaṃ śāstrairalaṃ smṛtipurāṇakaiḥ",
           "paramātmani vijñāte iti vedāntaḍiṇḍimaḥ", 24,
           "Enough of the Vedas, enough of the sciences, enough of the codes and "
           "the old lore, once the supreme Self is known" + _R),
        _v("narcā na yajuṣā'rtho'sti na sāmnārtho'sti kaścana",
           "jāte brahmātmavijñāne iti vedāntaḍiṇḍimaḥ", 25,
           "No purpose is left in the Ṛk, the Yajus, or the Sāman, once the "
           "oneness of Brahman and self is known" + _R),
        _v("karmāṇi cittaśuddhyarthaṃ aikāgryārthamupāsanā",
           "mokṣārthaṃ brahmavijñānam iti vedāntaḍiṇḍimaḥ", 26,
           "Rites are for the purifying of the heart, worship for one-pointedness "
           "of the mind, and the knowledge of Brahman for liberation" + _R),
        _v("sañcitāgāmikarmāṇi dahyante jñānavahninā",
           "prārabdhānubhavānmokṣaḥ iti vedāntaḍiṇḍimaḥ", 27,
           "Accumulated and future karmas are burnt by the fire of knowledge; "
           "liberation comes by living out what has begun to bear fruit" + _R),
        _v("na puṇyakarmaṇā vṛddhiḥ na hāniḥ pāpakarmaṇā",
           "nityāsaṅgātmaniṣṭhānāṃ iti vedāntaḍiṇḍimaḥ", 28,
           "For those settled in the ever-unattached Self, there is no gain from "
           "meritorious deeds and no loss from sinful ones" + _R),
        _v("buddhipūrvābuddhipūrvakṛtānāṃ pāpakarmaṇām",
           "prāyaścittamaho jñānaṃ iti vedāntaḍiṇḍimaḥ", 29,
           "For sins done deliberately and unknowingly — what a wonder! — "
           "knowledge itself is the atonement" + _R),
        _v("dṛgdṛśyau dvau padārthau staḥ parasparavilakṣaṇau",
           "dṛg brahma dṛśyaṃ māyā syāt iti vedāntaḍiṇḍimaḥ", 30,
           "Seer and seen are the two categories, each unlike the other; the "
           "seer is Brahman, the seen is māyā" + _R),
        _v("avidyopādhiko jīvo māyopādhika īśvaraḥ",
           "māyā'vidyāguṇātīta iti vedāntaḍiṇḍimaḥ", 31,
           "The jīva has ignorance for its limiting adjunct, Īśvara has māyā for "
           "its; Brahman transcends the qualities of both māyā and ignorance"
           + _R),
        _v("sākāraṃ ca nirākāraṃ nirguṇaṃ ca guṇātmakam",
           "tattvaṃ tatparamaṃ brahma iti vedāntaḍiṇḍimaḥ", 32,
           "That supreme Reality, Brahman, is both with form and formless, both "
           "without qualities and made of qualities" + _R),
        _v("dvijatvaṃ vidhyanuṣṭhānāt vipratvaṃ vedapāṭhataḥ",
           "brāhmaṇyaṃ brahmavijñānāt iti vedāntaḍiṇḍimaḥ", 33,
           "Twice-born status comes from performing the enjoined rites, the "
           "learning of a vipra from studying the Veda, but true brahminhood "
           "from the knowledge of Brahman" + _R),
        _v("sarvātmanā sthitaṃ brahma sarvaṃ brahmātmanā sthitam",
           "na kāryaṃ kāraṇādbhinnam iti vedāntaḍiṇḍimaḥ", 34,
           "Brahman abides as all, and all abides as the Brahman-self; the effect "
           "is not different from the cause" + _R),
        _v("sattāsphuraṇasaukhyāni bhāsante sarvavastuṣu",
           "tasmād brahmamayaṃ sarvam iti vedāntaḍiṇḍimaḥ", 35,
           "Existence, self-shining, and joy manifest in all things; therefore "
           "all is made of Brahman" + _R),
        _v("avasthātritayaṃ yasya krīḍābhūmitayā sthitam",
           "tadeva brahma jānīyāt iti vedāntaḍiṇḍimaḥ", 36,
           "He whose playground is the threefold state — waking, dream, and deep "
           "sleep — Him alone one should know as Brahman" + _R),
        _v("yannādau yacca nāstyante tanmadhye bhātamapyasat",
           "ato mithyā jagatsarvam iti vedāntaḍiṇḍimaḥ", 37,
           "What is not there at the beginning and the end, though it appears in "
           "between, is unreal; therefore the whole world is unreal" + _R),
        _v("yadastyādau yadastyante yanmadhye bhāti tatsvayam",
           "brahmaivaikamidaṃ satyam iti vedāntaḍiṇḍimaḥ", 38,
           "What is there at the beginning, at the end, and shines of itself in "
           "between — that non-dual Brahman alone is real" + _R),
        _v("puruṣārthatrayāviṣṭāḥ puruṣāḥ paśavo dhruvam",
           "mokṣārthī puruṣaśśreṣṭhaḥ iti vedāntaḍiṇḍimaḥ", 39,
           "People engrossed in the three human ends are surely as beasts; the "
           "seeker of liberation is the best of men" + _R),
        _v("ghaṭakuḍyādikaṃ sarvaṃ mṛttikāmātrameva ca",
           "tathā brahma jagatsarvam iti vedāntaḍiṇḍimaḥ", 40,
           "Pot, wall, and the rest are but clay alone; even so, the whole world "
           "is Brahman alone" + _R),
        _v("ṣaṇṇihatya trayaṃ hitvā dvayaṃ bhittvā'khilātigam",
           "ekaṃ buddhvā'śnute mokṣaṃ iti vedāntaḍiṇḍimaḥ", 41,
           "Slaying the six foes, abandoning the three guṇas, splitting the two, "
           "transcending all — knowing the One, one attains liberation" + _R),
        _v("bhittvā ṣaṭ pañca bhittvā'tha bhittvā'tha caturastrikam",
           "dvayaṃ hitvā''śrayedekam iti vedāntaḍiṇḍimaḥ", 42,
           "Splitting the six and the five, splitting again the four and the "
           "three, forsaking the two, one should take refuge in the One" + _R),
        _v("deho nāhamahaṃ dehī dehasākṣīti niścayāt",
           "janmamṛtyuprahīṇo'sau iti vedāntaḍiṇḍimaḥ", 43,
           "‘I am not the body; I am the body’s indweller, the witness "
           "of the body’ — by this certainty one is freed from birth and "
           "death" + _R),
        _v("prāṇo nāhamahaṃ devaḥ prāṇasākṣīti niścayāt",
           "kṣutpipāsopaśāntissyāt iti vedāntaḍiṇḍimaḥ", 44,
           "‘I am not the vital breath; I am the shining witness of the "
           "breath’ — by this certainty hunger and thirst are stilled" + _R),
        _v("mano nāhamahaṃ devaḥ manassākṣīti niścayāt",
           "śokamohāpahānissyāt iti vedāntaḍiṇḍimaḥ", 45,
           "‘I am not the mind; I am the shining witness of the mind’ — "
           "by this certainty sorrow and delusion fall away" + _R),
        _v("buddhirnāhamahaṃ devaḥ buddhisākṣīti niścayāt",
           "kartṛbhāvanivṛttissyāt iti vedāntaḍiṇḍimaḥ", 46,
           "‘I am not the intellect; I am the shining witness of the "
           "intellect’ — by this certainty the sense of doership ceases"
           + _R),
        _v("nājñānaṃ syāmahaṃ devo'jñānasākṣīti niścayāt",
           "sarvānarthanivṛttissyāt iti vedāntaḍiṇḍimaḥ", 47,
           "‘I am not ignorance; I am the shining witness of ignorance’ "
           "— by this certainty all misfortune ceases" + _R),
        _v("ahaṃ sākṣīti yo vidyāt vivicyaivaṃ punaḥ punaḥ",
           "sa eva mukto'sau vidvān iti vedāntaḍiṇḍimaḥ", 48,
           "Whoever knows ‘I am the witness,’ discerning thus again and "
           "again — he, the wise one, is verily the liberated" + _R),
        _v("nāhaṃ māyā na tatkāryaṃ na sākṣī paramo'smyaham",
           "iti nissaṃśayajñānānmuktirvedāntaḍiṇḍimaḥ", 49,
           "‘I am not māyā, nor its effect, nor even the witness; I am the "
           "Supreme’ — from this doubtless knowledge comes liberation" + _R),
        _v("nāhaṃ sarvamahaṃ sarvaṃ mama sarvamiti sphuṭam",
           "jñāte tattve kuto duḥkhamiti vedāntaḍiṇḍimaḥ", 50,
           "‘I am nothing; I am all; all is mine’ — clearly so; when the "
           "Reality is known, whence any sorrow?" + _R),
        _v("dehādipañcakośasthā yā sattā pratibhāsate",
           "sā sattā''tmā na sandeha iti vedāntaḍiṇḍimaḥ", 51,
           "The Existence that shines within the five sheaths beginning with the "
           "body — that Existence is the Self, beyond doubt" + _R),
        _v("dehādipañcakośasthā yā sphūrtiranubhūyate",
           "sā sphūrtirātmā naivānyat iti vedāntaḍiṇḍimaḥ", 52,
           "The awareness that is felt within the five sheaths beginning with the "
           "body — that awareness is the Self, nothing else" + _R),
        _v("dehādipañcakośasthā yā prītiranubhūyate",
           "sā prītirātmā kūṭastha iti vedāntaḍiṇḍimaḥ", 53,
           "The love that is felt within the five sheaths beginning with the "
           "body — that love is the Self, the changeless" + _R),
        _v("vyomādipañcabhūtasthā yā sattā bhāsate nṛṇām",
           "sā sattā paramaṃ brahma iti vedāntaḍiṇḍimaḥ", 54,
           "The Existence that shines to men within the five elements beginning "
           "with space — that Existence is the supreme Brahman" + _R),
        _v("vyomādipañcabhūtasthā yā cidekānubhūyate",
           "sā cideva paraṃ brahma iti vedāntaḍiṇḍimaḥ", 55,
           "The one consciousness experienced within the five elements beginning "
           "with space — that consciousness is the supreme Brahman" + _R),
        _v("vyomādipañcabhūtasthā yā prītiranubhūyate",
           "sā prītireva brahma syāt iti vedāntaḍiṇḍimaḥ", 56,
           "The love that is felt within the five elements beginning with space — "
           "that love alone is Brahman" + _R),
        _v("dehādikośagā sattā yā sā vyomādibhūtagā",
           "mānābhāvānna tadbheda iti vedāntaḍiṇḍimaḥ", 57,
           "The Existence in the sheaths and the Existence in the elements are "
           "one; there being no proof of difference, they are not two" + _R),
        _v("dehādikośagā sphūrtiḥ yā sā vyomādibhūtagā",
           "mānābhāvānna tadbheda iti vedāntaḍiṇḍimaḥ", 58,
           "The awareness in the sheaths and the awareness in the elements are "
           "one; there being no proof of difference, they are not two" + _R),
        _v("dehādikośagā prītiḥ yā sā vyomādibhūtagā",
           "mānābhāvānna tadbheda iti vedāntaḍiṇḍimaḥ", 59,
           "The love in the sheaths and the love in the elements are one; there "
           "being no proof of difference, they are not two" + _R),
        _v("saccidānandarūpatvāt brahmaivātmā na saṃśayaḥ",
           "pramāṇakoṭisandhānāt iti vedāntaḍiṇḍimaḥ", 60,
           "Since its nature is existence-consciousness-bliss, the Self is verily "
           "Brahman, beyond doubt, borne out by countless proofs" + _R),
        _v("na nāmarūpe niyate sarvatra vyabhicārataḥ",
           "anāmarūpaṃ sarvaṃ syāt iti vedāntaḍiṇḍimaḥ", 61,
           "Names and forms are nowhere fixed, shifting everywhere; hence all is "
           "in truth beyond name and form" + _R),
        _v("na jīvabrahmaṇorbhedassattārūpeṇa vidyate",
           "sattābhede na mānaṃ syāt iti vedāntaḍiṇḍimaḥ", 62,
           "Between jīva and Brahman there is no difference in respect of "
           "existence; of a difference in existence there is no proof" + _R),
        _v("na jīvabrahmaṇorbhedassphūrtirūpeṇa vidyate",
           "sphūrtibhede na mānaṃ syāt iti vedāntaḍiṇḍimaḥ", 63,
           "Between jīva and Brahman there is no difference in respect of "
           "awareness; of a difference in awareness there is no proof" + _R),
        _v("na jīvabrahmaṇorbhedaḥ priyarūpeṇa vidyate",
           "priyabhede na mānaṃ syāt iti vedāntaḍiṇḍimaḥ", 64,
           "Between jīva and Brahman there is no difference in respect of love; "
           "of a difference in love there is no proof" + _R),
        _v("na jīvabrahmaṇorbhedaḥ nāmnā rūpeṇa vidyate",
           "nāmno rūpasya mithyātvāt iti vedāntaḍiṇḍimaḥ", 65,
           "Between jīva and Brahman there is no difference by name or form, for "
           "name and form are unreal" + _R),
        _v("na jīvabrahmaṇorbhedaḥ piṇḍabrahmāṇḍabhedataḥ",
           "vyaṣṭessamaṣṭerekatvāt iti vedāntaḍiṇḍimaḥ", 66,
           "Between jīva and Brahman there is no difference from the difference "
           "of individual and cosmic bodies, for the individual and the "
           "collective are one" + _R),
        _v("brahma satyaṃ jaganmithyā jīvo brahmaiva nāparaḥ",
           "jīvanmuktastu tadvidvān iti vedāntaḍiṇḍimaḥ", 67,
           "Brahman is real, the world unreal; the jīva is Brahman itself, no "
           "other. Knowing this, one is liberated while yet living" + _R),
        _v("anāmarūpaṃ sakalaṃ sanmayaṃ cinmayaṃ param",
           "kuto bhedaḥ kuto bandha iti vedāntaḍiṇḍimaḥ", 68,
           "All, beyond name and form, is made of supreme existence and "
           "consciousness; where then is difference, where is bondage?" + _R),
        _v("na tattvāt kathyate loko nāmādyairvyabhicārataḥ",
           "vaṭurjaraṭha ityādyairiti vedāntaḍiṇḍimaḥ", 69,
           "The world is named not by its truth but by shifting appellations — "
           "‘boy,’ ‘old man,’ and the like" + _R),
        _v("nāmarūpātmakaṃ viśvamindrajālaṃ vidurbudhāḥ",
           "anāmatvādayuktatvāditi vedāntaḍiṇḍimaḥ", 70,
           "The wise know this world of name and form to be a conjurer’s "
           "illusion, for, being nameless, it cannot rightly be so named" + _R),
        _v("abhedadarśanam mokṣassaṃsāro bhedadarśanaḥ",
           "sarvavedāntasiddhānta iti vedāntaḍiṇḍimaḥ", 71,
           "The vision of non-difference is liberation; the vision of difference "
           "is the round of becoming. This is the settled conclusion of all "
           "Vedānta" + _R),
        _v("na matābhiniveśitvānna bhāṣā''veśamātrataḥ",
           "muktirvinā''tmavijñānāditi vedāntaḍiṇḍimaḥ", 72,
           "Not from clinging to a doctrine, not from mere zeal for a tongue, but "
           "only from knowledge of the Self comes liberation" + _R),
        _v("na kāmyapratiṣiddhābhiḥ kriyābhirmokṣavāsanā",
           "īśvarānugrahāt sā syāditi vedāntaḍiṇḍimaḥ", 73,
           "The longing for liberation does not arise from rites, whether desired "
           "or forbidden; it arises by the grace of the Lord" + _R),
        _v("avijñāte janma naṣṭaṃ vijñāte janma sārthakam",
           "jñāturātmā na dūre syāditi vedāntaḍiṇḍimaḥ", 74,
           "Unknown, one’s birth is wasted; known, one’s birth is "
           "fulfilled; the Self of the knower is never far away" + _R),
        _v("daśamasya parijñāne nāyāso'sti yathā tathā",
           "svasya brahmātmavijñāna iti vedāntaḍiṇḍimaḥ", 75,
           "As there is no toil in coming to know the tenth man, so too there is "
           "none in knowing one’s own self as Brahman" + _R),
        _v("upekṣyaupādhikān doṣān gṛhyante viṣayā yathā",
           "upekṣya dṛśyaṃ yad brahma iti vedāntaḍiṇḍimaḥ", 76,
           "As objects are taken up while their adjunct-borne faults are "
           "disregarded, so, disregarding the seen, one should know Brahman" + _R),
        _v("sukhamalpaṃ bahukleśo viṣayagrāhiṇāṃ nṛṇām",
           "anantaṃ brahmaniṣṭhānāmiti vedāntaḍiṇḍimaḥ", 77,
           "For men who grasp at sense-objects the pleasure is little, the "
           "trouble great; for those settled in Brahman it is infinite" + _R),
        _v("dhanairvā dhanadaiḥ putrairdārāgārasahodaraiḥ",
           "dhruvaṃ prāṇaharairduḥkhamiti vedāntaḍiṇḍimaḥ", 78,
           "By riches, or by the givers of riches, by sons, wife, house, and kin "
           "— who surely drain one’s life — comes only sorrow" + _R),
        _v("supterutthāya suptyantaṃ brahmaikaṃ pravicintyatām",
           "nātidūre nṛṇāṃ mṛtyuriti vedāntaḍiṇḍimaḥ", 79,
           "From waking until sleep, let the one Brahman be contemplated; for "
           "men, death is not far off" + _R),
        _v("pañcānāmapi kośānāṃ māyā'narthavyayocitā",
           "tatsākṣī brahmavijñānamiti vedāntaḍiṇḍimaḥ", 80,
           "All five sheaths, being māyā, are fit only for the spending-away of "
           "misfortune; their witness is the knowledge of Brahman" + _R),
        _v("daśamatvaparijñāne navajñasya yathā sukham",
           "tathā jīvasya samprāptiriti vedāntaḍiṇḍimaḥ", 81,
           "As the joy of one who missed the tenth man, on coming to know him, "
           "such is the attainment of the jīva on knowing itself" + _R),
        _v("navabhyo'sti paraṃ pratyak nava veda paraṃ param",
           "tadvijñānādbhavetturyā iti vedāntaḍiṇḍimaḥ", 82,
           "Beyond the nine is the inmost Self; the nine know it as the supreme "
           "beyond the supreme; by knowing it one gains the Fourth" + _R),
        _v("navābhāsā navajñatvāt navopādhin navātmanā",
           "mithyā jñātvā'vaśiṣṭe tu maunaṃ vedāntaḍiṇḍimaḥ", 83,
           "The nine, being appearances through the nine and adjuncts of the "
           "nine, are unreal; knowing them false, in the residue there is "
           "silence" + _R),
        _v("parame brahmaṇi svasmin pravilāpyākhilaṃ jagat",
           "gāyannadvaitamātmānamāste vedāntaḍiṇḍimaḥ", 84,
           "Dissolving the whole world into the supreme Brahman that is one’s "
           "own self, one abides singing of the non-dual Self" + _R),
        _v("pratilomānulomābhyāṃ viśvāropāpavādayoḥ",
           "cintane śiṣyate tattvamiti vedāntaḍiṇḍimaḥ", 85,
           "In the twofold contemplation — reverse and forward — of the world’s "
           "superimposition and its negation, the Reality remains as the residue"
           + _R),
        _v("nāmarūpābhimānassyāt saṃsārassarvadehinām",
           "saccidānandadṛṣṭissyānmuktirvedāntaḍiṇḍimaḥ", 86,
           "Identifying with name and form is bondage for all embodied beings; "
           "the vision of existence-consciousness-bliss is liberation" + _R),
        _v("saccidānandasatyatve mithyātve nāmarūpayoḥ",
           "vijñāte kimidaṃ jñeyamiti vedāntaḍiṇḍimaḥ", 87,
           "When the truth of existence-consciousness-bliss and the falsity of "
           "name and form are known, what more remains to be known?" + _R),
        _v("sālambanaṃ nirālambaṃ sarvālambāvalambitam",
           "ālambenākhilālambamiti vedāntaḍiṇḍimaḥ", 88,
           "It is with support and without support, the support of all supports, "
           "and by its own support the support of everything" + _R),
        _v("na kuryāt na vijānīyāt sarvaṃ brahmetyanusmaran",
           "yathā sukhaṃ tathā tiṣṭhediti vedāntaḍiṇḍimaḥ", 89,
           "Remembering all as Brahman, one need neither act nor seek to know "
           "anything in particular; let one abide at ease" + _R),
        _v("svakarmapāśavaśagaḥ prājño'nyo vā jano dhruvam",
           "prājñassukhaṃ nayetkālamiti vedāntaḍiṇḍimaḥ", 90,
           "Bound by the noose of his own karma, the wise and the unwise alike "
           "must reap it; yet the wise pass their time in joy" + _R),
        _v("na vidvān santapeccittaṃ karaṇā'karaṇo dhruvam",
           "sarvamātmeti vijñānāt iti vedāntaḍiṇḍimaḥ", 91,
           "The wise man does not scorch his mind, whether he acts or refrains, "
           "for he knows that all is the Self" + _R),
        _v("naivābhāsaṃ spṛśet karma mithyopādhimapi svayam",
           "kuto'dhiṣṭhānamatyacchamiti vedāntaḍiṇḍimaḥ", 92,
           "Action cannot touch even the reflection, itself a false adjunct; how "
           "much less the utterly pure substratum?" + _R),
        _v("aho'smākamalaṃ mohairātmā brahmeti nirbhayam",
           "śrutibheriravo'dyāpi śrūyate śrutirañjanaḥ", 93,
           "Ah, enough of delusions for us! ‘The Self is Brahman’ — "
           "fearlessly the drumbeat of scripture resounds even today, delighting "
           "the ear with revelation."),
        _v("vedāntabherijhaṅkāraḥ prativādibhayaṅkaraḥ",
           "śrūyatāṃ brāhmaṇaiśśrīmaddakṣiṇāmūrtyanugrahāt", 94,
           "The thunder of the Vedānta-drum, terrible to opponents — may it be "
           "heard by the brāhmaṇas, through the grace of the blessed "
           "Dakṣiṇāmūrti."),
    ],
}
