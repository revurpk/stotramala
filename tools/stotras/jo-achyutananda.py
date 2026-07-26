# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Telugu-LANGUAGE kīrtana (src="tel"). Telugu from Telugu Wikisource (public
# domain; romanized copy not used). Translation original. Jo Achyutānanda —
# Annamācārya's cradle-song (jōla) to the child Kṛṣṇa. See SOURCES §6.8.

def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}


STOTRA = {
    "src": "tel",
    "deity": "venkateshwara",
    "doc_title": "Jo Achyutānanda",
    "app_title": "Jo Achyutānanda",
    "h1": "Jo Achyutānanda",
    "subtitle": "Annamayya · a cradle-song to the child Kṛṣṇa",
    "note": "A Telugu-language lullaby (jōla) of Annamācārya (rāgam Navarōju) "
            "to the infant Kṛṣṇa. The Telugu is the source; the IAST is a "
            "reading aid.",
    "footer": "Source: Telugu Wikisource — జో అచ్యుతానంద జోజో ముకుంద (public domain)",
    "sections": [
        _v(["జోఅచ్యుతానంద జోజో ముకుంద",
            "రావె పరమానంద రామ గోవింద"],
           "Sleep, Acyutānanda; hush, jo-jo, Mukunda! Come, O supreme bliss, "
           "Rāma, Govinda!"),
        _v(["నందు నింటను జేరి నయము మీఱంగ",
            "చంద్రవదనలు నీకు సేవ చేయంగ",
            "నందముగ వారిండ్ల నాడుచుండంగ",
            "మందలకు దొంగ మా ముద్దురంగ"],
           "Come home to Nanda's house, tenderness overflowing, while the "
           "moon-faced women wait upon you and you play charmingly through "
           "their courtyards — O little thief of the cattle-folds, our darling "
           "Raṅga!"),
        _v(["పాలవారాశిలో పవళించినావు",
            "బాలుగా మునుల కభయమిచ్చినావు",
            "మేలుగా వసుదేవు కుదయించినావు",
            "బాలుడై యుండి గోపాలుడైనావు"],
           "You reclined upon the ocean of milk; as a child you granted "
           "fearlessness to the sages; auspiciously you were born to Vasudeva; "
           "and, though but a child, you became the cowherd Gopāla."),
        _v(["అంగజుని గన్న మా యన్న యిటు రారా",
            "బంగారు గిన్నెలో పాలు పోసేరా",
            "దొంగ నీవని సతులు గొంకుచున్నారా",
            "ముంగిట నాడరా మోహనాకార"],
           "O elder brother who fathered the Love-god, come here! They have "
           "poured milk in a golden bowl; the women hold back, calling you a "
           "thief — come play in the front yard, O one of enchanting form!"),
        _v(["హంగుగా తాళ్ళపా కన్నయ్య చాల",
            "శృంగార రచనగా చెప్పెనీ జోల",
            "సంగతిగ సకల సంపదల నీవేళ",
            "మంగళము తిరుపట్ల మదనగోపాల"],
           "Tāḷḷapāka Annayya has aptly framed this lullaby with much grace; may "
           "all riches be with you at this hour — auspiciousness to you, "
           "Madanagopāla of Tirupati!"),
    ],
}
