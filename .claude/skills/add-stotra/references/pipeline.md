# Pipeline details

Read the section you need; skip the rest.

- [1. Fetching from Wikisource](#1-fetching-from-wikisource)
- [2. Extracting accented Ṛgveda saṃhitā](#2-extracting-accented-ṛgveda-saṃhitā)
- [3. How svaras render (the shell side)](#3-how-svaras-render-the-shell-side)
- [4. Round-trip verification](#4-round-trip-verification)
- [5. Commentary-interleaved sources](#5-commentary-interleaved-sources)
- [6. Telugu-source pages](#6-telugu-source-pages)
- [7. Praṇava ॐ](#7-praṇava-ॐ)

## 1. Fetching from Wikisource

Use PowerShell — it handles Unicode titles without manual percent-encoding, and
writes UTF-8 cleanly:

```powershell
$u = "https://sa.wikisource.org/w/index.php?title=$([uri]::EscapeDataString('ऋग्वेदः सूक्तं १०.९०'))&action=raw"
$r = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 25
[System.IO.File]::WriteAllText("scratch\rv.txt", $r.Content, [System.Text.Encoding]::UTF8)
```

To hunt for the right title, the search API is handy:
`.../w/api.php?action=query&list=search&srsearch=<term>&format=json`.

## 2. Extracting accented Ṛgveda saṃhitā

The accented saṃhitā lives in the svara-bearing lines (`॒`/`॑`). Two layouts:

- **Contiguous** (e.g. RV 10.90): the svara-lines are just the saṃhitā, two per
  ṛc (an `a`-line ending `।`, a `b`-line ending `॥`). Take them in order; the
  first `2·N` lines are your `N` ṛcs.
- **Padapāṭha-interleaved** (e.g. RV 1.1): each saṃhitā pair is followed by its
  padapāṭha (also accented). Keep only the pairs where `(index // 2)` is even.

`scripts/dev2iast.py --samhita rv.txt` prints the svara-lines indexed so you can
see which layout you have before pairing. Then convert each line with the
converter, strip the trailing `।`/`॥`/`॥N॥`, and append the daṇḍa markers:
`a`-line + `" |"`, `b`-line into the verse, number into `num`.

Encoding (must match the shell): `_` = anudātta after the vowel, `^` = svarita,
udātta unmarked. Anunāsika `ँ` → `ṁ`. A **pluta** numeral inside a word (e.g.
`वो॒३॒॑` in RV 10.84.5) is kept as ASCII `3` between its marks — the converter
does this; don't strip it.

## 3. How svaras render (the shell side)

For understanding/verification only — this code already lives in the shell
(`stotra/devi/durga-saptashloki-iast.html`, the canonical shell). At render
time, for Devanāgarī:

```js
function devSvara(iast){
  var out="", re=/[_^]/g, last=0, m;
  while((m=re.exec(iast))){ out += toDev(iast.slice(last,m.index)) + SVARA[m[0]]; last=m.index+1; }
  out += toDev(iast.slice(last));
  return out.replace(/([॒॑])([ःं])/g, "$2$1");   // tone mark AFTER visarga/anusvāra
}
```

A mark always follows a vowel (a syllable boundary), so it reattaches to the
akṣara that ends each chunk. The final `.replace` normalises the handful of
sources that store the mark *before* a visarga/anusvāra into the canonical order
— without it you get dotted-circle artifacts. IAST and Telugu call `stripSvara`
and show the text unaccented. Because `_`/`^` never occur in ordinary IAST, all
non-accented pages are unaffected.

## 4. Round-trip verification

**Default: `scripts/verify.py` (pure Python, no browser, no Node).** It is a
faithful port of the live render pipeline (`iast2tel → tel2hin → post`, plus
`devSvara` for accents), so it runs anywhere and doesn't depend on a browser or
dev server — both of which the sandbox can block (a localhost host gets refused;
file-loading a page may render only a static snapshot).

```bash
python <skill>/scripts/verify.py --render < iast_lines.txt          # print Devanāgarī
python <skill>/scripts/verify.py --check iast_lines.txt source.txt   # byte-exact PASS/FAIL, line-aligned
```

- **Non-accented:** the render must reproduce the source Devanāgarī.
- **Accented:** it must reproduce the source accented line **byte-exact**.
  Expected, benign diffs: (a) canonical-order normalisation moves a tone mark to
  *after* a visarga/anusvāra; (b) anunāsika `ँ` renders as anusvāra `ं` (the
  `ṁ`→anusvāra collapse). Anything else is a real bug.

Prepare the two files by taking the source's accented saṃhitā lines (or the
plain source lines) and your data file's padas in the same order. Also confirm
the built `*-iast.html` has the right `|| N ||` badge and ornament counts.

Keep the port in sync: its tables are transcribed from the teltools block
inlined in every built page; teltools is stable, but if it changes, re-transcribe
`iast2tel`'s tables (`tel2hin` is a pure code-point shift, `-0x300`).

**Optional visual check.** Looking at the actual built page in a browser is a
nice extra, not the verification. If you do it, load the *built page itself*
(copy it somewhere the preview will run its JS) — do **not** stand up a separate
localhost teltools host; that is what the sandbox refuses. Toggle to Devanāgarī
and confirm the accents show with no leftover `_`/`^`.

## 5. Commentary-interleaved sources

Some Wikisource Upaniṣads (Taittirīya especially) give the mūla interleaved with
Śaṅkara's bhāṣya — each anuvāka's text, then paragraphs of commentary closing
`iti …ānuvākabhāṣyam`, plus interpolated maṅgala ślokas. Extracting the mūla is
delicate: keep only the scripture, drop every commentary paragraph and
interpolation, and reconcile OCR against the standard reading (logging fixes).
If the interleaving is heavy, it is often better to find a mūla-only source than
to carve it out — flag this to the user.

## 6. Telugu-source pages

For `src:"tel"`, the Telugu is the truth and teltools makes the IAST aid; no
Devanāgarī is offered. teltools is a Sanskrit transliterator, so it renders the
Telugu short e/o (ె/ొ) as Devanāgarī signs and inserts a spurious `a` — the
render shell already repairs this for `src:"tel"`. Supply clean Telugu from
Telugu Wikisource; strip its ప|| / చ|| markers and any romanised duplicate.

## 7. Praṇava ॐ

In-verse `oṃ` renders as the praṇava ligature `ॐ` in Devanāgarī (the shell's
`post()` maps a standalone `ओं` → `ॐ`). So just write `oṃ` in the IAST; the
header's big `ॐ` is separate (hard-coded in the shell).
