# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Lalitā Sahasranāma Stotram — the thousand names of Lalitā Tripurasundarī,
# from the Uttarakhaṇḍa of the Brahmāṇḍa Purāṇa (the dialogue of Hayagrīva
# and Agastya). Devanāgarī from Sanskrit Wikisource
# (श्रीललितासहस्रनामस्तोत्रम्, CC BY-SA; the verses themselves are ancient and
# public domain) via the bundled dev2iast converter. The source carries
# thirteen inline variant readings ("or X"); the primary reading is used and
# every variant is logged. Translations original. See SOURCES.md §5.22.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "devi",
    "doc_title": "Lalitā Sahasranāmam",
    "app_title": "Lalitā Sahasranāmam",
    "h1": "Lalitā Sahasranāmam",
    "subtitle": "The Thousand Names of Lalitā Tripurasundarī · Brahmāṇḍa Purāṇa",
    "note": "The great litany of the Śrīvidyā tradition, revealed by Hayagrīva "
            "to Agastya. It opens with a portrait of the Goddess from crown to "
            "feet, tells of her war against Bhaṇḍāsura, and rises through the "
            "cakras of the subtle body to the pure negations — nityā, nirguṇā, "
            "niṣkalā — before returning to her as Śrīvidyā herself. One hundred "
            "and eighty-two verses; the translations render each name in the "
            "order it is sung.",
    "audio": "https://www.youtube.com/watch?v=zgG-gjioU1g",
    "audio_label": "Ranjani–Gayatri — Lalitā Sahasranāmam",
    "footer": "Source: Sanskrit Wikisource — श्रीललितासहस्रनामस्तोत्रम् (verses public domain)",
    "sections": [
        _v(["sindūrāruṇavigrahāṃ trinayanāṃ māṇikyamaulisphurat",
            "tārānāyakaśekharāṃ smitamukhīmāpīnavakṣoruhām |",
            "pāṇibhyāmalipūrṇaratnacaṣakaṃ raktotpalaṃ bibhratīṃ",
            "saumyāṃ ratnaghaṭastharaktacaraṇāṃ dhyāyet parāmambikām"], "",
           "Dhyāna. Her form red as vermilion, three-eyed, her ruby crown "
           "ablaze, crested with the lord of stars; smiling-faced and full of "
           "breast; bearing in her two hands a jewelled cup brimming with "
           "nectar and a red lotus; gracious, her red feet resting on a jewelled "
           "vessel — thus let one meditate on the supreme Mother."),
        "ornament",
        _v(["oṃ śrīmātā śrīmahārājñī śrīmatsiṃhāsaneśvarī |",
            "cidagnikuṇḍasambhūtā devakāryasamudyatā"], "|| 1 ||",
           "The auspicious Mother; the great Empress; sovereign of the glorious "
           "lion-throne; born from the fire-pit of consciousness; risen up to "
           "accomplish the work of the gods."),
        _v(["udyadbhānusahasrābhā caturbāhusamanvitā |",
            "rāgasvarūpapāśāḍhyā krodhākārāṅkuśojjvalā"], "|| 2 ||",
           "Radiant as a thousand rising suns; endowed with four arms; holding "
           "the noose that is desire; bright with the goad that is wrath."),
        _v(["manorūpekṣukodaṇḍā pañcatanmātrasāyakā |",
            "nijāruṇaprabhāpūramajjadbrahmāṇḍamaṇḍalā"], "|| 3 ||",
           "Whose sugarcane bow is the mind; whose five arrows are the subtle "
           "elements; in the flood of whose own red radiance the whole sphere of "
           "the universe is bathed."),
        _v(["campakāśokapunnāgasaugandhikalasatkacā |",
            "kuruvindamaṇiśreṇīkanatkoṭīramaṇḍitā"], "|| 4 ||",
           "Her hair bright with campaka, aśoka, punnāga and fragrant blossoms; "
           "adorned with a crown gleaming with rows of ruby."),
        _v(["aṣṭamīcandravibhrājadalikasthalaśobhitā |",
            "mukhacandrakalaṅkābhamṛganābhiviśeṣakā"], "|| 5 ||",
           "Graced with a brow that shines like the moon of the eighth night; "
           "her musk mark like the shadow upon the moon of her face."),
        _v(["vadanasmaramāṅgalyagṛhatoraṇacillikā |",
            "vaktralakṣmīparīvāhacalanmīnābhalocanā"], "|| 6 ||",
           "Her brows the festal arch over the bridal house of Love that is her "
           "face; her eyes like fish darting in the flowing stream of her face's "
           "beauty."),
        _v(["navacampakapuṣpābhanāsādaṇḍavirājitā |",
            "tārākāntitiraskārināsābharaṇabhāsurā"], "|| 7 ||",
           "Resplendent with a nose fair as a fresh campaka bud; brilliant with "
           "a nose-jewel that outshines the lustre of the stars."),
        _v(["kadambamañjarīkḷiptakarṇapūramanoharā |",
            "tāṭaṅkayugalībhūtatapanoḍupamaṇḍalā"], "|| 8 ||",
           "Enchanting, with a cluster of kadamba blossoms set at her ear; the "
           "orbs of sun and moon become the pair of her earrings."),
        _v(["padmarāgaśilādarśaparibhāvikapolabhūḥ |",
            "navavidrumabimbaśrīnyakkāriradanacchadā"], "|| 9 ||",
           "Her cheeks like mirrors of ruby stone; her lips putting to shame the "
           "beauty of fresh coral and the bimba fruit."),
        _v(["śuddhavidyāṅkurākāradvijapaṅktidvayojjvalā |",
            "karpūravīṭikāmodasamākarṣidigantarā"], "|| 10 ||",
           "Bright with her two rows of teeth, shaped like the sprouting of pure "
           "Knowledge; the fragrance of her camphor-scented betel drawing to "
           "itself the whole horizon."),
        _v(["nijasallāpamādhuryavinirbhartsitakacchapī |",
            "mandasmitaprabhāpūramajjatkāmeśamānasā"], "|| 11 ||",
           "The sweetness of whose speech puts to shame Sarasvatī's lute; in the "
           "flood of whose gentle smile the mind of Kāmeśvara is drowned."),
        _v(["anākalitasādṛśyacibukaśrīvirājitā |",
            "kāmeśabaddhamāṅgalyasūtraśobhitakandharā"], "|| 12 ||",
           "Resplendent with the beauty of a chin beyond all comparison; her "
           "throat graced by the marriage-thread bound there by Kāmeśvara."),
        _v(["kanakāṅgadakeyūrakamanīyabhujānvitā |",
            "ratnagraiveyacintākalolamuktāphalānvitā"], "|| 13 ||",
           "Her lovely arms circled with golden armlets and bracelets; wearing a "
           "jewelled necklace and a pendant of glimmering pearls."),
        _v(["kāmeśvarapremaratnamaṇipratipaṇastanī |",
            "nābhyālavālaromālilatāphalakucadvayī"], "|| 14 ||",
           "Whose breasts are the price paid for the jewel of Kāmeśvara's love; "
           "whose breasts are the twin fruit of the creeper of hair rising from "
           "the basin of her navel."),
        _v(["lakṣyaromalatādhāratāsamunneyamadhyamā |",
            "stanabhāradalanmadhyapaṭṭabandhavalitrayā"], "|| 15 ||",
           "Whose waist can only be inferred as the support of that slender "
           "line of hair; the three folds at her waist a girdle binding a middle "
           "that seems to break beneath the weight of her breasts."),
        _v(["aruṇāruṇakausumbhavastrabhāsvatkaṭītaṭī |",
            "ratnakiṅkiṇikāramyaraśanādāmabhūṣitā"], "|| 16 ||",
           "The slope of her hips bright with safflower-red silk; adorned with a "
           "lovely girdle strung with jewelled bells."),
        _v(["kāmeśajñātasaubhāgyamārdavorudvayānvitā |",
            "māṇikyamukuṭākārajānudvayavirājitā"], "|| 17 ||",
           "Whose two thighs, soft and blessed, are known to Kāmeśvara alone; "
           "resplendent with knees shaped like crowns of ruby."),
        _v(["indragopaparikṣiptasmaratūṇābhajaṅghikā |",
            "gūḍhagulphā kūrmapṛṣṭhajayiṣṇuprapadānvitā"], "|| 18 ||",
           "Her calves like Love's quivers strewn with crimson insects; her "
           "ankles hidden; the arches of her feet surpassing the tortoise's "
           "shell."),
        _v(["nakhadīdhitisaṃchannanamajjanatamoguṇā |",
            "padadvayaprabhājālaparākṛtasaroruhā"], "|| 19 ||",
           "The radiance of whose toenails dispels the darkness in those who bow "
           "to her; the net of light from her two feet putting the lotus to "
           "shame."),
        _v(["siñjānamaṇimañjīramaṇḍitaśrīpadāmbujā |",
            "marālīmandagamanā mahālāvaṇyaśevadhiḥ"], "|| 20 ||",
           "Her lotus feet adorned with softly ringing jewelled anklets; whose "
           "gait is the slow grace of a swan; the very treasury of great "
           "loveliness."),
        _v(["sarvāruṇā'navadyāṅgī sarvābharaṇabhūṣitā |",
            "śivakāmeśvarāṅkasthā śivā svādhīnavallabhā"], "|| 21 ||",
           "All-red; of faultless limbs; adorned with every ornament; seated on "
           "the lap of Śiva-Kāmeśvara; the auspicious one; she whose beloved is "
           "wholly her own."),
        _v(["sumerumadhyaśṛṅgasthā śrīmannagaranāyikā |",
            "cintāmaṇigṛhāntasthā pañcabrahmāsanasthitā"], "|| 22 ||",
           "Dwelling on the middle peak of Meru; mistress of the glorious City; "
           "abiding within the house of the wish-granting gem; seated on the "
           "throne of the five Brahmās."),
        _v(["mahāpadmāṭavīsaṃsthā kadambavanavāsinī |",
            "sudhāsāgaramadhyasthā kāmākṣī kāmadāyinī"], "|| 23 ||",
           "Dwelling in the great forest of lotuses; inhabiting the kadamba "
           "grove; abiding in the midst of the ocean of nectar; Kāmākṣī, whose "
           "eyes are love; giver of every desire."),
        _v(["devarṣigaṇasaṃghātastūyamānātmavaibhavā |",
            "bhaṇḍāsuravadhodyuktaśaktisenāsamanvitā"], "|| 24 ||",
           "Whose own majesty is hymned by hosts of gods and seers; attended by "
           "the army of Śaktis roused to slay Bhaṇḍāsura."),
        _v(["sampatkarīsamārūḍhasindhuravrajasevitā |",
            "aśvārūḍhādhiṣṭhitāśvakoṭikoṭibhirāvṛtā"], "|| 25 ||",
           "Served by herds of elephants mounted by Sampatkarī; surrounded by "
           "many millions of horses commanded by Aśvārūḍhā."),
        _v(["cakrarājarathārūḍhasarvāyudhapariṣkṛtā |",
            "geyacakrarathārūḍhamantriṇīparisevitā"], "|| 26 ||",
           "Mounted on the chariot Cakrarāja, furnished with every weapon; "
           "attended by Mantriṇī riding the chariot Geyacakra."),
        _v(["kiricakrarathārūḍhadaṇḍanāthāpuraskṛtā |",
            "jvālāmālinikākṣiptavahniprākāramadhyagā"], "|| 27 ||",
           "Preceded by Daṇḍanāthā mounted on the chariot Kiricakra; moving "
           "within the rampart of fire flung up by Jvālāmālinī."),
        _v(["bhaṇḍasainyavadhodyuktaśaktivikramaharṣitā |",
            "nityāparākramāṭopanirīkṣaṇasamutsukā"], "|| 28 ||",
           "Delighted by the valour of the Śaktis bent on destroying Bhaṇḍa's "
           "army; eager to behold the swelling prowess of the Nityā "
           "goddesses."),
        _v(["bhaṇḍaputravadhodyuktabālāvikramananditā |",
            "mantriṇyambāviracitaviṣaṅgavadhatoṣitā"], "|| 29 ||",
           "Gladdened by the valour of Bālā, set on slaying Bhaṇḍa's sons; "
           "pleased by the death of Viṣaṅga brought about by Mother Mantriṇī."),
        _v(["viśukraprāṇaharaṇavārāhīvīryananditā |",
            "kāmeśvaramukhālokakalpitaśrīgaṇeśvarā"], "|| 30 ||",
           "Rejoicing in the might of Vārāhī, who took the life of Viśukra; who "
           "brought forth Śrī Gaṇeśa by a glance at Kāmeśvara's face."),
        _v(["mahāgaṇeśanirbhinnavighnayantrapraharṣitā |",
            "bhaṇḍāsurendranirmuktaśastrapratyastravarṣiṇī"], "|| 31 ||",
           "Delighted when great Gaṇeśa shattered the obstacle-engine; who "
           "rained counter-weapons against the arms loosed by Bhaṇḍāsura."),
        _v(["karāṅgulinakhotpannanārāyaṇadaśākṛtiḥ |",
            "mahāpāśupatāstrāgninirdagdhāsurasainikā"], "|| 32 ||",
           "From the nails of whose fingers arose the ten forms of Nārāyaṇa; who "
           "burned the demon armies in the fire of the great Pāśupata weapon."),
        _v(["kāmeśvarāstranirdagdhasabhaṇḍāsuraśūnyakā |",
            "brahmopendramahendrādidevasaṃstutavaibhavā"], "|| 33 ||",
           "Who consumed Bhaṇḍāsura and his city Śūnyaka with the Kāmeśvara "
           "weapon; whose majesty is hymned by Brahmā, Upendra, great Indra and "
           "the rest."),
        _v(["haranetrāgnisaṃdagdhakāmasañjīvanauṣadhiḥ |",
            "śrīmadvāgbhavakūṭaikasvarūpamukhapaṅkajā"], "|| 34 ||",
           "The herb that restored to life Kāma, burnt by the fire of Hara's "
           "eye; whose lotus face is the very form of the glorious Vāgbhava "
           "syllable-group."),
        _v(["kaṇṭhādhaḥkaṭiparyantamadhyakūṭasvarūpiṇī |",
            "śaktikūṭaikatāpannakaṭyadhobhāgadhāriṇī"], "|| 35 ||",
           "Whose form from throat to waist is the middle syllable-group; who "
           "bears below the waist the part that is one with the Śakti "
           "syllable-group."),
        _v(["mūlamantrātmikā mūlakūṭatrayakalebarā |",
            "kulāmṛtaikarasikā kulasaṃketapālinī"], "|| 36 ||",
           "Whose Self is the root mantra; whose body is the three root "
           "syllable-groups; who savours the one nectar of the Kula; guardian of "
           "the Kula's secret sign."),
        _v(["kulāṅganā kulāntasthā kaulinī kulayoginī |",
            "akulā samayāntasthā samayācāratatparā"], "|| 37 ||",
           "The lady of the Kula; abiding within the Kula; the Kaulinī; the "
           "yoginī of the Kula; she who is beyond Kula; dwelling within Samaya; "
           "devoted to the Samaya observance."),
        _v(["mūlādhāraikanilayā brahmagranthivibhedinī |",
            "maṇipūrāntaruditā viṣṇugranthivibhedinī"], "|| 38 ||",
           "Whose sole abode is the mūlādhāra; piercer of the knot of Brahmā; "
           "risen within the maṇipūra; piercer of the knot of Viṣṇu."),
        _v(["ājñācakrāntarālasthā rudragranthivibhedinī |",
            "sahasrārāmbujārūḍhā sudhāsārābhivarṣiṇī"], "|| 39 ||",
           "Abiding within the ājñā-cakra; piercer of the knot of Rudra; risen "
           "to the thousand-petalled lotus; showering down the essence of "
           "nectar."),
        _v(["taḍillatāsamaruciḥ ṣaṭcakroparisaṃsthitā |",
            "mahāśaktiḥ kuṇḍalinī bisatantutanīyasī"], "|| 40 ||",
           "Whose lustre is a flash of lightning; established above the six "
           "cakras; the great Power; the coiled Kuṇḍalinī; finer than the fibre "
           "of a lotus stalk."),
        _v(["bhavānī bhāvanāgamyā bhavāraṇyakuṭhārikā |",
            "bhadrapriyā bhadramūrtir bhaktasaubhāgyadāyinī"], "|| 41 ||",
           "Bhavānī; reached by contemplation; the axe that fells the forest of "
           "becoming; who loves what is good; whose form is blessing; giver of "
           "good fortune to devotees."),
        _v(["bhaktipriyā bhaktigamyā bhaktivaśyā bhayāpahā |",
            "śāmbhavī śāradārādhyā śarvāṇī śarmadāyinī"], "|| 42 ||",
           "Who loves devotion; reached by devotion; won over by devotion; "
           "remover of fear; consort of Śambhu; worshipped by Śāradā; Śarvāṇī; "
           "giver of happiness."),
        _v(["śāṅkarī śrīkarī sādhvī śaraccandranibhānanā |",
            "śātodarī śāntimatī nirādhārā nirañjanā"], "|| 43 ||",
           "Consort of Śaṅkara; maker of splendour; the virtuous; whose face is "
           "like the autumn moon; of slender waist; full of peace; without "
           "support; without stain."),
        _v(["nirlepā nirmalā nityā nirākārā nirākulā |",
            "nirguṇā niṣkalā śāntā niṣkāmā nirupaplavā"], "|| 44 ||",
           "Untouched by anything; spotless; eternal; formless; unagitated; "
           "beyond the qualities; without parts; tranquil; free of desire; "
           "beyond all calamity."),
        _v(["nityamuktā nirvikārā niṣprapañcā nirāśrayā |",
            "nityaśuddhā nityabuddhā niravadyā nirantarā"], "|| 45 ||",
           "Ever free; changeless; beyond all manifoldness; needing no support; "
           "ever pure; ever awake; blameless; without interval."),
        _v(["niṣkāraṇā niṣkalaṅkā nirupādhir nirīśvarā |",
            "nīrāgā rāgamathanī nirmadā madanāśinī"], "|| 46 ||",
           "Without cause; without blemish; without limiting adjunct; having no "
           "lord above her; free of passion; destroyer of passion; free of "
           "pride; destroyer of pride."),
        _v(["niścintā nirahaṃkārā nirmohā mohanāśinī |",
            "nirmamā mamatāhantrī niṣpāpā pāpanāśinī"], "|| 47 ||",
           "Free of anxiety; free of ego; free of delusion; destroyer of "
           "delusion; free of 'mine'; slayer of possessiveness; sinless; "
           "destroyer of sin."),
        _v(["niṣkrodhā krodhaśamanī nirlobhā lobhanāśinī |",
            "niḥsaṃśayā saṃśayaghnī nirbhavā bhavanāśinī"], "|| 48 ||",
           "Free of anger; queller of anger; free of greed; destroyer of greed; "
           "free of doubt; slayer of doubt; unborn; destroyer of the round of "
           "becoming."),
        _v(["nirvikalpā nirābādhā nirbhedā bhedanāśinī |",
            "nirnāśā mṛtyumathanī niṣkriyā niṣparigrahā"], "|| 49 ||",
           "Beyond all mental construction; unobstructed; without division; "
           "destroyer of division; imperishable; churner of death; beyond "
           "action; grasping at nothing."),
        _v(["nistulā nīlacikurā nirapāyā niratyayā |",
            "durlabhā durgamā durgā duḥkhahantrī sukhapradā"], "|| 50 ||",
           "Beyond compare; dark-haired; imperishable; beyond transgression; "
           "hard to attain; hard to approach; Durgā; slayer of sorrow; giver of "
           "happiness."),
        _v(["duṣṭadūrā durācāraśamanī doṣavarjitā |",
            "sarvajñā sāndrakaruṇā samānādhikavarjitā"], "|| 51 ||",
           "Far from the wicked; queller of evil conduct; free of every fault; "
           "all-knowing; of dense compassion; having neither equal nor "
           "superior."),
        _v(["sarvaśaktimayī sarvamaṅgalā sadgatipradā |",
            "sarveśvarī sarvamayī sarvamantrasvarūpiṇī"], "|| 52 ||",
           "Made of all power; wholly auspicious; giver of the good goal; "
           "sovereign of all; comprising all; whose form is every mantra."),
        _v(["sarvayantrātmikā sarvatantrarūpā manonmanī |",
            "māheśvarī mahādevī mahālakṣmīr mṛḍapriyā"], "|| 53 ||",
           "Whose Self is every yantra; whose form is every tantra; the mind "
           "transcending mind; consort of Maheśvara; the great Goddess; "
           "Mahālakṣmī; beloved of Mṛḍa."),
        _v(["mahārūpā mahāpūjyā mahāpātakanāśinī |",
            "mahāmāyā mahāsattvā mahāśaktir mahāratiḥ"], "|| 54 ||",
           "Of great form; supremely worthy of worship; destroyer of the great "
           "sins; the great Māyā; of great being; the great Power; the great "
           "Delight."),
        _v(["mahābhogā mahaiśvaryā mahāvīryā mahābalā |",
            "mahābuddhir mahāsiddhir mahāyogeśvareśvarī"], "|| 55 ||",
           "Of great enjoyment; of great sovereignty; of great valour; of great "
           "strength; of great intelligence; of great attainment; Empress of the "
           "great lords of yoga."),
        _v(["mahātantrā mahāmantrā mahāyantrā mahāsanā |",
            "mahāyāgakramārādhyā mahābhairavapūjitā"], "|| 56 ||",
           "The great tantra; the great mantra; the great yantra; of the great "
           "seat; worshipped by the sequence of the great sacrifice; adored by "
           "the great Bhairava."),
        _v(["maheśvaramahākalpamahātāṇḍavasākṣiṇī |",
            "mahākāmeśamahiṣī mahātripurasundarī"], "|| 57 ||",
           "Witness of the great tāṇḍava dance of Maheśvara at the great "
           "dissolution; queen of the great Kāmeśa; the great Tripurasundarī."),
        _v(["catuḥṣaṣṭyupacārāḍhyā catuḥṣaṣṭikalāmayī |",
            "mahācatuḥṣaṣṭikoṭiyoginīgaṇasevitā"], "|| 58 ||",
           "Honoured with the sixty-four services; comprising the sixty-four "
           "arts; served by the hosts of the great sixty-four crores of "
           "yoginīs."),
        _v(["manuvidyā candravidyā candramaṇḍalamadhyagā |",
            "cārurūpā cāruhāsā cārucandrakalādharā"], "|| 59 ||",
           "The Manu-vidyā; the Candra-vidyā; abiding in the midst of the moon's "
           "orb; of lovely form; of lovely smile; wearing the lovely crescent."),
        _v(["carācarajagannāthā cakrarājaniketanā |",
            "pārvatī padmanayanā padmarāgasamaprabhā"], "|| 60 ||",
           "Mistress of the world, moving and unmoving; whose dwelling is the "
           "Cakrarāja; Pārvatī; lotus-eyed; radiant as a ruby."),
        _v(["pañcapretāsanāsīnā pañcabrahmasvarūpiṇī |",
            "cinmayī paramānandā vijñānaghanarūpiṇī"], "|| 61 ||",
           "Seated on the couch of the five corpse-gods; whose form is the five "
           "Brahmās; made of consciousness; supreme bliss; whose form is a mass "
           "of pure knowing."),
        _v(["dhyānadhyātṛdhyeyarūpā dharmādharmavivarjitā |",
            "viśvarūpā jāgariṇī svapantī taijasātmikā"], "|| 62 ||",
           "Whose form is meditation, meditator and object of meditation; beyond "
           "both dharma and its opposite; the Universal in waking; the dreaming "
           "one; whose Self is the shining dream-state."),
        _v(["suptā prājñātmikā turyā sarvāvasthāvivarjitā |",
            "sṛṣṭikartrī brahmarūpā goptrī govindarūpiṇī"], "|| 63 ||",
           "The sleeping one; whose Self is the deep-sleep knower; the Fourth; "
           "free of all states; maker of creation, in the form of Brahmā; "
           "protectress, in the form of Govinda."),
        _v(["saṃhāriṇī rudrarūpā tirodhānakarīśvarī |",
            "sadāśivā'nugrahadā pañcakṛtyaparāyaṇā"], "|| 64 ||",
           "The destroyer, in the form of Rudra; she who veils, as Īśvara; "
           "Sadāśiva, bestower of grace; devoted to the five cosmic acts."),
        _v(["bhānumaṇḍalamadhyasthā bhairavī bhagamālinī |",
            "padmāsanā bhagavatī padmanābhasahodarī"], "|| 65 ||",
           "Abiding in the midst of the sun's orb; Bhairavī; Bhagamālinī; seated "
           "on the lotus; the Blessed Lady; sister of the lotus-naveled Viṣṇu."),
        _v(["unmeṣanimiṣotpannavipannabhuvanāvalī |",
            "sahasraśīrṣavadanā sahasrākṣī sahasrapāt"], "|| 66 ||",
           "By whose opening and closing of the eyes rows of worlds arise and "
           "perish; of a thousand heads and faces; thousand-eyed; "
           "thousand-footed."),
        _v(["ābrahmakīṭajananī varṇāśramavidhāyinī |",
            "nijājñārūpanigamā puṇyāpuṇyaphalapradā"], "|| 67 ||",
           "Mother of all from Brahmā to the worm; ordainer of the orders and "
           "stages of life; whose own command takes form as scripture; giver of "
           "the fruit of merit and demerit."),
        _v(["śrutisīmantasindūrīkṛtapādābjadhūlikā |",
            "sakalāgamasandohaśuktisampuṭamauktikā"], "|| 68 ||",
           "The dust of whose lotus feet reddens the parting of the Vedas' hair "
           "like vermilion; the pearl within the closed shell that is the whole "
           "body of the āgamas."),
        _v(["puruṣārthapradā pūrṇā bhoginī bhuvaneśvarī |",
            "ambikā'nādinidhanā haribrahmendrasevitā"], "|| 69 ||",
           "Giver of the ends of human life; the full; the enjoyer; sovereign of "
           "the worlds; the Mother; without beginning or end; served by Hari, "
           "Brahmā and Indra."),
        _v(["nārāyaṇī nādarūpā nāmarūpavivarjitā |",
            "hrīṃkārī hrīmatī hṛdyā heyopādeyavarjitā"], "|| 70 ||",
           "Nārāyaṇī; whose form is primal sound; free of name and form; she of "
           "the seed hrīṃ; possessed of modesty; dear to the heart; beyond what "
           "must be shunned and what must be sought."),
        _v(["rājarājārcitā rājñī ramyā rājīvalocanā |",
            "rañjanī ramaṇī rasyā raṇatkiṅkiṇimekhalā"], "|| 71 ||",
           "Worshipped by the king of kings; the queen; the delightful; "
           "lotus-eyed; the gladdener; the charming; the savoured; whose girdle "
           "is strung with tinkling bells."),
        _v(["ramā rākenduvadanā ratirūpā ratipriyā |",
            "rakṣākarī rākṣasaghnī rāmā ramaṇalampaṭā"], "|| 72 ||",
           "Ramā; whose face is the full moon; whose form is delight; who loves "
           "delight; the protectress; slayer of demons; the lovely; devoted to "
           "her beloved."),
        _v(["kāmyā kāmakalārūpā kadambakusumapriyā |",
            "kalyāṇī jagatīkandā karuṇārasasāgarā"], "|| 73 ||",
           "The desirable; whose form is the kāmakalā; who loves the kadamba "
           "blossom; the auspicious; the root-bulb of the world; an ocean of the "
           "essence of compassion."),
        _v(["kalāvatī kalālāpā kāntā kādambarīpriyā |",
            "varadā vāmanayanā vāruṇīmadavihvalā"], "|| 74 ||",
           "Rich in arts; whose speech is art; the beloved; who loves the "
           "kādambarī; giver of boons; of beautiful eyes; swaying with the "
           "rapture of the nectar-wine."),
        _v(["viśvādhikā vedavedyā vindhyācalanivāsinī |",
            "vidhātrī vedajananī viṣṇumāyā vilāsinī"], "|| 75 ||",
           "Greater than the universe; knowable through the Veda; dwelling on "
           "the Vindhya hill; the ordainer; mother of the Vedas; the māyā of "
           "Viṣṇu; the sportive."),
        _v(["kṣetrasvarūpā kṣetreśī kṣetrakṣetrajñapālinī |",
            "kṣayavṛddhivinirmuktā kṣetrapālasamarcitā"], "|| 76 ||",
           "Whose form is the field; mistress of the field; protectress of both "
           "field and knower of the field; free of waning and waxing; worshipped "
           "by the guardians of the field."),
        _v(["vijayā vimalā vandyā vandārujanavatsalā |",
            "vāgvādinī vāmakeśī vahnimaṇḍalavāsinī"], "|| 77 ||",
           "The victorious; the stainless; the adorable; tender to those who "
           "bow; who speaks through speech; of beautiful hair; dwelling in the "
           "orb of fire."),
        _v(["bhaktimatkalpalatikā paśupāśavimocinī |",
            "saṃhṛtāśeṣapāṣaṇḍā sadācārapravartikā"], "|| 78 ||",
           "The wish-granting creeper for the devout; who looses the bonds of "
           "the fettered soul; who has swept away every false doctrine; who sets "
           "right conduct in motion."),
        _v(["tāpatrayāgnisantaptasamāhlādanacandrikā |",
            "taruṇī tāpasārādhyā tanumadhyā tamo'pahā"], "|| 79 ||",
           "The moonlight that soothes those scorched by the fire of the three "
           "afflictions; the youthful; worshipped by ascetics; of slender waist; "
           "dispeller of darkness."),
        _v(["citistatpadalakṣyārthā cidekarasarūpiṇī |",
            "svātmānandalavībhūtabrahmādyānandasantatiḥ"], "|| 80 ||",
           "Pure consciousness, the meaning indicated by the word 'That'; whose "
           "form is the one savour of awareness; the whole succession of the "
           "bliss of Brahmā and the gods being but a fragment of the bliss of "
           "her own Self."),
        _v(["parā pratyakcitīrūpā paśyantī paradevatā |",
            "madhyamā vaikharīrūpā bhaktamānasahaṃsikā"], "|| 81 ||",
           "The supreme; whose form is the inward-turned consciousness; speech "
           "as paśyantī; the highest deity; speech as madhyamā; speech as "
           "vaikharī; the swan in the lake of the devotee's mind."),
        _v(["kāmeśvaraprāṇanāḍī kṛtajñā kāmapūjitā |",
            "śṛṅgārarasasampūrṇā jayā jālandharasthitā"], "|| 82 ||",
           "The very life-channel of Kāmeśvara; who knows all that is done; "
           "worshipped by Kāma; brimming with the mood of love; the victorious; "
           "abiding in the seat Jālandhara."),
        _v(["oḍyāṇapīṭhanilayā bindumaṇḍalavāsinī |",
            "rahoyāgakramārādhyā rahastarpaṇatarpitā"], "|| 83 ||",
           "Whose abode is the seat Oḍyāṇa; dwelling in the sphere of the "
           "bindu; worshipped by the sequence of the secret rite; satisfied by "
           "the secret offering."),
        _v(["sadyaḥprasādinī viśvasākṣiṇī sākṣivarjitā |",
            "ṣaḍaṅgadevatāyuktā ṣāḍguṇyaparipūritā"], "|| 84 ||",
           "Who grants grace at once; witness of the universe; yet herself "
           "without any witness; attended by the deities of the six limbs; "
           "filled with the six excellences."),
        _v(["nityaklinnā nirupamā nirvāṇasukhadāyinī |",
            "nityāṣoḍaśikārūpā śrīkaṇṭhārdhaśarīriṇī"], "|| 85 ||",
           "Ever moist with compassion; beyond compare; giver of the bliss of "
           "nirvāṇa; whose form is the sixteen eternal Nityās; who is half the "
           "body of Śrīkaṇṭha."),
        _v(["prabhāvatī prabhārūpā prasiddhā parameśvarī |",
            "mūlaprakṛtiravyaktā vyaktāvyaktasvarūpiṇī"], "|| 86 ||",
           "Full of radiance; whose form is radiance; the renowned; the supreme "
           "sovereign; root Nature, unmanifest; whose form is both manifest and "
           "unmanifest."),
        _v(["vyāpinī vividhākārā vidyāvidyāsvarūpiṇī |",
            "mahākāmeśanayanakumudāhlādakaumudī"], "|| 87 ||",
           "The all-pervading; of manifold forms; whose form is both knowledge "
           "and ignorance; the moonlight that gladdens the night-lotuses of "
           "great Kāmeśa's eyes."),
        _v(["bhaktahārdatamobhedabhānumadbhānusantatiḥ |",
            "śivadūtī śivārādhyā śivamūrtiḥ śivaṅkarī"], "|| 88 ||",
           "A stream of sunlight breaking the darkness in the devotee's heart; "
           "she whose messenger is Śiva; worshipped by Śiva; whose form is Śiva; "
           "maker of good."),
        _v(["śivapriyā śivaparā śiṣṭeṣṭā śiṣṭapūjitā |",
            "aprameyā svaprakāśā manovācāmagocarā"], "|| 89 ||",
           "Beloved of Śiva; devoted to Śiva; dear to the wise; worshipped by "
           "the wise; immeasurable; self-luminous; beyond the range of mind and "
           "speech."),
        _v(["cicchaktiścetanārūpā jaḍaśaktirjaḍātmikā |",
            "gāyatrī vyāhṛtiḥ sandhyā dvijabṛndaniṣevitā"], "|| 90 ||",
           "The power of consciousness, whose form is awareness; the power of "
           "matter, whose Self is the inert; Gāyatrī; the vyāhṛtis; the twilight "
           "worship; served by the throng of the twice-born."),
        _v(["tattvāsanā tattvamayī pañcakośāntarasthitā |",
            "niḥsīmamahimā nityayauvanā madaśālinī"], "|| 91 ||",
           "Whose seat is Reality; made of Reality; abiding within the five "
           "sheaths; of boundless majesty; of unfading youth; radiant with "
           "rapture."),
        _v(["madaghūrṇitaraktākṣī madapāṭalagaṇḍabhūḥ |",
            "candanadravadigdhāṅgī cāmpeyakusumapriyā"], "|| 92 ||",
           "Her reddened eyes rolling with rapture; her cheeks flushed rosy with "
           "it; her limbs anointed with liquid sandal; who loves the campaka "
           "flower."),
        _v(["kuśalā komalākārā kurukullā kuleśvarī |",
            "kulakuṇḍālayā kaulamārgatatparasevitā"], "|| 93 ||",
           "The skilful; of tender form; Kurukullā; mistress of the Kula; whose "
           "abode is the Kula-kuṇḍa; served by those devoted to the Kaula "
           "path."),
        _v(["kumāragaṇanāthāmbā tuṣṭiḥ puṣṭirmatirdhṛtiḥ |",
            "śāntiḥ svastimatī kāntirnandinī vighnanāśinī"], "|| 94 ||",
           "Mother of Kumāra and of Gaṇanātha; contentment; nourishment; "
           "understanding; steadfastness; peace; well-being; loveliness; the "
           "gladdener; destroyer of obstacles."),
        _v(["tejovatī trinayanā lolākṣīkāmarūpiṇī |",
            "mālinī haṃsinī mātā malayācalavāsinī"], "|| 95 ||",
           "Full of splendour; three-eyed; of restless eyes, taking the form she "
           "wills; the garlanded; the swan-like; the Mother; dwelling on the "
           "Malaya hill."),
        _v(["sumukhī nalinī subhrūḥ śobhanā suranāyikā |",
            "kālakaṇṭhī kāntimatī kṣobhiṇī sūkṣmarūpiṇī"], "|| 96 ||",
           "Of fair face; lotus-like; of lovely brows; the beautiful; leader of "
           "the gods; consort of the dark-throated Śiva; full of lustre; who "
           "stirs all; of subtle form."),
        _v(["vajreśvarī vāmadevī vayo'vasthāvivarjitā |",
            "siddheśvarī siddhavidyā siddhamātā yaśasvinī"], "|| 97 ||",
           "Vajreśvarī; Vāmadevī; untouched by age or condition; mistress of the "
           "siddhas; the perfected knowledge; mother of the siddhas; the "
           "glorious."),
        _v(["viśuddhicakranilayā''raktavarṇā trilocanā |",
            "khaṭvāṅgādipraharaṇā vadanaikasamanvitā"], "|| 98 ||",
           "Whose abode is the viśuddhi-cakra; of red hue; three-eyed; armed "
           "with the skull-staff and other weapons; having a single face."),
        _v(["pāyasānnapriyā tvaksthā paśulokabhayaṅkarī |",
            "amṛtādimahāśaktisaṃvṛtā ḍākinīśvarī"], "|| 99 ||",
           "Who loves the offering of milk-rice; abiding in the skin; a terror "
           "to the world of the fettered; surrounded by the great Śaktis "
           "beginning with Amṛtā; the Ḍākinī sovereign."),
        _v(["anāhatābjanilayā śyāmābhā vadanadvayā |",
            "daṃṣṭrojjvalā'kṣamālādidharā rudhirasaṃsthitā"], "|| 100 ||",
           "Whose abode is the lotus of the anāhata; dark-hued; two-faced; "
           "bright with tusks; bearing the rosary and the rest; abiding in the "
           "blood."),
        _v(["kālarātryādiśaktyaughavṛtā snigdhaudanapriyā |",
            "mahāvīrendravaradā rākiṇyambāsvarūpiṇī"], "|| 101 ||",
           "Encircled by the flood of Śaktis beginning with Kālarātri; who loves "
           "the offering of rich rice; giver of boons to the great heroes; whose "
           "form is Mother Rākiṇī."),
        _v(["maṇipūrābjanilayā vadanatrayasaṃyutā |",
            "vajrādikāyudhopetā ḍāmaryādibhirāvṛtā"], "|| 102 ||",
           "Whose abode is the lotus of the maṇipūra; endowed with three faces; "
           "furnished with the thunderbolt and other weapons; surrounded by "
           "Ḍāmarī and the rest."),
        _v(["raktavarṇā māṃsaniṣṭhā guḍānnaprītamānasā |",
            "samastabhaktasukhadā lākinyambāsvarūpiṇī"], "|| 103 ||",
           "Of red hue; abiding in the flesh; her heart pleased by the offering "
           "of sweetened rice; giver of happiness to every devotee; whose form "
           "is Mother Lākinī."),
        _v(["svādhiṣṭhānāmbujagatā caturvaktramanoharā |",
            "śūlādyāyudhasampannā pītavarṇā'tigarvitā"], "|| 104 ||",
           "Dwelling in the lotus of the svādhiṣṭhāna; enchanting, with four "
           "faces; furnished with the trident and other weapons; of yellow hue; "
           "exceedingly proud."),
        _v(["medoniṣṭhā madhuprītā bandhinyādisamanvitā |",
            "dadhyannāsaktahṛdayā kākinīrūpadhāriṇī"], "|| 105 ||",
           "Abiding in the marrow-fat; delighting in honey; attended by Bandhinī "
           "and the rest; her heart drawn to the offering of curd-rice; bearing "
           "the form of Kākinī."),
        _v(["mūlādhārāmbujārūḍhā pañcavaktrā'sthisaṃsthitā |",
            "aṅkuśādipraharaṇā varadādiniṣevitā"], "|| 106 ||",
           "Risen in the lotus of the mūlādhāra; five-faced; abiding in the "
           "bones; armed with the goad and the rest; served by Varadā and the "
           "others."),
        _v(["mudgaudanāsaktacittā sākinyambāsvarūpiṇī |",
            "ājñācakrābjanilayā śuklavarṇā ṣaḍānanā"], "|| 107 ||",
           "Her mind drawn to the offering of lentil-rice; whose form is Mother "
           "Sākinī; whose abode is the lotus of the ājñā-cakra; of white hue; "
           "six-faced."),
        _v(["majjāsaṃsthā haṃsavatīmukhyaśaktisamanvitā |",
            "haridrānnaikarasikā hākinīrūpadhāriṇī"], "|| 108 ||",
           "Abiding in the marrow; attended by the Śaktis led by Haṃsavatī; "
           "savouring the offering of turmeric-rice; bearing the form of "
           "Hākinī."),
        _v(["sahasradalapadmasthā sarvavarṇopaśobhitā |",
            "sarvāyudhadharā śuklasaṃsthitā sarvatomukhī"], "|| 109 ||",
           "Abiding in the thousand-petalled lotus; adorned with every letter "
           "and colour; bearing all weapons; established in the vital essence; "
           "her faces turned every way."),
        _v(["sarvaudanaprītacittā yākinyambāsvarūpiṇī |",
            "svāhā svadhā'matirmedhā śrutiḥ smṛtiranuttamā"], "|| 110 ||",
           "Her heart pleased with every offering of rice; whose form is Mother "
           "Yākinī; the call svāhā; the call svadhā; unknowing and "
           "understanding; revelation; tradition; she than whom none is "
           "higher."),
        _v(["puṇyakīrtiḥ puṇyalabhyā puṇyaśravaṇakīrtanā |",
            "pulomajārcitā bandhamocanī bandhurālakā"], "|| 111 ||",
           "Of holy renown; won by merit; the hearing and reciting of whom is "
           "itself merit; worshipped by Indra's queen; who looses every bond; of "
           "beautiful curling hair."),
        _v(["vimarśarūpiṇī vidyā viyadādijagatprasūḥ |",
            "sarvavyādhipraśamanī sarvamṛtyunivāriṇī"], "|| 112 ||",
           "Whose form is reflective awareness; Knowledge itself; mother of the "
           "world beginning with space; queller of every disease; averter of "
           "every death."),
        _v(["agragaṇyā'cintyarūpā kalikalmaṣanāśinī |",
            "kātyāyanī kālahantrī kamalākṣaniṣevitā"], "|| 113 ||",
           "First to be counted; of unthinkable form; destroyer of the stain of "
           "the Kali age; Kātyāyanī; slayer of Time; served by the lotus-eyed "
           "Viṣṇu."),
        _v(["tāmbūlapūritamukhī dāḍimīkusumaprabhā |",
            "mṛgākṣī mohinī mukhyā mṛḍānī mitrarūpiṇī"], "|| 114 ||",
           "Her mouth filled with betel; radiant as the pomegranate flower; "
           "doe-eyed; the enchantress; the foremost; consort of Mṛḍa; whose form "
           "is the friend of all."),
        _v(["nityatṛptā bhaktanidhirniyantrī nikhileśvarī |",
            "maitryādivāsanālabhyā mahāpralayasākṣiṇī"], "|| 115 ||",
           "Ever content; the treasure of her devotees; the controller; "
           "sovereign of all; won by cultivating friendliness and the rest; "
           "witness of the great dissolution."),
        _v(["parā śaktiḥ parā niṣṭhā prajñānaghanarūpiṇī |",
            "mādhvīpānālasā mattā mātṛkāvarṇarūpiṇī"], "|| 116 ||",
           "The supreme Power; the supreme ground; whose form is a mass of pure "
           "wisdom; languid with the nectar-draught; rapturous; whose form is "
           "the letters of the mātṛkā."),
        _v(["mahākailāsanilayā mṛṇālamṛdudorlatā |",
            "mahanīyā dayāmūrtirmahāsāmrājyaśālinī"], "|| 117 ||",
           "Whose abode is the great Kailāsa; her creeper-arms soft as lotus "
           "fibre; the venerable; compassion embodied; resplendent in her great "
           "sovereignty."),
        _v(["ātmavidyā mahāvidyā śrīvidyā kāmasevitā |",
            "śrīṣoḍaśākṣarīvidyā trikūṭā kāmakoṭikā"], "|| 118 ||",
           "The knowledge of the Self; the great Knowledge; the Śrīvidyā; served "
           "by Kāma; the glorious sixteen-syllabled vidyā; of the three "
           "syllable-groups; Kāmakoṭi."),
        _v(["kaṭākṣakiṅkarībhūtakamalākoṭisevitā |",
            "śiraḥsthitā candranibhā bhālasthendradhanuḥprabhā"], "|| 119 ||",
           "Served by crores of Lakṣmīs made her handmaids by a single glance; "
           "abiding in the head, resembling the moon; abiding in the brow, "
           "radiant as the rainbow."),
        _v(["hṛdayasthā raviprakhyā trikoṇāntaradīpikā |",
            "dākṣāyaṇī daityahantrī dakṣayajñavināśinī"], "|| 120 ||",
           "Abiding in the heart, bright as the sun; the lamp within the "
           "triangle; daughter of Dakṣa; slayer of demons; destroyer of Dakṣa's "
           "sacrifice."),
        _v(["darāndolitadīrghākṣī darahāsojjvalanmukhī |",
            "gurumūrtirguṇanidhirgomātā guhajanmabhūḥ"], "|| 121 ||",
           "Her long eyes gently moving; her face bright with a faint smile; "
           "whose form is the guru; a treasury of virtues; mother of the "
           "cow-tongued speech; the birthplace of Guha."),
        _v(["deveśī daṇḍanītisthā daharākāśarūpiṇī |",
            "pratipanmukhyarākāntatithimaṇḍalapūjitā"], "|| 122 ||",
           "Sovereign of the gods; established in the rule of justice; whose "
           "form is the tiny ether of the heart; worshipped in the circle of "
           "lunar days from the first to the full moon."),
        _v(["kalātmikā kalānāthā kāvyālāpavinodinī |",
            "sacāmararamāvāṇīsavyadakṣiṇasevitā"], "|| 123 ||",
           "Whose Self is the digits of the moon; mistress of those digits; "
           "delighting in the speech of poetry; attended on left and right by "
           "Ramā and Vāṇī bearing fly-whisks."),
        _v(["ādiśaktirameyā''tmā paramā pāvanākṛtiḥ |",
            "anekakoṭibrahmāṇḍajananī divyavigrahā"], "|| 124 ||",
           "The primal Power; the immeasurable Self; the supreme; of purifying "
           "form; mother of many crores of universes; of divine body."),
        _v(["klīṃkārī kevalā guhyā kaivalyapadadāyinī |",
            "tripurā trijagadvandyā trimūrtistridaśeśvarī"], "|| 125 ||",
           "She of the seed klīṃ; the absolute; the secret; giver of the state "
           "of aloneness; Tripurā; adored by the three worlds; the three forms; "
           "sovereign of the thirty gods."),
        _v(["tryakṣarī divyagandhāḍhyā sindūratilakāñcitā |",
            "umā śailendratanayā gaurī gandharvasevitā"], "|| 126 ||",
           "Of three syllables; rich with divine fragrance; marked with a "
           "vermilion tilaka; Umā; daughter of the mountain-king; Gaurī; served "
           "by gandharvas."),
        _v(["viśvagarbhā svarṇagarbhā varadā vāgadhīśvarī |",
            "dhyānagamyā'paricchedyā jñānadā jñānavigrahā"], "|| 127 ||",
           "In whose womb is the universe; the golden womb; giver of boons; "
           "sovereign of speech; reached by meditation; not to be divided; giver "
           "of knowledge; knowledge embodied."),
        _v(["sarvavedāntasaṃvedyā satyānandasvarūpiṇī |",
            "lopāmudrārcitā līlākḷiptabrahmāṇḍamaṇḍalā"], "|| 128 ||",
           "Known through all Vedānta; whose form is truth and bliss; worshipped "
           "by Lopāmudrā; who fashions the sphere of the universe in play."),
        _v(["adṛśyā dṛśyarahitā vijñātrī vedyavarjitā |",
            "yoginī yogadā yogyā yogānandā yugandharā"], "|| 129 ||",
           "The unseen; devoid of anything seen; the knower; having nothing to "
           "be known; the yoginī; giver of yoga; the worthy; the bliss of yoga; "
           "bearer of the ages."),
        _v(["icchāśaktijñānaśaktikriyāśaktisvarūpiṇī |",
            "sarvādhārā supratiṣṭhā sadasadrūpadhāriṇī"], "|| 130 ||",
           "Whose form is the power of will, the power of knowledge and the "
           "power of action; support of all; well established; bearing the form "
           "of both being and non-being."),
        _v(["aṣṭamūrtirajājaitrī lokayātrāvidhāyinī |",
            "ekākinī bhūmarūpā nirdvaitā dvaitavarjitā"], "|| 131 ||",
           "Of eight forms; conqueror of ignorance; who orders the course of the "
           "worlds; the solitary; whose form is the plenum; without duality; "
           "free of all dualism."),
        _v(["annadā vasudā vṛddhā brahmātmaikyasvarūpiṇī |",
            "bṛhatī brāhmaṇī brāhmī brahmānandā balipriyā"], "|| 132 ||",
           "Giver of food; giver of wealth; the ancient; whose form is the unity "
           "of Brahman and the Self; the vast; the Brāhmaṇī; Brāhmī; the bliss "
           "of Brahman; who loves the offering."),
        _v(["bhāṣārūpā bṛhatsenā bhāvābhāvavivarjitā |",
            "sukhārādhyā śubhakarī śobhanā sulabhā gatiḥ"], "|| 133 ||",
           "Whose form is language; of vast armies; beyond both being and "
           "non-being; easily worshipped; maker of good; the beautiful; the "
           "easily attained goal."),
        _v(["rājarājeśvarī rājyadāyinī rājyavallabhā |",
            "rājatkṛpā rājapīṭhaniveśitanijāśritā"], "|| 134 ||",
           "Sovereign of the king of kings; giver of kingdoms; beloved of the "
           "realm; whose grace is resplendent; who sets those who take refuge in "
           "her upon a royal throne."),
        _v(["rājyalakṣmīḥ kośanāthā caturaṅgabaleśvarī |",
            "sāmrājyadāyinī satyasandhā sāgaramekhalā"], "|| 135 ||",
           "The fortune of kingdoms; mistress of the treasury; commander of the "
           "fourfold army; giver of empire; true to her word; girdled by the "
           "ocean."),
        _v(["dīkṣitā daityaśamanī sarvalokavaśaṅkarī |",
            "sarvārthadātrī sāvitrī saccidānandarūpiṇī"], "|| 136 ||",
           "The consecrated; queller of demons; who brings all worlds under her "
           "sway; giver of every good; Sāvitrī; whose form is "
           "being-consciousness-bliss."),
        _v(["deśakālāparicchinnā sarvagā sarvamohinī |",
            "sarasvatī śāstramayī guhāmbā guhyarūpiṇī"], "|| 137 ||",
           "Unbounded by place or time; all-pervading; enchantress of all; "
           "Sarasvatī; made of the scriptures; mother of Guha; of secret form."),
        _v(["sarvopādhivinirmuktā sadāśivapativratā |",
            "sampradāyeśvarī sādhvī gurumaṇḍalarūpiṇī"], "|| 138 ||",
           "Free of every limiting adjunct; devoted wholly to Sadāśiva; mistress "
           "of the tradition; the virtuous; whose form is the circle of the "
           "gurus."),
        _v(["kulottīrṇā bhagārādhyā māyā madhumatī mahī |",
            "gaṇāmbā guhyakārādhyā komalāṅgī gurupriyā"], "|| 139 ||",
           "Risen beyond the Kula; worshipped in the bhaga; Māyā; full of "
           "sweetness; the earth; mother of the gaṇas; worshipped by the "
           "guhyakas; of tender limbs; dear to the guru."),
        _v(["svatantrā sarvatantreśī dakṣiṇāmūrtirūpiṇī |",
            "sanakādisamārādhyā śivajñānapradāyinī"], "|| 140 ||",
           "Independent; mistress of all tantras; whose form is Dakṣiṇāmūrti; "
           "worshipped by Sanaka and the rest; giver of the knowledge of Śiva."),
        _v(["citkalā''nandakalikā premarūpā priyaṅkarī |",
            "nāmapārāyaṇaprītā nandividyā naṭeśvarī"], "|| 141 ||",
           "The digit of consciousness; the bud of bliss; whose form is love; "
           "doer of what is dear; pleased by the recitation of her names; the "
           "Nandi-vidyā; mistress of the Dancer."),
        _v(["mithyājagadadhiṣṭhānā muktidā muktirūpiṇī |",
            "lāsyapriyā layakarī lajjā rambhādivanditā"], "|| 142 ||",
           "The ground on which the unreal world rests; giver of liberation; "
           "whose form is liberation; who loves the graceful dance; who brings "
           "all to dissolution; modesty itself; adored by Rambhā and the rest."),
        _v(["bhavadāvasudhāvṛṣṭiḥ pāpāraṇyadavānalā |",
            "daurbhāgyatūlavātūlā jarādhvāntaraviprabhā"], "|| 143 ||",
           "A rain of nectar on the wildfire of becoming; a forest-fire to the "
           "jungle of sin; a whirlwind to the cotton-down of misfortune; sunlight "
           "to the darkness of old age."),
        _v(["bhāgyābdhicandrikā bhaktacittakekighanāghanā |",
            "rogaparvatadambholirmṛtyudārukuṭhārikā"], "|| 144 ||",
           "Moonlight upon the ocean of fortune; the thundercloud to the peacock "
           "of the devotee's heart; the thunderbolt to the mountain of disease; "
           "the axe to the tree of death."),
        _v(["maheśvarī mahākālī mahāgrāsā mahāśanā |",
            "aparṇā caṇḍikā caṇḍamuṇḍāsuraniṣūdinī"], "|| 145 ||",
           "Maheśvarī; Mahākālī; the great devourer; the great eater; Aparṇā; "
           "Caṇḍikā; slayer of the demons Caṇḍa and Muṇḍa."),
        _v(["kṣarākṣarātmikā sarvalokeśī viśvadhāriṇī |",
            "trivargadātrī subhagā tryambakā triguṇātmikā"], "|| 146 ||",
           "Whose Self is both the perishable and the imperishable; mistress of "
           "all worlds; upholder of the universe; giver of the three ends of "
           "life; the blessed; the three-eyed; whose Self is the three "
           "qualities."),
        _v(["svargāpavargadā śuddhā japāpuṣpanibhākṛtiḥ |",
            "ojovatī dyutidharā yajñarūpā priyavratā"], "|| 147 ||",
           "Giver of heaven and of release; the pure; her form like the hibiscus "
           "flower; full of vigour; bearer of radiance; whose form is sacrifice; "
           "steadfast in her loving vow."),
        _v(["durārādhyā durādharṣā pāṭalīkusumapriyā |",
            "mahatī merunilayā mandārakusumapriyā"], "|| 148 ||",
           "Hard to worship; hard to assail; who loves the pāṭalī flower; the "
           "great; dwelling on Meru; who loves the mandāra flower."),
        _v(["vīrārādhyā virāḍrūpā virajā viśvatomukhī |",
            "pratyagrūpā parākāśā prāṇadā prāṇarūpiṇī"], "|| 149 ||",
           "Worshipped by heroes; whose form is the cosmic Virāj; the stainless; "
           "facing every direction; the inward Self; the supreme ether; giver of "
           "life; whose form is the life-breath."),
        _v(["mārtāṇḍabhairavārādhyā mantriṇīnyastarājyadhūḥ |",
            "tripureśī jayatsenā nistraiguṇyā parāparā"], "|| 150 ||",
           "Worshipped by Mārtāṇḍa-Bhairava; who laid the burden of the kingdom "
           "upon Mantriṇī; sovereign of Tripura; of victorious armies; beyond "
           "the three qualities; both supreme and immanent."),
        _v(["satyajñānānandarūpā sāmarasyaparāyaṇā |",
            "kapardinī kalāmālā kāmadhuk kāmarūpiṇī"], "|| 151 ||",
           "Whose form is truth, knowledge and bliss; devoted to perfect "
           "equipoise; wearer of the matted lock; garlanded with the digits of "
           "the moon; the wish-granting cow; taking the form she wills."),
        _v(["kalānidhiḥ kāvyakalā rasajñā rasaśevadhiḥ |",
            "puṣṭā purātanā pūjyā puṣkarā puṣkarekṣaṇā"], "|| 152 ||",
           "The treasury of arts; the art of poetry; the knower of savour; a "
           "storehouse of savour; the well-nourished; the ancient; the "
           "worshipful; the lotus; lotus-eyed."),
        _v(["paraṃjyotiḥ paraṃdhāma paramāṇuḥ parātparā |",
            "pāśahastā pāśahantrī paramantravibhedinī"], "|| 153 ||",
           "The supreme Light; the supreme Abode; the finest atom; higher than "
           "the highest; holding the noose in her hand; destroyer of the noose; "
           "breaker of hostile spells."),
        _v(["mūrtā'mūrtā'nityatṛptā munimānasahaṃsikā |",
            "satyavratā satyarūpā sarvāntaryāminī satī"], "|| 154 ||",
           "With form; and formless; ever content though never sated; the swan "
           "in the lake of the sage's mind; whose vow is truth; whose form is "
           "truth; the inner ruler of all; Satī."),
        _v(["brahmāṇī brahmajananī bahurūpā budhārcitā |",
            "prasavitrī pracaṇḍā''jñā pratiṣṭhā prakaṭākṛtiḥ"], "|| 155 ||",
           "Brahmāṇī; mother of Brahmā; of many forms; worshipped by the wise; "
           "the bringer-forth; the fierce; the command; the foundation; of "
           "manifest form."),
        _v(["prāṇeśvarī prāṇadātrī pañcāśatpīṭharūpiṇī |",
            "viśṛṅkhalā viviktasthā vīramātā viyatprasūḥ"], "|| 156 ||",
           "Mistress of the life-breath; giver of life; whose form is the fifty "
           "seats; the unfettered; abiding in solitude; mother of heroes; mother "
           "of space."),
        _v(["mukundā muktinilayā mūlavigraharūpiṇī |",
            "bhāvajñā bhavarogaghnī bhavacakrapravartinī"], "|| 157 ||",
           "The giver of release; the abode of liberation; whose form is the "
           "root image; knower of every heart; destroyer of the disease of "
           "becoming; who turns the wheel of becoming."),
        _v(["chandaḥsārā śāstrasārā mantrasārā talodarī |",
            "udārakīrtiruddāmavaibhavā varṇarūpiṇī"], "|| 158 ||",
           "The essence of metre; the essence of scripture; the essence of "
           "mantra; of slender waist; of noble renown; of unbounded majesty; "
           "whose form is the letters."),
        _v(["janmamṛtyujarātaptajanaviśrāntidāyinī |",
            "sarvopaniṣadudghuṣṭā śāntyatītakalātmikā"], "|| 159 ||",
           "Giver of rest to those scorched by birth, death and old age; "
           "proclaimed aloud by all the Upaniṣads; whose Self is the digit "
           "beyond even peace."),
        _v(["gambhīrā gaganāntasthā garvitā gānalolupā |",
            "kalpanārahitā kāṣṭhā'kāntā kāntārdhavigrahā"], "|| 160 ||",
           "The profound; abiding at the end of the sky; the proud; eager for "
           "song; free of all imagining; the ultimate limit; the beloved; who is "
           "half the body of her beloved."),
        _v(["kāryakāraṇanirmuktā kāmakelitaraṅgitā |",
            "kanatkanakatāṭaṅkā līlāvigrahadhāriṇī"], "|| 161 ||",
           "Free of both effect and cause; rippling with the play of love; "
           "wearing earrings of gleaming gold; who takes on forms in play."),
        _v(["ajā kṣayavinirmuktā mugdhā kṣipraprasādinī |",
            "antarmukhasamārādhyā bahirmukhasudurlabhā"], "|| 162 ||",
           "The unborn; free of decay; the artless; swift to grant grace; "
           "worshipped by those turned inward; hard indeed for those turned "
           "outward to reach."),
        _v(["trayī trivarganilayā tristhā tripuramālinī |",
            "nirāmayā nirālambā svātmārāmā sudhāsṛtiḥ"], "|| 163 ||",
           "The threefold Veda; the abode of the three ends of life; abiding in "
           "the three; garlanded with the three cities; free of disease; without "
           "support; delighting in her own Self; a stream of nectar."),
        _v(["saṃsārapaṅkanirmagnasamuddharaṇapaṇḍitā |",
            "yajñapriyā yajñakartrī yajamānasvarūpiṇī"], "|| 164 ||",
           "Skilled in lifting up those sunk in the mire of becoming; who loves "
           "sacrifice; the maker of sacrifice; whose form is the sacrificer "
           "himself."),
        _v(["dharmādhārā dhanādhyakṣā dhanadhānyavivardhinī |",
            "viprapriyā viprarūpā viśvabhramaṇakāriṇī"], "|| 165 ||",
           "The support of dharma; overseer of wealth; increaser of wealth and "
           "grain; dear to the wise; whose form is the wise; who sets the "
           "universe revolving."),
        _v(["viśvagrāsā vidrumābhā vaiṣṇavī viṣṇurūpiṇī |",
            "ayoniryoninilayā kūṭasthā kularūpiṇī"], "|| 166 ||",
           "Devourer of the universe; radiant as coral; Vaiṣṇavī; whose form is "
           "Viṣṇu; born of no womb; yet dwelling in the womb; the unmoving "
           "summit; whose form is the Kula."),
        _v(["vīragoṣṭhīpriyā vīrā naiṣkarmyā nādarūpiṇī |",
            "vijñānakalanā kalyā vidagdhā baindavāsanā"], "|| 167 ||",
           "Who loves the assembly of heroes; the heroic; beyond all action; "
           "whose form is primal sound; the unfolding of knowledge; the capable; "
           "the discerning; seated on the bindu."),
        _v(["tattvādhikā tattvamayī tattvamarthasvarūpiṇī |",
            "sāmagānapriyā saumyā sadāśivakuṭumbinī"], "|| 168 ||",
           "Higher than the categories; made of Reality; whose form is the "
           "meaning of 'That thou art'; who loves the singing of the Sāman; the "
           "gentle; the housewife of Sadāśiva."),
        _v(["savyāpasavyamārgasthā sarvāpadvinivāriṇī |",
            "svasthā svabhāvamadhurā dhīrā dhīrasamarcitā"], "|| 169 ||",
           "Abiding in both the right-hand and the left-hand paths; averter of "
           "every calamity; established in herself; sweet by her very nature; "
           "the steadfast; worshipped by the steadfast."),
        _v(["caitanyārghyasamārādhyā caitanyakusumapriyā |",
            "sadoditā sadātuṣṭā taruṇādityapāṭalā"], "|| 170 ||",
           "Worshipped with the offering of consciousness; who loves the flower "
           "of consciousness; ever risen; ever content; rosy as the young sun."),
        _v(["dakṣiṇādakṣiṇārādhyā darasmeramukhāmbujā |",
            "kaulinīkevalā'narghyakaivalyapadadāyinī"], "|| 171 ||",
           "Worshipped by both the southern and the other rites; her lotus face "
           "faintly smiling; the Kaulinī, the absolute; giver of the priceless "
           "state of aloneness."),
        _v(["stotrapriyā stutimatī śrutisaṃstutavaibhavā |",
            "manasvinī mānavatī maheśī maṅgalākṛtiḥ"], "|| 172 ||",
           "Who loves hymns; worthy of praise; whose majesty the Vedas hymn; of "
           "noble mind; worthy of honour; the great sovereign; whose very form "
           "is auspiciousness."),
        _v(["viśvamātā jagaddhātrī viśālākṣī virāgiṇī |",
            "pragalbhā paramodārā parāmodā manomayī"], "|| 173 ||",
           "Mother of the universe; nurse of the world; wide-eyed; free of "
           "passion; the confident; supremely generous; of supreme delight; made "
           "of mind."),
        _v(["vyomakeśī vimānasthā vajriṇī vāmakeśvarī |",
            "pañcayajñapriyā pañcapretamañcādhiśāyinī"], "|| 174 ||",
           "Whose hair is the sky; seated in the celestial car; bearer of the "
           "thunderbolt; the Vāmakeśvarī; who loves the five sacrifices; "
           "reclining on the couch of the five corpse-gods."),
        _v(["pañcamī pañcabhūteśī pañcasaṃkhyopacāriṇī |",
            "śāśvatī śāśvataiśvaryā śarmadā śambhumohinī"], "|| 175 ||",
           "The fifth; mistress of the five elements; served with the fivefold "
           "offering; the everlasting; of everlasting sovereignty; giver of "
           "happiness; enchantress of Śambhu."),
        _v(["dharā dharasutā dhanyā dharmiṇī dharmavardhinī |",
            "lokātītā guṇātītā sarvātītā śamātmikā"], "|| 176 ||",
           "The earth; daughter of the mountain; the blessed; the righteous; "
           "increaser of dharma; beyond the worlds; beyond the qualities; beyond "
           "all; whose Self is peace."),
        _v(["bandhūkakusumaprakhyā bālā līlāvinodinī |",
            "sumaṅgalī sukhakarī suveṣāḍhyā suvāsinī"], "|| 177 ||",
           "Radiant as the bandhūka flower; the young girl; who delights in "
           "play; the auspicious wife; maker of happiness; richly attired; the "
           "fragrant one."),
        _v(["suvāsinyarcanaprītā''śobhanā śuddhamānasā |",
            "bindutarpaṇasantuṣṭā pūrvajā tripurāmbikā"], "|| 178 ||",
           "Pleased by the worship offered by married women; the radiant; of "
           "pure mind; contented by the offering at the bindu; the first-born; "
           "Mother of the three cities."),
        _v(["daśamudrāsamārādhyā tripurāśrīvaśaṅkarī |",
            "jñānamudrā jñānagamyā jñānajñeyasvarūpiṇī"], "|| 179 ||",
           "Worshipped by the ten mudrās; who brings the splendour of Tripurā "
           "under her sway; the seal of knowledge; reached by knowledge; whose "
           "form is both knowledge and the known."),
        _v(["yonimudrā trikhaṇḍeśī triguṇāmbā trikoṇagā |",
            "anaghā'dbhutacāritrā vāñchitārthapradāyinī"], "|| 180 ||",
           "The yoni-mudrā; mistress of the three sections; mother of the three "
           "qualities; dwelling in the triangle; the sinless; of wondrous deeds; "
           "giver of every desired end."),
        _v(["abhyāsātiśayajñātā ṣaḍadhvātītarūpiṇī |",
            "avyājakaruṇāmūrtirajñānadhvāntadīpikā"], "|| 181 ||",
           "Known through surpassing practice; whose form transcends the six "
           "paths; compassion embodied without any motive; the lamp in the "
           "darkness of ignorance."),
        _v(["ābālagopaviditā sarvānullaṅghyaśāsanā |",
            "śrīcakrarājanilayā śrīmattripurasundarī"], "|| 182 ||",
           "Known even to children and cowherds; whose command none may "
           "transgress; whose abode is the royal Śrīcakra; the glorious "
           "Tripurasundarī."),
        "ornament",
        _v(["śrīśivā śivaśaktyaikyarūpiṇī lalitāmbikā |",
            "evaṃ śrīlalitādevyā nāmnāṃ sāhasrakaṃ jaguḥ"], "",
           "Śrī Śivā; whose form is the oneness of Śiva and Śakti; Mother "
           "Lalitā. — Thus have they sung the thousand names of the Goddess Śrī "
           "Lalitā."),
    ],
}
