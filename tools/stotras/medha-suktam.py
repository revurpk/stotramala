# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Medhā Sūktam — Mahānārāyaṇa / Taittirīya Āraṇyaka 10.41–44 (anuvākas 39–42 in the Andhra numbering of the
# source), accented, from Sanskrit Wikisource तैत्तिरीय-आरण्यकम् via dev2iast. Not in the Gita Press Pañcasūkta.
# Svaras: '_' anudātta, '^' svarita; udātta unmarked. Translations original. See SOURCES.md.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "veda",
    "script": "dev",
    "doc_title": "Medhā Sūktam",
    "app_title": "Medhā Sūktam",
    "h1": "Medhā Sūktam",
    "subtitle": "Mahānārāyaṇa (Taittirīya Āraṇyaka 10.41–44) · the hymn to Wisdom",
    "note": "The Medhā Sūkta of the Mahānārāyaṇa: five mantras praying to Medhā, wisdom and retentive understanding, as a goddess, and to Indra, Sarasvatī and the Aśvins for her gift. It is not in the Gita Press Pañcasūkta, so the accented text is that of the Taittirīya Āraṇyaka on Sanskrit Wikisource, kept with its Andhra spellings (aphsarāsu, citravviṁndate). Accents: anudātta ॒ below, svarita ॑ and dīrgha svarita ᳚ above, udātta unmarked, shown in the Devanāgarī, in which this page opens, and in the Telugu; the IAST is an unaccented reading aid.",
    "footer": "Source: Sanskrit Wikisource — तैत्तिरीय-आरण्यकम् (accented, prapāṭhaka 10, anuvākas 39–42 of that edition; public domain); translations original",
    "sections": [
        _v(["me_dhā de_vī ju_ṣamā^ṇā na_ āgā^^dvi_śvācī^ bha_drā su^mana_syamā^nā |", "tvayā_ juṣṭā^ ju_ṣamā^ṇā du_ruktā^^nbṛ_hadva^dema vi_dathe^ su_vīrāḥ^^"], "|| 1 ||",
           "Medhā, the goddess, has come to us, delighting in us, all-pervading, gracious, kindly-minded. Favoured by you and delighting, may we, rich in heroes, overcome ill speech and speak greatly in the assembly."),
        _v(["tvayā_ juṣṭa^ ṛ_ṣirbha^vati devi_ tvayā_ brahmā^''ga_taśrī^ru_ta tvayā^^ |", "tvayā_ juṣṭa^ści_travviṁ^ndate vasu_ sā no^ juṣasva_ dravi^ṇena medhe"], "|| 2 ||",
           "Favoured by you, O goddess, one becomes a seer; through you a priest of Brahman, one who has gained glory — through you. Favoured by you one finds bright wealth; O Medhā, delight in us with riches."),
        _v(["me_dhāṃ ma_ indro^ dadātu me_dhānde_vī sara^svatī |", "me_dhāṃ me^ a_śvinau^ de_vāvādha^ttāṃ_ puṣka^rasrajā"], "|| 3 ||",
           "May Indra give me wisdom, the goddess Sarasvatī wisdom; may the two divine Aśvins, garlanded with lotuses, place wisdom in me."),
        _v(["a_phsa_rāsu^ ca_ yā me_dhā ga^ndha_rveṣu^ ca_ yanmanaḥ^ |", "daivī^ me_dhā ma^nuṣya_jā sā māṃ^^ me_dhā su_rabhi^rjuṣatām"], "|| 4 ||",
           "The wisdom that is in the apsarases, and the mind that is in the gandharvas, divine wisdom and that born of men — may that fragrant wisdom delight in me."),
        _v(["ā māṃ^^ me_dhā su_rabhi^rvi_śvarū^pā_ hira^ṇyavarṇā_ jaga^tī jaga_myā |", "ūrja^svatī_ paya^sā_ pinva^mānā_ sā māṃ^^ me_dhā su_pratī^kā juṣatām"], "|| 5 ||",
           "May wisdom come to me, fragrant, of every form, golden-coloured, moving and ever on the move, full of strength, swelling with milk; may that fair-faced wisdom delight in me."),
    ],
}
