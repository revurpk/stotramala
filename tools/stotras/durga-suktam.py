# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Durgā Sūktam — Taittirīya Āraṇyaka 10.2 with the Kātyāyanī gāyatrī and śānti, as printed in the Gita
# Press Pañcasūktamūlam (Telugu, code 1026, p. 28): text and svaras decoded from the PDF and proofread
# against the page image; three misprints corrected from the TA (SOURCES.md). Svaras: '_' anudātta,
# '^' svarita, '^^' dīrgha svarita; udātta unmarked. Translations original.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "veda",
    "script": "dev",
    "doc_title": "Durgā Sūktam",
    "app_title": "Durgā Sūktam",
    "h1": "Durgā Sūktam",
    "subtitle": "Taittirīya Āraṇyaka 10.2 (Mahānārāyaṇa) · the hymn of crossing over",
    "note": "The Durgā Sūkta of the Mahānārāyaṇa (Taittirīya Āraṇyaka 10.2): seven ṛcs to Agni Jātavedas and to the goddess Durgā, the deliverer who carries the worshipper across (dur-ga, “hard to pass”) every danger, closed by the Kātyāyanī gāyatrī. Text and accents as printed by the Gita Press Pañcasūkta: anudātta ॒ below, svarita ॑ and dīrgha svarita ᳚ above, udātta unmarked, shown in the Devanāgarī, in which this page opens, and in the Telugu; the IAST is an unaccented reading aid.",
    "footer": "Source: Śrī Pañcasūktamūlam (Telugu), Gita Press, Gorakhpur (code 1026), p. 28 — text and svaras; collated with the accented Taittirīya Āraṇyaka on Sanskrit Wikisource (public domain); translations original",
    "sections": [
        _v(["oṃ jā_tave^dase sunavāma_ soma^marātī ya_to nida^hāti_ vedaḥ^ |", "sa naḥ^ parṣa_dati^ du_rgāṇi_ viśvā^ nā_veva_ siṃdhuṃ duri_tā'tya_gniḥ"], "|| 1 ||",
           "For Jātavedas, the knower of all beings, let us press the Soma; may he burn away the wealth of the hostile. May Agni carry us across all hardships, as a boat across the river, beyond all troubles."),
        _v(["tāma_gniva^rṇāṃ_ tapa^sā jva_laṃtīṃ vvaiṁ^roca_nīṃ karma^pha_leṣu_ juṣṭāṃ^^ |", "du_rgāṃ de_vīgṃ śara^ṇama_haṃ prapa^dye su_tara^si tarase_ na^maḥ"], "|| 2 ||",
           "I take refuge in the goddess Durgā, fire-coloured, blazing with ascetic ardour, radiant, delighting in the fruits of action. O you who carry across so well, homage to you, the swift deliverer."),
        _v(["agne_ tvaṃ pā^rayā_ navyo^ a_smānsvastibhira_ti^ du_rgāṇi_ viśvā^^ |", "pūśca^ pṛ_thvī ba^hu_lā na^ u_rvī bhavā^ to_kāya_ tana^yāya_ śaṃyyoḥ"], "|| 3 ||",
           "O Agni, you who are ever to be praised anew, lead us with blessings across all hardships. Be for us a stronghold and a broad, wide earth, and well-being and welfare to our children and their children."),
        _v(["viśvā^ni no du_rgahā^ jātaveda_ sindhuṃ_na nā_vā du^ri_tā'ti^parṣi |", "agne^ atri_vanmana^sā gṛṇā_no^^'smākaṃ^ bodhyavi_tā ta_nūnāṃ^^"], "|| 4 ||",
           "O Jātavedas, dispeller of hardships, carry us across all troubles as a boat across the sea. O Agni, praised with a mind like Atri's, be the guardian of our bodies."),
        _v(["pṛ_ta_nā_ jita_gṃ saha^mānamu_gramagni_gṃ hu^vema para_mātsadha_sthā^^t |", "sanaḥ^ parṣada_ti^ du_rgāṇi_ viśvā_ kṣāma^dde_vo ati^duri_tā'tya_gniḥ"], "|| 5 ||",
           "We call from the highest seat on Agni, the conqueror of armies, the overpowering, the fierce. May he carry us across all hardships; may the god Agni carry us beyond all troubles that wear us down."),
        _v(["pra_tnoṣi^ka_mīḍyo^ adhva_reṣu^ sa_nācca_hotā_ navya^cca_ satsi^ |", "svāṃcā^^gne ta_nuvaṃ^ pi_praya^svā_smabhyaṃ^ ca_ saubha^ga_māya^jasva"], "|| 6 ||",
           "Praiseworthy at the sacrifices, you add to our welfare, the ancient priest and the new; you take your seat. O Agni, gladden your own body, and win good fortune for us by sacrifice."),
        _v(["gobhi_rjuṣṭa^ma_yujo_ niṣi^ktaṃ_ taveṃ^^dra viṣṇora_nu_saṃca^rema |", "nāka^sya pṛ_ṣṭhama_bhi saṃvasā^no_ vvaiṁṣṇa^vīṃ lo_ka i_hamā^dayaṃtāṃ"], "|| 7 ||",
           "Following you, O Indra, unbroken, steeped in the gifts of cows, may we roam with Viṣṇu. May the gods who dwell on the vault of heaven gladden me here in the world of Viṣṇu."),
        _v(["kā_tyā_ya_nāya^ vi_dmahe^ kanyaku_māri^ dhīmahi |", "tanno^ durgiḥ praco_dayā^^t"], "|| 8 ||",
           "We know the maiden of the Kātyas; we meditate on Kanyakumārī. May Durgi impel us."),
        _v(["oṃ śāṃti_ śśāṃti_ śśāṃtiḥ^"], "",
           "Om, peace, peace, peace."),
    ],
}
