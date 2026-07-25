# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain, raw wikitext) via teltools
# dev2iast. Translations original. Mukunda Mālā of Kulaśekhara Āḻvār — a
# garland of verses to Mukunda / Kṛṣṇa (40 verses + an opening dedication).

def _v(l1, l2, n, gloss):
    num = f"|| {n} ||" if n else ""
    return {"padas": [l1 + " |", l2], "num": num, "gloss": gloss}


STOTRA = {
    "deity": "vishnu",
    "doc_title": "Mukunda Mālā",
    "app_title": "Mukunda Mālā",
    "h1": "Mukunda Mālā",
    "subtitle": "A Garland to Mukunda · Kulaśekhara",
    "footer": "Source: Sanskrit Wikisource — Mukundamālā (public domain)",
    "sections": [
        _v("ghuṣyate yasya nagare raṅgayātrā dine dine",
           "tam ahaṃ śirasā vande rājānaṃ kulaśekharam", "",
           "In whose city the temple-procession is proclaimed day after day — "
           "that king, Kulaśekhara, I revere with my head."),
        "ornament",
        _v("śrīvallabheti varadeti dayāpareti bhaktapriyeti bhavaluṇṭhanakovideti",
           "nātheti nāgaśayaneti jagannivāsetyālāpinaṃ pratidinaṃ kuru māṃ mukunda", 1,
           "'O beloved of Śrī, O boon-giver, O compassionate one, O lover of "
           "devotees, O adept at plundering away worldly bondage, O Lord, O "
           "serpent-reclining one, O dwelling of the worlds' — O Mukunda, make me "
           "one who calls on You thus each day."),
        _v("jayatu jayatu devo devakīnandano 'yaṃ jayatu jayatu kṛṣṇo vṛṣṇivaṃśapradīpaḥ",
           "jayatu jayatu meghaśyāmalaḥ komalāṅgo jayatu jayatu pṛthvībhāranāśo mukundaḥ", 2,
           "Victory, victory to this God, the son of Devakī! Victory to Kṛṣṇa, "
           "lamp of the Vṛṣṇi line! Victory to the cloud-dark, tender-limbed one! "
           "Victory, victory to Mukunda, remover of earth's burden!"),
        _v("mukunda mūrdhnā praṇipatya yāce bhavantamekāntamiyantamartham",
           "avismṛtistvaccaraṇāravinde bhave bhave me'stu bhavatprasādāt", 3,
           "O Mukunda, bowing my head, I beg of You this one thing alone: by Your "
           "grace, may I never forget Your lotus feet, birth after birth."),
        _v("nāhaṃ vande tava caraṇayordvandvam advandvahetoḥ kumbhīpākaṃ gurum api hare nārakaṃ nāpanetum",
           "ramyā rāmā mṛdutanulatā nandane nāpi rantuṃ bhāve bhāve hṛdayabhavane bhāvayeyaṃ bhavantam", 4,
           "I bow to Your feet not to escape the dreadful Kumbhīpāka hell, nor to "
           "sport with lovely, tender women in the pleasure-groves — but that in "
           "birth after birth, in the dwelling of my heart, I may ever meditate "
           "on You."),
        _v("nāsthā dharme na vasunicaye naiva kāmopabhoge yad bhāvyaṃ tad bhavatu bhagavan pūrvakarmānurūpam",
           "etat prārthyaṃ mama bahumataṃ janmajanmāntare'pi tvatpādāmbhoruhayugagatā niścalā bhaktirastu", 5,
           "No faith have I in dharma, nor in heaps of wealth, nor in enjoying "
           "pleasures; whatever must be, let it be, O Lord, according to my past "
           "deeds. This alone is my cherished prayer: birth after birth, may I "
           "have unwavering devotion to the pair of Your lotus feet."),
        _v("divi vā bhuvi vā mamāstu vāso narake vā narakāntaka prakāmam",
           "avadhīritaśāradāravindau caraṇau te maraṇe'pi cintayāmi", 6,
           "In heaven, on earth, or in hell — let my dwelling be where it will, O "
           "slayer of Naraka; for even at death I shall meditate on Your feet, "
           "which put the autumn lotus to shame."),
        _v("kṛṣṇa tvadīyapadapaṅkajapañjarāntar adyaiva me viśatu mānasarājahaṃsaḥ",
           "prāṇaprayāṇasamaye kaphavātapittaiḥ kaṇṭhāvarodhanavidhau smaraṇaṃ kutaste", 7,
           "O Kṛṣṇa, this very day let the royal swan of my mind enter the cage "
           "of Your lotus feet; for at the hour of death, when the throat is "
           "choked by phlegm, wind, and bile, how shall remembrance of You be "
           "possible?"),
        _v("cintayāmi harimeva santataṃ mandamandahāsitānanāmbujam",
           "nandagopatanayaṃ parātparaṃ nāradādimunivṛndavanditam", 8,
           "I meditate ceaselessly on Hari alone — his lotus-face softly smiling, "
           "the son of Nanda the cowherd, higher than the highest, worshipped by "
           "the throngs of sages led by Nārada."),
        _v("karacaraṇasaroje kāntimannetramīne śramamuṣi bhujavīcivyākule'gādhamārge",
           "harisarasi vigāhyāpīya tejojalaughaṃ bhavamaruparikhinnaḥ khedamadya tyajāmi", 9,
           "Plunging into the lake that is Hari — its lotuses his hands and feet, "
           "its fish his lustrous eyes, its deep waters stirred by the waves of "
           "his arms — and drinking my fill of the flood of his radiance, weary "
           "from the desert of existence, today I cast off my sorrow."),
        _v("sarasijanayane saśaṅkhacakre murabhidi mā viramasva citta rantum",
           "sukhataram aparaṃ na jātu jāne haricaraṇasmaraṇāmṛtena tulyam", 10,
           "O my mind, do not cease to sport in the lotus-eyed slayer of Mura who "
           "bears conch and discus; for I know of no other joy at all equal to "
           "the nectar of remembering Hari's feet."),
        _v("mābhīr mandamano vicintya bahudhā yāmīś ciraṃ yātanā nāmī naḥ prabhavanti pāparipavaḥ svāmī nanu śrīdharaḥ",
           "ālasyaṃ vyapanīya bhaktisulabhaṃ dhyāyasva nārāyaṇaṃ lokasya vyasanāpanodanakaro dāsasya kiṃ na kṣamaḥ", 11,
           "Fear not, O dull mind, brooding 'long shall I go to torments' — these "
           "sinful foes cannot prevail over us, for our Lord is surely Śrīdhara. "
           "Casting off sloth, meditate on Nārāyaṇa, so easily won by devotion: "
           "is the remover of the world's distress unable to save his servant?"),
        _v("bhavajaladhigatānāṃ dvandvavātāhatānāṃ sutaduhitṛkalatratrāṇabhārārditānām",
           "viṣamaviṣayatoye majjatām aplavānāṃ bhavatu śaraṇam eko viṣṇupoto narāṇām", 12,
           "For men fallen into the ocean of existence, battered by the winds of "
           "the pairs of opposites, burdened with protecting son, daughter, and "
           "wife, sinking rudderless in the dread waters of the senses — may "
           "Viṣṇu, the one ship, be their refuge."),
        _v("bhavajaladhim agādhaṃ dustaraṃ nistareyaṃ katham aham iti ceto mā sma gāḥ kātaratvam",
           "sarasijadṛśi deve tāvakī bhaktir ekā narakabhidi niṣaṇṇā tārayiṣyaty avaśyam", 13,
           "'How shall I cross this fathomless, hard-to-cross ocean of "
           "existence?' — O mind, fall not into such faint-heartedness; devotion "
           "alone to that lotus-eyed Lord, slayer of Naraka, once fixed within, "
           "will surely carry you across."),
        _v("tṛṣṇātoye madanapavanoddhūtamohormimāle dārāvarte tanayasahajagrāhasaṅghākule ca",
           "saṃsārākhye mahati jaladhau majjatāṃ nas tridhāman pādāmbhoje varada bhavato bhaktināvaṃ prayaccha", 14,
           "In the great ocean called saṃsāra — its water thirst, its "
           "delusion-waves whipped up by the wind of passion, its whirlpool "
           "one's wife, its crocodile-hosts one's children and kin — to us who "
           "sink there, O Lord of the three abodes, O boon-giver, grant the boat "
           "of devotion to Your lotus feet."),
        _v("mā drākṣaṃ kṣīṇapuṇyān kṣaṇam api bhavato bhaktihīnān padābje mā śrauṣaṃ śrāvyabandhaṃ tava caritam apāsyānyad ākhyānajātam",
           "mā smārṣaṃ mādhava tvām api bhuvanapate cetasāpahnuvānān mā bhūvaṃ tvatsaparyāvyatikararahito janmajanmāntare 'pi", 15,
           "May I never look, even a moment, on those poor in merit and devoid of "
           "devotion to Your feet; never hear any tale but Your deeds worthy to "
           "be heard; never remember, O Mādhava, those who deny You in their "
           "hearts; and never, birth after birth, be without a share in Your "
           "worship."),
        _v("jihve kīrtaya keśavaṃ muraripuṃ ceto bhaja śrīdharaṃ pāṇidvandva samarcayācyutakathāḥ śrotradvaya tvaṃ śṛṇu",
           "kṛṣṇaṃ lokaya locanadvaya harer gacchāṅghriyugmālayaṃ jighra ghrāṇa mukundapādatulasīṃ mūrdhan namādhokṣajam", 16,
           "O tongue, praise Keśava; O mind, worship Śrīdhara; O hands, honour "
           "him; O ears, hear the tales of Acyuta; O eyes, behold Kṛṣṇa; O feet, "
           "go to the abode of Hari's feet; O nose, smell the tulasī of "
           "Mukunda's feet; O head, bow to Adhokṣaja."),
        _v("he lokāḥ śṛṇuta prasūtimaraṇavyādheś cikitsām imāṃ yogajñāḥ samudāharanti munayo yāṃ yājñavalkyādayaḥ",
           "antarjyotir ameyam ekam amṛtaṃ kṛṣṇākhyam āpīyatāṃ tat pītaṃ paramauṣadhaṃ vitanute nirvāṇam ātyantikam", 17,
           "O people, hear this remedy for the disease of birth and death, which "
           "the yoga-knowing sages, Yājñavalkya and the rest, proclaim: let there "
           "be drunk that one immeasurable, immortal inner light named Kṛṣṇa — "
           "that supreme medicine, once drunk, brings absolute liberation."),
        _v("he martyāḥ paramaṃ hitaṃ śṛṇuta vo vakṣyāmi saṅkṣepataḥ saṃsārārṇavam āpadūrmibahulaṃ samyak praviśya sthitāḥ",
           "nānājñānam apāsya cetasi namo nārāyaṇāyety amuṃ mantraṃ sapraṇavaṃ praṇāmasahitaṃ prāvartayadhvaṃ muhuḥ", 18,
           "O mortals, hear the supreme good I shall tell in brief: standing "
           "having entered fully into the ocean of saṃsāra thick with the waves "
           "of calamity — cast aside all varied learning, and in your minds set "
           "going again and again, with praṇava and prostration, this mantra: "
           "'oṃ namo nārāyaṇāya.'"),
        _v("pṛthvī reṇur aṇuḥ payāṃsi kaṇikāḥ phalguḥ sphuliṅgo laghuḥ tejo niḥśvasanaṃ marut tanutaraṃ randhraṃ susūkṣmaṃ nabhaḥ",
           "kṣudrā rudrapitāmahaprabhṛtayaḥ kīṭāḥ samastāḥ surāḥ dṛṣṭe yatra sa tāvako vijayate bhūmāvadhūtāvadhiḥ", 19,
           "The earth but a mote, the waters a droplet, fire a faint spark, the "
           "mighty wind a breath, the vast ether a tiny hole; Rudra, Brahmā, and "
           "the rest mere insects, and all the gods — when He is seen: victorious "
           "is that (Lord) of Yours, whose vastness is beyond all bound."),
        _v("baddhenāñjalinā natena śirasā gātraiḥ saromodgamaiḥ kaṇṭhena svaragadgadena nayanenodgīrṇabāṣpāmbunā",
           "nityaṃ tvaccaraṇāravindayugaladhyānāmṛtāsvādinām asmākaṃ sarasīruhākṣa satataṃ sampadyatāṃ jīvitam", 20,
           "With folded hands, bowed head, limbs thrilling with joy, throat "
           "faltering in speech, eyes brimming with tears — for us who ever taste "
           "the nectar of meditating on Your two lotus feet, O lotus-eyed one, "
           "may our life be ever thus fulfilled."),
        _v("he gopālaka he kṛpājalanidhe he sindhukanyāpate he kaṃsāntaka he gajendrakaruṇāpārīṇa he mādhava",
           "he rāmānuja he jagattrayaguro he puṇḍarīkākṣa māṃ he gopījananātha pālaya paraṃ jānāmi na tvāṃ vinā", 21,
           "O cowherd! O ocean of mercy! O consort of the sea's daughter! O "
           "slayer of Kaṃsa! O You who pitied the elephant-king! O Mādhava! O "
           "younger brother of Balarāma! O guru of the three worlds! O "
           "lotus-eyed! O Lord of the cowherd-women — protect me; apart from You "
           "I know none."),
        _v("bhaktāpāyabhujāṅgagāruḍamaṇis trailokyarakṣāmaṇir gopīlocanacātakāmbudamaṇiḥ saundaryamudrāmaṇiḥ",
           "yaḥ kāntāmaṇirukmiṇīghanakucadvandvaikabhūṣāmaṇiḥ śreyo devaśikhāmaṇir diśatu no gopālacūḍāmaṇiḥ", 22,
           "The Garuḍa-gem against the serpent of devotees' peril, the "
           "crest-jewel guarding the three worlds, the rain-cloud gem to the "
           "cātaka-birds that are the gopīs' eyes, the seal-gem of beauty, the "
           "lover-gem, the sole ornament on Rukmiṇī's breast, the crown-jewel of "
           "gods — may that crest-gem of cowherds grant us blessing."),
        _v("śatrucchedaikamantraṃ sakalam upaniṣadvākyasampūjyamantraṃ saṃsārottāramantraṃ samupacitatamasaḥ saṅghaniryāṇamantram",
           "sarvaiśvaryaikamantraṃ vyasanabhujagasandaṣṭasantrāṇamantraṃ jihve śrīkṛṣṇamantraṃ japa japa satataṃ janmasāphalyamantram", 23,
           "The one mantra that cuts down foes, the mantra worshipped by all the "
           "words of the Upaniṣads, the mantra that ferries across saṃsāra, the "
           "mantra of deliverance from gathered darkness, the one mantra of all "
           "sovereignty, the mantra of rescue from the serpent-bite of calamity "
           "— O tongue, recite ever the Śrī-Kṛṣṇa mantra that makes birth "
           "fruitful."),
        _v("vyāmohapraśamauṣadhaṃ munimanovṛttipravṛttyauṣadhaṃ daityendrārtikarauṣadhaṃ tribhuvane sañjīvanaikauṣadham",
           "bhaktātyantahitauṣadhaṃ bhavabhayapradhvaṃsanaikauṣadhaṃ śreyaḥprāptikarauṣadhaṃ piba manaḥ śrīkṛṣṇadivyauṣadham", 24,
           "The medicine that stills delusion, that sets the sages' contemplation "
           "going, that torments the demon-kings, the one elixir of life in the "
           "three worlds, the utterly wholesome medicine for devotees, the sole "
           "medicine that destroys the fear of existence, that wins the highest "
           "good — drink, O mind, the divine medicine that is Śrī Kṛṣṇa."),
        _v("āmnāyābhyasanāny araṇyaruditaṃ vedavratāny anvahaṃ medaśchedaphalāni pūrtavidhayaḥ sarve hutaṃ bhasmani",
           "tīrthānām avagāhanāni ca gajasnānaṃ vinā yatpadadvandvāmbhoruhasaṃsmṛtīr vijayate devaḥ sa nārāyaṇaḥ", 25,
           "Recitations of scripture are a weeping in the wilderness; daily Vedic "
           "vows but the reducing of fat; all rites of merit an offering into "
           "ashes; bathings at holy fords but an elephant's bath — without the "
           "remembrance of whose two lotus feet: victorious is that God, "
           "Nārāyaṇa."),
        _v("śrīmannāma procya nārāyaṇākhyaṃ ke na prāpur vāñchitaṃ pāpino 'pi",
           "hā naḥ pūrvaṃ vāk pravṛttā na tasmiṃs tena prāptaṃ garbhavāsādiduḥkham", 26,
           "By uttering the glorious name called Nārāyaṇa, what desire have even "
           "sinners not gained? Alas, in the past our speech was not turned to "
           "that name — and thereby we won the sorrows of dwelling in the womb, "
           "and the rest."),
        _v("majjanmanaḥ phalam idaṃ madhukaiṭabhāre matprārthanīyamadanugraha eṣa eva",
           "tvadbhṛtyabhṛtyaparicārakabhṛtyabhṛtyabhṛtyasya bhṛtya iti māṃ smara lokanātha", 27,
           "This is the fruit of my birth, O foe of Madhu and Kaiṭabha; this "
           "alone the favour I pray of You: remember me, O Lord of the world, as "
           "'the servant of the servant of the servant of the servant of the "
           "attendant of Your servant's servant.'"),
        _v("nāthe naḥ puruṣottame trijagatāṃ ekādhipe cetasā sevye svasya padasya dātari sure nārāyaṇe tiṣṭhati",
           "yaṃ kañcit puruṣādhamaṃ katipayagrāmeśam alpārthadaṃ sevāyai mṛgayāmahe naram aho mūkā varākā vayam", 28,
           "While our Lord stands there — Puruṣottama, sole sovereign of the "
           "three worlds, to be served by the mind, the giver of His own state, "
           "the god Nārāyaṇa — we go seeking, for service, some lowest of men, "
           "lord of a few villages, giver of trifles. Alas, dumb and wretched "
           "are we!"),
        _v("madana parihara sthitiṃ madīye manasi mukundapadāravindadhāmni",
           "haranayanakṛśānunā kṛśo 'si smarasi na cakraparākramaṃ murāreḥ", 29,
           "O Passion, quit your dwelling in my mind, the abode of Mukunda's "
           "lotus feet; already are you withered by the fire of Hara's eye — do "
           "you not recall the might of Murāri's discus?"),
        _v("tattvaṃ bruvāṇāni paraṃ parastān madhu kṣarantīva satāṃ phalāni",
           "prāvartaya prāñjalir asmi jihve nāmāni nārāyaṇagocarāṇi", 30,
           "The names within reach of Nārāyaṇa — declaring the Truth beyond the "
           "beyond, dripping honey as it were, the very fruit of the good — set "
           "them going, O tongue; with joined palms I stand."),
        _v("idaṃ śarīraṃ pariṇāmapeśalaṃ pataty avaśyaṃ ślathasandhijarjaram",
           "kim auṣadhaiḥ kliśyasi mūḍha durmate nirāmayaṃ kṛṣṇarasāyanaṃ piba", 31,
           "This body, tender to decay, decrepit with loosened joints, must "
           "surely fall. Why torment yourself with medicines, O foolish, "
           "ill-minded one? Drink the disease-free elixir that is Kṛṣṇa."),
        _v("dārā vārākaravarasutā te tanūjo viriñcaḥ stotā vedas tava suragaṇo bhṛtyavargaḥ prasādaḥ",
           "muktir māyā jagad avikalaṃ tāvakī devakī te mātā mitraṃ balaripusutas tvayy ato 'nyan na jāne", 32,
           "Your wife is the ocean's daughter; Your son is Viriñca (Brahmā); Your "
           "praiser is the Veda; the host of gods, Your retinue; liberation, but "
           "Your favour; Māyā, the whole undivided world, is Yours; Devakī is "
           "Your mother; Your friend is Arjuna — so, apart from You, I know "
           "nothing."),
        _v("kṛṣṇo rakṣatu no jagattrayaguruḥ kṛṣṇaṃ namasyāmy ahaṃ kṛṣṇenāmaraśatravo vinihatāḥ kṛṣṇāya tasmai namaḥ",
           "kṛṣṇād eva samutthitaṃ jagad idaṃ kṛṣṇasya dāso 'smy ahaṃ kṛṣṇe tiṣṭhati sarvam etad akhilaṃ he kṛṣṇa saṃrakṣa mām", 33,
           "May Kṛṣṇa, guru of the three worlds, protect us; Kṛṣṇa I salute; by "
           "Kṛṣṇa the foes of the gods were slain; to that Kṛṣṇa, salutation. "
           "From Kṛṣṇa alone this world arose; of Kṛṣṇa I am the servant; in "
           "Kṛṣṇa all this rests — O Kṛṣṇa, protect me."),
        _v("sa tvaṃ prasīda bhagavan kuru mayy anāthe viṣṇo kṛpāṃ paramakāruṇikaḥ kila tvam",
           "saṃsārasāgaranimagnam ananta dīnam uddhartum arhasi hare puruṣottamo 'si", 34,
           "You, that very Lord, be gracious! Show mercy to me, the helpless, O "
           "Viṣṇu; surely You are supremely compassionate. Me, sunk in the ocean "
           "of saṃsāra, wretched, O Ananta, You ought to lift up, O Hari, for You "
           "are Puruṣottama."),
        _v("namāmi nārāyaṇapādapaṅkajaṃ karomi nārāyaṇapūjanaṃ sadā",
           "vadāmi nārāyaṇanāma nirmalaṃ smarāmi nārāyaṇatattvam avyayam", 35,
           "I bow to the lotus feet of Nārāyaṇa; I ever perform the worship of "
           "Nārāyaṇa; I utter the spotless name of Nārāyaṇa; I remember the "
           "imperishable truth of Nārāyaṇa."),
        _v("śrīnātha nārāyaṇa vāsudeva śrīkṛṣṇa bhaktapriya cakrapāṇe",
           "śrīpadmanābhācyuta kaiṭabhāre śrīrāma padmākṣa hare murāre", 36,
           "O Śrīnātha! Nārāyaṇa! Vāsudeva! Śrī Kṛṣṇa! Lover of devotees! "
           "Discus-bearer! Śrī Padmanābha! Acyuta! Foe of Kaiṭabha! Śrī Rāma! "
           "Lotus-eyed! Hari! Murāri!"),
        _v("ananta vaikuṇṭha mukunda kṛṣṇa govinda dāmodara mādhaveti",
           "vaktuṃ samartho 'pi na vakti kaścid aho janānāṃ vyasanābhimukhyam", 37,
           "'Ananta, Vaikuṇṭha, Mukunda, Kṛṣṇa, Govinda, Dāmodara, Mādhava' — "
           "though able to say it, no one says it. Alas, how bent are people "
           "toward calamity!"),
        _v("dhyāyanti ye viṣṇum anantam avyayaṃ hṛtpadmamadhye satataṃ vyavasthitam",
           "samāhitānāṃ satatābhayapradaṃ te yānti siddhiṃ paramāṃ tu vaiṣṇavīm", 38,
           "Those who meditate on Viṣṇu — endless, imperishable, ever seated in "
           "the lotus of the heart, granting constant fearlessness to the "
           "collected in mind — they attain the supreme Vaiṣṇava perfection."),
        _v("kṣīrasāgarataraṅgaśīkarāsāratārakitacārumūrtaye",
           "bhogibhogaśayanīyaśāyine mādhavāya madhuvidviṣe namaḥ", 39,
           "To Him whose lovely form is star-spangled with the spray of the "
           "milk-ocean's waves, who reclines on the serpent's coils as his couch "
           "— to Mādhava, foe of Madhu, salutation."),
        _v("yasya priyau śrutidharau kavilokavīrau mitre dvijanmavarapadmaśarāv abhūtām",
           "tenāmbujākṣacaraṇāmbujaṣaṭpadena rājñā kṛtā kṛtir iyaṃ kulaśekhareṇa", 40,
           "By that king Kulaśekhara — a bee at the lotus feet of the lotus-eyed "
           "Lord, whose two dear friends, bearers of the Veda and heroes among "
           "poets, were as choice lotus-arrows — this work was made."),
    ],
}
