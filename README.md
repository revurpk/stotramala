<!-- Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE) -->
# Stotramālā — स्तोत्रमाला

A garland of short devotional Sanskrit texts, each published as a
**single self-contained HTML file** — no scripts, no external fonts, no
network requests of any kind — designed to be read comfortably on a
phone.

Every stotra ships with the Sanskrit text in Roman transliteration and a
plain-English gloss written for the language enthusiast rather than the
specialist.

**Read it: <https://revurpk.github.io/stotramala/>**

## Contents

Stotras are grouped by deity under `stotra/<deity>/`. Each renders in
IAST, Devanāgarī, or Telugu (script bar at the top).

| Deity | Stotra | |
|---|---|---|
| Gaṇeśa | Gaṇeśa Pañcaratnam | [read](stotra/ganesha/ganesha-pancharatnam-iast.html) |
| Viṣṇu | Achyutāṣṭakam | [read](stotra/vishnu/achyutashtakam-iast.html) |
| Devī | Śrī Durgā Saptaślokī | [IAST](stotra/devi/durga-saptashloki-iast.html) · [source orthography](stotra/devi/durga-saptashloki-original.html) |
| Devī | Śrī Kanakadhārā Stotram | [read](stotra/devi/kanakadhara-stotram-iast.html) |
| Śiva | Śiva Mānasa Pūjā | [read](stotra/shiva/shiva-manasa-puja-iast.html) |
| Advaita | Nirvāṇa Ṣaṭkam | [read](stotra/advaita/nirvana-shatkam-iast.html) |

The Gaṇeśa, Viṣṇu, and Advaita stotras are works of Ādi Śaṅkara; see
[SOURCES.md](SOURCES.md) §5 for provenance. New stotras are generated
from a small data file by `tools/build_stotra.py`.

Open `index.html` for the browsable list, or open any file in
`stotra/` directly. The main edition renders the verses in **IAST,
Devanāgarī, or Telugu** — pick a script from the bar at the top; the
choice is remembered.

## Reading a stotra offline on an iPhone

Each stotra is one self-contained file — nothing is ever fetched, and
the script selector's transliterator is inlined into the page — so once
it is on the phone it works completely offline, script switching and
all. Pick whichever route suits you; all three end with a file in the
**Files** app that you tap to read.

**1. AirDrop (simplest, from a Mac).** AirDrop the `.html` to the
phone, choose **Save to Files**, then tap it in Files. It opens in a
full-screen viewer and renders exactly as designed.

**2. iCloud Drive / Dropbox (no Mac needed).** Drop the `.html` into a
synced folder from any computer, then open it in Files on the phone.
Tap the ⌄ **download** icon once so the file is stored on the device
rather than streamed — after that it works in Airplane Mode.

**3. Download from the site.** Open the stotra on
<https://revurpk.github.io/stotramala/> in Safari and use **Share →
Options → Web Archive → Save to Files**. A plain *Add to Reading List*
also works but keeps Safari's own formatting.

To fetch a copy from the command line before transferring:

```bash
curl -fL -o durga-saptashloki.html https://revurpk.github.io/stotramala/stotra/devi/durga-saptashloki-iast.html
```

### Home-screen icon

Open <https://revurpk.github.io/stotramala/> in Safari and choose
**Share → Add to Home Screen**: the page gets the mālā icon and
launches chrome-free. Safari offers this only for pages served over
`http(s)`, never for a file opened from Files — so the home-screen app
has to come from the site (or from `python -m http.server` on your
LAN), not from an AirDropped copy. Either way the page still works
offline afterwards, since nothing in it is ever fetched.

## Icon

The mark is a **mālā** — a bead garland with the larger *meru* bead at
the bottom, where it hangs when the mālā is held — for *stotramālā*,
"a garland of hymns." It is drawn from pure geometry (no glyph, no
font), so it stays crisp at every size and is deity-neutral as the
collection grows.

| Asset | Use |
|---|---|
| `icon.svg` | Master vector |
| `apple-touch-icon.png` (180×180) | iOS home screen |
| `icon-512.png` | Large / maskable |
| `favicon-32.png` | Raster fallback |

All four are generated from one geometry definition, so they cannot
drift apart.

## The two editions

Each stotra may appear in more than one romanization, because the
scheme used by the source is not always strict IAST:

- **`-iast`** — strict IAST throughout: `e`/`o` without macrons (both
  are inherently long in Sanskrit), `c` for च and `ch` for छ, `ḷ` for
  ळ, and daṇḍas romanized as `|` and `||`. The invocation ॐ is kept as
  the Devanagari emblem. This page also renders the verses in
  **Devanāgarī and Telugu** on demand, transliterated from the IAST at
  read time (see below).
- **`-original`** — the romanization as received from the source
  (`ē`/`ō`, `ch` for च), corrected only for demonstrable typographic
  damage. Retained so the source reading stays inspectable.

Every difference between the two is logged in [SOURCES.md](SOURCES.md).

## Design constraints

These are binding for anything added to this repo:

1. **Self-contained and offline-first.** All CSS inline; no external
   fonts, stylesheets, images, analytics, or network requests of any
   kind — a page must render identically with the network switched off.
   The favicon is inlined as an SVG `data:` URI so a page carries its
   own icon even when copied on its own.
2. **Scripting is optional enhancement, inlined not fetched.** Pages
   work fully with JavaScript off. Where script is used — currently the
   Devanāgarī/Telugu selector on the Durgā page — it is **inlined into
   the page**, never a sibling file, a CDN, or a remote import, and the
   page degrades gracefully to IAST without it. No build step, no
   framework.
3. **System fonts, with one embedded exception.** A serif stack (Iowan
   Old Style / Palatino / Georgia) present on iOS, macOS, and Windows,
   with the platform's own Devanagari face (Kohinoor / Nirmala UI / Noto
   named as fallbacks). Telugu is set in **Baloo Tammudu 2**, embedded
   as a subsetted woff2 because platform fallbacks mis-stack some Telugu
   conjuncts; it is OFL 1.1 (`fonts/BalooTammudu2-OFL.txt`) and embedded,
   never fetched. Nothing is loaded from the network.
4. **Legible on a phone first.** Single column, `viewport-fit=cover`
   with safe-area padding, and light/dark support via
   `prefers-color-scheme`.
5. **No silent emendation.** Any change to a received text — including
   transliteration normalization — is recorded in `SOURCES.md` with its
   justification.
6. **Provenance before publication.** Every external material is
   entered in `SOURCES.md` with origin URL, date, license, and what was
   changed, before it ships.

## Maintenance

**Regenerate the embedded Telugu font** (to pull a newer Baloo Tammudu 2,
or after adding scripts that need more glyphs):

```bash
python tools/regen-telugu-font.py
```

It re-fetches a Sanskrit-Telugu subset from Google Fonts and rewrites
the base64 `@font-face` in `stotra/devi/durga-saptashloki-iast.html` in
place (standard library only, no dependencies). Review the diff and the
rendered Telugu before committing.

## Licensing

Original work in this repository — the English translations, the
editorial apparatus, and the web presentation — is released under the
**Creative Commons Attribution 4.0 International** licence
([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)); see
`LICENSE` and `NOTICE`. You may share and adapt it, including
commercially, provided you give appropriate credit.

The Sanskrit verses themselves are ancient and in the public domain.
The electronic transcriptions they were keyed from may carry their own
claims; see [SOURCES.md](SOURCES.md), which also records where a
licensing question is **unresolved and therefore blocks commercial
redistribution**.
