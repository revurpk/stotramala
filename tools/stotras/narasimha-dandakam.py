# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE daṇḍaka (src="tel"). Telugu from Telugu Wikisource (public
# domain); translation original. Narasiṃha Daṇḍakam — a folk-devotional hymn
# to Narasiṃha weaving in praise of the name of Rāma. See SOURCES §6.5.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "vishnu",
    "doc_title": "Narasiṃha Daṇḍakam",
    "app_title": "Narasiṃha Daṇḍakam",
    "h1": "Narasiṃha Daṇḍakam",
    "subtitle": "A daṇḍaka to Narasiṃha",
    "note": "A folk-devotional Telugu daṇḍaka to Narasiṃha, praising the name of "
            "Rāma. The Telugu is the source; the IAST is a reading aid. A few "
            "colloquial phrases are obscure and are rendered by their apparent "
            "sense.",
    "footer": "Source: Telugu Wikisource — నరసింహ దండకము (public domain)",
    "sections": [
        _v(["శ్రీ హరి పతి నిన్ను - వేడితి నరశింహా",
            "నరుడా గురుడా - నివే నమ్మితి నరశింహా",
            "చీమల వరదా - చిత్తజీవుడా",
            "భావజ వరదా - భక్త వత్సలా!"],
           "O Lord Śrī Hari, I beseech you, Narasiṃha! O Man-lion, O teacher — "
           "in you alone I trust, Narasiṃha! O boon-giver even to the ants, O "
           "life of the heart; O boon-giver to Love (the mind-born), O tender "
           "to your devotees!"),
        _v(["గండ్రగొడ్డలి గల రాజులనెల్లా",
            "ఖండింతురు యమదూతలవల్లా",
            "గాలి ఇతడు ధూళి ఇతడు",
            "ఓనంబితడు, కైనంబితడు!"],
           "All the mighty axe-wielding kings — Yama's messengers cut them down "
           "in the end. Yet he is the wind, he is the dust (he is everywhere); "
           "he is the sacred syllable, he is our one recourse."),
        _v(["అంది పొంది నేర్చిన ఆది నారాయణమూర్తి ఇతండు",
            "ఇతండు అనగా నెవ్వరు గోళజంబు నరశింహా భళా నరశింహా",
            "నరశింహా నామములు ఎవరు తలుతురో",
            "నామీద భక్తితో ఎవరు ఉందురో!"],
           "This is the primordial Nārāyaṇa-form, won by long striving; who can "
           "say who he truly is? — Narasiṃha, bravo Narasiṃha! Whoever calls to "
           "mind the names of Narasiṃha, whoever abides in devotion to me…"),
        _v(["చింతామణి రామనామం",
            "కల్పవృక్షం రామనామం",
            "కామధేనువు రామనామం",
            "సకలం సంపూర్ణం రామనామం!"],
           "The name of Rāma is the wish-granting gem; the name of Rāma is the "
           "wish-fulfilling tree; the name of Rāma is the wish-granting cow; the "
           "name of Rāma is all, whole and complete!"),
        _v(["పడుకొని పఠన చేస్తే పసిబాలలకెల్లా రక్ష",
            "కూర్చొని పఠన చేస్తే గృహములకెల్లా రక్ష",
            "ప్రాతః కాల పఠన చేస్తే మహాపాపములు తొలుగును",
            "మధ్యన వేళ పఠన చేస్తే మహాపాతకములు బాసును!"],
           "Recited lying down, it guards all the little children; recited "
           "seated, it guards all the households; recited at dawn, great sins "
           "depart; recited at midday, grievous transgressions flee!"),
        _v(["సంధ్య వేళ పఠన చేస్తే శ్రీ మహాలక్ష్మి ఎదురుగుండా వచ్చును",
            "అర్ధరాత్రి పఠన చేస్తే చొరభయంలేదు",
            "అహొ వీర్యం",
            "అహొ బాహు పరాక్రమం!"],
           "Recited at twilight, Śrī Mahālakṣmī herself comes forth to meet "
           "one; recited at midnight, there is no fear of thieves. O his valour! "
           "O the might of his arms!"),
        _v(["శ్రీ నారశింహోనకు వైకుంఠ వాసునకి",
            "ఉక్కు స్తంభమున ఊర్హిన ఊర్హునకు",
            "వైకుంఠ వాసునకు వందితునకు",
            "జయ మంగళం నిత్య శుభమంగళం!"],
           "To Śrī Narasiṃha, dweller in Vaikuṇṭha; to him who burst forth from "
           "the iron pillar; to the Vaikuṇṭha-dweller, the adored one — victory "
           "and blessing, ever-auspicious weal!"),
        _v(["ఆకు మీదా ఉన్న ఆరామచంద్రునకు",
            "వైకుంఠ వాసునకు వందితునకు",
            "జయ మంగళం నిత్య శుభమంగళం",
            "ఓం శాంతిః శాంతిః శాంతిః"],
           "To the fair Rāmacandra who rests upon the (banyan) leaf; to the "
           "Vaikuṇṭha-dweller, the adored one — victory and blessing, "
           "ever-auspicious weal! Oṃ, peace, peace, peace."),
    ],
}
