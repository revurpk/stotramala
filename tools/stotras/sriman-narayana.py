# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE kīrtana (src="tel"), mostly Sanskrit vocatives. Telugu from
# Telugu Wikisource (public domain; the ప|| చ|| markers not used). Translation
# original. Śrīman Nārāyaṇa — Annamācārya's surrender at the Lord's feet, on a
# garland of lotus-epithets. See SOURCES §6.9.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "venkateshwara",
    "doc_title": "Śrīman Nārāyaṇa",
    "app_title": "Śrīman Nārāyaṇa",
    "h1": "Śrīman Nārāyaṇa",
    "subtitle": "Annamayya · your feet alone are my refuge",
    "note": "A kīrtana of Annamācārya, its epithets a play on kamala, "
            "‘lotus’. The text is mostly Sanskrit in Telugu script; the Telugu "
            "is the source and the IAST a reading aid.",
    "footer": "Source: Telugu Wikisource — శ్రీమన్నారాయణ (public domain)",
    "sections": [
        _v(["శ్రీమన్నారాయణ శ్రీమన్నారాయణ",
            "శ్రీమన్నారాయణ నీ శ్రీపాదమే శరణు"],
           "Śrīman Nārāyaṇa, Śrīman Nārāyaṇa, Śrīman Nārāyaṇa — your holy feet "
           "alone are my refuge."),
        _v(["కమలాసతీ ముఖకమల కమలహిత",
            "కమలప్రియ కమలేక్షణ",
            "కమలాసనహిత గరుడగమన శ్రీ",
            "కమలనాభ నీపదకమలమే శరణు"],
           "O sun to the lotus-face of Kamalā your consort; O beloved of the "
           "Lotus-lady, O lotus-eyed; O friend of the lotus-seated Brahmā, O "
           "rider of Garuḍa; O lotus-naveled Padmanābha — your lotus feet alone "
           "are my refuge."),
        _v(["పరమయోగిజన భాగధేయ శ్రీ",
            "పరమపూరుష పరాత్పర",
            "పరమాత్మ పరమాణురూప శ్రీ",
            "తిరువేంకటగిరి దేవ శరణు"],
           "O very fortune of the highest yogis; O supreme Person, higher than "
           "the highest; O supreme Self, subtle as the finest atom; O God of "
           "holy Veṅkaṭa hill — you are my refuge."),
    ],
}
