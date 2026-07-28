---
name: add-stotra
description: >-
  Add a new devotional text — a stotra, sūkta, aṣṭaka, Upaniṣad, kīrtana, or
  daṇḍaka — to the stotramālā site (github.com/revurpk/stotramala) from a
  source link or file path. Use this whenever the user wants to add, build,
  source, or include a Sanskrit or Telugu devotional text on the stotramala
  repo — e.g. "add Śrī Sūktam to the site", "build a page for this hymn",
  "source Puruṣa Sūkta with svaras", or when they hand you a Wikisource /
  Ṛgveda URL or a text/PDF to turn into a page. The skill triages the source
  and recommends an optimal model + reasoning effort before the heavy work,
  converts Devanāgarī to the IAST source-of-truth, writes the data file with
  original translations, builds and round-trip-verifies the page, and wires it
  into index.html / README.md / SOURCES.md. Reach for this even if the user
  doesn't name the pipeline — any "put this text on the stotra site" request
  qualifies.
---

# Add a stotra / sūkta entry to stotramālā

The site (`C:\Users\net\Projects\stotramala`) is a self-contained three-script
reader. Every page is generated from one data file by `tools/build_stotra.py`,
which injects the text into a shared shell. **IAST is the single source of
truth**; Devanāgarī and Telugu are produced in the browser by the inlined
`teltools` transliterator. Your job is to turn a source into a correct,
well-provenanced page without ever silently altering the text.

## Step 0 — Triage the source FIRST

Before any extraction, run the triage script. It classifies the source and
recommends a model + reasoning effort, because the categories differ hugely in
how much careful judgement they need.

```bash
python .claude/skills/add-stotra/scripts/triage.py <url-or-path>
```

If you are **not** already running under the recommended model, tell the user
and let them re-invoke before you do the heavy work — don't grind a
max-effort job on a small model, or waste a large model on a trivial one. The
categories and why they matter live in `references/triage.md`; the short form:

| Category | Model / effort | Because |
|---|---|---|
| `clean-stotra` | sonnet / medium | short, unaccented, `<poem>` — mechanical |
| `clean-but-large` | opus / medium | easy mechanics, lots of accurate translation |
| `accented-vedic` | opus / high | svara extraction + byte-exact round-trip, archaic text |
| `commentary-interleaved` | opus / high | must separate mūla from bhāṣya cleanly |
| `scanned-pdf` / `binary/image` | opus / high | OCR / visual reading, error-prone |
| `little-devanagari` | opus / high | probably the wrong page — find the real text |

Trust your eyes over the number: if the text looks messier than the count
suggests (OCR errors, odd conjuncts, a copyrighted-edition notice), bump up.

## Step 1 — Fetch & inspect

Wikisource is the preferred source (clean license). Pull raw wikitext:

```bash
# PowerShell (handles Unicode titles cleanly):
$u="https://sa.wikisource.org/w/index.php?title=<TITLE>&action=raw"
Invoke-WebRequest -Uri $u -UseBasicParsing | % Content
```

Read the whole thing. Note: `<poem>` blocks, section headers (`== … ==`,
`॥ … ॥`), verse numbering (`॥ १ ॥`), a śānti-pāṭha, interpolated commentator
ślokas, OCR errors, and **whether it carries svaras** (`॒` `॑`). Decide the
deity/section folder (`stotra/<deity>/`) — existing folders: ganesha, vishnu,
rama, hanuman, devi, shiva, subrahmanya, venkateshwara, advaita (non-personal
Vedānta), veda (accented Vedic hymns).

## Step 2 — Convert Devanāgarī → IAST

Use the bundled converter — don't re-derive it. It carries the exact encoding
conventions the render shell expects (svaras as `_`/`^` after the vowel,
anunāsika → `ṁ`, pluta numerals kept, avagraha → `'`).

```bash
python .claude/skills/add-stotra/scripts/dev2iast.py --danda < lines.txt   # prose mantras
python .claude/skills/add-stotra/scripts/dev2iast.py --samhita rv.txt       # accented Ṛgveda
```

For accented Ṛgveda pages the accented saṃhitā is in the pratīka lines; see
`references/pipeline.md` for the pairing (contiguous vs padapāṭha-interleaved)
and the svara details. **No silent emendation**: if the source has a typo or a
variant, keep it or fix it *and log the fix* in SOURCES.md.

## Step 3 — Write the data file

Create `tools/stotras/<slug>.py` with a module-level `STOTRA` dict. The full
field reference and worked examples (verse stotra, Telugu-source kīrtana,
prose-mantra Upaniṣad, accented sūkta) are in `references/data-template.md`.
Key points: `deity` picks the folder; `script:"dev"` opens accented pages in
Devanāgarī and `src:"tel"` marks Telugu-source pages; sections are `_v(padas,
num, gloss)` dicts or the string `"ornament"` for a separator; daṇḍas ride
inline as `|` / `||` and the verse number goes in `num`.

## Step 4 — Translate

Write **your own** translations — accurate, plain, faithful to the Sanskrit,
never copied or closely paraphrased from any edition's translation (especially
a copyrighted one). Fold section labels (Gāyatrī, dhyāna, phalaśruti…) into the
gloss where they add context. This is the part that most wants a strong model.

## Step 5 — Build

```bash
python tools/build_stotra.py <slug>          # one page
python tools/build_stotra.py --all           # after ANY shared-shell change
```

## Step 6 — Verify the round-trip

Never ship unverified. The bundled verifier renders IAST → Devanāgarī in **pure
Python** — the exact teltools pipeline, svaras included — so it needs no browser
and no dev server (the sandbox can block both):

```bash
python .claude/skills/add-stotra/scripts/verify.py --render < iast_lines.txt          # eyeball
python .claude/skills/add-stotra/scripts/verify.py --check iast_lines.txt source.txt   # byte-exact PASS/FAIL
```

For accented texts this is the real check: the rendered Devanāgarī must match the
source accented text **byte-exact** (a mismatch right before a visarga/anusvāra
is a canonical-ordering issue — already handled, but confirm). Also sanity-check
the built page: the `|| N ||` badge count matches the verse count and ornaments
match. Opening the built page in a browser to look at it is a nice-to-have, not
the verification — don't depend on it. Details in `references/pipeline.md` §4.

## Step 7 — Wire it in

Three edits, each in the right place:
- **index.html** — add an `.entry` under the correct `<p class="deity">` heading.
- **README.md** — add a row to the Contents table.
- **SOURCES.md** — add a `§N.M` provenance block: work, source URL, date, text
  status, and **editorial notes** (every emendation, the svara handling,
  anything dropped). This is the project's integrity record — be thorough.

## Step 8 — Commit & push

One text per commit. Message: what was added, the source, and any caveats.
End with the `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` trailer.
Push only after the round-trip verifies.

## Guardrails

- **Licensing.** Wikisource (PD / CC-BY-SA) and genuine public-domain scans are
  fine to redistribute. **sanskritdocuments.org and GRETIL/TITUS texts are NOT**
  — they carry explicit "do not repost" terms or proprietary restrictions;
  reposting them conflicts with the site's CC-BY license and the repo's
  fetch-don't-redistribute convention. The ancient verses are public domain, but
  a *restricted digital edition* of them is not yours to republish. If the only
  accented source is restricted, stop and tell the user rather than reposting.
- **No silent emendation.** Every change to the received text is logged in
  SOURCES.md. Faithfulness first.
- **Three scripts must all be right.** Verify Devanāgarī, IAST, and Telugu
  before shipping — a wrong akṣara is worse than no page.
