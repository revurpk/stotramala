# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Manyu Sūktam — Ṛgveda 10.83–84 with viniyoga, nyāsa and the closing ṛc, as printed in the Gita Press
# Pañcasūktamūlam (Telugu, code 1026, pp. 31–33): text and svaras decoded from the PDF and proofread
# against the page images; four misprints corrected from the Ṛgveda (SOURCES.md §5.19). Svaras: '_'
# anudātta, '^' svarita, '^^' dīrgha svarita; udātta unmarked. Translations original.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "veda",
    "script": "dev",
    "doc_title": "Manyu Sūktam",
    "app_title": "Manyu Sūktam",
    "h1": "Manyu Sūktam",
    "subtitle": "Ṛgveda 10.83–84 · the hymn to Manyu (ardour, wrath)",
    "note": "Two hymns to Manyu — passion, fervour, righteous wrath personified as an inner power that conquers foes and obstacles, identified with Indra and the great gods: Ṛgveda 10.83 (ṛcs 1–7) and 10.84 (ṛcs 8–14), by the seer Manyu Tāpasa, with the viniyoga, nyāsa and closing ṛc (dhanvanā gā…) as the Gita Press Pañcasūkta prints them. Text and accents as printed there: anudātta ॒ below, svarita ॑ and dīrgha svarita ᳚ above, udātta unmarked, shown in the Devanāgarī, in which this page opens, and in the Telugu; the IAST is an unaccented reading aid.",
    "audio": "https://www.youtube.com/watch?v=52ugjBz-hgM",
    "audio_label": "Vedic chant with Sanskrit text",
    "footer": "Source: Śrī Pañcasūktamūlam (Telugu), Gita Press, Gorakhpur (code 1026), pp. 31–33 — text and svaras; collated with the accented Ṛgveda (Sāyaṇa) on Sanskrit Wikisource (public domain); translations original",
    "sections": [
        {"padas": ["yaste manyo iti saptarcasya sūktasya | tāpaso manyurṛṣiḥ | manyurdevatā | jagatī chandaḥ | dvitīye saptame ca triṣṭup |", "tvayā manyo iti saptarcasya sūktasya | tāpaso manyurṛṣiḥ | manyurdevatā | ādyāstisrastriṣṭubhaḥ tataścatasro jagatyaḥ |", "manyudevatā prasāda siddhyarthe jape viniyogaḥ ||"], "num": "", "gloss": "Viniyoga. Of the seven-ṛc hymn “yaste manyo” the seer is Manyu Tāpasa, the deity Manyu, the metre jagatī, triṣṭubh in the second and seventh; of the seven-ṛc hymn “tvayā manyo” the seer is Manyu Tāpasa, the deity Manyu, the first three in triṣṭubh, then four in jagatī. The application: recitation for the grace of the deity Manyu and for success.", "prose": True},
        {"padas": ["saṃsṛṣṭaṃ dhana mubhayaṃ aṅguṣṭhābhyāṃ namaḥ | hṛdayāya namaḥ |", "samākṛtamasmabhyaṃ dattāṃ tarjanībhyāṃ namaḥ | śirase svāhā |", "varuṇaśca manyuḥ madhyamābhyāṃ namaḥ | śikhāyai vaṣaṭ |", "bhiyaṃ dadhānā anāmikābhyāṃ namaḥ | kavacāya hum |", "hṛdayeṣu śatravaḥ kaniṣṭhikābhyāṃ namaḥ | netratrayāya vauṣaṭ |", "parājitāso apanilayantāṃ karatalakarapṛṣṭhābhyāṃ namaḥ | astrāya phaṭ ||", "bhūrbhuvassuvaromiti digbandhaḥ ||"], "num": "", "gloss": "Nyāsa. The words of the last ṛc are placed on the fingers and the limbs: “saṃsṛṣṭaṃ dhanam ubhayam” on the thumbs and the heart; “samākṛtam asmabhyaṃ dattām” on the forefingers and the head; “varuṇaśca manyuḥ” on the middle fingers and the topknot; “bhiyaṃ dadhānā” on the ring fingers and as armour; “hṛdayeṣu śatravaḥ” on the little fingers and the three eyes; “parājitāso apanilayantām” on palms and backs of the hands and as the weapon. With bhūr bhuvas suvar om the quarters are bound.", "prose": True},
        {"padas": ["hariḥ_ om"], "num": "", "gloss": "Hari, om.", "prose": True},
        _v(["yaste^^ ma_nyo vi^dhadvajrasāyaka_saha_ojaḥ^ puṣyati_ viśva^mānu_ṣak |", "sā_hyāma_dāsa_ māryaṃ_ tvayā^^ yu_jā saha^skṛtena_ saha^sā_ saha^svatā"], "|| 1 ||",
           "He who has worshipped you, O Manyu — thunderbolt, arrow — gains power, might, and thrives in all things. With you as ally may we overcome the Dāsa and the Ārya, O strength-made, mighty, and full of force."),
        _v(["ma_nyuriṃdro^^ ma_nyure_vāsa^ de_vo ma_nyurhotā_ varu^ṇo jā_tave^^dāḥ |", "ma_nyuṃ viśa^ īḷate_ mānu^ṣī_ryāḥ pā_hi no^^ manyo_ tapa^sā sa_joṣāḥ^^"], "|| 2 ||",
           "Manyu was Indra, Manyu was the god himself; Manyu was the invoker, Varuṇa, Jātavedas. The human tribes extol Manyu. Guard us, O Manyu, in accord with Tapas (ardour)."),
        _v(["abhī^hi manyo ta_vasa_sta vī^^yā_n tapa^sāyu_jā vija^hi_ śatrū^n |", "a_mi_tra_hā vṛ^tra_hā da^syu_hā ca_ viśvā_vasū_ nyābha^rā_ tvaṃnaḥ^"], "|| 3 ||",
           "Come forth, O Manyu, mightier than the mighty; with ardour as your ally, strike down the foes. Slayer of enemies, slayer of Vṛtra, slayer of Dasyus — bring to us all treasures."),
        _v(["tvaṃ hi ma^nyo a_bhibhū^^tyojā ssvayaṃ_ bhūrbhāmo^^ abhimātiṣā_haḥ |", "vi_śvaca^rṣaṇi_ ssahu^ri_ssahā^^vā na_smā svojaḥ_ pṛta^nāsudhehi"], "|| 4 ||",
           "For you, O Manyu, are of overwhelming might, self-existent, the fury that vanquishes assailants. Belonging to all peoples, victorious, all-conquering — place strength in us in the battles."),
        _v(["abhā_ga ssanna pa_pare^^to asmi_ tava_ kratvā^^ tavi_ṣasya^ pracetaḥ |", "taṃtvā^manyo akra_turji^hīḷā_haṃ svāta_nūrba^la_deyā^^ ya_mehi^"], "|| 5 ||",
           "Portionless, I have been set apart, O wise and mighty one, by your will. Powerless, I have angered you, O Manyu, your very self — come to me, then, for the giving of strength."),
        _v(["a_yaṃ te^^ a_smyupa_me hya_rvāṅpra^tī cī_nassa^hure viśvadhāyaḥ |", "manyo^^ vajri nna_bhi māmāva^vṛtsva_hanā^^ va_dasyū^^n ṛ_tabo^^ dhyā_peḥ"], "|| 6 ||",
           "I am yours; come here to me, turned toward me, O all-sustaining conqueror. O Manyu, wielder of the bolt, turn to me; let us slay the Dasyus together, and be mindful of your friend."),
        _v(["a_bhiprehi^ dakṣiṇa_to bha^vā_medhā^^ vṛ_trāṇi^ jaṃghanāva_bhūri^ |", "ju_homi^ te dha_ruṇa_ mmadhvo_ agra^mu_bhā u^pāṃ_śu pra^tha_mā pi^bāva"], "|| 7 ||",
           "Advance! Be at my right hand, and let us slay the many foes. I offer you the sustaining choicest of the sweet draught; let us both drink it first, in secret."),
        _v(["tvayā^^ manyo sa_ratha^māru_jaṃto_ harṣa^ māṇāso dhṛṣi_tā ma^rutvaḥ |", "ti_gmeṣa^va_ āyu^dhāsaṃ_śiśā^^nā a_bhiprayaṃ^^tu_ naro^^ a_gnirū^^pāḥ"], "|| 8 ||",
           "With you, O Manyu, as chariot-mate, breaking through, exulting, emboldened, O Marut-companioned one — with keen arrows, whetting their weapons, may the fire-formed heroes march forth."),
        _v(["a_gniri^va manyo tviṣi_ta ssa^hasva senā_nīrna^ssahure hū_tae^^dhi |", "ha_tvāya_ śatrū_nvibha^jasva_ veda_ ojo_ mimā^no vi_mṛdho^^nudasva"], "|| 9 ||",
           "Like fire, O Manyu, ablaze, prevail; O our commander, O conqueror, be present when called. Having slain the foes, share out the spoils; measuring your might, thrust away the scorners."),
        _v(["saha^sva manyo a_bhimā^^ti ma_sme ru_jan mṛ_ṇan pra^mṛ_ṇan pre^hi_ śatrū^n |", "u_graṃte_ pājo^^na_nvāru^ rudhreva_śīvaśa^^nnayasa^eka ja_tvam"], "|| 10 ||",
           "Overpower our adversary, O Manyu; breaking, crushing, shattering, advance upon the foes. Your fierce force none could hold back; you, the ruler, lead the foe to submission, O sole-born."),
        _v(["eko^^ bahū_nā ma^simanyavīḷi_to viśaṃ^^ viśaṃ yu_dhaye_ saṃśi^śādhi |", "akṛ^ttaru_ktvayā^^ yu_jā va_yaṃ dyu_maṃtaṃ_ ghoṣaṃ^^ vija_yāya^ kṛṇmahe"], "|| 11 ||",
           "Alone of the many you are, O Manyu, invoked; whet each tribe for the fight. With you, of flawless lustre, as ally, we raise a resounding shout for victory."),
        _v(["vi_je_ṣa_kṛdiṃdra^ ivānavabravo_3'smākaṃ^^ manyo adhi_pā bha^ve_ha |", "pri_yaṃte_ nāma^ sahure gṛ^ṇīmasi vi_dmāta^mutthsaṃ_ yata^ ā ba_bhūtha^"], "|| 12 ||",
           "A maker of victory, not to be gainsaid, like Indra — be our overlord here, O Manyu. We sing your dear name, O conqueror; we know the wellspring from which you have come."),
        _v(["ābhū^^tyā saha_jā va^jrasāyaka_saho^^ bibha_rṣyabhi^bhūta_ utta^ram |", "kratvā^^no manyo sa_hame_dhye^^dhi mahādha_nasya^ puruhūta saṃ_sṛji^^"], "|| 13 ||",
           "Born together with power, O thunderbolt, O arrow, you bear ever-superior might, O invincible one. By your will, O Manyu, be our comrade in the winning of great wealth, O much-invoked."),
        _v(["saṃsṛ^ṣṭaṃ_ dhana^ mu_bhayaṃ^^ sa_mākṛ^ta ma_smabhyaṃ^^dhattāṃ_ varu^ṇaścama_nyuḥ |", "bhiyaṃ_ dadhā^^nā_ hṛda^yeṣu_ śatra^vaḥ_ parā^^jitāso_ apa_nila^yaṃtām"], "|| 14 ||",
           "May Varuṇa and Manyu grant us the wealth won and gathered on both sides. And may the enemies, bearing fear in their hearts, defeated, sink away."),
        _v(["dhanva^nā_gā dhanva^nā_ jiṃ ja^yema_ dhanva^nā tī_vrā ssa_mado^^ jayema |", "dhanu_śśatro^ rapakā_maṃ kṛ^ṇotu_ dhanva^nā_ ssarvāḥ^^ pra_diśo^^ jayema"], "|| 15 ||",
           "With the bow may we win the cattle, with the bow the contest, with the bow the fierce battles; the bow makes the foe's desire undone. With the bow may we win all the quarters."),
        _v(["oṃ śāṃti_ śśāṃti_ śśāṃtiḥ^"], "",
           "Om, peace, peace, peace."),
    ],
}
