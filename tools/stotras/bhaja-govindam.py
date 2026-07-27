# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Bhaja Govindam (Dvādaśamañjarikā / Moha Mudgara) of Ādi Śaṅkarācārya.
# IAST from Sanskrit Wikisource (भजगोविन्दम्, public domain) via the teltools
# dev2iast port; the Wikisource copy carries a run of small OCR typos, each
# corrected against the standard text and logged in SOURCES.md §5.15.
# Translations original. Public-domain source — no redistribution restriction.

def _v(p1, p2, p3, p4, n, gloss):
    return {"padas": [p1, p2 + " |", p3, p4], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "vishnu",
    "doc_title": "Bhaja Govindam",
    "app_title": "Bhaja Govindam",
    "h1": "Bhaja Govindam",
    "subtitle": "Worship Govinda · Dvādaśamañjarikā of Śaṅkara",
    "note": "Ādi Śaṅkara's celebrated hymn of dispassion and discernment — the "
            "‘Dvādaśamañjarikā’ (twelve blossoms) with the disciples' "
            "verses and colophons, 33 verses in all. The refrain bhaja "
            "govindaṃ urges the mind to turn from craving to the Self. The "
            "recited Hare-Kṛṣṇa prelude, not part of the composition, is omitted.",
    "footer": "Source: Sanskrit Wikisource — भजगोविन्दम् (public domain)",
    "sections": [
        _v("bhajagovindaṃ bhajagovindaṃ", "govindaṃ bhajamūḍhamate",
           "saṃprāpte sannihite kāle", "nahi nahi rakṣati ḍukṛñkaraṇe", 1,
           "Worship Govinda, worship Govinda, worship Govinda, O foolish mind! "
           "When the appointed hour draws near, rules of grammar will not save "
           "you at all."),
        _v("mūḍha jahīhi dhanāgamatṛṣṇāṃ", "kuru sadbuddhiṃ manasi vitṛṣṇām",
           "yallabhase nijakarmopāttaṃ", "vittaṃ tena vinodaya cittam", 2,
           "O fool, give up the thirst to amass wealth; make the mind free of "
           "craving, filled with right thought. With whatever you gain as the "
           "fruit of your own deeds, content your heart."),
        _v("nārīstanabhara nābhīdeśaṃ", "dṛṣṭvā mā gā mohāveśam",
           "etanmāṃsavasādivikāraṃ", "manasi vicintaya vāraṃ vāram", 3,
           "Seeing a woman's breast and navel, do not fall into the grip of "
           "delusion; ponder again and again in the mind that this is but a "
           "modification of flesh and fat."),
        _v("nalinīdalagata jalamatitaralaṃ", "tadvajjīvitamatiśayacapalam",
           "viddhi vyādhyabhimānagrastaṃ", "lokaṃ śokahataṃ ca samastam", 4,
           "The water on a lotus-leaf is utterly unsteady; so too is life, "
           "exceedingly fickle. Know that the whole world is seized by disease "
           "and conceit, and stricken with grief."),
        _v("yāvadvittopārjanasaktaḥ", "tāvannija parivāro raktaḥ",
           "paścājjīvati jarjara dehe", "vārtāṃ ko'pi na pṛcchati gehe", 5,
           "As long as you can earn wealth, so long is your family attached to "
           "you; afterwards, when you live on in a body worn with age, no one at "
           "home even asks after you."),
        _v("yāvatpavano nivasati dehe", "tāvatpṛcchati kuśalaṃ gehe",
           "gatavati vāyau dehāpāye", "bhāryā bibhyati tasminkāye", 6,
           "As long as the breath dwells in the body, so long do they ask after "
           "your welfare at home; once the breath is gone and the body falls, "
           "even the wife dreads that very corpse."),
        _v("bālastāvatkrīḍāsaktaḥ", "taruṇastāvattaruṇīsaktaḥ",
           "vṛddhastāvaccintāsaktaḥ", "pare brahmaṇi ko'pi na saktaḥ", 7,
           "In childhood one is absorbed in play; in youth, absorbed in a young "
           "woman; in old age, absorbed in anxiety — but in the supreme Brahman, "
           "alas, no one is absorbed."),
        _v("kā te kāntā kaste putraḥ", "saṃsāro'yamatīva vicitraḥ",
           "kasya tvaṃ kaḥ kuta āyātaḥ", "tattvaṃ cintaya tadiha bhrātaḥ", 8,
           "Who is your wife? Who is your son? Exceedingly strange is this round "
           "of becoming. Whose are you? Who are you? Whence have you come? "
           "Ponder that truth here, O brother."),
        _v("satsaṅgatve nissaṅgatvaṃ", "nissaṅgatve nirmohatvam",
           "nirmohatve niścalatattvaṃ", "niścalatattve jīvanmuktiḥ", 9,
           "From the company of the good comes non-attachment; from "
           "non-attachment, freedom from delusion; from freedom from delusion, "
           "the unshakable Reality; from the unshakable Reality, liberation "
           "while yet living."),
        _v("vayasi gate kaḥ kāmavikāraḥ", "śuṣke nīre kaḥ kāsāraḥ",
           "kṣīṇe vitte kaḥ parivāraḥ", "jñāte tattve kaḥ saṃsāraḥ", 10,
           "When youth is gone, where is the play of lust? When the water dries "
           "up, where is the lake? When wealth dwindles, where is the retinue? "
           "When the Truth is known, where is the round of becoming?"),
        _v("mā kuru dhana jana yauvana garvaṃ", "harati nimeṣātkālaḥ sarvam",
           "māyāmayamidamakhilaṃ hitvā", "brahmapadaṃ tvaṃ praviśa viditvā", 11,
           "Take no pride in wealth, in people, or in youth — Time carries all "
           "of it off in a moment. Renouncing this whole illusion-made world, "
           "know and enter the state of Brahman."),
        _v("dinayāminyau sāyaṃ prātaḥ", "śiśiravasantau punarāyātaḥ",
           "kālaḥ krīḍati gacchatyāyuḥ", "tadapi na muñcatyāśāvāyuḥ", 12,
           "Day and night, dusk and dawn, winter and spring come round again; "
           "Time sports on, life ebbs away — yet even so the wind of craving "
           "does not let go."),
        _v("dvādaśamañjarikābhiraśeṣaḥ", "kathito vaiyākaraṇasyaiṣaḥ",
           "upadeśo'bhūdvidyānipuṇaiḥ", "śrīmacchaṅkarabhagavaccharaṇaiḥ", "12a",
           "This whole ‘bunch of twelve blossoms’ was spoken as a "
           "teaching to the grammarian by the venerable, learning-perfected feet "
           "of Śrī Śaṅkara."),
        _v("kā te kāntā dhana gatacintā", "vātula kiṃ tava nāsti niyantā",
           "trijagati sajjanasaṃgatirekā", "bhavati bhavārṇavataraṇe naukā", 13,
           "What of your wife, what of your anxious care for wealth? O frantic "
           "one, have you no ruler? In the three worlds, the company of the good "
           "is the one boat to cross the ocean of becoming."),
        _v("jaṭilo muṇḍī luñchitakeśaḥ", "kāṣāyāmbarabahukṛtaveṣaḥ",
           "paśyannapi ca na paśyati mūḍhaḥ", "udaranimittaṃ bahukṛtaveṣaḥ", 14,
           "One with matted locks, one with shaven head, one with hair plucked "
           "out, one decked in ochre robes and many disguises — the fool sees "
           "and yet does not see; all this masquerade is for the belly's sake."),
        _v("aṅgaṃ galitaṃ palitaṃ muṇḍaṃ", "daśanavihīnaṃ jātaṃ tuṇḍam",
           "vṛddho yāti gṛhītvā daṇḍaṃ", "tadapi na muñcatyāśāpiṇḍam", 15,
           "The limbs are worn, the head gone grey, the mouth left toothless; "
           "the old man walks leaning on a staff — yet even so he does not let "
           "go the lump of craving."),
        _v("agre vahniḥ pṛṣṭhe bhānuḥ", "rātrau cubukasamarpitajānuḥ",
           "karatalabhikṣastarutalavāsaḥ", "tadapi na muñcatyāśāpāśaḥ", 16,
           "Fire in front, the sun at his back, at night his knees drawn up to "
           "his chin; alms in his cupped palm, his dwelling the foot of a tree — "
           "yet even so the noose of craving does not release him."),
        _v("kurute gaṅgāsāgaragamanaṃ", "vrataparipālanamathavā dānam",
           "jñānavihīnaḥ sarvamatena", "muktiṃ na bhajati janmaśatena", 17,
           "One makes the pilgrimage to Gaṅgāsāgara, keeps vows, or gives in "
           "charity; but devoid of knowledge, by the verdict of every school, "
           "one wins no liberation even in a hundred births."),
        _v("suramaṃdiratarumūlanivāsaḥ", "śayyā bhūtalamajinaṃ vāsaḥ",
           "sarvaparigrahabhogatyāgaḥ", "kasya sukhaṃ na karoti virāgaḥ", 18,
           "Dwelling in a temple or at the root of a tree, the bare earth for a "
           "bed and a deerskin for a garment, renouncing all possessing and "
           "enjoying — whom does such dispassion not make happy?"),
        _v("yogarato vā bhogarato vā", "saṅgarato vā saṅgavihīnaḥ",
           "yasya brahmaṇi ramate cittaṃ", "nandati nandati nandatyeva", 19,
           "Given to yoga or given to enjoyment, keeping company or apart from "
           "it — he whose mind delights in Brahman rejoices, rejoices, rejoices "
           "indeed."),
        _v("bhagavadgītā kiñcidadhītā", "gaṅgā jalalavakaṇikāpītā",
           "sakṛdapi yena murārisamarcā", "kriyate tasya yamena na carcā", 20,
           "By whom even a little of the Bhagavad-Gītā is studied, a single drop "
           "of Gaṅgā-water sipped, and Murāri worshipped but once — with him "
           "Yama holds no argument."),
        _v("punarapi jananaṃ punarapi maraṇaṃ", "punarapi jananījaṭhare śayanam",
           "iha saṃsāre bahudustāre", "kṛpayā'pāre pāhi murāre", 21,
           "Birth again, death again, lying again in the mother's womb — in this "
           "world so hard to cross, save me, O Murāri, in your boundless "
           "compassion."),
        _v("rathyācarpaṭaviracitakanthaḥ", "puṇyāpuṇyavivarjitapanthaḥ",
           "yogī yoganiyojitacitto", "ramate bālonmattavadeva", 22,
           "In a patched quilt stitched from rags off the road, walking a path "
           "beyond merit and demerit, the yogī, his mind yoked in yoga, sports "
           "like a child or a madman."),
        _v("kastvaṃ ko'haṃ kuta āyātaḥ", "kā me jananī ko me tātaḥ",
           "iti paribhāvaya sarvamasāram", "viśvaṃ tyaktvā svapnavicāram", 23,
           "Who are you? Who am I? Whence have I come? Who is my mother, who my "
           "father? Reflect thus that all is without substance, and give up this "
           "world as a dream to be pondered no more."),
        _v("tvayi mayi cānyatraiko viṣṇuḥ", "vyarthaṃ kupyasi mayyasahiṣṇuḥ",
           "bhava samacittaḥ sarvatra tvaṃ", "vāñchasyacirādyadi viṣṇutvam", 24,
           "In you, in me, and everywhere there is but the one Viṣṇu; in vain, "
           "impatient, do you rage at me. Become even-minded toward all, if you "
           "would soon attain the state of Viṣṇu."),
        _v("śatrau mitre putre bandhau", "mā kuru yatnaṃ vigrahasandhau",
           "sarvasminnapi paśyātmānaṃ", "sarvatrotsṛja bhedājñānam", 25,
           "Toward foe, friend, son, or kinsman make no effort at strife or "
           "alliance; see the Self in all, and cast off everywhere the ignorance "
           "of difference."),
        _v("kāmaṃ krodhaṃ lobhaṃ mohaṃ", "tyaktvātmānaṃ bhāvaya ko'ham",
           "ātmajñānavihīnā mūḍhāḥ", "te pacyante narakanigūḍhāḥ", 26,
           "Renouncing desire, anger, greed, and delusion, reflect on the Self: "
           "‘Who am I?’ Fools bereft of Self-knowledge are cooked, "
           "sunk deep in hell."),
        _v("geyaṃ gītā nāmasahasraṃ", "dhyeyaṃ śrīpatirūpamajasram",
           "neyaṃ sajjanasaṅge cittaṃ", "deyaṃ dīnajanāya ca vittam", 27,
           "Let the Gītā and the Thousand Names be sung; let the form of Śrī's "
           "Lord be meditated on without ceasing; let the mind be led into the "
           "company of the good; let wealth be given to the poor."),
        _v("sukhataḥ kriyate rāmābhogaḥ", "paścāddhanta śarīre rogaḥ",
           "yadyapi loke maraṇaṃ śaraṇaṃ", "tadapi na muñcati pāpācaraṇam", 28,
           "Pleasure is lightly taken in the delights of love — but afterwards, "
           "alas, disease in the body. Though in this world death is the end of "
           "all, even so one does not give up sinful conduct."),
        _v("arthamanarthaṃ bhāvaya nityaṃ", "nāsti tataḥ sukhaleśaḥ satyam",
           "putrādapi dhanabhājāṃ bhītiḥ", "sarvatraiṣā vihitā rītiḥ", 29,
           "Ever reflect that wealth is calamity; truly, not a particle of "
           "happiness comes from it. For the wealthy there is fear even from a "
           "son — such everywhere is the settled way of things."),
        _v("prāṇāyāmaṃ pratyāhāraṃ", "nityānityavivekavicāram",
           "jāpyasametasamādhividhānaṃ", "kurvavadhānaṃ mahadavadhānam", 30,
           "Breath-control, withdrawal of the senses, discernment between the "
           "eternal and the fleeting, and the practice of absorption joined with "
           "recitation — perform these with care, with great care."),
        _v("gurucaraṇāmbuja nirbhara bhaktaḥ", "saṃsārādacirādbhava muktaḥ",
           "sendriyamānasaniyamādevaṃ", "drakṣyasi nijahṛdayasthaṃ devam", 31,
           "O devotee leaning wholly on the guru's lotus-feet, be freed at once "
           "from the round of becoming; through this discipline of the senses "
           "and mind you will behold the God seated in your own heart."),
        _v("mūḍhaḥ kaścana vaiyākaraṇo", "ḍukṛñkaraṇādhyayanadhuriṇaḥ",
           "śrīmacchaṅkarabhagavacchiṣyai", "bodhita āsīcchodhitakaraṇaḥ", 32,
           "A certain foolish grammarian, engrossed in the study of the rule "
           "ḍukṛñ-karaṇa, was awakened and had his faculties made pure, by the "
           "disciples of the venerable Lord Śaṅkara."),
        _v("bhajagovindaṃ bhajagovindaṃ", "govindaṃ bhajamūḍhamate",
           "nāmasmaraṇādanyamupāyaṃ", "nahi paśyāmo bhavataraṇe", 33,
           "Worship Govinda, worship Govinda, worship Govinda, O foolish mind! "
           "For crossing beyond this world we see no other means than the "
           "remembrance of the Name."),
    ],
}
