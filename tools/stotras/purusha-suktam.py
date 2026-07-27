# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Puruṣa Sūkta — Ṛgveda 10.90 (Nārāyaṇa, to Puruṣa), 16 ṛcs. The ACCENTED
# saṃhitā is keyed from Sanskrit Wikisource (ऋग्वेदः सूक्तं १०.९०, Sāyaṇa
# edition, public domain) via the teltools dev2iast port: Vedic svaras carried
# as '_' (anudātta ॒) and '^' (svarita ॑) after the vowel; udātta unmarked.
# Accents render in Devanāgarī (the page opens there); IAST/Telugu drop them
# as reading aids. Translations original. See SOURCES.md §5.18.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "veda",
    "script": "dev",
    "doc_title": "Puruṣa Sūktam",
    "app_title": "Puruṣa Sūktam",
    "h1": "Puruṣa Sūktam",
    "subtitle": "Ṛgveda 10.90 · the hymn of the Cosmic Being",
    "note": "The hymn of the Puruṣa, the Cosmic Being from whose self-sacrifice "
            "the whole ordered world unfolds — the ṛcs, the metres, the "
            "creatures, and the social order. This is the sixteen-ṛc Ṛgvedic "
            "form (RV 10.90). The accented saṃhitā text carries the Vedic "
            "pitch-accents (anudātta ॒ below, svarita ॑ above; udātta unmarked), "
            "shown in the Devanāgarī, in which this page opens; the IAST and "
            "Telugu are unaccented reading aids.",
    "footer": "Source: Sanskrit Wikisource — ऋग्वेदः सूक्तं १०.९० (accented saṃhitā, Sāyaṇa edition; public domain)",
    "sections": [
        _v(["sa_hasra^śīrṣā_ puru^ṣaḥ sahasrā_kṣaḥ sa_hasra^pāt |",
            "sa bhūmiṃ^ vi_śvato^ vṛ_tvātya^tiṣṭhaddaśāṅgu_lam"], "|| 1 ||",
           "The Puruṣa has a thousand heads, a thousand eyes, a thousand feet. "
           "Enveloping the earth on every side, he stands beyond it, ten "
           "fingers' breadth."),
        _v(["puru^ṣa e_vedaṃ sarvaṃ_ yadbhū_taṃ yacca_ bhavya^m |",
            "u_tāmṛ^ta_tvasyeśā^no_ yadanne^nāti_roha^ti"], "|| 2 ||",
           "The Puruṣa alone is all this — what has been and what is yet to be. "
           "He is the lord of immortality, which he surpasses by (transcends "
           "through) food."),
        _v(["e_tāvā^nasya mahi_māto_ jyāyāṁ^śca_ pūru^ṣaḥ |",
            "pādo^'sya_ viśvā^ bhū_tāni^ tri_pāda^syā_mṛtaṃ^ di_vi"], "|| 3 ||",
           "Such is his greatness, and the Puruṣa is greater still. All beings "
           "are one quarter of him; three quarters, the immortal, are in "
           "heaven."),
        _v(["tri_pādū_rdhva udai_tpuru^ṣa_ḥ pādo^'sye_hābha^va_tpunaḥ^ |",
            "tato_ viṣva_ṅvya^krāmatsāśanānaśa_ne a_bhi"], "|| 4 ||",
           "With three quarters the Puruṣa rose upward; one quarter of him came "
           "to be here again. Thence he spread out in every direction, over "
           "what eats and what does not eat."),
        _v(["tasmā^dvi_rāḷa^jāyata vi_rājo_ adhi_ pūru^ṣaḥ |",
            "sa jā_to atya^ricyata pa_ścādbhūmi_matho^ pu_raḥ"], "|| 5 ||",
           "From him Virāj was born, and from Virāj the Puruṣa (again). Once "
           "born, he reached beyond the earth, behind and before."),
        _v(["yatpuru^ṣeṇa ha_viṣā^ de_vā ya_jñamata^nvata |",
            "va_sa_nto a^syāsī_dājyaṃ^ grī_ṣma i_dhmaḥ śa_raddha_viḥ"], "|| 6 ||",
           "When the gods spread out the sacrifice with the Puruṣa as oblation, "
           "spring was its clarified butter, summer the kindling, autumn the "
           "offering."),
        _v(["taṃ ya_jñaṃ ba_rhiṣi_ praukṣa_npuru^ṣaṃ jā_tama^gra_taḥ |",
            "tena^ de_vā a^yajanta sā_dhyā ṛṣa^yaśca_ ye"], "|| 7 ||",
           "That Puruṣa, born in the beginning, they consecrated as the "
           "sacrifice upon the sacred grass. With him the gods offered "
           "sacrifice, and the Sādhyas, and the seers."),
        _v(["tasmā^dya_jñātsa^rva_huta_ḥ sambhṛ^taṃ pṛṣadā_jyam |",
            "pa_śūntāṁśca^kre vāya_vyā^nāra_ṇyāngrā_myāśca_ ye"], "|| 8 ||",
           "From that sacrifice, wholly offered, the mixed curds and butter "
           "were gathered; and he formed the creatures of the air, of the "
           "forest, and of the village."),
        _v(["tasmā^dya_jñātsa^rva_huta_ ṛca_ḥ sāmā^ni jajñire |",
            "chandāṃ^si jajñire_ tasmā_dyaju_stasmā^dajāyata"], "|| 9 ||",
           "From that sacrifice, wholly offered, the ṛcs and the sāmans were "
           "born; the metres were born from it, and from it the yajus was "
           "born."),
        _v(["tasmā_daśvā^ ajāyanta_ ye ke co^bha_yāda^taḥ |",
            "gāvo^ ha jajñire_ tasmā_ttasmā^jjā_tā a^jā_vayaḥ^"], "|| 10 ||",
           "From it horses were born, and all creatures with two rows of teeth; "
           "cattle were born from it, and from it goats and sheep."),
        _v(["yatpuru^ṣaṃ_ vyada^dhuḥ kati_dhā vya^kalpayan |",
            "mukhaṃ_ kima^sya_ kau bā_hū kā ū_rū pādā^ ucyete"], "|| 11 ||",
           "When they divided the Puruṣa, into how many parts did they arrange "
           "him? What was his mouth, what his arms, what his thighs and his "
           "feet called?"),
        _v(["brā_hma_ṇo^'sya_ mukha^māsīdbā_hū rā^ja_nyaḥ^ kṛ_taḥ |",
            "ū_rū tada^sya_ yadvaiśyaḥ^ pa_dbhyāṃ śū_dro a^jāyata"], "|| 12 ||",
           "The brāhmaṇa was his mouth; the rājanya (kṣatriya) was made from his "
           "arms; his thighs became the vaiśya; from his feet the śūdra was "
           "born."),
        _v(["ca_ndramā_ mana^so jā_taścakṣo_ḥ sūryo^ ajāyata |",
            "mukhā_dindra^ścā_gniśca^ prā_ṇādvā_yura^jāyata"], "|| 13 ||",
           "The moon was born from his mind; from his eye the sun was born; from "
           "his mouth Indra and Agni, and from his breath the wind was born."),
        _v(["nābhyā^ āsīda_ntari^kṣaṃ śī_rṣṇo dyauḥ sama^vartata |",
            "pa_dbhyāṃ bhūmi_rdiśa_ḥ śrotrā_ttathā^ lo_kāṁ a^kalpayan"], "|| 14 ||",
           "From his navel arose the mid-air; from his head the heaven took "
           "shape; from his feet the earth, from his ear the quarters — thus "
           "they fashioned the worlds."),
        _v(["sa_ptāsyā^sanpari_dhaya_striḥ sa_pta sa_midhaḥ^ kṛ_tāḥ |",
            "de_vā yadya_jñaṃ ta^nvā_nā aba^dhna_npuru^ṣaṃ pa_śum"], "|| 15 ||",
           "Seven were the enclosing sticks, thrice seven the faggots of fuel "
           "made, when the gods, spreading the sacrifice, bound the Puruṣa as "
           "the victim."),
        _v(["ya_jñena^ ya_jñama^yajanta de_vāstāni_ dharmā^ṇi pratha_mānyā^san |",
            "te ha_ nākaṃ^ mahi_mānaḥ^ sacanta_ yatra_ pūrve^ sā_dhyāḥ santi^ de_vāḥ"], "|| 16 ||",
           "With the sacrifice the gods sacrificed to the sacrifice; these were "
           "the first ordinances. These great powers reached the firmament, "
           "where the ancient Sādhyas, the gods, abide."),
    ],
}
