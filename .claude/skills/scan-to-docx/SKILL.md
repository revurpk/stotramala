---
name: scan-to-docx
description: >-
  Transcribe scanned pages of Indic-script text — PDF scans, JPEG/PNG photos,
  multi-page TIFFs of Sanskrit, Telugu, Devanāgarī (also Kannada, Tamil,
  Malayalam, Gujarati, Bengali), including Vedic texts with svara accent
  marks — into a Word document, plus an HTML reading copy that renders the
  Vedic accents correctly. Built for compiling snippets from several books
  or scans into one document, each with its source and page recorded. Use
  this whenever the user wants to OCR, type up, transcribe, digitise or
  extract text from a scanned or photographed page, booklet or PDF in an
  Indian script, or to collect passages from different sources into one
  Word file — even if they don't say "OCR" or "docx" (e.g. "get the text
  out of this Telugu PDF", "put pages 3–5 of mahanyasam.pdf into my
  compilation", "type up this photo of a stotra with the svaras").
---

# Scanned Indic text → Word (+ accented HTML)

No OCR engine is installed here (no Tesseract, no Poppler), and generic OCR
is poor at Indic conjuncts and useless for Vedic accents anyway. You read
the page images yourself, line by line, and write Unicode. The scripts do the
mechanical parts: rendering pages at a legible size, and building the outputs.

All scripts run with `uv run` and install their own dependencies (inline
script metadata), so no project setup is needed. Paths below are relative to
this skill's folder.

## The compilation file is the source of truth

Everything goes into one UTF-8 text file (e.g. `rudra-readings.compile.txt`);
the `.docx` and `.html` are regenerated from it. Adding a snippet from
another book later = append to the file, rebuild. Format (full spec in
`scripts/compile_lib.py`):

```
# title: Śrī Rudra — collected readings
# compiler: <user's name>

=== snippet
source: Mahānyāsam, Vavilla Ramaswamy Sastrulu & Sons, Madras 1937
file: C:\Users\...\mahanyasam.pdf
pages: 3-4
script: dev
accents: yes — Taittirīya system (svarita ◌॑, anudātta ◌॒, ꣳ)
status: public domain (1937 print)
note: p.4 lower margin damaged
---
[p. 3]
## <a section heading, as printed>
<the text, line for line as printed; blank line between stanzas>
### <a sub-section heading>
[fn 1] <a footnote, where the page prints it>
```

Markup inside the text — the only markup there is:

| Line | Means | Becomes |
|---|---|---|
| `[p. 626]` | a new printed page begins | a small page marker; pages in the contents |
| `## …` / `### …` | a section / sub-section heading as printed | contents entry + Word heading & bookmark + HTML anchor |
| `[fn 1] …` | the page's footnote 1 | a footnote paragraph at that point |
| `[?X?]` / `[...]` | uncertain reading / illegible | highlighted |

Ask where the scan comes from if you can't tell: title, publisher/editor,
year and page go into `source`/`pages`, and `status` records whether it is
public domain or a copyrighted modern edition. That provenance is the point
of a compilation — later you or the user will need to know which book every
line came from. If the file already exists, read it first and append.

## Workflow

### 1. Prepare page images

```bash
uv run scripts/prepare_pages.py <file.pdf|.tif|.jpg ...> --out <work dir> --pages 3-5 --crop
```

For each page: a full-page PNG, overlapping horizontal **strips** (default 4),
and `manifest.json`. Work from the strips — a whole page gets downscaled
before you see it, and that erases vowel signs, conjunct detail and accent
strokes. Use more strips (`--strips 6`) for dense print or small type; fewer
for large type. Keep the work dir in a scratch location, not the user's
folders.

Check a scan has no text layer before transcribing: some PDFs are born
digital (`pymupdf` `page.get_text()` returns real text) and can be extracted
instead of read — but check the extracted text against the image, since
legacy-font PDFs often extract as garbage.

### 2. Transcribe — faithfully

Read each strip with the Read tool and write what is printed. The aim is a
**faithful copy of the page, not a corrected or selected text** — a
compilation is only trustworthy as a stand-in for the book if nothing was
quietly fixed, standardised or left out. Faithful is the default; the user
asking for it explicitly means hold the line even harder. So:

- **Everything on the page goes in**, in page order: headings, the mantras,
  the book's own instructions and prose (in whatever language — Telugu
  directions in a Sanskrit book stay), labels (*ślo॥ maṃ॥*), verse and
  section numbers, colophons (*iti …*), footnotes (`[fn N]`, at the point the
  page prints them), ornaments that mark a section end (`❖ ❖ ❖`).
- Two things are left out, because they are furniture, not text: the
  **running head and folio** (replaced by a `[p. N]` marker at each page
  start — so every line stays traceable), and pure layout (a `నమః ॥` set
  flush right is written at the end of its line; column spacing is not
  reproduced). If you leave out anything else, say what and why in `note:`.
- Keep the book's lines, word division, daṇḍas, numbers and labels.
- Mark a reading you can't be sure of as `[?X?]` (X = best guess) and an
  unreadable stretch as `[...]`. Don't guess silently: an unmarked guess in a
  sacred text is worse than a marked gap.
- A clearly printed misprint stays as printed; put the likely intended
  reading in the snippet's `note:`.
- Encode accents exactly as printed and in the right Unicode order (accent
  last in the akṣara). `references/transcription.md` has the Vedic mark
  table and the Devanāgarī/Telugu look-alike pairs that strips most often
  confuse (Telugu ష్ట/ష్ణ especially) — read it before a first
  transcription in a script.
- Strips overlap: don't copy the repeated lines twice.
- Mark each **section heading the book prints** with `##` (`###` for a
  sub-heading) — *atha prathamo nyāsaḥ*, *atha Śivārghya mantrāḥ*, a numbered
  anuvāka. These build the contents and bookmarks; don't invent headings the
  page doesn't have (add a `note:` instead if the book's structure is unclear).

**Long works (a whole booklet, dozens of pages).** Work page by page and
append each finished page to the compilation file straight away, so progress
survives an interruption and nothing depends on memory of earlier pages.
Survey first — `prepare_pages.py <book.pdf> --out <dir> --dpi 70 --strips 0
--sheets` tiles every page, 12 to an image, into `sheet-NN.png` — to see the
book's section structure before you start, and set `# toc:` (2 or 3) to the
depth that makes the contents useful. The lint warns when `[p. N]` markers
skip a number — the check that no page was missed.

### 3. Proofread against the image

A second, separate pass: go back over each strip and compare it with your
text **line by line, akṣara by akṣara**, looking especially at conjuncts,
vowel length, anusvāra vs arasunna/candrabindu, visarga, and every accent
mark. When a strip is too small to settle a doubt, open the full-page image
or crop tighter. Resolve what you can; leave `[?X?]` where you can't.

### 4. Build and check

```bash
uv run scripts/build_docx.py <file.compile.txt>     # -> .docx
uv run scripts/build_html.py <file.compile.txt>     # -> .html (accents rendered)
```

Both print `WARN` lines from a lint: mixed scripts within one word (a Telugu
letter typed into Devanāgarī), an accent placed before its vowel sign,
zero-width characters, Latin letters in Indic text, a skipped page number.
Fix every warning in the compilation file and rebuild.

Both outputs open with a **contents** list linked to every snippet and every
`##`/`###` heading, with its printed page. In Word the headings are real
heading styles (they appear in the Navigation Pane, View › Navigation Pane)
and each carries a bookmark (Insert › Bookmark lists them); the contents
entries are hyperlinks to those bookmarks. In HTML each heading has an anchor
and a ↑ link back to the contents.

Word defaults to Siddhanta for Devanāgarī and Gautami for Telugu — both
installed here and both verified to carry the Vedic marks — and Nirmala UI
for other scripts, set on the complex-script font slot. Word's handling of
stacked accents is weaker than a browser's, so for accented text the HTML is
the faithful reading copy; say so when you hand over the files. Override
fonts with `--font dev=… --font tel=…`.

**Look at the result, for accented text especially:**

```bash
uv run scripts/preview_render.py <file.html>        # -> <file>-render-N.png
```

Read the PNGs. The text being right doesn't prove the marks land on the right
akṣara: a box means the font lacks a glyph, a mark on a dotted circle means
wrong Unicode order. (Boxes for bare marks inside the Latin provenance text
are this renderer's missing fallback, not the page.) The in-app browser can't
script a local file, which is why this exists.

### 5. Report

Tell the user where the `.docx`, `.html` and `.compile.txt` are, how many
snippets and pages were added, and list every `[?…?]`/`[...]` with its
page — those are what a human needs to check against the book.

## Feeding a stotramālā page

A compilation is also a clean input for the `add-stotra` skill: its
`.docx` goes through `add-stotra/scripts/extract_doc.py`. Standardising
(word division, nasals, typo corrections, all logged) happens there — not
here, where the text stays true to the page.
