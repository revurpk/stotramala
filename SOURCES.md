<!-- Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE) -->
# Sources and provenance

Every external material used in this repository is recorded here before
it ships: origin, date recorded, license, and exactly what was changed.
Silent emendation is not permitted — every departure from the received
text appears in the tables below.

---

## 1. Śrī Durgā Saptaślokī

### 1.1 The work

The Saptaślokī ("seven verses") is a short devotional selection drawn
from the **Durgā Saptaśatī** (*Devī Māhātmya*), itself a section of the
**Mārkaṇḍeya Purāṇa**. The composition is ancient and in the **public
domain**. It circulates with a traditional frame — a question by Śiva,
the Devī's reply — and a *viniyoga* naming Nārāyaṇa as ṛṣi, anuṣṭubh as
the metre, and Mahākālī, Mahālakṣmī and Mahāsarasvatī as the deities.

### 1.2 Electronic transcription

| Field | Value |
|---|---|
| Origin | `https://shlokam.org/shloka/sri-durga-sapta-shloki.htm` |
| Recorded | 2026-07-23 |
| Obtained via | Maintainer's local note file (`Sri Sapta Shloki Durga.md`) |
| Stated license | **None stated on the page** |
| Used for | Romanized Sanskrit text only |

**Licensing analysis.** The underlying verses are public domain by age.
The site publishes a romanized transcription but asserts no explicit
licence, and offers no statement about reuse. Per the sourcing rule in
`README.md` §5, this doubt is recorded rather than ignored:

> **Unresolved.** A bare transcription of a public-domain text into
> Roman script is unlikely to attract fresh copyright in most
> jurisdictions (it is a mechanical rendering, not an original work).
> That reasoning is *not* a substitute for permission. **Commercial
> redistribution of this stotra is blocked** until either (a) the text
> is re-keyed against a public-domain print edition of the Durgā
> Saptaśatī, or (b) explicit permission is obtained. Non-commercial
> personal use is unaffected.

The English translations and all editorial matter are **original work by
the maintainer**, not derived from the source page, and are released
under CC BY 4.0.

### 1.3 Corrections applied to both editions

Typographic damage in the received transcription. Both are artifacts of
an ITRANS-style scheme in which capital `C` encodes छ, surviving into
display text where it reads as a stray capital.

| # | Received | Corrected | Justification |
|---|---|---|---|
| 1 | `anuṣṭup Chandaḥ` | `anuṣṭup chandaḥ` | छन्दः — stray capital mid-phrase; छ is `ch` in IAST |
| 2 | `prayachChati` | `prayacchati` | प्रयच्छति — stray capital mid-word; च्छ is `cch` in IAST |

### 1.4 Normalization applied to the `-iast` edition only

The source romanization is **not strict IAST**: it marks `ē`/`ō` (an
ISO 15919 / South-Indian convention; in Sanskrit *e* and *o* are always
long and take no macron) and writes च as `ch` (IAST reserves `ch` for
छ). The `-iast` edition normalizes this. The `-original` edition
preserves the source reading.

| # | Class | Source | Strict IAST | Instances |
|---|---|---|---|---|
| 1 | Vowel | `ē` | `e` | *dēvī → devī*, *durgē → durge*, *tē → te*, … |
| 2 | Vowel | `ō` | `o` | *mōhāya → mohāya*, *namō'stu → namo'stu*, … |
| 3 | Consonant | `ch` (= च) | `c` | *chētāṃsi → cetāṃsi*, *sadārdrachittā → sadārdracittā* |
| 4 | Consonant | `ḻ` (= ळ) | `ḷ` | *mahākāḻī → mahākāḷī*, *maṅgaḻa → maṅgaḷa* |
| 5 | Punctuation | `।` `॥` | `\|` `\|\|` | daṇḍa and double daṇḍa, incl. verse numbers |

Note that `uvāca` was already strict IAST in the source and is
unchanged.

### 1.5 Editorial emendation, `-iast` edition

| # | Received | Emended | Justification |
|---|---|---|---|
| 1 | `gaurī` (v. 3) | `gauri` | Vocative singular of *gaurī* is **short** *-i* (Pāṇini 7.3.107, *ambārthanadyor hrasvaḥ*). The verse addresses the Goddess in a string of vocatives — *śaraṇye tryambake gauri nārāyaṇi* — where every neighbour is correctly short. The source's long *ī* is a nominative form in a vocative slot. |

Applied at the maintainer's direction. The `-original` edition retains
`gaurī` as received.

### 1.6 Word division (*padaccheda*), `-iast` edition

The `-iast` edition separates the compounds and sandhi-joined words of
the received text with spaces and hyphens, so a reader can see where
one word ends and the next begins. This is a **presentational reading
aid, not a change to the text**: no syllable is added, removed, or
altered, and the recited sound is unchanged. Hyphens mark joins where
a space would misrepresent the sandhi; `pronunciation.html` tells the
reader to run the words together when reciting. The `-original`
edition keeps the received continuous spelling.

Three divisions were corrected after review:

| # | First split as | Corrected to | Reason |
|---|---|---|---|
| 1 | `mati matīva` (v. 2) | `matim atīva` | The compound is *matim* (acc. sg. of *mati*) + *atīva*, "an exceedingly auspicious mind". The first division dropped the *-m* and left *matīva*, which is not a word. |
| 2 | `hyā śrayatāṃ` (v. 6) | `hy-āśrayatāṃ` | The join is *hi* + *āśrayatām*; the *ā-* belongs to the stem *āśraya*, "refuge". The first division cut inside the stem, yielding two non-words and losing the sense the translation rests on. |
| 3 | `snehenāpi ambāstutiḥ` | `snehenāpy-ambāstutiḥ` | Correct as *padaccheda*, but undoing the sandhi *api + ambā → apy ambā* lengthens the pāda from eight syllables to nine and breaks the anuṣṭubh. The hyphen shows the join without altering what is chanted. |

Correction 3 is the reason hyphens, not spaces, are used wherever
separating the words would change the syllable count — the same
convention already applied in *balād-ākṛṣya*, *tvad-anyā*,
*bhayebhyas-trāhi*, and *trailokyasy-ākhileśvari*.

### 1.7 The ॐ glyph

The `-iast` edition opens with the Devanagari **ॐ** rather than a
romanized *oṃ*, at the maintainer's direction: it functions as a sacred
emblem rather than as running text. It relies on the platform's own
Devanagari font.

### 1.8 Devanāgarī and Telugu rendering, `-iast` edition

The `-iast` page offers a script selector (IAST / देवनागरी / తెలుగు).
The IAST verse text in the markup is the **single source of truth**;
the Devanāgarī and Telugu are generated from it in the browser at the
moment of switching, so the three scripts cannot drift and no
alternate spelling is stored by hand. With scripting off, the page
stays on IAST.

The transliteration path is IAST → Telugu → Devanāgarī, using a copy of
teltools.js inlined into the page (see §3). Two adjustments are applied
around the library call, matching this repository's conventions:

  * the reading-hyphens (§1.6) are dropped and our retroflex `ḷ` (ळ/ళ)
    is passed to the library as its `ḻ`, so `mahā-kāḷī` renders
    महाकाळी / మహాకాళీ, not the vocalic-*l* form;
  * `|` `||` become the daṇḍas । ॥, `'` becomes the avagraha ऽ / ఽ,
    and verse numbers are shown in native digits (॥ १ ॥ / ॥ ౧ ॥).

Devanāgarī uses the reader's platform Devanagari font (Kohinoor on
iOS/macOS, Nirmala UI on Windows, Noto as a named fallback). Telugu is
set in **Baloo Tammudu 2**, embedded in the page (§2), because the
platform fallbacks render some three-consonant conjuncts (e.g. the
*try-* stack in *tryambake* → త్ర్య) with visible viramas rather than
the conventional stacked vattu form; Baloo Tammudu 2 forms them
correctly. The font is embedded, not fetched, so the page stays
self-contained; if it fails to load the Telugu falls back to the
platform face.

---

## 2. Fonts

Latin/IAST text uses a system serif stack (Iowan Old Style, Palatino
Linotype, Palatino, Book Antiqua, Georgia, Times New Roman) with a
generic `serif` fallback; Devanāgarī uses the platform's default
Devanagari face. These are **not bundled and not fetched**.

One font is bundled:

| Field | Value |
|---|---|
| Font | Baloo Tammudu 2 (Telugu), weight 400 |
| Where | embedded in `stotra/durga-saptashloki-iast.html` as a base64 `woff2` in an `@font-face` rule |
| Origin | Google Fonts (`fonts.google.com/specimen/Baloo+Tammudu+2`); the upstream project is `github.com/EkType/Baloo2` |
| Recorded | 2026-07-24 |
| Subset | the Sanskrit-in-Telugu character set — every Telugu consonant, vowel, sign, mark and digit Sanskrit uses, plus space and the daṇḍas; 47,696-byte woff2 |
| Regenerated by | `tools/regen-telugu-font.py` (stdlib only; re-fetches and re-embeds) |
| License | **SIL Open Font License 1.1**, © 2019 The Baloo 2 Project Authors — text vendored at `fonts/BalooTammudu2-OFL.txt` |
| Used for | rendering the Telugu script on the `-iast` page (§1.8) |

The OFL 1.1 explicitly permits embedding the font in a document and its
bundling and sale as part of a larger work; the font may not be sold on
its own. The font is embedded, **never fetched at read time**, so the
page remains self-contained and offline. It is not relicensed — it
keeps the OFL, whose text travels with the repository.

## 3. Bundled code

| Field | Value |
|---|---|
| Code | teltools.js, inlined into `stotra/durga-saptashloki-iast.html` inside a `<script>` block |
| Origin | `github.com/revurpk/teltools` (the maintainer's own project), `js/teltools.js`, 12,660 bytes |
| Recorded | 2026-07-24 |
| License | **Apache-2.0**, © 2026 Pradyumna Revur (retained; the SPDX header and copyright are kept intact in the inlined copy) |
| Used for | IAST → Telugu → Devanāgarī transliteration on the `-iast` page (§1.8) |

`teltools.js` is a pure-JavaScript, dependency-free transliterator. It
is **inlined** into the page — not a sibling file and never fetched from
a network — so the page remains a single self-contained file. It is the
maintainer's own Apache-2.0 work; Apache-2.0 is a permissive licence and
its inclusion alongside the CC BY 4.0 repository content is compatible.
The inlined copy keeps its own licence and header — it is **not**
relicensed under CC BY 4.0.

No other libraries, frameworks, or third-party scripts are used.

## 4. Icon artwork

`icon.svg`, `apple-touch-icon.png`, `icon-512.png` and `favicon-32.png`
are **original work by the maintainer**, released under CC BY 4.0 with
the rest of the repository. The mark is a mālā of twelve beads — the
larger *meru* bead at the bottom — constructed from plain circles on
the repository's own palette (`#9a2f1f` on `#f7f1e6`). No third-party
artwork, icon set, glyph, or font is used or embedded: the beads are
geometry, not a typeset character, so nothing about the icon depends on
an external asset or licence.

All four files are generated from a single geometry definition, so the
raster and vector forms cannot drift apart.

## 5. Śrī Śaṅkara stotras (deity folders)

Works traditionally attributed to Ādi Śaṅkara (8th c. CE), added under
`stotra/<deity>/`. Each is generated by `tools/build_stotra.py` from the
shared Durgā shell plus a data file in `tools/stotras/`, so every page
stays single-source and self-contained. The **Sanskrit text is ancient
and public domain**; it is keyed from Sanskrit Wikisource and converted
to IAST by the maintainer's own teltools (`dev2iast`, §3), then daṇḍas,
digits and the avagraha are normalised to the repository's IAST
convention. **All translations are original work by the maintainer**
(CC BY 4.0), not taken from any source.

Sanskrit Wikisource text is contributed under CC BY-SA; a bare
transcription of a public-domain text attracts no new copyright, so the
verses are used as public domain, with the page cited for traceability.

### 5.1 Gaṇeśa Pañcaratnam — `stotra/ganesha/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *गणेशपंचरत्न स्तोत्रम्* | 
| URL | `sa.wikisource.org/wiki/गणेशपंचरत्न_स्तोत्रम्` |
| Recorded | 2026-07-24 |
| Text status | public domain (ancient) |
| Content | 5 verses + phala-śruti |

**Emendation:** verse 3, the Wikisource reading `समस्त लोकसंकरं`
(*saṃkaraṃ*, "mixing") is emended to `लोकशंकरं` (*śaṃkaraṃ*, "doer of
good to the worlds"), the standard reading and the one the sense
requires; the source spelling is a likely OCR error. Logged here per the
no-silent-emendation rule.

### 5.2 Nirvāṇa Ṣaṭkam (Ātma Ṣaṭkam) — `stotra/advaita/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *निर्वाणषट्कम्* |
| URL | `sa.wikisource.org/wiki/निर्वाणषट्कम्` |
| Recorded | 2026-07-24 |
| Text status | public domain (ancient) |
| Content | 6 verses |

Filed under `advaita/` rather than a deity: it is a hymn to the Self,
not addressed to a deity, though its refrain is *śivo'ham* ("I am
Śiva"). No emendations.

### 5.3 Achyutāṣṭakam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *अच्युताष्टकम् (मूलसहितम्)* — mūla verses only |
| URL | `sa.wikisource.org/wiki/अच्युताष्टकम्_(मूलसहितम्)` |
| Recorded | 2026-07-24 |
| Text status | public domain (ancient) |
| Content | 8 verses + phala-śruti (v. 9) |

Only the mūla (root) verses are taken; the page's commentary is not
used. No emendations.

### 5.4 Kanakadhārā Stotram — `stotra/devi/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *कनकधारास्तोत्रम्* |
| URL | `sa.wikisource.org/wiki/कनकधारास्तोत्रम्` |
| Recorded | 2026-07-24 |
| Text status | public domain (ancient) |
| Content | 22 verses + closing colophon |

**Normalisations** (Hindi-style nukta → Sanskrit, and a standard
reading), logged per the no-silent-emendation rule:

| # | Source | Used | Note |
|---|---|---|---|
| 1 | `तड़ित्` / `गरुड़` (with nukta ड़) | `तडित्` / `गरुड` (ड) | ड़ is a Hindi letter; the Sanskrit words use plain *ḍa* |
| 2 | `कैटाभारेर्` (v. 5) | `कैटभारेर्` | *kaiṭabha-ari*, "foe of Kaiṭabha"; the long *ā* is a source typo |

The daṇḍa falls after the second pāda of each verse (as in the source),
not after every pāda.

### 5.6 Śiva Mānasa Pūjā — `stotra/shiva/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *शिवमानसपूजा* |
| URL | `sa.wikisource.org/wiki/शिवमानसपूजा` |
| Recorded | 2026-07-25 |
| Text status | public domain (ancient); attributed to Ādi Śaṅkara |
| Content | 5 verses (four upacāra verses + the kṣamā verse) |

**Recension.** The canonical five-verse form is used: the four
mental-offering verses (Śārdūlavikrīḍita) and the closing kṣamāpaṇa
verse *karacaraṇakṛtaṃ* (Mālinī). The Wikisource copy additionally
carries an optional phala-śruti verse (*ityevaṃ harapūjane…*), whose
wording varies across sources; it is **omitted** here as a non-standard
addition rather than reproduced with its variant readings. No other
emendations. The daṇḍa falls after each pāda, as in the source.

### 5.7 Madhurāṣṭakam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *मधुराष्टकम्* (Vallabhācārya) |
| URL | `sa.wikisource.org/wiki/मधुराष्टकम्` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | 8 verses |

| # | Source | Used | Note |
|---|---|---|---|
| 1 | `वेणर्` (v. 3) | `वेणुर्` | *veṇur* ("the flute"); the source drops the *u*-mātrā — a typo |

### 5.8 Liṅgāṣṭakam — `stotra/shiva/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *लिङ्गाष्टकम्* |
| URL | `sa.wikisource.org/wiki/लिङ्गाष्टकम्` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | 8 verses + phala verse |

Orthography normalised to standard Sanskrit (the e-text carries
Hindi-influenced spellings): anusvāra → class nasal before stops
(*कुमकुम→कुङ्कुम*, *पंकज→पङ्कज*, *संचित→सञ्चित*, *वंदित→वन्दित*), and
typo fixes (*प्रवारार्चित→प्रवरार्चित*, *बुद्धी→बुद्धि*, *कोटी→कोटि*,
*देवागण→देवगण*, *अष्टोदलोपरी→अष्टदलोपरि*, *परामात्मक→परमात्मक*). No word
added or dropped.

### 5.9 Bilvāṣṭakam — `stotra/shiva/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *बिल्वाष्टकम्* |
| URL | `sa.wikisource.org/wiki/बिल्वाष्टकम्` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | 8 verses + phala verse (the eight sacred leaves) |

The Wikisource e-text abbreviates the refrain (*एक…*) after v. 1; it is
filled with the full **एकबिल्वं शिवार्पितम्** shown in vv. 1 and 8. The
e-text is otherwise loose; readings are normalised to the standard
recitation, notably v. 3 (*बिल्ववृक्षैश्च→बिल्ववृक्षस्य*), v. 6
(*महादेवैश्च पूजार्थ→महादेवस्य पूजार्थम्*), and v. 7 (the corrupt
*गयाप्रयागमे दृष्ट्वा→प्रयागे माधवं दृष्ट्वा*). These are documented, not
silent.

### 5.10 Mahālakṣmī Aṣṭakam — `stotra/devi/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *श्रीमहालक्ष्म्यष्टकम्* (from the Padma Purāṇa) |
| URL | `sa.wikisource.org/wiki/श्रीमहालक्ष्म्यष्टकम्` |
| Recorded | 2026-07-25 |
| Text status | public domain (ancient) |
| Content | 8 verses + 3 phala-stuti verses |

The e-text is rough; readings normalised to the standard recitation:

| # | Source | Used | Note |
|---|---|---|---|
| 1 | `सर्वसुष्ट` (v. 3) | `सर्वदुष्ट` | *sarva-duṣṭa*, "all the wicked" — typo |
| 2 | `शूल सूक्ष्म` (v. 6) | `स्थूलसूक्ष्म` | *sthūla-sūkṣma*, "gross and subtle" — the standard pair |
| 3 | `जगन्मातार्` (vv. 7–8) | `जगन्मातर्` | vocative sandhi *jaganmātar*; the long *ā* is a typo |
| 4 | `राज्य प्राप्तेति` (v. 9) | `राज्यं प्राप्नोति` | corrupt → the standard reading |
| 5 | `महाशत्रुं` (v. 11) | `महाशत्रु` | stray anusvāra removed |

### 5.11 Subrahmaṇya Bhujaṅgam — `stotra/subrahmanya/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *सुब्रह्मण्यभुजङ्गम्* (Ādi Śaṅkara), raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=सुब्रह्मण्यभुजङ्गम्&action=raw` |
| Recorded | 2026-07-25 |
| Text status | public domain (ancient) |
| Content | 33 verses (Bhujaṅgaprayāta metre; v. 33 is the phala) |

Long hymns are fetched as **raw wikitext** — WebFetch's summariser
truncates or declines them, so the raw MediaWiki `action=raw` endpoint is
used and the verses read verbatim. The e-text is rough; readings
normalised to standard Sanskrit, e.g. v5 `स्थैव→स्तथैव` & `पङ्गक्ती→पङ्क्ती`,
v8 `लसत्वर्ण→लसत्स्वर्ण`, v11 `काशमीर→काश्मीर`, v15 `अजस्त्रं→अजस्रं`,
v22 `पार्थये→प्रार्थये` & `क्षमोहं→क्षमोऽहं`, v24 `दुतं→द्रुतं`,
v25 `कुष्ट→कुष्ठ` & `ज्वरन्मादि→ज्वरोन्मादि`. Verse 1 is the customary
Gaṇeśa maṅgala invocation prefacing the hymn.

### 5.12 Mukunda Mālā — `stotra/vishnu/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *मुकुन्दमाला* (Kulaśekhara), raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=मुकुन्दमाला&action=raw` |
| Recorded | 2026-07-25 |
| Text status | public domain (ancient) |
| Content | 40 verses + an opening dedicatory verse to King Kulaśekhara |

Fetched as raw wikitext and parsed into verse halves. The opening
verse (*ghuṣyate yasya nagare…*) praises the poet-king and is shown
unnumbered before the hymn. No emendations.

### 5.13 Rāma Rakṣā Stotram — `stotra/rama/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *रामरक्षास्तोत्रम्* (Budha Kauśika), raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=रामरक्षास्तोत्रम्&action=raw` |
| Recorded | 2026-07-25 |
| Text status | public domain (ancient) |
| Content | 38 verses (the viniyoga and dhyāna preamble prose are omitted) |

Rough OCR readings normalised: v5 `ध्रुशौ→दृशौ`, v7 `ह्र्दयं→हृदयं`,
v18 `फ़लमूल→फलमूल` & `ब्रम्ह→ब्रह्म`, v30 `स्वामि→स्वामी`, v33
`जितेद्रियं→जितेन्द्रियं` & `दुद्धिमतां→बुद्धिमतां`, v37
`दासोऽस्मयं→दासोऽस्म्यहं`, and v3/v4 minor sandhi/typo fixes. New
`stotra/rama/` deity folder.

### 5.14 Mahiṣāsura Mardinī Stotram — `stotra/devi/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *महिषासुरमर्दिनी स्तोत्रम्* (attrib. Rāmakṛṣṇa Kavi), raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=महिषासुरमर्दिनी_स्तोत्रम्&action=raw` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | 21 verses; the identical closing refrain (`jaya jaya he mahiṣāsuramardini…`) is used uniformly, fixing per-verse number/ZWJ debris in the e-text |

This hymn's dense alliteration, rare epithets, and drum/dance
onomatopoeia make a literal rendering impossible in places; the
translations give the clear sense and paraphrase the sound-play, and the
page carries a `note` saying so. Compound-hyphens from the source are
kept in the IAST as reading aids (dropped for the native scripts at
render time).

### 5.15 Bhaja Govindam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Work | *Bhaja Govindam* / *Dvādaśamañjarikā* (*Moha Mudgara*), 33 verses |
| Author | Ādi Śaṅkarācārya (12-verse core), with disciples' verses |
| Source | Sanskrit Wikisource, *भजगोविन्दम्*, raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=भजगोविन्दम्&action=raw` |
| Recorded | 2026-07-27 |
| Text status | public domain |
| Content | opening refrain + 12 mañjarikā verses + colophon (12a) + disciples' verses 13–33; IAST via the teltools `dev2iast` port |

**On the choice of source.** The maintainer supplied a scanned PDF of
this text from a copyrighted study-notes collection (the same "Vedanta
Students" set used for the Vedānta Ḍiṇḍima, §7). Because Bhaja Govindam
is a canonical text available *clean and public-domain* on Sanskrit
Wikisource, it was keyed from there instead — so, unlike §7, **this page
carries no commercial-redistribution restriction.**

**Editorial notes (no silent emendation).** The recited Hare-Kṛṣṇa
mahāmantra that the Wikisource copy prepends is **omitted** (it is not
part of Śaṅkara's composition). Compound-internal spaces in the source
were closed up (cosmetic; the transliterator ignores them). The
Wikisource copy also carries a run of small OCR/typing errors, each
corrected against the universally-attested standard text:

| Verse | Wikisource | Corrected |
|---|---|---|
| 3 | मांसावसादि; मागामोहावेशम् | मांसवसादि; मा गा मोहावेशम् |
| 5 | सक्तः **स्**तावन्निज | सक्तः तावन्निज (stray initial स्) |
| 9 | निस्**स्**ङ्गत्वं | निस्सङ्गत्वं (malformed cluster) |
| 12a | उपदेशो भूद्; श्रीमच्छ**न्**कर | उपदेशोऽभूद्; श्रीमच्छङ्कर |
| 13 | सज्जनसं गति; गतिर**ै**का | सज्जनसंगति; गतिरेका |
| 14 | पश्यन्नपि **चन** | पश्यन्नपि च न |
| 15 | **जतं** | जातं |
| 17 | ज्ञानवि**हि**नः | ज्ञानविहीनः |
| 29 | विहि**आ** | विहिता |
| 31 | भ**कतः** | भक्तः |
| 32 | श्रीमच्छ**म्**कर; आ**सि**च् | श्रीमच्छङ्कर; आसीच् |

Translations are **original work by the maintainer**, written from the
Sanskrit.

### 5.16 Gaṇapati Atharvaśīrṣa — `stotra/ganesha/`

| Field | Value |
|---|---|
| Work | *Gaṇapati Atharvaśīrṣa* (*Gaṇeśa Upaniṣad*), Atharvan tradition |
| Source | Sanskrit Wikisource, *गणपत्यथर्वशीर्षम्*, raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=गणपत्यथर्वशीर्षम्&action=raw` |
| Recorded | 2026-07-27 |
| Text status | public domain |
| Content | opening śānti-pāṭha, 14 numbered mantras (with the Gaṇeśa mantra, Gāyatrī, and dhyāna), closing śānti-mantra; IAST via the teltools `dev2iast` port |

Prose-mantra Upaniṣad, so the daṇḍas are shown inline (`।`/`॥`) and the
fourteen mantras carry their traditional numbers; the two śānti-pāṭhas
are unnumbered blocks set off by ornaments, and the section labels
(Gaṇeśa mantra, Gāyatrī, dhyāna, phalaśruti…) are folded into the
translations. This text carries **no Vedic svara accents** (it is
conventionally recited unaccented). Editorial notes (no silent
emendation): two source typos corrected — v4 वाङ्ग्मय → वाङ्मय, v6
स्थिथोऽसि → स्थितोऽसि; and the parenthetical variant *(vadiṣyāmi)* after
*vacmi* (v2) is dropped in favour of the primary reading. Translations are
**original work by the maintainer**.

### 5.17 Īśāvāsya Upaniṣad — `stotra/advaita/`

| Field | Value |
|---|---|
| Work | *Īśāvāsya* (*Īśa*) *Upaniṣad*, 18 mantras — closing chapter of the Śukla-Yajurveda Vājasaneyi Saṃhitā |
| Source | Sanskrit Wikisource, *ईशोपनिषत्*, raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=ईशोपनिषत्&action=raw` |
| Recorded | 2026-07-27 |
| Text status | public domain |
| Content | pūrṇam-invocation (opening and closing), 18 mantras between ornaments; IAST via the teltools `dev2iast` port |

Placed under the **Advaita** grouping as core Vedānta scripture (with the
Nirvāṇa Ṣaṭkam and Vedānta Ḍiṇḍima). The Wikisource copy carries **no
Vedic svara accents**. Handling notes (no textual emendation): the Vedic
anunāsika candrabindu (ँ, e.g. *idaṁ*, *śataṁ*) is rendered **ṁ** in the
IAST and collapses to the common anusvāra (ं) in the Devanāgarī at render
time; source line-break hyphens (v8, v16) were joined; and the source's
anusvāra spelling of *śānti* (शांति) is written in the conventional
*śānti* (शान्ति) form. Translations are **original work by
the maintainer**.

### 5.18 Puruṣa Sūktam (accented) — `stotra/veda/`

| Field | Value |
|---|---|
| Work | *Puruṣa Sūkta*, Ṛgveda 10.90 (Nārāyaṇa, to Puruṣa), 16 ṛcs |
| Source | Sanskrit Wikisource, *ऋग्वेदः सूक्तं १०.९०* (Sāyaṇa edition), raw wikitext |
| URL | `sa.wikisource.org/w/index.php?title=ऋग्वेदः सूक्तं १०.९०&action=raw` |
| Recorded | 2026-07-27 |
| Text status | public domain |
| Content | the **accented saṃhitā** (16 ṛcs), extracted from the pratīka lines and transliterated to IAST-with-svara-markers |

First page to carry **Vedic svara accents**. The accented saṃhitā on the
source page is the clean, correct text (e.g. *atyatiṣṭhad daśāṅgulam*,
*viṣvaṅ vyakrāmat*) — unlike the corrupt unaccented *पुरुषसूक्तम्* copy,
which is **not** used. This is the sixteen-ṛc Ṛgvedic form (the
Taittirīya uttaranārāyaṇa continuation is not part of RV 10.90).
Translations are **original work by the maintainer**.

#### Svara pipeline (how accents are stored and rendered)

The IAST source of truth carries the Vedic pitch-accents as two markers
placed **right after the accented vowel**: `_` = anudātta (॒), `^` =
svarita (॑); udātta is unmarked. At render time (shared shell):

- **Devanāgarī** — `devSvara()` transliterates the text up to each marker
  and re-attaches the Devanāgarī sign to the akṣara that ends that chunk
  (a mark always follows a vowel, i.e. a syllable boundary), then
  normalises so a tone mark follows any visarga/anusvāra on its akṣara
  (`॒ः → ः॒`) for correct shaping. Round-trips **byte-exact** to the
  source accented text. Accented pages open in Devanāgarī (`script:"dev"`).
- **Telugu** — `telSvara()` does the same reattachment into Telugu, but the
  Telugu font (Baloo Tammudu 2) has no svara glyphs, so the marks are **drawn
  with CSS** (added 2026-09-28; "improvise where fonts lack support"): each
  accented akṣara is wrapped in a span, and its svarita stroke, dīrgha-svarita
  double stroke or anudātta bar is a pseudo-element placed from the akṣara's
  ink as measured by canvas `measureText` — above the highest ink, below the
  lowest (vattu), centred. The Unicode mark stays in the text at zero size, so
  copy, search and the review mode keep the accented text.
- **IAST** — the markers are dropped (`stripSvara`); an unaccented reading
  aid.

The anunāsika candrabindu (ँ) is written **ṁ** in IAST and renders as
anusvāra in Devanāgarī, as elsewhere on the site. Markers `_`/`^` never
occur in ordinary IAST, so all non-accented pages are unaffected.

### 5.19 Manyu Sūktam (accented) — `stotra/veda/`

| Field | Value |
|---|---|
| Work | *Manyu Sūkta*, Ṛgveda 10.83 (ṛcs 1–7) + 10.84 (ṛcs 8–14), to Manyu |
| Source | Sanskrit Wikisource, *ऋग्वेदः सूक्तं १०.८३* and *…१०.८४* (Sāyaṇa ed.), raw wikitext |
| Recorded | 2026-07-27 |
| Text status | public domain |
| Content | the accented saṃhitā (14 ṛcs), extracted from the pratīka lines |

Uses the svara pipeline (see §5.18). Numbered continuously 1–14 with an
ornament between the two component sūktas. The pluta of 10.84.5
(*anavabravo3'smākam*, वो॒३॒॑) is preserved — the Devanāgarī numeral 3 is
carried as ASCII `3` in the IAST source and shows the tone marks. Where
the source stores a tone mark **before** a visarga/anusvāra (a handful of
places, e.g. *ojaḥ*), the renderer normalises it to the canonical order
(mark after) for correct shaping; the anunāsika ँ renders as anusvāra.
Translations are **original work by the maintainer**.

### 5.21 Viṣṇu Sahasranāmam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Work | *Viṣṇu Sahasranāma Stotram* — Mahābhārata, Anuśāsana-parvan (Bhīṣma to Yudhiṣṭhira) |
| Source | Sanskrit Wikisource, *विष्णुसहस्रनामस्तोत्रम्*, raw wikitext |
| Recorded | 2026-08-09 |
| Text status | verses ancient / public domain; Wikisource page CC BY-SA |
| Content | 7 dhyāna verses, the 108 verses of names, 5 closing verses (120 blocks, 2 ornaments) |

**Provenance chain.** The Wikisource page's own `==स्रोतः==` notes it was
converted from an ITRANS version at sanskritdocuments.org. That is worth
recording plainly. It is *not* the blocked case of §7/Durgā Sūktam: what is
reused here is a bare, unaccented transcription of a Mahābhārata text that is
unambiguously public domain, carrying no editorial layer (no accents, no
commentary, no translation) in which a new copyright could subsist — and it is
taken from Wikisource under CC BY-SA, not fetched from the restricted source.
Translations are **original work by the maintainer**.

**Scope.** The Wikisource page is a full ritual manual. Included here: the
dhyāna, the thousand names, and the closing kṣamā-prārthanā. **Omitted** (with
reason, not silently): the pūrva-/kara-/ṣaḍaṅga-/uttara-nyāsa sections, which
are japa mechanics rather than reading text; the Mahābhārata frame dialogue
(Vaiśampāyana / Yudhiṣṭhira / Bhīṣma); and the Rāma-stuti appendix in
`==उपसंहारश्लोकाः==`, which belongs to Rāma rather than to this stotra.

**Editorial notes.** v43 the source carries a parenthetical variant
*विरजो (or विरतो)*; the primary reading **virajo** is used and the variant
recorded here, unaltered in the source. Round-trip verified with
`scripts/verify.py`: **214 of 216 padas byte-exact**; the two differences are
the v43 parenthetical above and v65 *śrīmāṁllokatrayāśrayaḥ*, where the
source's anunāsika ँ renders as anusvāra ं — the documented `ṁ` collapse
(§5.18), not an error.

**Audio.** Links to a recitation on the official rights-holder channel
(*M.S. Subbulakshmi – Topic*, `ATflA6WOy0I`), verified live via YouTube's
oEmbed endpoint. It is a plain outbound link, never an embed: nothing is
fetched from YouTube when the page is opened, so the page stays self-contained
and no reader is tracked for merely reading.

### 5.22 Lalitā Sahasranāmam — `stotra/devi/`

| Field | Value |
|---|---|
| Work | *Lalitā Sahasranāma Stotram* — Brahmāṇḍa Purāṇa, Uttarakhaṇḍa (Hayagrīva to Agastya) |
| Source | Sanskrit Wikisource, *श्रीललितासहस्रनामस्तोत्रम्*, raw wikitext |
| Recorded | 2026-08-09 |
| Text status | verses ancient / public domain; Wikisource page CC BY-SA |
| Content | the dhyāna verse, the 182 verses of names, the closing verse (184 blocks, 2 ornaments) |

Translations are **original work by the maintainer**.

**Scope.** The nyāsa/viniyoga preamble (ṛṣi, chandas, bīja, śakti, kīlaka) is
**omitted** — japa mechanics rather than reading text, consistent with the
Viṣṇu Sahasranāma page (§5.21). The dhyāna, the thousand names and the closing
verse are included.

**Editorial notes (no silent emendation).** The source carries **thirteen
inline variant readings**, written as `or <word>` after the line. In every case
the primary (in-verse) reading is used and the variant recorded here:
v9 *radanacchadā* / **daśanacchadā**; v11 *nijasallāpa* / **nijasaṃlāpa**;
v12 *cibukaśrī* / **cubukaśrī**; v20 *siñjāna* / **śiñjāna**;
v48 *niḥsaṃśayā* / **nissaṃśayā**; v78 *pāṣaṇḍā* / **pākhaṇḍā**;
v91 *niḥsīma* / **nissīma**; v111 *bandhamocanī* / **mocanī** and
*bandhurālakā* / **barbarālakā** (the latter stands on its own line in the
source and is not part of the verse); v123 *vinodinī* / **vimodinī**;
v131 *ajājaitrī* / **ajājetrī**; v150 *mārtāṇḍa* / **mārtaṇḍa**;
v163 *sudhāsṛtiḥ* / **sudhāsrutiḥ**; v168 *saumyā* / **somyā**.
One OCR split is corrected: the closing line's *nām nāṃ* is read as **nāmnāṃ**.

**Verification.** Round-trip checked with `scripts/verify.py` over all 364
padas: **358 identical**. The remaining six differ only in *word division* —
the source writes a word-final virāma consonant separated from a following
vowel (e.g. `मूलप्रकृतिर् अव्यक्ता`) where the page uses the conventional
joined form (`मूलप्रकृतिरव्यक्ता`). The akṣaras are the same; this is a
presentational difference in the source, not a textual one.

**Audio.** Links to the Ranjani–Gayatri recitation on the artists' own channel
(`zgG-gjioU1g`), verified live via YouTube's oEmbed endpoint. As on all pages,
this is a plain outbound link, never an embed.

### 5.24 Ardhanārīśvara Stotram — `stotra/shiva/`

| Field | Value |
|---|---|
| Source | Sanskrit Wikisource, *अर्धनारीश्वरस्तोत्रम्* (author given as शंकरभगवतः) |
| URL | `sa.wikisource.org/wiki/अर्धनारीश्वरस्तोत्रम्` |
| Recorded | 2026-10-18 |
| Text status | public domain (ancient); attributed to Ādi Śaṅkara |
| Content | 8 verses to Śivā and Śiva in paired epithets (Upajāti), a phalaśruti (9) and the Śaṅkara colophon |

**Editorial notes.** Verse text exactly as on Wikisource (verse 6 reads
*nirīśvarāyai*). The title line `॥ अर्धनारीश्वरस्तोत्रम् ॥` becomes the page
heading. In the colophon the anusvāra before a stop is written as the class
nasal by site convention (*śrīmacchaṃkara-* → *śrīmacchaṅkara-*), and
*sampūrṇam* likewise. No recitation link. Translations and the word-by-word
list (`tools/words/ardhanarishvara-stotram.txt`) are original.
`verify.py --data`: 18/18 padas pass.

### 5.23 Recitation links (all pages)

Every page except one carries an optional **recitation link** in its header
(`"audio"` / `"audio_label"` in the data file, rendered by
`tools/build_stotra.py`). Conventions, and why they matter:

- **Link, never embed.** The link is a plain outbound `<a href>` with
  `target="_blank" rel="noopener noreferrer"`. Nothing is fetched from YouTube
  when the page loads, so pages remain **self-contained** and no reader is
  tracked merely for opening one. Following the link is the reader's choice.
- **Every video ID was verified live** against YouTube's oEmbed endpoint
  (`/oembed?url=…&format=json`) before shipping, which confirms the video
  exists and returns its real title and channel. This matters: an
  unverified/remembered ID is worthless — the first candidate tried during this
  work 404'd. IDs are never written from memory.
- **Preference order** for the source channel: the rights-holder's own or
  official artist channel (e.g. *M.S. Subbulakshmi – Topic*, *Saregama Carnatic
  Classical*, *Ranjani–Gayatri*, *Challakere Brothers Official*, *SP
  Balasubrahmanyam – Topic*), then established devotional labels.
- **Labels are only what the verified title/author supports** — where the
  performer could not be confirmed from the verified metadata, the label names
  the piece rather than guessing a singer.
- **Recension matters.** Puruṣa Sūktam links a *Ṛgveda* recitation, matching
  the RV 10.90 text on the page rather than the commoner Yajurveda liturgical
  form.
- **Known limitation.** These links are checked for existence and title match,
  not audited for the quality or exactness of the recitation, and YouTube
  videos can be taken down later. They are an aid, not part of the text.
- **Vedānta Ḍiṇḍima has no link**: no recitation could be found, only a
  verse-by-verse English lecture series, which would be mislabelled as
  "listen". Left absent rather than misdescribed.

### 5.5 Durgā page moved into `stotra/devi/`

`durga-saptashloki-iast.html` and `-original.html` moved from
`stotra/` to `stotra/devi/` for deity-folder consistency. Their internal
relative paths were adjusted (`../` → `../../`), and a redirect stub was
left at each old top-level path so existing links do not break. The
generator (`tools/build_stotra.py`) reads the `-iast` page as its shared
shell, so its `SHELL` path was updated to the new location.

---

### 5.25 Vālmīki Rāmāyaṇa — `stotra/ramayana/`

| Field | Value |
|---|---|
| Work | Vālmīki Rāmāyaṇa, the seven kāṇḍas |
| Source | Sanskrit Wikisource, `रामायणम्/<kāṇḍa>/सर्गः N` (654 pages, fetched 2026-10-21 through the MediaWiki API, revision ids kept) |
| Recension | the vulgate (northern-southern "standard" text as in the Gita Press and Nirṇaya Sāgara prints): 77 + 119 + 75 + 67 + 68 + 128 + 111 = 645 sargas; Bāla 1 has 100 verses. Not the Baroda critical edition. |
| Text status | ancient and public domain; a bare transcription on Wikisource (CC BY-SA), used as public domain as for §5. The pages were created from 2005 (user Yann); no print edition is named. |

**Pipeline.** `tools/ramayana/fetch.py` (polite: 50 titles a request, 3 s
apart), `tools/ramayana/parse.py` (every layout on the site — `<poem>` with
॥k-s-v॥, `<pre>` with ॥ v॥, Uttara's ।। ७.२.१ ।।, `<br>` runs — reduced to verses),
`tools/ramayana/gen.py` (dev2iast, daṇḍas as | and ||; pages of whole sargas,
up to 150 verses; a contents page per kāṇḍa). Each sarga's colophon is kept as
printed on Wikisource, without its number. The e-text gives no speaker lines
(… uvāca), so none appear.

**Held back.** Ayodhyā 48–88 and Araṇya 14–15 are typed on Wikisource as a
word-split reading aid — sandhi undone and compounds opened (*prabhātāyām tu
śarvaryām*, *rakta akṣau*, *tataḥ daśa ahe atigate*), with slips of their own —
not as the received text. They are not built until re-keyed from a printed
edition.

**Interpolation.** Araṇya 56 is followed on the same page by an interpolated
sarga, labelled ५६अ प्रक्षिप्तः, with its own numbering; it is shown under its
own heading, "Sarga 56A · interpolated (prakṣipta)".

**Repairs to the e-text** (no reading is emended; only markup, numbering and evident typing slips, each listed below):
- wiki indents (`::`) before long-metre lines, inline links to outside notes,
  audio-player text and a reciter's credit (Yuddha 44) are markup, not text — removed;
- zero-width joiners hid three verse numbers in Yuddha 117 — removed;
- Ayodhyā 89–119 were typed with a stray sign (U+093A) through the words and
  with the visarga as a colon; the sign is removed and the colons read as ः.
  The old spelling र्य्य (*sūryya*, *bhāryyā*) is kept as typed;
- ऱ and the short-e sign ॆ, which Sanskrit does not use, are read as र and े
  (Sundara 8, 44; Uttara 95);
- bracketed notes are removed: glosses (*(=सर्प)*), variant readings
  (*(पात्यमानो)*, *(अग्रतः)*), and two one-letter corrections whose intent is
  unclear (Ayodhyā 91 *श्रोतृ(त्र)सुखे*, 116 *प्र(म)मादाभ्युचितां*) — the words are left as typed;
- a verse number inside a line ends the verse there; in Uttara the number is
  sometimes followed by a stray copy of nearby text, which is dropped;
- where the e-text dropped numbers, a block holding exactly two verses' lines
  is split; a duplicated number before a gap, or a stray number between two
  consecutive ones, is read as the missing one;
- Bāla 29's numbers are garbled throughout (25, 2, 25, 25 …) and the sarga is
  numbered by position;
- a gap with nothing to split is kept as printed (a verse missing from the
  e-text).

| Where | Repair |
|---|---|
| Bāla 26 | number 13 between 2 and 4 read as 3 |
| Bāla 28 | second 21 read as 22 |
| Bāla 29 | e-text numbers garbled ([25, 2, 25, 25]…); numbered by position 1–32 |
| Bāla 31 | number 19 after 19 kept as printed |
| Bāla 42 | number 15 between 13 and 15 read as 14 |
| Ayodhyā 7 | bracketed note “(=सर्प)” removed |
| Ayodhyā 9 | bracketed note “(=पृष्ठ-वक्रभागः)” removed |
| Ayodhyā 13 | second 16 read as 17 |
| Ayodhyā 17 | number 16 between 14 and 16 read as 15 |
| Ayodhyā 24 | e-text has no verse 23 (gap kept) |
| Ayodhyā 32 | e-text has no verse 4 (gap kept) |
| Ayodhyā 52 | bracketed note “(महेति!)” removed |
| Ayodhyā 55 | bracketed note “(प्रतिस्रोतःसमागताम् - पा.भे.)” removed |
| Ayodhyā 89 | 40 visargas typed as “:” restored |
| Ayodhyā 90 | 30 visargas typed as “:” restored |
| Ayodhyā 91 | 141 visargas typed as “:” restored |
| Ayodhyā 91 | bracketed note “(त्र)” removed |
| Ayodhyā 92 | 46 visargas typed as “:” restored |
| Ayodhyā 93 | 47 visargas typed as “:” restored |
| Ayodhyā 94 | 48 visargas typed as “:” restored |
| Ayodhyā 95 | 26 visargas typed as “:” restored |
| Ayodhyā 96 | 34 visargas typed as “:” restored |
| Ayodhyā 97 | 31 visargas typed as “:” restored |
| Ayodhyā 98 | 29 visargas typed as “:” restored |
| Ayodhyā 99 | 53 visargas typed as “:” restored |
| Ayodhyā 100 | 116 visargas typed as “:” restored |
| Ayodhyā 101 | 14 visargas typed as “:” restored |
| Ayodhyā 102 | 72 visargas typed as “:” restored |
| Ayodhyā 103 | 64 visargas typed as “:” restored |
| Ayodhyā 104 | 41 visargas typed as “:” restored |
| Ayodhyā 105 | 82 visargas typed as “:” restored |
| Ayodhyā 106 | 44 visargas typed as “:” restored |
| Ayodhyā 107 | 31 visargas typed as “:” restored |
| Ayodhyā 108 | 21 visargas typed as “:” restored |
| Ayodhyā 109 | 72 visargas typed as “:” restored |
| Ayodhyā 110 | 72 visargas typed as “:” restored |
| Ayodhyā 111 | 37 visargas typed as “:” restored |
| Ayodhyā 112 | 40 visargas typed as “:” restored |
| Ayodhyā 113 | 39 visargas typed as “:” restored |
| Ayodhyā 114 | 35 visargas typed as “:” restored |
| Ayodhyā 115 | 44 visargas typed as “:” restored |
| Ayodhyā 116 | 42 visargas typed as “:” restored |
| Ayodhyā 116 | bracketed note “(म)” removed |
| Ayodhyā 117 | 39 visargas typed as “:” restored |
| Ayodhyā 118 | 47 visargas typed as “:” restored |
| Ayodhyā 119 | 33 visargas typed as “:” restored |
| Araṇya 73 | block 41 split into 40–41 (their numbers were dropped) |
| Kiṣkindhā 22 | second 13 read as 14 |
| Kiṣkindhā 24 | second 33 read as 34 |
| Kiṣkindhā 39 | second 8 read as 9 |
| Sundara 8 | 1 × ऱ read as र |
| Sundara 30 | second 34 read as 35 |
| Sundara 44 | 1 × ॆ read as े |
| Yuddha 17 | second 63 read as 64 |
| Yuddha 30 | second 31 read as 32 |
| Yuddha 44 | dropped non-text line “०४४ इन्द्रजिता अदृश्यरूपेण युद्धरङ्गागमनम्” |
| Yuddha 44 | dropped non-text line “Your browser does not support the audio element, b” |
| Yuddha 44 | dropped non-text line “(श्रीराम-हरिसीताराममूर्ति-घनपाठिभ्यां वचनम्)” |
| Yuddha 117 | 1 visargas typed as “:” restored |
| Uttara 6 | dropped stray “धन्ते समरोद्धर्षा ये च तेषां पुरःसराः ।” after ।। ७.६.८ ।। |
| Uttara 9 | dropped stray “त्वं हि सर्वगुणोपेता श्रीः साक्षादिव पुत” after ।। ७.९.९ ।। |
| Uttara 17 | dropped stray “ैव भोगेन च बलेन च ।।” after ।। ७.१७.२५ ।। |
| Uttara 20 | dropped stray “्तम ।” after ।। ७.२०.७ ।। |
| Uttara 22 | bracketed note “(पात्यमानो)” removed |
| Uttara 23 | bracketed note “(प्रहसो)” removed |
| Uttara 24 | block 14 split into 13–14 (their numbers were dropped) |
| Uttara 25 | bracketed note “(अग्रतः)” removed |
| Uttara 26 | dropped stray “भिरुद्भासितवनान्तरे ।” after ।। ७.२६.७ ।। |
| Uttara 26 | dropped stray “स्मि यदवोचस्त्वमेकपत्नीष्वयं क्रमः ।” after ।। ७.२६.४१ ।। |
| Uttara 27 | dropped stray “यामि ज्ञात्वा कालमुपागतम् ।” after ।। ७.२७.२१ ।। |
| Uttara 30 | dropped stray “्वं हि कस्यचित्प्राणिनो भुवि ।” after ।। ७.३०.१२ ।। |
| Uttara 32 | dropped stray “चः श्रुत्वा मन्त्रिणो ऽथार्जुनस्य ते ।” after ।। ७.३२.२८ ।। |
| Uttara 40 | dropped stray “लोके च मामिका ।” after ।। ७.४०.२१ ।। |
| Uttara 49 | bracketed note “(?)” removed |
| Uttara 51 | e-text has no verse 18 (gap kept) |
| Uttara 94 | dropped stray “सोत्तराणि महात्मना ।” after ।। ७.९४.२८ ।। |
| Uttara 95 | 1 × ऱ read as र |
| Uttara 95 | dropped stray “परिषदो मध्ये रामो वचनमब्रवीत् ।” after ।। ७.९५.३ ।। |
| Uttara 110 | dropped stray “ां विशालाक्षीं तव पूर्वपरिग्रहाम् ।” after ।। ७.११०.११ ।। |

### 5.26 Durgā Saptaśatī — `stotra/devi/`

| Field | Value |
|---|---|
| Work | Durgā Saptaśatī (Devī Māhātmya, Mārkaṇḍeya Purāṇa), with its aṅgas |
| Source | *Saptaśatī*, Nirṇaya Sāgara Press, Bombay, Śaka 1839 (1917 CE); "saṃśodhita" by Vāsudeva Śarmā Paṇaśīkara, son of Lakṣmaṇa Śarmā (the editor Wasudev Laxman Shastri Paṇśīkar, d. 1925); published by Tukaram Javaji. Scan: archive.org `SaptashatiNirnayaSagarPress` (306 pages). |
| Recorded | 2026-10-22 |
| Text status | ancient and public domain; the 1917 print is public domain by age (published before 1931; editor died 1925). No digital text was used: the archive.org OCR is unusable. |

**Transcription.** Every line was read from the page images (scan pages
54–74, 105–249, 260–280) into `tools/saptashati/text/`, one file per chapter
or aṅga. The print runs the text on without word breaks; word division and
the half-verse line breaks are ours, the spelling the print's (its
anusvāra for a class nasal — *saṃbhūtā*, *naṃdā* — is kept). Refrains the
print abbreviates (*yā devī… namastasyai°*, *rūpaṃ dehi…°*, and chapter 13's
repeated mantras 28–29) are written out after the forms it spells in full.

**The seven hundred.** The numbering is the print's own, chapter by chapter.
Each chapter's colophon counts its uvāca, ardha (half-verse), tripād and
śloka mantras, the total, and the running total from the start;
`tools/saptashati/check.py` checks every chapter against those counts. All
thirteen agree exactly, and the running total ends at ७०० (104 · 69 · 44 ·
42 · 129 · 24 · 27 · 63 · 41 · 32 · 55 · 41 · 29).

**What the pages include.** Before the text: the Devī Kavaca (50 verses),
Argalā (23) and Kīlaka (14), each with its viniyoga. The three caritas, each
opening with its viniyoga and the print's dhyāna cue. After the text: the
Prādhānika (29), Vaikṛtika (39) and Mūrti (22) Rahasyas. Not yet included:
the navārṇa mantra's nyāsas and procedure (scan 74–105; its last two pages
are damaged in the scan).

**The Vedic sūktas, with svaras** (`saptashati-sukta-iast.html`). The print
gives the Vedic Rātri Sūkta (ṚV 10.127) before the text and the Vedic Devī
Sūkta (ṚV 10.125) after it, both with their svaras (scan 94–95, 250–252),
with their viniyogas. Read against the page images, the print's words and
accent marks agree with the accented Ṛgveda text on Sanskrit Wikisource
(`ऋग्वेदः सूक्तं १०.१२७`, `१०.१२५`; Sāyaṇa's text), whose lines are used — with
its spelling, so *padvanto* where the print writes the anusvāra, and the
kampa numeral १ as the Ṛgveda marks it. The print runs ṛcs together and
numbers its groups (॥१॥, ॥२॥); the page numbers the eight ṛcs. Svaras follow
the site's accented-Vedic convention (§5.18): the page opens in Devanāgarī,
Telugu draws the marks with CSS as on the Mahānyāsam page, IAST omits them.
The Purāṇic Rātri Sūkta (*viśveśvarīṃ jagaddhātrīṃ…*, chapter 1, 71–87) and
the Tantric Devī Sūkta (*namo devyai mahādevyai…*, chapter 5, 9–82) are
passages of the text itself and are read there.

**Checked against Gita Press.** The thirteen chapters were collated in full
against the Gita Press *Śrīdurgāsaptaśatī* (sthūlākṣara mūla, Gorakhpur;
archive.org `kggr-shri-durga-saptashati-sthulaksharair-mudrita-mula-`), a
modern copyrighted edition used only to check readings; none of its text or
Hindi is copied. Every difference was then read again on the 1917 page.
One was our slip and is corrected: 8.6, *maurvāḥ*, which the 1917 print has
and which we had keyed as *mauryāḥ*. The other 83 rows are the editions'
own variants, and the 1917 reading is kept. In 27 of them, Gita Press's own
footnote (पा॰) records a reading; usually it is the 1917 one. The rest
include several places where the two prints divide the half-verses
differently but give the same count, and one where the lines differ
(10.18 and 10.32). All are listed in `tools/saptashati/gitapress.tsv`. The
two prints agree on every chapter total and on the running total of ७००.
The aṅgas and rahasyas have not been collated.

### 5.27 Devī Bhāgavatam — `stotra/devibhagavatam/`

| Field | Value |
|---|---|
| Work | Śrīmad Devī Bhāgavata Mahāpurāṇa: the māhātmya (Skanda Purāṇa, 5 adhyāyas) and the twelve skandhas (318 adhyāyas) |
| Source | Sanskrit Wikisource, `देवीभागवतपुराणम्/स्कन्धः NN/अध्यायः NN` (337 pages, fetched 2026-10-22, revision ids kept); copied there in 2016 from satsangdhara.net ("courtesy Shri Bhide"), which names no edition |
| Checked against | *Śrīmaddevībhāgavatam* with Nīlakaṇṭha's commentary, Khemraj Śrīkṛṣṇadāsa, Śrī Veṅkaṭeśvara Steam Press, Bombay, 1902 — two archive.org scans (Ishwar Ashram Trust, CC0): skandhas 1–4 with the māhātmya, and 7–12 |
| Text status | ancient and public domain; the e-text is used as public domain as for §5 |

**Scan coverage.** The two scans hold the māhātmya, skandhas 1–3, skandha 4
adhyāyas 1–9 (the rest of that volume is handwritten), skandhas 7–10 and
skandha 12 adhyāyas 11–14. Skandha 5 is checked against Gita Press instead
(below). Skandhas 6 and 11, and the uncovered parts of 4 and 12, are the
e-text alone; their contents pages say so.

**Method (option 2: targeted).** `tools/devibhagavatam/parse.py` reads the
e-text and repairs its numbering by logged rules (the Rāmāyaṇa's, §5.25, plus
the e-text's own habits: a number glued to a word, `।। s.a.N ।।`, a colophon or
an adhyāya title set inside the poem, a verse closed by a bare ॥ with its
number dropped, a verse typed twice). Every adhyāya whose numbering stayed
broken was read against the Khemraj scan where the scan reaches it, and one
leaf of each scanned skandha was collated in full as a sample (about 130
verses: māhātmya 1; 1.5.95–112; 2.6.45–56; 3.7.14–25; 4.6.39–46;
7.3.63–7.4.8; 8.8.8–17; 9.8.76–86; 10.7.2–12; 12.12.37–49). The samples found
0–1 e-text slips a leaf except in the māhātmya (about a dozen in 50 verses) and
skandha 8 (five in ten), whose remaining adhyāyas most need a full collation.
Readings of the print are adopted (`tools/devibhagavatam/khemraj.tsv`, applied
by `gen.py`); spelling conventions (anusvāra for a class nasal, doubling) are
not collated. Volume 2 prints Nīlakaṇṭha's commentary in small type between
the verses; only the mūla is read.

Left as the e-text has them (no scan): 5.33 (a verse numbered 1 twice; Gita
Press prints the second as a bracketed passage inside verse 1), 6.1 (no
colophon). 9.20 exists twice on Wikisource with the same text; one copy is used.

**Skandha 5 against Gita Press.** No Khemraj scan reaches skandha 5. So all 35
of its adhyāyas (2,086 verses) were read against the Gita Press edition
(*Śrīmaddevībhāgavata Mahāpurāṇa* with Hindi translation, Gorakhpur, 2010
printing; archive.org `21-devi-bhagavata-with-hindi-translation-vol-1-gitapress-2010`,
leaves 539–730). Each Gita Press leaf was compared on the page image with the
e-text verses that the OCR places on it. Gita Press is a modern copyrighted
edition, so it was used only to correct the e-text's slips: 162 misspelt or
broken words, such as *mathurāṃ* for *madhurāṃ* or *gṛhītvā* for *gahītvā*.
One half-verse the e-text had dropped is restored, 5.31.22's *saukumāryañca
dhairyañca parasparavirodhi yat*, so the adhyāya's verse 22 is no longer
missing. Twelve real variants, where both readings are sound, are kept as
the e-text has them and only listed. Everything is in
`tools/devibhagavatam/gitapress.tsv`, which `gen.py` applies; none of Gita
Press's Hindi is used.

**Readings adopted from the Khemraj print**

| Where | Op | E-text | Print | Leaf |
|---|---|---|---|---|
| Māhātmya.1.1 | head | श्रीदुर्गादेव्यै नमः |  | k1 13 |
| Māhātmya.1.1 | head | श्रीमद्देवीभागवतमाहात्म्यम् |  | k1 13 |
| Māhātmya.1.7 | r | कलावपि वरं त्वत्तो | कलावपि परं त्वत्तो | k1 13 |
| Māhātmya.1.7 | split | सूत उवाच। |  | k1 13 |
| Māhātmya.1.8 | r | तो वक्ष्याम्यशेषतः | तद्वो वक्ष्याम्यशेषतः | k1 13 |
| Māhātmya.1.12 | r | तत्पुरायणं | तत्पुराणं | k1 13 |
| Māhātmya.1.19 | r | पूर्वं यस्य पिता | पूर्वमस्य पिता | k1 13 |
| Māhātmya.1.25 | split | सर्वयज्ञेषु तीर्थेषु |  | k1 13 |
| Māhātmya.1.27 | r | कृतादो बहवो | कृतादौ बहवो | k1 13 |
| Māhātmya.1.34 | r | परस्वदाराहणेतिऽलुब्धाये | परस्वदाराहरणेतिलुब्धा ये | k1 14 |
| Māhātmya.1.34 | r | नवाहज्ञेन | नवाहयज्ञेन | k1 14 |
| Māhātmya.1.38 | r | हैकसिंहासनस्थितम् | हैमसिंहासनस्थितम् | k1 14 |
| Māhātmya.1.50 | r | शूद्रोऽपि शृण्वन्स्वकृतोत्तमः स्यात् | शूद्रोऽपि शृण्वन्स्वकुलोत्तमः स्यात् | k1 14 |
| 7.22.48 | split | निष्कैः पुत्रो |  | k2 57 |
| 7.22.49 | r | स्वप्लमालक्ष्य | स्वल्पमालक्ष्य | k2 57 |
| 1.5.102 | r | अन्तर्धानं गता तथा | अन्तर्धानं गता तदा | k1 78 |
| 3.7.14 | r | निगुणौ | निर्गुणौ | k1 198 |
| 4.6.45 | r | गहीत्वेमा | गृहीत्वेमा | k1 290 |
| 8.8.9 | r | पुमान्तस्त्री | पुमान्स्त्री | k2 137 |
| 8.8.10 | r | स्वीणाम | स्त्रीणाम | k2 137 |
| 8.8.14 | r | यथानोस्त्रतमन्यु | यथानोजितमन्यु | k2 137 |
| 8.8.16 | r | मिवक्यचित् | मिवक्वचित् | k2 137 |
| 8.8.17 | r | यत्सवतो | यत्संवृतो | k2 137 |
| 9.8.85 | r | मृत्युज्जय | मृत्युञ्जय | k2 215 |
| 10.7.2 | r | बभूबु | बभूवु | k2 365 |
| 8.7.22 | r | चतुर्भद्रेति* | चतुर्भद्रेति | k2 135 |
| 8.7.23 | drop | *चक्षुर्भद्रेति? |  | k2 135 |

**Repairs to the e-text's numbering**

| Where | Repair |
|---|---|
| Māhātmya.1 | block 26 split into 25–26 (their numbers were dropped) |
| Māhātmya.1 | block 41 split into 40–41 (their numbers were dropped) |
| Māhātmya.1 | block 46 split into 45–46 (their numbers were dropped) |
| Māhātmya.4 | verse after 48 closed by a bare ॥, numbered 49 |
| Māhātmya.4 | verse after 52 closed by a bare ॥, numbered 53 |
| Māhātmya.4 | number 3 between 72 and 74 read as 73 |
| Māhātmya.5 | 1 brackets/backticks removed |
| Māhātmya.5 | verse ८७ ended mid-line |
| Māhātmya.5 | number 10 between 89 and 91 read as 90 |
| 5.17 | number 15 between 15 and 17 read as 16 |
| 5.17 | number 58 between 52 and 54 read as 53 |
| 5.18 | number 98 between 57 and 59 read as 58 |
| 5.31 | e-text has no verse 22 (gap kept) |
| 5.32 | verse after 42 closed by a bare ॥, numbered 43 |
| 5.33 | verse after 4 closed by a bare ॥, numbered 5 |
| 5.33 | number 1 after 1 kept as printed |
| 5.35 | verse after 29 closed by a bare ॥, numbered 30 |
| 7.5 | block 23 split into 22–23 (their numbers were dropped) |
| 7.8 | 2 brackets/backticks removed |
| 7.8 | number 23 between 23 and 25 read as 24 |
| 7.9 | 2 brackets/backticks removed |
| 7.17 | 2 brackets/backticks removed |
| 7.18 | number 28 between 37 and 39 read as 38 |
| 7.22 | block 4 split into 3–4 (their numbers were dropped) |
| 7.22 | e-text has no verse 47 (gap kept) |
| 7.26 | number 63 between 61 and 63 read as 62 |
| 7.27 | verse 21 repeated in the e-text, second copy dropped |
| 7.27 | number 8 between 6 and 8 read as 7 |
| 8.7 | verse २२ ended mid-line |
| 9.12 | 1 unnumbered prose passage(s) kept |
| 9.13 | number 7 between 116 and 118 read as 117 |
| 9.15 | verse १० ended mid-line |
| 12.4 | 1 unnumbered prose passage(s) kept |

### 5.28 Sandhyāvandanam, Kṛṣṇa Yajurveda (Taittirīya) — `stotra/veda/sandhyavandanam-iast.html`

| Field | Value |
|---|---|
| Work | The daily twilight worship (sandhyāvandana) of the Taittirīya household: preliminaries, mārjana, prāśana (morning, noon, evening), arghya, Gāyatrī āvāhana, nyāsa, japa, upasthāna for the three times, concluding salutations |
| Wording and order | B. V. Kamesvara Aiyar, *The Sandhyavandanam of Rig, Yajus, and Sâma Vedins*, Madras: G. A. Natesan, 1898 (archive.org `sandhyavandanam00aiyagoog`, Harvard copy scanned by Google). Public domain by age. The Yajurvedin mantras only; the Ṛgvedin and Sāmavedin alternatives the book also gives are left out |
| Svaras | Taittirīya Saṃhitā, ed. A. Mahadeva Sastri and K. Rangacharya, vol. V, Mysore, 1896 (archive.org `ksu.a27.taittiriyasamhit0000amah`, pp. 370–383, TS 3.4.11); Taittirīya Saṃhitā, Bombay, 1888 (archive.org `ksu.a238.taittiriyasamhit0000tuka`; TS 1.4.43, 1.5.6, 2.1.11 checked); accented Ṛgveda on Sanskrit Wikisource (revisions: 10.9 r315287, 4.39 r402356, 3.62 r330443, 1.50 r401983, 1.115 r329056, 1.24 r401826, 1.25 r283258, 7.89 r201385) |
| Recorded | 2026-11-07 |
| Text status | ancient and public domain; both prints are public domain by age |

**Why the svaras come from elsewhere.** The 1898 book prints the mantras
in Devanāgarī with some svara marks, but they are incomplete: many akṣaras
that need a mark are bare, and several mantras have none. Following the
maintainer's choice, the wording and order are the book's, and the svaras
come from the accented Saṃhitā and Ṛgveda texts the book itself cites.

- **TS mantras read on the Mysore 1896 page:** *mitrasya carṣaṇīdhṛtaḥ*,
  *mitro janān*, *pra sa mitra* (morning upasthāna), *ā satyena* (noon),
  *yac cid dhi te*, *yat kiñcedam*, *kitavāso* (evening), all TS 3.4.11.
  Where the TS reading differs from the Ṛgveda (*śravo … sānasim | satyaṃ*,
  *prajānan*, *satyāya … vidhema*, *ā satyena … bhuvanā vipaśyan*, *devāthā*),
  the TS reading is used, and it is also the book's.
- **Ṛgveda mantras whose TS text has the same words:** *āpo hi ṣṭhā*
  (ṚV 10.9.1–3 / TS 4.1.5), *dadhikrāvṇo* (4.39.6 / TS 1.5.11), the Gāyatrī
  (3.62.10 / TS 1.5.6), *udu tyam* and *citram* (1.50.1, 1.115.1 / TS 1.4.43),
  *imaṃ me varuṇa* and *tat tvā yāmi* (1.25.19, 1.24.11 / TS 2.1.11). Their
  svaras and sandhi are the Ṛgveda saṃhitā's, half-verse by half-verse, as
  Wikisource prints them; the TS prints compared (1888, leaves 41, 50, 110)
  carry the same marks. The book's pauses after each pāda are therefore not
  shown as daṇḍas.
- **Spellings from the book, not the Ṛgveda:** *mṛḍaya*, *aheḍamāno* (ḍ for
  the Ṛgveda's ḷ); Taittirīya *ꣳ* (shown *gṃ*, rendered ग्ं) in *aṃho* →
  *agṃho* and *uruśagṃsa*; *yas te āditya* and *carṣaṇīdhṛtaḥ śravo* without
  the TS's sandhi (*yasta āditya*, *dhṛtaśśravo*); *manuṣyāś carāmasi* in
  the TS form, without the Ṛgveda's pluta.
- **Unaccented:** the Taittirīya Āraṇyaka mantras (prāśana TA 10.23–25,
  Gāyatrī-śiras, āvāhana TA 10.26, *uttame śikhare*, *antaś carati* TA 10.31,
  *tac cakṣur … ya udagāt* TA 4) and the formulas (vyāhṛtis, saṅkalpa, nyāsa,
  *asāv ādityo brahma*, the closing salutations). The only accented
  public-domain TA 10 found, the Ānandāśrama print, is scanned at about 100
  dpi, too coarse to read its marks. *Udvayaṃ tamasas pari* (TS 4.1.7) is also
  unaccented: its TS reading (*paśyanto jyotir uttaram*) differs from the
  Ṛgveda's, and no legible accented TS page of it was found.

**Editorial notes.**
- The book abbreviates the prāṇāyāma vyāhṛtis ("oṃ bhūḥ &c."); they are
  written out as the seven (*oṃ bhūḥ … oṃ satyam*).
- The book gives the quarter-salutation for the east and says "and so on";
  only the east is printed, with a rubric for the others.
- The evening and noon prāśana changes are given as the book gives them, as a
  substitution list after the morning mantra.
- The book's footnoted variants (*juṣasva me*, *jāte*, *abhyanujñānam*,
  *netratrayāya*) are mentioned in the glosses, not adopted.
- Ācamana formulas and the nyāsa's ṛṣi–chandas–devatā statement are
  described in the book but not printed, so they are not given.
- Rubrics and glosses are original; the book's word-by-word English
  (after Sāyaṇa) was used only to check understanding.

### 5.29 Amarakośa (Nāmaliṅgānuśāsana) — `stotra/amarakosha/`

| Field | Value |
|---|---|
| Work | Amarasiṃha's *Nāmaliṅgānuśāsana*, the Amarakośa: three kāṇḍas, 25 vargas as the print divides them, 1,500 numbered ślokas plus the kṣepakas |
| Source | Sanskrit Wikisource, `अमरकोशः/प्रथमकाण्डम्` (rev 407023), `/द्वितीयकाण्डम्` (rev 340250), `/तृतीयकाण्डम्` (rev 407024), fetched 2026-11-09. The e-text names no edition; it sets one half-verse a line with a running count (॥ K.V.N ॥) |
| Read against | *Nāmaliṅgānuśāsanam* with Maheśvara's *Amaraviveka*, enlarged by Raghunātha Śāstrī Talekar, ed. Cintāmaṇi Śāstrī Thatte under F. Kielhorn, 2nd ed., Bombay: Government Central Book Depot, 1882, printed at the Nirṇaya Sāgara Press (archive.org `20231127_20231127_1402`, scan with tesseract OCR). Public domain by age |
| Recorded | 2026-11-09 |
| Text status | ancient and public domain; the e-text is used as public domain as for §5; the 1882 print is public domain |

**Why the print.** The e-text has no śloka division of its own: it
numbers half-verses straight through each kāṇḍa, and it runs later
interpolations (kṣepakas) into the mūla unmarked, so its half-verses
cannot simply be paired. The 1882 print sets the kośa in large type over
the commentary, numbers the ślokas afresh in each varga, and puts every
kṣepaka in quotation marks. Its structure is followed throughout; its
commentary is not used. (A 1940 Poona edition with English equivalents,
on archive.org as `AmaraKosa`, is in copyright and was not used.)

**Method.** `tools/amarakosha/`: `parse.py` reads the e-text into vargas
and applies `print1882.tsv`; `ocr.py` pulls the kośa lines out of the
print's OCR by type size; `align.py` aligns every e-text half-verse with
a print line (2,915 of 3,119 matched; the rest are lines the OCR lost or
lines the print lacks); `number.py` closes a śloka wherever the print
closes one with ॥ N ॥ and marks the quoted spans as kṣepakas, checking its
own count against the print's digits; `gen.py` writes the pages. Every
place where the count and the print's digits disagreed for more than a
stray misread was settled on the page image (`leaf.py`, `crop.ps1`), and
the outcome recorded in `print1882.tsv`; in the final state the two agree
everywhere except two runs of three where the OCR reads ४ as २. All
lines that fail the anuṣṭubh count (anything but 16 syllables, āryās
aside) were read against the print, as was one leaf of every varga in
full (leaves 11, 17, 21, 28, 34, 39, 47, 54, 56, 62, 67, 72, 77, 80, 101,
126, 149, 173, 194, 224, 244, 282, 318, 352, 365). Spelling conventions
(anusvāra for a class nasal, the print's `ऽ` spacing) are not collated.

**Structure.** The print's vargas are kept: it runs the opening verses
into the svargavarga, the vāgvarga and śabdavarga into one śabdādivarga,
each kāṇḍa's opening into its first varga, and the indeclinables of
several meanings into the nānārthavarga, and the pages follow (with a
heading where the e-text's section changes). The first kāṇḍa's closing
verse, numbered on its own in the print, ends the vārivarga page. A varga
may end on a half-śloka (as the print has it). Kṣepakas — 51 passages —
and the 20 runs the e-text has and the print lacks are kept, set a size
smaller under a rubric that says which they are, so nothing in the e-text
is dropped. The e-text's tallies of verses (अत्र मूलश्लोकाः …), a running
count fused to some lines (९७०, …), and a contributor's query are
removed; its group markers in the nānārthavarga (इति कान्ताः …) are kept
as colophons, three moved to where the print sets them. The print's
marker इति प्राणिवर्गः inside the viśeṣyanighnavarga, which falls between
the halves of a śloka, is not set. Each page closes with the print's
इति … वर्गः, and each kāṇḍa with its colophon as the print gives it (the
e-text cut the second's short and dropped the third's).

Translations will follow; the varga descriptions in English are original.

**Readings of the 1882 print adopted (r, line, add, join, move)**

| Where | Op | E-text | Print | Leaf |
|---|---|---|---|---|
| 2.8.963 | line | लिखिताक्षरविन्यासे संस्थाने | लिखिताक्षरसंस्थाने लिपिर्लिबिरुभे स्त्रियौ | 183 |
| 2.8.973 | line | साहसं तु समो दमो | साहसं तु दमो दण्डः साम सान्त्वमथो समौ | 185 |
| 2.8.1016 | line | दूष्या चूषा | दूष्या कक्ष्या वरत्रा स्यात्कल्पना सज्जना समे | 190 |
| 2.8.1019 | line | घोटके वीति पीति | घोटके वीतितुरगतुरङ्गाश्वतुरङ्गमाः | 190 |
| 3.3.348 | join | च यः |  | 290 |
| 3.3.352 | r | स्याद्व्याग्रेऽपि | स्याद्व्याघ्रेऽपि | 291 |
| 3.3.363 | r | धृणिज्वाले | घृणिज्वाले | 291 |
| 1.1.101 | line | व्ऱीद्धश्रवाः सुनासीरः पुरुहूतः पुरन्दरः | वृद्धश्रवाः शुनासीरः पुरुहूतः पुरन्दरः | 11 |
| 2.4.211 | add |  | शोणकश्चारलौ तिष्यफला त्वामलकी त्रिषु | 95 |
| 2.6.789 | add |  | घनसारश्चन्द्रसंज्ञः सिताभ्रो हिमवालुका | 163 |
| 2.6.789.1 | add |  | गन्धसारो मलयजो भद्रश्रीश्चन्दनोऽस्त्रियाम् | 163 |
| 3.3.414 | r | दक्षामन्दागदेषु तु | दक्षामन्दागदेषु च | 296 |
| 3.3.590 | line | व्युत्थानं प्रतिरोधे च विरोधाचरणेऽपि च | उत्थानं पौरुषे तन्त्रे संनिविष्टोद्गमेऽपि च | 313 |
| 3.3.591 | line | उत्थानं पौरुषे तन्त्रे संनिविष्टोद्गमेऽपि च | व्युत्थानं प्रतिरोधे च विरोधाचरणेऽपि च | 313 |
| 3.3.604 | r | संविधानम | संपिधानम | 314 |
| 3.3.815 | r | कोषोऽस्त्री | कोशोऽस्त्री | 337 |
| 3.3.815 | move |  | 806 | 337 |
| 1.1.139 | r | कोणपः क्रव्यात्क्र्व्यादो | कौणपः क्रव्यात्क्रव्यादो | 15 |
| 1.2.170 | r | विहासयोऽपि | विहायसोऽपि | 17 |
| 1.2.170 | r | तदव्यम् | तदव्ययम् | 17 |
| 1.3.176 | r | दीचीचीनम | दीचीनम | 18 |
| 1.3.194 | r | विद्युच्च्ञ्चला | विद्युच्चञ्चला | 19 |
| 1.3.208 | r | प्रसाद्स्तु | प्रसादस्तु | 20 |
| 1.6.353 | r | व्यवहार | व्याहार | 36 |
| 1.8.426 | r | साम्यममथा | साम्यमथा | 45 |
| 1.10.514 | r | निर्र्तिः | निर्ऋतिः | 55 |
| 2.1.24 | r | एवादिमावेववम | एवादिमावेवम | 72 |
| 2.4.194 | r | ष्ड्ग्रन्थो | षड्ग्रन्थो | 93 |
| 2.4.244 | r | कुरकण्टकः | कुरण्टकः | 99 |
| 2.4.370 | r | छगलान्त्रयावेगी | छगलान्त्र्यावेगी | 112 |
| 2.4.395 | r | स्याद्वाअतकः | स्याद्वातकः | 115 |
| 2.6.654 | r | क्र्व्यम | क्रव्यम | 149 |
| 2.6.655 | r | उत्ततप्तं शुश्कमांसं | उत्तप्तं शुष्कमांसं | 149 |
| 2.6.699 | r | संहततलप्रतलौ | संहतलप्रतलौ | 154 |
| 2.6.703 | r | स्तिर्यगनन्तरम् | स्तिर्यगन्तरम् | 154 |
| 2.6.803 | r | खट्व्या | खट्वया | 165 |
| 2.7.828 | r | गीर्पतीष्टया | गीष्पतीष्ट्या | 168 |
| 2.7.871 | r | म्र्तार्थं | मृतार्थं | 173 |
| 2.7.884 | r | चाअदिकविः | चादिकविः | 174 |
| 2.7.920 | r | तद्वत्क्.च्छं | तद्वत्कृच्छ्रं | 178 |
| 2.8.962 | r | लिपिकारोऽक्षरचरणो | लिपिकरोऽक्षरचणो | 183 |
| 2.8.1038 | r | प्रेङ्खाअदिकाः | प्रेङ्खादिकाः | 193 |
| 2.8.1117 | r | स्याच्छ्स्त्री | स्याच्छस्त्री | 202 |
| 2.8.1121 | r | राज्ञानां | राज्ञां | 203 |
| 2.8.1148 | r | पताहादम्बरओ | पटहाडम्बरौ | 206 |
| 2.8.1151 | r | मोहो.आप्यवमर्दस्तु पीदनम् | मोहोऽप्यवमर्दस्तु पीडनम् | 206 |
| 2.9.1193 | r | खरीवापस्तु | खारीवापस्तु | 211 |
| 2.9.1193 | r | उत्त्मर्ण | उत्तमर्ण | 211 |
| 2.9.1231 | r | अङ्गारधानिकाङ्गागरशकट्यपि | अङ्गारधानिकाङ्गारशकट्यपि | 217 |
| 2.9.1274 | r | गोमयस्त्रियाम् | गोमयमस्त्रियाम् | 223 |
| 2.9.1310 | r | चतुर्हाण्येवं | चतुर्हायण्येवं | 227 |
| 2.9.1315 | r | स्यात्नवसूतिका | स्यान्नवसूतिका | 228 |
| 3.1.68 | r | स्यादवाङ्प्यधोमुखः | स्यादवाङप्यधोमुखः | 260 |
| 3.1.118 | r | परार्ध्याग्रप्राग्रहरप्राग्रयाग्रयाग्रीयमग्रियम् | परार्ध्याग्र्यप्राग्रहरप्राग्र्याग्र्याग्रीयमग्रियम् | 265 |
| 3.1.122 | r | अप्राग्रयं | अप्राग्र्यं | 266 |
| 3.1.129 | r | भूयश च | भूयश्च | 267 |
| 3.1.177 | r | नुत्तनुन्नास्तनिष्ठयूता | नुत्तनुन्नास्तनिष्ठ्यूता | 271 |
| 3.2.303 | r | निष्ठयूति | निष्ठ्यूति | 285 |
| 3.3.480 | r | विस्तार वल्लयोर्व्रततिर् | विस्तारवल्ल्योर्व्रततिर् | 302 |
| 3.3.549 | r | स्यात्प्रकृतस्यादि विनश्वरे | स्यात्प्रकृत्यादिविनश्वरे | 309 |
| 3.3.550 | r | प्रकृत्यानुवर्तने | प्रकृतस्यानुवर्तने | 309 |
| 3.3.626 | r | पुमूबहुत्वेऽपि | पुंबहुत्वेऽपि | 316 |
| 3.6.987 | r | द्वयष्कम | द्व्यच्कम | 365 |
| 3.6.990 | r | द्वन्द्वैक्त्वा | द्वन्द्वैकत्वा | 365 |
| 2.4.248 | r | ओण्ड्रपुष्पं | ओड्रपुष्पं | 99 |
| 1.3.215 | r | स्यातगस्त्यः | स्यादगस्त्यः | 21 |
| 1.3.218 | r | दाक्षायिण्योऽश्विनी | दाक्षायण्योऽश्विनी | 21 |
| 1.3.220 | r | धनिष्ठाः स्युः | धनिष्ठा स्युः | 21 |
| 1.5.340 | r | पूतिगन्धस्तु | पूतिगन्धिस्तु | 34 |
| 2.4.265 | r | पाटाम्बष्टा विद्धकर्न्णी | पाठाम्बष्ठा विद्धकर्णी | 101 |
| 2.4.266 | r | एकाष्टीला | एकाष्ठीला | 101 |
| 2.6.660 | r | पुरीतगुल्मस्तु | पुरीतत् गुल्मस्तु | 149 |
| 2.7.872 | r | शस्त्रतः | शास्त्रतः | 173 |
| 2.8.1047 | r | अनुकर्षी | अनुकर्षो | 194 |
| 2.9.1281 | r | मन्डं | मण्डं | 224 |
| 2.10.1444 | r | मोपकाः | मोषकाः | 244 |
| 3.2.276 | r | स्यादपसर | स्यादवसर | 282 |
| 3.3.640 | r | निगमा | निगमो | 318 |
| 3.3.643 | r | कुतिले | कुटिले | 318 |
| 2.10.1491 | line | इत्यमरसिंहकृतौ नामलिङ्गानुशासने द्वितीयः काण्डो | इत्यमरसिंहकृतौ नामलिङ्गानुशासने | 250 |
| 2.10.1491 | add |  | द्वितीयः काण्डो भूम्यादिः साङ्ग एव समर्थितः | 250 |
| 3.6.1031 | add |  | इत्यमरसिंहकृतौ नामलिङ्गानुशासने | 374 |
| 3.6.1031.1 | add |  | सामान्यकाण्डस्तृतीयः साङ्ग एव समर्थितः | 374 |
| 2.10.1490 | r | वृत्तावूत्द्या | वृत्तावूह्या | 250 |

**Structure taken from the print (nip = in the e-text, not in the print, shown apart; ks = a kṣepaka the OCR did not mark; end = a śloka closes; mark = a group marker)**

| Where | Op | E-text | Print | Leaf |
|---|---|---|---|---|
| 3.3.349-358 | ks |  |  | 290-291 |
| 3.3.359 | nip | मृद्भाण्डेऽप्युष्ट्रिका मन्थे खजकं रसदर्वकः | (not in the print) | 291 |
| 1.1.57-60 | nip | अरविन्दमशोकं च … पञ्च बाणाः प्रकीर्तिताः | (not in the print) | 8-9 |
| 1.1.86-87 | nip | अणिमा महिमा … चाष्ट सिद्धयः | (quoted in the commentary, not mūla) | 10-11 |
| 1.1.92 | ks | कर्ममोटी तु चामुण्डा चर्ममुण्डा तु चर्चिका | (quoted half-verse) | 11 |
| 2.5.463 | nip | चुचुन्दरी गन्धमूषी दीर्घदेही तु मूषिका | (not in the print) | 124 |
| 2.8.984 | nip | सुधरणा सुधारा स्त्री सुस्थितिः सुदशोन्नतिः | (not in the print) | 186 |
| 3.1.107 | nip | रम्यं मनोहरं सौम्यं भद्रकं रमणीयकम् | (not in the print) | 264 |
| 3.3.389-390 | ks |  | (the chānta group, one kṣepaka śloka) | 294 |
| 3.3.401 | nip | दोषज्ञौ वैद्यविद्वांसौ ज्ञो विद्वान्सोमजोऽपि च | (not in the print) | 295 |
| 3.3.430-432 | nip | संघातग्रासयोः पिण्डी … शिखण्डो बर्हचूडयोः | (not in the print) | 297 |
| 3.3.416-417 | nip | पोटा दासी … कृपीटमुदरे जले | (not in the print) | 296 |
| 3.3.517 | mark |  | इति तान्ताः | 306 |
| 3.3.518-520 | nip | समूहोत्पन्नयोर्जातम् … व्यवस्थायामपि स्थितिः | (not in the print) | 306 |
| 3.3.562-563 | nip | लेशेऽपि गन्धः … ज्ञातृचान्द्रिसुरा बुधाः | (not in the print) | 310 |
| 3.3.576 | end |  | (OCR lost ॥ ११० ॥) | 311 |
| 3.3.620-622 | nip | शिफा शिखायां … बाहोरलंकारे च कीर्तितः | (not in the print) | 316 |
| 3.3.747-750 | nip | आसारो वेगवद्वर्षे … अधीरः कातरे चले | (not in the print) | 331 |
| 3.3.777-781 | nip | कुलं गृहेऽपि … शष्कुली कर्णपाल्यपि | (not in the print) | 334 |
| 3.3.781 | mark |  |  | 334 |
| 3.3.776 | mark |  | इति लान्ताः | 334 |
| 3.3.807-809 | nip | नाशः क्षये … पाशो बन्धनशस्त्रयोः | (not in the print) | 337 |
| 3.3.809 | mark |  |  | 337 |
| 3.3.815 | mark |  | इति शान्ताः | 337 |
| 3.3.825-828 | nip | व्याजसंख्याशरव्येषु … द्वयोश्च मुखपूरणे | (not in the print) | 339 |
| 3.3.828 | mark |  |  | 339 |
| 3.3.824 | mark |  | इति षान्ताः | 339 |
| 3.5.930-931 | nip | अमानुगुण्ये स्मरणे … हीनसंबोधते त्वरे | (not in the print) | 354 |
| 2.7.914 | nip | कक्षापटी च कौपीनं शाटी च स्त्रीति लक्ष्यतः | (not in the print) | 178 |
| 3.1.6 | nip | क्षेमङ्करोऽरिष्टतातिश्शिवतातिश्शिवङ्करः | (not in the print) | 252-253 |
| 3.3.626 | end |  | (OCR lost ॥ १३३ ॥) | 316 |
| 3.3.627-628 | nip | चित्रपुङ्खेऽपि कादम्बो … मण्डलेऽपि च | (not in the print) | 316-317 |
| 3.3.628 | mark |  |  | 316 |
| 3.3.626 | mark |  | इति बान्ताः | 316 |

**Real variants kept as the e-text has them**

| Where | Op | E-text | Print | Leaf |
|---|---|---|---|---|
| 2.8.972 | v | भेदो दण्डः साम दानमित्युपायचतुष्टयम् | सामदाने भेददण्डावित्युपायचतुष्टयम् | 185 |
| 1.1.162 | v | कैलासः स्थानमलका | कैलासस्थानमलका | 17 |

### 5.30 Nighaṇṭu — `stotra/veda/nighantu-iast.html`

| Field | Value |
|---|---|
| Work | The Nighaṇṭu, the Vedic word-lists on which Yāska's Nirukta is a commentary: five adhyāyas, 78 khaṇḍas (adhyāyas 1–3 synonyms, 4 the Naigama-kāṇḍa of single words, 5 the Daivata-kāṇḍa of deities) |
| Source | Lakshman Sarup, *The Nighaṇṭu and the Nirukta*, vol. I: Sanskrit text, University of the Panjab, Lahore, 1927, printed at the Nirṇaya Sāgara Press, Bombay — archive.org `in.ernet.dli.2015.282287` (Digital Library of India), leaves n40–n65 = printed pp. 1–26. Public domain: Sarup died in 1946 |
| Also used | Rudolph Roth, *Jâska's Nirukta sammt den Nighaṇṭavas*, Göttingen, 1852 (archive.org `india.history.resource.41273`, p. 18), for two words torn away in the scan (below) |
| Recorded | 2026-11-09 |
| Text status | ancient and public domain; both editions public domain by age |

**Why not Wikisource.** Sanskrit Wikisource has the Nighaṇṭu and the
Nirukta. Its Nirukta pages are marked as copied from the Maharishi
University of Management Vedic Literature Collection, which is
distributed "for education purpose only", so they were not used. Its
Nighaṇṭu pages name no source at all, so the text was taken from a print
instead.

**Method.** archive.org's OCR of the scan is unusable, so each leaf was
fetched at full size and read off the image; Tesseract 5 (Sanskrit
model, after `tools/nirukta/clean.py` removes the scan's grain) was run on
every leaf as a check. The transcription is `tools/nirukta/nighantu.txt`;
`tools/nirukta/check.py` compares each khaṇḍa's word count with the count
its own closing words state (गोत्रेत्येकविंशतिः …) — all 78 agree, two
counting one more word that only the longer recension has (2.5
*gabhastayaḥ*, 2.7 *yaśaḥ*) — and lists every word Tesseract does not
support, each of which was looked at again on the image.
`tools/nirukta/gen_nighantu.py` writes the page.

**Editorial notes.**

- Sarup's square brackets, which mark what is found in only part of the
  manuscripts (chiefly each khaṇḍa's count of its words), are kept.
- Sarup prints the svaras; they are not carried (a later pass may add them).
- His section numbers are kept; his footnotes (manuscript readings) and
  footnote markers are not.
- Where he prints the shorter recension's form of a khaṇḍa as an
  alternative (2.14, 3.14 from *bhandate*, 3.16), only his main text is
  given, and a rubric says so.
- The summary verses that some manuscripts add after each adhyāya, which
  Sarup prints with their sigla, are kept as small passages under a rubric.
- Leaf n54 (p. 15) is torn across 3.1–3.2: *sahasram । salilam* (3.1) and
  *hrasvaḥ । nighṛṣvaḥ* (3.2) are supplied from Roth (1852), whose text
  agrees with Sarup's on the rest of both khaṇḍas.
- 3.7 reads *śaṣyamiti rūpasya* (so the text and Sarup's footnote).

The English glosses, one for each khaṇḍa, are original.

### 5.31 Nirukta — `stotra/veda/nirukta-N-iast.html`, one page an adhyāya

| Field | Value |
|---|---|
| Work | Yāska's Nirukta, the commentary on the Nighaṇṭu (§5.30): twelve adhyāyas and the pariśiṣṭa (counted as adhyāya 13, or as 13–14), one page each; complete |
| Source | Lakshman Sarup, *The Nighaṇṭu and the Nirukta*, vol. I: Sanskrit text, 1927 (as §5.30) — archive.org `in.ernet.dli.2015.282287`, leaf nN = printed page N − 39. Public domain: Sarup died in 1946 |
| Recorded | 2026-11-10 onwards |
| Text status | ancient and public domain; the edition public domain by age |

| Adhyāya | Khaṇḍas | Leaves | Printed pp. | Words the OCR check flagged |
|---|---|---|---|---|
| 1 | 20 | n66–n82 | 27–43 | 64, all OCR failures |
| 2 | 28 | n83–n97 | 44–58 | 59, all OCR failures |
| 3 | 22 | n98–n113 | 59–74 | 68; two led to keeping the print's word division (below) |
| 4 | 27 | n114–n129 | 75–90 | 64, all OCR failures |
| 5 | 28 | n130–n147 | 91–108 | 76, all OCR failures |
| 6 | 36 | n148–n170 | 109–131 | 84, all OCR failures |
| 7 | 31 | n171–n188 | 132–149 | 74, all OCR failures |
| 8 | 22 | n189–n197 | 150–158 | 26, all OCR failures |
| 9 | 43 | n198–n211 | 159–172 | 48, all OCR failures |
| 10 | 47 | n212–n228 | 173–189 | 41, all OCR failures |
| 11 | 50 | n229–n244 | 190–205 | 49, all OCR failures |
| 12 | 46 | n245–n261 | 206–222 | 45, all OCR failures |
| 13 (pariśiṣṭa) | 48 | n262–n283 | 223–244 | 56, all OCR failures |

**Not Wikisource.** Sanskrit Wikisource's Nirukta is copied from the
Maharishi University of Management Vedic Literature Collection, which is
distributed "for education purpose only"; it was not used, not even as a
check.

**Method.** Each page of Sarup's Nirukta carries the text above a rule and
a long apparatus below it. `tools/nirukta/maintext.py` finds the rule and
crops the text; `tools/nirukta/ocrmain.sh` fetches each leaf and runs
Tesseract on the crop. The text was read off the page images, paragraph by
paragraph, into `tools/nirukta/niruktaN.txt`, with the OCR as a draft.
`tools/nirukta/ocrcheck.py` then lists every word the OCR does not
support, and each was looked at again on the image (the counts are in the
table above; nearly all were OCR failures, chiefly on mantras and long
compounds).
Readings in doubt were checked on the full-resolution scan.
`tools/nirukta/gen_nirukta.py` writes the page from the transcription and
the English keys `tools/nirukta/glossN.txt`.

**Editorial notes.**

- Sarup's square brackets (words found in only part of the manuscripts)
  and his khaṇḍa numbers are kept; his footnotes and footnote markers are
  not.
- Sarup prints svaras on the quoted mantras; they are not carried.
- Quotations he sets apart on their own lines (mantras, and in smaller type
  phrases from the Brāhmaṇas) are separate lines here, in his order.
- His spellings are kept as printed: anusvāra before a stop where he
  prints it (*paṃcamī-*, *saṃprayujyate*, *naighaṃṭukam*,
  *kiñcittṛṃdyāt*), the Ṛgvedic ḷ and ḷh (*krīḷantau*, *mṛḷa*,
  *parivṛḷhaḥ*), and his word division.
- 1.4 reads *[ ācārya kasmāt ]*, without visarga, as printed.
- 1.5 reads *athāpi nu nanu ity etābhyāṃ*, as printed.
- 1.6: an ink smudge on leaf n71 covers part of *śvastanam* and of
  *idam apītarad adbhutam*; what is legible agrees with that reading.
- The opening line (*śrīyāskamuniviracitaṃ niruktaṃ prārabhyate*), the
  closing lines, and the khaṇḍānukramaṇī (the opening words of the twenty
  khaṇḍas) that Sarup prints after the adhyāya are kept, the last as a
  small passage under a rubric.

- 2.3: the verse *yasmāt paraṃ nāparam asti* … (Taittirīya Āraṇyaka
  10.10.3), which Sarup numbers ॥ ३ ॥ in the middle of the khaṇḍa, keeps
  that number in the text; the khaṇḍa's own ॥ ३ ॥ follows on the next
  leaf.
- 2.6 reads *kṣākṣiyater nivāsakarmaṇaḥ*, 2.16 *śarīrasya śrotāṃsi*, 2.17
  *tadu vṛtrasya vṛtratvam* (three times), as printed.
- 2.28: the khaṇḍānukramaṇī reads *vidyā ha vai*; the vowel sign of *vai*
  is under a footnote mark in the scan, and the verse it cites (2.4) begins
  *vidyā ha vai*.

- 3.20: *dhārayater vā*, *ṛdhnoter vā* are closed up; the print spaces
  them *dhārayate rvā*, *ṛdhnote rvā*.
- 3.20 *abhīke cidulokakṛt* and 3.22 *kathājāte* keep Sarup's word
  division in the quoted mantras.
- 3.3, 3.20: bracketed alternatives *[ putraḥ ]*, *[ nigamau bhavataḥ ]*
  and the bracketed half-line *[ vamrībhiḥ putram agruvo adānam ]* are
  kept as printed.

- 4.19, 4.25: quotations that Sarup prints whole in square brackets
  (*[ rajāṃsi citrā vi caranti tānyavaḥ … ]*, *[ pratyagne harasā haraḥ
  śṛṇīhi … ]*, *[ gātuṃ kṛṇvann uṣaso janāya … ]*), being found in only part
  of the manuscripts, keep their brackets.

- 5.27: after the khaṇḍa Sarup prints, in brackets, a second version of
  its comment (*sudevas tvaṃ kalyāṇadevaḥ … bīriṭaṃ taiṭīkiḥ …*), found in
  only part of the manuscripts, which closes with its own ॥ २७ ॥. Both are
  kept, the bracketed one last in the khaṇḍa.
- 5.7 *akra juhvāno*, 5.17 *aṅkitam evāñcitam*, as printed.

- 6.5, 6.6: the story of Indra's question about famine (with its verse on
  the nine livelihoods) and the gloss *kṣoṇasya kṣayaṇasya* with its
  quotation are printed by Sarup in square brackets and kept so.
- 6.36: after the adhyāya Sarup prints the colophon of the first half,
  *iti naigamaṃ kāṇḍaṃ pūrvārdhaś ca samāptam*, kept as a closing line.

- 7.1: the praṇava Sarup prints before *athāto daivatam* is written
  *oṃ* in the IAST, which the page renders as ॐ.
- 7.20: the whole comment on *jātavedase sunavāma somam*, with its own
  closing numbers ॥ २ ॥ २५ ॥, is printed in square brackets and kept so,
  inside the khaṇḍa.
- 7.31: after the adhyāya Sarup prints *iti uttaraṣaṭke prathamo'dhyāyaḥ*
  (the second six counting afresh) as well as *iti nirukte saptamo'dhyāyaḥ*;
  both are kept.

- The pariśiṣṭa: Sarup numbers it as one adhyāya of 48 khaṇḍas, giving in
  his running heads the second numbering of the manuscripts that make it two
  (13.14 = 14.1 … 13.48 = 14.37); the page follows his main numbering, and a
  rubric marks where the old thirteenth adhyāya closes after 13.13. Two
  passages he prints in square brackets, with no khaṇḍa number of their own
  (the khila verse *ā yāhīndra pathibhiḥ* with its comment after 13.42, and
  the verse *idaṃ te 'nyābhiḥ* with its comment, closing ॥ १४ ॥ ३४ ॥, after
  13.46), are kept where he prints them, at the head of the khaṇḍa that
  follows. The list of the names of the
  great self (13.24), accented in the print, is given unaccented.

The heading and English summary of each khaṇḍa are original; they
summarise, they do not translate.

## 6. Telugu-language works

These are compositions in the **Telugu language** (not Sanskrit). For
them the **Telugu is the source of truth** (`src="tel"` in the data
file, `data-src="tel"` on the page); the page offers Telugu and an
**IAST reading aid**, generated at runtime with teltools `tel2iast`.
Devanāgarī is not offered — it is not a meaningful script for Telugu
literature.

teltools is a Sanskrit transliterator and does not map the Telugu
**short e/o** vowels (`ె`/`ొ`), which Sanskrit lacks (it also emits a
spurious inherent *a* before them). The page repairs this in a small
post-processor (`telIast`): the short signs become plain `e`/`o`. The
short/long *e-o* length distinction is therefore not marked in the IAST
aid — an acceptable simplification for a pronunciation guide, and one a
reader can refine through the correction facility.

Translations are original, made from the Telugu.

### 6.1 Adivo Alladivo — `stotra/venkateshwara/`

| Field | Value |
|---|---|
| Author | Annamācārya (Annamayya), 15th c. |
| Source | Telugu Wikisource, *అదివో అల్లదివో* |
| URL | `te.wikisource.org/wiki/అదివో అల్లదివో` |
| Recorded | 2026-07-25 |
| Text status | public domain (author d. 1503) |
| Content | pallavi + 3 caraṇas; rāgam Madhyamāvati, tāḷam Ādi |

### 6.2 Paluke Bangāramāyenā — `stotra/rama/`

| Field | Value |
|---|---|
| Author | Bhadrācala Rāmadāsu (Kañcarla Gōpanna), 17th c. |
| Source | Telugu Wikisource, *పలుకే బంగారమాయెనా* (`{{PD-old}}`) |
| URL | `te.wikisource.org/wiki/పలుకే బంగారమాయెనా` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | pallavi + 5 caraṇas; rāgam Ānandabhairavi, tāḷam Ādi. Structural labels (ప:/చ N:) and the inline `\|\| పలుకే \|\|` refrain cues are dropped; the pallavi is shown once. |

### 6.3 Gajendra Mokṣam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Author | Bammera Pōtana, 15th c. |
| Source | Telugu Wikisource, *పోతన తెలుగు భాగవతము / అష్ఠమ స్కంధము* — sections *గజేంద్రుని దీనాలాపములు* (8-71, 8-73…8-77, 8-90) and *విష్ణువు ఆగమనము* (8-96) |
| URL | `te.wikisource.org/wiki/పోతన తెలుగు భాగవతము/అష్ఠమ స్కంధము/గజేంద్రుని దీనాలాపములు` (and `…/విష్ణువు ఆగమనము`) |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | 8 padyams: the lament (8-71 *ē rūpambuna*), the "evvanicē janiñcu jagamu" stuti (8-73…8-77), the strength-gone plea (8-90 *lāvokkintayu*), and Viṣṇu's headlong rescue (8-96 *sirikiṃ jeppaḍu*). The page's yati/prāsa markup (`<u>`/`<b>`), word-gloss (టీక), and Telugu paraphrase (భావము) are not used — only the verse text. |

The `telIast` aid was extended for classical Telugu: the arasunna `ఁ`
(candrabindu) → `ṁ`, and `ఱ` (Dravidian *ṟa*) → `ṟ`. All Telugu pages
were regenerated.

### 6.4 Āñjaneya Daṇḍakam — `stotra/hanuman/`

| Field | Value |
|---|---|
| Form | daṇḍaka (continuous flowing lines, no verse numbers) |
| Source | Telugu Wikisource, *ఆంజనేయ దండకం* |
| URL | `te.wikisource.org/wiki/ఆంజనేయ దండకం` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | Sanskrit invocation + Telugu narrative of Hanumān's Rāmāyaṇa deeds + closing namaskāra. Rendered as 8 flowing segments (the source's paragraph breaks); the see-also/category wiki markup is dropped. New `stotra/hanuman/` deity folder. |

### 6.5 Narasiṃha Daṇḍakam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Form | daṇḍaka (folk-devotional, 8 short stanzas) |
| Source | Telugu Wikisource, *నరసింహ దండకము* |
| URL | `te.wikisource.org/wiki/నరసింహ దండకము` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | Telugu-language hymn to Narasiṃha weaving in praise of the name of Rāma. A few colloquial phrases are obscure and are rendered by apparent sense (flagged in the page note). |

### 6.6 Brahma Kaḍigina Pādamu — `stotra/venkateshwara/`

| Field | Value |
|---|---|
| Author | Annamācārya (Annamayya), 15th c. |
| Source | Telugu Wikisource, *బ్రహ్మకడిగిన పాదము* |
| URL | `te.wikisource.org/wiki/బ్రహ్మకడిగిన పాదము` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | kīrtana on the feet of Veṅkaṭeśvara: pallavi + 3 charaṇas. The `ప|| చ||` pallavi/charaṇa markers and the page's romanized copy are not used. |

### 6.7 Koṇḍalalō Nelakonna — `stotra/venkateshwara/`

| Field | Value |
|---|---|
| Author | Annamācārya (Annamayya), 15th c. |
| Source | Telugu Wikisource, *కొండలలో నెలకొన్న* |
| URL | `te.wikisource.org/wiki/కొండలలో నెలకొన్న` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | kīrtana on Veṅkaṭeśvara (rāgam Hindōḷam): pallavi + 3 charaṇas alluding to his legendary devotees. Markers and romanized copy not used. |

### 6.8 Jo Achyutānanda — `stotra/venkateshwara/`

| Field | Value |
|---|---|
| Author | Annamācārya (Annamayya), 15th c. |
| Source | Telugu Wikisource, *జో అచ్యుతానంద జోజో ముకుంద* |
| URL | `te.wikisource.org/wiki/జో అచ్యుతానంద జోజో ముకుంద` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | a cradle-song (jōla, rāgam Navarōju) to the child Kṛṣṇa: pallavi + 4 charaṇas. Romanized copy not used. |

### 6.9 Śrīman Nārāyaṇa — `stotra/venkateshwara/`

| Field | Value |
|---|---|
| Author | Annamācārya (Annamayya), 15th c. |
| Source | Telugu Wikisource, *శ్రీమన్నారాయణ* |
| URL | `te.wikisource.org/wiki/శ్రీమన్నారాయణ` |
| Recorded | 2026-07-25 |
| Text status | public domain |
| Content | surrender at the Lord's feet on a garland of *kamala* (lotus) epithets: pallavi + 2 charaṇas. Mostly Sanskrit in Telugu script; the ప\|\| చ\|\| markers not used. |

### 6.10 Nānāṭi Batuku Nāṭakamu — `stotra/venkateshwara/`

| Field | Value |
|---|---|
| Author | Annamācārya (Annamayya), 15th c. |
| Source | Telugu Wikisource, *నానాటి బదుకు నాటకము* |
| URL | `te.wikisource.org/wiki/నానాటి బదుకు నాటకము` |
| Recorded | 2026-07-27 |
| Text status | public domain |
| Content | philosophical kīrtana — everyday life a play, the unseen Reality kaivalya: pallavi + 3 charaṇas. The verse text uses బతుకు (batuku), the page title బదుకు (baduku). |

### 6.11 Rukmiṇī Kalyāṇam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Author | Bammera Pōtana, 15th c. |
| Source (authoritative) | *Bammera Potanamatya Praneeta Sri Mahabhagavatamu, with Commentary*, Vol. VI (Skandha 10-1). Commentary by Dr. Appajodu Venkatasubbaiah, Dr. A.S. Gopal Rao, Sri Prabhala Subrahmanya Sarma, Dr. P. Narasimha Reddy, Vidwan Mudivarthi Kondamacharyulu and Dr. P.R. Harinath; edited by Dr. Samudrala Lakshmanaiah. T.T.D. Religious Publications Series No. 1242, published by Tirumala Tirupati Devasthanams, Tirupati; first edition 2017. © TTD, all rights reserved. PDF supplied by the maintainer. |
| Recorded | 2026-10-18 |
| Range | verses 10.1-1680 to 10.1-1792 (book pp. 681–737; PDF pages 757–818): from *రుక్మిణీ కల్యాణ కథాప్రారంభము* to the wedding, with Śuka's closing verses (1790–1791) and the skandha's closing gadya (1792). 113 units: 75 padyams, 38 vacanams. |
| Text status | Pōtana's verse text is public domain. Only the verses are reproduced; the edition's ప్రతిపదార్థం (word meanings), తాత్పర్యం (paraphrase), విశేషం notes, introduction and index are not used. The English translations and headings are original. |

**Text.** The TTD edition is the authority for every reading. The text was
taken from the PDF's text layer, set in the Priyaanka DTP font, by
`scripts/priyaanka.py` (§7.4), reading only Pōtana's lines (PriyaankaBold,
18 pt; the section titles are 22 pt). For this book the converter gained the
Mac-Roman forms `∆` `µ` of the ṣa-vattu and u-sign, `€` (ḍa-vattu), `ñ`
(arasunna ఁ) and `రీ`+`î` (ఠీ) — additions only, so the Gītā conversion is
unchanged. It is run with `alveolar_ra=True`, which reads this book's glyph
`é` as **ఱ** (plain ర is `~`; the Gītā book has no ఱ and keeps `é` as ర) and
its two-glyph `|Ú` as ఋ (one occurrence, 1720). No reading has been changed; in particular nothing has been
"corrected" towards Telugu Wikisource or any other edition.

**Conventions (presentation, not text).**
- The metre labels (క. మ. ఉ. సీ. తే. ఆ. శా. చ. మత్త. మాలిని. గ. వ.) are taken out of
  the line and named in each translation, e.g. *[Sīsam with tēṭagīti]*. The
  book labels 1757 *వి.*, a vacanam; the translation calls it a vacanam.
- Verse lines are the book's lines. Prose (vacanam, gadyam) also keeps the
  book's line breaks, because the PDF does not record whether a line ends
  between words or inside one (the book wraps mid-word: *వాఁ / డితూపులం*).
- Verse numbers are the book's 10.1 series, shown as `॥ 1680 ॥` etc.
- The six section titles of the book are given as English headings.
- 1705: the avagraha of *లోకమనోఽభిరాముఁ* is set below the line in the book, and
  the PDF put it on a row of its own; it is restored in place.

**Word-by-word lists (2026-10-19).** All 113 units carry a list in
`tools/words/rukmini-kalyanam.txt`, made from the TTD text by the Telugu-page
conventions (§6, and the note after §7.4): Telugu-script words, unhyphenated,
with the sandhi resolved (*డమరేంద్రు* → *అమరేంద్రున్*); the long prose compounds
of the vacanams are glossed as units. The meanings are original.
`words_check.py` passes all 113.

**Check against a witness (2026-10-18).** The converted text was compared
verse by verse with Telugu Wikisource's Pōtana Bhāgavatam (same numbering).
After the two conversion fixes below, 27 of 113 units match exactly. The
remaining differences are the two editions' own: సేయు for చేయు, placement of
arasunna, Wikisource keeping a sīsa's pendant verse separately, and genuine
variant readings (1702 *వచ్చితి వయ్య నీవు* / *వచ్చితి రయ్య మీరు*, 1745 without
*ఫలంబులు*, 1757 without *విస్ఫోటితకపాలంబును*, 1766, 1779, 1781 …). These
follow TTD.

**Checked against the page images (2026-10-20).** The seven places where the
comparison could have hidden a conversion slip were read in the PDF's page
images (400 dpi crops of the verse lines):

| Verse | Book prints | Wikisource | Result |
|---|---|---|---|
| 1687 | అనయుఁడు | అనఘుఁడు | book's reading, kept |
| 1720 | ఋగ్యజుస్సామాథర్వణ | ఋగ్యజుస్సామ… | **conversion slip** (బు) — fixed |
| 1757 | వీకీర్ణ | వికీర్ణ | book's reading, kept |
| 1771 | హతప్రాయుండై | హతప్రాణుండై | book's reading, kept |
| 1786 | వరమానందము | పరమానందము | book's reading, kept |
| 1788 | రుక్మిణతోడ | రుక్మిణితోడ | book's reading, kept |
| 1791 | పోషీ | తోషీ | book's reading, kept |

The images also showed that the book **does** print ఱ (చిఱునగవు, గొఱిగి,
తెఱఁగున, కొఱకు, మఱియు …), which the first conversion had turned into ర; the
earlier note here that TTD "writes ర for ఱ" was wrong. All 80 ఱ are restored
(78 words in the word list), and a check confirmed the text changed by
ర → ఱ alone. No ర-against-ఱ difference with Wikisource remains.

### 6.12 Pōtana Bhāgavatam (the whole work) — `stotra/bhagavatam/`

| Field | Value |
|---|---|
| Author | Bammera Pōtana, 15th c. (with the portions traditionally ascribed to his successors, as the edition prints them) |
| Source (authoritative) | *Bammera Potanamatya Praneeta Sri Mahabhagavatamu, with Commentary*, Vols. I–VIII, T.T.D. Religious Publications Series Nos. 1237–1244, Tirumala Tirupati Devasthanams, Tirupati; first edition 2017. Vols. I–II ed. Vidwan Mudivarthi Kondamacharyulu; III–VIII ed. Dr. Samudrala Lakshmanaiah. © TTD, all rights reserved. PDFs supplied by the maintainer. |
| Recorded | 2026-10-21 |
| Range | all twelve skandhas, 9,010 units in the book's numbering per part (1: 529 · 2: 288 · 3: 1,055 · 4: 977 · 5.1: 184 · 5.2: 168 · 6: 530 · 7: 482 · 8: 744 · 9: 737 · 10.1: 1,792 · 10.2: 1,343 · 11: 127 · 12: 54) |
| Text status | Pōtana's verse text is public domain. Only the verses are reproduced; the edition's ప్రతిపదార్థం, తాత్పర్యం, విశేషం, introductions, story summaries and indexes are not used, nor are its section titles (the English headings in `tools/bhagavatam/headings.tsv` are original). |

**Text.** Extracted from the eight PDFs by `tools/bhagavatam/extract.py`, which
reads only Pōtana's lines (PriyaankaBold, 17–19.7 pt), the margin verse
numbers and the running heads that name the skandha, and converts them with
`priyaanka.py` (`alveolar_ra=True`, as for §6.11; it gained `i≠` → ఝి for this
work). An audit found every part's numbering complete, with no gaps, repeats
or unconverted glyphs. The extractor's own repairs:
- each part's opening verse begins with a 25-pt drop-cap శ్రీ, which is
  restored to the line (the book prints no metre label on these verses);
- a unit split across a page turn is rejoined; bare commentary labels set at
  verse size, and the closing *శ్రీకృష్ణార్పణమస్తు*, are dropped;
- 10.2-275 *ధాతునిర్ఝరరంజిత*: the text layer lacks the ఝ, which was read
  from the page image.

The reviewed Rukmiṇī Kalyāṇam text (§6.11) is reproduced exactly: 113 of 113.

**Check against a witness (2026-10-21).** All units were compared with Telugu
Wikisource's Pōtana Bhāgavatam (8,990 verses, fetched once, politely, for
comparison only), allowing for the two editions' numbering drifting by up to
eight. The commonest differences are the editions' spelling: TTD prints the
sandhi changes (చ→స, క→గ, త→ద, ప→వ/బ: *సముల్ సనునెడ*), ై where Wikisource has
యి and the reverse, and differs in placing arasunna. There is no sign of a
systematic glyph error. The units with no close match are short vacanams
(*మఱియును*, *అంత*) or stretches where the numbering drifts further. As with
§6.11, no reading is changed towards Wikisource.

**Presentation.**
- Pages hold whole story sections, at most about 120 units, and a longer
  section is split into "(continued)" pieces. Each part (skandha, or āśvāsa /
  half for 5 and 10) has a contents page, and `bhagavatam-iast.html` lists the
  parts. Links run through the whole work.
- Unlike §6.11, each unit keeps the book's metre label at its head (*క.*, *సీ.*,
  *వ.* …), since there is no translation yet to name it in; a vacanam or gadyam
  is set as prose. Lines are the book's lines; numbers are the book's, `॥ N ॥`.
- Text first: translations and word lists will be added over time. Verses
  10.1-1680…1792 already carry the Rukmiṇī Kalyāṇam translations and word
  lists, and 8-71, 73–77, 90 and 96 the Gajendra Mokṣam translations.
- The data files (`tools/stotras/bhagavatam-*.py`) were written by
  `tools/bhagavatam/gen.py` and are now the source to edit.

## 7. Sanskrit work from a scanned modern edition

### 7.1 Vedānta Ḍiṇḍima — `stotra/advaita/`

| Field | Value |
|---|---|
| Work | *Vedānta Ḍiṇḍima* ("The Kettledrum of Vedānta"), 94 verses |
| Author | traditionally ascribed to Śrī Śaṅkarācārya |
| Digital source | scanned PDF in the "Vedanta Students" archive.org collection (`dn720002.ca.archive.org/0/items/vedanta-students/.../022.-Vedanta-Dindima.pdf`) — a verse-by-verse presentation with Devanāgarī, IAST, and an English translation |
| Recorded | 2026-07-27 |
| Obtained via | the maintainer supplied the URL; the IAST was **transcribed by hand** from the page images (the Sanskrit sits in embedded images, so no text layer exists) and cross-checked **verse by verse against the printed Devanāgarī** |
| Used for | the 94 public-domain **verses** only (IAST) |

**Licensing analysis.** The verses themselves are public domain by age
(an old Advaita *prakaraṇa* text). The scanned PDF, however, is a
**copyrighted modern compilation** — its page layout and, in particular,
its **English translation are the editor's work and are NOT used here**.
Only the ancient verses were extracted; every English translation on the
page is **original work by the maintainer**, written from the Sanskrit,
not derived from the edition's translation.

> **Unresolved.** Because the only copy consulted is a copyrighted modern
> edition, **commercial redistribution of this work is blocked** until the
> 94 verses are re-keyed against an independent public-domain print
> edition of the *Vedānta Ḍiṇḍima* (or explicit permission is obtained).
> Non-commercial personal use is unaffected. The verses were transcribed
> under the project's "no silent emendation" rule; a handful of the
> edition's IAST typos (e.g. *yanmadye* → *yanmadhye*, *prahiṇo* →
> *prahīṇo*) were corrected against the facing Devanāgarī and are noted
> here rather than passed through silently.

### 7.2 Śrī Satyanārāyaṇa Vratakalpam — `stotra/vishnu/`

| Field | Value |
|---|---|
| Work | *Śrī Satyanārāyaṇa Vratakalpa* — the complete vrata: preliminaries, saṅkalpa, Gaṇapati pūjā, pañcalokapāla, navagraha and aṣṭadikpāla pūjā, the ṣoḍaśopacāra pūjā of Satyanārāyaṇa (Puruṣa Sūkta + Śrī Sūkta), and the five-chapter *vrata-kathā* of the Skānda Purāṇa, Revākhaṇḍa |
| Tradition | Annavaram (Śrī Vīra Veṅkaṭa Satyanārāyaṇa Svāmi devasthānam) |
| Digital source | `Satyanarayana_Vratakalpamu_Combined.htm` — the maintainer's own Word compilation, keyed from a couple of **Telugu-script vratakalpam booklets from Annavaram** |
| Recorded | 2026-09-26 |
| Obtained via | Telugu script → IAST by a code-point shift to Devanāgarī plus the skill's `dev2iast.py`; every block then re-set by hand against the extraction |
| Used for | the Sanskrit text only (IAST source of truth; 289 text blocks, 1,405 padas, 52 section headings, 16 English rubrics) |

**Licensing analysis.** The Sanskrit — Vedic mantras, Purāṇic ślokas, the
kathā, the ritual formulae — is public domain by age. The booklets are
**copyrighted modern editions**: their Telugu directions and their Telugu
*tātparya* (a prose meaning under every kathā verse) are **not reproduced,
paraphrased or translated here**. The page's English rubrics are the
maintainer's own brief statement of the ritual steps, and every gloss is
**original work by the maintainer, translated from the Sanskrit**.

> **Unresolved.** As with §7.1, the only copies consulted are modern
> booklets. Before any **commercial** redistribution, re-check the Sanskrit
> against an independent public-domain print of the vratakalpa (or obtain
> permission). Non-commercial use is unaffected.

**Scope.** Included: everything from the opening mantras through the
*maṇṭapa-dāna* and the closing colophon. **Omitted**, with reason: the Telugu
material described above; the booklet's list of required articles (a
shopping list, summarised in the first rubric); and the **Viṣṇu
Sahasranāmāvaḷi** appended after the colophon — the site already carries the
Sahasranāma stotra (§5.21), and the Word export had scrambled the
nāmāvaḷi's table order beyond reliable recovery.

**Normalisation (orthographic, not textual).** Applied throughout, following
site convention: word division re-set (Telugu print splits words at
geminates and vowel boundaries — *muhūrta ssumuhūrtostu* →
*muhūrtassumuhūrto'stu*, *bhagavā nuvāca* → *bhagavānuvāca*); anusvāra before
a stop written as the class nasal (*gaṃdha* → *gandha*); Telugu ళ in Sanskrit
words written *l* (*maṅgaḷa* → *maṅgala*), except the bīja *ḷaṃ*; missing
avagraha supplied (*namostute* → *namo'stu te*); Telugu aspirate spellings of
*artha* (*prītyardhaṃ* → *prītyarthaṃ*); *mahālakṣmi-* → *mahālakṣmī-* in the
recurring offering formula; Taittirīya anusvāra kept as *gṃ* (renders గ్ం /
ग्ं exactly as the source); the book's daṇḍa placement kept, with `|`/`||`
supplied at half-verse ends. Section labels (*dhyānaṃ*, *maṃ॥*, *ślo॥*,
*tā॥*) are dropped as markup. Vedic mantras carry no svaras (the source has
none).

**Table order restored.** The Word export flattened nine multi-column
tables row by row. Column order was restored, and each list set-checked
against the standard sequence so no name is lost or invented:
the 24 ācamana names (3 columns); the 16 Gaṇapati names (3 columns); the
karanyāsa and aṅganyāsa (2 columns); the Kṛṣṇa and Lakṣmī aṣṭottaras (one
interleaved table); the navagraha and dikpāla placement tables (rendered as
English rubrics).

**Additions.** The book's Lakṣmī aṣṭottara has 105 names. Three missing names
were restored at their standard positions: **#30 anugrahapradāyai, #55
prasādābhimukhyai, #58 candrāyai**, giving 108. The popular printed list
repeats *devyai* a third time (after *dāridryadhvaṃsinyai*, making 109); the
book omits it, and so does this page.

**Book readings kept** (variants, not errors): Kṛṣṇa aṣṭottara —
*madhurānāthāya*, *bṛndāvanānta-*, *avyaktagītāmṛtamahodadhaye* as one name,
*tīrthapādāya*, *sarvadevātmakāya*, and a closing *śrīsatyanārāyaṇaparabrahmaṇe*;
Lakṣmī — *śivakartryai*, *tuṣṭaye*, *dhanadhānyakartryai*,
*viṣṇuvakṣasthalasthitāyai*; the Āndhra Śrī Sūkta order (*ārdrāṃ puṣkariṇīṃ …
suvarṇāṃ … sūryāṃ* at dīpa, *ārdrāṃ yaḥ kariṇīṃ … piṅgalāṃ … candrāṃ* at
naivedya) and *jātavedo mamāvaha*; *kalaśaṃ tu samāśritāḥ*,
*mātṛgaṇāśritāḥ*; the navagraha dhyāna verses as printed (including the
repeated *tathāsidaṇḍaṃ* line for Guru and Śukra); the ṛṣi name *hiḷimbhiṣi*;
kathā readings *papracchurānataṃ*, *svargamartyeṣu*, *bilvamūlaṃ* (Ch. 5),
*satyavratarūpe*, *dhanadhānyādhikaṃ*.

**Corrections to the book's text** (each against the standard reading):

- *Preliminaries / saṅkalpa:* *bṛhaspatiḥ prasūtāḥ* → *bṛhaspatiprasūtāḥ*;
  *oṃ māpo* → *oṃ āpo*; *prītyarthyaṃ* → *prītyarthaṃ*; *dvitīya parārthe* →
  *dvitīyaparārdhe*; *vartamāna vyāvahārika* → *vartamāne vyāvahārike*;
  *brahma madhye* → *brahmā madhye*; *chandāgṃṣi* → *chandāgṃsi*.
- *Gaṇapati:* *upamaśravastavaṃ* → *upamaśravastamam* (×3); *dathātana* →
  *dadhātana*; *vaśśitamo* → *vaśśivatamo*; *pūjamānaḥ* → *pūyamānaḥ*;
  *yajñopavīṃ* → *yajñopavītaṃ*; *dūrvādussvapna* → *dūrvā duḥsvapna*;
  *pūjāyāca* → *pūjayā ca*.
- *Lokapālas:* *brahma devānāṃ* → *brahmā devānāṃ*; *gaurīmimāya* →
  *gaurīrmimāya* (×2); *sahasrākṣaparā* → *sahasrākṣarā*.
- *Navagraha:* *asatyena* → *ā satyena*; *saptā'śvorko* → *saptāśvo'rko*;
  *lokavapuḥ* → *lokaguruḥ*; *tavasye* → *tavyase*; *pratajmukhaṃ* →
  *pratyaṅmukhaṃ*; *bheṣaja* → *bheṣajā*; *kujastvaṃvantī* →
  *kujastvavantī*; *bharadhvāja* → *bharadvāja*; *pṛthivībhavā vṛkṣarā …
  śarmanaprathāḥ* → *pṛthivi bhavānṛkṣarā … śarma saprathāḥ*; *jayāmasī …
  poṣayitvā* → *jayāmasi … poṣayitnvā*; *kṛṇvaggṃ … tvayi* → *kṛṇvagṃs …
  ttvayi*; *bhūrbhuvasvaḥ* → *bhūrbhuvassuvaḥ*; *padmasthamalāpatiṃ* →
  *padmasthaṃ kamalāpatim*; *arhādyumad … śavasarta … dehi* → *arhāddyumad …
  śavasa ṛta- … dhehi*; *sabuddhiyā* → *sa budhniyā*; *parivāsametaṃ* →
  *parivārasametaṃ*; *patnīpīḍośāṃtaye* → *patnīpīḍopaśāntaye*;
  *svarṇānbhāṃ* → *svarṇābhāṃ*; *maśruvaṃ* → *maśravam*; *indramarutvaṃta miha*
  → *indra marutva iha*; *saurī* → *sauriḥ*; *skara cchanna* → *skaracchaṃ
  na*; *apastridhaḥ* → *apa sridhaḥ*; *prajāpate satvadetā … vayagg …
  patiyo* → *prajāpate na tvadetā … vayagṃ … patayo*; *parivāra* (typo
  *paravāra*); *rāhū-* → *rāhu-*; *sadanmātara ssuvaḥ pitaraṃ ca priyaṃtsuvaḥ*
  → *sadanmātaraṃ puraḥ pitaraṃ ca prayantsuvaḥ*; *madhucchaṃda* →
  *madhucchandā*; *duvasva* → *yuvasva*; *sāyudhāṃ* (Brahmā, typo) →
  *sāyudhaṃ*.
- *Dikpālas:* *nirbuti … sadīṣṭa* → *nirṛti … padīṣṭa*; *śṛdhī* → *śrudhī*;
  *adbhutā avāṃsyā* → *adbhuta avāgṃsyā*; *dadātu … pituśravaṇaṃ* → *dadāti …
  pitṛśravaṇaṃ*; *jinvamanase … vedanām … adabdha* → *jinvamavase … vedasām …
  adabdhaḥ*.
- *Satyanārāyaṇa pūjā:* *dadhikrāvuṇṇa* → *dadhikrāvṇṇa* (Telugu vowel
  spelling); *ṛtāya te* → *ṛtāyate*; *suhavetu* → *suhavītu*; *araṃgga …
  kṣamāya* → *araṃ gamāma … kṣayāya*; *ṛgyajussāmādharvaṇāni* →
  *-ātharvaṇāni*; *asunīte … mihino … vaiprāṇa* → *… miha no … vai prāṇā*;
  *jyāyāgśca* → *jyāyāgṃśca*; *viśvabhūtāni* → *viśvā bhūtāni*; *sa jātotyaricyata
  … madho* → *sa jāto atyaricyata … matho*; *alakṣmīr … sarvān* →
  *alakṣmīṃ … sarvāṃ*; *saṃbhṛtaḥ … tāg ścakre … grāmyāṃ ścaye* →
  *sambhṛtaṃ … tāgṃścakre … grāmyāśca ye*; *kardamā* → *kardama*; *katithā*
  → *katidhā*; *apasrajaṃtu* → *āpassṛjantu*; *sauvarṇa* → *sauvarṇe*;
  *satyaṃtyartena* → *satyaṃ tvartena*; *ekathā* → *ekadhā*; the *narya
  prajām* passage: *adharva … abaddhāyo … śaggsya … aśugāḥ … hi gṃsī jjātavedo
  … abhibhrad* → *atharva … adabdhāyo … śagṃsya … āśugāḥ … higṃsījjātavedaḥ …
  abibhrad*; Nārāyaṇa Sūkta *vyāpyanārāyaṇasthsitaḥ … tasmin tsarvaṃ …
  vyavasthitaḥ* (flame) → *vyāpya nārāyaṇassthitaḥ … tasminsarvaṃ …
  vyavasthitā*; *sāhiṇe* → *sāhine*; *jāgṛvāṃsaḥ* → *jāgṛvāgṃsaḥ*; *rakṣa
  rakṣa rakṣa* → *rakṣa rakṣa* (metre); *vistārayatu* → *nistārayatu*.
- *Kathā:* *mārtakaṃ* → *mārtikaṃ*; *satprateḥ* → *satpateḥ*; *satyanārāyaṇa
  devaṃ* → *satyanārāyaṇaṃ devaṃ*; *vidhāyādau vevaṃ* → *vidhāyādāvevaṃ*;
  *bhikṣārtha magama* → *bhikṣārthamagamad*; *ka(ki)manyat* (the book's own
  correction) → *kimanyat*; *dadāsādhuḥ* → *dadau sādhuḥ*; *putrī* → *putri*
  (vocative); *santuṣṭo satya-* → *santuṣṭassatya-*; *bhayavihvalāḥ* →
  *bhayavihvalau* (dual); *pādukai stasya* → *pāduke tasya*; *sā'paśyat
  punarāgatya* → *sā paścātpunarāgatya*; *saṃtuṣṭāṃ* (cowherds) →
  *santuṣṭā*; *kecitkālau* → *kecitkalau*; *īpsitapradaku* →
  *īpsitapradam*; *sarveṣāmipsita* → *sarveṣāmīpsita*; *devaśya* →
  *devasya* (maṇṭapa-dāna). The closing Telugu colophon *… vratakalpamu
  samāptamu* is given in Sanskrit as *… vratakalpaḥ samāptaḥ*.

**Builder.** `tools/build_stotra.py` gained three optional section types,
used first by this page and inert for every other: `{"heading": …}` (the
shell's existing `.speaker` style), `{"rubric": …}` (the `.colophon-gloss`
style, for the English ritual directions), and a verse flag `"prose": True`
(the existing `.viniyoga` style, one size down, for long formulae). All are
Latin and outside `.sans`, so they are never transliterated.

**Verification.** All 1,405 padas round-trip IAST → Devanāgarī → IAST with
`scripts/verify.py` / `dev2iast.py` with zero differences, and a
convention-normalised character diff against the source text leaves only the
logged items above, the table reorderings, and the omitted Telugu.

### 7.3 Mahānyāsam (accented) — `stotra/shiva/`

| Field | Value |
|---|---|
| Work | *Mahānyāsa* of Bodhāyana — the five *nyāsa*s of Rudra's mantras on the body (pañcāṅga and pañcamukha dhyāna, the limbs, the ten syllables, feet-to-crown with the Haṃsa Gāyatrī, the enclosed *digdevatā*, *daśāṅga* and *ṣoḍaśāṅga raudrīkaraṇa*, *ātmarakṣā*, and the six-fold fifth nyāsa with the Śivasaṅkalpa, Apratiratha, Tryambaka and Agni passages), the aṣṭāṅga praṇāma and Rudra dhyāna, the Rudra *snāna-arcana*, the elevenfold *Rudrābhiṣeka*, the *daśa śānti*, the *sāmrājya-paṭṭābhiṣeka*, a *Śivapūjā vidhi* using the *Mṛtyuñjaya-mānasa-pūjā* verses ascribed to Ādi Śaṅkara, and the Mahāśivarātri *arghya* verses |
| Edition | *Nityakarma-Pūjā Prakāśika* (Telugu script), Gita Press, Gorakhpur — pp. 622–697; year not shown in the extract used |
| Digital source | `mahanyasam.pdf` — a 76-page scan of those pages, supplied by the maintainer |
| Recorded | 2026-09-27 |
| Obtained via | a faithful page-by-page transcription made with the `scan-to-docx` skill (Telugu script, svaras as printed, page markers, footnotes; kept privately as `mahanyasam.compile.txt`); the Sanskrit extracted from it with a rule-based script (below), Telugu → IAST by the skill's `dev2iast.py` |
| Used for | the Sanskrit only (IAST source of truth; 318 text blocks, 1,375 padas, 64 section headings, 18 English rubrics) |

**Licensing analysis.** The Sanskrit — Taittirīya mantras and brāhmaṇa
passages, Bodhāyana's prose, the dhyāna and pūjā ślokas — is public domain by
age. The book is a **copyrighted modern edition**: its Telugu instructions,
Telugu footnotes and explanatory notes, and its Telugu summary of the
phalaśruti are **not reproduced, paraphrased or translated here**. Section
headings, rubrics and every gloss are the maintainer's **original English,
translated from the Sanskrit**. The rubrics state the ritual steps briefly in
our own words; where they rest on Sanskrit prescriptions printed in the book
(e.g. the list of the fifth nyāsa's six parts, Bodhāyana's own words), that
is noted in the gloss rather than the Telugu.

> **Unresolved.** As with §7.1–7.2, the only copy consulted is a modern
> edition. Before any **commercial** redistribution, re-check the Sanskrit
> against an independent public-domain print (the Mahānyāsa is widely printed
> in Devanāgarī) or obtain permission. Non-commercial use is unaffected.

**Faithfulness.** Unlike §7.2, the text is **not** re-set to a standard: the
book's readings, word division, Taittirīya spelling (*gṃ*, *ggṃ*), daṇḍas and
svaras are kept as printed, including readings that differ from the common
Taittirīya text (e.g. *vaidyu'to'si*, *bandanā*, *kṛśānū*, *hi sī dāṃgirobhiḥ*,
*site pakṣe*). The book abbreviates repeated or well-known mantras by their
first and last words with dots (*namaśśaṃbhave ca … śivatarāya ca*, the Puruṣa
Sūkta, the Namaka/Camaka); these are kept as `…`, not filled in.

**Svaras.** Taittirīya system as printed on Telugu letters: anudātta ॒,
svarita ॑, dīrgha svarita ᳚ (IAST `_`, `^`, `^^`), udātta unmarked; only the
Vedic mantras carry them. Two print conventions were read as follows during
transcription: the bar under a Telugu *ta*-vattu (స్త, న్తి) is an anudātta
only where that syllable is anudātta; a mark that sits between two akṣaras is
assigned by the standard accentuation. The page opens in Devanāgarī; a
byte-level comparison of every accented block against the source (Telugu
shifted to Devanāgarī) matches exactly, apart from the one spelling noted
below.

**Omitted** (Telugu-language, with reason: the edition's own work): all
footnotes; the parenthetical Telugu notes and section-closing lines (*… nyāsamu
mugisinadi*); the Telugu introduction to the Rudrābhiṣeka (p. 672) and its
closing instructions (p. 674); the Telugu labels of the pañcāmṛta items
(*pālu, perugu …*); cross-references to other pages of the book; the
Mahāśivarātri note before the arghyas; and the Telugu *mukhyāṃśamulu* notes
(p. 696–697), of which only the Sanskrit śloka *ekā caṇḍyā raveḥ sapta …* is
kept. The book's Telugu section titles are replaced by IAST + English
headings.

**Normalisation (orthographic, not textual).** Telugu ళ written *l* (site
convention); the vocalic-ḷ bīja ఌం written **Ḷṃ** (capital), which the
renderer maps to ऌं / ఌం — lower-case *ḷ* is its consonant ळ — and ౡం as
*ḹṃ*; the book's నిర్ృతి / నిర్ృతే (*r* + virāma + *ṛ*) written *nirṛti*,
rendering निरृति; the verse label *ślo॥*, footnote markers, exclamation marks,
quotation marks, the dashes the book sets between pādas, and a label colon
(*karanyāsaḥ :*) dropped; Telugu numerals and the book's verse numbers moved
into the `|| N ||` badge; the book's line breaks re-flowed at daṇḍas for the
Vedic prose (they are printer's wraps), but kept as printed in the Śivapūjā,
which is set one pāda per line.

**Uncertain readings** (damaged or faint print; best reading adopted):
*atithir duroṇasat* (p. 626, *thi* unclear); *oṃ namo bhagavate rudrāya*
(p. 641, *namo* faint); *manuṣyānnenmi yate* (p. 648, Śivasaṅkalpa 5 — the
book's reading; the standard text has *manuṣyānnenīyate*); *muñcantvagṃhasaḥ*
(p. 668, *muñca* faint). On p. 668 the opening words of the two lines of the
akṣata-water mantra (*… parāyaṇe dūrvā rohantu …*) are illegible in the scan
and appear as `…`.

**Shell, converter and verifier.** The shared shell's `devSvara` now also
renders `^^` as the dīrgha svarita ᳚ (and keeps it after a visarga/anusvāra
like the other marks); `dev2iast.py` emits `^^` for U+1CDA, and `verify.py`
understands both it and the capital-Ḷ vocalic *ḷ*. Pages without `^^` render
exactly as before (the rebuild changes only the shell's script text).

**Verification.** All 1,375 padas round-trip IAST → Devanāgarī → IAST with
`verify.py --data mahanyasam`: zero failures.

### 7.4 Bhagavad Gītā with Śaṅkara's bhāṣya — `stotra/gita/`

| Field | Value |
|---|---|
| Work | *Śrīmad Bhagavad Gītā* (Mahābhārata, Bhīṣma Parva), 18 chapters, 700 verses, with the *Gītābhāṣya* of Śaṅkara Bhagavatpāda: his introduction (*upodghāta*, printed as *sambandha-bhāṣya*), the chapter prefaces, the commentary on 2.10–18.78, and the colophons |
| Primary edition | *Śrīmadbhagavadgīta Śaṅkarabhāṣyamu (saṃskṛta mūlamu – telugu anuvādamu)*, Telugu translation by Sūraparāju Rādhākṛṣṇamūrti, Ramakrishna Math, Hyderabad, 2013 (ISBN 93-83142-63-7), 590 pp. — "© Ramakrishna Math, Hyderabad. All rights reserved" |
| Digital source | archive.org item `bhagavad-gita-by-sri-adi-shankaracharya` — `భగవద్గీత శంకర భాష్యము.pdf` (2.5 MB, a born-digital PDF with a text layer in the legacy *Priyaanka* Telugu font), fetched 2026-09-28 |
| Second witness | archive.org item `srimadbhagavadgita-telugu-shankaracharyabhashya-translatedbyshripulleysramachandra` — *Srimad Bhagavadgita, Telugu, Śaṅkarācārya bhāṣya, translated by Pullela Śrīrāmacandruḍu* (image scan, 183 MB; its OCR text `Gita (pullela)_djvu.txt` used) |
| Third witness | Sanskrit Wikisource, *भगवद्गीताभाष्यम् -श्रीशङ्करकृतम्* (chapters 1–17) and *भगवद्गीता/मोक्षसंन्यासयोगः* (its *शाङ्करभाष्यम्* sections, chapter 18), fetched 2026-09-28 |
| Recorded | 2026-09-28 |
| Used for | the Sanskrit only — mūla and bhāṣya (IAST source of truth; 1,401 verse padas, 1,145 bhāṣya paragraphs, 35 colophons) |

**Licensing analysis.** The Gītā and Śaṅkara's commentary are public domain
by age. Both printed editions are **copyrighted modern works**: their Telugu
translations (the Ramakrishna Math edition's *te.a.* paragraphs after every
verse and bhāṣya paragraph, its *rā.kṛ.* and *a.a.* notes; Pullela's *pra-a.*
word-glosses and *Bālānandinī* exposition), prefaces, section titles and
indexes are **not reproduced, paraphrased or translated here**. The verse
translations are the maintainer's **original English, made from the
Sanskrit**; the chapter notes are original. The **bhāṣya translation** — an
English rendering under every one of the 1,145 paragraphs (introduction,
chapter prefaces and commentary) — is likewise the maintainer's original work,
made directly from the collated Sanskrit; neither edition's Telugu nor any
published English translation of the bhāṣya was consulted or paraphrased. It
follows Śaṅkara's sentence order closely (glosses such as "X, that is, Y" are
kept), and the scripture he cites is rendered afresh. The editions' bracketed source references
inside the bhāṣya — e.g. *(2.19)*, *(bṛ.u.3.5.1)* — are kept, as they are
factual citations of the passages Śaṅkara quotes.

> **Unresolved.** As with §7.1–7.3, the base text is a modern edition's
> setting of a public-domain work, published under an all-rights-reserved
> notice. Its Sanskrit has been collated against two other witnesses (below),
> but before any **commercial** redistribution, re-check against a
> public-domain print (e.g. the Ānandāśrama or Vani Vilas editions) or obtain
> permission. Non-commercial use is unaffected.

**Method.** The PDF's text layer stores glyph codes, not letters, in visual
order: consonant bodies, talakaṭṭu ticks, vowel-sign pieces, subscript
(*vattu*) glyphs after the vowel sign, and the ra-vattu and e-sign pieces
*before* the base they belong to. A converter written for this book maps each
of the font's ~215 glyphs (charted and read by eye, then checked) to its role,
groups them into akṣaras and emits canonical Unicode (base + virāma-conjuncts +
vowel sign + anusvāra/visarga). It was calibrated on the 700 verses against
Wikisource: 96% of verse words matched exactly on the first pass, and every
remaining difference was traced either to the book's own spelling or to a
glyph rule, fixed and re-checked against the page image. The book's layout
was then parsed: Sanskrit is set in bold, the Telugu translation in regular
weight, verses under *mū.* with the number in the margin, bhāṣya paragraphs
under *bhāṣyam :* with the book's paragraph numbers (*N.0* = the lead-in
before verse *N*, *N.k* = commentary on it, *0.k* = the chapter's preface).
All 700 verses were recovered (47, 72, 43, 42, 29, 47, 30, 28, 34, 42, 55, 20,
34, 27, 20, 24, 28, 78).

**Collation and corrections.** Each chapter was diffed against Wikisource.
The book prints Śaṅkara with words split apart (*padaccheda*: *tasmāt*,
*saḥ ādikartā*, *ādīn agre*), so differences at the book's word boundaries are
sandhi and were set aside (about 10,800). Of the ~1,600 differences *inside*
a word, the Pullela edition's OCR was searched for each reading: where it
supports Wikisource and not the book, and on review the book's form is a
misprint (a non-word, a transposed, dropped or doubled letter), the reading is
corrected; everything else — real variants, and Telugu-print sandhi spellings
such as *prakṛtis sūyate* and *niśśreyasa* — is kept as printed. In the
verses, 7.11 and 11.49 were also decided by the metre. Every correction where
the conversion itself could have been at fault was checked against the page
image first (the book does print *pāpanaṃ*, *tumulo pyanunādayan*,
*balavatām asmi*, *mālyāmarbara* …). The corrections:

*Verses (mūla):* 1.19 *tumulo pyanunādayan* → *tumulo vyanunādayan* (p for v); 1.23 *durbuddheryudde* → *durbuddheryuddhe* (d for dh); 1.26 *pauttrānsakhīṃstathā* → *pautrānsakhīṃstathā* (doubled t); 1.37 *sabāndhavān* → *svabāndhavān* (dropped v); 2.18 *tasmādyuddhyasva* → *tasmādyudhyasva* (ddhy for dhy); 3.8 *prasiddhyedakarmaṇaḥ* → *prasidhyedakarmaṇaḥ* (ddhy for dhy); 4.12 *siddhirbhavati karmajāḥ* → *siddhirbhavati karmajā* (stray visarga: siddhiḥ … karmajā); 4.42 *chitvainaṃ* → *chittvainaṃ* (chittvā printed with one t); 5.20 *brahavid* → *brahmavid* (dropped m); 7.11 *balavatāmasmi cāhaṃ* → *balavatāṃ cāhaṃ* (intrusive asmi, which breaks the metre); 8.7 *yuddhya ca* → *yudhya ca* (ddhy for dhy); 8.18 *tattrevāvyaktasaṃjñake* → *tatraivāvyaktasaṃjñake* (tattreva for tatraiva); 11.11 *divyamālyāmarbaradharaṃ* → *divyamālyāmbaradharaṃ* (rb for mb); 11.49 *mā te vyathā ca vimūḍhabhāvo* → *mā te vyathā mā ca vimūḍhabhāvo* (dropped mā, which the triṣṭubh needs); 11.52 *darśinakāṅkṣiṇaḥ* → *darśanakāṅkṣiṇaḥ* (i for a); 13.25 *tvevamājānantaḥ* → *tvevamajānantaḥ* (mājānantaḥ for majānantaḥ); 16.3 *dhrutiḥ* → *dhṛtiḥ* (dhru for dhṛ); 16.11 *pralayantāmupāśritāḥ* → *pralayāntāmupāśritāḥ* (pralayanta for pralayānta); 17.9 *tīkṣarūkṣa* → *tīkṣṇarūkṣa* (dropped ṇ); 18.22 *saktamahetukam* → *saktamahaitukam* (ahetukam for ahaitukam).

*Commentary (bhāṣya), by chapter:* **2:** *yuktattvāt* → *yuktatvāt*; *jñānottpatti* → *jñānotpatti*; *nityattvāt* → *nityatvāt*; *saṃbaddhyate* → *saṃbadhyate*; *tadhā* → *tathā* (2×); *niravayatvāt* → *niravayavatvāt*; *avasdhāyāṃ* → *avasthāyāṃ*; *tadbuddhyastadātmānaḥ* → *tadbuddhayastadātmānaḥ*; *padrarśanārdhatvena* → *pradarśanārthatvena*; *vacanārdhaviveka* → *vacanārthaviveka*; *sadbhuddhi* → *sadbuddhi*; *upariṣṭhāt* → *upariṣṭāt*; *śruṇu* → *śṛṇu* (4×). **3:** *karyaṇyeva* → *karmaṇyeva*; *varthayata* → *vardhayata*; *śatṛṃ* → *śatruṃ*. **4:** *nibaddhyate* → *nibadhyate*; *pāpanaṃ* → *pāvanaṃ*; *nirūpādhikena* → *nirupādhikena*. **5:** *tattraiva* → *tatraiva* (2×). **6:** *hāntīti* → *hantīti*; *brahīṣi* → *bravīṣi*; *saṃbanthī* → *saṃbandhī*; *bhayo-* → *bhūyo-*. **7:** *bharatavarṣabha* → *bharatarṣabha*; *tadhetu* → *taddhetu* (2×). **8:** *pratipipsitasya* → *pratipitsitasya*; *yogadhāraṇaṃ* → *yogadhāraṇāṃ*; *daivataiva* → *devataiva*; *yathāśṛte* → *yathāśrute*; *śruṇu* → *śṛṇu*. **9:** *gṛdhniṃ* → *gṛddhiṃ*; *viśeṣanirthāraṇārthaḥ* → *viśeṣanirdhāraṇārthaḥ*; *chiṃdi* → *chindhi*; *tiṣṭatyasminniti* → *tiṣṭhatyasminniti*. **11:** *ānavāni* → *ānanāni*; *sraṣṭhṛtvāt* → *sraṣṭṛtvāt*; *sāmādharvavedaiḥ* → *sāmātharvavedaiḥ*; *athunā* → *adhunā*. **13:** *avidyādhyāropitvāt* → *avidyādhyāropitatvāt*; *nirnimitvatve* → *nirnimittatve*; *dūṣayitaṃ* → *dūṣayituṃ*; *tadvitādatho* → *tadviditādatho*; *anāditvat* → *anāditvāt*; *avidyādhyārohitāḥ* → *avidyādhyāropitāḥ*; *śṛtvā* → *śrutvā*; *draṣṭatvāt* → *draṣṭṛtvāt*. **14:** *samaloṣṭāśśakāñcanaḥ* → *samaloṣṭāśmakāñcanaḥ*. **15:** *puṇyakarmiṇāṃ* → *puṇyakarmaṇāṃ*; *tadhetu* → *taddhetu*. **16:** *viṣayaṃsaṃnidhau* → *viṣayasaṃnidhau*; *sarvādhā'pi* → *sarvathā'pi*; *hrīnābhijanam* → *hīnābhijanam*. **17:** *sātvikī* → *sāttvikī*; *mūḍhagrāmeṇa* → *mūḍhagrāheṇa*; *śṛtilakṣaṇaṃ* → *śrutilakṣaṇaṃ*; *vivarthanāḥ* → *vivardhanāḥ* (2×). **18:** *sarvadhā* → *sarvathā*; *viśuddikarāṇi* → *viśuddhikarāṇi*; *phalānabhisaṃdhināmi* → *phalānabhisaṃdhīnāmi*; *tadvan* → *tadvat*; *sannyāsanya* → *sannyāsasya*; *puraṣaḥ* → *puruṣaḥ*; *darśayitumaha* → *darśayitumāha*; *tyagītyabhidhīyate* → *tyāgītyabhidhīyate*; *nibaddhyate* → *nibadhyate* (4×); *saṃbaddhyate* → *saṃbadhyate*; *saṃbadyate* → *saṃbadhyate*; *sāmanyenaiva* → *sāmānyenaiva*; *viṣameva* → *viṣamiva*; *śatṛbhyaḥ* → *śatrubhyaḥ*; *ubhayāthā'pi* → *ubhayathā'pi*; *dyaṇukādeḥ* → *dvyaṇukādeḥ*; *vidyamānavatvāvidyamānatva* → *vidyamānatvāvidyamānatva*; *taimirakadṛṣṭyā* → *taimirikadṛṣṭyā*; *pramāṇāṃtarapekṣā* → *pramāṇāṃtarāpekṣā*; *kāryākaraṇasaṃghātaṃ* → *kāryakaraṇasaṃghātaṃ*; *virudyate* → *virudhyate*; *vivakṣittvāt* → *vivakṣitatvāt*; *kartavyattvopadeśāt* → *kartavyatvopadeśāt*; *niḥśśreyasa* → *niḥśreyasa* (5×); *kaivalyaphalāvasānattvaṃ* → *kaivalyaphalāvasānatvaṃ*; *karmayakṣayānupapattiḥ* → *karmakṣayānupapattiḥ*; *dukhamātraphaleṣu* → *duḥkhamātraphaleṣu*; *upabhoganaiva* → *upabhogenaiva*; *pāsasya* → *pāpasya*; *putrānāmā'si* → *putranāmā'si*; *saghāte* → *saṃghāte*; *rārabdaṃ* → *rārabdhaṃ*; *śabdābhilāṣāt* → *śabdābhilāpāt*; *vyuthtāyātha* → *vyutthāyātha*; *śāstrārdha* → *śāstrārtha*; *prakṛṣṭhāṃ* → *prakṛṣṭāṃ*; *vyāprutasya* → *vyāpṛtasya*; *vidhyānartakya* → *vidhyānarthakya*; *stulyarthatvāt* → *stutyarthatvāt*; *nimitteṣṭānisṭha* → *nimitteṣṭāniṣṭa*; *pramāṇānulabdhe* → *pramāṇānupalabdhe*; *upadeṣṭrutvāyāsaḥ* → *upadeṣṭṛtvāyāsaḥ*; *śṛtvā* → *śrutvā*; *naiṣkarma + ya-vattu split across a line* → *naiṣkarmyasiddhiḥ*.

*Throughout (print conventions):* ḷ → l (7×); śraddhadhā- → śraddadhā- (11×); ūrthva → ūrdhva (5×); jñk / ṅñk → ṅk (2×).

**Kept as printed** (variants, not errors): 11.42 *yaccāpahāsārtham*
(Wikisource *avahāsārtham*); 18.25 *anapekṣya* (*anavekṣya*); 9.11 *tanum
āsthitam* (*āśritam*); 18.75 *śrutavān imaṃ guhyatamaṃ param* (*etad guhyam
aham param*); 13.20 *kāryaka(kā)raṇa-*, where the book prints both readings
and Śaṅkara comments on *kāryakaraṇa*; 16.4 *abhimānaḥ* (Wikisource
*atimānaḥ*); the book's unsandhied visarga in the verses (*śūrāḥ maheṣvāsā*,
*āpaḥ na*) and its padaccheda in the bhāṣya.

**Structure.** 1.20–21: the book sets *hṛṣīkeśaṃ tadā vākyam idam āha mahīpate*
as its own line after 1.20; it is placed at the head of 1.21 (standard
numbering), with *(arjuna uvāca)* inside the verse. The book puts *arjuna
uvāca* before 1.29 rather than inside 1.28; that is kept. A stray centred line
*puruṣastūkaṃ* (p. 365, inside the commentary on 13.2) and the book's heading
*śāstra upasaṃhāra prakaraṇam* (before the concluding survey at 18.66) are
dropped. The book's paragraph numbers are not shown; a lead-in paragraph
(*N.0*, or an unnumbered one before a verse) opens that verse's bhāṣya fold,
set a shade lighter. Chapter prefaces (*0.k*) and, in chapter 1, Śaṅkara's
upodghāta (with its opening verse *nārāyaṇaḥ paro'vyaktāt …*) have their own
fold at the top of the page. Śaṅkara does not comment on chapter 1 or on
2.1–10, so those verses have no fold. Both colophons of each chapter (the
Mahābhārata's and the bhāṣya's) are kept, with an original gloss.

**Normalisation (orthographic, not textual).** Anusvāra before a stop or
nasal inside a word written as the class nasal (site convention); word-final
*ṃ* kept. A word ending in *a* that the book runs straight into *i*/*u*
(*jātasyaiti* for *jātasya iti*) is spaced, since IAST would read it as a
diphthong. The book's quotation marks are set as “ ”, because the renderer
reads ' and ’ as avagraha. Daṇḍas the book swaps (2.33, 2.72, 4.2) or sets as
commas and full stops are normalised to | … ||. Hyphens: nine are the
book's avagraha or line-break joins and are resolved individually (*me'mṛtam*,
*mato'dhikaḥ*, *bhūyo'bhijāyate*, *ūrdhvamūlo'vākśākhaḥ*;
*hiṃsālakṣaṇa*, *avidyādhyāropitaḥ* …); the book's gloss marker *iti :-* is
written *iti :*; other dashes are en dashes. The speaker labels split across a
line in the print (9.1, 18.74) are completed.

**Later conversion fixes (2026-10-01).** The font's dagger glyph (†) is the
book's semicolon; it had first been read as the syllable *nu* (giving stray
forms like *adharmāyanu*), and 79 semicolons are restored. Compounds the print
breaks across a line with a dash (*iṣṭāniṣṭa– janma*) are rejoined from a
checked list; the remaining dashes are the book's own. Verse accuracy is
unchanged, and the round-trip check still passes for all but the three
standalone *oṃ* units.

**Word-by-word glosses (2026-10-01).** Every one of the 700 verses carries a
word-by-word list (8,901 pairs) at the top of its translation fold. The words
are the maintainer's own *padaccheda* of the verse, in verse order: sandhi
resolved, each word in its pausal form (*samavetāḥ*, *kim*, *ca*, *eva*),
compound members joined by reading-hyphens (*dharma-kṣetre*), which the page
keeps in Devanāgarī and Telugu (धर्म-क्षेत्रे). The meanings are original, written to agree
with the verse translation and, where a word is disputed, with Śaṅkara's
reading (7.22 *hi tān*, 13.20 *kārya-karaṇa*). Neither edition's Telugu
word-glosses were used. A script checks each verse's joined words against the
verse text (sandhi-insensitive similarity), so a dropped or mistyped word shows
up; all 700 pass, and every word converts cleanly to both scripts. The check
also caught one misprint in the mūla: 4.37 *kuruterju'na* → *kurute'rjuna*
(avagraha set after *rju* instead of before *r*).

**Word-by-word glosses for the other stotras (2026-10-02).** The remaining 33
generated pages and the hand-written Durgā Saptaślokī page carry the same
lists: 1,388 units, about 26,000 pairs. They are kept apart from the text, in
`tools/words/<slug>.txt`, one line per verse or prose unit
(`N  word = meaning | word = meaning`, `N` counting the units of the page from
1); `build_stotra.py` merges a file into its page when the data file has no
`words=` of its own. The Durgā Saptaślokī page is the shell the others are
built from, so its lists are written into the page and
`tools/words/durga-saptashloki.txt` is the record of them. The conventions
are those of the Gītā glosses, with these additions:

- Vedic texts (the sūktas, the Upaniṣad, the mantras of the Mahānyāsam and
  the vratakalpam) are glossed without svara marks.
- The pages in Telugu (the Annamayya and Rāmadāsu kīrtanas, the daṇḍakams,
  Gajendra Mokṣam) give the words in Telugu script, unhyphenated.
- Nāma lists and ritual formulae are glossed as units where a word-level
  split would say nothing (*oṃ keśavāya namaḥ* = "om, salutation to Keśava").
- A mantra the page quotes only by its opening and closing words is glossed
  for the words shown.
- The words follow the page's reading, also where it differs from the usual
  one: Kanakadhārā 9 *duṣkarma-dharmam* (usually *-gharmam*), Subrahmaṇya
  Bhujaṅgam 31 *namaś ca tubhyam* and 32 *pitā*, Lalitā 128 *vara-dā*, and
  the vratakalpam's *ā satyena* for *ā kṛṣṇena* and *kubjākṛṣṇāmbaradharāya*
  for *kubjākṛṣṭa-*. These are noted here for a later check against the
  sources; the text itself was not changed.

The meanings are original. `tools/words_check.py` reports coverage and
compares each unit's joined words with its text; all units pass except three
whose text is elided or in close Telugu sandhi (Gajendra Mokṣam 3, Mahānyāsam
259–260), which were read by hand.

**Bhāṣya translation.** Each Sanskrit paragraph in a fold is followed by its
English (`<p class="bh-tr">`, italic, set off by a rule on the left); the data
files carry it as `{"text": …, "tr": …}`. The English is editable through
*Suggest a correction* like every other gloss.

**Site changes.** The shell gained a bhāṣya fold (`.bhashya`: justified
Sanskrit prose, one `.sans` line per paragraph so it renders in all three
scripts); `build_stotra.py` gained a `bhashya=` list on verses, and section
types `speaker` (a Sanskrit speaker line), `bhashya` (a standalone fold) and
`colophon`, plus an optional `nav` of links between the parts of a
multi-page work. The pages live in a new folder, `stotra/gita/`, one page per
chapter (`gita-bhashya-01` … `-18`), listed under a new *Bhagavad Gītā*
heading in the index.

**Verification.** Every verse pada and bhāṣya paragraph was rendered back
through the page's own pipeline (`verify.py`'s port of teltools) and compared
with the Telugu source, after the normalisations above: 2,579 of 2,582 units
match; the other three differ only in the praṇava, which the renderer draws
as the ligature ॐ. `verify.py --data` passes all 1,401 verse padas of the 18
pages with zero failures.

**Preamble (chapter 1 page), added 2026-09-30.** The traditional preamble
to a recitation is set before Śaṅkara's introduction, taken from the two
books first and only then from elsewhere:

- *Viniyoga and nyāsa* (karanyāsa, hṛdayādi-nyāsa, dig-bandha, the closing
  viniyoga) — Pullela edition, *Śrībhagavadgītāpārāyaṇavidhiḥ*, pp. 50–51,
  transcribed from the page images (leaves 50–51 of the archive.org scan;
  the OCR text is too noisy to use). The Ramakrishna Math book has none of
  it. The edition reads *asya śrībhagavadgītā**śāstramahā**mantrasya*, kept;
  many prints have *…gītāmālāmantrasya*. Its misprints are read as:
  *sarapāpebhyo* → *sarvapāpebhyo* (18.66), *nānāvarṇākṛtāni* →
  *nānāvarṇākṛtīni* (as 11.5 and the karanyāsa), *bhūrbhuvarom* →
  *bhūrbhuvassuvarom*.
- *Gītā dhyāna* (4 ślokas) and *guru stuti* (the book's *gurudhyānam*, 5
  ślokas, from *vasudevasutaṃ devaṃ … kṛṣṇaṃ vande jagadgurum*) — the
  Ramakrishna Math book, p. xi, from the converted text layer; the only change
  is spacing *śrīguravenamaḥ* as *śrīgurave namaḥ*. The Pullela edition's
  fuller ten-verse dhyāna (adding *vācakaḥ praṇavo yasya*, *bhīṣmadroṇataṭā*,
  *pārāśaryavacaḥ*, *mūkaṃ karoti*, *yaṃ brahmā varuṇendra*) is not used.
- *Phalaśruti* — neither book has one. Mahābhārata 6.43.1–5 (*gītā sugītā
  kartavyā …*, spoken by Vaiśampāyana), from Sanskrit Wikisource,
  *महाभारतम्-06-भीष्मपर्व-043*, fetched 2026-09-30; *sukhapadmād* read
  *mukhapadmād*. Its verse 4–5 count of 745 ślokas is the Mahābhārata's
  own tradition, not this edition's 700.

The translations of all of it are original. Every line passes
`verify.py --data gita-bhashya-01`.

## 8. Learning Sanskrit

Teaching books in the public domain, set as Learn pages: the author's prose
in English, with every Sanskrit word in IAST so that it follows the page's
script switch (`tools/build_stotra.py`: section types `para`, `table`,
`vocab`, `en`, and `te` on a sentence).

### 8.1 A Sanskrit Primer (Perry) — `stotra/learn/perry-NN-iast.html`

| Field | Value |
|---|---|
| Work | Edward Delavan Perry, *A Sanskrit Primer, based on the Leitfaden für den Elementarcursus des Sanskrit of Professor Georg Bühler of Vienna*: an introduction to the structure of the language (§§ 1–91), 45 graded lessons with vocabularies and exercises, and glossaries. The whole book is done, one page each: the introduction (§§ 1–91), Lessons I–XLV, the two glossaries to the exercises, and the appendix with Perry’s corrections |
| Source | Ginn & Co., Boston, 1885; the scan used is of the 1892 issue, Cornell University Library copy, archive.org `cu31924011121690` (Introduction §§ 1–91 = leaves n20–n42 = pp. 1–23; leaf n38 = p. 19; Lesson I = leaves n43–n45 = pp. 24–26; Lesson II = leaves n45–n48 = pp. 26–29; Lesson III = leaves n49–n51 = pp. 30–32, with the footnote to Exercise III continued on p. 33; Lesson IV = leaves n51–n55 = pp. 32–36; Lesson V = leaves n55–n58 = pp. 36–39; Lesson VI = leaves n58–n61 = pp. 39–42; Lesson VII = leaves n61–n63 = pp. 42–44; Lesson VIII = leaves n63–n67 = pp. 44–48; Lesson IX = leaves n67–n70 = pp. 48–51; Lesson X = leaves n70–n73 = pp. 51–54; Lesson XI = leaves n73–n75 = pp. 54–56; Lesson XII = leaves n75–n78 = pp. 56–59; Lesson XIII = leaves n78–n81 = pp. 59–62; Lesson XIV = leaves n81–n84 = pp. 62–65; Lesson XV = leaves n84–n87 = pp. 65–68; Lesson XVI = leaves n87–n90 = pp. 68–71; Lesson XVII = leaves n90–n93 = pp. 71–74; Lesson XVIII = leaves n93–n97 = pp. 74–78; Lesson XIX = leaves n97–n101 = pp. 78–82; Lesson XX = leaves n101–n105 = pp. 82–86; Lesson XXI = leaves n105–n109 = pp. 86–90; Lesson XXII = leaves n109–n113 = pp. 90–94; Lesson XXIII = leaves n113–n116 = pp. 94–97; Lesson XXIV = leaves n116–n120 = pp. 97–101; Lesson XXV = leaves n121–n124 = pp. 102–105; Lesson XXVI = leaves n124–n128 = pp. 105–109; Lesson XXVII = leaves n128–n132 = pp. 109–113; Lesson XXVIII = leaves n132–n136 = pp. 113–117; Lesson XXIX = leaves n136–n140 = pp. 117–121; Lesson XXX = leaves n140–n145 = pp. 121–126; Lesson XXXI = leaves n145–n149 = pp. 126–130; Lesson XXXII = leaves n149–n152 = pp. 130–133; Lesson XXXIII = leaves n152–n160 = pp. 133–141; Lesson XXXIV = leaves n160–n166 = pp. 141–147; Lesson XXXV = leaves n166–n171 = pp. 147–152; Lesson XXXVI = leaves n171–n175 = pp. 152–156; Lesson XXXVII = leaves n175–n179 = pp. 156–160; Lesson XXXVIII = leaves n179–n183 = pp. 160–164; Lesson XXXIX = leaves n183–n186 = pp. 164–167; Lesson XL = leaves n187–n190 = pp. 168–171; Lesson XLI = leaves n190–n194 = pp. 171–175; Lesson XLII = leaves n194–n198 = pp. 175–179; Lesson XLIII = leaves n198–n205 = pp. 179–186; Lesson XLIV = leaves n205–n209 = pp. 186–190; Lesson XLV = leaves n209–n212 = pp. 190–193; Glossary I, Sanskrit–English = leaves n213–n235 = pp. 194–216; Glossary II, English–Sanskrit = leaves n236–n247 = pp. 217–228; Appendix = leaves n248–n249 = pp. 229–230; Corrections and Additions = leaves n250–n251 = pp. 231–232). Public domain: published 1885, and Perry died in 1938 |
| Recorded | 2026-11-11 |
| Text status | public domain |

**Method.** The text is read off the page images (the scan is clean; the
pencil notes of a former owner are ignored) into `tools/perry/lessonNN.txt`,
and `tools/perry/gen_perry.py` writes the page. Perry prints each Sanskrit
word twice, in Devanāgarī and in transliteration; here it is given once, in
IAST, and the page renders it in whichever script the reader picks.
`verify.py --data` round-trips every Sanskrit string on the page, those
inside the prose, tables and vocabularies included.

**Editorial notes.**

- Perry's transliteration is converted to IAST: his *ç* is *ś*; his accent
  marks (*vádati*) are not carried; where he writes *ṅ* before a sibilant
  (*çaṅs*) and his Devanāgarī has anusvāra (शंस्), the IAST is *ṃ* (*śaṃs*).
- Perry's italics (words not to be translated in the English exercises),
  bold rule headings and superscript word-order figures are kept.
- English in [square brackets] is the editor's (Lesson I: the Latin
  abbreviation under *yaj*, and *-que* under *ca*).
- The Telugu meanings in the vocabularies, the English and Telugu
  translations of the Sanskrit exercises, and the Sanskrit answers (with
  their Telugu) to the English exercises are the editor's, folded under
  each sentence so a learner can try it first.
- Hyphens inside a Sanskrit word (Perry's *ti-stha-ti*, *agni-su*) show in
  IAST and disappear in Devanāgarī and Telugu, where the render drops them.
- Perry's footnote marks ∗ and ∗∗ are printed as ∗ (U+2217) so that * can
  keep its use for italics. His accent marks on the nouns of the
  vocabularies (*putrá*) are not carried.
- His *āi* and *āu* are written *ai* and *au* (*devāu* → *devau*).
- Perry separates words in the transliteration but not in his Devanāgarī
  (§ 106), and marks a vowel combination in the Devanāgarī with a point; the
  page renders one IAST text in all three scripts, so the words are
  separated in all of them and the apostrophe shows as an avagraha
  (*gatā ’pi* → गता ऽपि).
- Exercise II, sentence 12 is printed *putra grāmaṃ gacchanti* (a singular
  stem with a plural verb). It is kept as printed and the editor's
  translation notes that *putrāḥ* is meant.
- Lesson III: Perry separates the accented *á*-class from the unaccented
  *a*-class by the accent alone; with accents not carried, the vocabulary
  headings are labelled “(accented)” and “(unaccented)” by the editor. In
  § 110 his dotted *ṅ* (the anusvāra) is written ⟨ṃ⟩, with a bracketed note.
  The footnote to Exercise III (sentence 4) is printed across the foot of
  pp. 32–33, beneath the first paragraphs of Lesson IV; it is given whole
  here, under the exercise it belongs to.
- Lesson IV: Perry prints the ablative singular of agni as “A.” (agnes) in the paradigm; it is the ablative, and is labelled Ab. here.
- Lesson IV: In Exercise IV, sentence 4 is printed with ∗ (Perry’s note: modifiers generally precede the word modified) after the word read here as areḥ, “of the enemy”; the vowel sign in the scan is e, as in girer of sentence 7. Sentence 12 reads ṛṣibhī (§ 123), as printed.
- Lesson IV: The footnote “See preceding note”, under the paradigm of vāri on p. 33, refers to the long note on n and ṇ that begins on p. 32 under Exercise III; it is given in Lesson III, and here as a pointer.
- Lesson V: Leaf n58 of the Cornell scan (p. 39) is cut off at the right edge; the end of Exercise V (sentences 29–31) was read from the Toronto copy of the same edition, archive.org sanskritprimerb00perr, leaf n54.
- Lesson V: In Vocabulary V Perry prints “+ ā (ārohati)” on a line of its own under ruh, for the compound; it is given here as a second entry for ruh. His “gam + ā” is likewise “gam | + ā”. His “Hindu” forms in § 126 (dhe, hve, gai) are given in IAST.
- Lesson V: In Exercise V, sentence 5 is read agnir udadhau tiṣṭhati (Fire stays in the ocean); the scan is clear. The footnote of sentence 2 (the Vedic hymns were “seen” by their authors) is given whole.
- Lesson V: The editor’s answers to the English sentences keep Perry’s set of words but not always his numbered order; he says the order of words in Sanskrit is very free. Sentence 19 is given with adhunā first, to avoid a vowel combination Perry has not yet taught.
- Lesson VI: Leaf n58 of the Cornell scan (p. 39) is cut off at the right edge; the whole of p. 39 (§§ 131–136, the paradigm of madhu, and the end of Exercise V, sentences 29–31, which is in Lesson V) was read from the Toronto copy of the same edition, archive.org sanskritprimerb00perr, leaf n54. Perry’s § 132 there reads “written with final o”.
- Lesson VI: § 139: the nasalized l that Perry writes ल्ँ (l with candrabindu) and says is “the same thing” as anusvāra is given as ṃl; the scripts here have no candrabindu on l, so it shows as anusvāra and l. In Exercise VI, sentence 5 (viṣeṇāsīṃ limpanti) Perry applies that rule himself; in sentence 7 he applies § 138 (gurūñ chiṣyāṃś ca).
- Lesson VI: Where two words have coalesced, the editor writes them as one (paraśunākrāmati, jalenāgniḥ, as in Perry’s Devanāgarī) in the exercise sentences, so that no avagraha appears.
- Lesson VII: Perry’s causative stems carry an accent on the aya (corayati, tāḍayati); the accents are not carried. His āi and āu (§ 144) are written ai and au.
- Lesson VII: In Exercise VII the final-t rules of §§ 148–151 are applied by Perry in sentences 1, 5, 7, 10, 11 (gṛhāc corayati, grāmāj janān nagaraṃ, nṛpāc chatrūṇāṃ, kopād daṇḍayati, gṛhāl lokā); the editor’s answers apply them in 21 (kopān nṛpaḥ).
- Lesson VIII: Perry’s āi and āu are written ai and au (§§ 159, 161, 164). The accents on the verbs are not carried.
- Lesson VIII: Exercise VIII, sentence 6: the conjunct before ca is blurred in the scan; it is read udyogaś ca (the dual verb rocete wants two subjects). Sentence 13 is read pāṇyos (gen.-loc. dual of pāṇi). Sentence 2 is asinā 'rayo, with Perry’s sign for the dropped a.
- Lesson VIII: In sentence 4 (śāstre) Perry’s reference to § 161 shows that śāstre is the dual, “the two sciences”; sentence 11 (paśūṃ) shows § 139 applied.
- Lesson IX: Perry’s āi and āu are written ai and au (§ 164). His Devanāgarī sentences are given with the sandhi he prints (nāvagacchanti, sahāgacchataḥ, bālāv ṛṣir).
- Lesson IX: In Exercise IX, sentence 9 refers to § 164 (kanyāyai + annam → kanyāyā annam); the reference is moved into the English note. Sentence 13 is read atra cchāyāyāṃ (§ 165). Sentence 1 carries Perry’s footnote (“Birds of a feather flock together”).
- Lesson X: § 171: Perry lists six roots (vac, vad, vap, vas, vah, svap) but prints only the passives ucyate, upyate, uṣyate and supyate; they are kept as printed (the passives of vad and vah, udyate and uhyate, are not printed in this lesson).
- Lesson X: In § 173 Perry’s “variable ṛ”, which the natives write with ṝ, is written ṛ, and the natives’ sign as ṝ.
- Lesson X: In Exercise X, sentence 11 is read stenair lokānāṃ vasu coryate (vasu is neuter singular); the last syllable is blurred in the scan. Sentence 6 is printed guruṇāhvayadhve (guruṇā āhvayadhve), with the dot under the ā that Perry uses to show a coalesced vowel; it is kept as printed. Sentence 12 shows § 123 (iṣubhī raṇe for iṣubhis raṇe).
- Lesson XI: The augment is accented in Perry’s transliteration (ávadam); accents are not carried. His āi and āu are written ai and au.
- Lesson XI: In Exercise XI, sentence 3 is read dāsyo ’nnam ānayan (the plural verb is the editor’s reading of the last, partly blurred, syllable); sentence 7 is read putryā ayacchad viṣṇuḥ. In the English exercise 14 Perry’s “besought” is a prapad verb: the editor’s answer uses the imperfect middle prāpadyadhvam, which Perry teaches in the next lesson (Lesson XII).
- Lesson XII: Perry’s “kḷp” (klṛp in the native grammarians) is written kḶp, with the capital standing for the vocalic ḷ (ऌ), as the page’s round-trip check does. His accent marks (kálpate, vindáti) are not carried.
- Lesson XII: Exercise XII opens with a verse Perry numbers ॥ 1 ॥ (makṣikā vraṇam icchanti …, “flies want a wound, princes wealth, the base a quarrel, the good peace”); his sentences are then numbered 1–14. It is given as a paragraph, with the editor’s English and Telugu.
- Lesson XII: In sentence 1 the scan reads śāntyarṣaya iha śobhante (śāntyā + ṛṣayaḥ); in sentence 7 hanvām aśvaṃ laghvā yaṣṭyātāḍayam (hanvām the locative of hanu; Perry writes anusvāra for m before l, as in § 94 of the Introduction); sentence 4 is dhṛtyāvindan nṛpatiḥ.
- Lesson XIII: Perry’s āi and āu are written ai and au; the augmented forms carry an accent (álabhe) that is not carried.
- Lesson XIII: The footnote at the foot of p. 61 (continued on p. 62) says that, the principal euphonic rules having now been taught, Perry no longer marks by figures the position of the words in the Sanskrit; the English sentences from no. 15 on carry none.
- Lesson XIII: Exercise XIII opens with a verse Perry numbers ॥ 2 ॥ (lobhāt krodhaḥ prabhavati …, “From greed anger arises …”); his sentences are then numbered 1–25. Sentence 10 is printed bhānumaitrarṣiḥ, with no verb, and is kept so; sentence 10’s translation is the editor’s best reading. Sentence 1 reads pratyaṣidhyata, sentence 7 adhyaṣṭhīyata, sentence 8 śriyāśobhata (śriyā aśobhata).
- Lesson XIII: In the editor’s answers, 16 leaves out Perry’s “ye” (the pronoun is not taught until a later lesson) and 18 uses buddhyā where Perry’s English says “its cleverness”.
- Lesson XIV: Perry’s āi and āu are written ai and au; accents on the verbs (vádāni) are not carried. In the vocabulary he marks the accent of juhū-stems and nouns (putrá); it is not carried either.
- Lesson XIV: Exercise XIV opens with a verse Perry numbers ॥ 3 ॥ (dharmaṃ carata mādharmam …); his sentences are then numbered 1–24. Sentences 6 and 11 are read kṣipateṣūn muñcata and juhvāgnau ghṛtaṃ prāsyāni. In Vocabulary XIV the last adverb is printed hrasvam, “near by”.
- Lesson XIV: In the editor’s answers 22 uses the imperfect passive aucyata (a + ucyata) for Perry’s “spoke (pass.)”.
- Lesson XV: Perry’s āi and āu are written ai and au; his ṝ (written with a long vowel mark) is ṝ. Accents on the verbs and on the nouns in the vocabulary are not carried.
- Lesson XV: Exercise XV opens with a verse Perry numbers ॥ 4 ॥ (durjanasya ca sarpasya …, “of a rogue and a snake the snake is the better …”); his sentences are then numbered 1–9, and the English ones 10–20. The verse carries Perry’s footnote ∗ (words are repeated to give a distributive sense: “at every step”) and sentence 4 his footnote ∗∗ (locative absolute). Sentence 6 is read muktāya (dat.) īśvaraḥ …; the first word is printed so.
- Lesson XV: Sentence 3 means “the sister’s house” (svasṛ, sister, § 203). In the editor’s answers, 19 leaves out the pronoun “thee” (not yet taught) and 20 uses a passive with svasāraḥ as its subject.
- Lesson XVI: Perry’s āi and āu are written ai and au; his root “çaṅs” is śaṃs. Accents on the verbs are not carried.
- Lesson XVI: Exercise XVI opens with a verse Perry numbers ॥ 5 ॥ (gaur gauḥ kāmaduhā …, with a play on words throughout, his footnote ∗: “Predicate”); his sentences are then numbered 1–12, and the English ones 13–22. Sentence 9 is read yadi śāstram abhyaseyaṃ tadā guravas tuṣyeyuḥ; sentence 12 is read he śiśavaḥ pitṝn sevadhvaṃ bhrātṝṇāṃ snihyata (the vowel signs in the scan are clear).
- Lesson XVI: In the editor’s answers, 14 translates Perry’s “opt. or imv.” with the optative, and 22 gives the daughters as accusative duals.
- Lesson XVII: In the paradigm of viśvapā (§ 213) Perry prints, in the dual of the accusative row, the form viśvapābhyām and, in the dual of the instrumental row, viśvapos (with the transliteration viśvap-os); both are misplaced (the first belongs to the instrumental and the second is the genitive-locative). They are kept as printed.
- Lesson XVII: § 212 reads “those in ā are rare that it is not possible …” in this scan (so rare, evidently); it is kept as printed. Perry’s āi and āu are written ai and au; accents on the verbs and on the nouns are not carried.
- Lesson XVII: Exercise XVII opens with a verse Perry numbers ॥ 6 ॥ (nābhinandeta maraṇaṃ …, “Let him not rejoice in death nor in life, let him await his time, as a servant his orders”), with his footnote ∗ (“Rule for an ascetic …”); his sentences are then numbered 1–11, and the English ones 12–22. Sentence 1 is printed bhrātāra stenāḥ śarān amuñcan, the first word without its visarga; sentence 2 pairs the singular naraḥ with the plural anutiṣṭheyus; both are kept as printed. Sentence 2’s last verb is read śasyeran (the passive of śaṃs, § 170).
- Lesson XVIII: Perry’s āi and āu are written ai and au; accents on the verbs are not carried. His abbreviations “1 dā”, “1 pā”, “2 pā” (the roots numbered by him) are kept as numerals before the root.
- Lesson XVIII: § 221 prints the second form of the causative construction in short (vihagaiḥ piṇḍān khādayati is written vihagaiḥ pi° khā°); it is given here as printed, with the abbreviation signs.
- Lesson XVIII: Exercise XVIII: sentences 1 and 2 are separate (“sūta adhunā sthāpaya ratham” and “yathājñāpayati devaḥ”); sentence 3 is read daśarathaś cārūn putrān ajanayat (cārūn, acc. pl. of cāru, “handsome”; the vowel sign is blurred). Sentence 13’s first words are grantho ’smābhī racyate (§ 123). Perry’s note ∗ (on the expression of possession by pronouns) is given with the English exercises. In English sentence 23 Perry’s hint is “use kāthayati” (a form of kath not given in the vocabulary), which the editor’s answer follows.
- Lesson XIX: Perry’s āi and āu are written ai and au; the pencil notes in the scan are ignored. In § 229 the nominative sas appears as printed (the pausal saḥ is in the example gacchati saḥ).
- Lesson XIX: § 234: the second Sanskrit example is printed sa parvato ’tīva tuṅgo yaṃ hyo ’paśyāma, without vayam; it is kept as printed. § 236: the first example is read yad yad eṣā kathayati.
- Lesson XIX: Exercise XIX opens with a verse Perry numbers ॥ 7 ॥ (sahāyena vinā naiva …, “Without a helper nothing is accomplished; the wheel does not turn on one foot”); his sentences are then numbered 1–14, and the English ones 15–25. Sentence 6 is read yuṣman mama duḥkhaṃ bhavati; sentence 8, tvadanyasmai kasmaicid dīyatām; sentence 12, pitṝñ śrāddhaiḥ (Perry’s ñś, see § 138). His footnotes ∗ (“Other than thou”; with anya the ablative is used) and ∗∗ (“Makes us read”) are given with the English sentences.
- Lesson XX: Perry’s āi and āu are written ai and au. His paradigm of marut, āpad, jagat prints the three stems side by side in each row, separated by daṇḍas; here each stem has its own column, and the three numbers are three tables. The ornamental daṇḍas are dropped. In the genitive singular the “„” marks stand for the form above, as in his print.
- Lesson XX: § 239.4 and § 244 name the letters of the final-consonant rules (t, d, dh, bh and the others) in Devanāgarī in the scan; they are given here in IAST. The verse of the exercise carries Perry’s footnote ∗∗ (see § 225; yatra = yasmin and yasyām, § 235 end), and the vocabulary a footnote ∗ on lambhayati.
- Lesson XX: Exercise XX opens with a verse Perry numbers ॥ 8 ॥ (te putrā ye pitur bhaktāḥ …, “Those are sons who are devoted to their father …”); the first half-line is preceded by a pencil mark, ignored. His sentences are then numbered 1–13, and the English ones 14–22. Sentence 3 is read āpadi suhṛdo ’smān pālayeyuḥ; sentence 4, viśvasyāṃ bhuvi pāpā bhūbhṛdbhir dṛśyantām (the passive of daṇḍ, “punish”, is not given; the editor reads daṇḍyantām, as Perry’s print shows a ṇḍ conjunct).
- Lesson XXI: Perry’s āi and āu are written ai and au; the pencil marks in the scan are ignored. In § 246 his list of roots (diś, dṛś, spṛś) and the remark “4. The s of su becomes ṣ after k” are kept; in the paradigm of vāc, ruj, diś the locative plural is read vākṣu, rukṣu, dikṣu (the kṣu conjunct is small in the scan). The plural of the second paradigm prints an extra daṇḍa between viś and lih; it is dropped with the other ornamental daṇḍas.
- Lesson XXI: His paradigms print three (or two) stems side by side in each row; here each stem has its own column, and the numbers are separate tables, as in Lesson XX.
- Lesson XXI: Exercise XXI opens with a verse Perry numbers ॥ 9 ॥ (daridrān bhara kaunteya …, “Support the poor, son of Kuntī; do not give wealth to the rich; medicine is for the sick, and the well man — what use are medicines to him?”), with his footnote ∗ (on kim with the instrumental and genitive). His sentences are then numbered 1–13, and the English ones 14–25. Sentence 2 is read dviḍbhir vyanāśyata (the ā is clear); sentence 5, bāṣpai rugbhyāṃ dṛgbhyāṃ pitā putram aikṣata paryaṣvajata ca (the kṣ in aikṣata is read from the shape of the ligature; the first word is printed so, and the meaning is “with tears … he looked at his son and embraced him”); sentence 10, sragbhir upānadbhyāṃ sametāḥ … (the ā-sign and dbh are clear enough to read the printed ‘upānajbhyāṃ’ as a misprint for it).
- Lesson XXII: Perry’s paradigms print the stems side by side in each row, separated by daṇḍas; each stem has its own column here, as in Lessons XX–XXI. In the paradigm of manas, havis, dhanus the printed forms are kept (haviṣ in the singular is printed havis; the dual is manasī, haviṣī, dhanuṣī). § 254’s neuter dual of sumanas is read -nasī.
- Lesson XXII: The footnote to § 251 (almost any noun in a may form a possessive derivative with the suffix in; thus from bala n., “strength”, balin, “having strength, strong”) is given in full. § 252 refers to “the loc. pl., p. 27, bottom of page”, a reference to Perry’s Introduction.
- Lesson XXII: Exercise XXII opens with a verse Perry numbers ॥ 10 ॥ (gandhena gāvaḥ paśyanti …, “By smell the cows see, by the Vedas the twice-born see; by spies kings see, by eyes other men”); his sentences are then numbered 1–10, and the English ones 11–22. Sentence 5 is read viśvasyā bhuvaḥ samrāṭ purūravā urvaśīm apsarasaṃ paryaṇayat tasyāṃ ca putro ’jāyata; sentence 8, puri vāri taḍāgān nālyā pārthivo ’nāyayat (nālyā, instr.); sentence 10, etasyā dhenvāḥ payo bālān pitarāv apāyayatām (Perry’s causative of pā).
- Lesson XXIII: Perry’s āi and āu are written ai and au; the pencil marks (Greek words) in the scan are ignored. § 258’s list of examples (nayanti, tiṣṭhanti, nahyanti, daṇḍayanti, bhaviṣyanti) is kept as printed; so is § 260’s (kirat, kariṣyat and yāt).
- Lesson XXIII: In § 259 the root is hu (Perry prints it with the root sign), 3rd plural juhvati; the footnote ∗ (the grammarians allow these verbs to insert the n in the nom.-voc.-acc. pl. neuter of the present participle) is given whole.
- Lesson XXIII: Exercise XXIII opens with a verse Perry numbers ॥ 11 ॥ (santo ’pi na hi rājante …, “Even though they exist, the other virtues do not shine in a poor man; fortune lights up the virtues of beings as the sun does”), with his footnotes ∗∗ (“Even though they exist”) and ∗∗∗ (anu in composition often conveys the idea of imitation); his sentences are then numbered 1–13, and the English ones 14–24. Sentence 9 is printed udyāne pataṅgo vihagebhyo dhānyaṃ kirantīḥ kanyā apaśyam; pataṅgo is not clear (a scribal slip for a word agreeing with kanyāḥ is likely), and is kept as printed; the translation covers the clear words. Sentence 8, kupyate mā kupyata, is taken as “he is angry — do not be angry”.
- Lesson XXIV: Perry’s āi and āu are written ai and au. His paradigms of rājan, nāman and ātman, brahman print the masculine and neuter columns together; they are given as in Lessons XX–XXIII. The footnote ∗ to the instrumental rājñā (§ 265: a dental meeting a lingual or palatal is usually assimilated; thus tiṣṭhati from ti-stha-ti, rājñā for rājnā) is given in full; the footnote to § 263 (iyant, kiyant are declined alike) and those to § 264 (bhavant, probably from bhagavant; bhos loses its s before vowels and sonant consonants, bho bho ṛṣe) likewise.
- Lesson XXIV: In the paradigm the nominative singular rājā is printed with a small mark under the ā; it is kept as rājā. Vocabulary XXIV: Perry marks brahman (n.) and brahman (m.) by their accent (bráhman and brahmán); the accents are not carried, and the two are told apart by gender as he gives it.
- Lesson XXIV: Exercise XXIV opens with a verse Perry numbers ॥ 12 ॥ (nodvejayej jagad vācā rūkṣayā priyavāg bhavet …, “One should not frighten the world with harsh speech; one should be sweet-spoken; for, as a rule, a kind-acting man is served even if he is poor”); his sentences are then numbered 1–12, and the English ones 13–24. Sentence 4 is read kiyato māsān bhavān kāśyāṃ nyavasat; sentence 9, grāme parivrāṇ tiṣṭhed vane paribhramanbrahma dhyāyet.
- Lesson XXV: Perry’s āi and āu are written ai and au; his dotted ṅ before a sibilant (as in jagmivāṅs) is written ṃ. The pencil marks are ignored. The two footnotes of the page — the footnote under the paradigm of jagmivāṃs (another form of the perfect participle of gam makes the strong and middle stems jaganvāṃs and jaganvat; the weakest form is jagmuṣ) and the footnotes to the table of añc compounds (∗ y inserted irregularly in weakest forms only; ∗∗ irregular, tiras + añc) — are given as printed. In the table of the stems of añc the table’s “Middle” column is blank for prāñc and avāñc, as in his print.
- Lesson XXV: In § 271 the nominative-accusative singular of ahan is printed with “(-s)”: ahar (-s).
- Lesson XXV: Exercise XXV opens with a verse Perry numbers ॥ 13 ॥ (vidvān praśasyate loke …, “The learned man is praised in the world; the learned man attains honour; by learning everything is obtained; by learning he is honoured by all”); his sentences are then numbered 1–11, and the English ones 12–23. Sentence 2 is read vidvadbhir eva viduṣāṃ śramo jñāyate; sentence 3, tvaṣṭā triśīrṣāṇaṃ putraṃ maghavāmārayat (the macron over ā is printed on mārayat, for maghavā + amārayat); sentence 6, kāśyā ājagmuṣo bhrātṝn apaśyām; sentence 10, kiyadbhir ahobhiḥ kāśyāḥ prayāgam agacchata; sentence 11 is printed pāṭaliputraṃ nāma mahānagaraṃ vidyate udīcāṃ takṣaśilā pratīcāṃ bhṛgukaccham.
- Lesson XXVI: Perry’s āi and āu are written ai and au; his dotted ṅ before a sibilant is written ṃ. The pencil marks are ignored. §§ 273–284 are paragraphs of irregular forms printed in running text; they are given as paragraphs, each form in ⟨ ⟩. In § 274 the dual is sakhāyau, sakhibhyām, sakhyos; in § 275 “curds” is dadhan and the weakest cases are akṣṇā, dadhnas, sakthni (or sakthani); in § 276 acc. strīm is printed with a long ī; § 277 gives divam, dyubhis and rāyas as printed; in § 278 the strong stem is anaḍvāh, mid. anaḍud, weakest anaḍuh, nom. anaḍvān, voc. anaḍvan; in § 282 pād and pad are the stems; § 283’s footnote ∗ (an altering cause in one member sometimes lingualizes an n of the next member; a guttural or labial in direct combination with n sometimes prevents it, as in the instr. brahmaghnā) is given whole.
- Lesson XXVI: Exercise XXVI opens with a verse Perry numbers ॥ 14 ॥ (patyau bhaktir vrataṃ strīṇām adroho mantriṇāṃ vratam …, “For wives devotion to the husband is the vow; for ministers faithfulness; for kings the protection of their subjects is the fixed vow”); his sentences are then numbered 1–17, and the English ones 18–27. Sentence 5 is read bāhubhyāṃ bhūbhṛt kṛtsnaṃ jagad ajayat; sentence 6, kena pathā bhavān sakhyā sahāgacchat; sentence 7, padā mām aspṛśat sakhā (the prefix of mām aspṛśat is clear); sentence 11 is printed strī patye rūpakān arpayati, with the long ī of the nominative; sentence 15 is read brahmaghnā na sambhāṣeta na ca tam adhyāpayed yājayed vā.
- Lesson XXVII: Perry’s āi and āu are written ai and au. The pencil marks are ignored. His footnote to § 291.4 (the commonest exceptions: khādita from khād “eat”, matta from mad, mudita from mud “rejoice”, rudita from rud “weep”, udita from vad “speak”, vidita from vid “know”) is given whole, as are the footnotes to Exercise XXVII (∗ “I am so-and-so; N. or M.”; ∗∗ translate the pronoun-forms by “here”, and cf. § 225). His roots 2kṛ and 1pṛ carry the numerals before them as in the vocabulary.
- Lesson XXVII: Exercise XXVII opens with a verse Perry numbers ॥ 15 ॥ (vardhamānam ṛṇaṃ rājan paribhūtāś ca śatravaḥ …, “Growing debt, O king, and enemies who have been slighted, and disease neglected: they breed great fear”); his sentences are then numbered 1–11, and the English ones 12–22. Sentence 2 is read bho asāv aham∗ ity uccārayan garīyaso 'bhivādayeta; sentence 3, ayaṃ naḥ pitā rathād avatīrṇaḥ sakhyā saha sambhāṣamāṇas tiṣṭhati; sentence 5, udadhau majjantaṃ bhujyum aśvinau nāvoddharatām (nāvā + uddharatām), printed with a dot under the long ā; sentence 8, yudhyamānān amūn anaḍuhaḥ paśya; sentence 10 is printed idam∗∗ āsanam imā āpaḥ snānāyāyam madhuparka idaṃ bhojanam imāni vastrāṇīyaṃ śayyeti gṛhastho 'tithiṃ gṛham āgacchantaṃ vadet.
- Lesson XXVIII: Perry’s āi and āu are written ai and au; his dotted ṅ before a sibilant is written ṃ (in § 295 smṛs/sraṃs, śaṃs). The pencil marks are ignored. §§ 294–301 list participles in running text; each form is set in ⟨ ⟩ as Perry gives it (with its root), and the lists are kept as printed: for instance § 295.4 gata, yata, nata, rata (from gam etc.) and khata, tata, mata, vata, hata (from khan, tan, man, van, han); and § 296.1 kānta, krānta, śānta, tānta, dānta, śrānta from kram etc.
- Lesson XXVIII: The footnote of the vocabulary (palāy is a quasi-root from i “go” + parā “away”) is given whole. Perry’s final-t rules in § 294.4 (the h cases) are given with their examples: gāḍha from gāh; līḍha from lih; rūḍha from ruh; mūḍha from muh; but dṛḍha from dṛh; soḍha from sah; dagdha from dah; digdha from dih; dugdha from duh; mugdha; naddha from nah.
- Lesson XXVIII: Exercise XXVIII opens with an eight-sentence group Perry numbers 1–9 and sets in one paragraph; the English ones are 10–15. Sentence 1 is śrīmato (abl.) rājñaḥ sammatair ebhiḥ kavibhir iṣṭāni vasūni labdhāni; sentence 4 is read mūḍhaḥ kharaḥ mṛgālasya snigdhābhir vāgbhiḥ pratāritaḥ siṃhasya guhāyām āgatas tena hataḥ; sentence 5, kṣetreṣu siktābhir meghānām adbhir dhānyaṃ prarūḍham; sentence 7, udīcā diśo yavaneṣv āgacchatsu pṛthvīrāja indraprasthāt sainyena saha niṣkrāntaḥ. In sentence 9 the last words are printed paścād asinā ghātitaḥ. Perry’s “(abl.)” after śrīmato and diśo is moved into the editor’s notes. The note “(In the following render all finite verbs by participles.)” is given.
- Lesson XXIX: Perry’s āi and āu are written ai and au. The pencil marks are ignored. The long lists of gerunds in §§ 305–313 are kept as printed (the forms, in ⟨ ⟩, and his “cf.” links); in § 308 the example ⟨adhikṛtya⟩ stands after ⟨adhītya⟩ (adhi-i). § 311’s footnote ∗ (the absolutives are often best rendered by relative clauses, or even by clauses coordinate with the principal clause) is given whole. In § 312 the Greek words are given as printed in Perry’s Greek type.
- Lesson XXIX: In §§ 309–310 Perry prints the compound gerunds with a circle for the prefix (°gatya, °hatya, °gamya, °tīrya, °pūrya); here the circle is written as a hyphen: -gatya, -hatya, and so on.
- Lesson XXIX: Exercise XXIX opens with a verse Perry numbers ॥ 16 ॥ (gate hi durdaśāṃ loke kṣudro ’py ahitam ācaret …, “When misfortune has come upon the world, even a small man may do harm; when the elephant is sunk in the mud, the frog is on its head”); his sentences are then numbered 1–10 in one run, and the English ones 11–20. Sentence 1 is read gurāv uṣitvā vedam adhītya strīṃ pariṇīya putraṃ janayitvā nityāni karmāṇy anuṣṭhāya yajñān iṣṭvā dānāni ca dattvā pretya brāhmaṇo na cyavate brahmaṇo lokāt; sentence 4 has hanumatā ’nyaiś ca kapibhiḥ (so the vowel signs in the scan; “with Hanumān and other monkeys”); sentence 7 runs from the foot of p. 120 into p. 121 (the line is broken after haviṣeṣṭvartvig-); sentence 8 is haviṣeṣṭvartvigbhyo … dattam.
- Lesson XXX: Perry’s āi and āu are written ai and au; his ∗ marks are the footnote signs of §§ 315 and 318 and are kept (∗ the increments of ṛ are sometimes r and rā instead of ar and ār, especially where a difficult combination of consonants is thus avoided; ∗∗ in all the tense-systems, and in derivation, the root mṛj often shows vṛddhi instead of guṇa). § 324’s footnote (the original value of the suffix ya is ia; hence e becomes ay, and o becomes av, before it) is given whole.
- Lesson XXX: In § 324 Perry’s dabhya, vandya, sadya, but mādya (from mad), vācya (from vac); and, under e., īḍya, guhya, tṛdya; vedya, yodhya, bodhya. His circle for a prefix is not used in this lesson.
- Lesson XXX: In § 315 the examples are kept as printed: śak, śaktum; man, mantum; āp, āptum; kṣip, kṣeptum; lup, loptum; śap “curse”, śaptum; 3vas “dwell”, vastum; and, with the changes of final consonants, pac, paktum; tyaj, tyaktum; dṛś, draṣṭum∗; spṛś, spraṣṭum∗; kṛṣ, kraṣṭum∗; prach, praṣṭum; yaj, yaṣṭum; sṛj, sraṣṭum∗; krudh, kroddhum; labh, labdhum; ruh, roḍhum; vah, voḍhum; dah, dagdhum; nah, naddhum; ad, attum; vid “know”, vettum (also veditum); gam, gantum.
- Lesson XXX: Exercise XXX is one run of eleven sentences (the last is ॥ 11 ॥, ending the paragraph), followed by Perry’s note (“Sentences with must may be rendered either with arh or with gerundives”) and the English sentences 12–22. Sentence 3 is read pāpāny apamārṣṭum apo ’vagāhyarcaḥ paṭhanīyāḥ sāmāni vā geyāni; sentence 8, sarvāsu dikṣu svairaṃ caritum yajñiyo ’śvo bhavadbhir moktavya iti rājñādiśyata; sentence 11, svayambhuvā jagat sraṣṭuṃ manaḥ kṛtam. The English exercise 18 refers to § 177 and 21 asks for bhavant.
- Lesson XXXI: Perry’s āi and āu are written ai and au. His circle for a part of a word (°) is written as a hyphen (dvāca- for dvāca°, and so on); the hyphen shows in IAST and not in Devanāgarī and Telugu. The footnote of § 334 (eka forms no ordinal) and that of Exercise XXXI sentence 1 (“i. e., in the seven stars of the Great Bear”) are given whole.
- Lesson XXXI: Exercise XXXI opens with a verse Perry numbers ॥ 17 ॥ (sakṛj jalpanti rājānaḥ …, “Kings speak once, the good speak once; maidens are given once: these three, for the good, once”), then his sentences numbered 1–10 (the first two lines are the verse and not numbered separately), followed by the English sentences 11–21. Sentence 3 is caturṇāṃ vedānāṃ tu bahavaḥ śākhā vartante; sentence 4 is tadyathā: ṛgvedasya pañca śākhā yajurvedasya ṣaḍaśītiḥ sāmavedasya saptātharvavedasya naveti (so the print, with the gender of śākhā left in the singular); sentence 6 sāmprataṃ catvāri sahasrāṇi nava śatāni tryaśītiś ca kaliyugasya varṣāṇy atikrāntāni; sentence 7 śrīvikramādityād anantaraṃ pañcapañcāśādhike śatatame saṃvatsare śakānāṃ rājābhiṣiktaḥ; sentence 9 trīṇi lakṣāṇi gavāṃ ṣoḍaśa grāmāś carṣabhadattena brāhmaṇebhyo dattāni; sentence 10 sa eva varṣe varṣe śatasahasraṃ brāhmaṇānām abhojayat (so the print: the genitive, not the accusative).
- Lesson XXXI: The numbers in the exercise are those of the Indian historical tradition (the Śaka era began 78 A.D.; the Kali Yuga 3102 B.C., so that 4983 years of it fell in 1882); they are given as printed and not checked.
- Lesson XXXII: Perry’s āi and āu are written ai and au; his root sign (√) before ciṣ and vṛ in § 339 (√kṣip, √vṛ “encompass”) is written “the root” in the notes of this edition. In § 342 his circle (°) is written as a hyphen (-tara, -tama). The footnote of the verse (Translate as though genitive) is given whole.
- Lesson XXXII: In § 339 Perry prints kṣepīyas and kṣepiṣṭha (root kṣip) as attached to kṣipra “quick”, and varīyas and variṣṭha (root vṛ) to uru “broad”; his Devanāgarī shows the lingual ṣ in the superlative, which the page keeps.
- Lesson XXXII: Exercise XXXII opens with a verse Perry numbers ॥ 18 ॥ (jyeṣṭho bhrātā pitā vāpi yaś ca vidyāṃ prayacchati | trayas te pitaro jñeyā dharme ca pathi vartinaḥ, “the eldest brother, the father, and he who gives learning: these three are to be known as fathers, abiding in the path of law”), then his sentences 1–11 and the English ones 12–21. Sentence 5 is read yadi jyeṣṭhāyāṃ bhāryāyāṃ kaniṣṭhaḥ putro jāyeta tadā sa eva śreṣṭhaṃ dhanasya bhāgaṃ labhetety eke; sentence 6, paramāṇor apy aṇīyān mahato 'pi mahīyān vedānteṣu varṇyate; sentence 8, yā aṣṭāviṃśatir dakṣasya duhitaraś candramasā pariṇītās tāsāṃ rohiṇī bhartuḥ preṣṭhābhavat; sentence 10, pāpānāṃ pāpiṣṭhās tu brahmahaṇaḥ.
- Lesson XXXIII: Perry’s āi and āu are written ai and au; his circle (°) for the part of a word that stands for the rest is written as a hyphen (-akṣa, -aha, -mūrdha, -rāja; -bhūma, -rātra, -sakha, -patha; -ahna). In § 353.1 the first form is blurred in the scan and is read -akṣa; the others are clear.
- Lesson XXXIII: Footnotes kept in full: § 347 (this class of compounds is of comparatively recent development; only the other two are common in others of the related tongues); § 354 (this class is called by the Hindus dvandva, “couple”; but a dvandva of adjectives they do not recognise); § 357 (the Hindus reckon these as karmadhārayas); § 358 (the whole class of determinatives is called by the natives tatpuruṣa, a specimen of the class meaning “his man”; the second division, the descriptives, bears the special name karmadhāraya, a word of obscure meaning and application); § 364 (literally, a tiger which is not a tiger after all, but a man; or, perhaps better, “tiger of (or among) men”, so Whitney); the footnote to Exercise XXXIII, sentence 2 (to engage in the sport of hunting; cf. below, § 375, 3).
- Lesson XXXIII: Exercise XXXIII is six Sanskrit sentences, one paragraph; Perry’s English sentences 7–12 are to be turned into Sanskrit with the compounds he shows by hyphens (“Form compounds of words joined by hyphens”). Sentence 1 is read duṣṣanto nāma rājarṣiḥ pūruvaṃśatilakas trilokyāṃ viśrutaḥ kṛtsnāṃ pṛthivīm apālayat ; sentence 3, tasmin vane duṣṣanto 'nekān vyāghrasiṃharkṣadvīpino 'nyāṃś ca vanacarān prāṇinaḥ svaśarair vyāpādayat; sentence 5, kaṇvasya brahmarṣer ayam āśrama iti sūtamukhāc chrutvā sainikān vane saṃsthāpyarṣiṃ nantuṃ rājā tatra praviṣṭaḥ. The name is Duṣṣanta (Perry prints “Dussanta”), the later spelling being Duṣyanta.
- Lesson XXXIII: The editor’s answers to the English sentences 7–12 follow Perry’s hyphenation and the numerals on his words (for example in 10 and 11).
- Lesson XXXIV: Perry’s āi and āu are written ai and au; his circle for a part of a word is written as a hyphen. In § 369 the vocabulary of examples is kept: bahunadīka “rich in rivers”, mṛtabhartṛkā f. “whose husband is dead, i. e. widow”, mahāyaśas (nom. masc. and fem. -yāḥ) or mahāyaśaska; in § 370, gardabhanādin (= -nāda) “having an ass’s voice”. In § 380 the feminine trilokī is explained as “by the side of -loka n.”.
- Lesson XXXIV: Footnotes kept in full: § 371 (this class of compounds is called by the natives bahuvrīhi; the name is an example of the class, meaning “having much rice”; the possessive may generally, in accented texts, be distinguished from the original determinative by a difference of accent); § 380 (the name dvigu is a sample of the class and means “of two cows”, said to be used in the sense of “worth two cows”); § 381 (the word avyayībhāva means “conversion to an indeclinable”); Exercise sentences 17 and 23 (∗ secondary adjective compounds, feminine in ī; ∗∗ dependent compound, “skilled in speech”).
- Lesson XXXIV: Exercise XXXIV opens with a verse Perry numbers ॥ 19 ॥ (atitṛṣṇā na kartavyā tṛṣṇāṃ naiva parityajet | atitṛṣṇābhibhūtasya cūḍā bhavati mastake, “One should not feel excessive thirst, nor yet give up desire altogether; for him who is overcome by excessive thirst, a top-knot grows on the head”), then the story of the boar-hunter in fifteen numbered sentences, and English sentences 16–26. In the story sentence 3 (tena prasarpatā, pres. part. instr.) is Perry’s own gloss and is kept in the Sanskrit; sentence 2 is sa caikadā mṛgayāṃ kartuṃ prasthitaḥ; sentences 4 and 5 are as printed; sentence 9 is bhoḥ sānukūlo me vidhiḥ; sentence 10 tenaitac cintitaṃ bhojanam upasthitam; sentence 11 tad ahaṃ tathā bhakṣayāmi yathā bahūny ahāni me prāṇayātrā bhavati.
- Lesson XXXIV: Sentence 7 reads yāvad varāhapulindau paśyati tāvat prahṛṣṭo 'cintayat (the copulative dual compound varāha-pulindau, “the boar and the hunter”).
- Lesson XXXIV: The English exercise (16–26) is given with Perry’s hyphens kept, as he marks the compounds to be made; answers follow his hyphenation. Sentence 17 has two of his footnote marks; sentence 21’s “(cpd in loc. or instr.)” is kept in the English.
- Lesson XXXV: Perry’s āi and āu are written ai and au; the accent marks that he prints under the transliteration of each paradigm (sunómi, sunvánti, …) are not carried, and neither are the accented augments. The paradigms of su and āp are given cell by cell as printed; Perry abbreviates some middle and plural forms in the table of āp with a circle (°) for the part that repeats the form above; they are written out in full here, since the repeated part is always the same stem.
- Lesson XXXV: § 385 (the ending āna) and the Devanāgarī-only ligature for ṇ in the strong stem (ṇu, ṇo) are given in the editor’s IAST as nu and no, since the cerebral ṇ is a rule of sandhi for the roots that have r, ṛ or ṣ before the class-sign, not a separate suffix.
- Lesson XXXV: § 391.1: Perry prints “2nd du. ind. act.” for śṛṇuvas or śṛṇvas; this is the first dual, and is given as printed. Footnote ∗ to the imperfect (the augment, without any exception in verbal conjugation, is the accented element in the verbal form of which it makes a part); ∗∗ to the imperative (the rare imv. in tāt, cf. § 196, would be formed thus: sunutāt); ∗∗∗ to § 383 (for a comprehensive view of the ways of forming the present-stems of verbs following this general conjugation, see Introduction, § 78).
- Lesson XXXV: Exercise XXXV opens with a verse Perry numbers ॥ 20 ॥ (ācārād vicyuto vipro na vedaphalam aśnute | ācāreṇa tu saṃyuktaḥ saṃpūrṇaphalabhāg bhavet, “A Brāhman who has fallen from right conduct does not reap the fruit of the Veda; but joined to right conduct he would share the full fruit”), then ten Sanskrit sentences (1–10) and the English ones 11–19. His footnotes ∗ (infinitive of tṛ) and ∗∗ (the instrumental is sometimes used to express the medium, or space or distance or road, traversed) are given with the sentences. Sentence 3 is read svapitarāv udyānād āhvātuṃ bālaṃ prahiṇu; sentence 4, he maghavan paṇibhir apahṛtā asmadgāḥ pratyāhartuṃ marutaḥ sahāyān ādāya guhāyā dvāram apavṛṇuyā ity ṛṣibhir indraḥ prārthyata; sentence 5, vanavṛkṣān dhunvānasya vāyoḥ śabdaṃ pathā gacchantāv aśṛṇva (the verb is the briefer first dual aśṛṇva); sentence 6, … vidyārūpādīn guṇān āpnavāma; sentence 8, … giriśikharam avāpnuvata; sentence 9, … pracinvīraṃs tapasvinaḥ.
- Lesson XXXVI: Perry’s āi and āu are written ai and au; the accent marks that he prints under the verb forms in the vocabulary (karóti, kurute) are not carried. The paradigm of kṛ is given cell by cell; in the imperfect and optative Perry prints the second and third persons as “etc.”, and they are not supplied here (only the first-person row of the optative, and the full imperfect, are his).
- Lesson XXXVI: The Devanāgarī ligature for the root kṛ is blurred in a few cells of the scan (kurvas, kurmas, kurve, kurvahe, kurmahe) but is plainly the stem kur- with the endings of the nu-class; they are read as the nu-class forms. § 395: Perry prints saṃskaroti, saṃskurute, samaskurvan, with the initial s that kṛ takes after sam; the footnote sign after sam in the scan has no note on its page, so none is given.
- Lesson XXXVI: Footnote to Exercise XXXVI verse 21 (the possessive compound sānvayaḥ, cf. § 374, 5) is given with the verse. Perry’s “(pl.)”, “(mid.)”, “(dat.)”, “(instr.)” in the English sentences are kept as printed.
- Lesson XXXVI: Exercise XXXVI opens with three verses numbered ॥ 21 ॥, ॥ 22 ॥ and ॥ 23 ॥ (the first, on the twice-born who neglects the Veda: yo ’nadhītya dvijo vedam anyatra kurute śramam | sa jīvann eva śūdratvam āśu gacchati sānvayaḥ; the second, on whatever deed one does: yat karoty aśubhaṃ karma śubhaṃ vā yadi sattama | avaśyaṃ tat samāpnoti puruṣo ’tra na saṃśayaḥ; the third, on the loved even in fault: kurvann api vyalīkāni yaḥ priyaḥ priya eva saḥ | anekadoṣaduṣṭo ’pi kāyaḥ kasya na vallabhaḥ), then seven numbered Sanskrit sentences and the English ones 8–17. Sentence 1 is read yo brāhmaṇaḥ karṇāv āvṛṇoti taṃ pitaraṃ mātaraṃ ca manvāno na druhyet tasmai kadācana (so the print, with tasmai); sentence 2, idaṃ te lobhāndhasya vṛttaṃ manasi camatkāram ātanoti; sentence 4, asmadvaṃśāṃsi dikṣu pratanuyur iti matvā bhūyasīṃ śriyaṃ bhūbhujaḥ kavibhyo vibhajanti; sentence 5, māṃsamūlaphalādi prabhūtavyañjanaiḥ sūdā mahānase saṃskuryuḥ; sentence 7, apsarastiraskariṇā vapus tiraskurvate ’vijñātāś ca manuṣyān upāgacchanti.
- Lesson XXXVII: Perry’s āi and āu are written ai and au; the accent marks that he prints under the vocabulary forms (aśnāti, krīṇāti …) are not carried. The paradigm of krī is given cell by cell with the cerebral ṇ his Devanāgarī shows after r (krīṇā-, krīṇī-); in the imperfect middle he prints a circle (°) for the part that repeats the form above (°ṇi, °ṇīvahi …); it is written out in full here. In § 400 he gives the weak stem as krīṇī and the form before a vowel as krīṇ.
- Lesson XXXVII: § 401: the examples of the 2nd singular imperative in āna are badhāna, aśāna, stabhāna, gṛhāṇa; the first and the third differ from the usual badhnīhi, stabhnīhi, as Perry says. § 402: pū makes punāti, punīte, and grah is weakened to gṛh (gṛhṇāti). § 405 footnote: the ending us in the 3rd pl. impf. is also allowed in a few roots in consonants: 1vid “know”, cakṣ, dviṣ, duh, mṛj. The paradigm of yā puts the indicative and imperfect side by side, and the imperative and optative side by side; they are given as four tables here.
- Lesson XXXVII: Footnotes to the vocabulary (añjali: the two hands hollowed and opened, and raised to the forehead; adyatana: with the suffix tana, sometimes tya, are made adjectives from adverbs, especially of time; thus pratna “ancient”, prātastana “early”, śvastana “of the morrow”) are given whole. In Vocabulary XXXVII Perry marks the numbering of homophones before the root: 2aś (eat), 2pā (protect), 2luṭh, 2vṛ (choose), 1vara (suitor) and 2vara (choice).
- Lesson XXXVII: Exercise XXXVII opens with two verses numbered ॥ 24 ॥ and ॥ 25 ॥ (parakāvyena kavayaḥ … “Poets by another’s verse, and the powerful by another’s wealth, nourish their own work — by stealing — at the present moment”; vivekinam anuprāpya … “Qualities, on reaching a shrewd man, rise to eminence; a jewel set in gold shines the more”), then eight numbered Sanskrit sentences and the English ones 9–21. His English sentence 14 is printed “34.”, a misprint for 14. Sentence 3 is read devānāṃ kopāgniṃ śāntiṃ netuṃ tān stutibhir nalarājo ’prīṇāt (nalarājaḥ, “King Nala”); sentence 4, … tair ukto rājā dhārmikatvam avṛṇīta; sentence 5, somaṃ dṛṣadbhyāṃ sutvādhvaryavas taṃ punantu; sentence 8, lubdham arthena gṛhṇīyāt kruddham añjalikarmaṇā, the first half of the well-known maxim “the greedy by wealth, the angry by folded hands”.
- Lesson XXXVIII: Perry’s āi and āu are written ai and au; the accent marks that he prints under the vocabulary forms (éti, bravīti …) are not carried. The paradigm of i “go” (with adhi-i, “read”) is given as four tables (indicative, imperfect, imperative; the optative and participle in paragraphs, as he prints them). The footnote to § 407 (a number of roots in this class accent the root-syllable throughout, in weak as well as in strong forms, except in the imperfect) and to § 412 (special irregularities in this verb are occasionally met with, such as brūmi, bravīhi; some of the verbs in u are allowed to be inflected like brū, but forms so made are rare) are given whole.
- Lesson XXXVIII: In the paradigm of brū the print marks the length of u with the Devanāgarī signs; the forms read are bruve, brūvahe, brūmahe / brūṣe, bruvāthe, brūdhve / brūte, bruvāte, bruvate in the middle, and bravīmi, brūvas, brūmas / bravīṣi, brūthas, brūtha / bravīti, brūtas, bruvanti in the active. The vowel sign of a few of the dual and plural forms is blurred in the scan; the readings follow his rules (§§ 410, 412), and the paragraphs that give the rest of the tenses (the imperfect, imperative, optative and participle of stu and brū) are given as printed.
- Lesson XXXVIII: Exercise XXXVIII opens with a verse numbered ॥ 26 ॥ (puṣpāṇīva vicinvantam anyatra gatamānasam | anavāpteṣu kāmeṣu mṛtyur abhyeti mānavam, “Death comes upon the man, as upon one gathering flowers, whose mind has gone elsewhere, while his desires are unfulfilled”), then ten numbered Sanskrit sentences and the English ones 11–20. Sentence 1 is read bho duṣkṛtakāriṇaḥ asmād vanād apeteti krodhād ṛṣir āśramahariṇavadhodyatān vyādhān abravīt (Perry prints a daṇḍa after the vocative, which is left out here because the table format uses that sign as a separator); sentence 2 refers to § 264 for bho; sentence 5, agnīṣomāv aṣṭābhir ṛgbhir ṛṣir astaud indrāvaruṇau ca tisṛbhiḥ; sentence 10, śrīmadbhī rājabhir āhūtāḥ paṇḍitāḥ sabhāṃ yanti dharmapraśnāṃś ca vibruvate (śrīmadbhī for śrīmadbhir by § 123).
- Lesson XXXIX: Perry’s āi and āu are written ai and au; the accent marks that he prints under the vocabulary forms (véd, dvéṣṭi …) are not carried. The paradigms of vid and han and the first lines of dviṣ are given cell by cell as printed; for dviṣ only the active indicative and imperfect, and the singular of the imperative, are printed (the rest “etc.”). In § 417 the forms of the perfect-as-present are given in a paragraph, as he prints them; in § 421 the forms of caṣ (cakṣ “see”, middle) are given in a paragraph.
- Lesson XXXIX: § 419 footnote ∗ on jahi: “anomalous dissimilation”. Perry prints the imperative 2nd sg. of han as jahi, a form that does not follow the rule; it is kept as printed. § 415 reads vacmi, vakṣi, vakti (“only these three forms used”): the second of them is blurred in the scan and is read vakṣi from the rule he has just stated.
- Lesson XXXIX: § 421 reads (as printed) acaṣṭhās for the 2nd singular imperfect of cakṣ; it is kept as printed, though acaṣṭhās would be expected. In § 420 the second singular of dviṣ is read dvekṣi.
- Lesson XXXIX: Footnote ∗ to sentence 28 (the verse numbered ॥ 28 ॥: “Refers to false witness before a court. An untruth where small beasts (sheep, etc.) are concerned involves the destruction of five ancestors; where cattle are concerned, of ten, etc.”) and ∗∗ to English sentence 14 (sakṛd ity anye, “once, according to others”) are given whole.
- Lesson XXXIX: Exercise XXXIX opens with two verses numbered ॥ 27 ॥ and ॥ 28 ॥ (karoti pāpaṃ yo jñānān nātmano vetti ca kṣayam | pradveṣṭi sādhuvṛttāṃś ca sa lokasyeti vācyatām, “He who sins knowingly and knows not his own ruin, and hates those whose conduct is good — let him be called ‘of the world’”: the last words are blurred in the scan, and the translation is cautious; paśūnām … “untruth about animals destroys five, about cows ten, about horses a hundred, about men a thousand”), then eleven numbered Sanskrit sentences and the English ones 12–20. Sentence 3 reads pradviṣatīṃ bhāryāṃ kiṃ māṃ dveṣīty abravīt patiḥ; sentence 9 bhavo divo bhava dṛṣṭe pṛthivyāḥ (Perry’s dative-looking form, “be Bhava of heaven, be seen of earth”, is kept as printed); sentence 11 refers to § 374, 6.
- Lesson XL: Perry’s āi and āu are written ai and au; the accent marks that he prints under the vocabulary forms (ániti, ásti …) are not carried. The paradigm of as “be” is given cell by cell; of ās, śās, lih, duh and rud only what he prints (the first persons and the odd forms) is given, in paragraphs. His footnotes are kept: § 424 (ādhve, and so āddhvam or ādhvam in the imperative and imperfect), § 425 (see § 414; aśāt is said to be used in the 2nd person also), § 428 (cf. §§ 244, 249; and when the final sonant aspirate of a root is followed by t or th of an ending, the whole group is made sonant, and the aspiration of the root-final is not lost but is transferred to the initial of the ending), and the footnote to the vocabulary (after ud, the initial s of sthā and stambh is dropped; thus utthātum for utsthātum).
- Lesson XL: § 424 reads āse, āsse, āste; the second form is written with the doubled s as printed. In § 427 the 2nd singular of the imperative middle of lih is read likṣva (h before s becoming k, as the rule says); the form is blurred in the scan. § 429: Perry’s “°dos, °dat or °dīt” in the imperfect of rud are written out as arodīs, arodat and arodīt, from his rule.
- Lesson XL: In § 428 the second singular of duh is dhokṣi and the middle second singular dhukṣe, the stem showing the old guttural (dhokṣi from dohṣi); both are read from the print.
- Lesson XL: Exercise XL opens with a verse numbered ॥ 29 ॥ (nindantu nītinipuṇā yadi vā stuvantu | lakṣmīḥ samāviśatu gacchatu vā yatheṣṭam | adyaiva vā maraṇam astu yugāntare vā | nyāyyāt pathaḥ pravicalanti padaṃ na dhīrāḥ, “Let the politic blame or praise; let Fortune enter or depart at will; let death come today or at the end of an age: the resolute do not stir a step from the right path”), then ten numbered Sanskrit sentences and the English ones 11–20. Sentence 2 reads mitradhrukṣu pāpeṣu na viśvasiti buddhimān; sentence 4, pramattair ṛtvigbhir bhūmau nihitāni havīṃṣi śvānāv avālīḍhām; sentence 6, … abravīt; sentence 8 astu yaśaḥ śrutavṛtte stāṃ śriyaḥ santu na tu bhaktiṃ vinā svarge prāpnuyāḥ (read as printed: the dual stām, “let there be learning and conduct”).
- Lesson XLI: Perry’s āi and āu are written ai and au; the accent marks that he prints under the vocabulary forms (dádāti, dádhāti, jáhāti, jihréti) are not carried. The paradigms of bhṛ and dhā are given cell by cell as printed; in the imperfect middle of bhṛ Perry prints a circle (°) for the part that repeats the form above (°bhṛmahi, °bhṛdhvam, °bhrata); they are written out in full (abibhṛmahi, abibhṛdhvam, abibhrata). Perry’s dā “give” is inflected the same way as dhā, with d for dh except where dh belongs to the ending (§ 436), so no table is given for it. His footnotes are kept: § 430 (only a small proportion of the roots of this class retain the accent on the root-syllable in the strong forms; in the great majority the accent is on the reduplication, both in the strong forms and in those weak forms whose endings begin with vowels), § 435 (in combination with t or th of an ending, the dh of dadh does not give ddh, but follows the general rule of aspirate and of surd and sonant combination; and the lost aspiration is thrown back upon the initial of the root), and the footnote to verse 31 (with the suffix maya, f. -mayī, are formed adjectives signifying “made or composed or consisting of”; in the second line, “bear the name” merely, i. e. are not in reality such).
- Lesson XLI: § 431: the reduplicated forms are dadhā (from dhā), cikhid (khid), jihrī (hrī), tasthā (sthā), bibhī (bhī) and bibhṛ (bhṛ); § 432: bibhī, strong bibhe, and bibhṛ, strong bibhar. § 439: for hu “pour, sacrifice” (Perry’s print of the root is hu), the 2nd imperative is juhudhi and the 3rd persons of the imperfect are ajuhot, ajuhutām, ajuhavus, as printed.
- Lesson XLI: Exercise XLI opens with two verses numbered ॥ 30 ॥ and ॥ 31 ॥ (yad dadāsi viśiṣṭebhyo yac cāśnāsi dine dine | tat te vittam ahaṃ manye śeṣaṃ kasyāpi rakṣasi, “What you give to the excellent and what you eat day by day — that I take to be your wealth; the rest you guard for someone else”; yaś ca kāṣṭhamayo hastī yaś ca carmamayo mṛgaḥ | yaś ca vipro ’nadhīyānas trayas te nāma bibhrati, “The wooden elephant, the leather deer, and the Brāhman who has not studied — these three only bear the name”), then ten numbered Sanskrit sentences and the English ones 11–20. Sentence 1 reads yaḥ sarvabhūtebhyo ’bhayaṃ dattvā pravrajati tasmād api bhūtāni na bibhyati sa ca tebhyo na bibheti; sentence 3, ye dve kālaṃ vidhattas te mahatī jyotiṣī stavīmi; sentence 4, naikaṃ putram anyasmai dadyād anyasmāt pratigṛhṇīyād vā; sentence 6, bhikṣāṃ bhavati dehīti kṣatriyo bhikṣāṃ caran brūyāt (the glossed “bhavati”, voc. sing. f., “madam”); sentence 9, śatrūn āyāto (part., acc. pl.) dṛṣṭvā kṣatriyāv iṣū dhanuṣoḥ samadhattām (so, with the glossed participle). The English sentence 20 refers to the scholars as “who-have-not-learned-their-lessons” (hyphenated by Perry).
- Lesson XLII: Perry’s āi and āu are written ai and au; the accent marks that he prints under the vocabulary forms (yunákti, runáddhi …) are not carried. The paradigms of yuj and rudh are given cell by cell as printed (the roman forms of the vocabulary — yunakti, yuṅkte, ruṇaddhi, runddhe, chinatti, bhinatti, piṇaṣṭi, bhanakti, hinasti — confirm the readings of the tables, which Perry prints in Devanāgarī only). For piṣ and hiṃs only the imperfect, the 2nd persons of the indicative and imperative are printed; for tṛh only the two forms of § 446.
- Lesson XLII: Perry’s footnote to the paradigm of yuj: instead of yuṅkthas, yuṅgdhve and the like it is allowed (and more usual) to write yuṅthas, yuṅdhve etc.; also rundhas, rundhve etc., instead of runddhas etc.; in each case omitting the consonant immediately following the nasal. Given whole, with the printed forms in the table.
- Lesson XLII: The footnote to verse 32 (the antecedent of this relative is the subject of avāpnoti) and to sentence 1 (translate as though dative) are given with the verse and the sentence.
- Lesson XLII: Exercise XLII opens with three verses numbered ॥ 32 ॥, ॥ 33 ॥ and ॥ 34 ॥ (yad dhyāyati yat kurute dhṛtiṃ badhnāti yatra ca | tad avāpnoty ayatnena yo hinasti na kiñcana, “What one meditates on, does, and fixes one’s mind on, that he gets without effort, who injures nothing whatever”; yasyāṃ yasyām avasthāyāṃ yat karoti śubhāśubham | tasyāṃ tasyām avasthāyāṃ tat phalaṃ samupāśnute, “In whatever state one does good or evil, in that same state one reaps its fruit”; dūta eva hi saṃdhatte bhinatty eva ca saṃhatān | dūtas tat kurute karma yena bhidyante vā na vā, “The envoy alone joins, and the envoy alone splits those united: the envoy does that deed by which they are divided or not”), then ten numbered Sanskrit sentences and the English ones 11–19. In sentence 5 the verb (read yuṅkta) and the last word (read ṛkṣu, a locative plural of ṛc) are unclear in the scan; they are given as read, and the translation follows the sense (“it is heard in the Ṛks that in the morning the two Aśvins yoke the horses to the chariot, to wake the creatures, with Uṣas, their sister”). In sentence 7 the print reads viśinaṣṭi manorujaṃ (so, manoruj, “mind’s anguish”).
- Lesson XLIII: Perry’s āi and āu are written ai and au; the accent marks printed over the endings in §452 and under some roots are not carried. Roots are given in IAST without the √ sign.
- Lesson XLIII: The perfect paradigms are given cell by cell as printed; the readings of the Devanāgarī were checked against the forms Perry spells out in roman letters (iyeṣ, uvoc, īṣ, ūc, ni-ny-i-va and the like).
- Lesson XLIII: §449.4: Perry’s forms for nī are read nine or ninai (1st), nine (2nd), ninai (3rd); the printing of the vowel signs is small, and the reading follows his own rule (guṇa or vṛddhi in the 1st, guṇa in the 2nd, vṛddhi in the 3rd).
- Lesson XLIII: §460, end: the “simpler root-forms” are read pī and hu, and the root hvā “makes its strong forms also from hu”, as in juhava or juhāva; the hu is printed with a small hook under the ha. Given as read.
- Lesson XLIII: §473: the last example is read īḍ, īḍāṃcakre (the printed letter is blurred; īḍ is the root ‘praise’). Given as read.
- Lesson XLIII: §456: the last form, from lū, is printed luluviva and is given so.
- Lesson XLIII: Perry’s footnotes — to §448.5 (the grammarians prescribe, doubtless falsely, the ān-reduplication for all verbs beginning with a or ṛ followed by more than one consonant), to §465 (several roots not of the form defined are said to undergo the same contraction, most of them optionally) and to §471 (mechanically, the weakest participle-stem is the same as the 3rd pl. active, with ṣ instead of s) — are given in the text where they fall.
- Lesson XLIV: Perry’s āi and āu are written ai and au; the accent marks are not carried. Roots are given in IAST without the √ sign. Forms Perry abbreviates with a small circle (°) in §§492 and 494 are written out in full (for example °viṣma = apāviṣma), since the page check does not take the circle.
- Lesson XLIV: §476: Perry’s “some roots with medial ṛ gunate with r instead of ar” is given as printed (the printed letter is the plain semivowel r). §478: the root printed śrī (śrayiṣyati) is given as printed.
- Lesson XLIV: §488: the roots sraṃs (asrasat) and śvā (aśvat) are read from small print; the other aorists of that list are as printed. §491: the 2nd pl. middle is read anaiḍḍhvam as printed (the double ḍ is Perry’s).
- Lesson XLIV: §492 and §494: the middle forms are given as printed, with the circles expanded; in §494 the 1st and 2nd forms of the active (adikṣam, adikṣas, adikṣat) are read from the circle forms “°kṣas, °kṣat”.
- Lesson XLIV: Perry’s footnotes — to §483 (the Hindus also prescribe a middle formation, which has, however, practically no existence) and to §486 (the precative is strictly a peculiar aorist optative, but is so rare that its formation need not be explained here) — are given in the text where they fall.
- Lesson XLV: Perry’s āi and āu are written ai and au; accent marks are not carried. Roots are given in IAST without the √ sign. The running head of p. 193 reads “Lesson LXV” in the print for “Lesson XLV”; the page’s printer’s signature “Perry, Sanskrit Primer. 13” is omitted.
- Lesson XLV: §500a: the reduplicating vowels are read ā (for a and ṛ), e (for i and ī), o (for u and ū); the examples are read vāvad, dādhṛ, nenī and joghuṣ. The last example is blurred in the scan and is given as read (joghuṣ). §500b: carcar and marmṛj; §500c: varīvṛt.
- Lesson XLV: §507: in the gerunds of the last paragraph Perry writes the prefix with a small circle (°sthāpya, °gamayya); these are given as sthāpya and gamayya, with the prefix left out as the circle leaves it.
- Lesson XLV: §507: the aorists of dhṛ are read adīdharam and abūbhuvam (of bhū), as printed. §506: the desiderative stem īpsa (āp) and the aorist aipsiṣat are read as printed.
- Introduction: Perry’s Devanāgarī letters and examples are given in IAST inside the Sanskrit marks, so that they follow the script switch. Where Perry shows the shape of a sign (the hooks of i and u, the virāma, the conjunct signs, the avagraha, the numerals, the stroke order) the sign itself cannot be drawn in this setting, and the syllable or group it makes is given instead. Perry’s ç is written ś, his ai and au (āi, āu in his print) are written ai and au, and the vowel he writes with a dot below is written ḷ.
- Introduction: §1: the alphabet is given as two tables, the vowels and the consonants, with Perry’s column heads (“surd”, “surd asp.”, “sonant”, “sonant asp.”, “nasal”) kept. §5: the two Devanāgarī writings of the sentence (syllable by syllable, and run together) are given as the syllables and as one run of letters.
- Introduction: §§9–14: the conjuncts are read off the printed signs and given as the syllables they make; the OCR text of the scan is badly damaged there, so each was read from the page image. §19: the numerals 1–9 and 0 and the examples 24, 485, 7620 are given in ordinary figures. §20: the stroke-order figures are not drawn.
- Introduction: §16: the avagraha is shown as the inverted comma (’). §78: the examples are read as printed (dviṣ ‘hate’, juhu from hu, dadā from dā, ruṇadh with rundh, sunu, tanu, krīṇā and krīṇī, bhava, tuda, divya, adya, rudhya); the accent marks of these stems are not carried. “See note, p. 32” is Perry’s reference to a note in Lesson XXXI.
- Glossary and appendix: Glossaries (pp. 194–228): Perry’s headwords and Sanskrit forms are given in IAST inside the Sanskrit marks, so that they follow the script switch; his accent marks are not carried, and the sign for a root (√) is replaced by the word “root” in the entry, with his numbers 1, 2 (and 3 for ⟨vara⟩) kept. Perry’s section numbers and cross-references are kept as printed. The glossaries are Perry’s own and carry no Telugu meanings; the English–Sanskrit one is set as a two-column table.
- Glossary and appendix: Glossaries: the entries are given as printed, including the slips Perry lists in his Corrections and Additions (the corrections are given on the Appendix page and are not applied to the glossary text). Where the printed entry is incomplete, as at ⟨vraj⟩ (“+ wander forth” for + ⟨pra⟩), it is left as printed. Entries that run over a column or page are joined into one entry (⟨kṛ⟩, ⟨gam⟩, ⟨ci⟩, ⟨pad⟩, ⟨sthā⟩, ⟨brahman⟩ and a few more), and the rules between the letters of the alphabet are not drawn.
- Glossary and appendix: Appendix (pp. 229–230): the accent marks of the modern ictus-accent examples are small and are given as read; a few (the secondary accents of §3 and the compounds of §4) may be misread. Corrections and Additions (pp. 231–232): Perry’s Devanāgarī is given in IAST; the correction to p. 53 (“insert” the daṇḍa and the figure 1 after ⟨śrūyate⟩) is given in words, the correction to p. 182 is read ⟨ninyivahe⟩, and the one to p. 126 reads ⟨aṣṭātriṃśat⟩ as printed. The correction to p. 192 (⟨aipsīt⟩ for ⟨aipsiṣat⟩) was not applied to Lesson XLV §506, which keeps the form as printed.

### 8.2 The Dhātupāṭha — `stotra/learn/dhatu-NN-iast.html`

| Field | Value |
|---|---|
| Work | The Dhātupāṭha that goes under Pāṇini’s name, in the form in which Niels Ludvig Westergaard edited it (*Radices linguae Sanscritae*, Bonn, 1841) and Otto Böhtlingk reprinted it, without Westergaard’s apparatus, as “Der Dhātupāṭha nach N. L. Westergaard” in *Pāṇini’s Grammatik* (Leipzig, 1887), pp. 62*–84* (class 1, roots 1–1059; class 2, 1–72; class 3, 1–25; class 4, 1–137; class 5, 1–34; class 6, 1–143; class 7, 1–25; class 8, 1–10; class 9, 1–61; class 10, 1–395) |
| Source | archive.org `grammatikhrsgb00paniuoft` (University of Toronto copy), leaves n566–n589 (pp. 61*–84*). Westergaard’s own edition (archive.org `radiceslinguaesa00westuoft`) was checked and not used, because its roots are interleaved with a Latin apparatus of variants. Public domain: Böhtlingk died in 1904 |
| Recorded | 2026-11-12 |
| Text status | public domain |

The pages give each root with its number, the root in IAST, its meaning in Sanskrit as the Dhātupāṭha states it, and the editor’s English and Telugu (original). Böhtlingk’s accent marks, the bracketed variant readings and his remarks on single roots are not carried; roots that share one meaning (printed once, after the last) are given as one entry. The alphabetical index of the roots that follows the list in the book (pp. 84*–93*) is not transcribed. The list is read from the page images: many roots are small and some lettering is blurred, so a few readings, above all of the rarer roots, may be wrong. The English and Telugu are the editor’s glosses of the Sanskrit meanings and are not Böhtlingk’s.

## 9. Subhāṣita

### 9.1 Bhartṛhari’s Nītiśatakam — `stotra/subhashita/subhashita-niti-iast.html`

| Field | Value |
|---|---|
| Work | Bhartṛhari, *Nītiśatakam* (the hundred verses on wise conduct), 110 numbered verses and two unnumbered opening verses |
| Source | Sanskrit Wikisource, page *नीतिशतकम्* (`sa.wikisource.org`), fetched 2026-11-12 as raw wikitext and converted to IAST with the project’s `dev2iast.py` |
| Recorded | 2026-11-12 |
| Text status | public domain (the verses); the Wikisource transcription is freely licensed |

Editorial notes (the text is Wikisource’s, kept as it stands except for the points below):
- The first two verses carry no number in the source: a benediction (*dikkālādyanavacchinna…*) and the poet’s well-known verse on his disappointed love (*yāṃ cintayāmi satatam…*). They are given without a badge.
- The source’s numbering jumps from 6 to 8, with no verse 7; the numbers are kept as printed and no verse is supplied.
- The avagraha (ऽ) is written as an inverted comma. Printing slips of the source were corrected: *gṛdyṇāti* to *gṛhṇāti* (49), *nāḍkitaḥ* to *nāṅkitaḥ* (54), *kṛcchgato* to *kṛcchragato* (30), *prīrtigurau* to *prītirgurau* (62). Interjection marks (“!”) and the connective *api ca -* at the head of verses 18, 41 and 95 are dropped.
- Verses are kept in the source’s word-joining: long runs of sandhi are not divided.
- The English and Telugu translations are original; the Telugu follows the English closely.

### 9.2 Bhartṛhari’s Śṛṅgāraśatakam — `stotra/subhashita/subhashita-shringara-iast.html`

| Field | Value |
|---|---|
| Work | Bhartṛhari, *Śṛṅgāraśatakam* (the second śataka): 102 numbered verses, with two asterisked additions (35*1, 47*1) |
| Source | Sanskrit Wikisource, page *शृङ्गारशतकम्* (author Bhartṛhari), fetched 2026-11-12 as raw wikitext and converted to IAST with `dev2iast.py` |
| Recorded | 2026-11-12 |
| Text status | public domain (the verses); the Wikisource transcription is freely licensed |

Editorial notes:
- Numbers are the source’s (2.1 … 2.102), shown without the leading “2.”; verses marked with an asterisk are set apart as additions in the source’s numbering.
- In the source ॐ stands for the syllable *om* (the source’s typing of *komala*, *romāvali* and the like); these are read *komalaṃ* and *romāvaliḥ*, *kaumudī* is read for the source’s *kॐudī*, and in 2.3 and 2.5 *kuñcita*, *vakṣoja* replace the source’s *kuṣcita*, *bakṣoja*. The avagraha is written as an inverted comma; interjection marks are dropped.
- The Sanskrit of the source is garbled in several verses (2.27–2.29, 2.33, 2.34, 2.37, 2.101 and a few others: broken sandhi, lost words). It is given as it stands, and the English and Telugu of those verses say that the text is corrupt and give the general sense only.
- The pāda divisions follow the source’s line breaks, which in a few verses (for example 2.8) do not match the metre.
- The English and Telugu translations are original.

### 9.3 Bhartṛhari’s Vairāgyaśatakam — `stotra/subhashita/subhashita-vairagya-iast.html`

| Field | Value |
|---|---|
| Work | Bhartṛhari, *Vairāgyaśatakam* (the third śataka): 100 numbered verses, with asterisked additions (8*1, 39*1, 61*1, 71*1, 99*1, 100*1–3) and three verses the source leaves without a number |
| Source | Sanskrit Wikisource, page *वैराग्यशतकम् (भर्तृहरिविरचितम्)*, fetched 2026-11-12 as raw wikitext and converted to IAST with `dev2iast.py` |
| Recorded | 2026-11-12 |
| Text status | public domain (the verses); the Wikisource transcription is freely licensed |

Editorial notes:
- Numbers are the source’s (3.1 … 3.100), shown without the leading “3.”; asterisked verses are set apart as additions. Three verses carry only “3.” in the source and are given without a badge, in the order they stand.
- In the source ॐ stands for the syllable *om*; it is read *vyoma* (100) and *komalaiḥ* (100*1). In 71*1 the source’s *niḥsॐaśarma* is read *niḥsomaśarma*, which is almost certainly not what the poet wrote (probably *niḥsīma*, “boundless”), but it is given as the source has it. *néṇām* in the source is read *nṛṇām* (31, 49). The avagraha is written as an inverted comma; interjection marks are dropped.
- The Sanskrit of the source is garbled in several verses (3.4, 3.8*1, 3.39*1, 3.59, 3.61*1, 3.62, 3.71*1, 3.81 and the three unnumbered verses). It is given as it stands; the English and Telugu of those verses say that the text is corrupt and give the general sense only.
- The English and Telugu translations are original.

### 9.4 Sumati Śatakamu — `stotra/subhashita/subhashita-sumati-iast.html`

| Field | Value |
|---|---|
| Work | *Sumati Śatakamu*, attributed to Baddena (Bhadrabhūpāla): 110 verses as the source numbers them |
| Source | Telugu Wikisource, pages *సుమతీ శతకము* and *సుమతీ శతకము - రెండవభాగం*, fetched 2026-11-12 as raw wikitext |
| Recorded | 2026-11-12 |
| Text status | public domain |

Editorial notes:
- A Telugu-source page (`src: "tel"`): the Telugu is kept as the source has it, with the IAST as a reading aid; the source’s “భావం” (meaning) notes are not used.
- The source numbers 110 verses; 109 and 110 are variant readings of verses 4 and 27 and are kept, marked as variants in the English. The stray “[85]”, “[105]” markers of the source are removed.
- The English translations are original. The Telugu is in archaic orthography with many obscure words, and several verses (for example 14, 33, 77, 95) are translated loosely; they should be read as a guide to the sense, not a literal rendering.

### 9.5 Vemana Śatakamu (a selection) — `stotra/subhashita/subhashita-vemana-iast.html`

| Field | Value |
|---|---|
| Work | A hundred verses of the Telugu poet Vemana, selected by the editor from the Wikisource collection (*వేమన పద్యాలు*, about 1,360 poems arranged by initial letter); there is no traditional “Vemana Śatakamu” of exactly this content |
| Source | Telugu Wikisource, *వేమన పద్యాలు* (the pages by initial letter), fetched 2026-11-12 as raw wikitext |
| Recorded | 2026-11-12 |
| Text status | public domain |

Editorial notes:
- The selection favours the best-known and most characteristic verses; it is the editor’s, and the order is that of the Wikisource text (alphabetical by first word).
- The Telugu is kept as the source has it; the collection contains many variant versions of the same poem, and the one printed there is used. One poem (the Wikisource entry for *కాదు కాదు గురులు*) runs into the next on the source page; only its own four lines are taken. Verse 37 of the page (*కర్మము జ్ఞానికి*) closes with “వేమా!” rather than the usual refrain.
- The English translations are original and, because the Telugu is archaic and often obscure (a number of verses, especially 53–55, 72, 77 and 84, are translated loosely), should be read as a guide to the sense.

## 10. Kālidāsa and works attributed to him

Sections 10.1–10.4 are taken from Sanskrit Wikisource transcriptions of public-domain printed texts, 10.5 from a scan; all are converted to IAST with `dev2iast.py` (`tools/kalidasa/`), and the English translations are original. Apart from the Meghadūta, none is certainly by Kālidāsa the poet and playwright; the attributions are the traditional ones.

### 10.1 Śyāmalā Daṇḍakam — `stotra/devi/syamala-dandakam-iast.html`
- Source: Sanskrit Wikisource, *श्यामलादण्डकम् (कालिदासविरचितम्)*, pages 15–18 of the 1929 Kāvyamālā, part 1 (Nirṇaya Sāgara, Mumbai), fetched 2026-11-13. Public domain.
- **The text is repaired.** The Wikisource transcription (proofreading level 3) has OCR slips, and in the fourth and fifth paragraphs it has gaps (“xx”) where the print itself is illegible. I restored it from the scan where legible and otherwise from the standard text of the daṇḍaka as I remember it, so the Sanskrit is not strictly the print’s. The main changes: *ख* for *स्व* (*tantrīsvare*, *svarṇa*, *svedabindu*), *ग्व* for *ग्ध* (*snigdha*), *बिब्यो* for *बिम्बो*, *रल* for *रत्न*, *भाखर* for *भास्वर*, *द्विव्य* for *दिव्य*, *विघ्नेश*, *शिञ्जिनीडम्बर*, *गृहीत*, the gap *शङ्खपद्मद्वयोपाश्रिते* (para 4), and the end of para 5 (*vaktrāntarād ullasadgadyapadyātmikā bhāratī niḥsaret*); and *nandana* where the print has *candana* (*kelīvanaṃ nandanam*, para 5). The readings that remain doubtful are *siddhasaṅgānite* (para 3), *saṃyogariṅkhannakhendūjjvale* (para 4) and *pañcabāṇena ratyā na saṃbhāvite* (para 4, where *na* may be *ca*). **Please check these against a good edition.**
- Layout: two opening verses, five long invocations (numbered 1–5 in the print) and a closing verse, as the print has them.

### 10.2 Ambāṣṭakam — `stotra/devi/ambashtakam-iast.html`
- Source: Sanskrit Wikisource, *अम्बाष्टकम्*, Kāvyamālā, part 2 (1932), pp. 160–163 (proofreading level 4). Public domain.
- The Kāvyamālā colophon ascribes it to Śaṅkarācārya, and the page says so; tradition also calls it Kālidāsa’s Aśvadhāṭī stotra (the name is that of the metre). Slips corrected: *kuca* for *kuja* (1), *bhaya* spacing, *yālībhiḥ* for *yālīmiḥ* (5), *svapada* for *khapada* (5). Verses 3 and 4 run across page breaks in the source and are joined.

### 10.3 Śṛṅgāratilakam — `stotra/kavya/shringaratilakam-iast.html`
- Source: Sanskrit Wikisource, *शृङ्गारतिलकम् (मूलमात्रम्)*, pp. 86–91 of the 1910 edition of the *Ṛtusaṃhāra* with Candrikā commentary (proofreading level 4). Public domain.
- Thirty-one verses, numbered here by order. The print’s text is in places corrupt (verses 2, 8, 20 and 31 especially), and the translations of those say so. I corrected evident printing slips: *pīḍāṃ* (31), *dantadaśanaṃ* and *tat* for *dantadanalaṃ* and *te* (29), *prāpnoti* (21), word division in several verses. A few verses are close in wording to verses of other collections.

### 10.4 Meghadūta — `stotra/kavya/meghaduta-purva-iast.html`, `meghaduta-uttara-iast.html`
- Source: Sanskrit Wikisource, *मेघदूतम् - पूर्वमेघः* and *मेघदूतम् - उत्तरमेघः*, fetched 2026-11-13. Public domain. Verse numbers are those of the Wikisource text (Pūrvamegha 1–66, Uttaramegha 1–55); the two extra verses it carries, numbered here 19a (Pūrvamegha) and 45a (Uttaramegha), are verses not found in every recension, and 45a is textually uncertain (its translation says so).
- I did not collate the text against a printed edition, so readings are Wikisource’s; a stray misprint at Pūrvamegha 23 (*parvete te* for *parvate te*) is left as transcribed. The translations are my own, made verse by verse from the Sanskrit, and are literal in aim; the commentarial readings of a few place-names and epithets (Nirvindhyā, Śārṅgin, śarabha) are the usual ones.

### 10.5 Ghaṭakarparam — `stotra/kavya/ghatakarpara-iast.html`
- Source: the 22 verses read by me from the scanned pages of the *Kāvyasaṅgraha*, vol. 1 (Calcutta, 1888), on archive.org (public domain); no Wikisource transcription was used. Where the print is faint or looks corrupt the reading is my best one, and the Sanskrit should be treated as provisional.
- The poem is ascribed to a poet Ghaṭakarpara, one of the traditional nine gems of Vikramāditya’s court; some manuscripts name Kālidāsa, which is unproven. It is a yamaka poem, so the translations (especially verses 4, 6 and 22) give the sense only and are looser than the rest of the site.

## 11. Stories: Pañcatantra and Jātakamālā

Both are selections of tales (not the whole works), taken from Sanskrit Wikisource transcriptions of public-domain texts, fetched 2026-11-13, converted to IAST with `dev2iast.py` (`tools/stories/`). The English translations are original, made paragraph by paragraph and verse by verse from the Sanskrit.

### 11.1 Pañcatantra — `stotra/katha/pancatantra-tales-iast.html`
- Source: Sanskrit Wikisource, *पञ्चतन्त्रम्*, the pages for the first book (Mitrabheda) — the tales are in the pages *०१* to *०२छ* and carry its tale-headings. The tales are, from the first book, the monkey and the wedge, the jackal and the drum, the crane and the crab, the crows and the black snake, the lion and the hare, and the blue jackal; from the fourth book (page *०५*), the monkey and the crocodile; and from the fifth (page *०६*), the brahmin’s wife and the mongoose and the lion-makers. Wikisource numbers its pages one ahead of the books (page ०२ is the first book, ०६ the fifth).
- **The text is a patchwork.** The transcription mixes sources: some pages are sandhi-split and hyphenated in the manner of one edition, others are continuous. I removed the editorial hyphens in compounds (and turned the hyphen after a speech-verb into a space) and left the rest as transcribed, so the Sanskrit is not uniform in its spelling or its sandhi. A stray replacement character in the lion-and-hare passage was deleted.
- **Cutting.** The tales are told inside the frame story, and the Wikisource pages interleave them with frame dialogue and long runs of maxims. I took each tale’s own paragraphs and its verses, and left out the frame and the maxims around it. In the lion-and-hare tale this leaves out the verses on kingly duty between the covenant and the hare’s turn; the verses on forts and on enemies are kept. The monkey-and-wedge tale breaks off at the point of the accident with a back-reference (“what befell him has been told already”), as the text has it; my translation adds “(that is, he was crushed to death)”. The jackal-and-drum tale refers to a verse it does not give.
- Each tale ends with “so I say…” and the first words of the maxim it illustrates; the maxim itself is in the frame, not here.
- Verse 1.236 (crane and crab) is corrupt in the text; its translation is tentative and says so. The verse of the blue jackal (1.283) is also given tentatively. Verse numbers (1.118 and so on) are those of the Wikisource text, which has some verses under two numberings.

### 11.2 Jātakamālā — `stotra/katha/jatakamala-tales-iast.html`
- Source: Sanskrit Wikisource, *जातकमाला (आर्यशूरः)*, a transcription of Āryaśūra’s Jātakamālā (the page markers in it follow P. L. Vaidya’s edition); the four tales are Śaśajātaka (no. 6), Matsyajātaka (no. 15), Vartakāpotakajātaka (no. 16; its title is printed *वर्तकापीतक* in the heading and *वर्तकापोतक* in the colophon, and the page uses the heading’s) and Mahiṣajātaka (no. 33). I did not collate against Vaidya’s print.
- Removed: the Wikisource page markers “(वैद्य N)”, the square brackets, the colophon line closing each tale, and the line-division of ज्म् verse tags. The verse numbers (6.1, 15.1 …) are the Wikisource ones.
- The Sanskrit is ornate and difficult, and I translated it closely rather than freely; a few compound adjectives (the otter, jackal and monkey’s virtues in 1.6; “dharma” meaning heat in 1.33) are my best reading. In 1.5 the sense of the phrase on the beasts’ former wickedness is not certain. The Mahiṣajātaka’s text has several misprints (for instance *kśamāśrayād* and *bhaviṣayti*) which I left as transcribed; verses 33.8, 33.9 and 33.16 are obscure, and their translations (marked in the page) are tentative.

## 12. Name-lists (108 and 16 names)

Texts are taken from Sanskrit Wikisource transcriptions of public-domain printed texts (`tools/nama/`); the English translations are original. This section so far has only Subrahmaṇya. The lists for the other deities asked for (Gaṇeśa, Veṅkaṭeśvara, Śiva, Vīrabhadra, Āñjaneya, Durgā, Lakṣmī, Sarasvatī, Pārvatī, Gāyatrī, Kṛṣṇa, Lalitā) are not on Sanskrit Wikisource in a form I could source, and sanskritdocuments.org and similar sites are excluded by the licensing rules above; they are waiting for a supplied source.

### 12.1 Subrahmaṇya — `stotra/subrahmanya/subrahmanya-ashtottara-shatanama-stotram-iast.html`, `subrahmanya-shodashanama-stotram-iast.html`
- Source: Sanskrit Wikisource, *सुब्रह्मण्याष्टोत्तरशतनामस्तोत्रम्* (pp. 96–97) and *सुब्रह्मण्यषोडशनामस्तोत्रम्* (pp. 136–137) of the *बृहत्स्तोत्ररत्नाकरः*, part 1 (1953), proofreading level 4; fetched 2026-11-13. Public domain.
- Both are verse *nāma-stotras*, not ‘namaḥ’-lists; I have not turned them into nāmāvalis. The 108-name text does not number its names, and I did not recount them against 108.
- Edits to the print’s text: verse numbers supplied where the print omits them or runs two verses under one number (the print numbers 1, 3, 4, 5 … and leaves verse 8 unnumbered; I number the verses 1–15 by pairs of lines, the last being a single line); *krauñcadāraṇaḥ* (visarga added, v. 4), *śarodbhūta āhūtaḥ* for *śarodbhūtaṃ āhūtaḥ* (v. 6), *vīraghno*, *śyāmagaḷo* and the following sandhi-joins for the print’s spaced forms (v. 14). In the sixteen-name text: *alaṅkṛtaṃ* for the print’s misprint *alaṅkataṃ*, *dhyāyedīpsitasiddhidaṃ* for the misprint *dhyāyedīptasisiddhidaṃ*, *śikhivāhanaḥ* for *śikhivahanaḥ*, and *senānīrguho* for the print’s *senānī guho* (v. 4). The two names *kāraṇotpattideha* and *kāraṇānītavigraha* are obscure and their translations tentative.

