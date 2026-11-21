# Review packet · saptashati

Reviewed 2026-11-20 by `claude-opus-5-5` · coverage: **full**

Source collation, not a translation review: the Sanskrit of all 13 chapters, the dhyānas and viniyogas, and the six aṅgas was compared word by word with the Gita Press Śrīdurgāsaptaśatī (code 118, the user's PDF, decoded from its Chanakya font), and the site's text was re-based on it. Word glosses were re-mapped, and every verse whose text changed had its gloss checked and corrected; glosses of unchanged verses were not re-read. The Vedic sūktas were compared (same words; Gita Press has no svaras) and left as they were. There are no translations to review.

**5 item(s) need your decision; 10 fixed in the review.**

Write your answer after **Decision:** under each item (a letter, or your own words),
then ask for the decisions to be applied. Leave it empty to keep things as they are.

## Needs your decision

### 1. [saptashati-purva](../../../stotra/devi/saptashati-purva-iast.html) · whole page · text
<!-- id: saptashati-purva:0:text:c57aea -->

**Issue.** Gita Press prints no viniyoga for the Kavaca, Argalā, Kīlaka or the Rahasyas, so the 1917 viniyogas (e.g. asya śrīcaṇḍīkavacasya brahmā ṛṣiḥ…) were dropped along with their glosses (recoverable from git).

- A Leave them out, as in Gita Press.
- B Restore the 1917 viniyogas above each aṅga, marked as from the 1917 print.

**Recommended.** A, since the request was to follow Gita Press; B if you recite with them.

**Decision:** 

---

### 2. [saptashati-01](../../../stotra/devi/saptashati-01-iast.html) · unit 83 · text
<!-- id: saptashati-01:83:text:d97107 -->

> lajjā puṣṭistathā tuṣṭistvaṃ śāṃtiḥ kṣāṃtireva ca  
> khaḍginī śūlinī ghorā gadinī cakriṇī tathā  ‖ 80 ‖  
>
> <sub>lajjā = Shame · puṣṭiḥ = Nourishment · tathā = so · tuṣṭiḥ = Contentment · tvam śāṃtiḥ = you Peace · kṣāṃtiḥ = Patience · eva ca = also · khaḍginī = sword-bearer · śūlinī = trident-bearer · ghorā = terrible · gadinī = mace-bearer · cakriṇī = discus-bearer · tathā = so</sub>

**Issue.** 1.80: Gita Press prints khaṅginī (खङ्गिनी); the site kept khaḍginī as a spelling of the same word.

- A Keep khaḍginī.
- B Take khaṅginī as printed.

**Recommended.** A: the same word, and khaḍga is how every other place spells it.

**Decision:** 

---

### 3. [saptashati](../../../stotra/devi/saptashati-iast.html) · whole page · source
<!-- id: saptashati:0:source:bb26e5 -->

**Issue.** Gita Press marks many readings with footnotes (पा॰, e.g. 9.37, 12.22, 13.23) giving alternatives, often the 1917 reading. These footnotes were not transcribed.

- A Leave as is; gitapress.tsv already lists the 1917 readings.
- B Transcribe the Gita Press footnotes into gitapress.tsv as a further column.

**Recommended.** A.

**Decision:** 

---

### 4. [saptashati](../../../stotra/devi/saptashati-iast.html) · whole page · source
<!-- id: saptashati:0:source:82eb0d -->

**Issue.** Gita Press also contains matter that is not on the site: Devyatharvaśīrṣa, the Tantric Rātri and Devī Sūktas, the navārṇa nyāsa and procedure, Siddhakuñjikā, Durgā-dvātriṃśannāmamālā, Devyaparādhakṣamāpana and the other closing hymns.

- A Leave the site's scope as it is.
- B Add some or all of these as further pages from the same PDF.

**Recommended.** A for now; B is a separate piece of work.

**Decision:** 

---

### 5. [saptashati-uttara](../../../stotra/devi/saptashati-uttara-iast.html) · whole page · text
<!-- id: saptashati-uttara:0:text:c79e8b -->

**Issue.** Gita Press prints three passages in brackets, which suggests they are interpolations: Vaikṛtika 28 (balimāṃsādipūjeyaṃ…), Mūrti 11 (bhuktvā bhogān yathākāmaṃ…) and the three lines after Mūrti 25 (etasyāstvaṃ prasādena…). They are included, in brackets.

- A Keep them, in brackets, as Gita Press prints them.
- B Drop them.

**Recommended.** A.

**Decision:** 

---

## Fixed in the review

| Page | Unit | Area | Issue | Change |
|---|---|---|---|---|
| saptashati-01 | — | source | The user asked for the Saptaśatī to follow the Gita Press Śrīdurgāsaptaśatī (code 118) as the authentic reference; the site followed the 1917 Nirṇaya Sāgara print and had deliberately kept its ~80 variants (tools/saptashati/gitapress.tsv). | All 13 chapters now carry the Gita Press readings and half-verse division, keeping the site's anusvāra spelling where words agree; each change checked on the PDF page image where the font decoding was doubtful. Colophon check passes for all 13; running total ७००. gitapress.tsv now lists the replaced 1917 readings. |
| saptashati-02 | — | text | Gita Press lacks 2.20's half-verse tato devā daduḥ… and has kabandhā yuyudhurdevyā gṛhītaparamāyudhāḥ at 2.63; 2.55–63 pair their half-verses differently. | Structure and readings now as in Gita Press (pp. 79, 84–86); śyenānukāriṇaḥ for senānukāriṇaḥ. |
| saptashati-10 | — | text | Gita Press lacks 10.18's aśvāṃśca pātayāmāsa rathaṃ sārathinā saha and adds jajvaluścāgnayaḥ śāntāḥ śāntā digjanitasvanāḥ as 10.32. | As in Gita Press (pp. 156–158), with its closing oṃ. |
| saptashati-13 | — | text | Gita Press numbers the end of chapter 13 as 27 (half), 28 (verse), 29 (half) and repeats the closing verse unnumbered with klīṃ oṃ; its colophon counts are uvāca 6, ardha 11, śloka 12 (1917: 6, 7, 16). | As in Gita Press (p. 182); the repeat is an unnumbered line; the colophon counts are updated and check.py passes. |
| saptashati-08 | 7 | text | 8.6: the earlier collation recorded Gita Press as maurvāḥ, but code 118 prints mauryāḥ (p. 135). | mauryāḥ, kālakeyāḥ as printed in code 118. |
| saptashati-01 | — | text | Chapter heads: Gita Press gives a viniyoga for each carita and a dhyāna before every chapter; the site had the 1917 viniyogas, a full dhyāna only for chapter 1 and cues for 2 and 5. | Viniyogas (chapters 1, 2, 5) and all 13 dhyānas now as in Gita Press, with word glosses for each. |
| saptashati-purva | — | text | Kavaca, Argalā and Kīlaka are a different recension in Gita Press: Kavaca 56 verses (1917: 50), Argalā 25 (23), many readings and some verse order differ. | Re-keyed from Gita Press pp. 19–39 (verses, order, numbering, colophons); our spelling kept where words agree; glosses carried over and the new or changed verses glossed. |
| saptashati-uttara | — | text | The three Rahasyas differ in Gita Press: Prādhānika 31 verses (29), Mūrti 25 (22) plus three closing lines in brackets, and many readings. | Re-keyed from Gita Press pp. 192–213, bracketed lines included in brackets; glosses carried over and the new or changed verses glossed. |
| saptashati-01 | — | words | Word glosses are keyed by verse position; regrouped half-verses, new dhyānas and changed readings left glosses misplaced or wrong. | Glosses re-mapped to the new verse positions by text alignment; every verse whose text changed was checked and corrected by hand (all 15 pages: 912/912 glossed). |
| saptashati | — | wiring | Note, footer, README and index described the text as the 1917 print. | Generator note/footer, README, index and SOURCES §5.26 now name Gita Press as the reference text (the sūkta page keeps its 1917/Ṛgveda footer). |
