<!-- Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE) -->
# Stotramālā — स्तोत्रमाला

A garland of short devotional Sanskrit texts, each published as a
**single self-contained HTML file** — no scripts, no external fonts, no
network requests of any kind — designed to be read comfortably on a
phone.

Every stotra ships with the Sanskrit text in Roman transliteration and a
plain-English gloss written for the language enthusiast rather than the
specialist.

## Contents

| Stotra | Editions |
|---|---|
| Śrī Durgā Saptaślokī — the Seven Verses of Durgā | [strict IAST](stotra/durga-saptashloki-iast.html) · [source orthography](stotra/durga-saptashloki-original.html) |

Open `index.html` for the browsable list, or open any file in
`stotra/` directly.

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
   identically with the network switched off.
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
