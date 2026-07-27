# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE kīrtana (src="tel"). Telugu from Telugu Wikisource (public
# domain). Translation original. Nānāṭi Batuku Nāṭakamu — Annamācārya's
# philosophical kīrtana: everyday life is a play, and the unseen Reality is
# liberation. See SOURCES §6.10.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "venkateshwara",
    "doc_title": "Nānāṭi Batuku Nāṭakamu",
    "app_title": "Nānāṭi Batuku",
    "h1": "Nānāṭi Batuku Nāṭakamu",
    "subtitle": "Annamayya · everyday life is a play",
    "note": "A philosophical kīrtana of Annamācārya: the daily round is a "
            "passing drama, and the Reality glimpsed beyond it is liberation "
            "(kaivalya). The Telugu is the source; the IAST is a reading aid.",
    "footer": "Source: Telugu Wikisource — నానాటి బదుకు నాటకము (public domain)",
    "sections": [
        _v(["నానాటి బతుకు నాటకము",
            "కానక కన్నది కైవల్యము"],
           "This day-to-day life is a play; what is beheld beyond ordinary "
           "seeing — that is liberation."),
        _v(["పుట్టుటయు నిజము పోవుటయు నిజము",
            "నట్టనడిమి పని నాటకము",
            "యెట్ట నెదుట గల దీ ప్రపంచము",
            "కట్ట గడపటిది కైవల్యము"],
           "Being born is real, and dying is real; all the doing in between is "
           "the play. This world that stands plainly before our eyes — the very "
           "last thing, beyond it all, is liberation."),
        _v(["కుడిచే దన్నము కోక చుట్టెడిది",
            "నడ మంత్రపు పని నాటకము",
            "వొడి గట్టుకొనిన వుభయ కర్మములు",
            "గడి దాటినపుడె కైవల్యము"],
           "The food one eats, the cloth one wraps about oneself — this middling "
           "business is the play. The two kinds of karma (good and bad) one "
           "gathers into one's lap — only when one steps across their boundary "
           "is there liberation."),
        _v(["తెగదు పాపము తీరదు పుణ్యము",
            "నగి నగి కాలము నాటకము",
            "యెగువనె శ్రీ వేంకటేశ్వరుడేలిక",
            "గగనము మీదిది కైవల్యము"],
           "Sin is never cut off, merit is never used up; laughing and laughing, "
           "all this time is the play. High above, Śrī Veṅkaṭeśvara is the Lord; "
           "and that which lies beyond the sky is liberation."),
    ],
}
