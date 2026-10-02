# The `STOTRA` data file

Each page comes from `tools/stotras/<slug>.py`, a module with one dict named
`STOTRA`. `build_stotra.py` injects it into the shared shell and writes
`stotra/<deity>/<slug>-iast.html`. Below: the fields, then four worked shapes.

## Fields

| Key | Meaning |
|---|---|
| `deity` | folder under `stotra/` (ganesha, vishnu, rama, hanuman, devi, shiva, subrahmanya, venkateshwara, advaita, veda, gita). Required. |
| `nav` | optional list of `(label, href)` links between the pages of a multi-page work, shown above "all stotras" — e.g. the Gītā's `("‹ chapter 1", "gita-bhashya-01-iast.html")`, `("all chapters", "../../index.html#gita")`. |
| `script` | `"dev"` opens the page in Devanāgarī (use for **accented Vedic** texts; svaras show in Devanāgarī and — drawn with CSS — in Telugu, not in IAST). Omit for the default (IAST). |
| `src` | `"tel"` marks a **Telugu-source** page (Telugu is the truth, IAST is an aid, no Devanāgarī). Omit for Sanskrit pages. |
| `doc_title` / `app_title` / `h1` | page `<title>`, PWA name, and heading. Usually identical. |
| `subtitle` | one line under the title (e.g. "Ṛgveda 10.90 · the hymn of the Cosmic Being"). |
| `note` | optional italic caveat/description under the subtitle. Good place for "this page opens in Devanāgarī; accents also in Telugu, IAST is an unaccented aid", or a redistribution notice. |
| `footer` | the source line ("Source: Sanskrit Wikisource — <title> (public domain)"). |
| `sections` | a list; each item is a verse dict (via `_v`) or the string `"ornament"` (a ❧ separator). |

Besides verse dicts and `"ornament"`, `sections` may hold three optional
types, for long ritual texts (vratakalpas, pūjā-vidhānas). All three are
Latin and outside `.sans`, so they are never transliterated:

| Item | Renders as | Use |
|---|---|---|
| `{"heading": "Gaṇapati Pūjā"}` | `.speaker` (centred small-caps) | section titles |
| `{"rubric": "Sip water three times…"}` | `.colophon-gloss` (italic note) | ritual directions, in your own English |
| verse dict with `"prose": True` | `.verse.viniyoga` (one size down) | saṅkalpa, āvāhana formulae, nāma lists |

For a text **with a commentary** (the Gītā with Śaṅkara's bhāṣya), four more
types; these are Sanskrit and inside `.sans`, so they render in every script:

| Item | Renders as | Use |
|---|---|---|
| `_v(…, bhashya=[…])` | a `bhāṣya` fold under the verse's translation | the commentary on that verse, one string per paragraph; a paragraph given as `{"text": …, "intro": True}` is the commentator's lead-in before the verse, set a shade lighter |
| `_v(…, words=[[w, m], …])` | a word-by-word list at the top of the verse's translation fold (the fold is then labelled "word by word · translation") | each pair is a Sanskrit word in IAST — unsandhied, in its pausal form, compound members hyphenated (`dharma-kṣetre`) — and its English; the word follows the script switch, the meaning is editable through *Suggest a correction* |
| a paragraph `{"text": …, "tr": "…"}` in a `bhashya` list | the English of that paragraph, set under it | a translated commentary |
| `{"bhashya": […], "summary": "…"}` | a standalone fold | a preface not tied to one verse (a chapter's opening, the upodghāta) |
| `{"speaker": "arjuna uvāca"}` | `.speaker` with a `.sans` line | who speaks the verses that follow |
| `{"colophon": "iti …", "gloss": "Thus ends …"}` | `.colophon` + `.colophon-gloss` | closing colophons, with an English gloss |

**Word-by-word lists for a stotra** go in a sidecar file rather than the data
file: `tools/words/<slug>.txt`, one line per unit that has `padas`, numbered
from 1 in page order.

```
# comment lines start with #
1 devi = O Goddess | tvam = you | bhakta-su-labhe = easily reached by devotees
2 śṛṇu = listen | deva = O Lord | pravakṣyāmi = I will tell
```

- `python tools\words_check.py --dump <slug> [FROM TO]` prints the numbered
  units to gloss, svara marks removed.
- Words in verse order, sandhi resolved, pausal forms (final `-m`, `-ḥ`),
  compound members hyphenated; a long ornate compound may stay one unit.
  Vedic words without svara marks. A page in Telugu (`src="tel"`) takes
  Telugu-script words, no hyphens.
- Follow the page's reading even where the usual text differs, and note the
  difference in SOURCES.md.
- The separators are exactly ` = ` and ` | `; a meaning must not contain
  either. A line the builder cannot parse stops the build.
- `python tools\words_check.py [<slug>]` reports coverage and flags units
  whose joined words stray from the text (a dropped or mistyped word). It
  cannot judge a meaning. Then rebuild the page.

A `words=` given in the data file wins over the sidecar line.

Give commentary paragraphs as prose (no `|`), keep the quotation marks as “ ”
(the renderer reads `'` and `’` as avagraha), and verify them with the same
render check as the padas — `verify.py --data` checks padas only.

For a long page with many `heading`s, set `"toc": True` in `STOTRA`: the
builder adds a collapsible **contents** panel under the header linking to
every heading (ids `sec-1`, `sec-2`, …), and a small ↑ on each heading back to
it. Use it once a page has roughly ten or more headings (the Satyanārāyaṇa
Vratakalpam has 52); leave it off for ordinary stotras — pages without it
render byte-identical.

`_v(padas, num, gloss)` → `{"padas": padas, "num": num, "gloss": gloss}`:
- `padas` — list of lines. Daṇḍas ride inline: end a line with `" |"` for a
  single daṇḍa, `" ||"` for a double one mid-verse. The final numbered daṇḍa
  goes in `num`, not the padas.
- `num` — the badge, e.g. `"|| 1 ||"`; `""` for an unnumbered block (śānti-pāṭha).
- `gloss` — your original translation.

## Shape 1 — verse stotra (numbered ślokas)

```python
def _v(l1, l2, n, gloss):
    return {"padas": [l1 + " |", l2], "num": f"|| {n} ||", "gloss": gloss}

STOTRA = {
    "deity": "vishnu",
    "doc_title": "Madhurāṣṭakam", "app_title": "Madhurāṣṭakam", "h1": "Madhurāṣṭakam",
    "subtitle": "Eight Verses on Sweetness · Vallabhācārya",
    "footer": "Source: Sanskrit Wikisource — Madhurāṣṭakam (public domain)",
    "sections": [
        _v("adharaṃ madhuraṃ vadanaṃ madhuraṃ …",
           "hṛdayaṃ madhuraṃ gamanaṃ madhuraṃ …", 1,
           "Sweet are his lips, sweet his face …"),
        # …
    ],
}
```

## Shape 2 — Telugu-source kīrtana (`src:"tel"`)

Telugu is the truth; teltools makes IAST as a reading aid (no Devanāgarī).
teltools is a Sanskrit transliterator, so it mishandles the Telugu short e/o
(ె/ొ) — the render shell already repairs that for `src:"tel"` pages, so just
supply clean Telugu.

```python
def _v(lines, gloss):
    return {"padas": lines, "num": "", "gloss": gloss}

STOTRA = {
    "src": "tel", "deity": "venkateshwara",
    "doc_title": "Jo Achyutānanda", "app_title": "Jo Achyutānanda", "h1": "Jo Achyutānanda",
    "subtitle": "Annamayya · a cradle-song to the child Kṛṣṇa",
    "note": "A Telugu-language lullaby … The Telugu is the source; the IAST is a reading aid.",
    "footer": "Source: Telugu Wikisource — జో అచ్యుతానంద … (public domain)",
    "sections": [ _v(["జోఅచ్యుతానంద జోజో ముకుంద", "…"], "Sleep, Acyutānanda …"), ],
}
```

## Shape 3 — prose-mantra Upaniṣad

Daṇḍas inline; numbered mantras between śānti-pāṭha ornaments; section labels
folded into the gloss. Anunāsika comes through as `ṁ`.

```python
STOTRA = {
    "deity": "ganesha",
    "doc_title": "Gaṇapati Atharvaśīrṣa", "app_title": "Gaṇapati Atharvaśīrṣa",
    "h1": "Gaṇapati Atharvaśīrṣa",
    "subtitle": "The Atharva-Crown of Gaṇapati · Gaṇeśa Upaniṣad",
    "note": "A short Upaniṣad … framed by the peace-invocations (śānti-pāṭha).",
    "footer": "Source: Sanskrit Wikisource — गणपत्यथर्वशीर्षम् (public domain)",
    "sections": [
        _v(["oṃ bhadraṃ karṇebhiḥ śṛṇuyāma devāḥ |", "…", "oṃ śāntiḥ śāntiḥ śāntiḥ ||"],
           "", "Śānti-pāṭha. Oṃ. May we hear what is auspicious …"),
        "ornament",
        _v(["hariḥ oṃ namaste gaṇapataye |", "…", "tvaṃ sākṣādātmā'si nityam"],
           "|| 1 ||", "Hariḥ Oṃ. Salutation to you, Gaṇapati …"),
        # … mantras 2-14 …
        "ornament",
        _v(["oṃ sahanāvavatu |", "…", "oṃ śāntiḥ śāntiḥ śāntiḥ ||"], "", "Closing śānti. …"),
    ],
}
```

## Shape 4 — accented Vedic sūkta (`script:"dev"`)

Svaras marked after the vowel (`_` anudātta, `^` svarita, `^^` the Taittirīya dīrgha
svarita ᳚). The page opens in
Devanāgarī; Telugu shows them too (drawn with CSS, pipeline.md §3); IAST drops them.

```python
STOTRA = {
    "deity": "veda", "script": "dev",
    "doc_title": "Puruṣa Sūktam", "app_title": "Puruṣa Sūktam", "h1": "Puruṣa Sūktam",
    "subtitle": "Ṛgveda 10.90 · the hymn of the Cosmic Being",
    "note": "… The accented saṃhitā carries the Vedic pitch-accents (anudātta ॒ "
            "below, svarita ॑ above; udātta unmarked), shown in the Devanāgarī, in "
            "which this page opens, and in the Telugu; the IAST is an unaccented reading aid.",
    "footer": "Source: Sanskrit Wikisource — ऋग्वेदः सूक्तं १०.९० (accented saṃhitā, Sāyaṇa edition; public domain)",
    "sections": [
        _v(["sa_hasra^śīrṣā_ puru^ṣaḥ sahasrā_kṣaḥ sa_hasra^pāt |",
            "sa bhūmiṃ^ vi_śvato^ vṛ_tvātya^tiṣṭhaddaśāṅgu_lam"], "|| 1 ||",
           "The Puruṣa has a thousand heads …"),
        # …
    ],
}
```

Use two ornaments to bracket a two-hymn set (e.g. Manyu Sūkta = RV 10.83 + 10.84,
numbered 1–14 with one ornament between).
