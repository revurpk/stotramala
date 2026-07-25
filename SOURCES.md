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

### 5.5 Durgā page moved into `stotra/devi/`

`durga-saptashloki-iast.html` and `-original.html` moved from
`stotra/` to `stotra/devi/` for deity-folder consistency. Their internal
relative paths were adjusted (`../` → `../../`), and a redirect stub was
left at each old top-level path so existing links do not break. The
generator (`tools/build_stotra.py`) reads the `-iast` page as its shared
shell, so its `SHELL` path was updated to the new location.
