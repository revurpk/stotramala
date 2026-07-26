# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE kīrtana (src="tel"). Telugu from Telugu Wikisource (public
# domain; the pallavi/charaṇa markers ప|| చ|| and the romanized copy are not
# used). Translation original. Brahma Kaḍigina Pādamu — Annamācārya's kīrtana
# on the feet of Veṅkaṭeśvara. See SOURCES §6.6.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "venkateshwara",
    "doc_title": "Brahma Kaḍigina Pādamu",
    "app_title": "Brahma Kaḍigina Pādamu",
    "h1": "Brahma Kaḍigina Pādamu",
    "subtitle": "Annamayya · on the feet of Veṅkaṭeśvara",
    "note": "A Telugu-language kīrtana of Annamācārya — a garland of praise to "
            "the Lord's foot, each line naming one of its deeds. The Telugu is "
            "the source; the IAST is a reading aid.",
    "footer": "Source: Telugu Wikisource — బ్రహ్మకడిగిన పాదము (public domain)",
    "sections": [
        _v(["బ్రహ్మకడిగిన పాదము",
            "బ్రహ్మము దానె నీ పాదము"],
           "The foot that Brahmā (once) washed; that very foot is Brahman "
           "itself — your foot."),
        _v(["చెలగి వసుధ గొలిచిన నీ పాదము",
            "బలితల మోపిన పాదము",
            "తలకక గగనము తన్నిన పాదము",
            "బలరిపు గాచిన పాదము"],
           "The foot that gladly measured the earth; the foot set upon Bali's "
           "head; the foot that, undaunted, spurned the very sky (as "
           "Trivikrama); the foot that guarded Indra, the foe of the demons."),
        _v(["కామిని పాపము కడిగిన పాదము",
            "పాముతల నిడిన పాదము",
            "ప్రేమకు శ్రీసతి పిసికెడి పాదము",
            "పామిడి తురగపు పాదము"],
           "The foot that washed away the woman's sin (Ahalyā's); the foot set "
           "upon the serpent's head (Kāliya's); the foot that Śrī, the beloved "
           "consort, lovingly presses; the foot swift as a coursing steed."),
        _v(["పరమ యోగులకు పరి పరి విధముల",
            "వర మొసగెడి నీ పాదము",
            "తిరు వేంకటగిరి తిరమని చూపిన",
            "పరమ పదము నీ పాదము"],
           "The foot that grants boons in ways beyond counting to the highest "
           "yogis; the foot that, showing itself firm-set on holy Veṅkaṭa hill, "
           "is the supreme abode — your foot."),
    ],
}
