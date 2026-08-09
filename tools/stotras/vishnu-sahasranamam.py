# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Viṣṇu Sahasranāma Stotram — the thousand names of Viṣṇu, from the
# Anuśāsana-parvan of the Mahābhārata (Bhīṣma's answer to Yudhiṣṭhira).
# Devanāgarī from Sanskrit Wikisource (विष्णुसहस्रनामस्तोत्रम्, CC BY-SA;
# the underlying verses are ancient and public domain) via the bundled
# dev2iast converter. Translations original. See SOURCES.md §5.21.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "vishnu",
    "doc_title": "Viṣṇu Sahasranāmam",
    "app_title": "Viṣṇu Sahasranāmam",
    "h1": "Viṣṇu Sahasranāmam",
    "subtitle": "The Thousand Names of Viṣṇu · Mahābhārata, Anuśāsana-parvan",
    "note": "The most widely recited of all Sanskrit litanies: a thousand names "
            "of Viṣṇu, taught by Bhīṣma to Yudhiṣṭhira from his bed of arrows. "
            "Set out here as the seven dhyāna verses, the hundred and eight "
            "verses of names, and the closing prayer for forgiveness of errors "
            "in recitation. Each name is a door — the translations render them "
            "in the order they are sung.",
    "audio": "https://www.youtube.com/watch?v=ATflA6WOy0I",
    "audio_label": "M. S. Subbulakshmi — Viṣṇu Sahasranāmam",
    "footer": "Source: Sanskrit Wikisource — विष्णुसहस्रनामस्तोत्रम् (verses public domain)",
    "sections": [
        # ── dhyānam ──────────────────────────────────────────────────────
        _v(["kṣīrodanvatpradeśe śucimaṇivilasatsaikate mauktikānāṃ",
            "mālākḷptāsanasthaḥ sphaṭikamaṇinibhairmauktikairmaṇḍitāṅgaḥ |",
            "śubhrairabhrairadabhrairupariviracitairmuktapīyūṣavarṣair",
            "ānandī naḥ punīyādarinalinagadāśaṅkhapāṇirmukundaḥ"], "|| 1 ||",
           "In the region of the ocean of milk, on sands bright with pure gems, "
           "seated on a couch strung of pearls, his limbs adorned with pearls "
           "like crystal; canopied by white and boundless clouds that shower "
           "released nectar — may Mukunda, blissful, bearing discus, lotus, "
           "mace and conch in his hands, make us pure."),
        _v(["bhūḥ pādau yasya nābhirviyadasuranilaścandrasūryau ca netre",
            "karṇāvāśāḥ śiro dyaurmukhamapi dahano yasya vāsteyamabdhiḥ |",
            "antaḥsthaṃ yasya viśvaṃ suranarakhagagobhogigandharvadaityaiḥ",
            "citraṃ raṃramyate taṃ tribhuvanavapuṣaṃ viṣṇumīśaṃ namāmi"], "|| 2 ||",
           "Whose feet are the earth, whose navel the mid-air, whose breath the "
           "wind, whose eyes the moon and sun; whose ears are the quarters, "
           "whose head the heaven, whose mouth is fire, whose belly the sea; "
           "within whom the universe rests, sporting in wonder with gods, men, "
           "birds, cattle, serpents, gandharvas and demons — to him whose body "
           "is the three worlds, to Viṣṇu the Lord, I bow."),
        _v(["oṃ śāntākāraṃ bhujagaśayanaṃ padmanābhaṃ sureśaṃ",
            "viśvādhāraṃ gaganasadṛśaṃ meghavarṇaṃ śubhāṅgam |",
            "lakṣmīkāntaṃ kamalanayanaṃ yogibhirdhyānagamyaṃ",
            "vande viṣṇuṃ bhavabhayaharaṃ sarvalokaikanātham"], "|| 3 ||",
           "Oṃ. Of peaceful form, couched upon the serpent, lotus-naveled, Lord "
           "of the gods; support of the universe, vast as the sky, cloud-hued, "
           "beautiful of limb; beloved of Lakṣmī, lotus-eyed, reached by yogins "
           "in meditation — I praise Viṣṇu, remover of the fear of becoming, the "
           "one Lord of all the worlds."),
        _v(["meghaśyāmaṃ pītakauśeyavāsaṃ",
            "śrīvatsāṅkaṃ kaustubhodbhāsitāṅgam |",
            "puṇyopetaṃ puṇḍarīkāyatākṣaṃ",
            "viṣṇuṃ vande sarvalokaikanātham"], "|| 4 ||",
           "Dark as a raincloud, robed in yellow silk, marked with the Śrīvatsa, "
           "his body lit by the Kaustubha gem; endowed with all merit, his eyes "
           "long as lotus petals — I praise Viṣṇu, the one Lord of all worlds."),
        _v(["namaḥ samastabhūtānāmādibhūtāya bhūbhṛte |",
            "anekarūparūpāya viṣṇave prabhaviṣṇave"], "|| 5 ||",
           "Salutation to him who is the first of all beings, the bearer of the "
           "earth; whose form is many forms — to Viṣṇu, the ever-becoming, the "
           "mighty."),
        _v(["saśaṅkhacakraṃ sakirīṭakuṇḍalaṃ",
            "sapītavastraṃ sarasīruhekṣaṇam |",
            "sahāravakṣaḥsthalakaustubhaśriyaṃ",
            "namāmi viṣṇuṃ śirasā caturbhujam"], "|| 6 ||",
           "With conch and discus, with crown and earrings, with yellow raiment "
           "and eyes like lotuses; his breast graced with a garland and the "
           "splendour of the Kaustubha — I bow my head to four-armed Viṣṇu."),
        _v(["chāyāyāṃ pārijātasya hemasiṃhāsanopari",
            "āsīnamambudaśyāmamāyatākṣamalaṃkṛtam |",
            "candrānanaṃ caturbāhuṃ śrīvatsāṅkitavakṣasaṃ",
            "rukmiṇīsatyabhāmābhyāṃ sahitaṃ kṛṣṇamāśraye"], "|| 7 ||",
           "In the shade of the pārijāta tree, seated upon a golden throne, "
           "dark as a rain-cloud, long-eyed and richly adorned; moon-faced, "
           "four-armed, his breast marked with the Śrīvatsa — I take refuge in "
           "Kṛṣṇa, together with Rukmiṇī and Satyabhāmā."),
        "ornament",
        # ── the thousand names ───────────────────────────────────────────
        _v(["viśvaṃ viṣṇurvaṣaṭkāro bhūtabhavyabhavatprabhuḥ |",
            "bhūtakṛdbhūtabhṛdbhāvo bhūtātmā bhūtabhāvanaḥ"], "|| 1 ||",
           "The universe itself; the all-pervader; the vaṣaṭ-call by which "
           "oblation is offered; Lord of what was, what shall be, and what is; "
           "maker of beings; sustainer of beings; pure Being; the Self of all "
           "beings; the quickener of beings."),
        _v(["pūtātmā paramātmā ca muktānāṃ paramā gatiḥ |",
            "avyayaḥ puruṣaḥ sākṣī kṣetrajño'kṣara eva ca"], "|| 2 ||",
           "Of pure essence; the supreme Self; the highest goal of the "
           "liberated; the imperishable; the Person; the witness; the knower of "
           "the field; and the indestructible."),
        _v(["yogo yogavidāṃ netā pradhānapuruṣeśvaraḥ |",
            "nārasiṃhavapuḥ śrīmān keśavaḥ puruṣottamaḥ"], "|| 3 ||",
           "Yoga itself; leader of those who know yoga; Lord of Prakṛti and "
           "Puruṣa; he whose body is the man-lion; possessor of splendour; "
           "Keśava, of beautiful locks; the supreme Person."),
        _v(["sarvaḥ śarvaḥ śivaḥ sthāṇurbhūtādirnidhiravyayaḥ |",
            "saṃbhavo bhāvano bhartā prabhavaḥ prabhurīśvaraḥ"], "|| 4 ||",
           "He who is all; the destroyer; the auspicious; the firm-standing; the "
           "origin of beings; the imperishable treasure; he who takes birth by "
           "his own will; the bestower; the supporter; the source of all; the "
           "master; the sovereign."),
        _v(["svayaṃbhūḥ śambhurādityaḥ puṣkarākṣo mahāsvanaḥ |",
            "anādinidhano dhātā vidhātā dhāturuttamaḥ"], "|| 5 ||",
           "The self-existent; giver of happiness; the sun among the Ādityas; "
           "lotus-eyed; of mighty sound; without beginning or end; the "
           "sustainer; the ordainer; the highest ground of all."),
        _v(["aprameyo hṛṣīkeśaḥ padmanābho'maraprabhuḥ |",
            "viśvakarmā manustvaṣṭā sthaviṣṭhaḥ sthaviro dhruvaḥ"], "|| 6 ||",
           "The immeasurable; lord of the senses; the lotus-naveled; Lord of the "
           "immortals; maker of the universe; the thinker; the shaper; the "
           "vastest; the ancient; the unshakable."),
        _v(["agrāhyaḥ śāśvataḥ kṛṣṇo lohitākṣaḥ pratardanaḥ |",
            "prabhūtastrikakubdhāma pavitraṃ maṅgalaṃ param"], "|| 7 ||",
           "Not to be grasped; the eternal; the dark one; the red-eyed; the "
           "destroyer at the end; the abundant; the abode of the three "
           "quarters; the purifier; the supreme auspiciousness."),
        _v(["īśānaḥ prāṇadaḥ prāṇo jyeṣṭhaḥ śreṣṭhaḥ prajāpatiḥ |",
            "hiraṇyagarbho bhūgarbho mādhavo madhusūdanaḥ"], "|| 8 ||",
           "The ruler; giver of life; life itself; the eldest; the best; lord of "
           "creatures; the golden womb; he who holds the earth in his womb; "
           "Mādhava, lord of Mā (Lakṣmī); slayer of Madhu."),
        _v(["īśvaro vikramī dhanvī medhāvī vikramaḥ kramaḥ |",
            "anuttamo durādharṣaḥ kṛtajñaḥ kṛtirātmavān"], "|| 9 ||",
           "The sovereign; the valorous; the bearer of the bow; the wise; "
           "prowess itself; the strider; he than whom none is higher; the "
           "unassailable; the knower of what is done; action itself; self-"
           "possessed."),
        _v(["sureśaḥ śaraṇaṃ śarma viśvaretāḥ prajābhavaḥ |",
            "ahaḥ saṃvatsaro vyālaḥ pratyayaḥ sarvadarśanaḥ"], "|| 10 ||",
           "Lord of the gods; the refuge; supreme bliss; the seed of the "
           "universe; the source of creatures; the day; the year; the serpent; "
           "the certainty; the all-seeing."),
        _v(["ajaḥ sarveśvaraḥ siddhaḥ siddhiḥ sarvādiracyutaḥ |",
            "vṛṣākapirameyātmā sarvayogaviniḥsṛtaḥ"], "|| 11 ||",
           "The unborn; Lord of all; the accomplished; accomplishment itself; "
           "the beginning of all; the unfallen; Vṛṣākapi, the boar who lifts "
           "dharma; of immeasurable Self; free of every entanglement."),
        _v(["vasurvasumanāḥ satyaḥ samātmā'sammitaḥ samaḥ |",
            "amoghaḥ puṇḍarīkākṣo vṛṣakarmā vṛṣākṛtiḥ"], "|| 12 ||",
           "The dwelling of all; of generous mind; the truth; even-minded; "
           "beyond measure; the impartial; never fruitless; lotus-eyed; whose "
           "every act is dharma; whose very form is dharma."),
        _v(["rudro bahuśirā babhrurviśvayoniḥ śuciśravāḥ |",
            "amṛtaḥ śāśvataḥ sthāṇurvarāroho mahātapāḥ"], "|| 13 ||",
           "The remover of sorrow; the many-headed; the bearer of the worlds; "
           "the womb of the universe; of pure renown; the deathless; the "
           "everlasting; the immovable; the noble ascent; of great austerity."),
        _v(["sarvagaḥ sarvavidbhānurviṣvakseno janārdanaḥ |",
            "vedo vedavidavyaṅgo vedāṅgo vedavit kaviḥ"], "|| 14 ||",
           "All-pervading; all-knowing; the shining; he whose armies are "
           "everywhere; the refuge sought by people; the Veda itself; knower of "
           "the Veda; without defect; whose limbs are the Vedāṅgas; knower of "
           "the Veda; the seer-poet."),
        _v(["lokādhyakṣaḥ surādhyakṣo dharmādhyakṣaḥ kṛtākṛtaḥ |",
            "caturātmā caturvyūhaścaturdaṃṣṭraścaturbhujaḥ"], "|| 15 ||",
           "Overseer of the worlds; overseer of the gods; overseer of dharma; "
           "both the made and the unmade; of fourfold Self; of four vyūhas; "
           "four-tusked; four-armed."),
        _v(["bhrājiṣṇurbhojanaṃ bhoktā sahiṣṇurjagadādijaḥ |",
            "anagho vijayo jetā viśvayoniḥ punarvasuḥ"], "|| 16 ||",
           "The radiant; that which is enjoyed; the enjoyer; the forbearing; "
           "born at the world's beginning; the sinless; victory itself; the "
           "conqueror; the womb of the universe; he who dwells again and "
           "again."),
        _v(["upendro vāmanaḥ prāṃśuramoghaḥ śucirūrjitaḥ |",
            "atīndraḥ saṃgrahaḥ sargo dhṛtātmā niyamo yamaḥ"], "|| 17 ||",
           "The younger brother of Indra; the dwarf; the towering one; never "
           "fruitless; the pure; the mighty; surpassing Indra; the gatherer; "
           "creation itself; of steady Self; the restrainer; the controller."),
        _v(["vedyo vaidyaḥ sadāyogī vīrahā mādhavo madhuḥ |",
            "atīndriyo mahāmāyo mahotsāho mahābalaḥ"], "|| 18 ||",
           "He who is to be known; the physician; the ever-united; slayer of "
           "heroes; lord of knowledge; the sweet; beyond the senses; of great "
           "māyā; of great zeal; of great strength."),
        _v(["mahābuddhirmahāvīryo mahāśaktirmahādyutiḥ |",
            "anirdeśyavapuḥ śrīmānameyātmā mahādridhṛk"], "|| 19 ||",
           "Of great intelligence; of great vigour; of great power; of great "
           "brilliance; whose body cannot be pointed out; possessed of "
           "splendour; of immeasurable Self; upholder of the great mountain."),
        _v(["maheṣvāso mahībhartā śrīnivāsaḥ satāṃ gatiḥ |",
            "aniruddhaḥ surānando govindo govidāṃ patiḥ"], "|| 20 ||",
           "The great archer; bearer of the earth; the dwelling of Śrī; the goal "
           "of the good; the unobstructed; the joy of the gods; Govinda, finder "
           "of the earth; lord of those who know speech."),
        _v(["marīcirdamano haṃsaḥ suparṇo bhujagottamaḥ |",
            "hiraṇyanābhaḥ sutapāḥ padmanābhaḥ prajāpatiḥ"], "|| 21 ||",
           "The ray of light; the subduer; the swan; the fair-winged; best of "
           "serpents; the golden-naveled; of noble austerity; the lotus-naveled; "
           "lord of creatures."),
        _v(["amṛtyuḥ sarvadṛk siṃhaḥ sandhātā sandhimān sthiraḥ |",
            "ajo durmarṣaṇaḥ śāstā viśrutātmā surārihā"], "|| 22 ||",
           "The deathless; the all-seeing; the lion; the joiner; he who is "
           "joined to all; the steady; the unborn; hard to bear against; the "
           "teacher; whose Self is famed; slayer of the enemies of the gods."),
        _v(["gururgurutamo dhāma satyaḥ satyaparākramaḥ |",
            "nimiṣo'nimiṣaḥ sragvī vācaspatirudāradhīḥ"], "|| 23 ||",
           "The teacher; the greatest of teachers; the abode; the truth; whose "
           "valour is truth; he whose eyes close in yoga-sleep; the unwinking; "
           "the garlanded; lord of speech; of noble understanding."),
        _v(["agraṇīrgrāmaṇīḥ śrīmān nyāyo netā samīraṇaḥ |",
            "sahasramūrdhā viśvātmā sahasrākṣaḥ sahasrapāt"], "|| 24 ||",
           "He who leads in front; leader of the host; possessor of splendour; "
           "justice itself; the guide; the mover of all; the thousand-headed; "
           "Self of the universe; thousand-eyed; thousand-footed."),
        _v(["āvartano nivṛttātmā saṃvṛtaḥ saṃpramardanaḥ |",
            "ahaḥ saṃvartako vahniranilo dharaṇīdharaḥ"], "|| 25 ||",
           "He who turns the wheel of the world; whose Self is turned away from "
           "sense; the veiled; the crusher; he who sets the day revolving; the "
           "fire; the wind; upholder of the earth."),
        _v(["suprasādaḥ prasannātmā viśvadhṛgviśvabhugvibhuḥ |",
            "satkartā satkṛtaḥ sādhurjahnurnārāyaṇo naraḥ"], "|| 26 ||",
           "Of perfect grace; of serene Self; upholder of the universe; enjoyer "
           "of the universe; the all-pervading; honourer of the good; himself "
           "honoured; the holy; the withdrawer; Nārāyaṇa, whose abode is the "
           "waters; the primal Man."),
        _v(["asaṃkhyeyo'prameyātmā viśiṣṭaḥ śiṣṭakṛcchuciḥ |",
            "siddhārthaḥ siddhasaṃkalpaḥ siddhidaḥ siddhisādhanaḥ"], "|| 27 ||",
           "Beyond counting; of immeasurable Self; the pre-eminent; maker of the "
           "wise; the pure; whose every aim is achieved; whose will is "
           "fulfilled; giver of attainment; the means of attainment."),
        _v(["vṛṣāhī vṛṣabho viṣṇurvṛṣaparvā vṛṣodaraḥ |",
            "vardhano vardhamānaśca viviktaḥ śrutisāgaraḥ"], "|| 28 ||",
           "Lord of the days of dharma; the bull who showers blessing; the "
           "all-pervader; whose steps are dharma; from whose womb dharma is "
           "born; the increaser; the ever-growing; the unmingled; the ocean of "
           "sacred hearing."),
        _v(["subhujo durdharo vāgmī mahendro vasudo vasuḥ |",
            "naikarūpo bṛhadrūpaḥ śipiviṣṭaḥ prakāśanaḥ"], "|| 29 ||",
           "Of beautiful arms; hard to hold; eloquent; the great Lord; giver of "
           "wealth; wealth itself; of many forms; of vast form; he who pervades "
           "the rays of light; the illuminator."),
        _v(["ojastejodyutidharaḥ prakāśātmā pratāpanaḥ |",
            "ṛddhaḥ spaṣṭākṣaro mantraścandrāṃśurbhāskaradyutiḥ"], "|| 30 ||",
           "Bearer of vigour, splendour and radiance; of luminous Self; the "
           "burning one; the abundant; whose syllable Oṃ is manifest; the sacred "
           "formula; the moon's ray; bright as the sun."),
        _v(["amṛtāṃśūdbhavo bhānuḥ śaśabinduḥ sureśvaraḥ |",
            "auṣadhaṃ jagataḥ setuḥ satyadharmaparākramaḥ"], "|| 31 ||",
           "Source of the nectar-rayed moon; the shining; he who marks the moon "
           "as with a hare; Lord of the gods; the healing herb; the bridge "
           "across the world; whose truth, dharma and valour are real."),
        _v(["bhūtabhavyabhavannāthaḥ pavanaḥ pāvano'nalaḥ |",
            "kāmahā kāmakṛtkāntaḥ kāmaḥ kāmapradaḥ prabhuḥ"], "|| 32 ||",
           "Lord of past, future and present; the wind; the purifier; the fire; "
           "destroyer of desire; fulfiller of desire; the beautiful; desire "
           "itself; giver of desires; the master."),
        _v(["yugādikṛdyugāvarto naikamāyo mahāśanaḥ |",
            "adṛśyo vyaktarūpaśca sahasrajidanantajit"], "|| 33 ||",
           "Maker of the ages' beginning; he who turns the ages round; of "
           "manifold māyā; the great devourer; the unseen; and yet of manifest "
           "form; conqueror of thousands; conqueror of the endless."),
        _v(["iṣṭo'viśiṣṭaḥ śiṣṭeṣṭaḥ śikhaṇḍī nahuṣo vṛṣaḥ |",
            "krodhahā krodhakṛtkartā viśvabāhurmahīdharaḥ"], "|| 34 ||",
           "The beloved; who favours none above another; dear to the wise; "
           "crested with a peacock plume; he who binds beings by māyā; the bull "
           "of dharma; destroyer of wrath; rouser of wrath; the doer; whose arms "
           "are everywhere; upholder of the earth."),
        _v(["acyutaḥ prathitaḥ prāṇaḥ prāṇado vāsavānujaḥ |",
            "apāṃnidhiradhiṣṭhānamapramattaḥ pratiṣṭhitaḥ"], "|| 35 ||",
           "The unfallen; the renowned; the breath of life; giver of life; "
           "younger brother of Indra; the ocean, treasure of waters; the "
           "foundation; the ever-vigilant; the firmly established."),
        _v(["skandaḥ skandadharo dhuryo varado vāyuvāhanaḥ |",
            "vāsudevo bṛhadbhānurādidevaḥ purandaraḥ"], "|| 36 ||",
           "He who flows as nectar; upholder of dharma's course; bearer of the "
           "yoke; giver of boons; he who rides the wind; Vāsudeva, indweller of "
           "all; of vast radiance; the first of gods; breaker of cities."),
        _v(["aśokastāraṇastāraḥ śūraḥ śaurirjaneśvaraḥ |",
            "anukūlaḥ śatāvartaḥ padmī padmanibhekṣaṇaḥ"], "|| 37 ||",
           "Free of sorrow; he who carries others across; the deliverer; the "
           "valiant; scion of Śūra; Lord of beings; the favourable; he of a "
           "hundred turnings; bearer of the lotus; whose eyes are like "
           "lotuses."),
        _v(["padmanābho'ravindākṣaḥ padmagarbhaḥ śarīrabhṛt |",
            "maharddhirṛddho vṛddhātmā mahākṣo garuḍadhvajaḥ"], "|| 38 ||",
           "The lotus-naveled; lotus-eyed; seated in the lotus of the heart; "
           "bearer of bodies; of great prosperity; the flourishing; the ancient "
           "Self; the great-eyed; whose banner is Garuḍa."),
        _v(["atulaḥ śarabho bhīmaḥ samayajño havirhariḥ |",
            "sarvalakṣaṇalakṣaṇyo lakṣmīvān samitiñjayaḥ"], "|| 39 ||",
           "The incomparable; he who dwells as witness in the body; the fearful; "
           "knower of the fitting time; the oblation; Hari, remover of sorrow; "
           "known by every mark of proof; consort of Lakṣmī; victor in battle."),
        _v(["vikṣaro rohito mārgo heturdāmodaraḥ sahaḥ |",
            "mahīdharo mahābhāgo vegavānamitāśanaḥ"], "|| 40 ||",
           "The undecaying; he who took the fish form; the path; the cause; "
           "Dāmodara, bound at the waist by a cord; the forbearing; upholder of "
           "the earth; of great fortune; the swift; of measureless appetite."),
        _v(["udbhavaḥ kṣobhaṇo devaḥ śrīgarbhaḥ parameśvaraḥ |",
            "karaṇaṃ kāraṇaṃ kartā vikartā gahano guhaḥ"], "|| 41 ||",
           "The origin; the agitator at creation; the shining god; in whose womb "
           "is all splendour; the supreme Lord; the instrument; the cause; the "
           "doer; the maker of manifold forms; the unfathomable; the hidden."),
        _v(["vyavasāyo vyavasthānaḥ saṃsthānaḥ sthānado dhruvaḥ |",
            "pararddhiḥ paramaspaṣṭastuṣṭaḥ puṣṭaḥ śubhekṣaṇaḥ"], "|| 42 ||",
           "Resolve itself; the ordering of all; the final rest; giver of place; "
           "the constant; of supreme prosperity; utterly manifest; the "
           "contented; the full; of auspicious gaze."),
        _v(["rāmo virāmo virajo mārgo neyo nayo'nayaḥ |",
            "vīraḥ śaktimatāṃ śreṣṭho dharmo dharmaviduttamaḥ"], "|| 43 ||",
           "Rāma, in whom all delight; the place of rest; the stainless; the "
           "way; he who is to be led to; the leader; he who has none to lead "
           "him; the hero; best of the powerful; dharma itself; highest of those "
           "who know dharma."),
        _v(["vaikuṇṭhaḥ puruṣaḥ prāṇaḥ prāṇadaḥ praṇavaḥ pṛthuḥ |",
            "hiraṇyagarbhaḥ śatrughno vyāpto vāyuradhokṣajaḥ"], "|| 44 ||",
           "Lord of Vaikuṇṭha; the Person; the breath; giver of breath; the "
           "praṇava Oṃ; the wide; the golden womb; slayer of foes; the "
           "pervading; the wind; he who never sinks below his own nature."),
        _v(["ṛtuḥ sudarśanaḥ kālaḥ parameṣṭhī parigrahaḥ |",
            "ugraḥ saṃvatsaro dakṣo viśrāmo viśvadakṣiṇaḥ"], "|| 45 ||",
           "The season; of fair aspect; time itself; established in the highest; "
           "the receiver; the terrible; the year; the skilful; the resting "
           "place; most dexterous in all things."),
        _v(["vistāraḥ sthāvarasthāṇuḥ pramāṇaṃ bījamavyayam |",
            "artho'nartho mahākośo mahābhogo mahādhanaḥ"], "|| 46 ||",
           "The expanse; the fixed support of things immovable; the measure; the "
           "imperishable seed; the goal sought; he who needs nothing; the great "
           "treasury; of great enjoyment; of great wealth."),
        _v(["anirviṇṇaḥ sthaviṣṭho'bhūrdharmayūpo mahāmakhaḥ |",
            "nakṣatranemirnakṣatrī kṣamaḥ kṣāmaḥ samīhanaḥ"], "|| 47 ||",
           "Never despondent; the most massive; the unborn; the post to which "
           "dharma is bound; the great sacrifice; the hub of the stars; lord of "
           "the constellations; the patient; he who remains when all wanes; the "
           "well-wisher of every effort."),
        _v(["yajña ijyo mahejyaśca kratuḥ satraṃ satāṃ gatiḥ |",
            "sarvadarśī vimuktātmā sarvajño jñānamuttamam"], "|| 48 ||",
           "The sacrifice; the one to be worshipped; most worthy of worship; the "
           "rite; the sacrificial session; the goal of the good; the all-seeing; "
           "of ever-free Self; the omniscient; the highest knowledge."),
        _v(["suvrataḥ sumukhaḥ sūkṣmaḥ sughoṣaḥ sukhadaḥ suhṛt |",
            "manoharo jitakrodho vīrabāhurvidāraṇaḥ"], "|| 49 ||",
           "Of noble vow; of pleasing face; the subtle; of auspicious sound; "
           "giver of happiness; the true friend; stealer of the mind; conqueror "
           "of anger; of heroic arms; the render of the wicked."),
        _v(["svāpanaḥ svavaśo vyāpī naikātmā naikakarmakṛt |",
            "vatsaro vatsalo vatsī ratnagarbho dhaneśvaraḥ"], "|| 50 ||",
           "He who lays beings to sleep; subject to none but himself; the "
           "pervader; of many selves; doer of many works; the dwelling place of "
           "all; the affectionate; protector of the calf-like; whose womb holds "
           "jewels; lord of wealth."),
        _v(["dharmagubdharmakṛddharmī sadasatkṣaramakṣaram |",
            "avijñātā sahasrāṃśurvidhātā kṛtalakṣaṇaḥ"], "|| 51 ||",
           "Guardian of dharma; doer of dharma; possessor of dharma; the real "
           "and the unreal, the perishable and the imperishable; the "
           "unknowable; the thousand-rayed; the ordainer; he who made the marks "
           "by which things are known."),
        _v(["gabhastinemiḥ sattvasthaḥ siṃho bhūtamaheśvaraḥ |",
            "ādidevo mahādevo deveśo devabhṛdguruḥ"], "|| 52 ||",
           "The hub in the wheel of rays; established in sattva; the lion; great "
           "Lord of beings; the first god; the great god; Lord of the gods; "
           "teacher and upholder of the gods."),
        _v(["uttaro gopatirgoptā jñānagamyaḥ purātanaḥ |",
            "śarīrabhūtabhṛdbhoktā kapīndro bhūridakṣiṇaḥ"], "|| 53 ||",
           "He who rises above; lord of cattle and of the earth; the protector; "
           "reached by knowledge; the ancient; sustainer of the elements that "
           "make the body; the enjoyer; lord of the monkeys; of abundant "
           "gifts."),
        _v(["somapo'mṛtapaḥ somaḥ purujitpurusattamaḥ |",
            "vinayo jayaḥ satyasaṃdho dāśārhaḥ sāttvatāṃpatiḥ"], "|| 54 ||",
           "Drinker of soma; drinker of nectar; the moon that nourishes plants; "
           "conqueror of many; best of the many; the humbler; victory itself; "
           "true to his word; worthy of offerings; Lord of the Sāttvatas."),
        _v(["jīvo vinayitā sākṣī mukundo'mitavikramaḥ |",
            "ambhonidhiranantātmā mahodadhiśayo'ntakaḥ"], "|| 55 ||",
           "The living soul; the chastiser; the witness; Mukunda, giver of "
           "liberation; of measureless stride; the treasure of waters; of "
           "endless Self; he who sleeps on the great ocean; the ender."),
        _v(["ajo mahārhaḥ svābhāvyo jitāmitraḥ pramodanaḥ |",
            "ānando nandano nandaḥ satyadharmā trivikramaḥ"], "|| 56 ||",
           "The unborn; most worthy of worship; ever of his own nature; "
           "conqueror of foes; the gladdener; bliss itself; the delighter; the "
           "joyful; whose dharma is truth; he of the three strides."),
        _v(["maharṣiḥ kapilācāryaḥ kṛtajño medinīpatiḥ |",
            "tripadastridaśādhyakṣo mahāśṛṅgaḥ kṛtāntakṛt"], "|| 57 ||",
           "The great seer; the teacher Kapila; knower of all that is done; lord "
           "of the earth; he of the three steps; overseer of the thirty gods; "
           "the great-horned; he who makes an end of Death."),
        _v(["mahāvarāho govindaḥ suṣeṇaḥ kanakāṅgadī |",
            "guhyo gabhīro gahano guptaścakragadādharaḥ"], "|| 58 ||",
           "The great boar; Govinda; of goodly army; wearing golden armlets; the "
           "secret; the deep; the impenetrable; the hidden; bearer of discus and "
           "mace."),
        _v(["vedhāḥ svāṅgo'jitaḥ kṛṣṇo dṛḍhaḥ saṃkarṣaṇo'cyutaḥ |",
            "varuṇo vāruṇo vṛkṣaḥ puṣkarākṣo mahāmanāḥ"], "|| 59 ||",
           "The creator; his own instrument; the unconquered; the dark one; the "
           "firm; Saṃkarṣaṇa who draws all together; the unfallen; Varuṇa, the "
           "setting sun; son of Varuṇa; steady as a tree; lotus-eyed; of great "
           "mind."),
        _v(["bhagavān bhagahā''nandī vanamālī halāyudhaḥ |",
            "ādityo jyotirādityaḥ sahiṣṇurgatisattamaḥ"], "|| 60 ||",
           "The Blessed One, endowed with all excellence; destroyer of "
           "fortunes at dissolution; the blissful; wearer of the forest garland; "
           "whose weapon is the plough; son of Aditi; radiant as the sun; the "
           "forbearing; the best of goals."),
        _v(["sudhanvā khaṇḍaparaśurdāruṇo draviṇapradaḥ |",
            "divaḥspṛk sarvadṛgvyāso vācaspatirayonijaḥ"], "|| 61 ||",
           "Of the goodly bow; wielder of the broken axe; terrible to the "
           "unrighteous; giver of wealth; he who touches heaven; the all-seeing "
           "arranger; lord of speech; born of no womb."),
        _v(["trisāmā sāmagaḥ sāma nirvāṇaṃ bheṣajaṃ bhiṣak |",
            "saṃnyāsakṛcchamaḥ śānto niṣṭhā śāntiḥ parāyaṇam"], "|| 62 ||",
           "Praised by the three Sāmans; the singer of Sāman; the Sāman itself; "
           "the extinguishing of sorrow; the medicine; the physician; the maker "
           "of renunciation; the calm; the peaceful; the ground of all; peace "
           "itself; the highest goal."),
        _v(["śubhāṅgaḥ śāntidaḥ sraṣṭā kumudaḥ kuvaleśayaḥ |",
            "gohito gopatirgoptā vṛṣabhākṣo vṛṣapriyaḥ"], "|| 63 ||",
           "Of auspicious limbs; giver of peace; the creator; he who delights in "
           "the earth; who lies in the waters; benefactor of cattle; lord of the "
           "earth; the protector; whose eyes shower dharma; to whom dharma is "
           "dear."),
        _v(["anivartī nivṛttātmā saṃkṣeptā kṣemakṛcchivaḥ |",
            "śrīvatsavakṣāḥ śrīvāsaḥ śrīpatiḥ śrīmatāṃvaraḥ"], "|| 64 ||",
           "He who never turns back; whose Self is withdrawn from sense; he who "
           "draws all in at dissolution; doer of what is safe and good; the "
           "auspicious; bearing the Śrīvatsa on his breast; the dwelling of Śrī; "
           "Lord of Śrī; best of the glorious."),
        _v(["śrīdaḥ śrīśaḥ śrīnivāsaḥ śrīnidhiḥ śrīvibhāvanaḥ |",
            "śrīdharaḥ śrīkaraḥ śreyaḥ śrīmāṁllokatrayāśrayaḥ"], "|| 65 ||",
           "Giver of splendour; Lord of splendour; the abode of Śrī; the "
           "treasury of Śrī; the bestower of splendour; the bearer of Śrī; the "
           "maker of splendour; the highest good; possessed of splendour; the "
           "refuge of the three worlds."),
        _v(["svakṣaḥ svaṅgaḥ śatānando nandirjyotirgaṇeśvaraḥ |",
            "vijitātmā'vidheyātmā satkīrtiśchinnasaṃśayaḥ"], "|| 66 ||",
           "Of beautiful eyes; of beautiful limbs; of a hundred joys; joy "
           "itself; the light; Lord of the hosts; conqueror of the senses; whose "
           "Self is subject to none; of true renown; in whom all doubt is cut "
           "away."),
        _v(["udīrṇaḥ sarvataścakṣuranīśaḥ śāśvatasthiraḥ |",
            "bhūśayo bhūṣaṇo bhūtirviśokaḥ śokanāśanaḥ"], "|| 67 ||",
           "The exalted; whose eyes are on every side; who has no lord above "
           "him; eternal and unmoving; he who lay upon the earth; the ornament "
           "of all; being itself; free of sorrow; destroyer of sorrow."),
        _v(["arciṣmānarcitaḥ kumbho viśuddhātmā viśodhanaḥ |",
            "aniruddho'pratirathaḥ pradyumno'mitavikramaḥ"], "|| 68 ||",
           "The radiant; the worshipped; the vessel that holds all; of utterly "
           "pure Self; the purifier; the unobstructed; he who has no equal foe; "
           "Pradyumna of surpassing wealth; of measureless stride."),
        _v(["kālaneminihā vīraḥ śauriḥ śūrajaneśvaraḥ |",
            "trilokātmā trilokeśaḥ keśavaḥ keśihā hariḥ"], "|| 69 ||",
           "Slayer of Kālanemi; the hero; scion of Śūra; Lord of the valiant; "
           "Self of the three worlds; Lord of the three worlds; Keśava, of "
           "beautiful locks; slayer of Keśin; Hari, who takes away sorrow."),
        _v(["kāmadevaḥ kāmapālaḥ kāmī kāntaḥ kṛtāgamaḥ |",
            "anirdeśyavapurviṣṇurvīro'nanto dhanaṃjayaḥ"], "|| 70 ||",
           "The god of love; guardian of desires; he who has all he desires; the "
           "beautiful; author of the scriptures; whose body cannot be pointed "
           "out; the all-pervader; the hero; the endless; winner of wealth."),
        _v(["brahmaṇyo brahmakṛd brahmā brahma brahmavivardhanaḥ |",
            "brahmavid brāhmaṇo brahmī brahmajño brāhmaṇapriyaḥ"], "|| 71 ||",
           "Devoted to Brahman; maker of Brahman; the creator Brahmā; Brahman "
           "itself; increaser of Brahman; knower of Brahman; the brāhmaṇa; "
           "possessor of Brahman; who knows Brahman; to whom brāhmaṇas are "
           "dear."),
        _v(["mahākramo mahākarmā mahātejā mahoragaḥ |",
            "mahākraturmahāyajvā mahāyajño mahāhaviḥ"], "|| 72 ||",
           "Of mighty stride; of mighty deeds; of mighty splendour; the great "
           "serpent; the great rite; the great sacrificer; the great sacrifice; "
           "the great oblation."),
        _v(["stavyaḥ stavapriyaḥ stotraṃ stutiḥ stotā raṇapriyaḥ |",
            "pūrṇaḥ pūrayitā puṇyaḥ puṇyakīrtiranāmayaḥ"], "|| 73 ||",
           "Worthy of praise; who loves praise; the hymn itself; the praise; the "
           "praiser; who delights in battle; the full; the fulfiller; the "
           "meritorious; of holy renown; free of all disease."),
        _v(["manojavastīrthakaro vasuretā vasupradaḥ |",
            "vasuprado vāsudevo vasurvasumanā haviḥ"], "|| 74 ||",
           "Swift as thought; maker of holy fords; whose seed is golden; giver "
           "of wealth; giver of the highest wealth; Vāsudeva; the indwelling "
           "treasure; of generous mind; the oblation."),
        _v(["sadgatiḥ satkṛtiḥ sattā sadbhūtiḥ satparāyaṇaḥ |",
            "śūraseno yaduśreṣṭhaḥ sannivāsaḥ suyāmunaḥ"], "|| 75 ||",
           "The goal of the good; of noble deeds; pure existence; the true "
           "manifestation; the refuge of the good; of heroic armies; best of the "
           "Yadus; the abode of the good; attended by the folk of the Yamunā."),
        _v(["bhūtāvāso vāsudevaḥ sarvāsunilayo'nalaḥ |",
            "darpahā darpado dṛpto durdharo'thāparājitaḥ"], "|| 76 ||",
           "The dwelling of all beings; Vāsudeva; the abode of every breath; the "
           "fire, never satisfied; destroyer of pride; giver of just pride; the "
           "exultant; hard to hold; and the unvanquished."),
        _v(["viśvamūrtirmahāmūrtirdīptamūrtiramūrtimān |",
            "anekamūrtiravyaktaḥ śatamūrtiḥ śatānanaḥ"], "|| 77 ||",
           "Whose form is the universe; of mighty form; of blazing form; yet "
           "without form; of many forms; the unmanifest; of a hundred forms; of "
           "a hundred faces."),
        _v(["eko naikaḥ savaḥ kaḥ kiṃ yat tatpadamanuttamam |",
            "lokabandhurlokanātho mādhavo bhaktavatsalaḥ"], "|| 78 ||",
           "The one; the many; the sacrifice; who is bliss; the 'what?' of "
           "enquiry; the 'which' and 'that' — the state than which none is "
           "higher; kinsman of the world; Lord of the world; Mādhava; tender to "
           "his devotees."),
        _v(["suvarṇavarṇo hemāṅgo varāṅgaścandanāṅgadī |",
            "vīrahā viṣamaḥ śūnyo ghṛtāśīracalaścalaḥ"], "|| 79 ||",
           "Of golden hue; of golden limbs; of beautiful form; wearing armlets "
           "bright as sandal; slayer of heroes; the incomparable; the void; in "
           "whom all wishes are dissolved; the unmoving; and the moving."),
        _v(["amānī mānado mānyo lokasvāmī trilokadhṛk |",
            "sumedhā medhajo dhanyaḥ satyamedhā dharādharaḥ"], "|| 80 ||",
           "Without pride; giver of honour; worthy of honour; Lord of the world; "
           "upholder of the three worlds; of fine intelligence; born of "
           "sacrifice; the fortunate; of true understanding; bearer of the "
           "earth."),
        _v(["tejovṛṣo dyutidharaḥ sarvaśastrabhṛtāṃ varaḥ |",
            "pragraho nigraho vyagro naikaśṛṅgo gadāgrajaḥ"], "|| 81 ||",
           "He who showers splendour; bearer of radiance; best of all who bear "
           "weapons; the receiver of offerings; the restrainer of all; intent "
           "upon his devotees; of many horns; elder brother of Gada."),
        _v(["caturmūrtiścaturbāhuścaturvyūhaścaturgatiḥ |",
            "caturātmā caturbhāvaścaturvedavidekapāt"], "|| 82 ||",
           "Of four forms; of four arms; of four vyūhas; the fourfold goal; of "
           "fourfold Self; source of the four ends of life; knower of the four "
           "Vedas; who stands on a single foot."),
        _v(["samāvarto'nivṛttātmā durjayo duratikramaḥ |",
            "durlabho durgamo durgo durāvāso durārihā"], "|| 83 ||",
           "The skilful turner of the wheel of becoming; whose Self never turns "
           "from dharma; hard to conquer; hard to transgress; hard to attain; "
           "hard to reach; the fortress; hard to dwell in; slayer of hard-"
           "pressing foes."),
        _v(["śubhāṅgo lokasāraṅgaḥ sutantustantuvardhanaḥ |",
            "indrakarmā mahākarmā kṛtakarmā kṛtāgamaḥ"], "|| 84 ||",
           "Of auspicious form; who draws the essence of the worlds as a bee "
           "the honey; the fair-spun web of the universe; who spreads that web; "
           "whose deeds are lordly; of mighty deeds; whose work is accomplished; "
           "author of the scriptures."),
        _v(["udbhavaḥ sundaraḥ sundo ratnanābhaḥ sulocanaḥ |",
            "arko vājasanaḥ śṛṅgī jayantaḥ sarvavijjayī"], "|| 85 ||",
           "The origin; the beautiful; the tender; whose navel is a jewel; of "
           "lovely eyes; worthy of worship; giver of food; the horned one who "
           "took the fish form; the victorious; the all-knowing conqueror."),
        _v(["suvarṇabindurakṣobhyaḥ sarvavāgīśvareśvaraḥ |",
            "mahāhrado mahāgarto mahābhūto mahānidhiḥ"], "|| 86 ||",
           "Whose limbs are like gold; the unshakable; Lord of the lords of all "
           "speech; the great lake; the great chasm; the great being; the great "
           "treasure."),
        _v(["kumudaḥ kundaraḥ kundaḥ parjanyaḥ pāvano'nilaḥ |",
            "amṛtāṃśo'mṛtavapuḥ sarvajñaḥ sarvatomukhaḥ"], "|| 87 ||",
           "He who delights in the earth; giver of what is pure as jasmine; the "
           "jasmine-white; the raincloud; the purifier; the wind; whose portion "
           "is nectar; whose body is deathless; the omniscient; whose face is "
           "turned every way."),
        _v(["sulabhaḥ suvrataḥ siddhaḥ śatrujicchatrutāpanaḥ |",
            "nyagrodho'dumbaro'śvatthaścāṇūrāndhraniṣūdanaḥ"], "|| 88 ||",
           "Easily attained; of noble vow; the perfect; conqueror of foes; "
           "scorcher of foes; the banyan that spreads downward; the "
           "sky-nourishing fig; the aśvattha, tree of the world; slayer of "
           "Cāṇūra of the Andhras."),
        _v(["sahasrārciḥ saptajihvaḥ saptaidhāḥ saptavāhanaḥ |",
            "amūrtiranagho'cintyo bhayakṛdbhayanāśanaḥ"], "|| 89 ||",
           "Of a thousand rays; of seven tongues of flame; of sevenfold fuel; "
           "borne by seven horses; the formless; the sinless; the unthinkable; "
           "who strikes fear into the wicked; who destroys the fear of the "
           "good."),
        _v(["aṇurbṛhatkṛśaḥ sthūlo guṇabhṛnnirguṇo mahān |",
            "adhṛtaḥ svadhṛtaḥ svāsyaḥ prāgvaṃśo vaṃśavardhanaḥ"], "|| 90 ||",
           "The atom; the vast; the slender; the gross; bearer of the qualities; "
           "yet without quality; the great; upheld by none; upheld by himself; "
           "of beautiful face; the primal lineage; increaser of lineage."),
        _v(["bhārabhṛt kathito yogī yogīśaḥ sarvakāmadaḥ |",
            "āśramaḥ śramaṇaḥ kṣāmaḥ suparṇo vāyuvāhanaḥ"], "|| 91 ||",
           "Bearer of the burden; proclaimed in scripture; the yogin; Lord of "
           "yogins; giver of all desires; the resting place; who wearies the "
           "unrighteous; who remains when all wanes; the fair-leaved tree of "
           "life; who rides upon the wind."),
        _v(["dhanurdharo dhanurvedo daṇḍo damayitā damaḥ |",
            "aparājitaḥ sarvasaho niyantā'niyamo'yamaḥ"], "|| 92 ||",
           "Bearer of the bow; knower of the science of archery; the rod of "
           "rule; the subduer; self-restraint itself; the unvanquished; the "
           "all-enduring; the controller; bound by no rule; subject to no "
           "restraint."),
        _v(["sattvavān sāttvikaḥ satyaḥ satyadharmaparāyaṇaḥ |",
            "abhiprāyaḥ priyārho'rhaḥ priyakṛt prītivardhanaḥ"], "|| 93 ||",
           "Full of strength and goodness; of the nature of sattva; the true; "
           "devoted to truth and dharma; the one intended by all seekers; worthy "
           "of our love; worthy of worship; doer of what is dear; increaser of "
           "delight."),
        _v(["vihāyasagatirjyotiḥ surucirhutabhugvibhuḥ |",
            "ravirvirocanaḥ sūryaḥ savitā ravilocanaḥ"], "|| 94 ||",
           "Who moves through the sky; the light; of beautiful radiance; the "
           "eater of oblations; the all-pervading; the sun; the shining; Sūrya; "
           "the impeller; whose eye is the sun."),
        _v(["ananto hutabhugbhoktā sukhado naikajo'grajaḥ |",
            "anirviṇṇaḥ sadāmarṣī lokādhiṣṭhānamadbhutaḥ"], "|| 95 ||",
           "The endless; enjoyer of oblations; the enjoyer; giver of happiness; "
           "born many times; the first-born; never despondent; ever forbearing; "
           "the ground of the worlds; the wonderful."),
        _v(["sanātsanātanatamaḥ kapilaḥ kapiravyayaḥ |",
            "svastidaḥ svastikṛtsvasti svastibhuksvastidakṣiṇaḥ"], "|| 96 ||",
           "The ancient; most ancient of all; Kapila; the tawny sun; the "
           "imperishable; giver of well-being; maker of well-being; well-being "
           "itself; enjoyer of well-being; who bestows well-being as his gift."),
        _v(["araudraḥ kuṇḍalī cakrī vikramyūrjitaśāsanaḥ |",
            "śabdātigaḥ śabdasahaḥ śiśiraḥ śarvarīkaraḥ"], "|| 97 ||",
           "Free of cruelty; wearing earrings; bearer of the discus; the "
           "valorous; whose command is mighty; beyond the reach of words; who "
           "bears all sound; the cool refuge; maker of the night."),
        _v(["akrūraḥ peśalo dakṣo dakṣiṇaḥ kṣamiṇāṃvaraḥ |",
            "vidvattamo vītabhayaḥ puṇyaśravaṇakīrtanaḥ"], "|| 98 ||",
           "Free of harshness; graceful; the skilful; the courteous; best of the "
           "patient; wisest of the wise; free of fear; whose hearing and whose "
           "praise alike are holy."),
        _v(["uttāraṇo duṣkṛtihā puṇyo duḥsvapnanāśanaḥ |",
            "vīrahā rakṣaṇaḥ santo jīvanaḥ paryavasthitaḥ"], "|| 99 ||",
           "Who lifts beings across; destroyer of evil deeds; the holy; "
           "destroyer of evil dreams; who ends the round of births; the "
           "protector; the good; the life of all; who abides everywhere."),
        _v(["anantarūpo'nantaśrīrjitamanyurbhayāpahaḥ |",
            "caturaśro gabhīrātmā vidiśo vyādiśo diśaḥ"], "|| 100 ||",
           "Of endless forms; of endless splendour; conqueror of wrath; remover "
           "of fear; the four-square and just; of profound Self; giver of "
           "various fruits; who assigns each his due; the quarters "
           "themselves."),
        _v(["anādirbhūrbhuvo lakṣmīḥ suvīro rucirāṅgadaḥ |",
            "janano janajanmādirbhīmo bhīmaparākramaḥ"], "|| 101 ||",
           "Without beginning; the earth; the splendour of the worlds; of "
           "goodly valour; wearing bright armlets; the begetter; the first cause "
           "of all births; the terrible; of terrible prowess."),
        _v(["ādhāranilayo'dhātā puṣpahāsaḥ prajāgaraḥ |",
            "ūrdhvagaḥ satpathācāraḥ prāṇadaḥ praṇavaḥ paṇaḥ"], "|| 102 ||",
           "The support of every support; who needs no upholder; whose smile is "
           "the opening of flowers; the ever-wakeful; who moves upward; who "
           "walks the path of the good; giver of life; the praṇava; the "
           "sustainer."),
        _v(["pramāṇaṃ prāṇanilayaḥ prāṇabhṛtprāṇajīvanaḥ |",
            "tattvaṃ tattvavidekātmā janmamṛtyujarātigaḥ"], "|| 103 ||",
           "The measure of all knowing; the abode of the life-breath; sustainer "
           "of breath; the life of every breath; Reality itself; knower of "
           "Reality; the one Self; who has passed beyond birth, death and "
           "old age."),
        _v(["bhūrbhuvaḥsvastarustāraḥ savitā prapitāmahaḥ |",
            "yajño yajñapatiryajvā yajñāṅgo yajñavāhanaḥ"], "|| 104 ||",
           "The tree of the three worlds — earth, mid-air and heaven; the "
           "deliverer; the impeller; the great-grandfather of all; the "
           "sacrifice; lord of sacrifice; the sacrificer; whose limbs are the "
           "sacrifice; who bears the sacrifice."),
        _v(["yajñabhṛd yajñakṛd yajñī yajñabhuk yajñasādhanaḥ |",
            "yajñāntakṛd yajñaguhyamannamannāda eva ca"], "|| 105 ||",
           "Upholder of sacrifice; maker of sacrifice; enjoyer of sacrifice; "
           "eater of the offering; the means of sacrifice; who brings sacrifice "
           "to its end; the secret of sacrifice; the food; and the eater of "
           "food."),
        _v(["ātmayoniḥ svayaṃjāto vaikhānaḥ sāmagāyanaḥ |",
            "devakīnandanaḥ sraṣṭā kṣitīśaḥ pāpanāśanaḥ"], "|| 106 ||",
           "Whose womb is himself; self-born; who dug through the earth as the "
           "boar; singer of the Sāman; the joy of Devakī; the creator; Lord of "
           "the earth; destroyer of sin."),
        _v(["śaṅkhabhṛnnandakī cakrī śārṅgadhanvā gadādharaḥ |",
            "rathāṅgapāṇirakṣobhyaḥ sarvapraharaṇāyudhaḥ"], "|| 107 ||",
           "Bearer of the conch; wielder of the sword Nandaka; bearer of the "
           "discus; of the bow Śārṅga; bearer of the mace; with the chariot-"
           "wheel in his hand; the unshakable; whose weapons are all weapons."),
        _v(["vanamālī gadī śārṅgī śaṅkhī cakrī ca nandakī |",
            "śrīmān nārāyaṇo viṣṇurvāsudevo'bhirakṣatu"], "|| 108 ||",
           "Wearing the forest garland, bearing mace and Śārṅga bow, conch and "
           "discus and the sword Nandaka — may the glorious Nārāyaṇa, Viṣṇu, "
           "Vāsudeva, protect us on every side."),
        "ornament",
        # ── closing prayer ───────────────────────────────────────────────
        _v(["acyutānantagovindanāmoccāraṇabheṣajāt |",
            "naśyanti sakalā rogāssatyaṃ satyaṃ vadāmyaham"], "",
           "By the medicine that is the uttering of the names Acyuta, Ananta and "
           "Govinda, all ills are destroyed — this is the truth, the truth I "
           "speak."),
        _v(["śarīre jarjarībhūte vyādhigraste kalevare |",
            "auṣadhaṃ jāhnavītoyaṃ vaidyo nārāyaṇo hariḥ"], "",
           "When the body is worn out and the frame seized by disease, the "
           "medicine is the water of the Ganges and the physician is Nārāyaṇa, "
           "Hari."),
        _v(["āloḍya sarvaśāstrāṇi vicārya ca punaḥ punaḥ |",
            "idamekaṃ suniṣpannaṃ dhyeyo nārāyaṇo hariḥ"], "",
           "Having churned all the scriptures and pondered them again and again, "
           "this one thing stands well established: Nārāyaṇa, Hari, is to be "
           "meditated upon."),
        _v(["yadakṣarapadabhraṣṭaṃ mātrāhīnaṃ tu yadbhavet |",
            "tatsarvaṃ kṣamyatāṃ deva nārāyaṇa namo'stu te"], "",
           "Whatever has slipped in syllable or word, whatever has fallen short "
           "in measure — forgive it all, O God; salutation be to you, "
           "Nārāyaṇa."),
        _v(["visargabindumātrāṇi padapādākṣarāṇi ca |",
            "nyūnāni cātiriktāni kṣamasva puruṣottama"], "",
           "Visargas, anusvāras and vowel-lengths, words, quarter-verses and "
           "syllables — whatever is wanting or in excess, forgive it, O supreme "
           "Person."),
    ],
}
