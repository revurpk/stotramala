# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Manyu Sūktam — Ṛgveda 10.83 + 10.84 (seer Manyu Tāpasa, to Manyu), 14 ṛcs.
# ACCENTED saṃhitā keyed from Sanskrit Wikisource (ऋग्वेदः सूक्तं १०.८३ and
# १०.८४, Sāyaṇa edition, public domain) via the teltools dev2iast port; Vedic
# svaras carried as '_' (anudātta ॒) and '^' (svarita ॑), udātta unmarked; the
# pluta of 10.84.5 (vo3) is preserved. Accents render in Devanāgarī (the page
# opens there); IAST/Telugu drop them. Translations original. See SOURCES §5.19.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "veda",
    "script": "dev",
    "doc_title": "Manyu Sūktam",
    "app_title": "Manyu Sūktam",
    "h1": "Manyu Sūktam",
    "subtitle": "Ṛgveda 10.83–84 · the hymn to Manyu (ardour, wrath)",
    "note": "Two hymns to Manyu — passion, fervour, righteous wrath personified "
            "as an inner power that conquers foes and obstacles, identified with "
            "Indra and the great gods. Ṛgveda 10.83 (ṛcs 1–7) and 10.84 "
            "(ṛcs 8–14), by the seer Manyu Tāpasa. The accented saṃhitā carries "
            "the Vedic pitch-accents (anudātta ॒ below, svarita ॑ above; udātta "
            "unmarked), shown in the Devanāgarī, in which this page opens; the "
            "IAST and Telugu are unaccented reading aids.",
    "footer": "Source: Sanskrit Wikisource — ऋग्वेदः सूक्तं १०.८३ & १०.८४ (accented saṃhitā, Sāyaṇa edition; public domain)",
    "sections": [
        _v(["yaste^ ma_nyo'vi^dhadvajra sāyaka_ saha_ oja^ḥ puṣyati_ viśva^mānu_ṣak |",
            "sā_hyāma_ dāsa_māryaṃ_ tvayā^ yu_jā saha^skṛtena_ saha^sā_ saha^svatā"], "|| 1 ||",
           "He who has worshipped you, O Manyu — thunderbolt, arrow — gains "
           "power, might, and thrives in all things. With you as ally may we "
           "overcome the Dāsa and the Ārya, O strength-made, mighty, and "
           "full of force."),
        _v(["ma_nyurindro^ ma_nyure_vāsa^ de_vo ma_nyurhotā_ varu^ṇo jā_tave^dāḥ |",
            "ma_nyuṃ viśa^ īḷate_ mānu^ṣī_ryāḥ pā_hi no^ manyo_ tapa^sā sa_joṣā^ḥ"], "|| 2 ||",
           "Manyu was Indra, Manyu was the god himself; Manyu was the invoker, "
           "Varuṇa, Jātavedas. The human tribes extol Manyu. Guard us, O Manyu, "
           "at one with our ardour (tapas)."),
        _v(["a_bhī^hi manyo ta_vasa_stavī^yā_ntapa^sā yu_jā vi ja^hi_ śatrū^n |",
            "a_mi_tra_hā vṛ^tra_hā da^syu_hā ca_ viśvā_ vasū_nyā bha^rā_ tvaṃ na^ḥ"], "|| 3 ||",
           "Come forth, O Manyu, mightier than the mighty; with ardour as your "
           "ally, strike down the foes. Slayer of enemies, slayer of Vṛtra, "
           "slayer of Dasyus — bring to us all treasures."),
        _v(["tvaṃ hi ma^nyo a_bhibhū^tyojāḥ svaya_mbhūrbhāmo^ abhimātiṣā_haḥ |",
            "vi_śvaca^rṣaṇi_ḥ sahu^ri_ḥ sahā^vāna_smāsvoja_ḥ pṛta^nāsu dhehi"], "|| 4 ||",
           "For you, O Manyu, are of overwhelming might, self-existent, the fury "
           "that vanquishes assailants. Belonging to all peoples, victorious, "
           "all-conquering — place strength in us in the battles."),
        _v(["a_bhā_gaḥ sannapa_ pare^to asmi_ tava_ kratvā^ tavi_ṣasya^ pracetaḥ |",
            "taṃ tvā^ manyo akra_turji^hīḷā_haṃ svā ta_nūrba^la_deyā^ya_ mehi^"], "|| 5 ||",
           "Portionless, I have been set apart, O wise and mighty one, by your "
           "will. Powerless, I have angered you, O Manyu, your very self — come "
           "to me, then, for the giving of strength."),
        _v(["a_yaṃ te^ a_smyupa_ mehya_rvāṅpra^tīcī_naḥ sa^hure viśvadhāyaḥ |",
            "manyo^ vajrinna_bhi māmā va^vṛtsva_ hanā^va_ dasyūṁ^ru_ta bo^dhyā_peḥ"], "|| 6 ||",
           "I am yours; come here to me, turned toward me, O all-sustaining "
           "conqueror. O Manyu, wielder of the bolt, turn to me; let us slay the "
           "Dasyus together, and be mindful of your friend."),
        _v(["a_bhi prehi^ dakṣiṇa_to bha^vā_ me'dhā^ vṛ_trāṇi^ jaṅghanāva_ bhūri^ |",
            "ju_homi^ te dha_ruṇaṃ_ madhvo_ agra^mu_bhā u^pāṃ_śu pra^tha_mā pi^bāva"], "|| 7 ||",
           "Advance! Be at my right hand, and let us slay the many foes. I offer "
           "you the sustaining choicest of the sweet draught; let us both drink "
           "it first, in secret."),
        "ornament",
        _v(["tvayā^ manyo sa_ratha^māru_janto_ harṣa^māṇāso dhṛṣi_tā ma^rutvaḥ |",
            "ti_gmeṣa^va_ āyu^dhā saṃ_śiśā^nā a_bhi pra ya^ntu_ naro^ a_gnirū^pāḥ"], "|| 8 ||",
           "With you, O Manyu, as chariot-mate, breaking through, exulting, "
           "emboldened, O Marut-companioned one — with keen arrows, whetting "
           "their weapons, may the fire-formed heroes march forth."),
        _v(["a_gniri^va manyo tviṣi_taḥ sa^hasva senā_nīrna^ḥ sahure hū_ta e^dhi |",
            "ha_tvāya_ śatrū_nvi bha^jasva_ veda_ ojo_ mimā^no_ vi mṛdho^ nudasva"], "|| 9 ||",
           "Like fire, O Manyu, ablaze, prevail; O our commander, O conqueror, "
           "be present when called. Having slain the foes, share out the spoils; "
           "measuring your might, thrust away the scorners."),
        _v(["saha^sva manyo a_bhimā^tima_sme ru_janmṛ_ṇanpra^mṛ_ṇanprehi_ śatrū^n |",
            "u_graṃ te_ pājo^ na_nvā ru^rudhre va_śī vaśaṃ^ nayasa ekaja_ tvam"], "|| 10 ||",
           "Overpower our adversary, O Manyu; breaking, crushing, shattering, "
           "advance upon the foes. Your fierce force none could hold back; you, "
           "the ruler, lead the foe to submission, O sole-born."),
        _v(["eko^ bahū_nāma^si manyavīḷi_to viśaṃ^viśaṃ yu_dhaye_ saṃ śi^śādhi |",
            "akṛ^ttaru_ktvayā^ yu_jā va_yaṃ dyu_mantaṃ_ ghoṣaṃ^ vija_yāya^ kṛṇmahe"], "|| 11 ||",
           "Alone of the many you are, O Manyu, invoked; whet each tribe for the "
           "fight. With you, of flawless lustre, as ally, we raise a resounding "
           "shout for victory."),
        _v(["vi_je_ṣa_kṛdindra^ ivānavabra_vo_3_^'smākaṃ^ manyo adhi_pā bha^ve_ha |",
            "pri_yaṃ te_ nāma^ sahure gṛṇīmasi vi_dmā tamutsaṃ_ yata^ āba_bhūtha^"], "|| 12 ||",
           "A maker of victory, unyielding like Indra — be our overlord here, O "
           "Manyu. We sing your dear name, O conqueror; we know the wellspring "
           "from which you have come."),
        _v(["ābhū^tyā saha_jā va^jra sāyaka_ saho^ bibharṣyabhibhūta_ utta^ram |",
            "kratvā^ no manyo sa_ha me_dye^dhi mahādha_nasya^ puruhūta saṃ_sṛji^"], "|| 13 ||",
           "Born together with power, O thunderbolt, O arrow, you bear "
           "ever-superior might, O invincible one. By your will, O Manyu, be our "
           "comrade in the winning of great wealth, O much-invoked."),
        _v(["saṃsṛ^ṣṭaṃ_ dhana^mu_bhayaṃ^ sa_mākṛ^tama_smabhyaṃ^ dattāṃ_ varu^ṇaśca ma_nyuḥ |",
            "bhiyaṃ_ dadhā^nā_ hṛda^yeṣu_ śatra^va_ḥ parā^jitāso_ apa_ ni la^yantām"], "|| 14 ||",
           "May Varuṇa and Manyu grant us the wealth won and gathered on both "
           "sides. And may the enemies, bearing fear in their hearts, defeated, "
           "sink away."),
    ],
}
