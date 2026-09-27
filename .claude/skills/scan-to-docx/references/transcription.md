# Transcribing Indic print — encoding and look-alikes

Read the part you need.

- [1. Vedic accent marks](#1-vedic-accent-marks)
- [2. Unicode order inside an akṣara](#2-unicode-order-inside-an-akṣara)
- [3. Devanāgarī look-alikes](#3-devanāgarī-look-alikes)
- [4. Telugu look-alikes](#4-telugu-look-alikes)
- [5. Print conventions to keep, not "fix"](#5-print-conventions-to-keep-not-fix)

## 1. Vedic accent marks

Transcribe the marks the page prints; don't infer accents the page lacks.
Different traditions print different systems — identify it from the page
before encoding, and note it in the snippet's `accents:` line.

| Printed | Meaning (Ṛgveda / Taittirīya usage) | Code point |
|---|---|---|
| short vertical stroke above | svarita | U+0951 ॑ |
| horizontal bar below | anudātta | U+0952 ॒ |
| double vertical stroke above | dīrgha (double) svarita | U+1CDA ᳚ |
| three strokes above | triple svarita | U+1CDB ᳛ |
| ꣳ (Taittirīya anusvāra, "gṃ" sign) | anusvāra before ś ṣ s h r | U+A8F3 ꣳ |
| ꣴ | long anusvāra | U+A8F4 ꣴ |
| numerals 1 2 3 above (Sāmaveda) | svara numbers | U+A8E0–A8E9 (combining ꣠–꣩) |
| small ३ after a vowel | pluta (prolated vowel) | the digit ३ U+096B, in line |
| candrabindu ँ | anunāsika | U+0901 |

Udātta is normally **unmarked**. If a source prints an udātta mark (some
Kāṭhaka / Maitrāyaṇī editions do, as a vertical stroke above), the stroke
is U+0951 in the font but means udātta: say so in `accents:`.

Accents in **Telugu-script** Vedic books use the same combining marks
(U+0951, U+0952, U+1CDA) on Telugu letters; fonts vary in support, which is
why the HTML output exists.

## 2. Unicode order inside an akṣara

`consonant (+ nukta) (+ virāma + consonant …) + vowel sign + anusvāra /
candrabindu / visarga + accent mark`

The accent goes **last**, after any vowel sign and after anusvāra/visarga
(the lint flags the reverse). A mark that visually sits on a conjunct
belongs after the whole conjunct's vowel sign. An accent on an independent
vowel follows the vowel letter: `अ॒`, `ए॑`.

## 3. Devanāgarī look-alikes

At strip resolution these are the usual misreadings; check each doubtful
one on the full-page image or zoom in (`computer` zoom or a tighter crop).

- **घ / ध / थ / य** — the loop and the headstroke break; ध has no break, घ does.
- **भ / म / स** — भ has the extra loop on the left; म is closed on top.
- **ङ / ड / ड़** — ङ carries a dot to the right, ड़ a dot below.
- **व / ब / च** — ब has a diagonal inside; व is empty.
- **प / ष / फ** — ष has a stroke across the loop; फ a hook on the right.
- **द्व / द्ध / द्य**, **ह्म / ह्य / ह्व**, **क्त / क्र**, **त्त / त्र** — stacked conjuncts;
  read the lower member carefully.
- **ऽ (avagraha) / ऽ vs S** — use U+093D, never a Latin S.
- **। vs |** — use U+0964/0965, never a pipe or Latin l/I.
- **ः vs :** — visarga U+0903, never a colon.
- **०/ ॰** — zero vs abbreviation sign U+0970.

## 4. Telugu look-alikes

- **ష్ట / ష్ణ** — the commonest error in scanned Telugu; ష్ణ has the ణ foot.
- **త-vattu vs anudātta** (accented Telugu print) — the subscript త of స్త,
  న్తి, త్త is a short horizontal stroke under the line, easily read as an
  anudātta bar. A bar under a vattu is an accent only when the vattu's own
  syllable carries one (*nasta̱nuvā*: the bar is ta̱'s) or a second, separate
  bar is visible; otherwise it is just the letter (*nama̱s takṣa̍bhyo*).
  The standard accentuation of the passage is the tie-breaker.
- **Svarita strokes are tall**: in some prints they reach halfway to the line
  above. Use `prepare_pages.py --lines 1` so each crop holds one line with all
  its marks.
- **బ / భ**, **ద / ధ**, **గ / ఘ**, **ప / ఫ**, **చ / ఛ** — the aspirate carries an
  extra stroke inside or below; look at the full-size image.
- **ర / ఱ**, **ల / ళ** — keep what is printed (ళ for l is a Telugu-print
  convention in Sanskrit words; keep it, it is not an error to fix here).
- **ఎ ఒ ె ొ vs ఏ ఓ ే ో** — short vs long e/o. Sanskrit has only long e/o,
  but Telugu books often print the short signs; transcribe what is printed.
- **ఁ (arasunna)** vs **ం (anusvāra)** — different characters.
- **ఀ ౘ ౙ** — rare letters; don't normalise them away.
- **్ (virāma) marks**: a final halant is often tiny in print; check word-final
  consonants (…త్, …న్).

## 5. Print conventions to keep, not "fix"

The job is a faithful copy of the page; standardising is a later, logged
step (for stotramālā pages it happens in add-stotra). So keep:

- the book's word division, even when it splits words (Telugu print splits
  at geminates: *ముహూర్త స్సుముహూర్తోస్తు*);
- anusvāra where the book uses it for a nasal (*గంధ* for *గన్ధ*);
- the book's daṇḍas, verse numbers and labels (*శ్లో॥ మం॥ తా॥*);
- footnote markers — as plain `(1)`, not superscript characters (⁽¹⁾), which
  Indic fonts lack;
- the book's typos — a clearly printed but wrong akṣara stays as printed;
  record the likely intended reading in the snippet's `note:` line.

`[?X?]` is for something else: a **reading you can't be sure of** (broken
type, show-through, a smudged mark), with X your best guess. `[...]` is for a
stretch you can't read at all. Both come out highlighted in the outputs.
