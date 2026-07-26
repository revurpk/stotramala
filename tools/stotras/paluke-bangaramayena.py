# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE work (src="tel"): Telugu is the source, IAST a reading aid,
# no Devanāgarī. Telugu from Telugu Wikisource (public domain, {{PD-old}});
# translation original. Paluke Bangāramāyenā — a kīrtana of Bhadrācala
# Rāmadāsu (Kañcarla Gōpanna, 17th c.) to Rāma. See SOURCES §6.2.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "rama",
    "doc_title": "Paluke Bangāramāyenā",
    "app_title": "Paluke Bangāramāyenā",
    "h1": "Paluke Bangāramāyenā",
    "subtitle": "Bhadrācala Rāmadāsu · a kīrtana on Rāma",
    "note": "A Telugu-language kīrtana of Bhadrācala Rāmadāsu. The Telugu is the "
            "source; the IAST is a reading aid for pronunciation. The pallavi is "
            "the refrain, returned to after each caraṇa. (rāgam Ānandabhairavi, "
            "tāḷam Ādi.)",
    "footer": "Source: Telugu Wikisource — పలుకే బంగారమాయెనా (public domain)",
    "sections": [
        _v(["పలుకే బంగారమాయెనా కోదండపాణి"],
           "Has your very speech turned to gold, O Kodaṇḍapāṇi (Rāma, wielder of "
           "the Kodaṇḍa bow)? — that you have grown so silent."),
        "ornament",
        _v(["పలుకే బంగారమాయె పిలిచిన పలుకవేమి",
            "కలలో నీ నామస్మరణ మరువ చక్కని తండ్రి"],
           "Your speech has become gold — why do you not answer, though I call? "
           "O handsome Father, I who never forget the remembrance of your name "
           "even in my dreams."),
        _v(["ఇరువుగ ఇసుకలోన పొరలిన యుడుత భక్తికి",
            "కరుణించి బ్రోచితివని నెర నమ్మితిని తండ్రి"],
           "I firmly trusted, O Father, that out of compassion you rewarded the "
           "devotion of the little squirrel that rolled snugly in the sand (as "
           "it helped build the bridge to Laṅkā)."),
        _v(["రాతి నాతిగజేసి భూతలమందున ప్రఖ్యాతి",
            "జెందితివని ప్రీతితో నమ్మితి తండ్రి"],
           "I lovingly trusted, O Father, that you turned a stone into a woman "
           "(Ahalyā) and won great renown upon this earth."),
        _v(["ఎంత వేడినను నీకు సుంతైన దయరాదు",
            "పంతము చేయ నేనెంతవాడను తండ్రి"],
           "However much I plead, not the least mercy stirs in you; and what am "
           "I, O Father, to press you with a stubborn demand?"),
        _v(["శరణాగత త్రాణ బిరుదాంకితుడవుగావా",
            "కరుణించు భద్రాచల వర రామదాస పోష"],
           "Are you not adorned with the very title, ‘protector of those who "
           "take refuge’? Then be gracious, O cherisher of Rāmadāsa of "
           "Bhadrācala, O excellent Rāma."),
    ],
}
