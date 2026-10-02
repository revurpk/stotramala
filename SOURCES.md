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
