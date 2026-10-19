# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# IAST from Sanskrit Wikisource (public domain), converted via teltools
# dev2iast. Translations are original work. See SOURCES §5.

def _v(padas, num, gloss):
    return {"padas": padas, "num": num, "gloss": gloss}


STOTRA = {
    "deity": "shiva",
    "doc_title": "Ardhanārīśvara Stotram",
    "app_title": "Ardhanārīśvara",
    "h1": "Ardhanārīśvara Stotram",
    "subtitle": "Śaṅkara · to the Lord who is half woman",
    "note": "Each verse pairs a line to Śivā, the left half of the one form, "
            "with a line to Śiva, the right half, and ends in salutation to both.",
    "footer": "Source: Sanskrit Wikisource — Ardhanārīśvarastotram (public domain)",
    "sections": [
        _v(["cāmpeyagaurārdhaśarīrakāyai karpūragaurārdhaśarīrakāya |",
            "dhammillakāyai ca jaṭādharāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 1 ||",
           "To her whose half of the body is golden as the campaka flower, to him "
           "whose half is white as camphor; to her with braided hair, to him who "
           "bears matted locks — salutation to Śivā, and salutation to Śiva."),
        _v(["kastūrikākuṅkumacarcitāyai citārajaḥpuñjavicarcitāya |",
            "kṛtasmarāyai vikṛtasmarāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 2 ||",
           "To her anointed with musk and saffron, to him smeared with heaps of "
           "ash from the pyre; to her who awakens love, to him who undid Love — "
           "salutation to Śivā, and salutation to Śiva."),
        _v(["jhaṇatkvaṇatkaṅkaṇanūpurāyai pādābjarājatphaṇinūpurāya |",
            "hemāṅgadāyai bhujagāṅgadāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 3 ||",
           "To her whose bracelets and anklets jingle and chime, to him whose "
           "lotus feet shine with serpents for anklets; to her with armlets of "
           "gold, to him with armlets of snakes — salutation to Śivā, and "
           "salutation to Śiva."),
        _v(["viśālanīlotpalalocanāyai vikāsipaṅkeruhalocanāya |",
            "samekṣaṇāyai viṣamekṣaṇāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 4 ||",
           "To her whose eyes are wide blue water-lilies, to him whose eyes are "
           "opening lotuses; to her of even-numbered eyes, to him of the "
           "odd-numbered, three — salutation to Śivā, and salutation to Śiva."),
        _v(["mandāramālākalitālakāyai kapālamālāṅkitakandharāya |",
            "divyāmbarāyai ca digambarāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 5 ||",
           "To her whose curls are graced with garlands of mandāra flowers, to "
           "him whose neck is marked by a garland of skulls; to her in heavenly "
           "garments, to him clothed in the quarters of space — salutation to "
           "Śivā, and salutation to Śiva."),
        _v(["ambhodharaśyāmalakuntalāyai taḍitprabhātāmrajaṭādharāya |",
            "nirīśvarāyai nikhileśvarāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 6 ||",
           "To her whose tresses are dark as rain-clouds, to him whose matted "
           "locks are copper-red as the flash of lightning; to her who has no "
           "lord above her, to him who is lord of all — salutation to Śivā, and "
           "salutation to Śiva."),
        _v(["prapañcasṛṣṭyunmukhalāsyakāyai samastasaṃhārakatāṇḍavāya |",
            "jagajjananyai jagadekapitre namaḥ śivāyai ca namaḥ śivāya"],
           "|| 7 ||",
           "To her whose gentle dance is turned towards the making of the world, "
           "to him whose tāṇḍava brings the dissolution of all; to the mother of "
           "the world, to the one father of the world — salutation to Śivā, and "
           "salutation to Śiva."),
        _v(["pradīptaratnojjvalakuṇḍalāyai sphuranmahāpannagabhūṣaṇāya |",
            "śivānvitāyai ca śivānvitāya namaḥ śivāyai ca namaḥ śivāya"],
           "|| 8 ||",
           "To her whose earrings blaze with glowing gems, to him adorned with "
           "great glittering serpents; to her who is one with Śiva, to him who is "
           "one with Śivā — salutation to Śivā, and salutation to Śiva."),
        "ornament",
        _v(["etatpaṭhedaṣṭakamiṣṭadaṃ yo bhaktyā sa mānyo bhuvi dīrghajīvī |",
            "prāpnoti saubhāgyamanantakālaṃ bhūyātsadā tasya samastasiddhiḥ"],
           "|| 9 ||",
           "Whoever recites with devotion this octet, which grants what one "
           "wishes, is honoured on earth and lives long; he gains good fortune "
           "for endless time, and may every attainment be his always."),
        {"colophon": "iti śrīmatparamahaṃsaparivrājakācāryasya "
                     "śrīgovindabhagavatpūjyapādaśiṣyasya śrīmacchaṅkarabhagavataḥ "
                     "kṛtau ardhanārīśvarastotram sampūrṇam",
         "gloss": "Thus ends the Ardhanārīśvara Stotram, the work of Śrī Śaṅkara "
                  "Bhagavat, wandering ascetic of the highest order and disciple "
                  "of Śrī Govinda Bhagavatpāda."},
    ],
}
