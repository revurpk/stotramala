# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE work (src="tel"): Telugu is the source, IAST a reading aid,
# no Devanāgarī. Rukmiṇī Kalyāṇam — Bammera Pōtana's Telugu Bhāgavatam,
# 10th skandha, first part, verses 10.1-1680 to 1792, as printed in the
# Tirumala Tirupati Devasthanams edition (Sri Mahabhagavatamu with
# Commentary, vol. VI, ed. Dr. Samudrala Lakshmanaiah, 2017). Pōtana's
# verses only; the edition's word meanings, paraphrase and notes are not
# used. Converted from the PDF's Priyaanka text layer (priyaanka.py).
# Metre labels (క. మ. సీ. …) are named in the glosses. Translation
# original. See SOURCES §6.11.

def _v(lines, num, gloss, prose=False):
    v = {"padas": lines, "num": num, "gloss": gloss}
    if prose:
        v["prose"] = True
    return v


STOTRA = {
    "src": "tel",
    "deity": "vishnu",
    "doc_title": "Rukmiṇī Kalyāṇam",
    "app_title": "Rukmiṇī Kalyāṇam",
    "h1": "Rukmiṇī Kalyāṇam",
    "subtitle": "Pōtana · the wedding of Rukmiṇī and Kṛṣṇa",
    "note": "Bammera Pōtana's Telugu Bhāgavatam, 10th skandha (first part), "
            "verses 10.1-1680 to 1792, as printed by Tirumala Tirupati "
            "Devasthanams. Rukmiṇī's love for Kṛṣṇa, her letter carried by a "
            "brāhmaṇa, her abduction from the temple of Gaurī, Rukmī's defeat "
            "and the wedding at Dvārakā. The Telugu is the source; the IAST is "
            "a reading aid; prose passages (vacanam) keep the book's line "
            "breaks.",
    "toc": True,
    "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, "
              "Vol. VI (Skandha 10-1), ed. Dr. Samudrala Lakshmanaiah, T.T.D. "
              "Religious Publications Series No. 1242, Tirumala Tirupati "
              "Devasthanams, Tirupati, first edition 2017 — Pōtana's verses only "
              "(public domain); the edition's commentary is not reproduced; "
              "translations original",
    "sections": [
    {"heading": "The tale of Rukmiṇī's wedding begins"},
    _v([
        "ఆ వనజగర్భుపంపున, రైవతుఁ డను రాజు దెచ్చి రామున కిచ్చెన్",
        "రేవతి యనియెడు కన్యను, భూవర! మును వింటి కాదె బుద్ధిం దెలియన్."], "॥ 1680 ॥", "[Kandam] At the bidding of the lotus-born Brahmā a king named Raivata brought a maiden called Revatī and gave her to Balarāma — you heard this before, O king, and know it well, do you not?"),
    _v([
        "తదనంతరంబ."], "॥ 1681 ॥", "[Vacanam] After that —", prose=True),
    _v([
        "ఖగనాథుం డమరేంద్రు గెల్చి సుధ మున్ గైకొన్న చందంబునన్",
        "జగతీనాథులఁ జైద్యపక్షచరులన్ సాళ్వాదులం గెల్పి భ",
        "ద్రగుఁడై చక్రి వరించె భీష్మకసుతన్ రాజీవగంధిన్ రమా",
        "భగవత్యంశభవన్ మహాగుణమణిన్ బాలామణిన్ రుక్మిణిన్."], "॥ 1682 ॥", "[Mattebham] As Garuḍa, lord of birds, once overcame Indra, king of the gods, and carried off the nectar, so the discus-bearer, blessed with good fortune, overcame the kings — the partisans of the Cedi king, Śālva and the rest — and wed Bhīṣmaka's daughter Rukmiṇī: fragrant as a lotus, born of a portion of the goddess Ramā, a jewel of great virtues, the jewel among maidens."),
    _v([
        "అనిన రాజిట్లనియె. మున్ను రాక్షసవివాహంబున స్వయంవరంబునకు వచ్చి హరి రుక్మిణిం గొనిపోయె",
        "నని పలికితివి. కృష్ణుం డొక్కరుం డెవ్విధంబున సాళ్వాదుల జయించి తన పురంబునకుం జనియె; నదియునుం",
        "గాక."], "॥ 1683 ॥", "[Vacanam] At this the king (Parīkṣit) said: \"You told me before that Hari came to the svayaṃvara and carried Rukmiṇī off by the rākṣasa form of marriage. How did Kṛṣṇa, alone, defeat Śālva and the others and return to his city? And more —\"", prose=True),
    _v([
        "కల్యాణాత్మకమైన విష్ణుకథ లాకర్ణించుచున్ ముక్త వై",
        "కల్యుం డెవ్వఁడు తృప్తుఁ డౌ; నవి వినంగాఁ గ్రొత్త లౌచుండు సా",
        "కల్యం బేర్పడ భూసురోత్తమ! యెరుంగం బల్కవే! రుక్మిణీ",
        "కల్యాణంబు వినంగ నాకు మదిలోఁ గౌతూహలం బయ్యెడిన్."], "॥ 1684 ॥", "[Śārdūlam] \"Who, hearing the tales of Viṣṇu, auspicious in themselves, and freed by them from every fault, is ever sated? Each hearing makes them new. O best of brāhmaṇas, tell it in full, that I may know it: my heart is eager to hear of Rukmiṇī's wedding.\""),
    _v([
        "భూషణములు సెవులకు బుధ, తోషణము లనేకజన్మదురితౌఘవిని",
        "శ్శోషణములు మంగళతర, ఘోషణములు గరుడగమనుగుణభాషణముల్."], "॥ 1685 ॥", "[Kandam] \"Words in praise of the virtues of him who rides Garuḍa are ornaments to the ears, a delight to the wise; they dry up the flood of sins of many births; they are proclamations most auspicious.\""),
    _v([
        "అని రా జడిగిన శుకుం డిట్లనియె."], "॥ 1686 ॥", "[Vacanam] When the king asked thus, Śuka said:", prose=True),
    _v([
        "వినుము విదర్భదేశమున వీరుఁడు కుండినభర్త భీష్మకుం",
        "డను నొక దొడ్డరాజు గల; డాతని కేవురు పుత్త్రు లగ్రజుం",
        "డనయుఁడు రుక్మి నాఁ బరఁగు; నందరకున్ గడగొట్టుచెల్లెలై",
        "మనుజవరేణ్య! పుట్టె నొక మానిని రుక్మిణి నాఁ బ్రసిద్ధయై."], "॥ 1687 ॥", "[Campakam] Listen. In the land of Vidarbha there is a hero, lord of Kuṇḍina, a great king named Bhīṣmaka. He has five sons; the eldest, a wicked one, goes by the name Rukmī. Last of all, the youngest sister of them all, O best of men, was born a lady renowned as Rukmiṇī."),
    _v([
        "బాలేందురేఖ దోఁచిన, లాలిత యగు నపరదిక్కులాగున ధరణీ",
        "పాలునిగేహము మెరసెను, బాలిక జన్మించి యెదుగ భాసుర మగుచున్."], "॥ 1688 ॥", "[Kandam] As the western sky grows lovely when the crescent of the young moon shows in it, so the king's house shone bright as the girl was born and grew."),
    _v([
        "మరియు దినదినప్రవర్ధమానయై."], "॥ 1689 ॥", "[Vacanam] And growing day by day,", prose=True),
    _v([
        "పేర్వేర బొమ్మలపెండ్లిండ్లు సేయుచు నబలలతోడ వియ్యంబు లందు",
        "గుజ్జెనగూళ్ళను గొమరొప్ప వండించి చెలులకుఁ బెట్టించుఁ జెలువు మెరసి",
        "రమణీయమందిరారామదేశంబులఁ బువ్వుఁదీఁగెలకును బ్రోదివెట్టు",
        "సదమలమణిమయసౌధభాగంబుల లీలతో భర్మడోలికల నూఁగు",
        "బాలికలతోడఁ జెలరేగి బంతులాడు, శారికాకీరపంక్తికిఁ జదువు సెప్పు",
        "బర్హిసంఘంబులకు మురిపములు గరపు, మదమరాళంబులకుఁ జూపు మందగతులు."], "॥ 1690 ॥", "[Sīsam with tēṭagīti] she would hold weddings of dolls one after another and make marriage alliances with her girl-friends; she had pretend meals cooked handsomely and served to her companions, shining in her charm; in the lovely gardens of the palace she tended the flowering creepers; in the parts of the mansion set with spotless gems she swung playfully on golden swings; she romped with the girls at ball, taught lessons to rows of mynas and parrots, taught the peacocks their coquetry, and showed the proud swans a slow gait."),
    _v([
        "అంత."], "॥ 1691 ॥", "[Vacanam] Then —", prose=True),
    _v([
        "దేవకీసుతుకోర్కి తీఁగెలు వీడంగ వెలఁదికి మైదీఁగె వీడఁ దొడఁగెఁ;",
        "గమలనాభునిచిత్తకమలంబు వికసింపఁ గాంతి నింతికి ముఖకమల మొప్పె;",
        "మధువిరోధికి లోన మదనాగ్ని పొడసూపఁ బొలఁతికి చనుదోయి పొడవు సూపె;",
        "శౌరికి ధైర్యంబు సన్నమై డయ్యంగ జలజాక్షిమధ్యంబు సన్నమయ్యె;",
        "హరికిఁ బ్రేమబంధ మధికంబుగాఁ కేశ, బంధ మధిక మగుచు బాల కమరెఁ",
        "బద్మనయనువలనఁ బ్రమదంబు నిండార, నెలఁత యౌవనంబు నిండి యుండె."], "॥ 1692 ॥", "[Sīsam with āṭaveladi] As the tendrils of desire in Devakī's son began to unfold, the slender creeper of the maiden's body began to unfold; as the lotus of the lotus-naveled one's heart blossomed, the lotus of the girl's face shone bright; as the fire of love showed itself within Madhu's foe, the woman's breasts showed their height; as Śauri's composure grew thin and gave way, the waist of the lotus-eyed one grew thin; as Hari's bond of love grew greater, the girl's braid grew greater and graced her; and as delight filled the lotus-eyed lord, youth filled the maiden."),
    _v([
        "ఇట్లు రుక్మి, రుక్మరథ, రుక్మబాహు, రుక్మకేశ, రుక్మనేత్రులను నేవురకుం జెలియలైన రుక్మిణీదేవి తన",
        "యెలప్రాయంబున."], "॥ 1693 ॥", "[Vacanam] So Rukmiṇī Devī, sister to the five — Rukmī, Rukmaratha, Rukmabāhu, Rukmakeśa and Rukmanetra — in her young years", prose=True),
    _v([
        "తనతండ్రిగేహమునకుం, జనుదెంచుచు నున్న యతిథిజనులవలనఁ గృ",
        "ష్ణునిరూపబలగుణాదులు, విని కృష్ణుఁడు దనకుఁ దగినఁ విభుఁ డని తలఁచెన్."], "॥ 1694 ॥", "[Kandam] heard from the guests who came to her father's house of Kṛṣṇa's beauty, strength, virtues and the rest, and thought: Kṛṣṇa is the lord fit for me."),
    _v([
        "ఆ లలనరూపు బుద్ధియు, శీలము లక్షణము గుణముఁ జింతించి తగన్",
        "బాలారత్నముఁ దన కి, ల్లాలుగఁ జేకొందు ననుచు హరియుం దలఁచెన్."], "॥ 1695 ॥", "[Kandam] Considering that lady's beauty, mind, character, marks and virtues, Hari too resolved, as was fitting: I shall take this jewel of a girl as my wife."),
    _v([
        "అంత."], "॥ 1696 ॥", "[Vacanam] Then —", prose=True),
    _v([
        "బంధువు లెల్లఁ గృష్ణునకు బాలిక నిచ్చెద మంచు శేముషీ",
        "సింధువులై విచారములు సేయఁగ వారల నడ్డుపెట్టి దు",
        "స్సంధుఁడు రుక్మి కృష్ణునెడఁ జాలవిరోధముఁ జేసి మత్త పు",
        "ష్పంధయవేణి నిత్తు శిశుపాలున కంచుఁ దలంచె నంధుఁడై."], "॥ 1697 ॥", "[Utpalam] While her kinsmen, oceans of wisdom, deliberated, saying \"We shall give the girl to Kṛṣṇa,\" the ill-minded Rukmī stopped them; bearing great enmity towards Kṛṣṇa, blind (with folly), he resolved: \"I shall give her, whose braid is dark as a maddened bee, to Śiśupāla.\""),
    _v([
        "అన్నతలంపు దా నెరిఁగి య న్నవనీరజగంధి లోన నా",
        "పన్నత నొంది, యాప్తుఁడగు బ్రాహ్మణు నొక్కనిఁ జీరి గర్వ సం",
        "ఛన్నుఁడు రుక్మి నేఁడు ననుఁ జైద్యున కిచ్చెద నంచు నున్న వాఁ",
        "డెన్ని విధంబులం జని బుధేశ్వర! చక్రికి విన్నవింపవే!"], "॥ 1698 ॥", "[Utpalam] Learning her brother's intent, that lady fragrant as a fresh lotus was stricken within. She called a trusted brāhmaṇa and said: \"Rukmī, wrapped in pride, is set on giving me to the Cedi king today. O lord of the learned, go by whatever means you can and make this known to the discus-bearer!\""),
    _v([
        "అయ్యా! కొడుకు విచారము, లయ్యయు వారింపఁ జాలఁ డటు గాకుండన్",
        "నెయ్య మెరిఁగించి చీరుము, చయ్యన నిజసేవకానుసారిన్ శౌరిన్."], "॥ 1699 ॥", "[Kandam] \"Sir! (My father) cannot hold back his son's schemes. Before it comes to that, make my love known and swiftly summon Śauri, who follows the wishes of his servants.\""),
    _v([
        "అని కొన్ని రహస్యవచనంబులు సెప్పిన విని బ్రాహ్మణుండు ద్వారకానగరంబునకుం జని, ప్రతీహారుల",
        "వలనఁ దనరాక యెరింగించి య న్నగధరుం డున్ననగరుఁ బ్రవేశించి,యందుఁ గనకాసనాసీనుండై",
        "యున్నపురుషోత్తముం గాంచి 'పెండ్లికొడుకవు గ’ మ్మని దీవించిన ముసిముసినగవులు నగుచు",
        "బ్రహ్మణ్యదేవుండైనహరి తనగద్దియ దిగ్గన డిగ్గి, బ్రాహ్మణుం గూర్చుండ నియోగించి, తనకు దేవతలు",
        "సేయుచందంబునం బూజలు సేసి, సరసపదార్థసంపన్నంబైన యన్నంబు పెట్టించి, రెట్టించిన ప్రియంబున",
        "నయంబున భాసురుండైన భూసురుం జేరి లోకరక్షణప్రశస్తంబయిన హస్తంబున నతనియడుగులు పుడుకుచు",
        "మెల్లన నతని కిట్లనియె."], "॥ 1700 ॥", "[Vacanam] When she had told him certain secret words, the brāhmaṇa went to the city of Dvārakā. Announcing his arrival through the doorkeepers, he entered the palace where the bearer of the mountain lived, and there saw the supreme Person seated on a golden throne. He blessed him, \"May you become a bridegroom!\" Smiling softly, Hari, the god devoted to brāhmaṇas, came down quickly from his seat, had the brāhmaṇa sit, worshipped him as the gods worship Hari himself, had food rich in fine dishes served to him, and with doubled kindness and courtesy came close to the radiant brāhmaṇa and, stroking his feet with the hand famed for protecting the worlds, gently said to him:", prose=True),
    _v([
        "జగతీసురేశ్వర! సంతోషచిత్తుండ వై యున్న నీధర్మ మతిసులభము",
        "వృద్ధసమ్మత మిది విత్త మెయ్యది యైనఁ బ్రాపింప హర్షించు బ్రాహ్మణుండు",
        "తనధర్మమున నుండుఁ దరలఁ డా ధర్మంబు గోరిక లతనికిఁ గురియుచుండు",
        "సంతోషి గాఁ డేని శక్రుఁ డైన నశించు నిర్ధనుం డైనను నింద్రుఁ బోలు",
        "సంతసించెనేని, సర్వభూతసుహృత్త, ములకుఁ బ్రాప్తలాభ ముదిత మాన",
        "సులకు శాంతులకును సుజనులకును గర్వ, హీనులకును వినతు లే నొనర్తు."], "॥ 1701 ॥", "[Sīsam with āṭaveladi] \"O lord among brāhmaṇas, when your mind is content your dharma comes easily. The elders hold it so: a brāhmaṇa rejoices to gain whatever wealth comes; he keeps to his dharma and does not stray, and that dharma rains his wishes upon him. One who is not content perishes though he be Indra; one who is content is like Indra though he be penniless. To those who are content, friends to all beings, glad at heart with what they gain, peaceful, good and free of pride, I make my bow.\""),
    _v([
        "ఎవ్వని దేశమం దునికి; యెవ్వనిచేఁ గుశలంబు గల్గు మీ;",
        "కెవ్వని రాజ్యమందుఁ బ్రజలెల్ల సుఖింతురు వాఁడు మత్ప్రియుం",
        "'డివ్వనరాశి దుర్గమున కె ట్లరుదెంచితి వయ్య! నీవు? లే",
        "నవ్వులు గావు; నీ తలఁపునం గల మే లొనరింతు ధీమణీ!"], "॥ 1702 ॥", "[Utpalam] \"In whose land do you dwell? By whom is your welfare secured? He in whose kingdom all the people live happily is dear to me. How did you come to this fortress in the ocean, sir? These are no idle words: whatever good you have in mind I shall bring about, O wise one!\""),
    _v([
        "అని యిట్లు లీలాగృహీతశరీరుండైన యప్పరమేశ్వరుం డడిగిన ధరణీసురవరుం డతనికి సవినయంబుగ",
        "నిట్లనియె. దేవా! విదర్భదేశాధీశ్వరుండైన భీష్మకుండను రాజు గలం; డా రాజుకూఁతురు రుక్మిణి యను",
        "కన్యకామణి గల; ద య్యిందువదన నీకుఁ గైంకర్యంబు సేయంగోరి వివాహమంగళ ప్రశస్తంబయిన",
        "యొక్కసందేశంబు విన్నవింపు మని పుత్తెంచె నవధరింపుము."], "॥ 1703 ॥", "[Vacanam] When the supreme Lord, who had taken a body in play, asked thus, the excellent brāhmaṇa answered humbly: \"Lord! There is a king named Bhīṣmaka, ruler of Vidarbha. That king has a daughter, a jewel among maidens, named Rukmiṇī. That moon-faced girl, longing to serve you, has sent me to make known a message about an auspicious marriage. Please hear it.\"", prose=True),
    _v([
        "ఏ నీ గుణములు కర్ణేంద్రియంబులు సోఁక దేహతాపంబులు దీరిపోవు",
        "నే నీ శుభాకార మీక్షింపఁ గన్నుల కఖిలార్థలాభంబు గలుగుచుండు",
        "నే నీ చరణసేవ లేప్రొద్దుఁ జేసిన భువనోన్నతత్వంబు బొందఁ గలుగు",
        "నే నీ లసన్నామ మే ప్రొద్దు భక్తితోఁ దడవిన బంధసంతతులు వాయు",
        "నట్టి నీ యందు నాచిత్త మనవరతము, నచ్చి యున్నది నీ యాన నాన లేదు,",
        "కరుణఁ జూడుము కంసారి! ఖలవిదారి! శ్రీయుతాకార! మానినీచిత్తచోర!"], "॥ 1704 ॥", "[Sīsam with tēṭagīti] \"You whose virtues, once they touch the ears, end the body's torments; whose auspicious form, once seen, brings the eyes the gain of all things; whose feet, served at every hour, raise one to the heights of the worlds; whose shining name, recalled with devotion at any hour, loosens the chains of bondage — on such a one my heart is set, always. I swear by you, I feel no shame in saying it. Look on me with compassion, foe of Kaṃsa, destroyer of the wicked, of glorious form, thief of women's hearts!\""),
    _v([
        "ధన్యున్ లోకమనోఽభిరాముఁ గులవిద్యారూపతారుణ్య సౌ",
        "జన్యశ్రీబలదానశౌర్యకరుణాసంశోభితున్ నిన్ను నే",
        "కన్యల్ గోరరు? కోరదే మును రమాకాంతాలలామంబు రా",
        "జన్యానేకపసింహ! నావలననే జన్మించెనే మోహముల్?"], "॥ 1705 ॥", "[Śārdūlam] \"Blessed one, delight of the hearts of the world, adorned with lineage, learning, beauty, youth, goodness, fortune, strength, generosity, valour and compassion — what maiden would not desire you? Did not Ramā, the jewel among women, choose you long ago? O lion to the elephants that are kings, is this longing born in me alone?\""),
    _v([
        "శ్రీయుతమూర్తి! యో పురుషసింహమ! సింహముపాలి సొమ్ము గో",
        "మాయువు గోరుచందమున మత్తుఁడు చైద్యుఁడు నీ పదాంబుజ",
        "ధ్యాయినియైన నన్ను వడిఁ దాఁ గొనిపోయెద నంచు నున్న వాఁ",
        "డా యధమాధముం డెరుఁగఁ డద్భుతమైనభవత్ప్రతాపమున్."], "॥ 1706 ॥", "[Utpalam] \"O glorious one, lion among men! Like a jackal wanting the lion's share, the arrogant Cedi king thinks to carry me off by force — me who meditate on your lotus feet. That lowest of the low does not know your wondrous might.\""),
    _v([
        "వ్రతముల్ దేవగురుద్విజన్మబుధసేవల్ దానధర్మాదులున్",
        "గతజన్మంబుల నీశ్వరున్ హరి జగత్కల్యాణుఁ గాంక్షించి చే",
        "సితి నేనిన్ వసుదేవనందనుఁడు నా చిత్తేశుఁ డౌఁగాక ని",
        "ర్జితులై పోదురుగాక సంగరములోఁ జేదీశముఖ్యాధముల్."], "॥ 1707 ॥", "[Mattebham] \"If in past births I have kept vows, served the gods, teachers, the twice-born and the wise, given gifts and done good works, longing for the Lord, Hari, the good of the world, then may Vasudeva's son become my heart's lord, and may the Cedi king and the other vile chiefs go down defeated in battle.\""),
    _v([
        "అంకిలి సెప్పలేదు; చతురంగబలంబులతోడ నెల్లి యో",
        "పంకజనాభ! నీవు శిశుపాలజరాసుతులన్ జయించి నా",
        "వంకకు వచ్చి రాక్షసవివాహమునన్ భవదీయశౌర్యమే",
        "యుంకువ సేసి కృష్ణ! పురుషోత్తమ! చేకొని పొమ్ము వచ్చెదన్."], "॥ 1708 ॥", "[Utpalam] \"There is no holding back in saying it: tomorrow, O lotus-naveled one, come with your fourfold army, defeat Śiśupāla and Jarāsandha, come to my side and, making your own valour my bride-price, take me by the rākṣasa rite and go, Kṛṣṇa, supreme Person — I will come.\""),
    _v([
        "లోపలి సౌధంబులోన వర్తింపంగఁ దేవచ్చునే నిన్నుఁ దెత్తునేనిఁ",
        "గావలివారలఁ గల బంధువులఁ జంపి కాని తేరా దని కమలనయన!",
        "భావించితేని నుపాయంబు సెప్పెద నాలింపు కులదేవయాత్రఁ జేసి",
        "నగరంబు వెలువడి నగజాతకును మ్రొక్కఁ బెండ్లికి మునుపడఁ బెండ్లికూఁతు",
        "నెలమి మావారు పంపుదు రేను నట్లు, పురము వెలువడి యేతెంచి భూతనాథు",
        "సతికి మ్రొక్కంగ నీవు నా సమయమందు, వచ్చి కొనిపొమ్ము నన్ను నవార్యచరిత!"], "॥ 1709 ॥", "[Sīsam with tēṭagīti] \"If you think, lotus-eyed one, 'How could I bring her out of the inner palace? I could not without killing the guards and her kinsmen,' I shall tell you a way; listen. Before the wedding, in a procession to the family goddess, the bride goes out of the city to bow to the mountain's daughter. My people will send me out gladly; I shall leave the city and come to bow to the wife of the lord of beings. At that moment, you whose deeds none can withstand, come and take me away.\""),
    _v([
        "ఘను లాత్మీయ తమోనివృత్తికొరకై గౌరీశుమర్యాద నె",
        "వ్వని పాదాంబుజతోయమందు మునుఁగన్ వాంఛింతు రే నట్టి నీ",
        "యనుకంపన్ విలసింపనేని వ్రతచర్యన్ నూరుజన్మంబులన్",
        "నినుఁ జింతించుచుఁ బ్రాణముల్ విడిచెదన్ నిక్కంబు ప్రాణేశ్వరా!"], "॥ 1710 ॥", "[Mattebham] \"The great long to bathe in the water of your lotus feet, as Gaurī's lord does, to be rid of their own darkness. If your grace does not shine on me, I shall keep my vows and give up my life thinking of you, through a hundred births — truly, lord of my life!\""),
    _v([
        "ప్రాణేశ! నీ మంజుభాషలు వినలేని కర్ణరంధ్రంబులకలిమి యేల?",
        "పురుషరత్నమ! నీవు భోగింపఁగా లేని తనులతవలనిసౌందర్య మేల?",
        "భువనమోహన! నిన్నుఁ బొడగానఁగా లేని చక్షురింద్రియములసత్త్వ మేల?",
        "దయిత! నీ యధరామృతం బానఁగా లేని జిహ్వకు ఫలరససిద్ధి యేల?",
        "నీరజాతనయన! నీ వనమాలికా, గంధ మబ్బలేని ఘ్రాణ మేల?",
        "ధన్యచరిత! నీకు దాస్యంబు సేయని, జన్మ మేల? యెన్ని జన్మములకు?"], "॥ 1711 ॥", "[Sīsam with āṭaveladi] \"Lord of my life, what use is the wealth of ears that cannot hear your sweet words? Jewel among men, what use is the beauty of a creeper-like body that you do not enjoy? Enchanter of the worlds, what use is the power of eyes that cannot behold you? Beloved, what use is the tongue's gift of taste if it cannot drink the nectar of your lips? Lotus-eyed one, what use is a nose that cannot catch the fragrance of your forest garland? Blessed one, what use is a birth not spent in your service — in any number of births?\""),
    _v([
        "అని యిట్లు రుక్మిణీదేవి పుత్తెంచిన సందేశంబును, రూపసౌందర్యాదివిశేషంబులును బ్రాహ్మణుండు",
        "హరికి విన్నవించి 'కర్తవ్యం బెద్ది సేయ నవధరింపు’ మని సవర్ణనంబుగా మరియు నిట్లనియె."], "॥ 1712 ॥", "[Vacanam] When the brāhmaṇa had told Hari the message Rukmiṇī Devī had sent, and the excellences of her beauty and the rest, he said, \"Be pleased to decide what is to be done,\" and, describing her, spoke further:", prose=True),
    _v([
        "పల్లవవైభవాస్పదములు పదములు గనకరంభాతిరస్కారు లూరు;",
        "లరుణప్రభామనోహరములు గరములు గంబు సౌందర్యమంగళము గళము",
        "మహితభావాభావమధ్యంబు మధ్యంబు చక్షురుత్సవదాయి చన్నుదోయి",
        "పరిహసితార్ధేందుపటలంబు నిటలంబు జితమత్తమధుకరశ్రేణి వేణి",
        "భావజాశుగములప్రాపులు చూపు లు, కుసుమశరునివింటికొమలు బొమలు",
        "చిత్తతోషణములు చెలువభాషణములు, జలజనయనముఖము చంద్రసఖము."], "॥ 1713 ॥", "[Sīsam with āṭaveladi] \"Her feet are the home of the splendour of fresh shoots; her thighs put golden plantain stems to shame; her hands are lovely with the glow of dawn; her throat has the auspicious beauty of a conch; her waist is so fine it seems both to be and not to be; her breasts are a feast for the eyes; her forehead mocks the half-moon; her braid outdoes a row of maddened bees; her glances are the home of Love's arrows; her brows are the tips of the flower-archer's bow; her charming words delight the heart; the face of that lotus-eyed one is a friend to the moon.\""),
    _v([
        "ఆ యెలనాఁగ నీకుఁ దగు; నంగనకుం దగు దీవు; మా యుపా",
        "ధ్యాయులయాన పెండ్లి యగుఁ; దప్పదు; జాడ్యము లేల? నీవు నీ",
        "తోయమువారిఁ గూడుకొని తోయరుహాననఁ దెత్తుగాని వి",
        "చ్చేయుము; శత్రులన్ నురుముసేయుము; సేయుము శోభనం బిలన్."], "॥ 1714 ॥", "[Utpalam] \"That young woman is fit for you; you are fit for her. By our teacher's oath, the wedding will take place; it cannot fail. Why delay? Gather your own people and come to bring the lotus-faced one; crush the enemies; and celebrate the auspicious wedding on earth.\""),
    {"heading": "Kṛṣṇa sets out by chariot for Kuṇḍina"},
    _v([
        "అని యిట్లు పలికి, బ్రాహ్మణునివలన విదర్భరాజతనయ పుత్తెంచిన సందేశంబును, రూపసౌందర్యాది",
        "విశేషంబులును విని, యవధరించి, నిజకరంబున నతని కరంబుఁబట్టి నగుచు న య్యాదవేంద్రుం డిట్లనియె."], "॥ 1715 ॥", "[Vacanam] So the brāhmaṇa spoke. Having heard from him the message sent by Vidarbha's princess and the excellences of her beauty, the lord of the Yādavas weighed it, took the brāhmaṇa's hand in his own, and said, smiling:", prose=True),
    _v([
        "కన్నియమీఁద నాతలఁపు గాఢము; కూరుకు రాదు రేయి నా",
        "కెన్నఁడు; నా వివాహము సహింపక రుక్మి తలంచు కీడు నే",
        "మున్నె యెరుంగుదున్; బరులమూఁక లడంచి కుమారిఁ దెత్తు వి",
        "ద్వన్నుత! మాను ద్రచ్చి నవవహ్నిశిఖన్ వడిఁ దెచ్చు కైవడిన్."], "॥ 1716 ॥", "[Utpalam] \"My thoughts are deep on the maiden; sleep never comes to me at night. I knew long ago the harm Rukmī plans, unable to bear my marriage. I shall crush the hosts of my enemies and bring the princess, O you praised by the learned, as one churns the fire-wood and swiftly draws out a fresh flame.\""),
    _v([
        "వచ్చెద విదర్భభూమికిఁ; జొచ్చెద భీష్మకునిపురము; సురుచిరలీలన్",
        "దెచ్చెద బాలన్; వ్రేల్మిడి, వ్రచ్చెద నడ్డంబు రిపులు వచ్చినఁ బోరన్."], "॥ 1717 ॥", "[Kandam] \"I shall come to the land of Vidarbha; I shall enter Bhīṣmaka's city; with graceful ease I shall bring the girl; and if enemies come in my way to fight, I shall split them in a snap of the fingers.\""),
    _v([
        "అని పలికి, రుక్మిణీదేవిపెండ్లినక్షత్రంబు దెలిసి, తన పంపున రథసారథియైన దారుకుండు శైబ్య సుగ్రీవ",
        "మేఘపుష్పవలాహకంబులను తురగంబులం గట్టి, రథ మాయత్తంబు చేసి తెచ్చిన, నమోఘ మనోరథుండైన",
        "హరి తానును, బ్రాహ్మణుండును రథారోహణంబు సేసి, యేకరాత్రంబున నానర్తకదేశంబులు గడచి,",
        "విదర్భదేశంబునకుం జనియె; నందుఁ గుండినపురీశ్వరుండైన భీష్మకుండు కొడుకునకు వశుండై, కూఁతు",
        "శిశుపాలున కిత్తు నని తలంచి, శోభనోద్యోగంబు సేయించె; నప్పుడు."], "॥ 1718 ॥", "[Vacanam] So saying, he learned the star of Rukmiṇī's wedding. At his order his charioteer Dāruka yoked the horses Śaibya, Sugrīva, Meghapuṣpa and Valāhaka and brought the chariot ready; Hari, whose wishes never fail, mounted it with the brāhmaṇa, crossed the Ānarta lands in a single night and came to Vidarbha. There Bhīṣmaka, lord of Kuṇḍina, yielding to his son and resolved to give his daughter to Śiśupāla, had the wedding preparations made. Then —", prose=True),
    _v([
        "రచ్చలు క్రంతలు రాజమార్గంబులు విపణిదేశంబులు విశదములుగఁ",
        "జేసిరి; చందనసిక్తతోయంబులు గలయంగఁ జల్లిరి; కలువడములు",
        "రమణీయవివిధతోరణములు గట్టిరి సకలగృహంబులఁ జక్క సేసి;",
        "కర్పూరకుంకుమాగరుధూపములు వెట్టి రతివలుఁ బురుషులు నన్నియెడల",
        "వివిధవస్త్రములను వివిధమాల్యాభర, ణానులేపనముల నమరియుండి",
        "రఖిలవాద్యములు మహాప్రీతి మ్రోయించి, రుత్సవమున నగర మొప్పి యుండె."], "॥ 1719 ॥", "[Sīsam with āṭaveladi] the squares, lanes, royal roads and market places were made clean; they sprinkled water mixed with sandal; they hung garlands of lilies and lovely arches of many kinds; they set every house in order; men and women everywhere burned camphor, saffron and aloe incense; adorned with fine clothes, garlands, ornaments and unguents, they had every instrument sounded with great joy, and the city shone with festival."),
    _v([
        "అంత నా భీష్మకుండు విహితప్రకారంబునం బితృదేవతల నర్చించి బ్రాహ్మణులకు భోజనంబులు వెట్టించి,",
        "మంగళాశీర్వచనంబులు సదివించి, రుక్మిణీదేవి నభిషిక్తం జేసి, వస్త్రయుగళభూషితం గావించి, రత్నభూషణంబు",
        "లిడం జేసె; బుగ్యజుస్సామాథర్వణమంత్రంబుల మంగళాచరణంబు లొనరించి, భూసురులు రక్షాకరణంబు",
        "లాచరించిరి; పురోహితుండు గ్రహశాంతికొరకు నిగమనిగదితన్యాయంబున హోమంబుఁ గావించె; మరియు",
        "నా రాజుదంపతుల మేలుకొరకుఁ దిలధేనుకలధౌతకనకచేలాదిదానంబులు ధరణీదేవతల కొసంగె",
        "నయ్యవసరంబున."], "॥ 1720 ॥", "[Vacanam] Then Bhīṣmaka, as prescribed, worshipped the ancestors, fed the brāhmaṇas, had blessings recited, had Rukmiṇī Devī bathed, dressed in a pair of garments and decked with jewels. The brāhmaṇas performed the auspicious rites with mantras of the Ṛk, Yajus, Sāman and Atharvan, and the rites of protection; the family priest made the fire-offering to appease the planets by the method the Veda lays down; and for the good of the royal couple the king gave sesame, cows, silver, gold, cloth and other gifts to the brāhmaṇas. At that time —", prose=True),
    _v([
        "భటసంఘంబులతో రథావళులతో భద్రేభయూథంబుతోఁ",
        "బటువేగాన్వితఘోటకవ్రజముతో బంధుప్రియశ్రేణితోఁ",
        "గటుసంరంభముతో విదర్భతనయం గైకొందు నంచున్ విశం",
        "కట వృత్తిం జనుదెంచెఁ జైద్యుఁడు గడున్ గర్వించి య వ్వీటికిన్."], "॥ 1721 ॥", "[Mattebham] with hosts of soldiers, rows of chariots, herds of fine elephants, troops of swift horses and lines of kin and friends, in fierce pomp, the Cedi king came to that city, full of pride, boldly, saying, \"I shall take the princess of Vidarbha.\""),
    _v([
        "బంధులఁ గూడి కృష్ణబలభద్రులు వచ్చినఁ బారఁ దోలి ని",
        "ర్మంథరవృత్తిఁ జైద్యునికి మానినిఁ గూర్చెద మంచు నుల్లస",
        "త్సింధుర వీరరథ్యరథసేనలతోఁ జనుదెంచి రా జరా",
        "సంధుఁడు దంతవక్త్రుఁడును సాల్వవిదూరకపౌండ్రకాదులున్."], "॥ 1722 ॥", "[Utpalam] \"If Kṛṣṇa and Balabhadra come with their kin, we shall drive them off and calmly give the lady to the Cedi king,\" they said; and with gleaming elephants, heroic chariot-fighters and chariot forces there came King Jarāsandha, Dantavaktra, Sālva, Vidūraka, Pauṇḍraka and others."),
    _v([
        "మరియు నానాదేశంబుల రాజు లనేకు లేతెంచి; రందు శిశుపాలు నెదుర్కొని పూజించి, భీష్మకుం డొక్క",
        "నివేశంబున నతని విడియించె; నంత నా వృత్తాంతంబు విని."], "॥ 1723 ॥", "[Vacanam] And many kings came from many lands. Bhīṣmaka received Śiśupāla, honoured him and lodged him in a residence. Then, hearing the news,", prose=True),
    _v([
        "హరి యొకఁ డేగినాఁడు మగధాదులు చైద్యహితానుసారులై",
        "నరపతు లెందరేనిఁ జనినారు కుమారికఁ దెచ్చుచోట సం",
        "గర మగుఁ; దోడు గావలయుఁ గంసవిరోధికి నంచు వేగఁ దా",
        "నరిగె హలాయుధుండు గమలాక్షునిజాడ ననేకసేనతోన్."], "॥ 1724 ॥", "[Campakam] \"Hari has gone alone; the kings of Magadha and others, partisans of the Cedi king, have gone in great numbers; there will be a battle where the maiden is fetched, and Kaṃsa's foe must have help\" — so saying, the plough-bearer (Balarāma) went quickly after the lotus-eyed one with a large army."),
    _v([
        "ఆ లోపల నేకతమున, నాలోలవిశాలనయన యగు రుక్మిణి త",
        "న్నా లోకలోచనుఁడు హరి, యాలోకము చేసి కదియఁ డని శంకితయై."], "॥ 1725 ॥", "[Kandam] Meanwhile, alone, Rukmiṇī of the wide, restless eyes grew anxious, thinking: \"Hari, eye of the world, has not looked my way and is not coming near.\""),
    _v([
        "లగ్నం బెల్లి; వివాహముం గదిసె; నేలా రాఁడు గోవిందు? డు",
        "ద్విగ్నం బయ్యెడి మానసంబు; వినెనో వృత్తాంతమున్; బ్రాహ్మణుం",
        "డగ్నిద్యోతనుఁ డేటికిం దడసె? నా యత్నంబు సిద్ధించునో",
        "భగ్నంబై చనునో విరించికృత మెబ్భంగిన్ బ్రవర్తించునో?"], "॥ 1726 ॥", "[Śārdūlam] \"The auspicious hour is tomorrow; the wedding is upon me; why does Govinda not come? My mind is troubled. Did he hear the news? Why does the brāhmaṇa Agnidyotana delay? Will my effort succeed, or will it be broken? How will what Brahmā has written turn out?\""),
    _v([
        "ఘనుఁ డా భూసురుఁ డేఁగెనో? నడుమ మార్గశ్రాంతుఁడై చిక్కెనో",
        "విని కృష్ణుం డిది తప్పుగాఁ దలఁచెనో? విచ్చేసెనో? యీశ్వరుం",
        "డనుకూలింపఁ దలంచునో తలఁపఁడో? యార్యామహాదేవియున్",
        "నను రక్షింప నెరుంగునో యెరుఁగదో? నా భాగ్య మెట్లున్నదో?"], "॥ 1727 ॥", "[Mattebham] \"Did that great brāhmaṇa go? Did he get stuck on the way, worn out by the road? Did Kṛṣṇa hear it and think it wrong? Is he coming? Does the Lord mean to favour me or not? Does the great goddess Āryā know to protect me or not? How does my fortune stand?\""),
    _v([
        "అని వితర్కించుచు."], "॥ 1728 ॥", "[Vacanam] Pondering thus,", prose=True),
    _v([
        "పోఁ డను బ్రాహ్మణుండు యదుపుంగవు వీటికి; వాసుదేవుఁడున్",
        "రాఁ డను; నింకఁ బోయి హరి రమ్మని చీరెడి యిష్టబంధుఁడున్",
        "లేఁ డను; రుక్మికిం దగవు లే దిటఁ జైద్యున కిత్తు నంచు ను",
        "న్నాఁ డను; గౌరి కీశ్వరికి నావలనం గృప లేదు నేఁ డనున్."], "॥ 1729 ॥", "[Utpalam] she says, \"The brāhmaṇa will not have gone to the city of the best of Yadus\"; she says, \"Vāsudeva will not come\"; she says, \"There is no dear kinsman now to go and call Hari here\"; she says, \"Rukmī has no sense of right; he means to give me to the Cedi king\"; she says, \"Gaurī, the goddess, has no pity for me today.\""),
    _v([
        "చెప్పదు తల్లికిం దలఁపుఁజిక్కు; దిశల్ దరహాసచంద్రికం",
        "గప్పదు; వక్త్రతామరసగంధసమాగతభృంగసంఘమున్",
        "రొప్పదు; నిద్రఁ గైకొన దురోజపరస్పరసక్తహారముల్",
        "విప్పదు; కృష్ణమార్గగతవీక్షణపంక్తులు ద్రిప్ప దెప్పుడున్."], "॥ 1730 ॥", "[Utpalam] She does not tell her mother the trouble in her mind; she does not cover the quarters with the moonlight of her smile; she does not drive off the swarm of bees drawn to the fragrance of her lotus face; she takes no sleep; she does not undo the necklaces tangled on her breasts; she never turns away the rows of glances fixed on the road Kṛṣṇa will come by."),
    _v([
        "తుడువదు కన్నులన్ వెడలు తోయకణంబులు; కొప్పుఁ జక్కగా",
        "ముడువదు; నెచ్చెలిం గదిసి ముచ్చటకుం జన; దన్న మేమియుం",
        "గుడువదు; నీరముం గొనదు; కూరిమి కీరముఁ జేరి పద్యమున్",
        "నొడువదు; వల్లకీగుణవినోదము సేయదు; డాయ దన్యులన్."], "॥ 1731 ॥", "[Campakam] She does not wipe the drops that flow from her eyes; she does not tie up her hair neatly; she does not go to her friend to talk; she eats no food at all; she takes no water; she does not go to her dear parrot to recite verse; she does not amuse herself with the strings of the vīṇā; she does not go near anyone."),
    _v([
        "మృగనాభి యలఁదదు మృగరాజమధ్యమ జలముల నాడదు జలజగంధి",
        "ముకురంబుఁ జూడదు ముకురసన్నిభముఖి పువ్వులు దురుమదు పువ్వుఁబోణి",
        "వనకేళిఁ గోరదు వనజాతలోచన హంసంబుఁ బెంపదు హంసగమన",
        "లతలఁ బోషింపదు లతికాలలితదేహ తొడవులు దొడవదు తొడవు తొడవు",
        "తిలక మిడదు నుదుటఁ దిలకినీతిలకంబు, కమలగృహముఁ జొరదు కమలహస్త",
        "గారవించి తన్నుఁ గరుణఁ గైకొన వన, మాలి రాఁడు తగవుమాలి యనుచు."], "॥ 1732 ॥", "[Sīsam with āṭaveladi] She of the lion's waist puts on no musk; she, fragrant as a lotus, does not bathe; she whose face is like a mirror does not look in the mirror; she, lovely as a flower, puts no flowers in her hair; the lotus-eyed one cares nothing for play in the garden; she of the swan's gait does not tend the swan; she of the creeper-like body does not nurture the creepers; she, ornament of ornaments, wears no ornaments; the best of fair women puts no mark on her forehead; she of the lotus hands does not enter the lotus-house — \"He who wears the forest garland will not come to take me in kindness and honour; he has forgotten what is right,\" she says."),
    _v([
        "మరియును."], "॥ 1733 ॥", "[Vacanam] And further,", prose=True),
    _v([
        "మలఁగున్ మెల్లని గాలికిం; బటురటన్మత్తద్విరేఫాళికిం",
        "దలఁగుం; గోయిలమ్రోఁతకై యలఁగు; నుద్యత్కీరసంభాషలం",
        "గలఁగున్; వెన్నెలవేడిమి న్నలఁగు; మాకందాంకురచ్ఛాయకుం",
        "దొలఁగుం గొమ్మ మనోభవానలశిఖాదోదూయమానాంగియై."], "॥ 1734 ॥", "[Mattebham] the girl, her limbs shaken by the flames of the fire of love, shrinks from the soft breeze, draws back from the swarms of loud-humming bees, is upset by the cuckoo's call, is troubled by the chatter of the parrots, is worn by the heat of the moonlight, and moves away from the shade of the mango shoots."),
    _v([
        "ఇట్లు హరిరాక కెదురు సూచుచు సకలప్రయోజనంబులందును విరక్తయై మనోజానలంబునం బొగిలెడి",
        "మగువకు శుభంబుఁ జెప్పుచందంబున వామలోచనభుజంబు లదరె నంతఁ గృష్ణునియోగంబున వేగంబున",
        "బ్రాహ్మణుండు సనుదెంచిన, నతనిముఖలక్షణం బుపలక్షించి యా కలకంఠి మహోత్కంఠతోడ నకుంఠితయై",
        "మొగంబునం జిరునగవు నిగుడ నెదురు సని నిలువంబడిన బ్రాహ్మణుం డిట్లనియె."], "॥ 1735 ॥", "[Vacanam] As the lady, watching thus for Hari's coming, indifferent to everything and burning in the fire of love, lay tormented, her left eye and arm throbbed, as if foretelling good. Then the brāhmaṇa, sent back quickly by Kṛṣṇa, arrived; reading the signs on his face, she of the cuckoo's voice, full of longing and now unhindered, went to meet him with a smile spreading on her face and stood before him, and the brāhmaṇa said:", prose=True),
    _v([
        "మెచ్చె భవద్గుణోన్నతి; కమేయధనావళు లిచ్చె నాకుఁ; దా",
        "వచ్చె సుదర్శనాయుధుఁడు వాఁడె; సురాసురు లెల్ల నడ్డమై",
        "వచ్చిన నైన రాక్షసవివాహమునం గొనిపోవు నిన్ను; నీ",
        "సచ్చరితంబు భాగ్యమును సర్వము నేఁడు ఫలించెఁ గన్యకా!"], "॥ 1736 ॥", "[Utpalam] \"He praised your lofty virtues; he gave me boundless wealth; he has come himself, the bearer of Sudarśana — there he is! Even if all the gods and demons stood in his way, he will carry you off by the rākṣasa rite. Your good conduct, your fortune, everything has borne fruit today, maiden!\""),
    _v([
        "అనిన వైదర్భి యిట్లనియె."], "॥ 1737 ॥", "[Vacanam] At this the princess of Vidarbha said:", prose=True),
    {"heading": "Rukmiṇī bows to Agnidyotana, the brāhmaṇa messenger"},
    _v([
        "జలజాతేక్షణుఁ దోడితెచ్చితివి నా సందేశమున్ జెప్పి; నన్",
        "నిలువం బెట్టితి; నీ కృపన్ బ్రదికితిన్; నీయంత పుణ్యాత్మకుల్",
        "గలరే? దీనికి నీకుఁ బ్రత్యుపకృతిం గావింప నే నేర; నం",
        "జలిఁ గావించెద; భూసురాన్వయమణీ! సద్బంధుచింతామణీ!"], "॥ 1738 ॥", "[Mattebham] \"You brought the lotus-eyed one, telling him my message; you have kept me alive; by your grace I live. Is anyone as virtuous as you? I cannot repay you for this; I fold my hands to you, jewel of the brāhmaṇa line, wish-jewel among true kinsmen!\""),
    _v([
        "అని నమస్కరించె; నంత రామకృష్ణులు తమకూఁతువివాహంబునకు వచ్చుట విని, తూర్యఘోషంబు",
        "లతో నెదుర్కొని, విధ్యుక్తప్రకారంబునం బూజించి మధుపర్కంబు లిచ్చి, వివిధాంబరాభరణంబులు మొదలైన",
        "కానుక లొసంగి, భీష్మకుండు బంధుజనసేనాసమేతులైనవారలకుం దూర్ణంబున సకల సంపత్పరిపూర్ణంబులైన",
        "నివేశంబులు కల్పించి విడియించె; నిట్లు కూడినరాజుల కెల్లను వయోవీర్య బలవిత్తంబు లెట్లట్ల కోరినపదార్థంబు",
        "లెల్ల నిప్పించి పూజించె; నంత విదర్భపురంబుప్రజలు హరిరాక విని వచ్చి చూచి, నేత్రాంజలులం",
        "దదీయవదనకమలమధుపానంబు సేయుచు."], "॥ 1739 ॥", "[Vacanam] So she bowed to him. Then Bhīṣmaka, hearing that Rāma and Kṛṣṇa had come to his daughter's wedding, went out to meet them with the sound of trumpets, worshipped them as prescribed, gave them madhuparka, presented gifts of fine clothes, ornaments and the like, and quickly lodged them with their kinsmen and armies in residences full of every comfort. So he honoured all the assembled kings, having whatever each wished given according to age, valour, strength and wealth. Then the people of Vidarbha's city, hearing of Hari's coming, came to see him and, drinking the honey of his lotus face with the cupped hands of their eyes, (said:)", prose=True),
    _v([
        "తగు నీచక్రి విదర్భరాజసుతకుం; దథ్యంబు వైదర్భియుం",
        "దగు నీచక్రికి; నింతమంచి దగునే? దాంపత్య మీ యిద్దరిం",
        "దగులం గట్టిన బ్రహ్మ నేర్పరి గదా! దర్పాహతారాతియై",
        "మగఁడౌ గావుతఁ జక్రి యీ రమణికిన్ మా పుణ్యమూలంబునన్."], "॥ 1740 ॥", "[Mattebham] \"This discus-bearer is fit for Vidarbha's daughter; truly, the princess too is fit for him. Could a better match be found? How skilled is Brahmā, to have bound these two in marriage! May the discus-bearer, crushing the pride of his foes, become this lady's husband, by the root of our merit.\""),
    _v([
        "అని పలికి రా సమయంబున."], "॥ 1741 ॥", "[Vacanam] So they said. At that time —", prose=True),
    _v([
        "సన్నద్ధులై బహుశస్త్రసమేతులై బలసి చుట్టును వీరభటులు గొలువ",
        "ముందట నుపహారములు గానుకలుఁ గొంచు వర్గంబులై వారవనిత లేఁగఁ",
        "బుష్పగంధాంబరభూషణకలితలై పాడుచు భూసురభార్య లరుగఁ",
        "బణవమర్దలశంఖపటహకాహళవేణుభేరీధ్వనుల మిన్ను పిక్కటిలఁగఁ",
        "దగిలి సఖులు గొలువఁ దల్లులు బాంధవ, సతులుఁ దోడ రాఁగ సవినయముగ",
        "నగరు వెడలి నడచె నగజాతకును మ్రొక్క, బాల చికురపిహితఫాల యగుచు."], "॥ 1742 ॥", "[Sīsam with āṭaveladi] armed heroes bearing many weapons around her on every side; courtesans going ahead in groups with offerings and gifts; the wives of brāhmaṇas walking and singing, decked with flowers, perfumes, fine clothes and ornaments; the sky resounding with tabors, drums, conches, kettle-drums, horns, flutes and great drums; her friends close about her and her mothers and the wives of kinsmen coming with her — the girl, her forehead hidden by her locks, humbly left the palace and walked to bow to the mountain's daughter."),
    _v([
        "మరియు సూతమాగధవందిగాయకపాఠకజను లంతంత నభినందించుచుం జనుదేర మందగమనంబున,",
        "ముకుందచరణారవిందంబులు డెందంబునం దలంచుచు నిందుధరసుందరీ మందిరంబు సేరి",
        "సలిలధారాధౌతకరచరణారవిందయై వార్చి శుచియై, గౌరీసమీపంబునకుం జనియె; నంత ముత్తైదువలగు",
        "భూసురోత్తముల భార్యలు భవసహితయైన భవానికి మజ్జనంబు గావించి గంధాక్షతంబు లిడి,",
        "వస్త్రమాల్యభూషణాదుల నలంకరించి, ధూపదీపంబు లొసంగి, నానావిధోపహారంబులు సమర్పించి, కానుక",
        "లిచ్చి, దీపమాలికల నివాళించి రుక్మిణీదేవిని మ్రొక్కించి రప్పుడు."], "॥ 1743 ॥", "[Vacanam] And with bards, heralds, panegyrists, singers and reciters praising her on every side, she went at a slow pace, thinking in her heart of Mukunda's lotus feet, and reached the temple of the lovely consort of the moon-bearer. She washed her lotus hands and feet in streams of water, sipped water, became pure, and went up to Gaurī. Then the wives of brāhmaṇas, married women with husbands living, bathed Bhavānī together with Bhava, applied sandal and rice, adorned her with cloth, garlands and ornaments, offered incense, lamps and food of many kinds, gave gifts, waved rows of lamps, and had Rukmiṇī Devī bow down. Then —", prose=True),
    _v([
        "నమ్మితి నా మనంబున సనాతనులైన యుమామహేశులన్",
        "మిమ్ముఁ బురాణదంపతుల మేలు భజింతు గదమ్మ! మేటి పె",
        "ద్దమ్మ దయాంబురాశివి గదమ్మ హరిం బతి సేయు మమ్మ నిన్",
        "నమ్మినవారి కెన్నఁడును నాశము లేదు గదమ్మ యీశ్వరీ!"], "॥ 1744 ॥", "[Utpalam] \"I have trusted in my heart in you, Umā and Maheśa, the eternal ones; I worship you, the ancient couple, for my good, mother. You are the great elder mother, an ocean of mercy, mother; make Hari my husband, mother. Those who trust in you never come to ruin, mother, O Goddess!\""),
    _v([
        "అని గౌరీదేవికి మ్రొక్కి పతులతోడం గూడిన బ్రాహ్మణభార్యలకు లవణాపూపంబులును, దాంబూల",
        "కంఠసూత్రంబులును, నిక్షుదండంబులు నిచ్చి రుక్మిణీదేవి వారలం బూజించిన."], "॥ 1745 ॥", "[Vacanam] So saying she bowed to Gaurī Devī; and when Rukmiṇī Devī honoured the brāhmaṇa wives with their husbands, giving them salted cakes, betel, sacred necklaces and sugarcane,", prose=True),
    _v([
        "వార లుత్సహించి వలనొప్ప దీవించి, సేస లిడిరి యువతిశిరమునందు;",
        "సేస లెల్లఁ దాల్చి శివవల్లభకు మ్రొక్కి, మౌననియతి మాని మగువ వెడలె."], "॥ 1746 ॥", "[Āṭaveladi] they blessed her with joy and grace and placed sacred rice on the young woman's head. Bearing all the rice, she bowed to Śiva's beloved, ended her vow of silence, and came out."),
    _v([
        "ఇట్లు మేఘమధ్యంబు వెలువడి విలసించు క్రొక్కారు మెరుంగుతెరంగున, మృగధరమండలంబు నిర్గమించి",
        "చరించుమృగంబు చందంబునఁ, గమలభవ నర్తకుం డెత్తిన జవనిక మరుఁగు దెరలి పొడసూపిన",
        "మోహినీదేవతకైవడి, దేవదానవసంఘాతకరతలసవ్యాపసవ్యసమాకృష్యమాణపన్నగేంద్రపాశపరివలయిత",
        "పర్యాయపరిభ్రాంతమందరాచలమంథానమథ్యమానఘూర్ణిత ఘుమఘుమాయిత మహార్ణవమధ్యంబున నుండి",
        "చనుదెంచు నిందిరాసుందరీవైభవంబున, బహువిధప్రభాభాసమానయై, యిందుధర సుందరీమందిరంబు వెడలి",
        "మానసకాసారహేమకమలకాననవిహరమాణమత్తమరాళంబు భంగి, మందగమనంబునఁ",
        "గనకకలశయుగళసంకాశకర్కశపయోధరభారపరికంప్యమానమధ్యయై, రత్నముద్రికాలంకృతం బైన కెంగేల",
        "నొక్క సఖీలలామంబు కైదండ గొని, రత్ననివహసముదంచితకాంచనకర్ణపత్త్రమయూఖంబులు గండభాగంబుల",
        "నర్తనంబులు సలుప, నరవిందపరిమళకుతూహలావతీర్ణ మత్తమధుకరంబుల మాడ్కి నరాళంబులైన",
        "కుంతలజాలంబులు ముఖమండలంబునఁ గ్రందుకొన, సుందర మందహాసరోచులు దిశలందు",
        "బాలచంద్రికాసౌందర్యంబు నావహింప, నధరబింబఫలారుణ మరీచిమాలికలు రదనకుందకుట్మలంబుల",
        "కనురాగంబు సంపాదింప, మనోజాతకేతనసన్నిభంబైన పయ్యెదకొంగు దూఁగ, సువర్ణమేఖలాఘటిత",
        "మణికిరణపటలంబు లకాలశక్రచాపజనకంబులై మెరయఁ, జెరకువిలుతుం డొరవెరికి వాఁడి యిడి జళిపించిన",
        "ధగద్ధగాయమానంబు లగు బాణంబుల పగిది, సురుచిరవిలోకననికరంబులు రాజవీరులహృదయంబులు భేదింప,",
        "శింజానమంజుమంజీర నినదంబులు చెవుల పండువులు సేయఁ, బాదసంచారంబున హరిరాక కెదురుచూచుచు,",
        "వీరమోహినియై చనుదెంచుసమయంబున."], "॥ 1747 ॥", "[Vacanam] Then — like a flash of fresh lightning gleaming out of the midst of clouds; like the deer leaving the moon's orb to roam free; like the enchantress Mohinī appearing when the dancer, Brahmā, drew the curtain aside; with the splendour of the lovely Indirā rising from the midst of the great ocean as it whirled and roared, churned by the Mandara mountain turning to and fro, girt by the king of serpents and pulled left and right by the hands of the hosts of gods and demons — shining with many kinds of radiance, she came out of the temple of the moon-bearer's consort; like a proud swan moving in the forest of golden lotuses on Lake Mānasa she walked with a slow gait, her waist trembling under the weight of firm breasts like a pair of golden jars; she took the hand of a dear friend in her red hand graced with jewelled rings; the rays of her gem-set golden ear-ornaments danced on her cheeks; her curling locks crowded about her face like bees maddened and come down for the fragrance of the lotus; the light of her lovely smile spread the beauty of young moonlight in every direction; the garlands of rays, red as bimba fruit, from her lips coloured the jasmine-bud teeth; the end of her upper cloth, like the banner of Love, swayed; the clusters of rays from the gems in her golden girdle flashed like untimely rainbows; her bright glances, like gleaming arrows the sugarcane-bowed god had drawn from the quiver, sharpened and brandished, pierced the hearts of the heroic kings; the tinkling of her lovely anklets was a feast to the ears; and as she walked she watched for Hari's coming — at that moment, when she came forth an enchantress of heroes,", prose=True),
    _v([
        "అలినీలాలకఁ బూర్ణచంద్రముఖి నేణాక్షిం బ్రవాళాధరం",
        "గలకంఠిన్ నవపల్లవాంఘ్రియుగళన్ గంధేభకుంభస్తనిం",
        "బులినశ్రోణి నిభేంద్రయాన నరుణాంభోజాతహస్తన్ మహో",
        "త్పలగంధిన్ మృగరాజమధ్యఁ గని విభ్రాంతాత్ములై రందరున్."], "॥ 1748 ॥", "[Mattebham] seeing her — with curls dark as bees, face like the full moon, eyes like a doe's, lips like coral, voice like a cuckoo's, feet like fresh shoots, breasts like the temples of a scented elephant, hips like a sandbank, gait like a lordly elephant's, hands like red lotuses, fragrant as the great water-lily, waist like a lion's — they were all bewildered in their hearts."),
    _v([
        "మరియు న య్యింతి దరహాసలజ్జావలోకనంబులం జిత్తంబు లేమరి ధైర్యంబు దిగనాడి, గాంభీర్యంబులు",
        "విడిచి, గౌరవంబులు మరచి, చేష్టలు మాని, యెరుక లుడిగి, యాయుధంబులు దిగవైచి గజతురగరథా",
        "రోహణంబులు సేయనేరక, రాజులెల్ల నేలకు వ్రాలి; రా యేణీలోచన తన వామకరనఖంబుల నలకంబులు",
        "దలఁగం ద్రోయుచు నుత్తరీయంబు సక్కనొత్తుచుఁ గడగంటిచూపులం గ్రమంబున నా రాజలోకంబు",
        "నాలోకింపుచు."], "॥ 1749 ॥", "[Vacanam] And their minds lost in that woman's smiles and bashful glances, they gave up their courage, abandoned their dignity, forgot their honour, ceased to move, lost their senses, dropped their weapons and, unable to mount their elephants, horses or chariots, all the kings sank to the ground. The doe-eyed one, pushing back her curls with the nails of her left hand and straightening her upper cloth, looked over that assembly of kings in turn with sidelong glances, and", prose=True),
    _v([
        "కనియెన్ రుక్మిణి చంద్రమండలముఖుం గంఠీరవేంద్రావ ల",
        "గ్ను నవాంభోజదళాక్షుఁ జారుతరవక్షున్ మేఘసంకాశ దే",
        "హు నగారాతిగజేంద్రహస్తనిభబాహుం జక్రిఁ బీతాంబరున్",
        "ఘనభూషాన్వితుఁ గంబుకంఠు విజయోత్కంఠున్ జగన్మోహనున్."], "॥ 1750 ॥", "[Mattebham] Rukmiṇī saw him: moon-faced, waisted like a lion-king, eyes like fresh lotus petals, broad and handsome chest, body like a cloud, arms like the trunk of the elephant of Indra, the discus-bearer clad in yellow, richly adorned, conch-necked, eager for victory, enchanter of the world."),
    {"heading": "Kṛṣṇa carries off Rukmiṇī as the enemy kings look on"},
    _v([
        "కని తదీయ రూపవయోలావణ్య వైభవగాంభీర్యచాతుర్యతేజోవిశేషంబులకు సంతసించి, మనోభవ",
        "శరాక్రాంతయై రథారోహణంబు గోరుచున్న వరారోహం జూచి, పరిపంథిరాజలోకంబు సూచుచుండ",
        "మందగమనంబున గంధసింధురంబు లీలం జనుదెంచి ఫేరవంబుల నడిమిభాగంబు గొనిచను కంఠీరవంబు",
        "కైవడి నిఖిలభూపాలగణంబుల గణింపక తృణీకరించి రాజకన్యకం దెచ్చి హరి తనరథంబుమీఁద నిడికొని",
        "భూనభోంతరాళంబులు నిండ శంఖంబు పూరించుచు బలభద్రుండు తోడ నడవ యాదవవాహినీ పరివృతుండై",
        "ద్వారకానగరమార్గంబు వట్టి చనియె; నంత జరాసంధవశులయినరాజులందరు హరిపరాక్రమంబు విని, సహింప",
        "నోపక."], "॥ 1751 ॥", "[Vacanam] Seeing him, she rejoiced at the excellence of his form, youth, grace, splendour, depth, skill and radiance; struck by the arrows of Love, she longed to mount his chariot. Seeing that lovely-hipped woman, as the hostile kings looked on, Hari came forward with the slow gait of a scented elephant and, like a lion carrying off its share from the midst of jackals, paid no heed to the whole host of kings, treated them as straw, took the princess and placed her on his chariot; and blowing his conch till earth and sky were filled, with Balabhadra going beside him and surrounded by the Yādava army, he took the road to Dvārakā. Then all the kings in Jarāsandha's sway, hearing of Hari's prowess and unable to bear it,", prose=True),
    _v([
        "ఘనసింహంబులకీర్తి నీచమృగముల్ గైకొన్నచందంబునన్",
        "మనకీర్తుల్ గొని బాలఁ దోడ్కొనుచు నున్మాదంబుతో గోపకుల్",
        "సనుచున్నా రదె? శౌర్య మెన్నటికి? మీ శస్త్రాస్త్రముల్ గాల్పనే?",
        "తనుమధ్యన్ విడిపింపమేని నగరే ధాత్రీజనుల్ క్రంతలన్."], "॥ 1752 ॥", "[Mattebham] said: \"Like low beasts taking the glory of mighty lions, these cowherds go off in their madness, taking our glory along with the girl — look there! When will our valour show? Shall we burn our weapons and missiles? If we do not free that slender-waisted one, will the people of the earth not laugh at us in the streets?\""),
    _v([
        "అని యొండొరులం దెలుపుకొని, రోషంబులు హృదయంబుల నిలుపుకొని, సంరంభించి, తనుత్రాణంబుల",
        "వహించి, ధనురాదిసాధనంబులు ధరియించి, పంతంబు లాడి, తమ తమ చతురంగబలంబులం గూడికొని,",
        "జరాసంధాదులు యదువీరుల వెంటనంటి, తాఁకి నిలు నిలుండని ధిక్కరించి పలికి యుక్కు మిగిలి, మహీధరంబుల",
        "మీఁద సలిలధారలు గురియు ధారాధరంబులచందంబున బాణవర్షంబులు గురిసిన యాదవసేనలం గల",
        "దండనాయకులు కోదండంబు లెక్కిడి, గుణంబులు మ్రోయించి, నిలువంబడి రప్పుడు."], "॥ 1753 ॥", "[Vacanam] So urging one another, holding anger in their hearts, eagerly they put on their armour, took up bows and other arms, swore oaths, gathered their fourfold armies, and Jarāsandha and the others went after the Yadu heroes, attacked them, shouting \"Stand! Stand!\" in defiance, and in overweening pride poured showers of arrows on them, like rain-clouds pouring streams of water on the mountains. The commanders of the Yādava army strung their bows, twanged the strings and stood their ground. Then —", prose=True),
    _v([
        "అరిబలభటసాయకముల, హరిబలములు గప్పఁబడిన నడరెడు భీతిన్",
        "హరిమధ్య సిగ్గుతోడను, హరివదనముఁ జూచెఁ జకితహరిణేక్షణయై."], "॥ 1754 ॥", "[Kandam] when the hosts of Hari were covered by the arrows of the enemy soldiers, the lion-waisted maiden, in rising fear and with bashfulness, looked at Hari's face, her eyes like a startled doe's."),
    _v([
        "ఇట్లు చూచిన."], "॥ 1755 ॥", "[Vacanam] When she looked at him so,", prose=True),
    _v([
        "చొచ్చెద రదె యదువీరులు, వ్రచ్చెద రరిసేన నెల్ల వైరులు పెలుచున్",
        "నొచ్చెదరును విచ్చెదరును, జచ్చెదరును నేఁడు చూడు జలజాతాక్షీ!"], "॥ 1756 ॥", "[Kandam] \"There — the Yadu heroes are charging in; they will split the whole enemy army; today the foes will be hurt, will scatter and will die, fiercely — watch, lotus-eyed one!\""),
    _v([
        "అని రుక్మిణీదేవిని హరి యూరడించె; నంత బలభద్రప్రముఖులైనయదువీరులు ప్రళయవేళల మిన్నునం",
        "బన్ని బలుపిడుగు లడరించు పెనుమొగిళులవడువున జరాసంధాదిపరిపంథిరాజచక్రంబుమీఁద",
        "నవక్రపరాక్రమంబున శిఖిశిఖాసంకాశనిశితశిలీముఖనారాచభల్ల ప్రముఖంబులైన బహువిధ బాణపరంపరలు",
        "గురియ, నదియును విదళితమత్తమాతంగంబును, విచ్ఛిన్నతురంగంబును, విభిన్న రథవరూథంబును, వినిహత",
        "పదాతియూథంబును, విఖండితవాహవారణరథారోహణమస్తకంబును, విశకలితవక్షోమధ్యకర్ణకంఠ",
        "కపోలహస్తంబును, వీకీర్ణ కేశజాలంబును, విపాటితచరణజానుజంఘంబును, విదళిత దంతసంఘంబును,",
        "విఘటిత వీరమంజీర కేయూరంబును, విభ్రష్ట కుండల కిరీట హారంబును, విస్మృతవీరాలాపంబును,",
        "విదార్యమాణగదాకుంతతోమరపరశుపట్టిసప్రాసకరవాలశూలచక్రచాపంబును, వినిపాతిత",
        "కేతనచామరచ్ఛత్రంబును, విలూనతనుత్రాణంబును, వికీర్యమాణఘోటకసంఘరింఖాసముద్ధూత",
        "ధరణీపరాగంబును, వినష్టరథవేగంబును, వినివారితసూతమాగధవందివాదంబును,",
        "వికుంఠితహయహేషాపటహభాంకార, కరటిఘటాఘీంకార, రథనేమిఫటాత్కార, తురగనాభిఘంటా",
        "ఘణఘణాత్కార, వీరహుంకారభూషణఝణఝణాత్కార, నిస్సాణధణధణాత్కార, మణినూపురక్రేంకార,",
        "కింకిణీగణకిణాత్కార, శింజినీటంకార, భటపరస్పరధిక్కారనాదంబును, వినిర్భిద్యమాన రాజసమూహంబును,",
        "విద్యమానరక్తప్రవాహంబును, విశ్రూయమాణభూతబేతాళకలకలంబును, విజృంభమాణఫేరవకాకకంకాది",
        "సంకులంబును, బ్రచలితకబంధంబును, బ్రభూతపలలగంధంబును, ప్రదీపిత మేదోమాంసరుధిర",
        "ఖాదంబును, బ్రవర్తితడాకినీ ప్రమోదంబునునై యుండె; నప్పుడు."], "॥ 1757 ॥", "[Vacanam] So Hari comforted Rukmiṇī Devī. Then the Yadu heroes led by Balabhadra, like great clouds that gather in the sky at the dissolution of the world and hurl mighty thunderbolts, with unswerving valour rained streams of arrows of every kind — śilīmukhas, nārācas, bhallas and others, sharp and like flames of fire — on the circle of hostile kings led by Jarāsandha. That army became a place where maddened elephants were torn, horses cut apart, fine chariots shattered and hosts of foot-soldiers slain; where the heads of those on elephants, horses and chariots were cut off; chests, waists, ears, throats, cheeks and hands hacked apart; masses of hair strewn about; feet, knees and shanks split; teeth broken; the anklets and armlets of heroes torn off; earrings, crowns and necklaces fallen; heroic shouts forgotten; maces, spears, javelins, axes, swords, lances, sabres, tridents, discuses and bows smashed; banners, whisks and parasols thrown down; armour cut; the dust of the earth raised by the hooves of scattering horses; the speed of chariots gone; the praises of bards, heralds and panegyrists stilled; where there rang the neighing of horses and the roll of drums, the trumpeting of elephant troops, the crack of chariot wheels, the jangle of bells on horses, the war-cries of heroes and the clash of their ornaments, the boom of kettle-drums, the tinkle of jewelled anklets and clusters of bells, the twang of bowstrings and the taunts of soldiers at one another; where the throng of kings was rent, streams of blood flowed, the clamour of goblins and vetālas was heard, jackals, crows, herons and the like swarmed, headless trunks moved, the stench of flesh spread, fat, flesh and blood were devoured and the ḍākinīs revelled. Then —", prose=True),
    _v([
        "మగిడి చలించి పారుచును మాగధముఖ్యులు గూడి యొక్కచో",
        "వగచుచు నాలిఁ గోల్పడినవానిక్రియన్ గడు వెచ్చనూర్చుచున్",
        "మొగమున దప్పిదేరఁ దమ ముందటఁ బొక్కుచు నున్న చైద్యుతోఁ",
        "బగతురచేతిలోఁ బడక ప్రాణముతోడుత నున్నవాఁడవే."], "॥ 1758 ॥", "[Campakam] turning back and fleeing, Māgadha and the other chiefs gathered in one place and, grieving, said to the Cedi king, who stood before them sighing hotly like a man who has lost his wife, his face drawn and smarting: \"You are alive, and have not fallen into the enemy's hands.\""),
    _v([
        "అని మరియును."], "॥ 1759 ॥", "[Vacanam] So saying, and more:", prose=True),
    _v([
        "బ్రతుకవచ్చు నొడలఁ బ్రాణంబు లుండిన, బ్రతుకు గలిగెనేని భార్య గలదు;",
        "బ్రతికి తీవు; భార్యపట్టు దైవ మెరుంగు, వగవ వలదు చైద్య! వలదు వలదు."], "॥ 1760 ॥", "[Āṭaveladi] \"One can go on living while there is life in the body; if there is life, there will be a wife. You are alive; as for a wife, fate knows. Do not grieve, Cedi king — do not, do not.\""),
    _v([
        "వినుము. దేహధారి స్వతంత్రుఁడు గాఁడు. జంత్రగానిచేతి జంత్రపుబొమ్మకైవడి నీశ్వరతంత్ర పరాధీనుండై,",
        "సుఖదుఃఖంబులందు నర్తనంబులు సలుపు. తొల్లి నేను మథురాపురంబుమీఁదఁ బదియేడు మారులు",
        "పరాక్రమంబునన్ విడిసి, చక్రిచేత నిర్మూలితబలచక్రుండనై, కామపాలుచేతం బట్టువడి, యీ కృష్ణుండు కరుణతో",
        "విడిపించిన వచ్చి, క్రమ్మర నిరువదిమూఁ డక్షౌహిణులం గూడికొని, పదునెనిమిదవ మారు దాడిచేసి, శత్రువులం",
        "దోలి, విజయంబు చేకొంటిని. జయాపజయంబులందు హర్షశోకంబుల నెన్నండును జెంద; నేఁటిదినంబున",
        "నీ కృష్ణుని కెదిరి పోర మన రాజలోకంబు లెల్ల నుగ్రాక్షుం గూడుకొని, యెదిరి పోరిన నోడు. ఇంతియ కాక",
        "దైవయుక్తంబైన కాలంబునం జేసి, లోకంబులు పరిభ్రమించుచు నుండు; నదియునుం గాక."], "॥ 1761 ॥", "[Vacanam] \"Listen. An embodied being is not his own master; like a puppet in the puppeteer's hand, dependent on the Lord's will, he dances in joy and sorrow. Once I laid siege to Mathurā seventeen times in my might; my forces were destroyed by the discus-bearer, I was captured by Kāmapāla (Balarāma), and this Kṛṣṇa let me go out of pity. I came back, gathered twenty-three akṣauhiṇīs, attacked an eighteenth time, drove off the enemy and won the victory. In victory and defeat I never feel joy or grief. Today, even if all our kings joined with the fierce-eyed god and fought against this Kṛṣṇa, they would lose. More than that, the worlds turn by time, which is joined with fate. And further:\"", prose=True),
    _v([
        "తమకుం గాలము మంచిదైన మనలం ద్రైలోక్యవిఖ్యాత వి",
        "క్రములం గెల్చిరి యాదవుల్ హరిభుజాగర్వంబునన్ నేఁడు; కా",
        "లము మేలై చనుదెంచెనేని మనమున్ లక్షించి విద్వేషులన్",
        "సమరక్షోణి జయింత మింతపనికై శంకింప నీ కేటికిన్."], "॥ 1762 ॥", "[Mattebham] \"Because time was good for them, the Yādavas today, proud of Hari's arms, have defeated us, whose prowess is famed in the three worlds. When time turns good for us, we shall mark our enemies and conquer them on the field of battle. Why should you be troubled over this?\""),
    _v([
        "అని యిట్లు జరాసంధుండును, నతని యొద్దిరాజులును, శిశుపాలునిపరితాపంబు నివారించి, తమ",
        "తమభూములకుం జనిరి. శిశుపాలుండు ననుచరసేనాసమేతుం డయి తన నగరంబునకుం జనియె; నంత",
        "రుక్మి యనువాఁడు కృష్ణుండు రాక్షసవివాహంబునం దన చెలియలిం గొనిపోవుటకు సహింపక,",
        "యేకాక్షౌహిణీబలంబుతోడ సమరసన్నాహంబునం గృష్ణుని వెనుదగిలి పోవుచుఁ, దన సారథితో నిట్లనియె."], "॥ 1763 ॥", "[Vacanam] So Jarāsandha and the kings with him eased Śiśupāla's distress and went back to their lands, and Śiśupāla went to his city with his followers and army. Then Rukmī, unable to bear Kṛṣṇa's carrying off his sister by the rākṣasa rite, went after Kṛṣṇa ready for battle with an army of one akṣauhiṇī, and said to his charioteer:", prose=True),
    _v([
        "బల్లిదు నన్ను భీష్మజనపాలకుమారునిఁ జిన్నఁ జేసి నా",
        "చెల్లెలి రుక్మిణిం గొనుచుఁ జిక్కని నిక్కపు బంటువోలె నీ",
        "గొల్లఁడు వోయెడిన్; రథముఁ గూడఁగఁ దోలుము; తేజితోల్లస",
        "ద్భల్లపరంపరన్ మదముఁ బాపెదఁ జూపెద నా ప్రతాపమున్."], "॥ 1764 ॥", "[Utpalam] \"Making light of me, the mighty son of King Bhīṣmaka, this cowherd goes off with my sister Rukmiṇī like a true soldier who cannot be caught. Drive the chariot close; with a stream of sharpened, gleaming arrows I shall take away his pride and show him my valour.\""),
    _v([
        "అని యిట్లు రుక్మి హరికొలంది యెరుంగక సారథి నదలించి రథముఁ గూడ దోలించి 'గోపాలకా!",
        "వెన్నమ్రుచ్చ! నిమిషమాత్రంబు నిలు నిలు, మని తిరస్కరించి, బలువింట నారి సారించి మూఁడు",
        "వాఁడితూపుల హరి నొప్పించి యిట్లనియె."], "॥ 1765 ॥", "[Vacanam] So Rukmī, not knowing Hari's measure, urged his charioteer to drive close and, taunting him — \"Cowherd! Butter-thief! Stand, stand, for just a moment!\" — drew the string of his mighty bow, struck Hari with three sharp arrows and said:", prose=True),
    _v([
        "మా సరివాఁడవా మా పాపఁ గొనిపోవ? నేపాటి గలవాఁడ? వేది వంశ?",
        "మెందు జన్మించితి? వెక్కడఁ బెరిఁగితి? వెయ్యది నడవడి? యెవ్వఁ డెరుఁగు?",
        "మానహీనుఁడ వీవు? మర్యాద లెరుఁగవు; మాయఁ గైకొని కాని మలయ రావు;",
        "నిజరూపమున శత్రునివహంబుపైఁ బోవు; వసుధేశుఁడవు గావు వావి లేదు;",
        "కొమ్మ నిమ్ము; నీవు గుణరహితుండవు, విడువు; విడువ వేని విలయకాల",
        "శిఖిశిఖాసమానశితశిలీముఖముల, గర్వ మెల్లఁ గొందుఁ గలహమందు."], "॥ 1766 ॥", "[Sīsam with āṭaveladi] \"Are you our equal, to carry off our girl? What are you worth? What is your lineage? Where were you born? Where did you grow up? What is your conduct? Who knows you? You have no honour; you know no decorum; you never come except by trickery; you never go against your enemies in your true form; you are no king; you have no kinship. Give the girl back; you have no virtues — let her go. If you do not, I shall take all your pride in battle with sharp arrows like the flames of the fire at the end of the world.\""),
    _v([
        "అని పలికిన నగధరుండు నగి, యొక్క బాణంబున వానికోదండంబు ఖండించి, యారు శరంబుల",
        "శరీరంబు దూరనేసి, యెనిమిది విశిఖంబుల రథ్యంబులం గూల్చి, రెండమ్ముల సారథిం జంపి, మూఁడు వాఁ",
        "డితూపులం గేతనంబు ద్రుంచి, మరియు నొక్క విల్లందినం ద్రుంచి, వెండియు నొక్క ధనువు వట్టిన విదళించి,",
        "క్రమంబున పరిఘపట్టిసశూలచర్మాసిశక్తితోమరంబులు ధరియించినం దునుకలు సేసి, క్రమ్మర నాయుధంబు",
        "లెన్ని యెత్తిన నన్నియు శకలంబులు గావించె. నంతటం దనివిసనక వాఁడు రథంబు డిగ్గి, ఖడ్గహస్తుండై,",
        "దవానలంబుపైఁ బడు మిడుతచందంబునం గదిసిన, ఖడ్గకవచంబులు చూర్ణంబులు సేసి, మెరుంగులు",
        "చెదర నడిదంబు వెరికి ఝళిపించి వానిశిరంబుఁ దెగవ్రేయుదు నని గమకించి, నడచుచున్న నడ్డంబు వచ్చి",
        "రుక్మిణీదేవి హరిచరణారవిందంబులు పట్టుకొని యిట్లనియె."], "॥ 1767 ॥", "[Vacanam] At these words the bearer of the mountain smiled. With one arrow he cut his bow; with six shafts he pierced his body through; with eight arrows he felled his horses; with two he killed his charioteer; with three sharp shafts he cut down his banner. When he took another bow he broke it; when he grasped yet another he shattered it; when in turn he took up club, lance, trident, shield, sword, spear and javelin he cut them to pieces; however many weapons he raised again, Hari broke them all to fragments. Still not satisfied, Rukmī got down from his chariot, sword in hand, and rushed at him like a moth falling on a forest fire; Hari ground his sword and armour to powder, drew his own sword and brandished it till it scattered flashes, meaning to cut off his head; and as he moved forward, Rukmiṇī Devī came between them, clasped Hari's lotus feet and said:", prose=True),
    _v([
        "నిన్ను నీశ్వరు దేవదేవుని నిర్ణయింపఁగ లేక యో",
        "సన్నుతామరకీర్తిశోభిత! సర్వలోకశరణ్య! మా",
        "యన్న యీతఁడు నేఁడు చేసె మహాపరాధము నీ యెడన్",
        "నన్ను మన్నన చేసి కావు మనాథనాథ! దయానిధీ!"], "॥ 1768 ॥", "[Mattakōkila] \"Not knowing you as the Lord, the god of gods — you whose fame, praised by the immortals, shines; refuge of all the worlds — this brother of mine has today committed a great offence against you. Have regard for me and spare him, lord of the helpless, treasury of compassion!\""),
    _v([
        "కల్ల లేదని విన్నవించుట గాదు వల్లభ! యీతనిన్",
        "బ్రల్లదుం దెగఁ జూచితేనియు భాగ్యవంతుల మైతి మే",
        "మల్లుఁ డయ్యె ముకుందుఁ డిశ్వరుఁ డంచు మోదితు లైన మా",
        "తల్లిదండ్రులు పుత్త్రశోకముఁ దాల్చి చిక్కుదు రీశ్వరా!"], "॥ 1769 ॥", "[Mattakōkila] \"I do not say this falsely, beloved: if you mean to cut down this braggart, my parents — who rejoiced, 'We are blessed: Mukunda, the Lord, has become our son-in-law' — will be stricken with grief for their son, O Lord!\""),
    _v([
        "అని డగ్గుత్తికతో మహాభయముతో నాకంపితాంగంబుతో",
        "వినతశ్రాంతముఖంబుతో శ్రుతిచలద్వేణీకలాపంబుతోఁ",
        "గనుదోయిన్ జడిగొన్న బాష్పములతోఁ గన్యాలలామంబు మ్రొ",
        "క్కిన రుక్మిం దెగవ్రేయఁ బోక మగిడెన్ గృష్ణుండు రోచిష్ణుఁడై."], "॥ 1770 ॥", "[Mattebham] When the jewel among maidens bowed thus, her throat choking, in great fear, her limbs trembling, her face bent and weary, her braid swinging at her ears, her eyes streaming with tears, Kṛṣṇa, shining in glory, drew back and did not cut Rukmī down."),
    _v([
        "ఇట్లు చంపక బావా! రమ్మని చిరునగవు నగుచు, వానింబట్టి బంధించి గడ్డంబును మీసంబును దలయును",
        "నొకకత్తివాతి యమ్మున రేవులువారఁ గొరిగి, విరూపిం జేసె; నంతట యదువీరులు పరసైన్యంబులం బారఁ",
        "దోలి, తత్సమీపంబునకు వచ్చి; రప్పుడు హతప్రాయుండై కట్టువడి యున్న రుక్మిం జూచి కరుణచేసి, బలభద్రుండు",
        "బంధంబులు విడిచి హరిని డగ్గరి యిట్లనియె."], "॥ 1771 ॥", "[Vacanam] So, not killing him, smiling — \"Come, brother-in-law!\" — he seized him, bound him and with the edge of a sword shaved his beard, moustache and head in patches, leaving him disfigured. Meanwhile the Yadu heroes, having driven off the enemy forces, came near; and Balabhadra, seeing Rukmī lying bound and half dead, took pity, loosed his bonds, went up to Hari and said:", prose=True),
    _v([
        "తల మనక భీష్మనందను, తలయును మూతియును గొరుగఁ దగవే! బంధుం",
        "దలయును మూతియు గొరుగుట, తల దరుగుటకంటె దుచ్ఛతరము మహాత్మా!"], "॥ 1772 ॥", "[Kandam] \"Was it right, heedless, to shave the head and face of Bhīṣmaka's son? For a kinsman, a shaven head and face is a meaner thing than losing the head, great one!\""),
    _v([
        "కొందరు రిపు లని కీడును, గొందరు హితు లంచు మేలు గూర్పవు; నిజ మీ",
        "వందరియందును సముఁడవు, పొందఁగ నేలయ్య! విషమబుద్ధి ననంతా!"], "॥ 1773 ॥", "[Kandam] \"You do not harm some as enemies, nor do good to some as friends; in truth you are the same to all of them. Why then take on this partial mind, Ananta?\""),
    {"heading": "Balabhadra consoles Rukmiṇī, grieving at her brother's humbling"},
    _v([
        "అని వితర్కించి రుక్మిణీదేవి నుపలక్షించి యిట్లనియె."], "॥ 1774 ॥", "[Vacanam] So reasoning, he turned to Rukmiṇī Devī and said:", prose=True),
    _v([
        "తోడంబుట్టిన వానిభంగమునకున్ దుఃఖించి మా కృష్ణు నె",
        "గ్గాడం జూడకు మమ్మ! పూర్వభవకర్మాధీనమై ప్రాణులన్",
        "గీడున్ మేలును జెందు; లేఁ డొకఁడు శిక్షింపంగ రక్షింప నీ",
        "తోడంబుట్టువు కర్మశేషపరిభూతుం డయ్యె నేఁ డియ్యెడన్."], "॥ 1775 ॥", "[Śārdūlam] \"Do not, mother, grieving at your brother's humiliation, look on our Kṛṣṇa as at fault. Bound by the deeds of former births, creatures meet harm and good; no one punishes or protects. Your brother today has been overcome by what remained of his own karma.\""),
    _v([
        "చంపెడి దోషము గలిగినఁ, జంపఁ జనదు బంధుజనులఁ జను విడువంగాఁ",
        "జంపిన దోషము సిద్ధము, చంపను మరి యేల మున్న చచ్చినవానిన్."], "॥ 1776 ॥", "[Kandam] \"Even when there is a fault deserving death, one should not kill one's kin; one should let them go. To kill them is surely a sin; why then kill one who is as good as dead already?\""),
    _v([
        "బ్రహ్మచేత భూమిపతుల కీ ధర్మంబు, కల్పితంబు రాజ్యకాంక్షఁ జేసి",
        "తోడిచూలు నైనఁ దోడఁబుట్టినవాఁడు, చంపుచుండుఁ గ్రూరచరితుఁ డగుచు."], "॥ 1777 ॥", "[Āṭaveladi] \"This is the dharma Brahmā fixed for kings; yet out of lust for a kingdom a man grows cruel and kills even his own brother, born of the same womb.\""),
    _v([
        "భూమికి ధనధాన్యములకు, భామలకును మానములకుఁ బ్రాభవమునకుం",
        "గామించి మీఁదు గానరు, శ్రీమదమున మానధనులు చెనకుదు రొరులన్."], "॥ 1778 ॥", "[Kandam] \"Greedy for land, wealth and grain, for women, honour and power, the proud, blinded by the intoxication of fortune, do not see what lies ahead and fall upon others.\""),
    _v([
        "వినుము. దైవమాయం జేసి దేహాభిమానులైన మానవులకున్ బగవాఁడు, బంధుండు, నుదాసీనుండు",
        "నను మోహంబు సిద్ధంబై యుండు; జలాదులయందుఁ జంద్రసూర్యాదులును, ఘటాదులయందు గగనంబును",
        "బెక్కై కానంబడు భంగి, దేహధారుల కందరికి నాత్మ యొక్కం డయ్యును బెక్కండ్రై తోఁచు; నాద్యంతంబులు",
        "గల యీ దేహంబు ద్రవ్యప్రాణగుణాత్మకంబై, యాత్మయందు నవిద్యచేతఁ గల్పితంబై, దేహిని సంసారంబునం",
        "ద్రిప్పు. సూర్యుండు తటస్థుండై యుండఁ బ్రకాశమానంబు లయిన దృష్టిరూపంబులుంబోలె నాత్మ",
        "తటస్థుండైయుండ దేహేంద్రియంబులు ప్రకాశమానంబు లగు; నాత్మకు వేరొక్కటితోడ సంయోగవియోగంబులు",
        "లేవు; వృద్ధిక్షయంబులు చంద్రకళలకుం గాని చంద్రునికి లేని కైవడి, జన్మనాశంబులు దేహంబునకుఁ గాని,",
        "యాత్మకుఁ గలుగనేరవు. నిద్ర వోయినవాఁ డాత్మను విషయఫలానుభవంబులు సేయించు తెరంగున, నెరుక",
        "లేనివాఁడు నిజము గాని యర్థమునందు ననుభవము నొందుచుండుఁ గావున."], "॥ 1779 ॥", "[Vacanam] \"Listen. Through the Lord's māyā, men who take the body for the self fall into the delusion of 'enemy, kinsman, stranger'. As the moon, the sun and the like appear many in water and the like, and space in pots and the like, so the Self, though one, appears as many to all embodied beings. This body, which has a beginning and an end, made of matter, breath and the guṇas and imagined upon the Self through ignorance, whirls the embodied one in saṃsāra. As forms seen become manifest while the sun stands apart, so the body and the senses become manifest while the Self stands apart. The Self has no union with or separation from anything else; as waxing and waning belong to the moon's digits and not to the moon, so birth and death belong to the body and cannot touch the Self. As a sleeper makes the self live through the fruits of objects in a dream, so one without knowledge lives through things that are not real. Therefore,\"", prose=True),
    _v([
        "అజ్ఞానజ మగు శోకము, విజ్ఞాన విలోకనమున విడువుము నీకుం",
        "బ్రజ్ఞావతికిం దగునే, యజ్ఞానుల భంగి వగవ నంభోజముఖీ!"], "॥ 1780 ॥", "[Kandam] \"give up, with the eye of knowledge, the grief born of ignorance. Is it fitting for you, wise as you are, to grieve like the ignorant, lotus-faced one?\""),
    _v([
        "ఇట్లు బలభద్రునిచేతఁ దెలుపంబడి, రుక్మిణీదేవిదుఃఖంబు మాని యుండె; నట రుక్మి యను వాఁడు",
        "ప్రాణావశిష్టుండై, విడువఁబడి తన విరూపభావంబునకు నెరియుచు, హరిం గెల్చికాని కుండిన పురంబుఁ",
        "జూడ నని ప్రతిజ్ఞ సేసి, తత్సమీపంబున నుండె నివ్విధంబున."], "॥ 1781 ॥", "[Vacanam] Taught thus by Balabhadra, Rukmiṇī Devī put aside her grief. And Rukmī, left with only his life and let go, burning at his disfigurement, vowed that he would not see the city of Kuṇḍina without first defeating Hari, and stayed near that place. In this way,", prose=True),
    _v([
        "రాజీవలోచనుఁడు హరి, రాజసమూహముల గెల్చి రాజస మొప్పన్",
        "రాజిత యగు తన పురికిని, రాజాననఁ దెచ్చె బంధురాజి నుతింపన్."], "॥ 1782 ॥", "[Kandam] Hari, the lotus-eyed, conquered the hosts of kings and, in kingly splendour, brought the moon-faced one to his shining city, as the throng of his kin sang his praise."),
    {"heading": "Kṛṣṇa weds Rukmiṇī"},
    _v([
        "అంత న య్యాదవేంద్రునినగరంబు సమారబ్ధవివాహకృత్యంబును, బ్రవర్తమానగీతవాద్యనృత్యంబును,",
        "బ్రతిగృహాలంకృతవిలసితాశేషనరనారీవర్గంబును, బరిణయమహోత్సవసమాహూయమానమహీపాలగజఘటా",
        "గండమండలదానసలిలధారాసిక్తమార్గంబును, బ్రతిద్వారమంగళాచారసంఘటితక్రముకకదళికాకర్పూర",
        "కుంకుమాగరుధూపదీపపరిపూర్ణకుంభంబును, విభూషితసకలగృహవేదికాకవాటదేహళీస్తంభంబును,",
        "విచిత్రకుసుమాంబరరత్నతోరణవిరాజితంబును, సముద్ధూతకేతనవిభ్రాజితంబును నై యుండె;",
        "న య్యవసరంబున."], "॥ 1783 ॥", "[Vacanam] Then the city of the Yādava lord was in the midst of the wedding rites; songs, music and dances went on; every house was decorated and the men and women in all of them shone; the streets were wet with the streams of rut from the temples of the elephant troops of the kings invited to the wedding festival; at every door, for the auspicious rites, stood full jars with areca, plantain, camphor, saffron, aloe incense and lamps; the platforms, doors, thresholds and pillars of every house were adorned; it was splendid with arches of bright flowers, cloth and gems, and resplendent with banners raised high. At that time —", prose=True),
    _v([
        "ధ్రువకీర్తిన్ హరి పెండ్లి యాడె నిజచేతోహారిణిన్ మాన వై",
        "భవగాంభీర్యవిహారిణిన్ నిఖిలసంపత్కారిణిన్ సాధు బాం",
        "ధవ సత్కారిణిఁ బుణ్యచారిణిఁ మహాదారిద్ర్యసంహారిణిన్",
        "సువిభూషాంబరధారిణిన్ గుణవతీచూడామణిన్ రుక్మిణిన్."], "॥ 1784 ॥", "[Śārdūlam] Hari, of lasting fame, married Rukmiṇī — who stole his heart, who moves in glory, splendour and depth, who brings all prosperity, honours the good and her kin, walks in virtue, destroys great poverty, wears fine ornaments and garments, the crest-jewel of virtuous women."),
    _v([
        "సతులుం దారును బౌరులు, హితమతిఁ గానుకలు దెచ్చి యిచ్చిరి కరుణో",
        "న్నతవర్ధిష్ణులకును మా, నితరోచిష్ణులకు రుక్మిణీకృష్ణులకున్."], "॥ 1785 ॥", "[Kandam] The citizens, women and men, with loving minds, brought gifts and gave them to Rukmiṇī and Kṛṣṇa, ever growing in compassion, radiant with honour."),
    _v([
        "హరి పెండ్లికిఁ గైకేయక, కురు సృంజయ యదు విదర్భ కుంతినరేంద్రుల్",
        "వరమానందముఁ బొందిరి, ధరణీశులలోన గాఢతాత్పర్యములన్."], "॥ 1786 ॥", "[Kandam] At Hari's wedding the kings of Kekaya, Kuru, Sṛñjaya, Yadu, Vidarbha and Kunti, among the rulers of the earth, attained the highest joy, with deep devotion."),
    _v([
        "హరి యీ తెరఁగున రుక్మిణి, నరుదుగఁ గొనితెచ్చి పెండ్లి యాడుట విని దు",
        "ష్కరకృత్య మనుచు వెరఁగం, దిరి రాజులు రాజసుతులు దిక్కుల నెల్లన్."], "॥ 1787 ॥", "[Kandam] Hearing that Hari had carried off Rukmiṇī in this way and married her, kings and princes in every quarter marvelled, calling it a deed hard to do."),
    _v([
        "అనఘ! యాదిలక్ష్మి యైన రుక్మిణతోడఁ, గ్రీడ సలుపుచున్న కృష్ణుఁ జూచి",
        "పట్టణంబులోని ప్రజ లుల్లసిల్లిరి, ప్రీతు లగుచు ముక్తభీతు లగుచు."], "॥ 1788 ॥", "[Āṭaveladi] O sinless one, seeing Kṛṣṇa at play with Rukmiṇī, who is the primal Lakṣmī, the people of the city rejoiced, delighted and free from fear."),
    _v([
        "అని చెప్పి."], "॥ 1789 ॥", "[Vacanam] Having told this (Śuka concluded).", prose=True),
    _v([
        "కువలయరక్షాతత్పర, కువలయదళనీలవర్ణకోమలదేహా!",
        "కువలయనాథశిరోమణి!, కువలయజనవినుతవిమలగుణసంఘాతా!"], "॥ 1790 ॥", "[Kandam] (The poet's closing address, playing on kuvalaya, \"earth\" and \"blue water-lily\":) O you intent on protecting the earth; you whose tender body is dark as a blue water-lily petal; crest-jewel of the lords of the earth; you whose pure virtues are praised by the people of the earth!"),
    _v([
        "సరసిజనిభహస్తా! సర్వలోకప్రశస్తా!",
        "నిరుపమశుభమూర్తీ! నిర్మలారూఢకీర్తీ!",
        "పరహృదయవిదారీ! భక్తలోకోపకారీ!",
        "గురుబుధజనపోషీ! ఘోరదైతేయశోషీ!"], "॥ 1791 ॥", "[Mālinī] O you whose hands are like lotuses, praised by all the worlds; of peerless auspicious form, of spotless, exalted fame; who rend the hearts of enemies, benefactor of devotees; who nourish the elders and the wise, who dry up the terrible Daityas!"),
    _v([
        "ఇది శ్రీపరమేశ్వరకరుణాకలితకవితావిచిత్రకేసనమంత్రిపుత్త్రసహజపాండిత్యపోతనామాత్య ప్రణీతంబయిన",
        "శ్రీమహాభాగవతంబను మహాపురాణమునందు దేవకీదేవివివాహంబును, గగనవాణీశ్రవణంబును,",
        "కంసోద్రేకంబును, వసుదేవ ప్రార్థనంబును, యోగమాయాప్రభావంబును, బలభద్రుని జన్మంబును,",
        "బ్రహ్మాదిసురస్తోత్రంబును, కృష్ణావతారంబును, ఘోషప్రవేశంబును, యోగనిద్రాచరితంబును,",
        "నందపుత్త్రోత్సవంబును, పూతనాసంహారంబును, శకట భంజనంబును, తృణావర్తుమరణంబును,",
        "గర్గాగమనంబును, నారాయణాదినామనిర్దేశంబును, బాలక్రీడయును, మృద్భక్షణంబును,",
        "వాసుదేవవదనగహ్వరవిలోక్యమానాఖిలలోకాలోకనంబును, నవనీతచౌర్యంబును, యశోదారోషంబును,",
        "ఉలూఖలబంధనంబును, అర్జునతరుయుగళనిపాతనంబును, నలకూబరమణిగ్రీవులశాపమోక్షణంబును,",
        "బృందావనగమనంబును, వత్సపాలనంబును, వత్సాసురవధయును, బకదనుజవిదారణంబును,",
        "అఘాసురమరణంబును, వత్సాపహరణంబును, నూతనవత్సబాలకకల్పనంబును, బ్రహ్మవినుతియును,",
        "గోపాలనంబును, గార్దభాసురదమనంబును, కాళియఫణి మర్దనంబును, గరుడకాళియనాగవిరోధకథనంబును,",
        "ప్రలంబాసురహింసనంబును, దవానల పానంబును, వర్షర్తువర్ణనంబును, శరత్కాలలక్షణంబును,",
        "వేణువిలాసంబును, హేమంతసమయ సమాగమంబును, గోపకన్యాచరితహవిష్యవ్రతంబును,",
        "కాత్యాయనీసేవనంబును, వల్లనీ వస్త్రావహరణంబును, విప్రవనితాదత్తాన్నభోజనంబును,",
        "ఇంద్రయాగనివారణంబును, నందముకుంద సంవాదంబును, పర్వతభంజనంబును, పాషాణసలిలవర్షంబును,",
        "గోవర్ధనోద్ధరణంబును, వరుణకింకరుండు నందునిం గొనిపోయినహరి దెచ్చుటయు, వేణుపూరణంబును,",
        "గోపికాజనఘోషనిర్గమంబును, యమునాతీరవనవిహరణంబును, కృష్ణాంతర్థానంబును,",
        "ఘోషకామినీగణపరిదేవనంబును, గోపికాన్వేషణంబును, గోపికాగీతలును, హరిప్రసన్నతయును,",
        "రాసక్రీడనంబును, జలకేళియును, సర్పరూపకుం డయిన సుదర్శనవిద్యాధరుండు హరిచరణతాడనంబున",
        "నిజరూపంబు వడయుటయును, శంఖచూడుండనుగుహ్యకుని వధించుటయును, వృషభాసురవిదళనంబును,",
        "నారదోపదేశంబున హరిజన్మకథ నెరిఁగి కంసుండు దేవకీవసుదేవుల బద్ధులం జేయుటయును, ఘోటకాసురుం",
        "డయిన కేశి యను దనుజుని వధించుటయును, నారదస్తుతియును, వ్యోమదానవమరణంబును,",
        "అక్రూరాగమనంబును, అక్రూరరామకృష్ణులసల్లాపంబును, ఘోషనిర్గమంబును, యమునాజలాంతరాళంబున",
        "నక్రూరుండు హరివిశ్వరూపమును గాంచుటయును, అక్రూరస్తవంబును, మథురానగరప్రవేశంబును,",
        "రజకవధయును, వాయకమాలికులచే సమ్మానమొందుటయును, కుబ్జాప్రసాదకరణంబును, ధనుర్భంగంబును,",
        "కంసుదుస్స్వప్నంబును, కువలయాపీడపీడనంబును, రంగస్థలప్రవేశంబును, చాణూరముష్టికుల వధయును,",
        "కంసవధయును, వసుదేవదేవకీబంధమోక్షణంబును, ఉగ్రసేనురాజ్యస్థాపనంబును, రామకృష్ణులు సాందీపనివలన",
        "విద్య లభ్యసించుటయును, సంయమనీనగరగమనంబును, గురుపుత్త్రదానంబును, ఉద్ధవునిఘోషయాత్రయును,",
        "భ్రమరగీతలును, కుబ్జావాసగమనంబును, కరినగరంబునకు నక్రూరుండు సని కుంతీదేవి నూరార్చుటయు,",
        "కంసభార్యలగు నస్తి ప్రాస్తులు జరాసంధునకుఁ గంసుమరణం బెరింగించుటయును, జరాసంధుని",
        "దండయాత్రయును, మథురానగరనిరోధనంబును, యుద్ధంబున జరాసంధుండు సప్తదశవారంబులు పలాయితుం",
        "డగుటయు, నారదప్రేరితుండై కాలయవనుండు మథురపై దాడి వెడలుటయును, ద్వారకానగరనిర్మాణంబును,",
        "మథురాపురనివాసులం దనయోగబలంబున హరి ద్వారకానగరంబునకుఁ దెచ్చుటయు, కాలయవనుండు",
        "హరివెంటం జని గిరిగుహయందు నిద్రితుండైన ముచుకుందునికోపదృష్టివలన నీరగుటయును, ముచుకుందుండు",
        "హరిని సంస్తుతి చేసి తపంబునకుం జనుటయును, జరాసంధుఁడు గ్రమ్మర రామకృష్ణులపై నేతెంచుటయును,",
        "ప్రవర్షణపర్వతారోహణంబును, గిరిదహనంబును, గిరి డిగ్గ నురికి రామకృష్ణులు ద్వారకకుం జనుటయు,",
        "రుక్మిణీజన్మంబును, రుక్మిణీ సందేశంబును, వాసుదేవాగమనంబును, రుక్మిణీగ్రహణంబును,",
        "రాజలోకపలాయనంబును, రుక్మి యనువాని భంగంబును, రుక్మిణీకల్యాణంబును ననుకథలు గల",
        "దశమస్కంధంబునందుఁ బూర్వభాగంబు సంపూర్ణము."], "॥ 1792 ॥", "[Gadyam] Thus, in the Śrī Mahābhāgavatam, the great Purāṇa composed by Pōtanāmātya — son of the minister Kesana, whose poetry is wonderful through the grace of the Supreme Lord, whose learning was inborn — ends the first part of the tenth skandha, which holds the tales of Devakī's marriage, the voice from the sky, Kaṃsa's frenzy, and the rest of Kṛṣṇa's childhood and youth, down to the birth of Rukmiṇī, her message, Vāsudeva's coming, the taking of Rukmiṇī, the flight of the kings, the humbling of Rukmī and Rukmiṇī's wedding.", prose=True),
    ],
}
