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
