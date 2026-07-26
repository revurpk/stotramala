# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE kīrtana (src="tel"). Telugu from Telugu Wikisource (public
# domain; the pallavi/charaṇa markers and romanized copy are not used).
# Translation original. Koṇḍalalō Nelakonna — Annamācārya's kīrtana on
# Veṅkaṭeśvara of the seven hills. See SOURCES §6.7.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "venkateshwara",
    "doc_title": "Koṇḍalalō Nelakonna",
    "app_title": "Koṇḍalalō Nelakonna",
    "h1": "Koṇḍalalō Nelakonna",
    "subtitle": "Annamayya · Veṅkaṭeśvara of the hills",
    "note": "A Telugu-language kīrtana of Annamācārya (rāgam Hindōḷam). The "
            "charaṇas recall the Lord's grace to his legendary devotees — "
            "Kuruvaratinambi, Toṇḍamān, Anantāḻvār, Tirumalanambi, "
            "Tirukkacchinambi. The Telugu is the source; the IAST is a reading "
            "aid, and the devotee-legends are rendered by their traditional "
            "sense.",
    "footer": "Source: Telugu Wikisource — కొండలలో నెలకొన్న (public domain)",
    "sections": [
        _v(["కొండలలో నెలకొన్న కోనేటి రాయడు వాడు",
            "కొండలంత వరములు గుప్పెడువాడు"],
           "He is the Lord of the temple-tank who has settled among the hills — "
           "he who lavishes boons as vast as the hills themselves."),
        _v(["కుమ్మర దాసుడైన కురువరతినంబి",
            "యిమ్మన్న వరములెల్ల నిచ్చినవాడు",
            "దొమ్ములు సేసినయట్టి తొండమాం చక్కురవర్తి",
            "రమ్మన్న చోటికి వచ్చి నమ్మినవాడు"],
           "He who granted every boon that Kuruvaratinambi, the potter-devotee, "
           "asked of him; he who, when the war-waging Toṇḍamān Cakravartī "
           "called, came to the very place he was bidden and won his trust."),
        _v(["అచ్చపు వేడుకతో ననంతాళువారికి",
            "ముచ్చిలి వెట్టికి మన్ను మోచినవాడు",
            "మచ్చిక దొలక దిరుమలనంబి తోడుత",
            "నిచ్చనిచ్చ మాటలాడి నొచ్చినవాడు"],
           "He who, in pure delight, carried earth as a hidden bond-servant for "
           "Anantāḻvār; he who, affection overflowing, conversed day after day "
           "with Tirumalanambi — and (in that loving nearness) even bore hurt."),
        _v(["కంచిలోన నుండ దిరుకచ్చినంబి మీద",
            "కరుణించి తనయెడకు రప్పించిన వాడు",
            "ఎంచి యెక్కుడైన వేంకటేశుడు మనలకు",
            "మంచివాడై కరుణ బాలించినవాడు"],
           "He who took pity on Tirukkacchinambi, dwelling in Kāñci, and had him "
           "brought to his own side; that Veṅkaṭeśa, exalted beyond all "
           "reckoning, who — being good to us — has cherished us with "
           "compassion."),
    ],
}
