# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Śrī Satyanārāyaṇa Vratakalpam — the complete vrata as observed in the
# Annavaram (Śrī Vīra Veṅkaṭa Satyanārāyaṇa Svāmi) tradition: saṅkalpa,
# Gaṇapati pūjā, the lokapālas, navagrahas and dikpālas, the ṣoḍaśopacāra
# pūjā of Satyanārāyaṇa, and the five-chapter kathā of the Skānda Purāṇa
# (Revākhaṇḍa). Sanskrit keyed from Telugu-script vratakalpam booklets of the
# Annavaram tradition (maintainer's compilation). The booklets' Telugu
# instructions and Telugu meanings (tātparya) are NOT reproduced: rubrics and
# glosses here are original English, translated from the Sanskrit. Spacing,
# anusvāra and ḷ are normalised to site convention; every textual correction
# is logged in SOURCES.md §7.2. The Viṣṇu Sahasranāmāvaḷi appended to the
# booklet is omitted (the site carries the Sahasranāma stotra itself).


def _v(padas, gloss, num=""):
    return {"padas": padas, "num": num, "gloss": gloss}


def _p(padas, gloss):                    # long ritual prose, set a size down
    d = _v(padas, gloss)
    d["prose"] = True
    return d


def _h(text):
    return {"heading": text}


def _r(text):
    return {"rubric": text}


def _names(names, gloss, suffix="namaḥ"):
    return _p([f"oṃ {n} {suffix}" for n in names], gloss)


def _chunks(names, size):
    return [names[i:i + size] for i in range(0, len(names), size)]


# the offering formula repeated after each upacāra
SN = "ādyādi mahālakṣmīsameta śrī vīraveṅkaṭa satyanārāyaṇa svāmine namaḥ"

S = []

# ───────────────────────── preliminaries ─────────────────────────
S += [
    _h("Pūrvāṅgam · the preliminaries"),
    _r("The vrata may be kept on a full-moon day, an Ekādaśī, the day the sun "
       "enters a new sign, or any auspicious day, in the evening or the morning, "
       "after bathing and the daily rites. Clean the place of worship, draw a "
       "rangoli of rice-flour, turmeric and kuṅkuma, raise a small maṇḍapa hung "
       "with mango leaves, and light the lamp. Sit facing east or north. "
       "Devotion matters more than expense: do it as your means allow."),
    _r("Husband and wife stand together holding betel leaves with a fruit (or a "
       "tender coconut) and bow."),
    _v(["oṃ devīṃ vācamajanayanta devāstāṃ viśvarūpāḥ paśavo vadanti |",
        "sā no mandreṣamūrjaṃ duhānā dhenurvāgasmānupa suṣṭutaitu ||",
        "ayaṃ muhūrtassumuhūrto'stu ||"],
       "The gods brought forth the goddess Speech; creatures of every form give "
       "voice to her. May she, delightful, yielding refreshment and strength "
       "like a milch-cow, come to us, well praised. May this hour be an "
       "auspicious hour."),
    _r("The betel leaves are set down on plates."),
    _v(["yāḥ phalinīryā aphalā apuṣpā yāśca puṣpiṇīḥ |",
        "bṛhaspatiprasūtāstā no muñcantvagṃhasaḥ ||"],
       "The plants that bear fruit and those that bear none, the flowerless and "
       "the flowering — sent forth by Bṛhaspati, may they free us from distress."),
    _v(["phalaṃ manorathaphalaṃ putrapautrapravardhanam |",
        "yasmāttasmācchivaṃ me syādataśśāntiṃ prayaccha me ||",
        "phaladānakalpoktasampūrṇasakalaphalāvāptirastu ||",
        "manorathaphalasiddhirastu ||"],
       "This fruit is the fruit of the heart's wish, increasing sons and "
       "grandsons; so may it bring me good, and grant me peace. May every fruit "
       "promised for the gift of fruit be fully gained; may the heart's wish be "
       "fulfilled."),
    _r("Sip water (ācamana). Light the lamp, offer akṣata and bow; then sip "
       "three times more from the spoon, reciting the twenty-four names."),
    _h("Ācamanam · the twenty-four names"),
    _p(["oṃ keśavāya svāhā | oṃ nārāyaṇāya svāhā | oṃ mādhavāya svāhā |",
        "oṃ govindāya namaḥ | oṃ viṣṇave namaḥ | oṃ madhusūdanāya namaḥ |",
        "oṃ trivikramāya namaḥ | oṃ vāmanāya namaḥ | oṃ śrīdharāya namaḥ |",
        "oṃ hṛṣīkeśāya namaḥ | oṃ padmanābhāya namaḥ | oṃ dāmodarāya namaḥ |",
        "oṃ saṅkarṣaṇāya namaḥ | oṃ vāsudevāya namaḥ | oṃ pradyumnāya namaḥ |",
        "oṃ aniruddhāya namaḥ | oṃ puruṣottamāya namaḥ | oṃ adhokṣajāya namaḥ |",
        "oṃ nārasiṃhāya namaḥ | oṃ acyutāya namaḥ | oṃ janārdanāya namaḥ |",
        "oṃ upendrāya namaḥ | oṃ haraye namaḥ | oṃ kṛṣṇāya namaḥ ||"],
       "Water is sipped at each of the first three names (svāhā); the hands are "
       "washed at the next two; the rest are recited with salutation. Keśava, "
       "Nārāyaṇa, Mādhava, Govinda, Viṣṇu, Madhusūdana, Trivikrama, Vāmana, "
       "Śrīdhara, Hṛṣīkeśa, Padmanābha, Dāmodara, Saṅkarṣaṇa, Vāsudeva, "
       "Pradyumna, Aniruddha, Puruṣottama, Adhokṣaja, Nārasiṃha, Acyuta, "
       "Janārdana, Upendra, Hari, Kṛṣṇa — salutation to each."),
    _h("Daiva prārthanā · prayers to the gods"),
    _v(["yaśśivo nāmarūpābhyāṃ yā devī sarvamaṅgalā |",
        "tayossaṃsmaraṇātpuṃsāṃ sarvato jayamaṅgalam ||"],
       "Śiva, known by name and form, and the Goddess who is all-auspicious: by "
       "remembering the two, people gain victory and blessing on every side."),
    _v(["lābhasteṣāṃ jayasteṣāṃ kutasteṣāṃ parābhavaḥ |",
        "yeṣāmindīvaraśyāmo hṛdayastho janārdanaḥ ||"],
       "Theirs is gain, theirs is victory — how could they be overcome, in whose "
       "hearts dwells Janārdana, dark as the blue lotus?"),
    _v(["āpadāmapahartāraṃ dātāraṃ sarvasampadām |",
        "lokābhirāmaṃ śrīrāmaṃ bhūyo bhūyo namāmyaham ||"],
       "Again and again I bow to Śrī Rāma, remover of calamities, giver of all "
       "riches, the delight of the world."),
    _v(["sarvamaṅgalamāṅgalye śive sarvārthasādhike |",
        "śaraṇye tryambake devi nārāyaṇi namo'stu te ||"],
       "O auspiciousness of all that is auspicious, gracious one, accomplisher of "
       "every aim, refuge, three-eyed Goddess Nārāyaṇī — salutation to you."),
    _p(["śrīlakṣmīnārāyaṇābhyāṃ namaḥ | umāmaheśvarābhyāṃ namaḥ |",
        "vāṇīhiraṇyagarbhābhyāṃ namaḥ | śacīpurandarābhyāṃ namaḥ |",
        "arundhatīvasiṣṭhābhyāṃ namaḥ | śrīsītārāmābhyāṃ namaḥ |",
        "sarvebhyo mahājanebhyo namaḥ | ayaṃ muhūrtassumuhūrto'stu ||"],
       "Salutation to Lakṣmī and Nārāyaṇa, to Umā and Maheśvara, to Vāṇī and "
       "Brahmā, to Śacī and Indra, to Arundhatī and Vasiṣṭha, to Sītā and Rāma, "
       "and to all the great ones. May this hour be an auspicious hour."),
    _r("Bhūtoccāṭanam — dispelling the spirits: sprinkle a few grains of akṣata "
       "behind you."),
    _v(["uttiṣṭhantu bhūtapiśācāḥ ete bhūmibhārakāḥ |",
        "eteṣāmavirodhena brahmakarma samārabhe ||"],
       "Let the spirits and goblins rise and go, these burdens of the earth; "
       "without hindrance from them I begin this sacred rite."),
    _r("Prāṇāyāma — restrain the breath while reciting:"),
    _p(["oṃ bhūḥ | oṃ bhuvaḥ | ogṃ suvaḥ | oṃ mahaḥ | oṃ janaḥ | oṃ tapaḥ | ogṃ satyam |",
        "oṃ tatsaviturvareṇyaṃ bhargo devasya dhīmahi | dhiyo yo naḥ pracodayāt ||",
        "oṃ āpo jyotī raso'mṛtaṃ brahma bhūrbhuvassuvarom ||"],
       "Oṃ — the seven worlds, from earth to the world of truth. We meditate on "
       "the adorable radiance of the divine Savitṛ; may he impel our minds. Oṃ — "
       "the waters, the light, the essence, the immortal, Brahman: earth, "
       "atmosphere, heaven, Oṃ."),
    _h("Saṅkalpam · the resolve"),
    _r("Holding akṣata and water, fill in the year, season, month, fortnight, "
       "tithi and weekday where the dots stand, and your gotra and name."),
    _p(["mamopāttaduritakṣayadvārā śrīparameśvaraprītyarthaṃ",
        "śubhe śobhane muhūrte śrīmahāviṣṇorājñayā pravartamānasya",
        "adya brahmaṇaḥ dvitīyaparārdhe śvetavarāhakalpe vaivasvatamanvantare",
        "kaliyuge prathamapāde jambūdvīpe bharatavarṣe bharatakhaṇḍe",
        "asmin vartamāne vyāvahārike cāndramānena … saṃvatsare … ayane",
        "… māse … pakṣe … tithau … vāsare śubhanakṣatre śubhayoge śubhakaraṇe",
        "evaṃ guṇaviśeṣaṇaviśiṣṭāyāṃ śubhatithau",
        "śrīmān … gotraḥ … nāmadheyaḥ dharmapatnīsameto'haṃ",
        "śrīmataḥ … gotrasya … nāmadheyasya dharmapatnīsametasya mama sakuṭumbasya",
        "kṣemasthairyavijayābhayāyurārogyaiśvaryābhivṛddhyarthaṃ",
        "dharmārthakāmamokṣacaturvidhapuruṣaphalāvāptyarthaṃ",
        "cintitamanorathasiddhyarthaṃ śrīsatyanārāyaṇamuddiśya",
        "śrīsatyanārāyaṇaprītyarthaṃ puruṣasūktavidhānena",
        "dhyānāvāhanādiṣoḍaśopacārapūjāṃ kariṣye |",
        "ādau nirvighnaparisamāptyarthaṃ gaṇādhipatipūjāṃ kariṣye |",
        "tadaṅgakalaśārādhanaṃ kariṣye ||"],
       "For the removal of the sins I have gathered and for the pleasure of the "
       "Supreme Lord — at this bright and auspicious hour, in the age set going "
       "by the command of Mahāviṣṇu, in the second half of Brahmā's life, in the "
       "Śvetavarāha kalpa, the manvantara of Vaivasvata, the first quarter of "
       "the Kali age, in Jambūdvīpa, in the land of Bharata; in the present "
       "year, half-year, month, fortnight, lunar day and weekday so "
       "named, under an auspicious star, yoga and karaṇa — I, of such a gotra "
       "and name, with my wife, for the safety, steadiness, victory, "
       "fearlessness, long life, health and increasing prosperity of myself and "
       "my family, for the four ends of life — dharma, wealth, desire and "
       "liberation — and for the fulfilment of the wishes I hold, will perform "
       "the sixteen-fold worship of Śrī Satyanārāyaṇa, from meditation and "
       "invocation onward, in the manner of the Puruṣa Sūkta, for his pleasure. "
       "First, that it may be completed without obstacle, I will worship "
       "Gaṇapati; and as part of it, worship the sacred vessel."),
    _h("Kalaśārādhanam · worship of the vessel"),
    _v(["kalaśasya mukhe viṣṇuḥ kaṇṭhe rudrassamāśritaḥ |",
        "mūle tatra sthito brahmā madhye mātṛgaṇāśritāḥ ||",
        "kukṣau tu sāgarāssarve saptadvīpā vasundharā |",
        "ṛgvedo'tha yajurvedassāmavedo hyatharvaṇaḥ |",
        "aṅgaiśca sahitāssarve kalaśaṃ tu samāśritāḥ ||"],
       "At the mouth of the vessel dwells Viṣṇu, at its neck Rudra, at its base "
       "Brahmā, and in its middle the hosts of Mothers. In its belly are all the "
       "oceans and the earth with its seven continents; the Ṛg, Yajus, Sāma and "
       "Atharva Vedas with their limbs have all taken refuge in the vessel."),
    _r("Put sandal-paste, flowers and akṣata into the vessel and cover its "
       "mouth with the right hand."),
    _p(["āpo vā idagṃ sarvaṃ viśvā bhūtānyāpaḥ prāṇā vā āpaḥ paśava",
        "āpo'nnamāpo'mṛtamāpassamrāḍāpo virāḍāpassvarāḍāpaśchandāgṃsyāpo",
        "jyotīgṃṣyāpo yajūgṃṣyāpassatyamāpassarvā devatā āpo bhūrbhuvassuvarāpa om ||"],
       "The waters are all this. All beings are the waters; the waters are the "
       "breaths, the cattle, food, the immortal; the waters are sovereign, "
       "far-ruling, self-ruling; the metres, the lights, the sacrificial "
       "formulae, the truth, all the gods are the waters. Earth, atmosphere, "
       "heaven — the waters. Oṃ."),
    _v(["gaṅge ca yamune caiva godāvari sarasvati |",
        "narmade sindhu kāveri jale'smin sannidhiṃ kuru ||",
        "āyāntu śrīsatyanārāyaṇapūjārthaṃ duritakṣayakārakāḥ ||"],
       "O Gaṅgā, Yamunā, Godāvarī, Sarasvatī, Narmadā, Sindhu and Kāverī, be "
       "present in this water. May they come, destroyers of sin, for the "
       "worship of Śrī Satyanārāyaṇa."),
    _r("Kalaśodakena devam ātmānaṃ pūjādravyāṇi ca samprokṣya — with water from "
       "the vessel, sprinkle the deity, yourself and the articles of worship."),
]

# ───────────────────────── Gaṇapati pūjā ─────────────────────────
GN = "śrīmahāgaṇādhipataye namaḥ"
S += [
    "ornament",
    _h("Gaṇapati Pūjā"),
    _v(["gaṇānāṃ tvā gaṇapatigṃ havāmahe kaviṃ kavīnāmupamaśravastamam |",
        "jyeṣṭharājaṃ brahmaṇāṃ brahmaṇaspata ā naśśṛṇvannūtibhissīda sādanam ||"],
       "We call on you, lord of the hosts, poet among poets, of highest renown, "
       "eldest king of prayers, Brahmaṇaspati: hearing us, come with your help "
       "and sit in your seat."),
    _p([f"{GN} | dhyāyāmi | āvāhayāmi | ratnasiṃhāsanaṃ samarpayāmi |",
        "pādayoḥ pādyaṃ samarpayāmi | hastayorarghyaṃ samarpayāmi |",
        "mukhe ācamanīyaṃ samarpayāmi ||"],
       "Salutation to the great lord of the hosts: I meditate on you, invoke you, "
       "offer a jewelled throne, water for the feet, water for the hands, and "
       "water to sip."),
    _v(["āpo hi ṣṭhā mayobhuvastā na ūrje dadhātana mahe raṇāya cakṣase |",
        "yo vaśśivatamo rasastasya bhājayateha naḥ uśatīriva mātaraḥ |",
        "tasmā araṃ gamāma vo yasya kṣayāya jinvatha āpo janayathā ca naḥ ||",
        f"{GN} snapayāmi | snānānantaraṃ śuddhācamanīyaṃ samarpayāmi ||"],
       "O waters, you are the source of well-being: set us in strength, to see "
       "great joy. Your most blessed essence — let us share in it here, like "
       "loving mothers. To you we come gladly, for whose dwelling you quicken "
       "us; waters, give us birth. — I bathe him; after the bath I offer pure "
       "water to sip."),
    _v(["abhi vastrā suvasanānyarṣābhi dhenūssudughāḥ pūyamānaḥ |",
        "abhi candrā bhartave no hiraṇyābhyaśvānrathino deva soma ||",
        f"{GN} vastrayugmaṃ samarpayāmi ||"],
       "Flowing clear, O god Soma, bring us garments, fine clothing, and cows "
       "that yield milk readily; bring us shining gold to keep, and horses with "
       "chariots. — I offer a pair of garments."),
    _v(["yajñopavītaṃ paramaṃ pavitraṃ prajāpateryatsahajaṃ purastāt |",
        "āyuṣyamagryaṃ pratimuñca śubhraṃ yajñopavītaṃ balamastu tejaḥ ||",
        f"{GN} yajñopavītaṃ samarpayāmi ||"],
       "The sacred thread, supremely pure, born of old together with "
       "Prajāpati — put on this bright thread, foremost giver of long life; may "
       "it be strength and splendour. — I offer the sacred thread."),
    _v(["gandhadvārāṃ durādharṣāṃ nityapuṣṭāṃ karīṣiṇīm |",
        "īśvarīgṃ sarvabhūtānāṃ tāmihopahvaye śriyam ||",
        f"{GN} divyaśrīcandanaṃ samarpayāmi ||"],
       "Her whose door is fragrance, unassailable, ever-nourishing, rich in "
       "harvest, sovereign over all beings — Śrī I call here. — I offer divine "
       "sandal."),
    _v(["āyane te parāyaṇe dūrvā rohantu puṣpiṇīḥ |",
        "hradāśca puṇḍarīkāṇi samudrasya gṛhā ime ||",
        f"{GN} dūrvādinānāvidhapuṣpāṇi pūjayāmi ||"],
       "Where you come and where you go, may flowering dūrvā grow, and ponds "
       "with lotuses: these are the ocean's homes. — I worship with dūrvā and "
       "many flowers."),
    _names(["sumukhāya", "ekadantāya", "kapilāya", "gajakarṇakāya", "lambodarāya",
            "vikaṭāya", "vighnarājāya", "gaṇādhipāya", "dhūmaketave",
            "gaṇādhyakṣāya", "phālacandrāya", "gajānanāya", "vakratuṇḍāya",
            "śūrpakarṇāya", "herambāya", "skandapūrvajāya",
            "sarvasiddhipradāyakāya", "śrīmahāgaṇādhipataye"],
           "Ṣoḍaśa-nāma pūjā — the sixteen names: the fair-faced, the one-tusked, "
           "the tawny, the elephant-eared, the pot-bellied, the formidable, king "
           "of obstacles, lord of the hosts, the smoke-bannered, chief of the "
           "hosts, moon-browed, elephant-faced, curved-trunked, winnow-eared, "
           "Heramba, elder brother of Skanda; giver of every success; the great "
           "lord of the hosts. — Then: many fragrant flowers are offered."),
    _v(["vanaspatyudbhavairdivyairnānāgandhaissusaṃyutaḥ |",
        "āghreyassarvadevānāṃ dhūpo'yaṃ pratigṛhyatām ||",
        f"{GN} dhūpamāghrāpayāmi ||"],
       "Made of heavenly things sprung from the trees, rich with many scents, "
       "fit to be smelled by all the gods — accept this incense. — I offer "
       "incense."),
    _v(["sājyaṃ trivartisaṃyuktaṃ vahninā yojitaṃ priyam |",
        "gṛhāṇa maṅgalaṃ dīpaṃ trailokyatimirāpaham ||",
        "bhaktyā dīpaṃ prayacchāmi devāya paramātmane |",
        "trāhi māṃ narakādghorāddivyajyotirnamo'stu te ||",
        f"{GN} dīpaṃ darśayāmi | dhūpadīpānantaram ācamanīyaṃ samarpayāmi ||"],
       "With ghee and a triple wick, lit with fire, dear to you — accept this "
       "auspicious lamp that drives away the darkness of the three worlds. With "
       "devotion I offer the lamp to the god, the supreme Self: save me from "
       "dreadful hell; salutation to you, divine light. — I show the lamp; after "
       "incense and lamp, I offer water to sip."),
    _r("Naivedya: place a piece of jaggery before him and sprinkle water around "
       "it while reciting. (At night say ṛtaṃ tvā satyena pariṣiñcāmi instead.)"),
    _p(["oṃ bhūrbhuvassuvaḥ | oṃ tatsaviturvareṇyaṃ bhargo devasya dhīmahi | dhiyo yo naḥ pracodayāt ||",
        "satyaṃ tvartena pariṣiñcāmi |",
        f"{GN} guḍopahāranaivedyaṃ samarpayāmi |",
        "amṛtamastu | amṛtopastaraṇamasi |",
        "oṃ prāṇāya svāhā | oṃ apānāya svāhā | oṃ vyānāya svāhā |",
        "oṃ udānāya svāhā | oṃ samānāya svāhā |",
        "madhye madhye pānīyaṃ samarpayāmi | amṛtāpidhānamasi | uttarāpośanaṃ samarpayāmi |",
        "hastau prakṣālayāmi | pādau prakṣālayāmi | śuddhācamanīyaṃ samarpayāmi ||"],
       "After the Gāyatrī: I sprinkle you, truth, with order. I offer an "
       "offering of jaggery. May it be nectar; you are the nectar-spread "
       "beneath. Hail to the five vital breaths. I offer water to drink between "
       "mouthfuls; you are the nectar-covering; I offer the closing sip; I wash "
       "the hands and feet, and offer pure water to sip."),
    _v(["pūgīphalaissakarpūrairnāgavallīdalairyutam |",
        "muktācūrṇena saṃyuktaṃ tāmbūlaṃ pratigṛhyatām ||",
        f"{GN} tāmbūlaṃ samarpayāmi ||"],
       "Accept this betel — areca nut with camphor, betel leaves, and lime of "
       "pearl. — I offer betel."),
    _v(["gaṇānāṃ tvā gaṇapatigṃ havāmahe kaviṃ kavīnāmupamaśravastamam |",
        "jyeṣṭharājaṃ brahmaṇāṃ brahmaṇaspata ā naśśṛṇvannūtibhissīda sādanam ||",
        f"{GN} suvarṇamantrapuṣpaṃ samarpayāmi ||"],
       "We call on you, lord of the hosts … sit in your seat. — I offer the "
       "golden flower of mantra."),
    _v(["mantrahīnaṃ kriyāhīnaṃ bhaktihīnaṃ gaṇādhipa |",
        "yatpūjitaṃ mayā deva paripūrṇaṃ tadastu te ||"],
       "Lacking in mantra, lacking in rite, lacking in devotion — whatever "
       "worship I have done, O lord of the hosts, may it be made complete for "
       "you."),
    _p(["anayā dhyānāvāhanādiṣoḍaśopacārapūjayā ca bhagavān sarvātmakaḥ",
        "śrīmahāgaṇādhipatissuprīto varado bhūtvā",
        "uttare karmaṇyavighnamastviti bhavanto bruvantu |",
        "uttare karmaṇyavighnamastu |",
        "gaṇādhipatiprasādaṃ śirasā gṛhṇāmi ||"],
       "By this sixteen-fold worship may the Lord, the Self of all, the great "
       "lord of the hosts, be well pleased and grant boons. — Let the assembly "
       "say: may the rite that follows be free of obstacles. (They answer:) May "
       "it be free of obstacles. I receive Gaṇapati's grace upon my head."),
    _v(["sahasraparamā devī śatamūlā śatāṅkurā |",
        "sarvagṃ haratu me pāpaṃ dūrvā duḥsvapnanāśanī ||",
        "gaṇapatiṃ yathāsthānamudvāsayāmi ||"],
       "The goddess Dūrvā, of a thousand shoots, a hundred roots and a hundred "
       "sprouts, destroyer of evil dreams — may she take away all my sin. I "
       "bid Gaṇapati return to his place."),
    _v(["yajñena yajñamayajanta devāstāni dharmāṇi prathamānyāsan |",
        "te ha nākaṃ mahimānassacante yatra pūrve sādhyāssanti devāḥ ||"],
       "With sacrifice the gods worshipped the Sacrifice; these were the first "
       "ordinances. Those great ones reached the vault of heaven, where the "
       "ancient Sādhyas, the gods, abide."),
]

# ───────────────────────── the five lokapālas ─────────────────────────
LP = "sāṅgaṃ sāyudhaṃ savāhanaṃ saśaktiṃ patnīputraparivārasametaṃ"
S += [
    "ornament",
    _h("Pañcalokapāla Pūjā · the five world-guardians"),
    _p(["ācamya | pūrvokta evaṃguṇaviśeṣaṇaviśiṣṭāyāṃ śubhatithau",
        "śrīsatyanārāyaṇavratāṅgagaṇapatyādipañcalokapālakapūjāṃ",
        "ādityādinavagrahapūjām indrādyaṣṭadikpālakapūjāṃ ca kariṣye ||"],
       "Having sipped water: on this auspicious day of the qualities named "
       "before, as limbs of the Satyanārāyaṇa vrata I will worship the five "
       "world-guardians beginning with Gaṇapati, the nine planets beginning "
       "with the Sun, and the eight guardians of the quarters beginning with "
       "Indra."),
    _v(["oṃ gaṇānāṃ tvā gaṇapatigṃ havāmahe kaviṃ kavīnāmupamaśravastamam |",
        "jyeṣṭharājaṃ brahmaṇāṃ brahmaṇaspata ā naśśṛṇvannūtibhissīda sādanam ||",
        f"{LP} gaṇapatiṃ lokapālakamāvāhayāmi sthāpayāmi pūjayāmi ||"],
       "1. Gaṇapati: “We call on you, lord of the hosts …” — with his limbs, "
       "weapons, mount and power, with consort, sons and retinue, I invoke, "
       "install and worship Gaṇapati as world-guardian."),
    _v(["oṃ brahmā devānāṃ padavīḥ kavīnāmṛṣirviprāṇāṃ mahiṣo mṛgāṇām |",
        "śyeno gṛdhrāṇāgṃ svadhitirvanānāgṃ somaḥ pavitramatyeti rebhan ||",
        f"{LP} brahmāṇaṃ lokapālakamāvāhayāmi sthāpayāmi pūjayāmi ||"],
       "2. Brahmā: “Brahmā among the gods, leader among poets, seer among "
       "sages, buffalo among beasts, falcon among birds of prey, axe among the "
       "trees — Soma passes through the filter, singing.” I invoke, install "
       "and worship Brahmā as world-guardian."),
    _v(["oṃ idaṃ viṣṇurvicakrame tredhā nidadhe padam |",
        "samūḍhamasya pāgṃsure ||",
        f"{LP} viṣṇuṃ lokapālakamāvāhayāmi sthāpayāmi pūjayāmi ||"],
       "3. Viṣṇu: “Viṣṇu strode over this; three times he set down his foot; "
       "all is gathered in his dusty footprint.” I invoke, install and worship "
       "Viṣṇu as world-guardian."),
    _v(["kadrudrāya pracetase mīḍhuṣṭamāya tavyase |",
        "vocema śantamagṃ hṛde ||",
        f"{LP} rudraṃ lokapālakamāvāhayāmi sthāpayāmi pūjayāmi ||"],
       "4. Rudra: “What shall we say to Rudra, the wise, most bountiful, most "
       "mighty, that is dearest to his heart?” I invoke, install and worship "
       "Rudra as world-guardian."),
    _v(["oṃ gaurīrmimāya salilāni takṣatyekapadī dvipadī sā catuṣpadī |",
        "aṣṭāpadī navapadī babhūvuṣī sahasrākṣarā parame vyoman ||",
        "sāṅgāṃ sāyudhāṃ savāhanāṃ saśaktiṃ patiputraparivārasametāṃ",
        "gaurīṃ lokapālikāmāvāhayāmi sthāpayāmi pūjayāmi ||"],
       "5. Gaurī: “The buffalo-cow lowed, fashioning the floods — one-footed, "
       "two-footed, four-footed, eight-footed, nine-footed, of a thousand "
       "syllables in the highest heaven.” I invoke, install and worship Gaurī "
       "as world-guardian, with her consort, sons and retinue."),
    _p(["gaṇeśādipañcalokapālakadevatābhyo namaḥ |",
        "dhyāyāmi āvāhayāmi ratnasiṃhāsanaṃ samarpayāmi pādyaṃ samarpayāmi",
        "arghyaṃ samarpayāmi ācamanīyaṃ samarpayāmi snānaṃ samarpayāmi",
        "śuddhācamanīyaṃ samarpayāmi vastraṃ samarpayāmi yajñopavītaṃ samarpayāmi",
        "gandhaṃ samarpayāmi akṣatān samarpayāmi puṣpāṇi samarpayāmi",
        "dhūpamāghrāpayāmi dīpaṃ darśayāmi naivedyaṃ samarpayāmi",
        "tāmbūlaṃ samarpayāmi mantrapuṣpaṃ samarpayāmi ||",
        "gaṇeśādipañcalokapālakadevatāprasādasiddhirastu ||"],
       "Salutation to the five world-guardians led by Gaṇeśa: meditation, "
       "invocation, throne, water for feet and hands, water to sip, bath, pure "
       "water, garment, sacred thread, sandal, akṣata, flowers, incense, lamp, "
       "food, betel and the flower of mantra are offered. May the grace of the "
       "five world-guardians be gained."),
]

# ───────────────────────── the nine planets ─────────────────────────
AVA = "māvāhayāmi sthāpayāmi pūjayāmi ||"
S += [
    "ornament",
    _h("Navagraha Pūjā · the nine planets"),
    _r("The planets are set out around the Sun, who stands near the vessel on "
       "its west side: the Moon to the south-east, Mars south, Mercury "
       "north-east, Jupiter north, Venus east, Saturn west, Rāhu south-west and "
       "Ketu north-west. Each is invoked with his presiding deity "
       "(adhidevatā) on his right and his counter-deity (pratyadhidevatā) on "
       "his left."),

    # 1 Sūrya
    _h("1 · Sūrya"),
    _v(["sūryāriṣṭe tu samprāpte sūryapūjāṃ ca kārayet |",
        "sūryadhyānaṃ pravakṣyāmi ātmapīḍopaśāntaye ||"],
       "When affliction from the Sun befalls, let the Sun be worshipped. I will "
       "tell the meditation on the Sun, to quiet suffering of the self."),
    _p(["ā satyenetyasya mantrasya hiraṇyastūpa ṛṣiḥ | savitā devatā | triṣṭup chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitasūryagrahaprasādasiddhyarthe",
        "sūryagrahārādhane viniyogaḥ ||"],
       "Of the mantra “ā satyena” the seer is Hiraṇyastūpa, the deity Savitṛ, "
       "the metre triṣṭubh; it is applied in the worship of the Sun, with his "
       "adhidevatā and pratyadhidevatā, to win his grace for the sacrificer."),
    _v(["vedīmadhye lalitakamale karṇikāyāṃ rathasthaḥ",
        "saptāśvo'rko'ruṇarucivapuḥ saptarajjurdvibāhuḥ |",
        "gotre ramye bahuvidhaguṇe kāśyapākhye prasūtaḥ",
        "kāliṅgākhye viṣayajanitaḥ prāṅmukhaḥ padmahastaḥ ||",
        "padmāsanaḥ padmakaro dvibāhuḥ padmadyutissaptaturaṅgavāhaḥ |",
        "divākaro lokaguruḥ kirīṭī mayi prasādaṃ vidadhātu devaḥ ||"],
       "Dhyāna: in the middle of the altar, on the pericarp of a lovely lotus, "
       "stands the Sun in his chariot — seven horses, seven reins, two arms, "
       "body the red of dawn; born in the noble Kāśyapa line, sprung from the "
       "land of Kaliṅga, facing east, lotus in hand. Seated on a lotus, lotus "
       "in his hands, lotus-bright, drawn by seven steeds — may the Day-maker, "
       "teacher of the world, crowned, show me his grace."),
    _v(["ā satyena rajasā vartamāno niveśayannamṛtaṃ martyaṃ ca |",
        "hiraṇyayena savitā rathenā devo yāti bhuvanā vipaśyan ||",
        "oṃ bhūrbhuvassuvaḥ sūryagrahehāgaccha ||"],
       "Moving through the realm of space by truth, laying to rest the immortal "
       "and the mortal, god Savitṛ comes in his golden chariot, beholding the "
       "worlds. — Come here, Sun."),
    _p(["sūryagrahaṃ raktavarṇaṃ raktagandhaṃ raktapuṣpaṃ raktamālyāmbaradharaṃ",
        "raktacchatradhvajarathapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ prāṅmukhaṃ padmāsanasthaṃ dvibhujaṃ",
        "saptāśvaṃ saptarajjuṃ kaliṅgadeśādhipatiṃ kāśyapasagotraṃ",
        "prabhavasaṃvatsare māghamāse śuklapakṣe saptamyāṃ bhānuvāsare",
        "aśvinīnakṣatrajātaṃ siṃharāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "madhye vartulākāramaṇḍale sthāpitasvarṇapratimārūpeṇa",
        f"sūryagraha{AVA}"],
       "The Sun — red of colour, with red sandal, red flowers, red garland and "
       "garments, adorned with red parasol, banner and pennant, mounted on his "
       "divine chariot, circling Meru sunwise, facing east, seated on a lotus, "
       "two-armed, with seven horses and seven reins, lord of Kaliṅga, of the "
       "Kāśyapa gotra, born in the year Prabhava, in Māgha, the bright "
       "fortnight, the seventh tithi, a Sunday, under Aśvinī, lord of Leo, "
       "crowned, seated at ease, with consort, sons and retinue — I invoke, "
       "install and worship in the golden image set in the circular maṇḍala "
       "at the centre of the planetary diagram."),
    _v(["oṃ agniṃ dūtaṃ vṛṇīmahe hotāraṃ viśvavedasam |",
        "asya yajñasya sukratum ||",
        f"sūryagrahādhidevatām agniṃ {LP}",
        f"sūryagrahasya dakṣiṇataḥ agni{AVA}"],
       "“We choose Agni as messenger, the invoker, knower of all, most skilful "
       "in this sacrifice.” Agni, presiding deity of the Sun, is invoked on the "
       "Sun's right."),
    _v(["oṃ kadrudrāya pracetase mīḍhuṣṭamāya tavyase |",
        "vocema śantamagṃ hṛde ||",
        f"sūryagrahapratyadhidevatāṃ rudraṃ {LP}",
        f"sūryagrahasya uttarataḥ rudra{AVA}"],
       "“What shall we say to Rudra … dearest to his heart?” Rudra, "
       "counter-deity of the Sun, is invoked on the Sun's left."),

    # 2 Candra
    _h("2 · Candra"),
    _v(["candrāriṣṭe tu samprāpte candrapūjāṃ ca kārayet |",
        "candradhyānaṃ pravakṣyāmi manaḥpīḍopaśāntaye ||"],
       "When affliction from the Moon befalls, let the Moon be worshipped. I "
       "will tell the meditation on the Moon, to quiet suffering of the mind."),
    _p(["āpyāyasvetyasya mantrasya gautama ṛṣiḥ | candro devatā | gāyatrī chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitacandragrahaprasādasiddhyarthe",
        "candragrahārādhane viniyogaḥ ||"],
       "Of the mantra “āpyāyasva” the seer is Gautama, the deity the Moon, the "
       "metre gāyatrī; it is applied in the worship of the Moon."),
    _v(["āgneyabhāge saratho daśāśvaścātreyajo yāmunadeśajaśca |",
        "pratyaṅmukhasthaścaturaśrapīṭhe gadādharāṅgo himavatsvabhāvaḥ ||",
        "śvetāmbaraśśvetavapuḥ kirīṭī śvetadyutirdaṇḍadharo dvibāhuḥ |",
        "candro'mṛtātmā varadaḥ kirīṭī śreyāṃsi mahyaṃ vidadhātu devaḥ ||"],
       "Dhyāna: in the south-east, in his chariot of ten horses, born of Atri's "
       "line in the land of the Yamunā, facing west on a square seat, bearing a "
       "mace, cool as the snows. White-robed, white of body, crowned, "
       "white-shining, staff in hand, two-armed — may the Moon, whose self is "
       "nectar, giver of boons, bestow blessings on me."),
    _v(["oṃ āpyāyasva sametu te viśvatassoma vṛṣṇiyam |",
        "bhavā vājasya saṅgathe ||",
        "oṃ bhūrbhuvassuvaḥ candragrahehāgaccha ||"],
       "“Swell, O Soma; let manly vigour gather to you from every side; be "
       "present where strength is won.” — Come here, Moon."),
    _p(["candragrahaṃ śvetavarṇaṃ śvetagandhaṃ śvetapuṣpaṃ śvetamālyāmbaradharaṃ",
        "śvetacchatradhvajapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ daśāśvarathavāhanaṃ pratyaṅmukhaṃ",
        "dvibhujaṃ daṇḍadharaṃ yāmunadeśādhipatim ātreyasagotraṃ",
        "saumyasaṃvatsare kārtikamāse śuklapakṣe paurṇamāsyām induvāsare",
        "kṛttikānakṣatrajātaṃ karkaṭarāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "sūryagrahasyāgneyadigbhāge samacaturaśramaṇḍale",
        f"sthāpitarajatapratimārūpeṇa candragraha{AVA}"],
       "The Moon — white, with white sandal, flowers, garland and garments, "
       "white parasol and banner, in his divine ten-horsed chariot circling "
       "Meru, facing west, two-armed, holding a staff, lord of the Yamunā "
       "country, of Atri's gotra, born in the year Saumya, in Kārttika, on the "
       "full moon, a Monday, under Kṛttikā, lord of Cancer — I invoke in the "
       "silver image set in the square maṇḍala south-east of the Sun."),
    _v(["oṃ apsu me somo abravīdantarviśvāni bheṣajā |",
        "agniṃ ca viśvaśambhuvamāpaśca viśvabheṣajīḥ ||",
        "candragrahādhidevatāḥ sāṅgāḥ sāyudhāḥ savāhanāḥ saśaktīḥ putraparivārasametāḥ",
        "candragrahasya dakṣiṇataḥ apaḥ āvāhayāmi sthāpayāmi pūjayāmi ||"],
       "“Soma told me that within the waters are all remedies, and Agni who "
       "blesses all, and the waters that heal all.” The Waters, presiding "
       "deities of the Moon, are invoked on his right."),
    _v(["oṃ gaurīrmimāya salilāni takṣatyekapadī dvipadī sā catuṣpadī |",
        "aṣṭāpadī navapadī babhūvuṣī sahasrākṣarā parame vyoman ||",
        "candragrahapratyadhidevatāṃ gaurīṃ sāṅgāṃ sāyudhāṃ savāhanāṃ saśaktiṃ",
        f"putraparivārasametāṃ candragrahasyottarataḥ gaurī{AVA}"],
       "“The buffalo-cow lowed …” Gaurī, counter-deity of the Moon, is invoked "
       "on his left."),

    # 3 Aṅgāraka
    _h("3 · Aṅgāraka (Kuja)"),
    _v(["kujāriṣṭe tu samprāpte kujapūjāṃ ca kārayet |",
        "kujadhyānaṃ pravakṣyāmi rogapīḍopaśāntaye ||"],
       "When affliction from Mars befalls, let Mars be worshipped. I will tell "
       "the meditation on Mars, to quiet the suffering of disease."),
    _p(["agnirmūrdhetyasya mantrasya virūpa ṛṣiḥ | aṅgārakagraho devatā | triṣṭup chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitāṅgārakagrahaprasādasiddhyarthe",
        "aṅgārakagrahārādhane viniyogaḥ ||"],
       "Of the mantra “agnirmūrdhā” the seer is Virūpa, the deity Mars; it is "
       "applied in the worship of Mars."),
    _v(["yāmye gadāśaktidharaśca śūlī varaprado yāmyamukho'tiriktaḥ |",
        "kujastvavantīviṣayastrikoṇastasminbharadvājakule prasūtaḥ ||",
        "raktāmbaro raktavapuḥ kirīṭī caturbhujo meṣagamo gadābhṛt |",
        "dharāsutaśśaktidharaśca śūlī sadā mama syādvaradaḥ praśāntaḥ ||"],
       "Dhyāna: in the south, bearing mace, spear and trident, giver of boons, "
       "facing south, fierce; Mars, of the Avantī country, on a triangular "
       "seat, born in Bharadvāja's line. Red-robed, red of body, crowned, "
       "four-armed, riding a ram, mace-bearing — may the son of the Earth, "
       "holding spear and trident, be ever gracious and calm toward me."),
    _v(["oṃ agnirmūrdhā divaḥ kakutpatiḥ pṛthivyā ayam |",
        "apāgṃ retāgṃsi jinvati ||",
        "oṃ bhūrbhuvassuvaḥ aṅgārakagrahehāgaccha ||"],
       "“Agni is the head, the summit of heaven, this lord of the earth; he "
       "quickens the seed of the waters.” — Come here, Mars."),
    _p(["aṅgārakagrahaṃ raktavarṇaṃ raktagandhaṃ raktapuṣpaṃ raktamālyāmbaradharaṃ",
        "raktacchatradhvajapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ meṣavāhanaṃ dakṣiṇābhimukhaṃ caturbhujaṃ",
        "gadāśūlaśaktidharam avantīdeśādhipatiṃ bhāradvājasagotraṃ",
        "rākṣasanāmasaṃvatsare āṣāḍhamāse śuklapakṣe daśamyāṃ bhaumavāsare",
        "anūrādhānakṣatrajātaṃ meṣavṛścikarāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "sūryagrahasya dakṣiṇadigbhāge trikoṇākāramaṇḍale",
        f"sthāpitatāmrapratimārūpeṇa aṅgārakagraha{AVA}"],
       "Mars — red, with red sandal, flowers, garland and garments, riding a "
       "ram, facing south, four-armed, bearing mace, trident and spear, lord of "
       "Avantī, of Bharadvāja's gotra, born in the year Rākṣasa, in Āṣāḍha, the "
       "bright tenth, a Tuesday, under Anurādhā, lord of Aries and Scorpio — I "
       "invoke in the copper image set in the triangular maṇḍala south of the "
       "Sun."),
    _v(["oṃ syonā pṛthivi bhavānṛkṣarā niveśanī |",
        "yacchā naśśarma saprathāḥ ||",
        "aṅgārakagrahādhidevatāṃ pṛthivīṃ sāṅgāṃ sāyudhāṃ savāhanāṃ saśaktiṃ",
        f"putraparivārasametām aṅgārakagrahasya dakṣiṇataḥ pṛthivī{AVA}"],
       "“Be kindly, Earth, thornless, a resting-place; grant us wide shelter.” "
       "Earth, presiding deity of Mars, is invoked on his right."),
    _v(["oṃ kṣetrasya patinā vayagṃ hiteneva jayāmasi |",
        "gāmaśvaṃ poṣayitnvā sa no mṛḍātīdṛśe ||",
        f"aṅgārakagrahapratyadhidevatāṃ kṣetrapālakaṃ {LP}",
        f"aṅgārakagrahasyottarataḥ kṣetrapālaka{AVA}"],
       "“With the Lord of the Field, as with a friend, we win cows and horses "
       "and all that nourishes; may he be gracious to us in such things.” The "
       "Guardian of the Field, counter-deity of Mars, is invoked on his left."),

    # 4 Budha
    _h("4 · Budha"),
    _v(["budhāriṣṭe tu samprāpte budhapūjāṃ ca kārayet |",
        "budhadhyānaṃ pravakṣyāmi buddhipīḍopaśāntaye ||"],
       "When affliction from Mercury befalls, let Mercury be worshipped. I will "
       "tell the meditation on Mercury, to quiet troubles of the intellect."),
    _p(["udbudhyasvetyasya mantrasya praskaṇva ṛṣiḥ | budhagraho devatā | triṣṭup chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitabudhagrahaprasādasiddhyarthe",
        "budhagrahārādhane viniyogaḥ ||"],
       "Of the mantra “udbudhyasva” the seer is Praskaṇva, the deity Mercury, "
       "the metre triṣṭubh; it is applied in the worship of Mercury."),
    _v(["udaṅmukho māgadhajo haristhaścātreyagotraśśaramaṇḍalasthaḥ |",
        "sakhaḍgacarmorugadādharo jñastvīśānabhāge varadassupītaḥ ||",
        "pītāmbaraḥ pītavapuḥ kirīṭī caturbhujo daṇḍadharaśca saumyaḥ |",
        "carmāsidhṛk somasutassumerussiṃhādhirūḍho varado budhaśca ||"],
       "Dhyāna: facing north, born in Magadha, riding a lion, of Atri's gotra, "
       "on an arrow-shaped maṇḍala, bearing sword, shield and great mace — "
       "Budha in the north-east, deep yellow, giver of boons. Yellow-robed, "
       "yellow of body, crowned, four-armed, staff in hand, gentle, bearing "
       "shield and sword, son of the Moon, riding a lion — may Budha grant "
       "boons."),
    _v(["oṃ udbudhyasvāgne pratijāgṛhyenamiṣṭāpūrte sagṃsṛjethāmayaṃ ca |",
        "punaḥ kṛṇvagṃstvā pitaraṃ yuvānamanvātāgṃsīttvayi tantumetam ||",
        "oṃ bhūrbhuvassuvaḥ budhagrahehāgaccha ||"],
       "“Awake, Agni, and watch over him; may you and he be joined in sacrifice "
       "and good works; making the father young again, he has spun this thread "
       "out through you.” — Come here, Mercury."),
    _p(["budhagrahaṃ pītavarṇaṃ pītagandhaṃ pītapuṣpaṃ pītamālyāmbaradharaṃ",
        "pītacchatradhvajarathapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ siṃhavāhanam udaṅmukhaṃ magadhadeśādhipatiṃ",
        "caturbhujaṃ khaḍgacarmāmbaradharam ātreyasagotram",
        "āṅgīrasanāmasaṃvatsare mārgaśīrṣamāse śuklapakṣe saptamyāṃ saumyavāsare",
        "pūrvābhādrānakṣatrajātaṃ mithunakanyārāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "sūryagrahasya īśānyadigbhāge bāṇākāramaṇḍale",
        f"sthāpitakāṃsyapratimārūpeṇa budhagraha{AVA}"],
       "Mercury — yellow, with yellow sandal, flowers, garland and garments, "
       "riding a lion, facing north, lord of Magadha, four-armed, with sword "
       "and shield, of Atri's gotra, born in the year Āṅgīrasa, in "
       "Mārgaśīrṣa, the bright seventh, a Wednesday, under Pūrvābhādrā, lord of "
       "Gemini and Virgo — I invoke in the bell-metal image set in the "
       "arrow-shaped maṇḍala north-east of the Sun."),
    _v(["mahāviṣṇuṃ śaṅkhapadmasudarśanagadādharam |",
        "dhyāye'haṃ nīlagaurāṅgaṃ padmasthaṃ kamalāpatim ||",
        "oṃ idaṃ viṣṇurvicakrame tredhā nidadhe padam | samūḍhamasya pāgṃsure ||",
        f"budhagrahādhidevatāṃ viṣṇuṃ {LP}",
        f"budhagrahasya dakṣiṇataḥ viṣṇu{AVA}"],
       "I meditate on Mahāviṣṇu, bearing conch, lotus, the discus Sudarśana and "
       "mace, of blue and fair limbs, seated on a lotus, lord of Kamalā. "
       "“Viṣṇu strode over this …” Viṣṇu, presiding deity of Mercury, is "
       "invoked on his right."),
    _v(["pītapadmāsanāsīnaṃ caturbāhuṃ kirīṭinam |",
        "cintaye śaṅkhacakrābhyāṃ gadādhāriṇamacyutam ||",
        "oṃ sahasraśīrṣā puruṣaḥ sahasrākṣassahasrapāt |",
        "sa bhūmiṃ viśvato vṛtvā atyatiṣṭhaddaśāṅgulam ||",
        f"budhagrahapratyadhidevatāṃ nārāyaṇaṃ {LP}",
        f"budhagrahasyottarataḥ nārāyaṇa{AVA}"],
       "I contemplate Acyuta, seated on a yellow lotus, four-armed, crowned, "
       "holding conch, discus and mace. “The Puruṣa has a thousand heads, a "
       "thousand eyes, a thousand feet; enveloping the earth on every side, he "
       "stands beyond it by ten fingers.” Nārāyaṇa, counter-deity of Mercury, "
       "is invoked on his left."),

    # 5 Bṛhaspati
    _h("5 · Bṛhaspati (Guru)"),
    _v(["gurvariṣṭe tu samprāpte gurupūjāṃ ca kārayet |",
        "gurudhyānaṃ pravakṣyāmi putrapīḍopaśāntaye ||"],
       "When affliction from Jupiter befalls, let Jupiter be worshipped. I will "
       "tell the meditation on Jupiter, to quiet troubles concerning children."),
    _p(["bṛhaspate atiyadaryetyasya mantrasya gṛtsamada ṛṣiḥ |",
        "bṛhaspatigraho devatā | triṣṭup chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitabṛhaspatigrahaprasādasiddhyarthe",
        "bṛhaspatigrahārādhane viniyogaḥ ||"],
       "Of the mantra “bṛhaspate ati yadaryaḥ” the seer is Gṛtsamada, the deity "
       "Bṛhaspati, the metre triṣṭubh; it is applied in the worship of "
       "Jupiter."),
    _v(["saumye sudīrghe caturaśrapīṭhe rathe'ṅgirāḥ pūrvamukhasvabhāvaḥ |",
        "daṇḍākṣamālājalapātradhārī sindhvākhyadeśe varadassureśaḥ ||",
        "pītāmbaraḥ pītavapuḥ kirīṭī caturbhujo devaguruḥ praśāntaḥ |",
        "tathāsidaṇḍaṃ ca kamaṇḍaluṃ ca tathākṣasūtraṃ varado'stu mahyam ||"],
       "Dhyāna: in the north, on a long rectangular seat, in his chariot, "
       "Āṅgirasa by descent, facing east, bearing staff, rosary and water-pot, "
       "of the Sindhu country — the lord among gods, giver of boons. "
       "Yellow-robed, yellow of body, crowned, four-armed, the calm teacher of "
       "the gods, with sword and staff, water-pot and rosary — may he grant me "
       "boons."),
    _v(["oṃ bṛhaspate ati yadaryo arhāddyumadvibhāti kratumajjaneṣu |",
        "yaddīdayacchavasa ṛtaprajāta tadasmāsu draviṇaṃ dhehi citram ||",
        "oṃ bhūrbhuvassuvaḥ bṛhaspatigrahehāgaccha ||"],
       "“Bṛhaspati, the wealth that the noble one deserves, that shines "
       "brightly and with power among the peoples, that blazes with strength, "
       "O you born of truth — that wondrous wealth place in us.” — Come here, "
       "Jupiter."),
    _p(["bṛhaspatigrahaṃ pītavarṇaṃ pītagandhaṃ pītapuṣpaṃ pītamālyāmbaradharaṃ",
        "pītacchatradhvajapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ pūrvābhimukhaṃ padmāsanasthaṃ caturbhujaṃ",
        "daṇḍākṣamālādhāriṇaṃ sindhudvīpadeśādhipatim āṅgīrasagotram",
        "āṅgīrasanāmasaṃvatsare vaiśākhamāse śuklapakṣe ekādaśyāṃ guruvāsare",
        "uttarānakṣatrajātaṃ dhanurmīnarāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "sūryagrahasyottaradigbhāge dīrghacaturasramaṇḍale",
        f"sthāpitatrapupratimārūpeṇa bṛhaspatigraha{AVA}"],
       "Jupiter — yellow, with yellow sandal, flowers, garland and garments, "
       "facing east, seated on a lotus, four-armed, bearing staff and rosary, "
       "lord of the Sindhu country, of Aṅgiras's gotra, born in the year "
       "Āṅgīrasa, in Vaiśākha, the bright eleventh, a Thursday, under Uttarā, "
       "lord of Sagittarius and Pisces — I invoke in the tin image set in the "
       "rectangular maṇḍala north of the Sun."),
    _v(["brahmāṇaṃ raktagaurāṅgaṃ caturvaktraṃ jagatprabhum |",
        "akṣasrakkuṇḍikābhītivarapāṇiṃ vicintaye ||",
        "oṃ brahma jajñānaṃ prathamaṃ purastādvi sīmatassuruco vena āvaḥ |",
        "sa budhniyā upamā asya viṣṭhāssataśca yonimasataśca vivaḥ ||",
        f"bṛhaspatigrahādhidevatāṃ brahmāṇaṃ {LP}",
        f"bṛhaspatigrahasya dakṣiṇataḥ brahmāṇa{AVA}"],
       "I contemplate Brahmā, of red and fair limbs, four-faced, lord of the "
       "world, holding rosary and water-pot, his hands granting fearlessness and "
       "boons. “Brahman, first born in the east — Vena unveiled the shining "
       "ones from the horizon; he revealed the deepest forms of it, the womb of "
       "the existent and the non-existent.” Brahmā, presiding deity of Jupiter, "
       "is invoked on his right."),
    _v(["indramairāvatārūḍhaṃ vajrāyudhadharaṃ prabhum |",
        "pūrvadikpālakaṃ devaṃ sarvadevanamaskṛtam ||",
        "oṃ indraṃ vo viśvataspari havāmahe janebhyaḥ | asmākamastu kevalaḥ ||",
        f"bṛhaspatigrahapratyadhidevatām indraṃ {LP}",
        f"bṛhaspatigrahasya uttarataḥ indra{AVA}"],
       "Indra, mounted on Airāvata, bearing the thunderbolt, the lord, guardian "
       "of the east, saluted by all the gods. “We call Indra for you from among "
       "all peoples; may he be ours alone.” Indra, counter-deity of Jupiter, is "
       "invoked on his left."),

    # 6 Śukra
    _h("6 · Śukra"),
    _v(["śukrāriṣṭe tu samprāpte śukrapūjāṃ ca kārayet |",
        "śukradhyānaṃ pravakṣyāmi patnīpīḍopaśāntaye ||"],
       "When affliction from Venus befalls, let Venus be worshipped. I will tell "
       "the meditation on Venus, to quiet troubles concerning one's wife."),
    _p(["śukraṃ te anyadityasya mantrasya bharadvāja ṛṣiḥ | śukragraho devatā | triṣṭup chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitaśukragrahaprasādasiddhyarthe",
        "śukragrahārādhane viniyogaḥ ||"],
       "Of the mantra “śukraṃ te anyat” the seer is Bharadvāja, the deity "
       "Venus, the metre triṣṭubh; it is applied in the worship of Venus."),
    _v(["prācyāṃ bhṛgurbhojakaṭipradeśassabhārgavaḥ pūrvamukhasvabhāvaḥ |",
        "sa pañcakoṇeśarathādhirūḍho daṇḍākṣamālāvarado'mbupātraḥ ||",
        "śvetāmbaraḥ śvetavapuḥ kirīṭī caturbhujo daityaguruḥ praśāntaḥ |",
        "tathāsidaṇḍaṃ ca kamaṇḍaluṃ ca tathākṣasūtraṃ varado'stu mahyam ||"],
       "Dhyāna: in the east, Bhṛgu of the Bhojakaṭa country, of Bhārgava line, "
       "facing east, mounted in his chariot on a five-cornered seat, with staff, "
       "rosary and water-pot, granting boons. White-robed, white of body, "
       "crowned, four-armed, the calm teacher of the daityas, with sword and "
       "staff, water-pot and rosary — may he grant me boons."),
    _v(["oṃ śukraṃ te anyadyajataṃ te anyadviṣurūpe ahanī dyaurivāsi |",
        "viśvā hi māyā avasi svadhāvo bhadrā te pūṣanniha rātirastu ||",
        "oṃ bhūrbhuvassuvaḥ śukragrahehāgaccha ||"],
       "“One form of yours is bright, another worshipful; like heaven you are "
       "day and night, two in appearance. You guard all wondrous powers, O "
       "self-reliant one; Pūṣan, may your kind gift be here.” — Come here, "
       "Venus."),
    _p(["śukragrahaṃ śvetavarṇaṃ śvetagandhaṃ śvetapuṣpaṃ śvetamālyāmbaradharaṃ",
        "śvetacchatradhvajapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ pūrvābhimukhaṃ padmāsanasthaṃ caturbhujaṃ",
        "daṇḍākṣamālājaṭāvalkaladhāriṇaṃ kāmbhojadeśādhipatiṃ bhārgavasagotraṃ",
        "pārthivasaṃvatsare śrāvaṇamāse śuklapakṣe aṣṭamyāṃ bhṛguvāsare",
        "svātīnakṣatrajātaṃ tulāvṛṣabharāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "sūryagrahasya prāgbhāge pañcakoṇākāramaṇḍale",
        f"sthāpitasīsapratimārūpeṇa śukragraha{AVA}"],
       "Venus — white, with white sandal, flowers, garland and garments, facing "
       "east, seated on a lotus, four-armed, bearing staff, rosary, matted hair "
       "and bark garment, lord of Kāmboja, of Bhṛgu's gotra, born in the year "
       "Pārthiva, in Śrāvaṇa, the bright eighth, a Friday, under Svātī, lord of "
       "Libra and Taurus — I invoke in the lead image set in the five-cornered "
       "maṇḍala east of the Sun."),
    _v(["siṃhāsanasthāṃ dvibhujāṃ svarṇābhāṃ ca susundarīm |",
        "śilāsanāṃ śacīṃ dhyāye raktāmbujakarāmbujām ||",
        "oṃ indrāṇīmāsu nāriṣu supatnīmahamaśravam |",
        "na hyasyā aparaṃ cana jarasā marate patiḥ ||",
        "śukragrahādhidevatām indrāṇīṃ sāṅgāṃ sāyudhāṃ savāhanāṃ saśaktiṃ",
        f"patiputraparivārasametāṃ śukragrahasya dakṣiṇataḥ indrāṇī{AVA}"],
       "I meditate on Śacī, enthroned, two-armed, golden and most lovely, a "
       "red lotus in her lotus hand. “Among these women I have heard Indrāṇī "
       "called most fortunate in her husband; for her lord will never die of "
       "old age.” Indrāṇī, presiding deity of Venus, is invoked on his right."),
    _v(["indraṃ sitaṃ caturbāhuṃ sahasranayanojjvalam |",
        "vajrāṅkuśādisaṃyuktapāṇiṃ dhyāyetsusaṃyutam ||",
        "oṃ indra marutva iha pāhi somaṃ yathā śāryāte apibassutasya |",
        "tava praṇītī tava śūra śarmannā vivāsanti kavayassuyajñāḥ ||",
        f"śukragrahapratyadhidevatām indraṃ marutvantaṃ {LP}",
        f"śukragrahasya uttarataḥ indraṃ marutvanta{AVA}"],
       "Let one meditate on Indra, white, four-armed, blazing with a thousand "
       "eyes, holding thunderbolt and goad. “Indra, with the Maruts, drink the "
       "Soma here, as you drank the pressed juice at Śāryāta's; under your "
       "guidance, hero, in your shelter, the poets of good sacrifice seek to "
       "win you.” Indra Marutvān, counter-deity of Venus, is invoked on his "
       "left."),

    # 7 Śani
    _h("7 · Śanaiścara"),
    _v(["śanyariṣṭe tu samprāpte śanipūjāṃ ca kārayet |",
        "śanidhyānaṃ pravakṣyāmi prāṇipīḍopaśāntaye ||"],
       "When affliction from Saturn befalls, let Saturn be worshipped. I will "
       "tell the meditation on Saturn, to quiet the sufferings of living "
       "beings."),
    _p(["śamagniragnibhirityasya mantrasya hiḷimbhiṣi ṛṣiḥ | śanaiścaragraho devatā | uṣṇik chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitaśanaiścaragrahaprasādasiddhyarthe",
        "śanaiścaragrahārādhane viniyogaḥ ||"],
       "Of the mantra “śam agnir agnibhiḥ” the seer is named Hiḷimbhiṣi, the "
       "deity Saturn, the metre uṣṇih; it is applied in the worship of "
       "Saturn."),
    _v(["cāpāsano gṛdhrarathassunīlaḥ pratyaṅmukhaḥ kāśyapajaḥ pratīcyām |",
        "saśūlacāpeṣuvarapradaśca saurāṣṭradeśe prabhavaśca sauriḥ ||",
        "nīladyutirnīlavapuḥ kirīṭī gṛdhrasthitaścāpakaro dhanuṣmān |",
        "caturbhujassūryasutaḥ praśāntassa cāstu mahyaṃ varamandagāmī ||"],
       "Dhyāna: in the west, on a bow-shaped seat, his chariot drawn by a "
       "vulture, deep blue, facing west, born of Kaśyapa's line, with trident, "
       "bow and arrows, granting boons — the son of the Sun, arisen in "
       "Saurāṣṭra. Blue-shining, blue of body, crowned, seated on a vulture, "
       "bow in hand, four-armed, the Sun's calm son, the slow-moving — may he "
       "be the giver of boons to me."),
    _v(["oṃ śamagniragnibhiskaracchaṃ nastapatu sūryaḥ |",
        "śaṃ vāto vātvarapā apa sridhaḥ ||",
        "oṃ bhūrbhuvassuvaḥ śanaiścaragrahehāgaccha ||"],
       "“May Agni with his fires bring us good; may the Sun warm us kindly; may "
       "the wind blow gently; away with the foes.” — Come here, Saturn."),
    _p(["śanaiścaragrahaṃ nīlavarṇaṃ nīlagandhaṃ nīlapuṣpaṃ nīlamālyāmbaradharaṃ",
        "nīlacchatradhvajarathapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "meruṃ pradakṣiṇīkurvāṇaṃ cāpāsanasthaṃ pratyaṅmukhaṃ gṛdhrarathaṃ",
        "caturbhujaṃ śūlāyudhadharaṃ saurāṣṭradeśādhipatiṃ kāśyapasagotraṃ",
        "viśvāmitraṛṣiṃ vibhavasaṃvatsare pauṣamāse śuklapakṣe navamyāṃ sthiravāsare",
        "bharaṇīnakṣatrajātaṃ makarakumbharāśyadhipatiṃ kirīṭinaṃ sukhāsīnaṃ",
        "patnīputraparivārasametaṃ grahamaṇḍale praviṣṭamasminnadhikaraṇe",
        "sūryagrahasya paścimadigbhāge dhanurākāramaṇḍale",
        f"sthāpita ayaḥpratimārūpeṇa śanaiścaragraha{AVA}"],
       "Saturn — blue, with blue sandal, flowers, garland and garments, seated "
       "on a bow, facing west, in a vulture-chariot, four-armed, bearing a "
       "trident, lord of Saurāṣṭra, of Kaśyapa's gotra, born in the year "
       "Vibhava, in Pauṣa, the bright ninth, a Saturday, under Bharaṇī, lord of "
       "Capricorn and Aquarius — I invoke in the iron image set in the "
       "bow-shaped maṇḍala west of the Sun."),
    _v(["daṇḍapāṇiṃ yamaṃ devaṃ mahiṣottamavāhanam |",
        "yamunābhrātaraṃ prītyā yamamāvāhayāmyaham ||",
        "oṃ yamāya somagṃ sunuta yamāya juhutā haviḥ |",
        "yamagṃ ha yajño gacchatyagnidūto araṅkṛtaḥ ||",
        f"śanaiścaragrahādhidevatāṃ yamaṃ {LP}",
        f"śanaiścaragrahasya dakṣiṇataḥ yama{AVA}"],
       "With love I invoke Yama, staff in hand, riding a great buffalo, brother "
       "of the Yamunā. “Press Soma for Yama, offer oblation to Yama; to Yama "
       "goes the sacrifice, well prepared, with Agni as its messenger.” Yama, "
       "presiding deity of Saturn, is invoked on his right."),
    _v(["viriñciṃ vākpatiṃ śvetaṃ paṅkajāsanamacyutam |",
        "akṣasrakkuṇḍikābhītivarapāṇiṃ vicintaye ||",
        "oṃ prajāpate na tvadetānyanyo viśvā jātāni pari tā babhūva |",
        "yatkāmāste juhumastanno astu vayagṃ syāma patayo rayīṇām ||",
        f"śanaiścaragrahapratyadhidevatāṃ prajāpatiṃ {LP}",
        f"śanaiścaragrahasyottarataḥ prajāpati{AVA}"],
       "I contemplate Viriñci, lord of speech, white, lotus-seated, "
       "imperishable, holding rosary and water-pot, granting fearlessness and "
       "boons. “Prajāpati, none but you encompasses all these created things; "
       "may we gain what we desire in offering to you; may we be lords of "
       "riches.” Prajāpati, counter-deity of Saturn, is invoked on his left."),

    # 8 Rāhu
    _h("8 · Rāhu"),
    _v(["rāhvariṣṭe tu samprāpte rāhupūjāṃ ca kārayet |",
        "rāhudhyānaṃ pravakṣyāmi cakṣuḥpīḍopaśāntaye ||"],
       "When affliction from Rāhu befalls, let Rāhu be worshipped. I will tell "
       "the meditation on Rāhu, to quiet troubles of the eyes."),
    _p(["kayānaścitretyasya mantrasya vāmadeva ṛṣiḥ | rāhugraho devatā | gāyatrī chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitarāhugrahaprasādasiddhyarthe",
        "rāhugrahārādhane viniyogaḥ ||"],
       "Of the mantra “kayā naścitraḥ” the seer is Vāmadeva, the deity Rāhu, "
       "the metre gāyatrī; it is applied in the worship of Rāhu."),
    _v(["paiṭhīnaso barbaradeśajātaśśūrpāsanassiṃhagatasvabhāvaḥ |",
        "yāmyānano nairṛtidikkarālo varapradaśśūlasacarmakhaḍgaḥ ||",
        "nīlāmbaro nīlavapuḥ kirīṭī karālavaktraḥ karavālaśūlī |",
        "caturbhujaścarmadharaśca rāhussiṃhādhirūḍho varado'stu mahyam ||"],
       "Dhyāna: of the Paiṭhīnasa line, born in the Barbara country, seated on "
       "a winnow-shaped seat, riding a lion, facing south, terrible in the "
       "south-west, granting boons, with trident, shield and sword. Blue-robed, "
       "blue of body, crowned, fearsome-faced, bearing sword and trident, "
       "four-armed, holding a shield, mounted on a lion — may Rāhu grant me "
       "boons."),
    _v(["oṃ kayā naścitra ā bhuvadūtī sadāvṛdhassakhā |",
        "kayā śaciṣṭhayā vṛtā ||",
        "oṃ bhūrbhuvassuvaḥ rāhugrahehāgaccha ||"],
       "“With what help will he come to us, the wondrous, ever-waxing friend? "
       "With what most powerful company?” — Come here, Rāhu."),
    _p(["rāhugrahaṃ nīlavarṇaṃ nīlagandhaṃ nīlapuṣpaṃ nīlamālyāmbaradharaṃ",
        "nīlacchatradhvajarathapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "merumapradakṣiṇīkurvāṇaṃ siṃhāsanaṃ nairṛtimukhaṃ śūrpāsanasthaṃ",
        "caturbhujaṃ karālavaktraṃ khaḍgacarmadharaṃ paiṭhīnasagotraṃ",
        "barbaradeśādhipatiṃ rākṣasanāmasaṃvatsare bhādrapadamāse kṛṣṇapakṣe",
        "caturdaśyāṃ bhānuvāsare viśākhānakṣatrajātaṃ siṃharāśiprayuktaṃ",
        "kirīṭinaṃ sukhāsīnaṃ saśaktiṃ patnīputraparivārasametaṃ",
        "grahamaṇḍale praviṣṭamasminnadhikaraṇe sūryagrahasya nairṛtidigbhāge",
        f"śūrpākāramaṇḍale sthāpitalohapratimārūpeṇa rāhugraha{AVA}"],
       "Rāhu — blue, with blue sandal, flowers, garland and garments, circling "
       "Meru counter-sunwise, on a lion seat, facing south-west, on a winnow "
       "seat, four-armed, fearsome-faced, with sword and shield, of the "
       "Paiṭhīnasa gotra, lord of the Barbara country, born in the year "
       "Rākṣasa, in Bhādrapada, the dark fourteenth, a Sunday, under Viśākhā, "
       "joined with Leo — I invoke in the metal image set in the winnow-shaped "
       "maṇḍala south-west of the Sun."),
    _v(["nīlotpaladalaśyāmāṃ dīrghaśṛṅgopaśobhitām |",
        "mūrdhajaṃ pāśadaṇḍaṃ ca dadhānāṃ sarvamaṅgalām ||",
        "oṃ āyaṅgauḥ pṛśnirakramīdasadanmātaraṃ puraḥ |",
        "pitaraṃ ca prayantsuvaḥ ||",
        "rāhugrahādhidevatāṃ gāṃ sāṅgāṃ sāyudhāṃ savāhanāṃ saśaktiṃ",
        f"putraparivārasametāṃ rāhugrahasya dakṣiṇataḥ gā{AVA}"],
       "The Cow, dark as a blue lotus petal, graced with long horns, bearing "
       "noose and staff, all-auspicious. “This dappled bull has come forth and "
       "sat before the Mother, going to the Father, heaven.” The Cow, presiding "
       "deity of Rāhu, is invoked on his right."),
    _v(["kirīṭinaṃ dvibāhuṃ ca khaḍgacarmagadādharam |",
        "karālavadanaṃ bhīmaṃ dīrghapucchaṃ mahābalam ||",
        "oṃ namo astu sarpebhyo ye ke ca pṛthivīmanu |",
        "ye antarikṣe ye divi tebhyassarpebhyo namaḥ ||",
        f"rāhugrahapratyadhidevatāṃ sarpaṃ {LP}",
        f"rāhugrahasya uttarataḥ sarpa{AVA}"],
       "The Serpent — crowned, two-armed, with sword, shield and mace, "
       "fearsome-faced, terrible, long-tailed, of great strength. “Salutation "
       "to the serpents, whichever are on the earth, in the mid-air and in "
       "heaven: to those serpents, salutation.” The Serpent, counter-deity of "
       "Rāhu, is invoked on his left."),

    # 9 Ketu
    _h("9 · Ketu"),
    _v(["ketvariṣṭe tu samprāpte ketupūjāṃ ca kārayet |",
        "ketudhyānaṃ pravakṣyāmi jñānapīḍopaśāntaye ||"],
       "When affliction from Ketu befalls, let Ketu be worshipped. I will tell "
       "the meditation on Ketu, to quiet troubles of understanding."),
    _p(["ketuṃ kṛṇvannityasya mantrasya madhucchandā ṛṣiḥ | ketugaṇo devatā | gāyatrī chandaḥ |",
        "(mama) yajamānasyādhidevatāpratyadhidevatāsahitaketugaṇaprasādasiddhyarthe",
        "ketugaṇārādhane viniyogaḥ ||"],
       "Of the mantra “ketuṃ kṛṇvan” the seer is Madhucchandas, the deity the "
       "host of Ketus, the metre gāyatrī; it is applied in the worship of "
       "Ketu."),
    _v(["dhvajāsano jaiminigotrajo'ntarvedeṣu deśeṣu vicitravarṇaḥ |",
        "yāmyāsano vāyudiśaḥ prakhaḍgaścarmāsibhiścāṣṭasutaśca ketuḥ ||",
        "dhūmro dvibāhurvarado gadābhṛdgṛdhrāsanastho vikṛtānanaśca |",
        "kirīṭakeyūravibhūṣitāṅgassa cāstu me ketugaṇaḥ praśāntaḥ ||"],
       "Dhyāna: on a banner-shaped seat, of Jaimini's gotra, of the Antarvedī "
       "lands, many-coloured, seated towards the south in the north-west, "
       "bearing sword and shield. Smoke-grey, two-armed, giver of boons, "
       "mace-bearing, seated on a vulture, of strange visage, adorned with "
       "crown and armlets — may the host of Ketus be calm toward me."),
    _v(["oṃ ketuṃ kṛṇvannaketave peśo maryā apeśase |",
        "samuṣadbhirajāyathāḥ ||",
        "oṃ bhūrbhuvassuvaḥ ketugaṇehāgaccha ||"],
       "“Making light where there was no light, form where there was no form, "
       "O mortals, you were born together with the dawns.” — Come here, host "
       "of Ketus."),
    _p(["ketugaṇaṃ citravarṇaṃ citragandhaṃ citrapuṣpaṃ citramālyāmbaradharaṃ",
        "citracchatradhvajarathapatākādiśobhitaṃ divyarathasamārūḍhaṃ",
        "merumapradakṣiṇīkurvāṇaṃ dhvajāsanasthaṃ dakṣiṇābhimukham",
        "antarvedideśādhipatiṃ dvibāhuṃ gadādharaṃ jaiminigotraṃ",
        "rākṣasanāmasaṃvatsare caitramāse kṛṣṇapakṣe caturdaśyām induvāsare",
        "revatīnakṣatrajātaṃ karkaṭakarāśiprayuktaṃ siṃhāsanāsīnaṃ",
        "grahamaṇḍale praviṣṭamasminnadhikaraṇe sūryagrahasya vāyavyadigbhāge",
        f"dhvajākāramaṇḍale sthāpitapañcalohapratimārūpeṇa ketugaṇa{AVA}"],
       "The host of Ketus — many-coloured, with varied sandal, flowers, garland "
       "and garments, circling Meru counter-sunwise, on a banner seat, facing "
       "south, lord of Antarvedī, two-armed, mace-bearing, of Jaimini's gotra, "
       "born in the year Rākṣasa, in Caitra, the dark fourteenth, a Monday, "
       "under Revatī, joined with Cancer, seated on a lion throne — I invoke in "
       "the five-metal image set in the banner-shaped maṇḍala north-west of "
       "the Sun."),
    _v(["citraguptaṃ mahāprājñaṃ vetradhāriṇamavyayam |",
        "raktavarṇāmbaradharaṃ sarvapāpaharaṃ vibhum ||",
        "oṃ sacitra citraṃ citayantamasme citrakṣatra citratamaṃ vayodhām |",
        "candraṃ rayiṃ puruvīraṃ bṛhantaṃ candra candrābhirgṛṇate yuvasva ||",
        f"ketugaṇādhidevatāṃ citraguptaṃ {LP}",
        f"ketugaṇasya dakṣiṇataḥ citragupta{AVA}"],
       "Citragupta, greatly wise, cane-bearing, unfailing, in red garments, "
       "remover of all sin, the lord. “O bright one of bright dominion, bring us "
       "bright, shining wealth that gives vigour, rich in heroes, great; O "
       "radiant one, with your radiance draw it to the one who praises you.” "
       "Citragupta, presiding deity of Ketu, is invoked on his right."),
    _v(["brahmāṇaṃ raktagaurāṅgaṃ caturvaktraṃ jagatprabhum |",
        "akṣasrakkuṇḍikābhītivarapāṇiṃ vicintaye ||",
        "oṃ brahmā devānāṃ padavīḥ kavīnāmṛṣirviprāṇāṃ mahiṣo mṛgāṇām |",
        "śyeno gṛdhrāṇāgṃ svadhitirvanānāgṃ somaḥ pavitramatyeti rebhan ||",
        f"ketugaṇapratyadhidevatāṃ brahmāṇaṃ {LP}",
        f"ketugaṇasyottarataḥ brahmāṇa{AVA}"],
       "I contemplate Brahmā … “Brahmā among the gods …” Brahmā, counter-deity "
       "of Ketu, is invoked on his left."),
    _p(["adhidevatāpratyadhidevatāsahita ādityādinavagrahadevatābhyo namaḥ |",
        "dhyāyāmi āvāhayāmi ratnasiṃhāsanaṃ samarpayāmi pādyaṃ samarpayāmi",
        "arghyaṃ samarpayāmi ācamanīyaṃ samarpayāmi snānaṃ samarpayāmi",
        "śuddhācamanīyaṃ samarpayāmi vastraṃ samarpayāmi yajñopavītaṃ samarpayāmi",
        "gandhaṃ samarpayāmi akṣatān samarpayāmi puṣpāṇi samarpayāmi",
        "dhūpamāghrāpayāmi dīpaṃ darśayāmi naivedyaṃ samarpayāmi",
        "tāmbūlaṃ samarpayāmi mantrapuṣpaṃ samarpayāmi ||",
        "adhidevatāpratyadhidevatāsahita ādityādinavagrahadevatāprasādasiddhirastu ||"],
       "Salutation to the nine planets beginning with the Sun, with their "
       "presiding and counter-deities; the sixteen services are offered. May "
       "their grace be gained."),
]

# ───────────────────────── the eight dikpālas ─────────────────────────
S += [
    "ornament",
    _h("Aṣṭadikpāla Pūjā · the guardians of the quarters"),
    _r("Around the planets, the guardians are set in their quarters: Indra "
       "east, Agni south-east, Yama south, Nirṛti south-west, Varuṇa west, Vāyu "
       "north-west, Kubera north and Īśāna north-east."),
    _v(["oṃ indraṃ vo viśvataspari havāmahe janebhyaḥ | asmākamastu kevalaḥ ||",
        f"{LP} indraṃ dikpālaka{AVA}"],
       "1. Indra: “We call Indra for you from among all peoples; may he be ours "
       "alone.” I invoke, install and worship Indra as guardian of the "
       "quarter."),
    _v(["oṃ agniṃ dūtaṃ vṛṇīmahe hotāraṃ viśvavedasam | asya yajñasya sukratum ||",
        f"{LP} agniṃ dikpālaka{AVA}"],
       "2. Agni: “We choose Agni as messenger …” I invoke Agni as guardian of "
       "the quarter."),
    _v(["oṃ yamāya somagṃ sunuta yamāya juhutā haviḥ |",
        "yamagṃ ha yajño gacchatyagnidūto araṅkṛtaḥ ||",
        f"{LP} yamaṃ dikpālaka{AVA}"],
       "3. Yama: “Press Soma for Yama …” I invoke Yama as guardian of the "
       "quarter."),
    _v(["oṃ mo ṣu ṇaḥ parāparā nirṛtirdurhaṇā vadhīt | padīṣṭa tṛṣṇayā saha ||",
        f"{LP} nirṛtiṃ dikpālaka{AVA}"],
       "4. Nirṛti: “Let not Nirṛti, hard to strike down, smite us from far and "
       "near; may she perish together with thirst.” I invoke Nirṛti as "
       "guardian of the quarter."),
    _v(["oṃ imaṃ me varuṇa śrudhī havamadyā ca mṛḍaya | tvāmavasyurācake ||",
        f"{LP} varuṇaṃ dikpālaka{AVA}"],
       "5. Varuṇa: “Hear this call of mine, Varuṇa, and be gracious today; "
       "seeking help, I long for you.” I invoke Varuṇa as guardian of the "
       "quarter."),
    _v(["oṃ tava vāyavṛtaspate tvaṣṭurjāmātaradbhuta | avāgṃsyā vṛṇīmahe ||",
        f"{LP} vāyuṃ dikpālaka{AVA}"],
       "6. Vāyu: “Wondrous Vāyu, lord of order, son-in-law of Tvaṣṭṛ, we choose "
       "your protection.” I invoke Vāyu as guardian of the quarter."),
    _v(["oṃ somo dhenugṃ somo arvantamāśugṃ somo vīraṃ karmaṇyaṃ dadāti |",
        "sādanyaṃ vidathyagṃ sabheyaṃ pitṛśravaṇaṃ yo dadāśadasmai ||",
        f"{LP} kuberaṃ dikpālaka{AVA}"],
       "7. Kubera: “Soma gives a milch-cow, Soma a swift steed, Soma a hero "
       "skilled in work — fit for home, for council and assembly, the glory of "
       "his father — to whoever worships him.” I invoke Kubera as guardian of "
       "the quarter."),
    _v(["oṃ tamīśānaṃ jagatastasthuṣaspatiṃ dhiyañjinvamavase hūmahe vayam |",
        "pūṣā no yathā vedasāmasadvṛdhe rakṣitā pāyuradabdhassvastaye ||",
        f"{LP} īśānaṃ dikpālaka{AVA}"],
       "8. Īśāna: “We call for help on that Lord, master of the moving and the "
       "unmoving, who quickens thought; that Pūṣan may be for the increase of "
       "our wealth, our guardian and protector, unassailable, for our "
       "welfare.” I invoke Īśāna as guardian of the quarter."),
    _p(["indrādyaṣṭadikpālakadevatābhyo namaḥ |",
        "dhyāyāmi āvāhayāmi ratnasiṃhāsanaṃ samarpayāmi pādyaṃ samarpayāmi",
        "arghyaṃ samarpayāmi ācamanīyaṃ samarpayāmi snapayāmi",
        "vastraṃ samarpayāmi yajñopavītaṃ samarpayāmi gandhaṃ samarpayāmi",
        "akṣatān samarpayāmi puṣpāṇi samarpayāmi dhūpamāghrāpayāmi",
        "dīpaṃ darśayāmi naivedyaṃ samarpayāmi tāmbūlaṃ samarpayāmi",
        "mantrapuṣpaṃ samarpayāmi ||",
        "indrādyaṣṭadikpālakadevatāprasādasiddhirastu ||"],
       "Salutation to the eight guardians of the quarters beginning with "
       "Indra; the services are offered. May their grace be gained."),
]

# ───────────────────── Satyanārāyaṇa pūjā: purification ─────────────────────
S += [
    "ornament",
    _h("Śrī Satyanārāyaṇa Pūjā"),
    _r("Set the image of Satyanārāyaṇa on a betel leaf and cleanse it with the "
       "five nectars in turn — milk, curd, ghee, honey — and then pure water."),
    _v(["āpyāyasveti kṣīram ||",
        "oṃ āpyāyasva sametu te viśvatassoma vṛṣṇiyam | bhavā vājasya saṅgathe ||"],
       "With “āpyāyasva”, milk: “Swell, O Soma; let vigour gather to you from "
       "every side; be present where strength is won.”"),
    _v(["dadhikrāvṇṇa iti dadhi ||",
        "dadhikrāvṇṇo akāriṣaṃ jiṣṇoraśvasya vājinaḥ |",
        "surabhi no mukhā karatpra ṇa āyūgṃṣi tāriṣat ||"],
       "With “dadhikrāvṇaḥ”, curd: “I have praised Dadhikrāvan, the victorious, "
       "swift steed; may he make our mouths fragrant and lengthen our lives.”"),
    _v(["śukramasītyājyam ||",
        "śukramasi jyotirasi tejo'si devo vassavitotpunātvacchidreṇa",
        "pavitreṇa vasossūryasya raśmibhiḥ ||"],
       "With “śukramasi”, ghee: “You are bright, you are light, you are "
       "splendour; may god Savitṛ purify you with the flawless strainer, with "
       "the rays of the good sun.”"),
    _v(["madhu vātā ṛtāyateti madhu ||",
        "madhu vātā ṛtāyate madhu kṣaranti sindhavaḥ | mādhvīrnassantvoṣadhīḥ |",
        "madhu naktamutoṣasi madhumatpārthivagṃ rajaḥ | madhu dyaurastu naḥ pitā |",
        "madhumānno vanaspatirmadhumāgṃ astu sūryaḥ | mādhvīrgāvo bhavantu naḥ ||"],
       "With “madhu vātāḥ”, honey: “For the one who keeps the order the winds "
       "blow honey, the rivers stream honey; sweet be the plants to us. Honey "
       "by night and at dawn, sweet the dust of the earth, sweet be Heaven our "
       "father; sweet be the tree to us, sweet the sun, sweet the cows.”"),
    _v(["svāduḥ pavasveti śuddhodakam ||",
        "svāduḥ pavasva divyāya janmane svādurindrāya suhavītu nāmne |",
        "svādurmitrāya varuṇāya vāyave bṛhaspataye madhumāgṃ adābhyaḥ ||"],
       "With “svāduḥ pavasva”, pure water: “Flow sweet for the heavenly race, "
       "sweet for Indra whose name is good to call, sweet for Mitra, Varuṇa and "
       "Vāyu, for Bṛhaspati, honeyed and unharmed.”"),
    _v(["āpo hi ṣṭheti śuddhodakasnānam ||",
        "āpo hi ṣṭhā mayobhuvastā na ūrje dadhātana mahe raṇāya cakṣase |",
        "yo vaśśivatamo rasastasya bhājayateha naḥ uśatīriva mātaraḥ |",
        "tasmā araṃ gamāma vo yasya kṣayāya jinvatha āpo janayathā ca naḥ ||"],
       "With “āpo hi ṣṭhā”, the bath of pure water: “O waters, you are the "
       "source of well-being …”"),
    _h("Prāṇapratiṣṭhā · installing the life-breath"),
    _p(["prāṇapratiṣṭhāpanaṃ kariṣye |",
        "oṃ asya śrīprāṇapratiṣṭhāpanamahāmantrasya brahmaviṣṇumaheśvarā ṛṣayaḥ |",
        "ṛgyajussāmātharvaṇāni chandāṃsi | prāṇaśśaktiḥ parā devatā |",
        "hrāṃ bījaṃ | hrīṃ śaktiḥ | kroṃ kīlakam |",
        "śrīsatyanārāyaṇaprāṇapratiṣṭhājape viniyogaḥ ||"],
       "I will install the life-breath. Of this great mantra the seers are "
       "Brahmā, Viṣṇu and Maheśvara; the metres the four Vedas; the deity the "
       "supreme power of breath; hrāṃ the seed, hrīṃ the power, kroṃ the pin; "
       "it is applied to installing the life of Śrī Satyanārāyaṇa."),
    _p(["karanyāsaḥ — hrāṃ aṅguṣṭhābhyāṃ namaḥ | hrīṃ tarjanībhyāṃ namaḥ |",
        "hrūṃ madhyamābhyāṃ namaḥ | hraiṃ anāmikābhyāṃ namaḥ |",
        "hrauṃ kaniṣṭhikābhyāṃ namaḥ | hraḥ karatalakarapṛṣṭhābhyāṃ namaḥ ||",
        "aṅganyāsaḥ — hrāṃ hṛdayāya namaḥ | hrīṃ śirase svāhā |",
        "hrūṃ śikhāyai vaṣaṭ | hraiṃ kavacāya hum |",
        "hrauṃ netratrayāya vauṣaṭ | hraḥ astrāya phaṭ ||",
        "bhūrbhuvassuvaromiti digbandhaḥ ||"],
       "The placings on the hands — thumbs, forefingers, middle, ring and "
       "little fingers, palms and backs — and on the body — heart, head, crown "
       "of the head, the armour of the arms, the three eyes, and the weapon; "
       "then the quarters are sealed with “bhūr bhuvaḥ suvar om”."),
    _v(["śāntākāraṃ bhujagaśayanaṃ padmanābhaṃ sureśaṃ",
        "viśvākāraṃ gaganasadṛśaṃ meghavarṇaṃ śubhāṅgam |",
        "lakṣmīkāntaṃ kamalanayanaṃ yogihṛddhyānagamyaṃ",
        "vande viṣṇuṃ bhavabhayaharaṃ sarvalokaikanātham ||"],
       "Dhyāna: I bow to Viṣṇu — of peaceful form, lying on the serpent, "
       "lotus-naveled, lord of the gods, the universe his form, like the sky, "
       "cloud-coloured, of lovely limbs, Lakṣmī's beloved, lotus-eyed, reached "
       "by yogins in the heart's meditation, remover of the fear of worldly "
       "life, sole lord of all the worlds."),
    _p(["oṃ hrāṃ hrīṃ kroṃ aṃ yaṃ raṃ laṃ vaṃ śaṃ ṣaṃ saṃ haṃ ḷaṃ kṣaṃ",
        "śrīsatyanārāyaṇaprāṇa iha prāṇa |",
        "oṃ hrāṃ hrīṃ kroṃ śrīsatyanārāyaṇasarvendriyāṇi",
        "vāṅmanastvakcakṣuśśrotrajihvāghrāṇa",
        "ihaivāgatya sukhaṃ ciraṃ tiṣṭhantu svāhā ||"],
       "With the seed-syllables: the life of Śrī Satyanārāyaṇa is here; may all "
       "his senses — speech, mind, touch, sight, hearing, taste and smell — "
       "come here and dwell long and happily. Svāhā."),
    _v(["oṃ asunīte punarasmāsu cakṣuḥ punaḥ prāṇamiha no dhehi bhogam |",
        "jyokpaśyema sūryamuccarantamanumate mṛḍayā nassvasti ||",
        "amṛtaṃ vai prāṇā amṛtamāpaḥ prāṇāneva yathāsthānamupahvayate ||",
        f"{LP} śrīsatyanārāyaṇa{AVA}"],
       "“O Asunīti, give us again sight, again breath here, and enjoyment; long "
       "may we see the sun rising; Anumati, be gracious to us, for our "
       "welfare.” The breaths are immortal, the waters are immortal: so he "
       "calls the breaths each to its place. With his limbs, weapons, mount and "
       "power, with consort, sons and retinue, I invoke, install and worship "
       "Śrī Satyanārāyaṇa."),
    _v(["dhyāyetsatyaṃ guṇātītaṃ guṇatrayasamanvitam |",
        "lokanāthaṃ trilokeśaṃ kaustubhābharaṇaṃ harim ||",
        "pītāmbaraṃ nīlavarṇaṃ śrīvatsapadabhūṣitam |",
        "govindaṃ gokulānandaṃ brahmādyairabhipūjitam ||",
        f"{SN} dhyānaṃ samarpayāmi ||"],
       "Dhyāna: let one meditate on Satya, beyond the three qualities yet "
       "endowed with them, lord of the world, master of the three worlds, Hari "
       "adorned with the Kaustubha gem, yellow-robed, blue of hue, marked with "
       "the Śrīvatsa, Govinda, joy of Gokula, worshipped by Brahmā and the "
       "gods. — Salutation to Śrī Vīra Veṅkaṭa Satyanārāyaṇa Svāmi, with Ādyā "
       "Mahālakṣmī: I offer meditation."),
]

# ───────────────────── the sixteen upacāras ─────────────────────
def _upa(name, purusha, sri, sloka, offer, gloss):
    return [_h(name), _v(purusha + sri + sloka + [f"{SN} {offer} ||"], gloss)]


S += _upa(
    "Āvāhanam · invocation",
    ["oṃ sahasraśīrṣā puruṣaḥ | sahasrākṣassahasrapāt |",
     "sa bhūmiṃ viśvato vṛtvā | atyatiṣṭhaddaśāṅgulam ||"],
    ["hiraṇyavarṇāṃ hariṇīṃ suvarṇarajatasrajām |",
     "candrāṃ hiraṇmayīṃ lakṣmīṃ jātavedo mamāvaha ||"],
    ["jyotiśśāntaṃ sarvalokāntarastham oṅkārākhyaṃ yogihṛddhyānagamyam |",
     "sāṅgaṃ śaktiṃ sāyudhaṃ bhaktisevyaṃ sarvākāraṃ viṣṇumāvāhayāmi ||"],
    "āvāhayāmi",
    "Puruṣa Sūkta 1: “The Puruṣa has a thousand heads, a thousand eyes, a "
    "thousand feet; enveloping the earth on every side, he stands beyond it by "
    "ten fingers.” Śrī Sūkta 1: “Bring me, Jātavedas, Lakṣmī — golden of hue, "
    "the doe, wearing garlands of gold and silver, moon-like, made of gold.” "
    "The light, peaceful, dwelling within all worlds, called Oṃ, reached in "
    "the yogin's heart — with his limbs, power and weapons, served by "
    "devotion, whose form is everything: Viṣṇu I invoke.")
S += _upa(
    "Āsanam · seat",
    ["oṃ puruṣa evedagṃ sarvam | yadbhūtaṃ yacca bhavyam |",
     "utāmṛtatvasyeśānaḥ | yadannenātirohati ||"],
    ["tāṃ ma āvaha jātavedo lakṣmīmanapagāminīm |",
     "yasyāṃ hiraṇyaṃ vindeyaṃ gāmaśvaṃ puruṣānaham ||"],
    ["kalpadrumūle maṇivedimadhye siṃhāsanaṃ svarṇamayaṃ vicitram |",
     "vicitravastrāvṛtamacyuta prabho gṛhāṇa lakṣmīdharaṇīsamanvita ||"],
    "ratnasiṃhāsanaṃ samarpayāmi",
    "Puruṣa Sūkta 2: “The Puruṣa alone is all this, what has been and what is "
    "to be; he is lord of immortality, which he transcends through food.” Śrī "
    "Sūkta 2: “Bring me, Jātavedas, that Lakṣmī who does not depart, in whom I "
    "may find gold, cattle, horses and people.” At the foot of the wishing-tree, "
    "on a jewelled altar, a golden throne of many colours, spread with rich "
    "cloths — accept it, Lord Acyuta, with Lakṣmī and Earth. — I offer a "
    "jewelled throne.")
S += _upa(
    "Pādyam · water for the feet",
    ["oṃ etāvānasya mahimā | ato jyāyāgṃśca pūruṣaḥ |",
     "pādo'sya viśvā bhūtāni | tripādasyāmṛtaṃ divi ||"],
    ["aśvapūrvāṃ rathamadhyāṃ hastinādaprabodhinīm |",
     "śriyaṃ devīmupahvaye śrīrmā devī juṣatām ||"],
    ["nārāyaṇa namaste'stu narakārṇavatāraka |",
     "pādyaṃ gṛhāṇa deveśa mama saukhyaṃ vivardhaya ||"],
    "pādayoḥ pādyaṃ samarpayāmi",
    "Puruṣa Sūkta 3: “Such is his greatness, and the Puruṣa is greater still; "
    "all beings are a quarter of him, three quarters the immortal in heaven.” "
    "Śrī Sūkta 3: “I call the goddess Śrī, with horses before and chariots in "
    "the midst, roused by the trumpeting of elephants; may the goddess Śrī "
    "delight in me.” Salutation, Nārāyaṇa, who carries us across the sea of "
    "hell; accept water for your feet, lord of gods, and increase my happiness.")
S += _upa(
    "Arghyam · water for the hands",
    ["oṃ tripādūrdhva udaitpuruṣaḥ | pādo'syehābhavātpunaḥ |",
     "tato viṣvaṅvyakrāmat | sāśanānaśane abhi ||"],
    ["kāṃ so'smitāṃ hiraṇyaprākārāmārdrāṃ jvalantīṃ tṛptāṃ tarpayantīm |",
     "padme sthitāṃ padmavarṇāṃ tāmihopahvaye śriyam ||"],
    ["vyaktāvyaktasvarūpāya hṛṣīkapataye namaḥ |",
     "mayā nivedito bhaktyā hyarghyo'yaṃ pratigṛhyatām ||"],
    "hastayorarghyaṃ samarpayāmi",
    "Puruṣa Sūkta 4: “With three quarters the Puruṣa rose up; one quarter of "
    "him came to be here again; thence he spread everywhere, over what eats "
    "and what does not.” Śrī Sūkta 4: “Her who is bliss, gently smiling, "
    "walled in gold, moist, blazing, contented and contenting, standing on the "
    "lotus, lotus-hued — Śrī I call here.” Salutation to the lord of the "
    "senses, whose form is manifest and unmanifest; accept this water I offer "
    "with devotion.")
S += _upa(
    "Ācamanīyam · water to sip",
    ["oṃ tasmādvirāḍajāyata | virājo adhi pūruṣaḥ |",
     "sa jāto atyaricyata | paścādbhūmimatho puraḥ ||"],
    ["candrāṃ prabhāsāṃ yaśasā jvalantīṃ śriyaṃ loke devajuṣṭāmudārām |",
     "tāṃ padminīmīṃ śaraṇamahaṃ prapadye'lakṣmīrme naśyatāṃ tvāṃ vṛṇe ||"],
    ["mandākinyāstu yadvāri sarvapāpaharaṃ śubham |",
     "tadidaṃ kalpitaṃ deva samyagācamyatāṃ vibho ||"],
    "ācamanīyaṃ samarpayāmi",
    "Puruṣa Sūkta 5: “From him Virāj was born, and from Virāj the Puruṣa; once "
    "born he reached beyond the earth, behind and before.” Śrī Sūkta 5: “Moon-"
    "like, shining, blazing with glory, Śrī honoured by the gods in the world, "
    "generous — in her, the lotus-lady, I take refuge: may my misfortune "
    "perish; I choose you.” The water of the heavenly Gaṅgā, pure, taking away "
    "all sin — this is prepared for you, Lord: sip it.")
S += _upa(
    "Snānam · bath",
    ["oṃ yatpuruṣeṇa haviṣā | devā yajñamatanvata |",
     "vasanto asyāsīdājyam | grīṣma idhmaśśaraddhaviḥ ||"],
    ["ādityavarṇe tapaso'dhijāto vanaspatistava vṛkṣo'tha bilvaḥ |",
     "tasya phalāni tapasā nudantu māyāntarāyāśca bāhyā alakṣmīḥ ||"],
    ["tīrthodakaiḥ kāñcanakumbhasaṃsthaissuvāsitairdeva kṛpārasārdraiḥ |",
     "mayārpitaṃ snānavidhiṃ gṛhāṇa pādābjaniṣṭhyūtanadīpravāha ||"],
    "snapayāmi",
    "Puruṣa Sūkta 6: “When the gods spread the sacrifice with the Puruṣa as "
    "oblation, spring was its ghee, summer the fuel, autumn the offering.” Śrī "
    "Sūkta 6: “O sun-hued one, by your austerity was born the bilva, king of "
    "trees; may its fruits by austerity drive away illusion, the inner "
    "hindrances and outer misfortune.” With holy waters in golden jars, "
    "scented and soft with compassion, accept the bath I offer, O Lord from "
    "whose lotus-feet the river flowed.")
S += [
    _h("Pañcāmṛtasnānam · bath of the five nectars"),
    _p(["āpyāyasva sametu te viśvatassoma vṛṣṇiyam | bhavā vājasya saṅgathe ||",
        "dadhikrāvṇṇo akāriṣaṃ jiṣṇoraśvasya vājinaḥ | surabhi no mukhā karatpra ṇa āyūgṃṣi tāriṣat ||",
        "śukramasi jyotirasi tejo'si devo vassavitotpunātvacchidreṇa pavitreṇa vasossūryasya raśmibhiḥ ||",
        "madhu vātā ṛtāyate madhu kṣaranti sindhavaḥ mādhvīrnassantvoṣadhīḥ |",
        "madhu naktamutoṣasi madhumatpārthivagṃ rajaḥ madhu dyaurastu naḥ pitā |",
        "madhumānno vanaspatirmadhumāgṃ astu sūryaḥ mādhvīrgāvo bhavantu naḥ ||",
        "svāduḥ pavasva divyāya janmane svādurindrāya suhavītu nāmne |",
        "svādurmitrāya varuṇāya vāyave bṛhaspataye madhumāgṃ adābhyaḥ ||"],
       "The five mantras of milk, curd, ghee, honey and pure water, recited "
       "together."),
    _v(["snānaṃ pañcāmṛtairdeva gṛhāṇa puruṣottama |",
        "anāthanātha sarvajña gīrvāṇapraṇatipriya ||",
        f"{SN} pañcāmṛtasnānaṃ samarpayāmi ||"],
       "Accept the bath of the five nectars, O god, Puruṣottama, protector of "
       "the unprotected, all-knowing, fond of the homage of the gods. (The "
       "nectars are sprinkled on the image with a flower.)"),
    _h("Śuddhodakasnānam · bath of pure water"),
    _v(["āpo hi ṣṭhā mayobhuvastā na ūrje dadhātana mahe raṇāya cakṣase |",
        "yo vaśśivatamo rasastasya bhājayateha naḥ uśatīriva mātaraḥ |",
        "tasmā araṃ gamāma vo yasya kṣayāya jinvatha āpo janayathā ca naḥ ||",
        "nadīnāṃ caiva sarvāsāmānītaṃ nirmalodakam |",
        "snānaṃ svīkuru deveśa mayā dattaṃ sureśvara ||",
        f"{SN} śuddhodakasnānaṃ samarpayāmi ||"],
       "“O waters, you are the source of well-being …” Pure water brought from "
       "all the rivers — accept this bath I give you, lord of gods. (Water is "
       "shown to the image with the spoon and poured into the plate.)"),
]
S += _upa(
    "Vastram · garments",
    ["oṃ saptāsyāsanparidhayaḥ | trissapta samidhaḥ kṛtāḥ |",
     "devā yadyajñaṃ tanvānāḥ | abadhnanpuruṣaṃ paśum ||"],
    ["upaitu māṃ devasakhaḥ kīrtiśca maṇinā saha |",
     "prādurbhūto'smi rāṣṭre'smin kīrtimṛddhiṃ dadātu me ||"],
    ["vedasūktasamāyukte yajñasāmasamanvite |",
     "sarvavarṇaprade deva vāsasī te vinirmite ||"],
    "vastrayugmaṃ samarpayāmi",
    "Puruṣa Sūkta 7: “Seven were its enclosing sticks, thrice seven its fuel, "
    "when the gods, spreading the sacrifice, bound the Puruṣa as victim.” Śrī "
    "Sūkta 7: “May the friend of the gods come to me, and fame with the jewel; "
    "I am born in this land — may he grant me fame and plenty.” These two "
    "garments, joined with Vedic hymns and sacrificial chants, giving every "
    "colour, are made for you, O god. — I offer a pair of garments.")
S += _upa(
    "Yajñopavītam · sacred thread",
    ["oṃ taṃ yajñaṃ barhiṣi praukṣan | puruṣaṃ jātamagrataḥ |",
     "tena devā ayajanta | sādhyā ṛṣayaśca ye ||"],
    ["kṣutpipāsāmalāṃ jyeṣṭhāmalakṣmīṃ nāśayāmyaham |",
     "abhūtimasamṛddhiṃ ca sarvāṃ nirṇuda me gṛhāt ||"],
    ["brahmaviṣṇumaheśānāṃ nirmitaṃ brahmasūtrakam |",
     "gṛhāṇa bhagavan viṣṇo sarveṣṭaphalado bhava ||"],
    "yajñopavītaṃ samarpayāmi",
    "Puruṣa Sūkta 8: “They sprinkled on the sacred grass that sacrifice, the "
    "Puruṣa born in the beginning; with him the gods sacrificed, the Sādhyas "
    "and the seers.” Śrī Sūkta 8: “I destroy Alakṣmī, the elder sister, "
    "defiled with hunger and thirst; drive out of my house all ill-fortune and "
    "want.” The sacred thread made by Brahmā, Viṣṇu and Śiva — accept it, Lord "
    "Viṣṇu, and grant every wished-for fruit.")
S += _upa(
    "Gandham · sandal",
    ["oṃ tasmādyajñātsarvahutaḥ | sambhṛtaṃ pṛṣadājyam |",
     "paśūgṃstāgṃścakre vāyavyān | āraṇyāngrāmyāśca ye ||"],
    ["gandhadvārāṃ durādharṣāṃ nityapuṣṭāṃ karīṣiṇīm |",
     "īśvarīgṃ sarvabhūtānāṃ tāmihopahvaye śriyam ||"],
    ["śrīkhaṇḍaṃ candanaṃ divyaṃ gandhāḍhyaṃ sumanoharam |",
     "vilepanaṃ suraśreṣṭha prītyarthaṃ pratigṛhyatām ||"],
    "divyaśrīcandanaṃ samarpayāmi",
    "Puruṣa Sūkta 9: “From that sacrifice, offered whole, the clotted ghee was "
    "gathered; he made the creatures of the air, and those of the forest and "
    "the village.” Śrī Sūkta 9: “Her whose door is fragrance … Śrī I call "
    "here.” Divine sandal, fragrant and lovely — accept this unguent for your "
    "pleasure, best of gods.")
S += _upa(
    "Ābharaṇam · ornaments",
    ["oṃ tasmādyajñātsarvahutaḥ | ṛcassāmāni jajñire |",
     "chandāgṃsi jajñire tasmāt | yajustasmādajāyata ||"],
    ["manasaḥ kāmamākūtiṃ vācassatyamaśīmahi |",
     "paśūnāgṃ rūpamannasya mayi śrīśśrayatāṃ yaśaḥ ||"],
    ["hiraṇyahārakeyūragraiveyamaṇikaṅkaṇaiḥ |",
     "suhāraṃ bhūṣaṇairyuktaṃ gṛhāṇa puruṣottama ||"],
    "ābharaṇaṃ samarpayāmi",
    "Puruṣa Sūkta 10: “From that sacrifice, offered whole, the ṛcs and sāmans "
    "were born; the metres were born from it; from it the yajus arose.” Śrī "
    "Sūkta 10: “May we gain the mind's desire and intent, truth of speech; may "
    "the beauty of cattle and of food, fortune and fame rest in me.” With "
    "golden chains, armlets, necklaces and jewelled bracelets — accept these "
    "ornaments, Puruṣottama.")
S += _upa(
    "Puṣpam · flowers",
    ["oṃ tasmādaśvā ajāyanta | ye ke cobhayādataḥ |",
     "gāvo ha jajñire tasmāt | tasmājjātā ajāvayaḥ ||"],
    ["kardamena prajābhūtā mayi sambhava kardama |",
     "śriyaṃ vāsaya me kule mātaraṃ padmamālinīm ||"],
    ["mallikādisugandhīni mālatyādīni vai prabho |",
     "mayāhṛtāni pūjārthaṃ puṣpāṇi pratigṛhyatām ||"],
    "puṣpāṇi samarpayāmi",
    "Puruṣa Sūkta 11: “From it horses were born, and all with teeth in both "
    "jaws; from it cows were born, from it goats and sheep.” Śrī Sūkta 11: "
    "“Through Kardama she has offspring; Kardama, dwell with me, and settle in "
    "my family Śrī, the mother garlanded with lotuses.” Fragrant jasmine, "
    "mālatī and other flowers I have brought for your worship — accept them, "
    "Lord.")
S += [
    _h("Aṅgapūjā · worship of the limbs"),
    _p(["oṃ keśavāya namaḥ pādau pūjayāmi | oṃ govindāya namaḥ gulphau pūjayāmi |",
        "oṃ indirāpataye namaḥ jaṅghe pūjayāmi | oṃ anaghāya namaḥ jānunī pūjayāmi |",
        "oṃ janārdanāya namaḥ ūrū pūjayāmi | oṃ viṣṭaraśravase namaḥ kaṭiṃ pūjayāmi |",
        "oṃ kukṣisthākhilabhuvanāya namaḥ udaraṃ pūjayāmi |",
        "oṃ lakṣmīvakṣasthalālayāya namaḥ vakṣasthalaṃ pūjayāmi |",
        "oṃ śaṅkhacakragadāśārṅgapāṇaye namaḥ bāhūn pūjayāmi |",
        "oṃ kambukaṇṭhāya namaḥ kaṇṭhaṃ pūjayāmi |",
        "oṃ pūrṇendunibhavaktrāya namaḥ vaktraṃ pūjayāmi |",
        "oṃ kundakuṭmaladantāya namaḥ dantān pūjayāmi |",
        "oṃ nāsāgramauktikāya namaḥ nāsikāṃ pūjayāmi |",
        "oṃ sūryacandrāgnidhāriṇe namaḥ netre pūjayāmi |",
        "oṃ sahasraśirase namaḥ śiraḥ pūjayāmi |",
        "oṃ śrīsatyanārāyaṇasvāmine namaḥ sarvāṇyaṅgāni pūjayāmi ||",
        "śrīmadādyādi mahālakṣmīsameta śrīvīraveṅkaṭasatyanārāyaṇasvāmine namaḥ",
        "sarvāṇyaṅgāni pūjayāmi ||"],
       "I worship his feet as Keśava, ankles as Govinda, shanks as lord of "
       "Indirā, knees as the sinless, thighs as Janārdana, waist as "
       "Viṣṭaraśravas, belly as the one who holds all worlds within, chest as "
       "the one on whose breast Lakṣmī dwells, arms as bearer of conch, discus, "
       "mace and bow, throat as conch-necked, face as moon-faced, teeth as "
       "jasmine-bud-toothed, nose as the one with a pearl at its tip, eyes as "
       "bearer of sun, moon and fire, head as thousand-headed; and all his "
       "limbs as Śrī Satyanārāyaṇa."),
]

KRISHNA_108 = [
    "śrīkṛṣṇāya", "kamalānāthāya", "vāsudevāya", "sanātanāya", "vasudevātmajāya",
    "puṇyāya", "līlāmānuṣavigrahāya", "śrīvatsakaustubhadharāya", "yaśodāvatsalāya",
    "haraye", "caturbhujāttacakrāsigadāśaṅkhādyāyudhadharāya", "devakīnandanāya",
    "śrīśāya", "nandagopapriyātmajāya", "yamunāvegasaṃhāriṇe", "balabhadrapriyānujāya",
    "pūtanājīvitaharāya", "śakaṭāsurabhañjanāya", "nandavrajajanānandine",
    "saccidānandavigrahāya", "navanītaviliptāṅgāya", "navanītanaṭāya", "anaghāya",
    "navanītanavāhārāya", "mucukundaprasādakāya", "ṣoḍaśastrīsahasreśāya",
    "tribhaṅgine", "madhurākṛtaye", "śukavāgamṛtābdhīndave", "govindāya",
    "yogināmpataye", "vatsavāṭacarāya", "anantāya", "dhenukāsurabhañjanāya",
    "tṛṇīkṛtatṛṇāvartāya", "yamalārjunabhañjanāya", "uttālatālabhetre",
    "tamālaśyāmalākṛtaye", "gopagopīśvarāya", "yogine", "koṭisūryasamaprabhāya",
    "ilāpataye", "parañjyotiṣe", "yādavendrāya", "yadūdvahāya", "vanamāline",
    "pītavāsase", "pārijātāpahārakāya", "govardhanācaloddhartre", "gopālāya",
    "sarvapālakāya", "ajāya", "nirañjanāya", "kāmajanakāya", "kañjalocanāya",
    "madhughne", "madhurānāthāya", "dvārakānāyakāya", "baline",
    "bṛndāvanāntasañcāriṇe", "tulasīdāmabhūṣaṇāya", "śyamantakamaṇerhartre",
    "naranārāyaṇātmakāya", "kubjākṛṣṇāmbaradharāya", "māyine", "paramapuruṣāya",
    "muṣṭikāsuracāṇūramallayuddhaviśāradāya", "saṃsāravairiṇe", "kaṃsāraye",
    "murāraye", "narakāntakāya", "anādibrahmacāriṇe", "kṛṣṇāvyasanakarśakāya",
    "śiśupālaśiraśchetre", "duryodhanakulāntakāya", "vidurākrūravaradāya",
    "viśvarūpapradarśakāya", "satyavāce", "satyasaṅkalpāya", "satyabhāmāratāya",
    "jayine", "subhadrāpūrvajāya", "jiṣṇave", "bhīṣmamuktipradāyakāya",
    "jagadgurave", "jagannāthāya", "veṇunādaviśāradāya", "vṛṣabhāsuravidhvaṃsine",
    "bāṇāsurakarāntakāya", "yudhiṣṭhirapratiṣṭhātre", "barhibarhāvataṃsakāya",
    "pārthasārathaye", "avyaktagītāmṛtamahodadhaye",
    "kālīyaphaṇimāṇikyarañjitaśrīpadāmbujāya", "dāmodarāya", "yajñabhoktre",
    "dānavendravināśakāya", "nārāyaṇāya", "parabrahmaṇe", "pannagāśanavāhanāya",
    "jalakrīḍāsamāsaktagopīvastrāpahārakāya", "puṇyaślokāya", "tīrthapādāya",
    "vedavedyāya", "dayānidhaye", "sarvadevātmakāya", "sarvagraharūpiṇe",
    "parātparāya",
]

LAKSHMI_108 = [
    "prakṛtyai", "vikṛtyai", "vidyāyai", "sarvabhūtahitapradāyai", "śraddhāyai",
    "vibhūtyai", "surabhyai", "paramātmikāyai", "vāce", "padmālayāyai", "padmāyai",
    "śucaye", "svāhāyai", "svadhāyai", "sudhāyai", "dhanyāyai", "hiraṇmayyai",
    "lakṣmyai", "nityapuṣṭāyai", "vibhāvaryai", "adityai", "dityai", "dīptāyai",
    "vasudhāyai", "vasudhāriṇyai", "kamalāyai", "kāntāyai", "kāmākṣyai",
    "krodhasambhavāyai", "anugrahapradāyai", "buddhaye", "anaghāyai",
    "harivallabhāyai", "aśokāyai", "amṛtāyai", "dīptāyai", "lokaśokavināśinyai",
    "dharmanilayāyai", "karuṇāyai", "lokamātre", "padmapriyāyai", "padmahastāyai",
    "padmākṣyai", "padmasundaryai", "padmodbhavāyai", "padmamukhyai",
    "padmanābhapriyāyai", "ramāyai", "padmamālādharāyai", "devyai", "padminyai",
    "padmagandhinyai", "puṇyagandhāyai", "suprasannāyai", "prasādābhimukhyai",
    "prabhāyai", "candravadanāyai", "candrāyai", "candrasahodaryai", "caturbhujāyai",
    "candrarūpāyai", "indirāyai", "induśītalāyai", "āhlādajananyai", "puṣṭyai",
    "śivāyai", "śivakartryai", "satyai", "vimalāyai", "viśvajananyai", "tuṣṭaye",
    "dāridryanāśinyai", "prītipuṣkariṇyai", "śāntāyai", "śuklamālyāmbarāyai",
    "śriyai", "bhāskaryai", "bilvanilayāyai", "varārohāyai", "yaśasvinyai",
    "vasundharāyai", "udārāṅgāyai", "hariṇyai", "hemamālinyai",
    "dhanadhānyakartryai", "siddhaye", "straiṇasaumyāyai", "śubhapradāyai",
    "nṛpaveśmagatānandāyai", "varalakṣmyai", "vasupradāyai", "śubhāyai",
    "hiraṇyaprākārāyai", "samudratanayāyai", "jayāyai", "maṅgalāyai", "devyai",
    "viṣṇuvakṣasthalasthitāyai", "viṣṇupatnyai", "prasannākṣyai",
    "nārāyaṇasamāśritāyai", "dāridryadhvaṃsinyai", "sarvopadravavāriṇyai",
    "navadurgāyai", "mahākālyai", "brahmaviṣṇuśivātmikāyai",
    "trikālajñānasampannāyai", "bhuvaneśvaryai",
]
assert len(KRISHNA_108) == 108 and len(LAKSHMI_108) == 108

K_GLOSS = [
    "Names 1–12: Śrī Kṛṣṇa; lord of Kamalā; son of Vasudeva; the eternal; born "
    "of Vasudeva; the holy; who took a human form in play; bearer of the "
    "Śrīvatsa and Kaustubha; darling of Yaśodā; Hari; four-armed, bearing "
    "discus, sword, mace, conch and other weapons; joy of Devakī.",
    "13–24: lord of Śrī; beloved son of the cowherd Nanda; who checked the "
    "Yamunā's flood; dear younger brother of Balabhadra; who took the life of "
    "Pūtanā; breaker of the cart-demon; delight of the folk of Nanda's "
    "pasture; whose form is being, awareness and bliss; whose limbs are "
    "smeared with butter; who dances for butter; the sinless; whose fresh "
    "food is butter.",
    "25–36: who blessed Mucukunda; lord of the sixteen thousand wives; "
    "bent in three places; of charming form; the moon risen from the "
    "nectar-sea of Śuka's words; Govinda; lord of yogins; who roamed among "
    "the calves; the endless; slayer of Dhenuka; who made the whirlwind-demon "
    "as straw; breaker of the twin arjuna trees.",
    "37–48: who felled the tall palms; dark as the tamāla tree; lord of the "
    "cowherds and gopīs; the yogin; bright as ten million suns; lord of the "
    "earth; the supreme light; chief of the Yādavas; best of Yadu's line; "
    "wearing the forest garland; yellow-robed; who carried off the pārijāta "
    "tree.",
    "49–60: who lifted Govardhana hill; the cowherd; protector of all; the "
    "unborn; the stainless; father of Kāma; lotus-eyed; slayer of Madhu; lord "
    "of Mathurā; master of Dvārakā; the mighty; who wanders through "
    "Vṛndāvana.",
    "61–72: adorned with a garland of tulasī; who took the Syamantaka gem; "
    "whose self is Nara and Nārāyaṇa; who wore the garment offered by Kubjā; "
    "master of māyā; the supreme Person; skilled in wrestling Muṣṭika and "
    "Cāṇūra; enemy of worldly bondage; foe of Kaṃsa; foe of Mura; ender of "
    "Naraka; the beginningless celibate.",
    "73–84: who wore away Draupadī's distress; who cut off Śiśupāla's head; "
    "destroyer of Duryodhana's line; giver of boons to Vidura and Akrūra; who "
    "showed the cosmic form; truthful of speech; true of resolve; delighting "
    "in Satyabhāmā; the victorious; elder brother of Subhadrā; the conqueror; "
    "who granted liberation to Bhīṣma.",
    "85–96: teacher of the world; lord of the world; master of the flute's "
    "music; destroyer of the bull-demon; who cut off Bāṇa's arms; who "
    "established Yudhiṣṭhira; crowned with peacock feathers; charioteer of "
    "Arjuna; the unmanifest, great ocean of the Gītā's nectar; whose lotus "
    "feet are coloured by the gems of Kāliya's hoods; Dāmodara; enjoyer of "
    "sacrifice.",
    "97–108: destroyer of the dānava lords; Nārāyaṇa; the supreme Brahman; "
    "whose mount is the serpent-eater Garuḍa; who in water-play took the "
    "gopīs' clothes; of holy fame; whose feet are sacred; known through the "
    "Veda; treasure of compassion; whose self is all the gods; whose form is "
    "all the planets; higher than the highest.",
]

L_GLOSS = [
    "Names 1–12: Nature; its transformations; knowledge; who gives the good of "
    "all beings; faith; majesty; the wish-granting cow; the supreme Self; "
    "speech; dwelling in the lotus; the lotus; the pure.",
    "13–24: Svāhā; Svadhā; nectar; the blessed; golden; Lakṣmī; ever-"
    "nourishing; the radiant night; Aditi; Diti; the shining; the earth.",
    "25–36: upholder of the earth; Kamalā; the beloved; lovely-eyed; born of "
    "the churning's wrath; bestower of grace; wisdom; the sinless; dear to "
    "Hari; free of sorrow; immortal; the shining.",
    "37–48: destroyer of the world's sorrow; abode of dharma; compassion; "
    "mother of the world; fond of lotuses; lotus-handed; lotus-eyed; lovely as "
    "the lotus; lotus-born; lotus-faced; beloved of Padmanābha; Ramā.",
    "49–60: wearing a lotus garland; the Goddess; the lotus-lady; "
    "lotus-scented; of holy fragrance; well pleased; turned toward grace; "
    "radiance; moon-faced; the moon; sister of the moon; four-armed.",
    "61–72: moon-formed; Indirā; cool as the moon; giver of joy; nourishment; "
    "the auspicious; maker of welfare; the true; the spotless; mother of the "
    "universe; contentment; destroyer of poverty.",
    "73–84: lotus-pool of love; the peaceful; in white garland and robe; "
    "Śrī; the radiant; dwelling in the bilva; the fair-hipped; the glorious; "
    "the earth; of noble limbs; the doe; garlanded with gold.",
    "85–96: giver of wealth and grain; perfection; gentle in womanly grace; "
    "giver of good; the joy that enters royal palaces; Varalakṣmī; giver of "
    "riches; the good; walled in gold; daughter of the ocean; victory; the "
    "auspicious.",
    "97–108: the Goddess; dwelling on Viṣṇu's breast; Viṣṇu's consort; "
    "clear-eyed; refuge of Nārāyaṇa; destroyer of poverty; warder-off of all "
    "calamity; the ninefold Durgā; Mahākālī; whose self is Brahmā, Viṣṇu and "
    "Śiva; possessed of knowledge of the three times; queen of the worlds.",
]

S += [_h("Aṣṭottaraśatanāma Pūjā · the hundred and eight names")]
S += [_names(c, g) for c, g in zip(_chunks(KRISHNA_108, 12), K_GLOSS)]
S += [_v(["oṃ śrīsatyanārāyaṇaparabrahmaṇe namaḥ ||"],
         "Salutation to Śrī Satyanārāyaṇa, the supreme Brahman.")]
S += [_r("With the following names, worship with turmeric and kuṅkuma "
         "(the hundred and eight names of Lakṣmī).")]
S += [_names(c, g) for c, g in zip(_chunks(LAKSHMI_108, 12), L_GLOSS)]
S += [_v([f"{SN} nānāvidhaparimalapuṣpāṇi samarpayāmi ||"],
         "I offer flowers of many fragrances.")]

S += _upa(
    "Dhūpam · incense",
    ["oṃ yatpuruṣaṃ vyadadhuḥ | katidhā vyakalpayan |",
     "mukhaṃ kimasya kau bāhū | kāvūrū pādāvucyete ||"],
    ["āpassṛjantu snigdhāni ciklīta vasa me gṛhe |",
     "ni ca devīṃ mātaraṃ śriyaṃ vāsaya me kule ||"],
    ["vanaspatirasodbhūtaiścandanāgarusaṃyutaiḥ |",
     "āghreyassarvadevānāṃ dhūpo'yaṃ pratigṛhyatām ||",
     "daśāṅgaṃ guggulūpetaṃ sugandhaṃ sumanoharam |",
     "dhūpaṃ gṛhāṇa deveśa sarvadevanamaskṛta ||"],
    "dhūpamāghrāpayāmi",
    "Puruṣa Sūkta 12: “When they divided the Puruṣa, into how many parts did "
    "they arrange him? What was his mouth, what his arms, what are his thighs "
    "and feet called?” Śrī Sūkta 12: “May the waters bring forth smooth things; "
    "Ciklīta, dwell in my house, and settle the divine mother Śrī in my "
    "family.” Made of the saps of trees, with sandal and aloe, fit to be "
    "smelled by all the gods — accept this incense; accept the tenfold "
    "fragrant incense with guggulu, O lord saluted by all the gods.")
S += _upa(
    "Dīpam · lamp",
    ["oṃ brāhmaṇo'sya mukhamāsīt | bāhū rājanyaḥ kṛtaḥ |",
     "ūrū tadasya yadvaiśyaḥ | padbhyāgṃ śūdro ajāyata ||"],
    ["ārdrāṃ puṣkariṇīṃ puṣṭiṃ suvarṇāṃ hemamālinīm |",
     "sūryāṃ hiraṇmayīṃ lakṣmīṃ jātavedo mamāvaha ||"],
    ["sājyaṃ trivartisaṃyuktaṃ vahninā yojitaṃ priyam |",
     "gṛhāṇa maṅgalaṃ dīpaṃ trailokyatimirāpaha ||",
     "bhaktyā dīpaṃ prayacchāmi devāya paramātmane |",
     "trāhi māṃ narakādghorāddivyajyotirnamo'stu te ||",
     "ghṛtāktavartisaṃyuktaṃ vahninā yojitaṃ priyam |",
     "dīpaṃ gṛhāṇa deveśa trailokyatimirāpaham ||"],
    "dīpaṃ darśayāmi",
    "Puruṣa Sūkta 13: “The brāhmaṇa was his mouth, the warrior was made his "
    "arms, his thighs the vaiśya; from his feet the śūdra was born.” Śrī Sūkta: "
    "“Bring me, Jātavedas, Lakṣmī — moist, lotus-pool, nourishing, golden, "
    "garlanded with gold, sun-like, made of gold.” The auspicious lamp with "
    "ghee and triple wick — accept it, dispeller of the three worlds' "
    "darkness; save me from dreadful hell, divine light; accept this lamp of "
    "ghee-soaked wicks.")
S += [
    _h("Naivedyam · food offering"),
    _v(["oṃ candramā manaso jātaḥ | cakṣossūryo ajāyata |",
        "mukhādindraścāgniśca | prāṇādvāyurajāyata ||",
        "ārdrāṃ yaḥ kariṇīṃ yaṣṭiṃ piṅgalāṃ padmamālinīm |",
        "candrāṃ hiraṇmayīṃ lakṣmīṃ jātavedo mamāvaha ||",
        "sauvarṇe sthālimadhye maṇigaṇakhacite goghṛtāktān supakvān",
        "bhakṣyān bhojyāṃśca lehyānaparimitarasāñcoṣyamannaṃ nidhāya |",
        "nānāśākairupetaṃ dadhimadhusaguḍakṣīrapānīyayuktaṃ",
        "tāmbūlaṃ cāpi viṣṇo pratidivasamahaṃ mānase kalpayāmi ||",
        "rājānnaṃ sūpasaṃyuktaṃ śākacoṣyasamanvitam |",
        "ghṛtabhakṣyasamāyuktaṃ naivedyaṃ pratigṛhyatām ||"],
       "Puruṣa Sūkta 14: “The moon was born from his mind, from his eye the sun; "
       "from his mouth Indra and Agni, from his breath the wind.” Śrī Sūkta: "
       "“… moist, active, the staff, tawny, garlanded with lotuses, moon-like, "
       "made of gold.” Daily in my mind, Viṣṇu, I set on a golden plate studded "
       "with gems well-cooked foods soaked in cow's ghee — things to chew, eat, "
       "lick and suck, of countless flavours, with rice and many vegetables, "
       "curd, honey, jaggery, milk and water, and betel too. Accept this "
       "offering of fine rice with dal, vegetables and ghee-cooked sweets."),
    _p(["oṃ bhūrbhuvassuvaḥ | oṃ tatsaviturvareṇyaṃ bhargo devasya dhīmahi | dhiyo yo naḥ pracodayāt ||",
        "satyaṃ tvartena pariṣiñcāmi | amṛtamastu | amṛtopastaraṇamasi |",
        "oṃ prāṇāya svāhā | oṃ apānāya svāhā | oṃ vyānāya svāhā |",
        "oṃ udānāya svāhā | oṃ samānāya svāhā | oṃ brahmaṇe svāhā |",
        f"{SN} mahānaivedyaṃ samarpayāmi |",
        "amṛtāpidhānamasi | uttarāpośanaṃ samarpayāmi |",
        "hastau prakṣālayāmi | pādau prakṣālayāmi | śuddhācamanīyaṃ samarpayāmi ||"],
       "After the Gāyatrī the offering is sprinkled round and made over to "
       "the five breaths and to Brahman; the great food-offering is presented, "
       "then the closing sip, and water for washing hands and feet and for "
       "sipping."),
]
S += _upa(
    "Tāmbūlam · betel",
    ["oṃ nābhyā āsīdantarikṣam | śīrṣṇo dyaussamavartata |",
     "padbhyāṃ bhūmirdiśaśśrotrāt | tathā lokāgṃ akalpayan ||"],
    ["tāṃ ma āvaha jātavedo lakṣmīmanapagāminīm |",
     "yasyāṃ hiraṇyaṃ prabhūtaṃ gāvo dāsyo'śvān vindeyaṃ puruṣānaham ||"],
    ["pūgīphalaissakarpūrairnāgavallīdalairyutam |",
     "muktācūrṇasamāyuktaṃ tāmbūlaṃ pratigṛhyatām ||"],
    "tāmbūlaṃ samarpayāmi",
    "Puruṣa Sūkta 15: “From his navel came the mid-air; from his head the sky "
    "came forth; from his feet the earth, from his ear the quarters: so they "
    "fashioned the worlds.” Śrī Sūkta 15: “Bring me, Jātavedas, that Lakṣmī "
    "who does not depart, in whom I may find abundant gold, cattle, servants, "
    "horses and people.” Accept this betel with areca, camphor and pearl-lime.")
S += [
    _h("Nīrājanam · waving of lights"),
    _v(["oṃ vedāhametaṃ puruṣaṃ mahāntam | ādityavarṇaṃ tamasastu pāre |",
        "sarvāṇi rūpāṇi vicitya dhīraḥ | nāmāni kṛtvā'bhivadan yadāste ||",
        "hiraṇyapātraṃ madhoḥ pūrṇaṃ dadāti madhavyo'sānīti |",
        "ekadhā brahmaṇa upaharati | ekadhaiva yajamāna āyustejo dadhāti ||",
        "yaśśuciḥ prayato bhūtvā juhuyādājyamanvaham |",
        "śriyaḥ pañcadaśarcaṃ ca śrīkāmassatataṃ japet ||",
        "caturvartisamāyuktaṃ goghṛtena supūritam |",
        "nīrājanena santuṣṭo bhavatveva jagatpatiḥ ||",
        f"{SN} karpūranīrājanaṃ darśayāmi ||"],
       "Puruṣa Sūkta 16: “I know this great Puruṣa, sun-coloured, beyond the "
       "darkness; the wise one who, having fashioned all forms and given them "
       "names, dwells calling them.” He gives a golden vessel full of honey, "
       "thinking, may I be rich in sweetness; he offers it whole to the "
       "brahmin, and wholly the sacrificer gains life and lustre. Whoever, "
       "pure and restrained, offers ghee daily and, desiring fortune, "
       "constantly recites the fifteen verses of Śrī. With four wicks filled "
       "with cow's ghee — may the lord of the world be pleased by this waving "
       "of lights."),
    _p(["narya prajāṃ me gopāya | amṛtatvāya jīvase | jātāṃ janiṣyamāṇāṃ ca | amṛte satye pratiṣṭhitām |",
        "atharva pituṃ me gopāya | rasamannamihāyuṣe | adabdhāyo'śītatano | aviṣaṃ naḥ pituṃ kṛṇu |",
        "śagṃsya paśūnme gopāya | dvipādo ye catuṣpadaḥ | aṣṭāśaphāśca ya ihāgne | ye caikaśaphā āśugāḥ |",
        "saprātha sabhāṃ me gopāya | ye ca sabhyāssabhāsadaḥ | tānindriyāvataḥ kuru | sarvamāyurupāsatām |",
        "ahe budhniya mantraṃ me gopāya | yamṛṣayastraividā viduḥ | ṛcassāmāni yajūgṃṣi | sā hi śrīramṛtā satām |",
        "mā no higṃsījjātavedaḥ | gāmaśvaṃ puruṣaṃ jagat | abibhradagna āgahi | śriyā mā paripātaya ||",
        "samrājaṃ ca virājaṃ cābhiśrīryā ca no gṛhe |",
        "lakṣmī rāṣṭrasya yā mukhe tayā mā sagṃsṛjāmasi ||",
        "santataśrīrastu | sarvamaṅgalāni bhavantu | nityaśrīrastu | nityamaṅgalāni bhavantu ||"],
       "O manly one, guard my offspring, born and yet to be born, for "
       "immortality and life, established in the immortal truth. Atharvan, "
       "guard my food, the savoury nourishment here, for long life; unharmed "
       "one, of unfevered body, make our food free of poison. Praiseworthy "
       "one, guard my cattle, two-footed and four-footed, cloven-hoofed and "
       "whole-hoofed. Far-reaching one, guard my assembly and those who sit in "
       "it; make them strong of sense, and let them attain full life. Ahi "
       "Budhnya, guard my mantra, which the seers of the three Vedas know — "
       "ṛc, sāman and yajus; for that is the immortal fortune of the good. "
       "Jātavedas, harm not our cows, horses, people or world; come, Agni, "
       "without hostility, and guard me with fortune. The sovereign, the "
       "far-ruling, the fortune that is in our house, the Lakṣmī at the head of "
       "the realm — with her we unite ourselves. May fortune be unceasing, all "
       "blessings be; may fortune be constant, blessings be constant."),
    _v(["nīrājanaṃ gṛhāṇedaṃ pañcavartisamanvitam |",
        "tejorāśimayaṃ dattaṃ gṛhāṇa tvaṃ sureśvara ||",
        f"{SN} karpūranīrājanaṃ samarpayāmi ||"],
       "Accept this waving of five-wicked lights, a mass of radiance given to "
       "you, lord of gods. — I offer the camphor light."),
    _h("Mantrapuṣpam · the flower of mantra"),
    _v(["oṃ dhātā purastādyamudājahāra | śakraḥ pravidvānpradiśaścatasraḥ |",
        "tamevaṃ vidvānamṛta iha bhavati | nānyaḥ panthā ayanāya vidyate ||"],
       "He whom the Creator proclaimed in the beginning, whom Indra knew in all "
       "four quarters — one who knows him thus becomes immortal here; there is "
       "no other path to go."),
    _v(["oṃ sahasraśīrṣaṃ devaṃ viśvākṣaṃ viśvaśambhuvam |",
        "viśvaṃ nārāyaṇaṃ devamakṣaraṃ paramaṃ padam ||",
        "viśvataḥ paramānnityaṃ viśvaṃ nārāyaṇagṃ harim |",
        "viśvamevedaṃ puruṣastadviśvamupajīvati ||",
        "patiṃ viśvasyātmeśvaragṃ śāśvatagṃ śivamacyutam |",
        "nārāyaṇaṃ mahājñeyaṃ viśvātmānaṃ parāyaṇam ||",
        "nārāyaṇa paro jyotirātmā nārāyaṇaḥ paraḥ |",
        "nārāyaṇa paraṃ brahma tattvaṃ nārāyaṇaḥ paraḥ |",
        "nārāyaṇa paro dhyātā dhyānaṃ nārāyaṇaḥ paraḥ ||",
        "yacca kiñcijjagatsarvaṃ dṛśyate śrūyate'pi vā |",
        "antarbahiśca tatsarvaṃ vyāpya nārāyaṇassthitaḥ ||"],
       "Nārāyaṇa Sūkta: the thousand-headed god, all-eyed, source of all "
       "happiness, the All, god Nārāyaṇa, the imperishable, the highest state; "
       "eternal, beyond the universe, the universe itself, Nārāyaṇa, Hari. The "
       "Person is all this universe; the universe lives on him. Lord of the "
       "universe, lord of selves, eternal, auspicious, unfailing, Nārāyaṇa, the "
       "great object of knowledge, the Self of all, the final refuge. Nārāyaṇa "
       "is the supreme light, the supreme Self, the supreme Brahman, the "
       "supreme reality; Nārāyaṇa is the supreme meditator and the supreme "
       "meditation. Whatever in the world is seen or heard, pervading all of "
       "it within and without, Nārāyaṇa stands."),
    _v(["anantamavyayaṃ kavigṃ samudre'ntaṃ viśvaśambhuvam |",
        "padmakośapratīkāśagṃ hṛdayaṃ cāpyadhomukham ||",
        "adho niṣṭyā vitastyānte nābhyāmupari tiṣṭhati |",
        "jvālamālākulaṃ bhāti viśvasyāyatanaṃ mahat ||",
        "santatagṃ śilābhistu lambatyākośasannibham |",
        "tasyānte suṣiragṃ sūkṣmaṃ tasminsarvaṃ pratiṣṭhitam ||",
        "tasya madhye mahānagnirviśvārcirviśvatomukhaḥ |",
        "so'grabhugvibhajantiṣṭhannāhāramajaraḥ kaviḥ ||",
        "tiryagūrdhvamadhaśśāyī raśmayastasya santatā |",
        "santāpayati svaṃ dehamāpādatalamastakam |",
        "tasya madhye vahniśikhā aṇīyordhvā vyavasthitā ||",
        "nīlatoyadamadhyasthādvidyullekheva bhāsvarā |",
        "nīvāraśūkavattanvī pītā bhāsvatyaṇūpamā ||",
        "tasyāśśikhāyā madhye paramātmā vyavasthitaḥ |",
        "sa brahma sa śivassa harissendrassokṣaraḥ paramassvarāṭ ||"],
       "The endless, imperishable seer, the goal of the ocean of existence, "
       "source of all happiness — the heart, like a lotus bud hanging "
       "downward, a span below the throat and above the navel, shines wreathed "
       "in flames, the great dwelling of the universe. Surrounded by nerves, it "
       "hangs like a lotus bud; within it is a subtle space in which all is "
       "established. In its midst is a great fire, all-radiant, facing every "
       "way, which eats first, dividing the food, unaging, the seer; its rays "
       "spread across, above and below, warming its body from sole to crown. "
       "In its centre stands a tongue of flame, very subtle, rising upward, "
       "shining like lightning in the middle of a dark rain-cloud, slender as "
       "the awn of wild rice, golden, radiant, subtle beyond compare. In the "
       "midst of that flame dwells the supreme Self: he is Brahmā, he is Śiva, "
       "he is Hari, he is Indra; he is the imperishable, supreme, self-luminous."),
    _v(["oṃ rājādhirājāya prasahyasāhine | namo vayaṃ vaiśravaṇāya kurmahe |",
        "sa me kāmānkāmakāmāya mahyam | kāmeśvaro vaiśravaṇo dadātu |",
        "kuberāya vaiśravaṇāya | mahārājāya namaḥ ||",
        "tadviṣṇoḥ paramaṃ padagṃ sadā paśyanti sūrayaḥ | divīva cakṣurātatam |",
        "tadviprāso vipanyavo jāgṛvāgṃsassamindhate | viṣṇoryatparamaṃ padam ||",
        f"{SN} suvarṇamantrapuṣpaṃ samarpayāmi ||"],
       "To the king of kings, who conquers by force, to Vaiśravaṇa we pay "
       "homage; may he, the lord of desires, Vaiśravaṇa, grant desires to me "
       "who desire. Salutation to Kubera Vaiśravaṇa, the great king. That "
       "highest step of Viṣṇu the wise ever behold, like an eye spread across "
       "the sky; that the sages, wakeful and eloquent, kindle — the highest "
       "step of Viṣṇu. — I offer the golden flower of mantra."),
    _h("Pradakṣiṇa Namaskārāḥ · circumambulation"),
    _v(["yāni kāni ca pāpāni janmāntarakṛtāni ca |",
        "tāni tāni praṇaśyanti pradakṣiṇapade pade ||",
        "pāpo'haṃ pāpakarmā'haṃ pāpātmā pāpasambhavaḥ |",
        "trāhi māṃ kṛpayā deva śaraṇāgatavatsala ||",
        "anyathā śaraṇaṃ nāsti tvameva śaraṇaṃ mama |",
        "tasmātkāruṇyabhāvena rakṣa rakṣa janārdana ||",
        "pradakṣiṇaṃ kariṣyāmi sarvabhramanivāraṇam |",
        "saṃsārasāgarānmāṃ tvamuddharasva mahāprabho ||",
        f"{SN} pradakṣiṇanamaskārān samarpayāmi ||"],
       "Whatever sins were done, in this and other births, perish at every "
       "step of the circling. I am sinful, my deeds are sinful, my self is "
       "sinful, born of sin: save me in your mercy, Lord, kind to those who "
       "seek refuge. I have no other refuge; you alone are my refuge — so, "
       "out of compassion, protect me, protect me, Janārdana. I will circle "
       "you, which removes all delusion; lift me out of the ocean of worldly "
       "life, great Lord."),
    _p(["chatraṃ samarpayāmi | cāmaraṃ samarpayāmi | gītaṃ śrāvayāmi |",
        "nṛtyaṃ darśayāmi | nāṭyaṃ samarpayāmi | samastarājopacārān samarpayāmi ||"],
       "I offer the royal parasol and the fly-whisk; I sing to you, show you "
       "dance and drama, and offer all the honours due to a king."),
    _h("Prārthanā · prayer"),
    _v(["amoghaṃ puṇḍarīkākṣaṃ nṛsiṃhaṃ daityasūdanam |",
        "hṛṣīkeśaṃ jagannāthaṃ vāgīśaṃ varadāyakam ||",
        "saguṇaṃ ca guṇātītaṃ govindaṃ garuḍadhvajam |",
        "janārdanaṃ janānandaṃ jānakīvallabhaṃ harim ||",
        "praṇamāmi sadā bhaktyā nārāyaṇamajaṃ param |",
        "durgame viṣame ghore śatruṇā paripīḍite ||",
        "nistārayatu sarveṣu tathāniṣṭabhayeṣu ca |",
        "nāmānyetāni saṅkīrtya phalamīpsitamāpnuyāt ||",
        "satyanārāyaṇaṃ devaṃ vande'haṃ kāmadaṃ prabhum |",
        "līlayā vitataṃ viśvaṃ yena tasmai namo namaḥ ||",
        f"{SN} prārthanānamaskārān samarpayāmi ||"],
       "The unfailing, the lotus-eyed, Nṛsiṃha, slayer of daityas, Hṛṣīkeśa, "
       "lord of the world, master of speech, giver of boons; with qualities "
       "and beyond them, Govinda, whose banner bears Garuḍa, Janārdana, joy of "
       "the people, beloved of Jānakī, Hari — to Nārāyaṇa, unborn and supreme, "
       "I ever bow with devotion. In hard, rough and dreadful straits, when "
       "pressed by an enemy, and in every dread of harm, may he carry one "
       "through; singing these names one gains the fruit one seeks. I bow to "
       "the god Satyanārāyaṇa, the lord who grants desires, by whom the "
       "universe was spread out in play: to him, salutation again and again."),
    _v(["idaṃ phalaṃ mayā deva sthāpitaṃ puratastava |",
        "tena me saphalāvāptirbhavejjanmani janmani ||",
        "śrīsatyanārāyaṇasvāmine namaḥ phalaṃ samarpayāmi ||"],
       "This fruit, O God, I have set before you; by it may I gain fulfilment "
       "in birth after birth. — I offer fruit."),
    _v(["yasya smṛtyā ca nāmoktyā tapaḥpūjākriyādiṣu |",
        "nyūnaṃ sampūrṇatāṃ yāti sadyo vande tamacyutam ||",
        "mantrahīnaṃ kriyāhīnaṃ bhaktihīnaṃ janārdana |",
        "yatpūjitaṃ mayā deva paripūrṇaṃ tadastu te ||"],
       "I bow to Acyuta, by remembering whom and speaking whose name whatever "
       "is lacking in austerity, worship and rite at once becomes complete. "
       "Lacking in mantra, in rite, in devotion — whatever worship I have done, "
       "Janārdana, may it be made complete for you."),
    _p(["anayā dhyānāvāhanādiṣoḍaśopacārapūjayā ca bhagavān sarvātmakaḥ",
        "ādyādi mahālakṣmīsameta śrīvīraveṅkaṭasatyanārāyaṇasvāmī suprīto varado bhavatu ||",
        "ādyādi mahālakṣmīsameta śrīvīraveṅkaṭasatyanārāyaṇasvāmiprasādaṃ śirasā gṛhṇāmi ||"],
       "By this sixteen-fold worship may the Lord, the Self of all, Śrī Vīra "
       "Veṅkaṭa Satyanārāyaṇa Svāmi with Ādyā Mahālakṣmī, be well pleased and "
       "grant boons. I receive his grace upon my head."),
]

# ───────────────────────── the vrata-kathā ─────────────────────────
S += [
    "ornament",
    _h("Śrī Satyanārāyaṇa Vratakathā"),
    _r("The kathā is heard after the pūjā, holding akṣata, which are offered "
       "to the Lord at the close of each chapter."),

    # ── Chapter 1 ──
    _h("Prathamo'dhyāyaḥ · Chapter One"),
    _v(["ekadā naimiśāraṇye ṛṣayaśśaunakādayaḥ |",
        "papracchurānataṃ sarve sūtaṃ paurāṇikaṃ khalu ||",
        "vratena tapasā kiṃ vā prāpyate vāñchitaṃ phalam |",
        "tatsarvaṃ śrotumicchāmaḥ kathayasva mahāmune ||"],
       "Once, in the Naimiśa forest, Śaunaka and the other sages all questioned "
       "Sūta, the teller of the Purāṇas, who bowed before them: “By what vow or "
       "austerity is the fruit one longs for obtained? We wish to hear all of "
       "it; tell us, great sage.”"),
    _v(["sūtovāca —",
        "nāradenaiva sampṛṣṭo bhagavān kamalāpatiḥ |",
        "surarṣaye yathaivāha tacchṛṇudhvaṃ samāhitāḥ ||"],
       "Sūta said: “When Nārada asked this very question, the Lord, husband of "
       "Kamalā, answered the divine sage. Hear it as he told it, with attentive "
       "minds.”"),
    _v(["ekadā nārado yogī parānugrahakāṅkṣayā |",
        "paryaṭan vividhān lokān martyalokamupāgataḥ ||",
        "tatra dṛṣṭvā janān sarvān nānākleśasamanvitān |",
        "nānāyonisamutpannān kliśyamānān svakarmabhiḥ ||",
        "kenopāyena caiteṣāṃ duḥkhanāśo bhaviṣyati |",
        "iti sañcintya manasā viṣṇulokaṃ gatastadā ||"],
       "Once the yogin Nārada, wishing to help others, wandered through the "
       "many worlds and came to the world of mortals. There he saw all the "
       "people beset by many troubles, born in many kinds of wombs, suffering "
       "through their own deeds. Thinking, “By what means will their sorrow be "
       "ended?”, he went to the world of Viṣṇu."),
    _v(["tatra nārāyaṇaṃ devaṃ śuklavarṇaṃ caturbhujam |",
        "śaṅkhacakragadāpadmavanamālāvibhūṣitam |",
        "dṛṣṭvā taṃ devadeveśaṃ stotuṃ samupacakrame ||"],
       "There he saw the god Nārāyaṇa, white of hue, four-armed, adorned with "
       "conch, discus, mace, lotus and the forest garland; seeing that lord of "
       "the gods, he began to praise him."),
    _v(["namo vāṅmanasātītarūpāyāmitaśaktaye |",
        "ādimadhyāntahīnāya nirguṇāya guṇātmane |",
        "sarveṣāmādibhūtāya bhaktānāmārtināśine ||"],
       "“Salutation to you, whose form is beyond speech and mind, of boundless "
       "power, without beginning, middle or end, beyond qualities yet the self "
       "of qualities, the origin of all, destroyer of your devotees' "
       "distress.”"),
    _v(["śrutvā stotraṃ tato viṣṇurnāradaṃ pratyabhāṣata ||",
        "śrībhagavānuvāca —",
        "kimarthamāgato'si tvaṃ kiṃ te manasi vartate |",
        "kathayasva mahābhāga tatsarvaṃ kathayāmi te ||"],
       "Hearing the hymn, Viṣṇu replied to Nārada. The Lord said: “Why have you "
       "come? What is in your mind? Tell me, fortunate one, and I will tell you "
       "all.”"),
    _v(["nārada uvāca —",
        "martyaloke janāssarve nānākleśasamanvitāḥ |",
        "nānāyonisamutpannāḥ pacyante pāpakarmabhiḥ ||",
        "tatkathaṃ śamayennātha laghūpāyena tadvada |",
        "śrotumicchāmi tatsarvaṃ kṛpāsti yadi te mayi ||"],
       "Nārada said: “In the world of mortals all people are beset by many "
       "troubles; born in many kinds of wombs, they are tormented by their sinful "
       "deeds. How, Lord, may that be quieted by some easy means? Tell me; I "
       "wish to hear it all, if you have compassion for me.”"),
    _v(["śrībhagavānuvāca —",
        "sādhu pṛṣṭaṃ tvayā vatsa lokānugrahakāṅkṣayā |",
        "yatkṛtvā mucyate mohāttacchṛṇuṣva vadāmi te ||",
        "vratamasti mahāpuṇyaṃ svargamartyeṣu durlabham |",
        "tava snehānmayā vatsa prakāśaḥ kriyate'dhunā ||",
        "satyanārāyaṇasyedaṃ vrataṃ samyagvidhānataḥ |",
        "kṛtvā sadyassukhaṃ bhuktvā cāmuṣminmokṣamāpnuyāt ||"],
       "The Lord said: “Well asked, my child, out of a wish to help the world. "
       "Hear what I tell you, by doing which one is freed from delusion. There "
       "is a vow of great merit, rare in heaven and on earth; out of love for "
       "you, child, I now make it known. This is the vow of Satyanārāyaṇa: "
       "keeping it duly, one enjoys happiness at once and gains liberation in "
       "the world beyond.”"),
    _v(["nārada uvāca —",
        "tacchrutvā bhagavadvākyaṃ nārado munirabravīt |",
        "kiṃ phalaṃ kiṃ vidhānaṃ ca kṛtaṃ kenaiva tadvratam |",
        "tatsarvaṃ vistarādbrūhi kathaṃ kāryaṃ ca tadvratam ||"],
       "Hearing the Lord's words the sage Nārada said: “What is its fruit, what "
       "its method? Who has kept this vow? Tell me all of it in detail, and how "
       "the vow is to be kept.”"),
    _v(["śrībhagavānuvāca —",
        "duḥkhaśokādiśamanaṃ dhanadhānyavivardhanam |",
        "saubhāgyasantatikaraṃ sarvatra vijayapradam ||",
        "māghe vā mādhave māsi kārtike vā śubhe dine |",
        "saṅgrāmārambhavelāyāṃ yadā kleśasya sambhavaḥ |",
        "dāridryaśamanārthaṃ ca vrataṃ kāryaṃ varepsubhiḥ ||"],
       "The Lord said: “It quiets sorrow and grief, increases wealth and grain, "
       "brings good fortune and offspring, and gives victory everywhere. In "
       "Māgha, Vaiśākha or Kārttika, on an auspicious day; at the outset of a "
       "conflict; whenever trouble arises; and to end poverty — the vow should "
       "be kept by those who seek blessings.”"),
    _v(["māse māse ca kartavyaṃ varṣe varṣe'thavā punaḥ |",
        "kartavyatāsti he vipra yathāvibhavasārataḥ ||"],
       "“It may be done every month, or again every year; it is to be done, O "
       "brahmin, according to one's means.”"),
    _v(["ekādaśyāṃ pūrṇimāyāṃ ravisaṅkramaṇe'pi vā |",
        "vrataṃ kāryaṃ muniśreṣṭha satyanārāyaṇasya hi ||",
        "prātarutthāya niyato dantadhāvanapūrvakam |",
        "nityakarma vidhāyādāvevaṃ saṅkalpayennaraḥ ||",
        "bhagavandevadeveśa satyanārāyaṇa vratam |",
        "tvatpriyārthaṃ kariṣyāmi prasīda kamalāpate ||"],
       "“On Ekādaśī, on the full moon, or when the sun enters a sign, best of "
       "sages, the vow of Satyanārāyaṇa should be kept. Rising at dawn, "
       "self-controlled, cleaning the teeth and doing the daily rites first, a "
       "person should resolve thus: ‘Lord, god of gods, Satyanārāyaṇa, I will "
       "keep your vow for your pleasure; be gracious, husband of Kamalā.’”"),
    _v(["evaṃ saṅkalpya madhyāhne kṛtvā mādhyāhnikīḥ kriyāḥ |",
        "sāyaṅkāle punassnātvā yajeddevaṃ niśāmukhe ||",
        "pūjāgṛhaṃ samāsādya nānālaṅkāraśobhitam |",
        "pūjāsthānaviśuddhyarthaṃ gomayena vilepayet ||",
        "tataḥ pañcavidhaiścūrṇai raṅgavallīṃ prakalpayet |",
        "tasyopari nyasedvastraṃ sadaśaṃ nūtanaṃ dṛḍham ||",
        "taṇḍulaṃ tatra vinyasya tanmadhye kalaśaṃ nyaset |",
        "rājataṃ vā'thavā tāmramārakūṭena nirmitam ||",
        "dravyābhāve mārtikaṃ vā vittaśāṭhyaṃ na kārayet |",
        "tasyopari nyasedvastraṃ sadaśaṃ nūtanaṃ dṛḍham ||"],
       "“Having so resolved, and done the midday rites at noon, one should "
       "bathe again in the evening and worship the god at nightfall. Coming to "
       "the place of worship, adorned with many ornaments, one should smear it "
       "with cow-dung to purify it, draw a rangoli with five kinds of powder, "
       "and spread on it a new, strong, bordered cloth. Placing rice there, one "
       "should set a vessel in its midst — of silver, copper or brass, or, "
       "lacking means, of clay; but one should not be miserly with one's "
       "wealth — and spread on it a new, strong, bordered cloth.”"),
    _v(["tasyopari nyaseddevaṃ satyanārāyaṇaṃ prabhum |",
        "karṣamātrasuvarṇena tadardhārdhena vā punaḥ ||",
        "pratimāṃ kārayedvipra satyadevasya satpateḥ |",
        "pañcāmṛtena susnātaṃ maṇṭapopari vinyaset ||"],
       "“On it one should place the Lord Satyanārāyaṇa. One should have an "
       "image made of Satyadeva, lord of the good, with a karṣa of gold, or a "
       "half, or a quarter of that, O brahmin; bathed well in the five nectars, "
       "it is set upon the maṇḍapa.”"),
    _v(["vighneśaḥ padmajā viṣṇurmahādevaśca pārvatī |",
        "ādityādigrahāssarve śakrādyaṣṭadigīśvarāḥ |",
        "atrāṅgadevatāḥ proktāstasmādagre prapūjayet ||",
        "agrataḥ kalaśe devaṃ varuṇaṃ pṛthagarcayet ||"],
       "“Gaṇeśa, Lakṣmī, Viṣṇu, Mahādeva and Pārvatī, all the planets beginning "
       "with the Sun, and the eight guardians of the quarters beginning with "
       "Indra — these are declared the attendant deities here, so they should "
       "be worshipped first. Before them, one should worship Varuṇa separately "
       "in the vessel.”"),
    _v(["gaṇeśaprabhṛtīnpañca kalaśasyottare nyaset |",
        "udaksamāptyā saṃsthāpya pūjanīyāḥ prayatnataḥ ||",
        "pūrvādidikṣu cendrādīnpūjayecchuddhamānasaḥ |",
        "tato nārāyaṇaṃ devaṃ kalaśe pūjayetsudhīḥ ||"],
       "“The five beginning with Gaṇeśa are placed north of the vessel, set in "
       "a row ending toward the north, and worshipped with care. With a pure "
       "mind one should worship Indra and the others in the eastern and other "
       "quarters; then the wise one should worship the god Nārāyaṇa on the "
       "vessel.”"),
    _v(["cāturvarṇyairvrataṃ kāryaṃ strībhirvāpi munīśvara |",
        "paurāṇikairvaidikaiśca mantrairbrāhmaṇasattamaḥ ||",
        "kalpoktavidhinā kuryātsatyadevasya pūjanam |",
        "paurāṇikaireva mantraiḥ kuryātpūjāṃ dvijetaraḥ ||"],
       "“The vow may be kept by people of all four classes, and by women too, "
       "lord of sages. The best of brahmins should worship Satyadeva by the "
       "method of the ritual manual, with Purāṇic and Vedic mantras; others "
       "should worship with Purāṇic mantras alone.”"),
    _v(["yasminkasmindine martyo bhaktiśraddhāsamanvitaḥ |",
        "satyanārāyaṇaṃ devaṃ yajeccaivaṃ niśāmukhe ||"],
       "“On any day at all, a mortal endowed with devotion and faith should "
       "worship the god Satyanārāyaṇa thus at nightfall.”"),
    _v(["brāhmaṇairbāndhavaiścaiva sahito dharmatatparaḥ |",
        "naivedyaṃ bhaktito dadyātprasādaṃ bhakṣyamuttamam ||",
        "rambhāphalaṃ ghṛtaṃ kṣīraṃ godhūmasya ca cūrṇakam |",
        "abhāve śālicūrṇaṃ vā śarkarāṃ ca guḍaṃ tathā |",
        "sapādaṃ sarvabhakṣyāṇi caikīkṛtya nivedayet ||"],
       "“Devoted to dharma, together with brahmins and kinsfolk, one should "
       "offer with devotion the food-offering, the excellent prasāda: plantain, "
       "ghee, milk and wheat semolina — or, lacking it, rice semolina — with "
       "sugar or jaggery; taking each ingredient in the measure of one and a "
       "quarter, one should mix them and offer them.”"),
    _v(["viprebhyo dakṣiṇāṃ dadyātkathāṃ śrutvā janaissaha |",
        "tataśca bandhubhissārdhaṃ viprānsaprīti bhojayet ||",
        "prasādaṃ bhakṣayedbhaktyā nṛtyagītādikaṃ caret |",
        "tataśca svagṛhaṃ gacchetsatyanārāyaṇaṃ smaran ||",
        "evaṃ kṛte manuṣyāṇāṃ vāñchāsiddhirbhaveddhruvam |",
        "viśeṣataḥ kaliyuge laghūpāyo hi bhūtale ||"],
       "“Having heard the story together with the people, one should give "
       "gifts to the brahmins, then feed them gladly along with one's kin; eat "
       "the prasāda with devotion, and have dancing and singing; then go home "
       "remembering Satyanārāyaṇa. When this is done, people's wishes are "
       "surely fulfilled. Above all in the Kali age, this is the easy means on "
       "earth.”"),
    _v(["iti prathamo'dhyāyaḥ ||"],
       "Thus ends the first chapter."),

    # ── Chapter 2 ──
    _h("Dvitīyo'dhyāyaḥ · Chapter Two"),
    _v(["sūta uvāca —",
        "athānyatsampravakṣyāmi kṛtaṃ yena purā dvija |",
        "kaścitkāśīpure ramye hyāsīdvipro'tinirdhanaḥ ||",
        "kṣuttṛḍbhyāṃ vyākulo bhūtvā nityaṃ babhrāma bhūtale ||"],
       "Sūta said: “Now I will tell you further, O brahmins, who kept this vow "
       "of old. In the lovely city of Kāśī there was a very poor brahmin. "
       "Distressed by hunger and thirst, he wandered the earth every day.”"),
    _v(["duḥkhitaṃ brāhmaṇaṃ dṛṣṭvā bhagavānbrāhmaṇapriyaḥ |",
        "vṛddhabrāhmaṇarūpastaṃ papraccha dvijamādarāt ||",
        "kimarthaṃ bhramase vipra mahīṃ nityaṃ suduḥkhitaḥ |",
        "tatsarvaṃ śrotumicchāmi kathyatāṃ dvijasattama ||"],
       "Seeing the brahmin in distress, the Lord, who loves brahmins, took the "
       "form of an old brahmin and asked him kindly: “Why, brahmin, do you "
       "wander the earth every day in such sorrow? I wish to hear all of it; "
       "tell me, best of the twice-born.”"),
    _v(["brāhmaṇa uvāca —",
        "brāhmaṇo'tidaridro'haṃ bhikṣārthaṃ vai bhrame mahīm |",
        "upāyaṃ yadi jānāsi kṛpayā kathaya prabho ||"],
       "The brahmin said: “I am a brahmin, very poor; I wander the earth for "
       "alms. If you know a remedy, sir, tell it to me in your kindness.”"),
    _v(["vṛddhabrāhmaṇa uvāca —",
        "satyanārāyaṇo viṣṇurvāñchitārthaphalapradaḥ |",
        "tasya tvaṃ pūjanaṃ vipra kuruṣva vratamuttamam |",
        "yatkṛtvā sarvaduḥkhebhyo mukto bhavati mānavaḥ ||"],
       "The old brahmin said: “Satyanārāyaṇa is Viṣṇu, who grants the fruit of "
       "one's wishes. Worship him, brahmin; keep his excellent vow, by which a "
       "person is freed from every sorrow.”"),
    _v(["vidhānaṃ ca vratasyāsya viprāyābhāṣya yatnataḥ |",
        "satyanārāyaṇo vṛddhastatraivāntaradhīyata ||"],
       "Having carefully told the brahmin the method of the vow, Satyanārāyaṇa "
       "in the form of the old man vanished on the spot."),
    _v(["tadvrataṃ śvaḥ kariṣyāmi yaduktaṃ brāhmaṇena vai |",
        "iti sañcintya vipro'sau rātrau nidrāṃ na labdhavān ||",
        "tataḥ prātassamutthāya satyanārāyaṇavratam |",
        "kariṣya iti saṅkalpya bhikṣārthamagamaddvijaḥ ||"],
       "“Tomorrow I will keep the vow the brahmin described,” thought the "
       "brahmin, and could not sleep that night. Rising at dawn, resolving “I "
       "will keep the Satyanārāyaṇa vow,” he went out for alms."),
    _v(["etasmindivase vipraḥ pracuraṃ dravyamāptavān |",
        "tenaiva bandhubhissārdhaṃ satyasya vratamācarat ||"],
       "That very day the brahmin gained much wealth, and with it, together "
       "with his kinsfolk, he kept the vow of Satya."),
    _v(["sarvaduḥkhavinirmuktassarvasampatsamanvitaḥ |",
        "babhūva sa dvijaśreṣṭho vratasyāsya prabhāvataḥ ||"],
       "By the power of this vow that excellent brahmin was freed from every "
       "sorrow and blessed with every kind of wealth."),
    _v(["tataḥ prabhṛti vipreṇa māsi māsi vrataṃ kṛtam ||",
        "evaṃ nārāyaṇasyedaṃ vrataṃ kṛtvā dvijottamaḥ |",
        "sarvapāpavinirmukto durlabhaṃ mokṣamāptavān ||"],
       "From then on the brahmin kept the vow every month. Having thus kept "
       "Nārāyaṇa's vow, the best of brahmins was freed from all sins and "
       "attained liberation, which is hard to win."),
    _v(["vratametadyadā vipraḥ pṛthivyāṃ saṅkariṣyati |",
        "tathaiva sarvaduḥkhaṃ ca manujasya vinaśyati ||"],
       "Whenever anyone on earth keeps this vow, just so every sorrow of that "
       "person is destroyed."),
    _v(["sūta uvāca —",
        "evaṃ nārāyaṇenoktaṃ nāradāya mahātmane |",
        "mayā tatkathitaṃ viprāḥ kimanyatkathayāmi vaḥ ||"],
       "Sūta said: “Thus Nārāyaṇa told it to the great-souled Nārada, and I "
       "have told it to you, brahmins. What more shall I tell you?”"),
    _v(["ṛṣaya ūcuḥ —",
        "tasmādviprācchrutaṃ kena pṛthivyāṃ caritaṃ mune |",
        "tatsarvaṃ śrotumicchāmaśśraddhāsmākaṃ prajāyate ||"],
       "The sages said: “Who on earth heard it from that brahmin and kept it, "
       "sage? We wish to hear all of it; faith is arising in us.”"),
    _v(["sūta uvāca —",
        "śṛṇudhvaṃ munayassarve vrataṃ kena kṛtaṃ bhuvi |",
        "ekadā sa dvijavaro yathāvibhavavistaraiḥ |",
        "bandhubhissvajanaissārdhaṃ vrataṃ kartuṃ samudyataḥ ||"],
       "Sūta said: “Hear, all you sages, who kept the vow on earth. Once that "
       "excellent brahmin, with all the splendour his means allowed, was about "
       "to keep the vow together with his kin and people.”"),
    _v(["etasminnantare kāle kāṣṭhakretā samāgataḥ |",
        "bahiḥ kāṣṭhāni saṃsthāpya viprasya gṛhamāyayau ||",
        "tṛṣṇayā pīḍitātmā ca dṛṣṭvā vipraṃ kṛtavratam |",
        "praṇipatya dvijaṃ prāha kimidaṃ kriyate tvayā |",
        "kṛte kiṃ phalamāpnoti vistarādvada me prabho ||"],
       "Just then a woodcutter came by. Leaving his wood outside, he came into "
       "the brahmin's house. Parched with thirst, he saw the vow the brahmin "
       "was keeping, bowed to him and said: “What is this you are doing? What "
       "fruit does one gain by it? Tell me in full, sir.”"),
    _v(["vipra uvāca —",
        "satyanārāyaṇasyedaṃ vrataṃ sarvepsitapradam |",
        "tasya prapūjane sarvaṃ dhanadhānyādikaṃ mahat ||"],
       "The brahmin said: “This is the vow of Satyanārāyaṇa, which grants all "
       "that one desires. By worshipping him comes every great thing — wealth, "
       "grain and all the rest.”"),
    _v(["tasmādetadvrataṃ jñātvā kāṣṭhakretā'tiharṣitaḥ |",
        "papau jalaṃ prasādaṃ ca bhuktvā svanagaraṃ yayau ||"],
       "Learning of this vow from him, the woodcutter was overjoyed. He drank "
       "water, ate the prasāda, and went back to his own town."),
    _v(["satyanārāyaṇaṃ devaṃ mānasenetyacintayat |",
        "kāṣṭhavikrayato grāme prāpsyate cādya yaddhanam |",
        "tenaiva satyadevasya kariṣye vratamuttamam ||",
        "iti sañcintya manasā kāṣṭhaṃ kṛtvā tu mastake ||"],
       "In his mind he thought of the god Satyanārāyaṇa thus: “With whatever "
       "money I get today by selling wood in the town, I will keep the "
       "excellent vow of Satyadeva.” So resolving, he set the wood upon his "
       "head …"),
    _v(["jagāma nagare ramye dhanināṃ yatra saṃsthitiḥ |",
        "taddine kāṣṭhamūlyaṃ ca dviguṇaṃ prāptavānasau ||",
        "tataḥ prasannahṛdayassupakvaṃ kadalīphalam |",
        "śarkarāghṛtadugdhaṃ ca godhūmasya ca cūrṇakam ||",
        "kṛtvaikatra sapādaṃ ca gṛhītvā svagṛhaṃ yayau ||"],
       "… and went to the lovely part of the city where the wealthy lived. "
       "That day he got twice the price for his wood. Glad at heart, he took "
       "ripe plantains, sugar, ghee, milk and wheat semolina, each a measure "
       "and a quarter, and went home."),
    _v(["tato bandhūnsamāhūya cakāra vidhinā vratam |",
        "tadvratasya prabhāvena dhanaputrānvito'bhavat |",
        "ihaloke sukhaṃ bhuktvā cānte satyapuraṃ yayau ||"],
       "Then he called his kinsfolk together and kept the vow as prescribed. "
       "By the power of that vow he was blessed with wealth and sons; he "
       "enjoyed happiness in this world and at the end went to the city of "
       "Satya."),
    _v(["iti dvitīyo'dhyāyaḥ ||"],
       "Thus ends the second chapter."),

    # ── Chapter 3 ──
    _h("Tṛtīyo'dhyāyaḥ · Chapter Three"),
    _v(["sūta uvāca —",
        "punaragre pravakṣyāmi śṛṇudhvaṃ munisattamāḥ |",
        "purā colkāmukho nāma nṛpaścāsīnmahīpatiḥ ||",
        "jitendriyassatyavādī gacchandevālayaṃ prati |",
        "dine dine dhanaṃ dattvā dvijānsantoṣayetsudhīḥ ||"],
       "Sūta said: “I will tell you more; listen, best of sages. Long ago there "
       "was a king, a lord of the earth, named Ulkāmukha — master of his "
       "senses, truthful. Going to the temple, the wise king pleased the "
       "brahmins every day with gifts of wealth.”"),
    _v(["bhāryā tasya pramugdhā ca sarojavadanā satī |",
        "bhadraśīlānadītīre satyasya vratamācarat ||"],
       "His wife, most charming, lotus-faced and virtuous — together they kept "
       "the vow of Satya on the bank of the river Bhadraśīlā."),
    _v(["etasminnantare tatra sādhurekassamāgataḥ |",
        "vāṇijyārthaṃ bahudhanairanekaiḥ paripūritām ||",
        "nāvaṃ saṃsthāpya tattīre jagāma nṛpatiṃ prati |",
        "dṛṣṭvā ca vratinaṃ bhūpaṃ papraccha vinayānvitaḥ ||"],
       "Just then a merchant named Sādhu arrived there, his boat laden with "
       "much wealth of many kinds for trade. Mooring the boat at the bank, he "
       "went to the king, and seeing him keeping the vow, asked him humbly:"),
    _v(["sādhuruvāca —",
        "kimidaṃ kuruṣe rājanbhaktiyuktena cetasā |",
        "prakāśaṃ kuru tatsarvaṃ śrotumicchāmi sāmpratam ||"],
       "Sādhu said: “What is this you are doing, O king, with a mind so full of "
       "devotion? Make it all known to me; I wish to hear it now.”"),
    _v(["rājā uvāca —",
        "pūjanaṃ kriyate sādho viṣṇoratulatejasaḥ |",
        "vrataṃ ca svajanaissārdhaṃ putrādiprāptikāmyayā ||"],
       "The king said: “Sādhu, we are worshipping Viṣṇu of matchless splendour "
       "and keeping his vow with our people, wishing for sons and other "
       "blessings.”"),
    _v(["bhūpasya vacanaṃ śrutvā sādhuḥ provāca sādaram |",
        "mamāpi santatirnāsti hyetasmājjāyate dhruvam ||"],
       "Hearing the king's words, Sādhu said respectfully: “I too have no "
       "children; surely through this they will be born.”"),
    _v(["tato nivṛtya vāṇijyātsānando gṛhamāyayau |",
        "bhāryāyai kathitaṃ sarvaṃ vrataṃ santatidāyakam ||",
        "tadā vrataṃ kariṣyāmi yadā me santatirbhavet |",
        "iti līlāvatīṃ prāha svapatnīṃ sādhusattamaḥ ||"],
       "Returning from his trading, he came home happy and told his wife all "
       "about the vow that grants children. “When a child is born to me, I will "
       "keep the vow,” said that excellent merchant to his wife Līlāvatī."),
    _v(["ekasmindivase tasya bhāryā līlāvatī satī |",
        "bhartṛyuktānandacittā'bhavaddharmaparāyaṇā ||",
        "garbhiṇī sā'bhavattasya bhāryā satyaprasādataḥ |",
        "daśame māsi vai tasyāḥ kanyāratnamajāyata ||"],
       "One day his virtuous wife Līlāvatī, devoted to dharma, was joyful with "
       "her husband; by the grace of Satya she conceived, and in the tenth "
       "month a jewel of a daughter was born to her."),
    _v(["dine dine sā vavṛdhe śuklapakṣe yathā śaśī |",
        "nāmnā kalāvatī ceti tannāmakaraṇaṃ kṛtam ||"],
       "Day by day she grew, like the moon in the bright fortnight; she was "
       "given the name Kalāvatī."),
    _v(["tato līlāvatī prāha svāminaṃ madhuraṃ vacaḥ |",
        "na karoṣi kimarthaṃ vai purā saṅkalpitaṃ vratam ||"],
       "Then Līlāvatī spoke sweetly to her husband: “Why do you not keep the "
       "vow you resolved on before?”"),
    _v(["vivāhasamaye tasyāḥ kariṣyāmi vrataṃ priye |",
        "iti bhāryāṃ samāśvāsya jagāma nagaraṃ prati ||"],
       "“At the time of her marriage I will keep the vow, my dear.” So "
       "reassuring his wife, he went off to the city."),
    _v(["tataḥ kalāvatī kanyā vavṛdhe pitṛveśmani |",
        "dṛṣṭvā kanyāṃ tatassādhurnagare sakhibhissaha |",
        "mantrayitvā drutaṃ dūtaṃ preṣayāmāsa dharmavit ||",
        "vivāhārthaṃ ca kanyāyā varaśreṣṭhaṃ vicāraya ||"],
       "The girl Kalāvatī grew up in her father's house. Seeing her grown, "
       "Sādhu, knower of dharma, consulted his friends in the city and quickly "
       "sent a messenger: “Seek out an excellent groom for my daughter's "
       "marriage.”"),
    _v(["tenājñaptaśca dūto'sau kāñcanaṃ nagaraṃ yayau |",
        "tasmādekaṃ vaṇikputraṃ samādāyāgato hi saḥ ||",
        "dṛṣṭvā taṃ sundaraṃ bālaṃ vaṇikputraṃ guṇānvitam |",
        "dadau sādhuḥ kumārīṃ tāṃ kanyāṃ vidhividhānataḥ ||"],
       "So commanded, the messenger went to the city of Kāñcana and came back "
       "with a merchant's son. Seeing that handsome youth, a merchant's son "
       "endowed with virtues, Sādhu gave him his daughter in marriage with due "
       "rites."),
    _v(["tato'bhāgyavaśāttena vismṛtaṃ vratamuttamam |",
        "vivāhasamaye tasyāstena ruṣṭo'bhavatprabhuḥ ||"],
       "But by ill fortune he forgot the excellent vow at the time of her "
       "wedding, and the Lord was angered by it."),
    _v(["tataḥ kālena niyato nijakarmaviśāradaḥ |",
        "vāṇijyārthaṃ gataśśīghraṃ jāmātṛsahito vaṇik ||",
        "ratnasānupure ramye sthitvā sindhusamīpataḥ |",
        "vāṇijyamakarotsādhurjāmātrā śrīmatā saha ||"],
       "In time the merchant, diligent and skilled in his work, soon set out "
       "to trade together with his son-in-law. Staying in the lovely city of "
       "Ratnasānu by the sea, Sādhu traded there with his prosperous "
       "son-in-law."),
    _v(["tau gatau nagaraṃ ramyaṃ candraketornṛpasya ca |",
        "etasminnantare kāle satyanārāyaṇaḥ prabhuḥ ||",
        "bhraṣṭapratijñamālokya śāpaṃ tasmai pradattavān |",
        "dāruṇaṃ kaṭhinaṃ cāsya mahadduḥkhaṃ bhaviṣyati ||"],
       "The two had come to the lovely city of King Candraketu. Just then the "
       "Lord Satyanārāyaṇa, seeing him fall from his promise, laid a curse on "
       "him: “Dreadful, hard and great sorrow shall come upon him.”"),
    _v(["etasmindivase rājño dhanamādāya taskaraḥ |",
        "tatraiva cāgataścauryādvaṇijau yatra saṃsthitau ||",
        "tatpaścāddhāvakāndūtāndṛṣṭvā bhītena cetasā |",
        "dhanaṃ saṃsthāpya tatraiva sa tu śīghramalakṣitaḥ ||"],
       "That day a thief who had stolen the king's treasure came to the very "
       "place where the two merchants were staying. Seeing the king's men "
       "running after him, he took fright, left the treasure right there, and "
       "quickly slipped away unseen."),
    _v(["tato dūtāssamāyātā yatrāste sajjano vaṇik |",
        "dṛṣṭvā nṛpadhanaṃ tatra baddhvā nītau vaṇiksutau ||",
        "harṣeṇa dhāvamānāśca ūcurnṛpasamīpataḥ |",
        "taskarau dvau samānītau vilokyājñāpaya prabho ||",
        "rājñājñaptāstataśśīghraṃ dṛḍhaṃ baddhvā tu tāvubhau |",
        "sthāpitau ca mahādurge kārāgāre'vicārataḥ ||"],
       "The messengers came to where the good merchant was, saw the king's "
       "wealth there, bound the two merchants and led them away. Running "
       "gleefully to the king they said: “We have brought two thieves; look at "
       "them and give your command, lord.” At the king's command they quickly "
       "bound both fast and, without any inquiry, put them in prison in a great "
       "fortress."),
    _v(["māyayā satyadevasya na śrutaṃ taistayorvacaḥ |",
        "tatastayordhanaṃ rājñā gṛhītaṃ candraketunā ||",
        "tacchāpācca tayorgehe bhāryā caivātiduḥkhitā |",
        "coreṇāpahṛtaṃ sarvaṃ gṛhe yacca sthitaṃ dhanam ||"],
       "By Satyadeva's māyā no one listened to their words, and King Candraketu "
       "seized their wealth. Through that curse, at their home the wife too "
       "fell into great sorrow: all the wealth kept in the house was carried "
       "off by a thief."),
    _v(["ādhivyādhisamāyuktā kṣutpipāsātiduḥkhitā |",
        "annacintāparā bhūtvā babhrāma ca gṛhe gṛhe ||",
        "kalāvatī tu kanyāpi babhrāma prativāsaram ||"],
       "Beset by grief and sickness, tormented by hunger and thirst, anxious "
       "for food, she wandered from house to house; and the girl Kalāvatī too "
       "wandered about every day."),
    _v(["ekasmindivase yātā kṣudhārtā dvijamandiram |",
        "gatā'paśyadvrataṃ tatra satyanārāyaṇasya ca ||",
        "upaviśya kathāṃ śrutvā devaṃ prārthitavatyapi |",
        "prasādabhakṣaṇaṃ kṛtvā yayau rātriṃ gṛhaṃ prati ||"],
       "One day, pinched with hunger, she went to a brahmin's house, and there "
       "she saw the vow of Satyanārāyaṇa being kept. She sat down, heard the "
       "story, prayed to the god, ate the prasāda, and went home at night."),
    _v(["mātā kalāvatīṃ kanyāṃ kathayāmāsa premataḥ |",
        "putri rātrau sthitā kutra kiṃ te manasi vartate ||",
        "kanyā kalāvatī prāha mātaraṃ prati satvaram |",
        "dvijālaye vrataṃ mātardṛṣṭaṃ vāñchitasiddhidam ||"],
       "Her mother spoke lovingly to Kalāvatī: “Daughter, where were you till "
       "night? What is on your mind?” The girl Kalāvatī answered her mother at "
       "once: “Mother, at a brahmin's house I saw a vow that fulfils one's "
       "wishes.”"),
    _v(["tacchrutvā kanyakāvākyaṃ vrataṃ kartuṃ samudyatā |",
        "sā mudā tu vaṇigbhāryā satyanārāyaṇasya vai ||",
        "vrataṃ cakre tadā sādhvī bandhubhissvajanaissaha |",
        "bhartṛjāmātarau kṣipramāgacchetāṃ svamāśrayam ||",
        "aparādhaṃ ca me bhartuḥ jāmātuḥ kṣantumarhasi ||"],
       "Hearing her daughter's words, she resolved to keep the vow. Joyfully "
       "the merchant's good wife kept the vow of Satyanārāyaṇa with her kin "
       "and people: “May my husband and son-in-law quickly come home. Please "
       "forgive the offence of my husband and son-in-law.”"),
    _v(["vratenānena santuṣṭassatyanārāyaṇaḥ prabhuḥ |",
        "darśayāmāsa svapnaṃ hi candraketornṛpasya ca ||",
        "bandhitau mocaya prātarvaṇijau nṛpasattama |",
        "deyaṃ dhanaṃ ca tatsarvaṃ gṛhītaṃ yattvayādhunā ||",
        "no cettvāṃ nāśayiṣyāmi sarājyadhanaputrakam |",
        "evamābhāṣya rājānaṃ dhyānagamyo'bhavatprabhuḥ ||"],
       "Pleased by this vow, the Lord Satyanārāyaṇa appeared in a dream to King "
       "Candraketu: “Best of kings, release the two bound merchants at dawn, "
       "and give back all the wealth you have taken. Otherwise I will destroy "
       "you with your kingdom, wealth and sons.” Having spoken so to the king, "
       "the Lord withdrew, to be reached only in meditation."),
    _v(["tataḥ prabhātasamaye rājā ca svajanaissaha |",
        "upaviśya sabhāmadhye prāha svapnaṃ janaṃ prati ||",
        "baddhau mahājanau śīghraṃ mocayadhvaṃ vaṇiksutau |",
        "iti rājño vacaśśrutvā mocayitvā mahājanau ||",
        "samānīya nṛpasyāgre prāhuste vinayānvitāḥ |",
        "ānītau dvau vaṇikputrau muktau nigalabandhanāt ||"],
       "At daybreak the king sat in the midst of his court with his people and "
       "told them the dream: “Quickly release the two worthy merchants who are "
       "in bonds.” Hearing the king's words, they released the two good men, "
       "brought them before the king, and said humbly: “The two merchants have "
       "been brought, freed from their fetters.”"),
    _v(["tato mahājanau natvā candraketuṃ nṛpottamam |",
        "smarantau pūrvavṛttāntaṃ nocaturbhayavihvalau ||"],
       "The two merchants bowed to Candraketu, best of kings, and remembering "
       "what had happened before, stood speechless, trembling with fear."),
    _v(["rājā vaṇiksutau vīkṣya vacaḥ provāca sādaram |",
        "daivātprāptaṃ mahadduḥkhamidānīṃ nāsti vai bhayam ||",
        "tadā nigalasantyāgaṃ kṣaurakarmādyakārayat |",
        "vastrādyalaṅkṛtiṃ dattvā paritoṣya nṛpaśca tau ||",
        "puraskṛtya vaṇikputrau vacasā'toṣayadbhṛśam |",
        "purānītaṃ tu yaddravyaṃ dviguṇīkṛtya dattavān ||"],
       "Looking at the merchants, the king said kindly: “By fate great sorrow "
       "befell you; now there is nothing to fear.” He had their fetters "
       "removed, had them shaved and bathed, gave them clothes and ornaments "
       "and made them content. Honouring the two merchants, he cheered them "
       "greatly with his words, and gave back twice the wealth he had taken."),
    _v(["provāca tau tato rājā gaccha sādho nijāśramam |",
        "rājānaṃ praṇipatyāha gantavyaṃ tvatprasādataḥ ||"],
       "Then the king said to them: “Go home, Sādhu.” Bowing to the king he "
       "said: “By your grace we shall go.”"),
    _v(["iti tṛtīyo'dhyāyaḥ ||"],
       "Thus ends the third chapter."),

    # ── Chapter 4 ──
    _h("Caturtho'dhyāyaḥ · Chapter Four"),
    _v(["sūta uvāca —",
        "yātrāṃ kṛtvā tatassādhurmaṅgalācārapūrvakam |",
        "brāhmaṇebhyo dhanaṃ dattvā yayau svanagaraṃ prati ||"],
       "Sūta said: “Then Sādhu, having performed the auspicious rites for a "
       "journey and given wealth to brahmins, set out for his own city.”"),
    _v(["kiyaddūraṃ gate cābdhau satyanārāyaṇaḥ prabhuḥ |",
        "jijñāsāṃ kṛtavānsādho naukāyāmasti kiṃ tava ||"],
       "When he had gone some distance on the sea, the Lord Satyanārāyaṇa, "
       "wishing to test him, asked: “Sādhu, what is in your boat?”"),
    _v(["tato mahājanau mattau helayā ca prahasya vai |",
        "kathaṃ pṛcchasi bho daṇḍin mudrāṃ netuṃ kimicchasi ||",
        "latāpatrādikaṃ caiva vartate taraṇau mama |",
        "ityuktaṃ vacanaṃ śrutvā satyaṃ bhavatu te vacaḥ ||"],
       "The two merchants, proud of their wealth, laughed at him scornfully: "
       "“Why do you ask, ascetic? Do you want to carry off our money? There is "
       "nothing in my boat but creepers and leaves.” Hearing these words he "
       "said: “Let your word be true.”"),
    _v(["evamuktvā gataśśīghraṃ daṇḍī tasya samīpataḥ |",
        "kiyaddūraṃ tato gatvā sthitassindhusamīpataḥ ||",
        "gate daṇḍini sādhuśca kṛtanityakriyastathā |",
        "utthitāṃ taraṇiṃ dṛṣṭvā vismayaṃ paramaṃ yayau ||"],
       "Having said this, the ascetic quickly left him, went some distance "
       "away, and stayed near the shore. When the ascetic had gone, Sādhu "
       "finished his daily rites, and seeing the boat riding high in the "
       "water, was utterly amazed."),
    _v(["dṛṣṭvā latādikaṃ caiva mūrchito nyapatadbhuvi |",
        "labdhasaṃjño vaṇikputrastataśśokānvito'bhavat ||"],
       "Seeing only creepers and leaves in it, he fainted and fell to the "
       "ground; when he came to, the merchant was overcome with grief."),
    _v(["tadā tu duhituḥ kānto vacanaṃ cedamabravīt |",
        "kimarthaṃ kriyate śokaśśāpo dattaśca daṇḍinā ||",
        "śakyate'nena sarvaṃ hi kartuṃ cātra na saṃśayaḥ |",
        "atastaṃ śaraṇaṃ yāvo vāñchitārtho bhaviṣyati ||"],
       "Then his daughter's husband said: “Why grieve? The ascetic has laid a "
       "curse on us. He can do anything, no doubt of it. So let us go to him "
       "for refuge; what we wish for will come about.”"),
    _v(["jāmāturvacanaṃ śrutvā tatsakāśaṃ gato vaṇik |",
        "dṛṣṭvā ca daṇḍinaṃ bhaktyā natvā provāca sādaram ||",
        "kṣamasva cāparādhaṃ me yaduktaṃ tava sannidhau |",
        "evaṃ punaḥ punarnatvā mahāśokākulo'bhavat ||"],
       "Hearing his son-in-law's words the merchant went to him, and seeing "
       "the ascetic, bowed with devotion and said respectfully: “Forgive the "
       "offence of what I said before you.” Bowing again and again, he was "
       "overwhelmed with grief."),
    _v(["provāca vacanaṃ daṇḍī vilapantaṃ vilokya ca |",
        "mā rodīśśṛṇu madvākyaṃ mama pūjābahirmukhaḥ ||",
        "mamājñayaiva durbuddhe labdhaṃ duḥkhaṃ muhurmuhuḥ ||"],
       "Seeing him lament, the ascetic said: “Do not weep; hear my words. You "
       "turned away from my worship; by my command alone, foolish one, you have "
       "met sorrow again and again.”"),
    _v(["sādhuruvāca —",
        "tacchrutvā bhagavadvākyaṃ stutiṃ kartuṃ samudyataḥ ||",
        "tvanmāyāmohitāssarve brahmādyāstridivaukasaḥ |",
        "na jānanti guṇānrūpaṃ tavāścaryamidaṃ prabho ||",
        "mūḍho'haṃ tvāṃ kathaṃ jāne mohitastava māyayā |",
        "prasīda pūjayiṣyāmi yathāvibhavavistaram ||",
        "purā vittaṃ ca yatsarvamanugṛhṇīṣva tatprabho |",
        "pāhi māṃ puṇḍarīkākṣa tvāmadya śaraṇāgatam ||"],
       "Hearing the Lord's words, Sādhu set about praising him: “Deluded by "
       "your māyā, all the dwellers of heaven, Brahmā and the rest, do not know "
       "your qualities or your form — this is a wonder, Lord. I am a fool; how "
       "should I know you, deluded by your māyā? Be gracious: I will worship "
       "you with all the splendour my means allow. Restore, Lord, all the "
       "wealth that was mine before. Protect me, lotus-eyed one, who today "
       "come to you for refuge.”"),
    _v(["śrutvā bhaktiyutaṃ vākyaṃ parituṣṭo janārdanaḥ |",
        "varaṃ ca vāñchitaṃ dattvā tatraivāntaradhīyata ||"],
       "Hearing these words full of devotion, Janārdana was pleased; granting "
       "the boon he wished, he vanished on the spot."),
    _v(["tato nāvaṃ samāruhya dṛṣṭvā vittaprapūritām |",
        "kṛpayā satyadevasya saphalaṃ vāñchitaṃ mama ||",
        "ityuktvā svajanaissārdhaṃ pūjāṃ kṛtvā yathāvidhi |",
        "harṣeṇa cābhavatpūrṇassatyadevaprasādataḥ ||"],
       "Then, boarding the boat and seeing it full of wealth, he said: “By the "
       "mercy of Satyadeva my wish is fulfilled.” Saying this, he worshipped "
       "duly with his people, and was filled with joy by Satyadeva's grace."),
    _v(["sādhurjāmātaraṃ prāha paśya ratnapurīṃ mama |",
        "dūtaṃ ca preṣayāmāsa nijavittasya rakṣakam ||"],
       "Sādhu said to his son-in-law, “Look, there is my city of jewels,” and "
       "sent a messenger, the guardian of his wealth, ahead."),
    _v(["dūto'sau nagaraṃ gatvā sādhubhāryāṃ vilokya ca |",
        "provācātmahitaṃ vākyaṃ natvā baddhāñjalistathā ||",
        "nikaṭe nagarasyaiva jāmātrā sahito vaṇik |",
        "āgato bandhuvargaiśca svajanairbahubhiryutaḥ ||"],
       "The messenger went to the city, saw Sādhu's wife, bowed with folded "
       "hands and gave her the welcome news: “The merchant has arrived near the "
       "city with his son-in-law, together with many kinsfolk and people.”"),
    _v(["śrutvā dūtamukhādvākyaṃ mahāharṣavatī satī |",
        "satyapūjāṃ tataḥ kṛtvā provāca tanujāṃ prati ||",
        "vrajāmi śīghramāgaccha sādhusandarśanāya ca |",
        "iti mātṛvacaśśrutvā vrataṃ kṛtvā samāpya ca ||",
        "prasādaṃ tu parityajya gatā sāpi patiṃ prati ||"],
       "Hearing the message from the messenger's mouth, the good woman was "
       "overjoyed. Having done the worship of Satya, she said to her daughter: "
       "“I am going; come quickly to see Sādhu.” Hearing her mother's words, "
       "the daughter finished the vow — but leaving the prasāda behind, she too "
       "went to meet her husband."),
    _v(["tena ruṣṭassatyadevo bhartāraṃ taraṇiṃ tadā |",
        "saṃhṛtya ca dhanaissārdhaṃ jale tasminnamajjayat ||",
        "dṛṣṭvā tathāvidhāṃ nāvaṃ kanyāṃ ca bahuduḥkhitām |",
        "bhītena manasā duḥkhamāpurāścaryamantikāḥ ||",
        "cintayānāśca te sarve babhūvustīravāsakāḥ ||"],
       "Angered by that, Satyadeva seized the husband and the boat together "
       "with the wealth, and sank them in that water. Seeing the boat so, and "
       "the girl in great sorrow, those nearby were frightened, grieved and "
       "amazed; all who stood on the shore became anxious."),
    _v(["tato līlāvatī kanyāṃ dṛṣṭvā sā vihvalābhavat |",
        "vilalāpātiduḥkhena bhartāraṃ cedamabravīt ||",
        "idānīṃ naukayā sārdhaṃ kathaṃ so'bhūdalakṣitaḥ |",
        "na jāne kasya devasya helayā nauśca sā hṛtā ||",
        "satyadevasya māhātmyaṃ jñātuṃ kartuṃ na śakyate |",
        "ityuktvā vilalāpaivaṃ tataśca svajanaissaha ||",
        "tato līlāvatī kanyāṃ kroḍe kṛtvā ruroda hi ||"],
       "Then Līlāvatī, seeing her daughter, was distraught; she wept in great "
       "sorrow and said to her husband: “How has he vanished just now together "
       "with the boat? I do not know by the slight of which god that boat was "
       "taken. Satyadeva's greatness cannot be known or wrought by us.” So "
       "saying she lamented with her people, and taking her daughter in her "
       "lap, she wept."),
    _v(["tataḥ kalāvatī kanyā naṣṭe svāmini duḥkhitā |",
        "gṛhītvā pāduke tasya hyanugantuṃ mano dadhau ||"],
       "Then the girl Kalāvatī, grieving for her lost husband, took his sandals "
       "and set her mind on following him in death."),
    _v(["kanyāyāścaritaṃ dṛṣṭvā sabhāryassvajano vaṇik |",
        "atiśokena santaptaścintayāmāsa dharmavit ||",
        "hṛtaṃ vā satyadevena bhrānto'haṃ satyamāyayā |",
        "satyapūjāṃ kariṣyāmi yathāvibhavavistaram ||",
        "iti sarvānsamāhūya kathayitvā manogatam |",
        "natvā ca daṇḍavadbhūmau satyadevaṃ punaḥ punaḥ ||"],
       "Seeing what his daughter was doing, the merchant, knower of dharma, "
       "with his wife and people, burned with great grief and reflected: "
       "“Surely it was taken by Satyadeva; I am bewildered by Satya's māyā. I "
       "will do the worship of Satya with all the splendour my means allow.” "
       "Calling everyone together and telling them his mind, he prostrated "
       "full length on the ground to Satyadeva again and again."),
    _v(["tatastuṣṭassatyadevo dīnānāṃ paripālakaḥ |",
        "jagāda vacanaṃ caivaṃ kṛpayā bhaktavatsalaḥ ||",
        "tyaktvā prasādaṃ te kanyā patiṃ draṣṭuṃ samāgatā |",
        "ato'dṛṣṭo'bhavattasyāḥ kanyakāyāḥ patirdhruvam ||",
        "gṛhaṃ gatvā tatprasādaṃ bhuktvā sāyāti cetpunaḥ |",
        "labdhabhartrī sutā sādho bhaviṣyati na saṃśayaḥ ||"],
       "Then Satyadeva, protector of the helpless, loving to his devotees, was "
       "pleased, and spoke thus in mercy: “Your daughter left the prasāda and "
       "came to see her husband; that is why her husband vanished. If she goes "
       "home, eats the prasāda and comes back, your daughter will regain her "
       "husband, Sādhu; there is no doubt.”"),
    _v(["kanyakā tādṛśaṃ vākyaṃ śrutvā gaganamaṇḍalāt |",
        "kṣipraṃ tadā gṛhaṃ gatvā prasādamanubhujya ca |",
        "sā paścātpunarāgatya dadarśa svaṃ mudā patim ||"],
       "Hearing such words from the sky, the girl went home at once and ate "
       "the prasāda; then, coming back, she saw her own husband, and "
       "rejoiced."),
    _v(["tataḥ kalāvatī kanyā jagāda pitaraṃ prati |",
        "idānīṃ svagṛhaṃ yāhi vilambaṃ kuruṣe katham ||",
        "tacchrutvā kanyakāvākyaṃ santuṣṭo'bhūdvaṇiksutaḥ |",
        "pūjanaṃ satyadevasya kṛtvā vidhividhānataḥ |",
        "dhanairbandhugaṇaissārdhaṃ jagāma nijamandiram ||"],
       "Then the girl Kalāvatī said to her father: “Now let us go home; why do "
       "you delay?” Hearing his daughter's words the merchant was content; "
       "having worshipped Satyadeva with due rites, he went to his own house "
       "with his wealth and his kinsfolk."),
    _v(["paurṇamāsyāṃ ca saṅkrāntau kṛtavānsatyapūjanam |",
        "ihaloke sukhaṃ bhuktvā cānte satyapuraṃ yayau ||"],
       "On every full moon and every saṅkrānti he performed the worship of "
       "Satya; he enjoyed happiness in this world and at the end went to the "
       "city of Satya."),
    _v(["iti caturtho'dhyāyaḥ ||"],
       "Thus ends the fourth chapter."),

    # ── Chapter 5 ──
    _h("Pañcamo'dhyāyaḥ · Chapter Five"),
    _v(["sūta uvāca —",
        "athānyatsampravakṣyāmi śṛṇudhvaṃ munisattamāḥ |",
        "āsīttuṅgadhvajo rājā prajāpālanatatparaḥ ||"],
       "Sūta said: “Now I will tell you another story; listen, best of sages. "
       "There was a king named Tuṅgadhvaja, devoted to protecting his "
       "people.”"),
    _v(["ekadā sa vanaṃ gatvā hatvā bahuvidhānpaśūn |",
        "āgatya bilvamūlaṃ ca dṛṣṭvā satyasya pūjanam ||",
        "gopāḥ kurvanti santuṣṭā bhaktiyuktāssabāndhavāḥ |",
        "rājā dṛṣṭvāpi darpeṇa na gatvā taṃ nanāma saḥ ||"],
       "Once he went into the forest and killed many kinds of animals. Coming "
       "to the foot of a bilva tree, he saw cowherds joyfully worshipping Satya with "
       "devotion, together with their kin. Though he saw it, the king in his "
       "pride did not go near and did not bow to the Lord."),
    _v(["tato gopagaṇāssarve prasādaṃ nṛpasannidhau |",
        "saṃsthāpya punarāgatya bubhujuśca yathepsitam ||"],
       "Then all the cowherds set the prasāda before the king, came back, and "
       "ate as they wished."),
    _v(["tataḥ prasādaṃ santyajya rājā duḥkhamavāpa saḥ |",
        "tasya putraśataṃ naṣṭaṃ dhanadhānyādikaṃ ca yat ||"],
       "Having rejected the prasāda, the king met with sorrow: his hundred sons "
       "perished, and all his wealth, grain and possessions."),
    _v(["satyadevena tatsarvaṃ nāśitaṃ mama niścitam |",
        "atastatraiva gacchāmi yatra devasya pūjanam ||",
        "manaseti viniścitya yayau gopālasannidhim |",
        "tato'sau satyadevasya pūjāṃ gopagaṇaissaha ||",
        "bhaktiśraddhānvito bhūtvā cakāra vidhinā nṛpaḥ |",
        "satyadevaprasādena dhanaputrānvito'bhavat |",
        "ihaloke sukhaṃ bhuktvā cānte satyapuraṃ yayau ||"],
       "“Surely Satyadeva has destroyed all this of mine; so I will go to the "
       "very place where the god was worshipped.” Resolving so in his mind, he "
       "went to the cowherds, and with them the king, full of devotion and "
       "faith, performed the worship of Satyadeva as prescribed. By Satyadeva's "
       "grace he was blessed with wealth and sons; he enjoyed happiness in this "
       "world and at the end went to the city of Satya."),
    _v(["ya idaṃ kurute satyavrataṃ paramadurlabham |",
        "śṛṇoti ca kathāṃ puṇyāṃ bhaktimuktiphalapradām ||",
        "dhanadhānyādhikaṃ tasya bhavetsatyaprasādataḥ |",
        "daridro labhate vittaṃ baddho mucyeta bandhanāt ||",
        "bhīto bhayātpramucyeta satyameva na saṃśayaḥ ||"],
       "Whoever keeps this supremely rare vow of Satya, and hears this holy "
       "story that yields devotion and liberation, gains wealth, grain and all else by Satya's "
       "grace. The poor man gains riches, the bound are freed from bonds, the "
       "fearful are freed from fear — this is truth, there is no doubt."),
    _v(["īpsitaṃ ca phalaṃ bhuktvā cānte satyapuraṃ vrajet |",
        "iti vaḥ kathitaṃ viprāssatyanārāyaṇavratam |",
        "yatkṛtvā sarvaduḥkhebhyo mukto bhavati mānavaḥ ||"],
       "Having enjoyed the fruit he desires, at the end he goes to the city of "
       "Satya. Thus I have told you, brahmins, the vow of Satyanārāyaṇa, by "
       "keeping which a person is freed from every sorrow."),
    _v(["viśeṣataḥ kaliyuge satyapūjā phalapradā |",
        "kecitkalau vadiṣyanti satyamīśaṃ tameva ca |",
        "satyanārāyaṇaṃ kecitsatyadevaṃ tathaiva ca ||",
        "śrīviṣṇunā dhṛtaṃ rūpaṃ sarveṣāmīpsitapradam ||"],
       "Above all in the Kali age the worship of Satya bears fruit. In Kali "
       "some will call him Satya, others Īśa, some Satyanārāyaṇa, and others "
       "Satyadeva — the form taken by Śrī Viṣṇu to grant what all desire."),
    _v(["nānārūpadharo bhūtvā sarveṣāmīpsitapradaḥ |",
        "bhaviṣyati kalau satyavratarūpe sanātanaḥ ||"],
       "Taking many forms, granting what all desire, the Eternal One will "
       "appear in the Kali age in the form of the vow of Satya."),
    _v(["kathāṃ vā śṛṇuyādyastu paśyedvā vratamuttamam |",
        "tasya naśyanti pāpāni satyadevaprasādataḥ ||"],
       "Whoever only hears the story, or witnesses the excellent vow — his sins "
       "are destroyed by the grace of Satyadeva."),
    _v(["iti śrīskāndapurāṇe revākhaṇḍe satyanārāyaṇavratakathāyāṃ",
        "pañcamo'dhyāyassamāptaḥ ||"],
       "Thus ends the fifth chapter of the story of the Satyanārāyaṇa vow, in "
       "the Revākhaṇḍa of the Skānda Purāṇa."),
]

# ───────────────────────── closing ─────────────────────────
S += [
    "ornament",
    _h("Punaḥpūjā · the worship repeated"),
    _p(["punaḥ prāṇānāyamya | śrīsatyanārāyaṇamuddiśya śrīsatyanārāyaṇasvāmiprītyarthaṃ",
        "śrīsatyanārāyaṇasvāminaḥ punaḥpūjāṃ kariṣye ||",
        "śrīsatyanārāyaṇasvāmine namaḥ | dhyāyāmi | āvāhayāmi | ratnasiṃhāsanaṃ samarpayāmi |",
        "pādayoḥ pādyaṃ samarpayāmi | hastayorarghyaṃ samarpayāmi | snapayāmi |",
        "śuddhācamanīyaṃ samarpayāmi | vastrayugmaṃ samarpayāmi | yajñopavītaṃ samarpayāmi |",
        "divyaśrīcandanaṃ samarpayāmi | akṣatān samarpayāmi | nānāvidhapuṣpāṇi pūjayāmi |",
        "oṃ keśavāya namaḥ … | dhūpamāghrāpayāmi | dīpaṃ darśayāmi |",
        "dhūpadīpānantaram ācamanīyaṃ samarpayāmi ||"],
       "Restraining the breath again: for the pleasure of Śrī Satyanārāyaṇa I "
       "will worship him once more. Salutation to him — meditation, "
       "invocation, throne, water for feet and hands, bath, pure water, "
       "garments, sacred thread, sandal, akṣata, many flowers; the names from "
       "Keśava onward; incense, lamp, and water to sip after them."),
    _p(["naivedyam — oṃ bhūrbhuvassuvaḥ … pracodayāt | satyaṃ tvartena pariṣiñcāmi |",
        "śrīsatyanārāyaṇasvāmine namaḥ | amṛtamastu | amṛtopastaraṇamasi |",
        "oṃ prāṇāya svāhā … samānāya svāhā | madhye madhye pānīyaṃ samarpayāmi |",
        "amṛtāpidhānamasi | uttarāpośanaṃ samarpayāmi | tāmbūlaṃ samarpayāmi |",
        "suvarṇamantrapuṣpaṃ samarpayāmi | pradakṣiṇanamaskārān samarpayāmi ||",
        "anayā dhyānāvāhanādiṣoḍaśopacārapūjayā bhagavān sarvātmakaḥ",
        "śrīsatyanārāyaṇasvāmī suprītassuprasanno varado bhavatu |",
        "śrīsatyanārāyaṇaprasādaṃ śirasā gṛhṇāmi ||"],
       "The food-offering as before, with betel, the flower of mantra, and "
       "circumambulation. By this worship may the Lord, Self of all, Śrī "
       "Satyanārāyaṇa, be well pleased, gracious, and grant boons; I receive his "
       "grace upon my head."),
    _h("Udvāsanam · farewell"),
    _v(["yajñena yajñamayajanta devāstāni dharmāṇi prathamānyāsan |",
        "te ha nākaṃ mahimānassacante yatra pūrve sādhyāssanti devāḥ ||"],
       "With sacrifice the gods worshipped the Sacrifice; these were the first "
       "ordinances. Those great ones reached the vault of heaven, where the "
       "ancient Sādhyas, the gods, abide. (The deity is bidden farewell.)"),
    _h("Maṇṭapadānam · gift of the maṇḍapa"),
    _r("The image and maṇḍapa are given to the officiating priest, honoured as "
       "Satyanārāyaṇa himself."),
    _p(["punaḥ prāṇānāyamya | parameśvaraprītyarthaṃ",
        "svarṇasvarcitapratimāmaṇṭapadānaṃ kariṣye ||",
        "śrīsatyanārāyaṇasvarūpasya brāhmaṇasya ubhābhyāṃ pādyam ||"],
       "Restraining the breath again: for the pleasure of the Supreme Lord I "
       "will give the maṇḍapa with its gilded image. Water for both feet of the "
       "brahmin who is the form of Śrī Satyanārāyaṇa."),
    _v(["namo'stvanantāya sahasramūrtaye sahasrapādākṣiśirorubāhave |",
        "sahasranāmne puruṣāya śāśvate sahasrakoṭīyugadhāriṇe namaḥ ||",
        "śrīsatyanārāyaṇasvarūpasya brāhmaṇasya gandhaṃ akṣatān puṣpāṇi ||"],
       "Salutation to the Infinite, of a thousand forms, with a thousand feet, "
       "eyes, heads, thighs and arms; to the eternal Person of a thousand "
       "names, who sustains a thousand crores of ages — salutation. Sandal, "
       "akṣata and flowers to the brahmin who is the form of Satyanārāyaṇa."),
    _p(["asmai brāhmaṇāya yajuśśākhādhyāyine … gotrāya … śarmaṇe pratigṛhītre",
        "śrīmān … gotraḥ … nāmadheyaḥ dharmapatnīsameto'haṃ",
        "… gotrasya … nāmadheyasya dharmapatnīsametasya",
        "mamopāttaduritakṣayadvārā śrīparameśvaraprītyarthaṃ",
        "satyanārāyaṇasvarṇasvarcitapratimāmaṇṭapaṃ tubhyamahaṃ sampradade na mama ||"],
       "To this brahmin, student of the Yajur-veda branch, of such a gotra and "
       "name, the receiver — I, of such a gotra and name, with my wife, for the "
       "removal of my sins and the pleasure of the Supreme Lord, give you this "
       "maṇḍapa with the gilded image of Satyanārāyaṇa: it is no longer mine."),
    _v(["devasya tvā savituḥ prasave'śvinorbāhubhyāṃ pūṣṇo hastābhyāṃ pratigṛhṇāmi |",
        "vaśśreyasī pratigṛhṇāmi ||",
        "etaddānasādguṇyārthaṃ yathāśakti dakṣiṇāṃ tubhyamahaṃ sampradade na mama ||"],
       "(The priest:) At the impulse of god Savitṛ, with the arms of the "
       "Aśvins and the hands of Pūṣan, I receive you. — To make this gift "
       "complete, I give you a fee as my means allow: it is no longer mine."),
    _v(["śrīsatyanārāyaṇavratakalpaḥ samāptaḥ ||"],
       "Here ends the Śrī Satyanārāyaṇa Vratakalpa."),
]

STOTRA = {
    "deity": "vishnu",
    "doc_title": "Śrī Satyanārāyaṇa Vratakalpam",
    "app_title": "Satyanārāyaṇa Vratam",
    "h1": "Śrī Satyanārāyaṇa Vratakalpam",
    "subtitle": "The observance of Satyanārāyaṇa · pūjā and the kathā of the Skānda Purāṇa",
    "note": "The whole vrata as kept at Annavaram: the preliminaries and resolve, "
            "Gaṇapati pūjā, the lokapālas, the nine planets and the guardians of "
            "the quarters, the sixteen-fold worship of Satyanārāyaṇa with the "
            "Puruṣa and Śrī Sūktas, and the five chapters of the vrata-kathā "
            "(Skānda Purāṇa, Revākhaṇḍa). The Sanskrit only is given; the "
            "ritual directions appear as short English notes between the texts. "
            "Vedic mantras are shown without accents.",
    "footer": "Source: Telugu-script vratakalpam booklets of the Annavaram "
              "(Śrī Vīra Veṅkaṭa Satyanārāyaṇa Svāmi) tradition, compiled by the "
              "maintainer; Sanskrit text public domain; directions and "
              "translations original",
    "sections": S,
}
