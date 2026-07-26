# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE work: the Telugu is the source of truth (src="tel"); the
# page offers Telugu + an IAST pronunciation aid (no Devanāgarī). Telugu from
# Telugu Wikisource (public domain); translation original. Adivo Alladivo —
# a kīrtana of Annamācārya (Annamayya) on Veṅkaṭeśvara. See SOURCES §6.1.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "venkateshwara",
    "doc_title": "Adivo Alladivo",
    "app_title": "Adivo Alladivo",
    "h1": "Adivo Alladivo",
    "subtitle": "Annamayya · a kīrtana on Veṅkaṭeśvara",
    "note": "A Telugu-language kīrtana of Annamācārya. The Telugu is the source; "
            "the IAST is a reading aid for pronunciation. (rāgam Madhyamāvati, "
            "tāḷam Ādi.)",
    "footer": "Source: Telugu Wikisource — అదివో అల్లదివో (public domain)",
    "sections": [
        _v(["అదివో అల్లదివో శ్రీహరివాసము",
            "పదివేల శేషుల పడగలమయము ॥"],
           "There it is, there yonder — the abode of Śrī Hari! It is the mass "
           "of the raised hoods of ten thousand serpents (the hill is Ādiśeṣa "
           "himself)."),
        "ornament",
        _v(["అదె వేంకటాచల మఖిలోన్నతము",
            "అదివో బ్రహ్మాదుల కపురూపము",
            "అదివో నిత్యనివాస మఖిలమునులకు",
            "అదె చూడుడదె మ్రొక్కుడానందమయము ॥"],
           "There is Veṅkaṭācala, highest of all; there yonder, the very form "
           "of Brahmā and the gods; there, the eternal dwelling for all sages; "
           "behold it, bow to it — it is full of bliss."),
        _v(["చెంగట నల్లదివో శేషాచలము",
            "నింగి నున్నదేవతల నిజవాసము",
            "ముంగిట నల్లదివో మూలనున్నధనము",
            "బంగారు శిఖరాల బహు బ్రహ్మమయము ॥"],
           "Close by, there yonder is Śeṣācala, the true dwelling of the gods "
           "who abide in the sky; right in front, there yonder is the treasure "
           "that lies at the very foundation; with its golden peaks it is one "
           "great mass of Brahman."),
        _v(["కైవల్యపదము వేంకటనగమదివో",
            "శ్రీ వేంకటపతికి సిరులైనవి",
            "భావింప సకలసంపదరూపమదివో",
            "పావనములకెల్ల పావనమయము ॥"],
           "The very state of liberation is this Veṅkaṭa hill, there yonder; "
           "all these have become the riches of the Lord of Veṅkaṭa; when you "
           "contemplate it, it is the form of all abundance — the holiest of "
           "all holy things."),
    ],
}
