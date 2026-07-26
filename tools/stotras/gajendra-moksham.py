# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE work (src="tel"): Telugu is the source, IAST a reading aid,
# no Devanāgarī. Telugu from Telugu Wikisource (public domain); the yati/prāsa
# markup and the page's word-gloss and Telugu paraphrase are not used.
# Translation original. Gajendra Mokṣam — Bammera Pōtana's rendering, in the
# Telugu Bhāgavatam (8th skandha), of the elephant-king's surrender (padyams
# 8-73…8-77, the famous "evvanicē janiñcu jagamu" sequence). See SOURCES §6.3.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "vishnu",
    "doc_title": "Gajendra Mokṣam",
    "app_title": "Gajendra Mokṣam",
    "h1": "Gajendra Mokṣam",
    "subtitle": "Pōtana · the elephant-king's surrender",
    "note": "Telugu-language padyams of Bammera Pōtana, from his Telugu "
            "Bhāgavatam (8th skandha): Gajendra, seized by the crocodile, gives "
            "up all else and appeals to the Supreme. The Telugu is the source; "
            "the IAST is a reading aid.",
    "footer": "Source: Telugu Wikisource — పోతన తెలుగు భాగవతము, అష్టమ స్కంధము (public domain)",
    "sections": [
        _v(["ఎవ్వనిచే జనించు జగ; మెవ్వని లోపల నుండు లీనమై;",
            "యెవ్వని యందు డిందుఁ; బరమేశ్వరుఁ డెవ్వఁడు; మూలకారణం",
            "బెవ్వఁ; డనాదిమధ్యలయుఁ డెవ్వఁడు; సర్వముఁ దానయైన వాఁ",
            "డెవ్వఁడు; వాని నాత్మభవు నీశ్వరు నే శరణంబు వేడెదన్."],
           "By whom this world is born; within whom it abides, dissolved; into "
           "whom it sinks again; who is the Supreme Lord; who is the root "
           "cause; who is without beginning, middle, or end; who has himself "
           "become all — that self-existent Lord I beg for refuge."),
        _v(["ఒకపరి జగములు వెలి నిడి",
            "యొకపరి లోపలికిఁ గొనుచు నుభయముఁ దానై",
            "సకలార్థ సాక్షి యగు న",
            "య్యకలంకుని నాత్మమూలు నర్థిఁ దలంతున్."],
           "Who at one moment sets the worlds forth (creating them), at another "
           "draws them within, being both himself — that stainless one, witness "
           "of all things, the very root of the Self — Him I meditate on with "
           "longing."),
        _v(["లోకంబులు లోకేశులు",
            "లోకస్థులుఁ దెగినఁ దుది నలోకం బగు పెం",
            "జీకటి కవ్వల నెవ్వం",
            "డేకాకృతి వెలుఁగు నతని నే సేవింతున్."],
           "When the worlds, the world-rulers, and the world-dwellers are all "
           "destroyed — beyond the vast blind darkness that is then the "
           "world-less end — whoever shines there in one undivided form, Him I "
           "serve."),
        _v(["నర్తకుని భంగిఁ బెక్కగు",
            "మూర్తులతో నెవ్వఁ డాడు? మునులు దివిజులుం",
            "గీర్తింప నేర? రెవ్వని",
            "వర్తన మొరు లెఱుఁగ? రట్టివాని నుతింతున్."],
           "Who, like a dancer, plays in many forms; whom the sages and the "
           "gods cannot fully praise; whose ways others do not know — that One "
           "I extol."),
        _v(["ముక్తసంగులైన మునులు దిదృక్షులు",
            "సర్వభూత హితులు సాధుచిత్తు",
            "లసదృశవ్రతాఢ్యులై కొల్తు రెవ్వని",
            "దివ్యపదము వాఁడు దిక్కు నాకు."],
           "The sages freed from all attachment, longing to behold Him, "
           "well-wishers of every creature, pure of heart, rich in matchless "
           "vows — whose divine feet they worship: that One is my refuge."),
    ],
}
