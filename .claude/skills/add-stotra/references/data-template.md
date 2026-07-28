# The `STOTRA` data file

Each page comes from `tools/stotras/<slug>.py`, a module with one dict named
`STOTRA`. `build_stotra.py` injects it into the shared shell and writes
`stotra/<deity>/<slug>-iast.html`. Below: the fields, then four worked shapes.

## Fields

| Key | Meaning |
|---|---|
| `deity` | folder under `stotra/` (ganesha, vishnu, rama, hanuman, devi, shiva, subrahmanya, venkateshwara, advaita, veda). Required. |
| `script` | `"dev"` opens the page in Devanāgarī (use for **accented Vedic** texts, where svaras only show in Devanāgarī). Omit for the default (IAST). |
| `src` | `"tel"` marks a **Telugu-source** page (Telugu is the truth, IAST is an aid, no Devanāgarī). Omit for Sanskrit pages. |
| `doc_title` / `app_title` / `h1` | page `<title>`, PWA name, and heading. Usually identical. |
| `subtitle` | one line under the title (e.g. "Ṛgveda 10.90 · the hymn of the Cosmic Being"). |
| `note` | optional italic caveat/description under the subtitle. Good place for "this page opens in Devanāgarī; IAST/Telugu are unaccented aids", or a redistribution notice. |
| `footer` | the source line ("Source: Sanskrit Wikisource — <title> (public domain)"). |
| `sections` | a list; each item is a verse dict (via `_v`) or the string `"ornament"` (a ❧ separator). |

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

Svaras marked after the vowel (`_` anudātta, `^` svarita). The page opens in
Devanāgarī; IAST/Telugu drop the marks.

```python
STOTRA = {
    "deity": "veda", "script": "dev",
    "doc_title": "Puruṣa Sūktam", "app_title": "Puruṣa Sūktam", "h1": "Puruṣa Sūktam",
    "subtitle": "Ṛgveda 10.90 · the hymn of the Cosmic Being",
    "note": "… The accented saṃhitā carries the Vedic pitch-accents (anudātta ॒ "
            "below, svarita ॑ above; udātta unmarked), shown in the Devanāgarī, in "
            "which this page opens; the IAST and Telugu are unaccented reading aids.",
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
