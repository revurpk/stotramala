<!-- Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE) -->
# Rendering corrections

Human-reviewed overrides for the automatic transliteration on the stotra
pages. One file per stotra, `<slug>.json`, keyed by the **line index**
(the position of a `.sans` node on the page, counting every verse line,
verse number, speaker, and colophon from 0) → script → corrected text:

```json
{
  "12": { "tel": "…corrected Telugu…", "dev": "…corrected Devanāgarī…" }
}
```

`build_stotra.py` bakes each file into its page as
`window.STOTRA_CORRECTIONS`; at runtime an entry overrides the
teltools output for that line and script. The IAST in
`tools/stotras/<slug>.py` remains the single source of truth — these
overrides only touch the Devanāgarī / Telugu (or, rarely, the IAST
*display*) of specific lines where the mechanical transliteration is
wrong.

**How entries get here:** a reader opens a page, taps *suggest a
correction*, edits the offending line, and exports a JSON file; the
maintainer runs `python tools/apply_corrections.py <export.json>`, which
merges it here. Then rebuild the page and review the diff.
