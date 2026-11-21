# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Puruṣa Sūktam — Taittirīya Āraṇyaka 3.12–13 with the śānti, 23 mantras, as printed in the
# Gita Press Pañcasūktamūlam (Telugu, code 1026, pp. 5–8): text and svaras decoded from the PDF
# (legacy Gowthami font; svara strokes placed by position) and proofread against the page images;
# collated with the accented TA on Sanskrit Wikisource. Svaras: '_' anudātta, '^' svarita, '^^'
# dīrgha svarita; udātta unmarked. Translations original. See SOURCES.md §5.18.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "veda",
    "script": "dev",
    "doc_title": "Puruṣa Sūktam",
    "app_title": "Puruṣa Sūktam",
    "h1": "Puruṣa Sūktam",
    "subtitle": "Taittirīya Āraṇyaka 3.12–13 · the hymn of the Cosmic Being",
    "note": "The hymn of the Puruṣa, the Cosmic Being from whose self-sacrifice the whole ordered world unfolds — the ṛcs, the metres, the creatures and the social order — with the uttara-nārāyaṇa that follows it in the Taittirīya Āraṇyaka (3.13), framed by the śānti tacchaṃ yorā vṛṇīmahe. Text and accents as printed by the Gita Press Pañcasūkta: anudātta ॒ below, svarita ॑ and dīrgha svarita ᳚ above, udātta unmarked, shown in the Devanāgarī, in which this page opens, and in the Telugu; the IAST is an unaccented reading aid.",
    "footer": "Source: Śrī Pañcasūktamūlam (Telugu), Gita Press, Gorakhpur (code 1026), pp. 5–8 — text and svaras; collated with the accented Taittirīya Āraṇyaka on Sanskrit Wikisource (public domain); translations original",
    "sections": [
        _v(["hariḥ_ om tacchaṃ_yorā vṛ^ṇīmahe |", "gā_tuṃ ya_jñāya^ |", "gā_tuṃ ya_jñapa^taye |", "daivī^^ sva_stira^stu naḥ |", "sva_stirmānu^ṣebhyaḥ |", "ū_rdhvaṃ ji^gātu bheṣa_jam |", "śaṃ no^ astu dvi_pade^^ |", "śaṃ catu^ṣpade |", "oṃ śāṃti_ śśāṃti_ śśāṃtiḥ^"], "",
           "Peace chant. We choose that peace and well-being: the way for the sacrifice, the way for the lord of the sacrifice. May divine well-being be ours, well-being for men; may the healing herb grow upward. May there be peace for our two-footed, peace for our four-footed. Om, peace, peace, peace."),
        _v(["oṃ sa_hasra^śīrṣā_ puru^ṣaḥ |", "sa_ha_srā_kṣassa_hasra^pāt |", "sa bhūmiṃ^ vi_śvato^ vṛ_tvā |", "atya^tiṣṭhaddaśāṃgu_lam"], "|| 1 ||",
           "Peace chant. We choose that peace and well-being: the way for the sacrifice, the way for the lord of the sacrifice. May divine well-being be ours, well-being for men; may the healing herb grow upward. May there be peace for our two-footed, peace for our four-footed. Om, peace, peace, peace."),
        _v(["puru^ṣa e_vedagṃ sarva^^m |", "yadbhū_taṃ yacca_ bhavya^^m |", "u_tāmṛ^ta_tvasyeśā^naḥ |", "yadanne^nāti_roha^ti"], "|| 2 ||",
           "The Puruṣa has a thousand heads, a thousand eyes, a thousand feet. Enveloping the earth on every side, he stands beyond it, ten fingers' breadth."),
        _v(["e_tāvā^nasya mahi_mā |", "ato_ jyāyāg^śca_ pūru^ṣaḥ |", "pādo^^'sya_ viśvā^ bhū_tāni^ |", "tri_pāda^syā_mṛtaṃ^ di_vi"], "|| 3 ||",
           "The Puruṣa alone is all this — what has been and what is yet to be. And he is the lord of immortality, in that he grows beyond (this world) by food."),
        _v(["tri_pādū_rdhva udai_tpuru^ṣaḥ |", "pādo^^'sye_hābha^vā_tpunaḥ^ |", "tato_ viṣva_ṅvya^krāmat |", "sā_śa_nā_na_śa_ne a_bhi"], "|| 4 ||",
           "Such is his greatness, and the Puruṣa is greater still. All beings are one quarter of him; three quarters, the immortal, are in heaven."),
        _v(["tasmā^^dvi_rāḍa^jāyata |", "vi_rājo_ adhi_pūru^ṣaḥ |", "sa jā_to atya^ricyata |", "pa_ścādbhū^mi_ matho^ pu_raḥ"], "|| 5 ||",
           "With three quarters the Puruṣa rose upward; one quarter of him came to be here again. Thence he spread out in every direction, over what eats and what does not eat."),
        _v(["yatpuru^ṣeṇa ha_viṣā^^ |", "de_vā ya_jñamata^nvata |", "va_saṃ_to a^syā'sī_dājya^^m |", "grī_ṣma i_dhmaśśa_raddha_viḥ"], "|| 6 ||",
           "From him Virāj was born, and from Virāj the Puruṣa (again). Once born, he reached beyond the earth, behind and before."),
        _v(["sa_ptāsyā^sanpari_dhayaḥ^ |", "trissa_ptasa_midhaḥ^ kṛ_tāḥ |", "de_vā yadya_jñaṃ ta^nvā_nāḥ |", "aba^dhna_npuru^ṣaṃ pa_śum"], "|| 7 ||",
           "The moon was born from his mind; from his eye the sun was born; from his mouth Indra and Agni, and from his breath the wind was born."),
        _v(["taṃ ya_jñaṃ ba_rhiṣi_ praukṣa^nn |", "puru^ṣaṃ jā_ta ma^gra_taḥ |", "tena^ de_vā aya^jaṃta |", "sā_dhyā ṛṣa^yaśca_ ye"], "|| 8 ||",
           "When the gods spread out the sacrifice with the Puruṣa as oblation, spring was its clarified butter, summer the kindling, autumn the offering."),
        _v(["tasmā^^dya_jñātsa^rva_hutaḥ^ |", "saṃbhṛ^taṃ pṛṣadā_jyam |", "pa_śūgstāgśca^kre vāya_vyā^n |", "ā_ra_ṇyāngrā_myāśca_ ye"], "|| 9 ||",
           "Seven were the enclosing sticks, thrice seven the faggots of fuel made, when the gods, spreading the sacrifice, bound the Puruṣa as the victim."),
        _v(["tasmā^^dya_jñātsa^rva_hutaḥ^ |", "ṛca_ssāmā^ni jajñire |", "chaṃdāgṃ^si jajñire_ tasmā^^t |", "yaju_stasmā^dajāyata"], "|| 10 ||",
           "That Puruṣa, born in the beginning, they consecrated as the sacrifice upon the sacred grass. With him the gods offered sacrifice, and the Sādhyas, and the seers."),
        _v(["tasmā_daśvā^ ajāyaṃta |", "ye ke co^bha_yāda^taḥ |", "gāvo^ ha jajñire_ tasmā^^t |", "tasmā^^jjā_tā a^jā_vayaḥ^"], "|| 11 ||",
           "From that sacrifice, wholly offered, the mixed curds and butter were gathered; and he formed the creatures of the air, of the forest, and of the village."),
        _v(["yatpuru^ṣaṃ_ vya^dadhuḥ |", "kati_dhā vya^kalpayan |", "mukhaṃ_ kima^sya_ kau bā_hū |", "kāvū_rū pādā^vucyete"], "|| 12 ||",
           "From that sacrifice, wholly offered, the ṛcs and the sāmans were born; the metres were born from it, and from it the yajus was born."),
        _v(["brā_hma_ṇo^^sya_ mukha^māsīt |", "bā_hū rā^ja_nyaḥ^ kṛ_taḥ |", "ū_rū tada^sya_ yadvaiśyaḥ^ |", "pa_dbhyāgṃ śū_dro a^jāyata"], "|| 13 ||",
           "From it horses were born, and all creatures with two rows of teeth; cattle were born from it, and from it goats and sheep."),
        _v(["caṃ_dramā_ mana^so jā_taḥ |", "cakṣo_ ssūryo^ ajāyata |", "mukhā_diṃdra^ ścā_gniśca^ |", "prā_ṇādvā_yu ra^jāyata"], "|| 14 ||",
           "When they divided the Puruṣa, into how many parts did they arrange him? What was his mouth, what his arms, what his thighs and his feet called?"),
        _v(["nābhyā^ āsīdaṃ_tari^kṣam |", "śī_rṣṇodyau ssama^vartata |", "pa_dbhyāṃ bhūmi_rdiśa_śśrotrā^^t |", "tathā^ lo_kāgṃ a^kalpayan"], "|| 15 ||",
           "The brāhmaṇa was his mouth; the rājanya (kṣatriya) was made from his arms; his thighs became the vaiśya; from his feet the śūdra was born."),
        _v(["vedā_ha me_taṃ puru^ṣaṃ ma_hāṃta^^m |", "ā_di_tya_va^rṇaṃ_ tama^sa_stu pā_re |", "sarvā^ṇi rūpāṇi^ vicitya_ dhīraḥ^ |", "nāmā^ni kṛ_tvā'bhi_vada_n yadāste^^"], "|| 16 ||",
           "I know this great Puruṣa, coloured like the sun, beyond the darkness — the wise one who, having fashioned all forms and made their names, abides calling them by name."),
        _v(["dhā_tā pu_rastā_dyamu^dāja_hāra^ |", "śa_kraḥ pra^vi_dvān pra_di^śa_ ścata^sraḥ |", "tame_vaṃ vi_dvā na_mṛta^ i_ha bha^vati |", "nānyaḥ panthā_ aya^nāya vidyate"], "|| 17 ||",
           "He whom Dhātṛ, the Ordainer, proclaimed in the beginning, whom Śakra, knowing, proclaimed to the four quarters — one who knows him thus becomes immortal here; there is no other path for the going."),
        _v(["ya_jñena^ ya_jña ma^yajaṃta de_vāḥ |", "tāni_ dharmā^ṇi pratha_mā nyā^san |", "te ha_ nākaṃ^ mahi_māna^ssacante |", "yatra_ pūrve^ sā_dhyāssaṃti^ de_vāḥ"], "|| 18 ||",
           "From his navel arose the mid-air; from his head the heaven took shape; from his feet the earth, from his ear the quarters — thus they fashioned the worlds."),
        _v(["a_dbhyassaṃbhū^taḥ pṛthi_vyai rasā^^cca |", "vi_śvaka^rmaṇa_ ssama^varta_tādhi^ |", "tasya_ tvaṣṭā^ vi_dadha^ drū_pame^ti |", "tatpuru^ṣasya_ viśva_mājā^na_ magre^^"], "|| 19 ||",
           "Born of the waters and of the essence of the earth, he arose from Viśvakarman. Tvaṣṭṛ goes forth fashioning his form; that was the Puruṣa's whole birth in the beginning."),
        _v(["vedā_ha me_taṃ puru^ṣaṃ ma_hāṃta^^m |", "ā_di_tyava^rṇaṃ_ tama^saḥ_ para^stāt |", "tame_vaṃ vi_dvāna_mṛta^ i_ha bha^vati |", "nānyaḥ paṃthā^ vidya_te'ya^nāya"], "|| 20 ||",
           "I know this great Puruṣa, coloured like the sun, beyond the darkness. Knowing him thus one becomes immortal here; there is no other path for the going."),
        _v(["pra_jāpa^tiścarati_ garbhe^ aṃ_taḥ |", "a_jāya^māno bahu_dhā vijā^yate |", "tasya_ dhīrāḥ_ pari^jānaṃti_ yoni^^m |", "marī^cīnāṃ pa_da mi^cchaṃti ve_dhasaḥ^"], "|| 21 ||",
           "Prajāpati moves within the womb; unborn, he is born in many ways. The wise know his source; the creators seek the station of the Marīcis."),
        _v(["yo de_vebhya āta^pati |", "yo de_vānāṃ^^ pu_rohi^taḥ |", "pūrvo_ yo de_vebhyo^ jā_taḥ |", "namo^ ru_cāya_ brāhma^ye |", "rucaṃ^ brā_hmaṃ ja_nayaṃ^taḥ |", "de_vā agre_ tada^bruvan |", "yastvai_vaṃ brā^^hma_ṇo vi_dyāt |", "tasya^ de_vā asa_n vaśe^^"], "|| 22 ||",
           "He who shines for the gods, who is the gods' foremost priest, who was born before the gods — homage to the radiant one, of the nature of Brahman! Bringing forth the radiant Brahman, the gods said in the beginning: the brāhmaṇa who knows you thus — the gods shall be in his power."),
        _v(["hrīśca^ te la_kṣmīśca_ patnyau^^ |", "aho_rā_tre pā_rśve |", "nakṣa^trāṇi rū_pam |", "a_śvinau_ vyātta^^m |", "i_ṣṭaṃ ma^niṣāṇa |", "a_muṃ ma^niṣāṇa |", "sarvaṃ^ maniṣāṇa"], "|| 23 ||",
           "Hrī and Lakṣmī are your two wives; day and night are your two sides; the stars your form; the Aśvins your open mouth. Wishing, wish for me that (world); wish all for me."),
        _v(["om tacchaṃ_yorā vṛ^ṇīmahe |", "gā_tuṃ ya_jñāya^ |", "gā_tuṃ ya_jñapa^taye |", "daivī^^ sva_stira^stu naḥ |", "sva_stirmānu^ṣebhyaḥ |", "ū_rdhvaṃ ji^gātu bheṣa_jam |", "śaṃ no^ astu dvi_pade^^ |", "śaṃ catu^ṣpade |", "oṃ śāṃti_ śśāṃti_ śśāṃtiḥ^ |", "hariḥ^ om |", "iti śrī puruṣasūktam"], "",
           "Peace chant. We choose that peace and well-being: the way for the sacrifice, the way for the lord of the sacrifice. May divine well-being be ours, well-being for men; may the healing herb grow upward. May there be peace for our two-footed, peace for our four-footed. Om, peace, peace, peace. Hari, om."),
    ],
}
