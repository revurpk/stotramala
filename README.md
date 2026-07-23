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

| Stotra | Editions |
|---|---|
| Śrī Durgā Saptaślokī — the Seven Verses of Durgā | [strict IAST](stotra/durga-saptashloki-iast.html) · [source orthography](stotra/durga-saptashloki-original.html) |

Open `index.html` for the browsable list, or open any file in
`stotra/` directly.

## Reading a stotra offline on an iPhone

Each stotra is one file with everything inlined, so once it is on the
phone it needs no network at all — ever. Pick whichever route suits
you; all three end with a file in the **Files** app that you tap to
read.

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
curl -fL -o durga-saptashloki.html https://revurpk.github.io/stotramala/stotra/durga-saptashloki-iast.html
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
  the Devanagari emblem.
- **`-original`** — the romanization as received from the source
  (`ē`/`ō`, `ch` for च), corrected only for demonstrable typographic
  damage. Retained so the source reading stays inspectable.

Every difference between the two is logged in [SOURCES.md](SOURCES.md).

## Design constraints

These are binding for anything added to this repo:

1. **One file per stotra.** All CSS inline; no JavaScript; no external
   fonts, stylesheets, images, or analytics. A file must render
   identically with the network switched off. The favicon is inlined as
   an SVG `data:` URI so a page carries its own icon even when the
   single file is copied or AirDropped on its own; the only sibling
   reference is `apple-touch-icon.png`, and a missing one costs nothing
   but the home-screen icon.
2. **System fonts only.** A serif stack (Iowan Old Style / Palatino /
   Georgia) that is present on iOS, macOS, and Windows. Devanagari, if
   used, falls back to the platform's own Devanagari face.
3. **Legible on a phone first.** Single column, `viewport-fit=cover`
   with safe-area padding, and light/dark support via
   `prefers-color-scheme`.
4. **No silent emendation.** Any change to a received text — including
   transliteration normalization — is recorded in `SOURCES.md` with its
   justification.
5. **Provenance before publication.** Every external material is
   entered in `SOURCES.md` with origin URL, date, license, and what was
   changed, before it ships.

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
