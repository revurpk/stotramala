# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain, raw wikitext) via teltools
# dev2iast. Translations original. Mahiṣāsura Mardinī Stotram ("Ayi Giri
# Nandini"), traditionally attributed to Rāmakṛṣṇa Kavi — 21 verses to the
# Goddess who slew the buffalo-demon Mahiṣa. Compound-hyphens are kept as
# reading aids (dropped for the native scripts at render time).

REFRAIN = "jaya jaya he mahiṣāsuramardini ramya kapardini śailasute"

def _v(l1, l2, l3, n, gloss):
    return {"padas": [l1, l2 + " |", l3, REFRAIN], "num": f"|| {n} ||", "gloss": gloss}


STOTRA = {
    "deity": "devi",
    "doc_title": "Mahiṣāsura Mardinī Stotram",
    "app_title": "Mahiṣāsura Mardinī",
    "h1": "Mahiṣāsura Mardinī Stotram",
    "subtitle": "Hymn to the Slayer of Mahiṣa",
    "note": "This hymn revels in dense alliteration, rare epithets, and "
            "drum-and-dance onomatopoeia; the translations give the sense where "
            "it is clear and paraphrase the sound-play. Every verse closes with "
            "the refrain — “Victory, victory to you, slayer of the demon Mahiṣa, "
            "lovely-tressed daughter of the mountain!”",
    "footer": "Source: Sanskrit Wikisource — Mahiṣāsuramardinī Stotram (public domain)",
    "sections": [
        _v("ayigirinandini nanditamedini viśvavinodini nandanute",
           "girivaravindhya-śirodhinivāsini viṣṇuvilāsini jiṣṇunute",
           "bhagavati he śitikaṇṭhakuṭumbini bhūrikuṭumbini bhūrikṛte", 1,
           "O delight of the Mountain, gladdener of the earth, joy of all the "
           "world, praised by the blessed; dweller on the crest of great "
           "Vindhya, in whom Viṣṇu takes delight, praised by the victorious; O "
           "Bhagavatī, consort of the blue-throated Śiva, of a vast household, "
           "of manifold deeds."),
        _v("suravaravarṣiṇi durdharadharṣiṇi durmukhamarṣiṇī harṣarate",
           "tribhuvanapoṣiṇi śaṃkaratoṣiṇi kilbiṣamoṣiṇi ghoṣarate",
           "danujaniroṣiṇi ditisutaroṣiṇi durmadaśoṣiṇi sindhusute", 2,
           "O showerer of boons on the good, assailer of the unassailable, "
           "crusher of the foul-mouthed, delighting in joy; nourisher of the "
           "three worlds, pleaser of Śaṅkara, stealer of sin, revelling in the "
           "battle-roar; wrathful at the demons, furious at the sons of Diti, "
           "drier-up of the arrogant, O daughter of the ocean."),
        _v("ayi jagadamba madamba kadambavanapriyavāsini hāsarate",
           "śikhariśiromaṇi tuṅgahimālayaśṛṅganijālayamadhyagate",
           "madhumadhure madhukaiṭabhagañjini kaiṭabhabhañjini rāsarate", 3,
           "O Mother of the world, my Mother, dwelling happily in your beloved "
           "kadamba grove, delighting in laughter; crest-jewel of mountains, "
           "abiding in your own home amid the high Himālaya peaks; sweet as "
           "honey, vanquisher of Madhu and Kaiṭabha, breaker of Kaiṭabha, "
           "delighting in the round-dance."),
        _v("ayi śatakhaṇḍavikhaṇḍitaruṇḍavituṇḍitaśuṇḍagajādhipate",
           "ripugajagaṇḍavidāraṇacaṇḍaparākramaśuṇḍamṛgādhipate",
           "nijabhujadaṇḍanipātitakhaṇḍavipātitamuṇḍabhaṭādhipate", 4,
           "O conqueror of the elephant-king whose trunk was hewn and head "
           "split into a hundred pieces; whose lion, of fierce valour, tore "
           "with its paws the temples of the foe-elephants; who felled the "
           "warrior-hosts, their severed heads struck down and split by the "
           "staff of your own arm."),
        _v("ayi raṇadurmadaśatruvadhodyatadurdharanirjaraśaktibhṛte",
           "caturavicāradhurīṇamahāśivadūtakṛtapramathādhipate",
           "duritadurīhadurāśayadurmatidānavadūtakṛtāntamate", 5,
           "O bearer of the irresistible, undecaying power, poised to slay the "
           "battle-maddened foes; commander of the pramatha-hosts, whose envoy "
           "was great Śiva, foremost in shrewd counsel; O you whose mind is "
           "very Death to the demons — those wicked, ill-intentioned, "
           "foul-hearted messengers."),
        _v("ayi śaraṇāgatavairivadhūvaravīravarābhayadānakare",
           "tribhuvanamastakaśūlavirodhiśirodhikṛtāmalaśūlakare",
           "dumidumitāmaradundubhinādamaho mukharīkṛtatigmakare", 6,
           "O you whose hand grants fearlessness even to the brave lords and "
           "husbands of the surrendered foe's women; whose hand bears the "
           "spotless spear raised against the head-piercing spears (the "
           "afflictions) of the three worlds; whose fierce hand is made "
           "resonant with the ‘dumi-dumi’ beat of the gods' great war-drums."),
        _v("ayi nijahuṅkṛtimātranirākṛtadhūmravilocanadhūmraśate",
           "samaraviśoṣitaśoṇitabījasamudbhavaśoṇitabījalate",
           "śivaśivaśumbhaniśumbhamahāhavatarpitabhūtapiśācarate", 7,
           "O you who by a mere roar undid the smoke-eyed demon and his hundred "
           "smoke-hosts; O destroying creeper of the blood-seeds — the "
           "Raktabīja drops that sprang up, dried in battle; who, crying "
           "‘Śiva, Śiva!’, in the great war with Śumbha and Niśumbha gratified "
           "the hosts of ghosts and goblins."),
        _v("dhanuranusaṃgaraṇakṣaṇasaṃgaparisphuradaṅganaṭatkaṭake",
           "kanakapiśaṅgapṛṣatkaniṣaṅgarasadbhaṭaśṛṅgahatābaṭuke",
           "kṛtacaturaṃgabalakṣitiraṅgaghaṭadbahuraṅgaraṭadbaṭuke", 8,
           "O you on whose arm the bangles flash and dance as it draws the bow "
           "in the instant of battle; whose golden-tawny arrows and quiver lay "
           "low the boastful warriors' pride; who make the earth a stage of the "
           "fourfold army, thronged with clamouring, many-hued troops."),
        _v("suralalanā-tatatheyi-tatheyi-kṛtābhinayodara-nṛtyarate",
           "kṛtakukuthaḥ kukutho gaḍadādika-tāla-kutūhala-gānarate",
           "dhudhukuṭa dhukkuṭa dhiṃdhimitadhvanidhīramṛdaṅganinādarate", 9,
           "O you who delight in the dance the celestial maidens mime with "
           "‘tatatheyi tatheyi’ steps; who delight in the merry song of "
           "‘kukutha kukutha, gaḍadādika’ rhythm; who delight in the deep "
           "mṛdaṅga sounding ‘dhudhukuṭa dhukkuṭa dhiṃdhimita’."),
        _v("jaya-jaya-japya-jayejayaśabda-parastuti-tatparaviśvanute",
           "jhaṇa-jhaṇa-jhiñjhimi jhiṅkṛta nūpurasiṃjitamohita bhūtapate",
           "naṭitanaṭārdha naṭī naṭa nāyaka nāṭitanāṭya sugānarate", 10,
           "O you praised by all the world intent on hymns of ‘jaya jaya, jaya’; "
           "O lord of the ghost-hosts, enchanted by the ‘jhaṇa jhaṇa jhiñjhimi’ "
           "jingling of anklets; delighting in the fine song and the acted "
           "dance of dancing-girl, dancer, and dance-master."),
        _v("ayi sumanaḥ sumanaḥ sumanaḥ sumanaḥ sumanoharakāṃtiyute",
           "śritarajanī-rajanīrajanī-rajanīrajanīkara-vaktravṛte",
           "sunayanavibhramara-bhramarabhramara-bhramarabhramarādhipate", 11,
           "O you endowed with a loveliness more charming than flower upon "
           "flower upon flower; whose face is haloed like moon upon radiant "
           "moon of the night; O queen-bee among the roving bees — the swarming "
           "glances of your lovely eyes."),
        _v("sahitamahāhava-mallamatallika-mallitarallaka-mallarate",
           "viracitavallika-pallikamallika-bhillikabhillika-vargavṛte",
           "sitkṛtpullasamullasitāruṇa-tallaja-pallava-sallalite", 12,
           "O you who delight amid the great combat of champion wrestlers; "
           "encircled by the throngs of Bhilla hill-folk in their bowers and "
           "huts; graced with the tender red shoots that gleam and open with a "
           "soft ‘sit’ of delight."),
        _v("aviralagaṇḍa-galanmadamedura-mattamattaṃgaja-rājapate",
           "tribhivanabhūṣaṇabhūta-kalānidhi-rūpapayonidhi-rājasute",
           "ayi sudatījana-lālasamānasa-mohanamanmatharājasute", 13,
           "O queen over the lordly rutting elephant, thick with the ceaseless "
           "flow of temple-ichor; O daughter arisen from the nectar-ocean, "
           "moon-formed ornament of the three worlds; O royal daughter of "
           "Manmatha, enchantress of the longing hearts of fair-toothed women."),
        _v("kamaladalāmala-komalakānti-kalā-kalitāmala-bhālalate",
           "sakalavilāsa-kalānilayakrama-kelicalatkala-haṃsakule",
           "alikulasaṅkula-kuvalayamaṇḍala-maulimiladbakulālikule", 14,
           "O you whose spotless brow-creeper holds the tender radiant grace of "
           "a pure lotus-petal; through whose every sporting movement glides a "
           "flock of graceful swans; over whom a swarm of bees clusters on the "
           "blue-lotus circle, meeting the bakula blossoms at your crown."),
        _v("karamuralīrava-vījitakūjita-lajjitakokila-mañjumate",
           "militapulinda-manoharaguṃjita-raṃjitaśaila-nikuñjagate",
           "nijaguṇabhūta-mahāśabarīgaṇa-sadguṇasambhṛta-kelitale", 15,
           "O sweet-minded one, before whose flute's warble the cuckoo is "
           "shamed; O dweller in the mountain bowers, lovely with the humming "
           "of the gathered Pulinda folk; whose playground is heaped with the "
           "good virtues of the great Śabara hosts, your own devotees."),
        _v("kaṭitaṭapīta-dukūlavicitra-mayūkhatiraskṛta-candraruce",
           "praṇatasurāsura-maulimaṇisphuradaṃśula-sannakha-candraruce",
           "jitakanakācala-maulipadorjita-nirbharakuṃjara-kumbhakuce", 16,
           "O you whose radiance, from the wondrous yellow silk at your hips, "
           "outshines the moon; whose fair nails gleam moon-bright with the rays "
           "of the crest-gems of gods and demons bowed at your feet; whose "
           "full, firm breasts surpass the golden peak and the elephant's "
           "temples."),
        _v("vijitasahasra-karaika-sahasra-karaika-sahasra-karaikanute",
           "kṛtasuratāraka-saṅgaratāraka-saṅgaratāraka-sunūsute",
           "surathasamādhi-samānasamādhi-samādhi-samādhi-sujātarate", 17,
           "O you hymned by thousand upon thousand hands of the thousand-handed; "
           "helper in the god-and-Tāraka war, mother of the one born for it "
           "(Skanda); O you well pleased, arisen from the deep, matchless "
           "meditation of King Suratha and the merchant Samādhi."),
        _v("padakamalaṃ karuṇānilaye varivasyati yonudinam sa śive",
           "ayi kamale kamalānilaye kamalānilayaḥ sa kathaṃ na bhavet",
           "tava padameva parampadamityanuśīlayato mama kiṃ na śive", 18,
           "Whoever daily worships your lotus feet, O gracious one, O auspicious "
           "one — O Kamalā, dweller in the lotus, how should he not himself "
           "become an abode of Lakṣmī? For me, who hold that ‘your foot alone "
           "is the supreme state’ — what, O auspicious one, is not attained?"),
        _v("kanakalasatkalasindhu-jalairanu-siñcinute guṇaraṅgabhuvam",
           "bhajati sa kiṃ na śacīkucakumbhataṭīparirambha-sukhānubhavam",
           "tavacaraṇaṃ śaraṇaṅkaravāṇi natāmaravāṇinivāsiśivam", 19,
           "For one who sprinkles the arena of your virtues with waters from a "
           "gleaming golden pitcher-sea — does he not taste the bliss of "
           "embracing the jar-like breasts of Śacī? O you in whom the bowed "
           "gods' Speech and Śiva dwell — let me make your foot my refuge."),
        _v("tava vimalendukulaṃ vadanendumalaṃ sakalaṃ nanukūlayate",
           "kimu puruhūtapurīndu-mukhī-sumukhībhirasau vimukhīkriyate",
           "mama tu mataṃ śivanāmadhane bhavatī kṛpayā kimuta kriyate", 20,
           "Your face-moon, of spotless-moon lineage, makes all things wholly "
           "favourable; is it thereby outshone by the moon-faces of the fair "
           "women of Indra's city? But this is my conviction, O treasure of "
           "Śiva's name: what is not accomplished by your grace?"),
        _v("ayi mayi dīna dayālutayā kṛpayaiva tvayā bhavitavyamume",
           "ayi jagato jananī kṛpayāsi yathāsi tathānumitāsirate",
           "yaducitamatra bhavatyurarī-kurutādurutāpamapākurute", 21,
           "O Umā, toward me, wretched, you must surely, of your very nature, be "
           "compassionate; O Mother of the world, as you are merciful, so are "
           "you rightly known to be; whatever is fitting here, take it up, and "
           "drive away my grievous affliction."),
    ],
}
