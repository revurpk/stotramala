---
name: review-works
description: >-
  Critically review a work on the stotramālā site (text, translation, word-by-word
  glosses, wiring) and fix the problems found. Use when the user asks to review,
  audit, proofread, QA or fix existing pages of the stotramala repo, one work
  or all of them. Meant to be run on the strongest available model.
---

# Review and fix works on stotramālā

**Model.** Run this on the strongest model available (recommended: Fable 5.2,
`claude-fable-5-2`, high effort; Opus 5.5 is an acceptable cheaper pass for the
long epics). If you are not on it, tell the user and let them switch first.

## Order of work
1. `python .claude/skills/review-works/scripts/manifest.py --pending` lists the
   series with verse counts and review status (`tools/reviews/status.json`).
   Scale is large (Rāmāyaṇa ~22k verses, Devībhāgavatam ~19k): review the short
   hand-built works fully first; for the epics review in samples (every page's
   first, last and a few random verses, plus every verse the checks flag).
2. Work one series at a time; one commit per series.

## Per work
- **Text.** Compare `tools/stotras/<slug>.py` IAST against the source named in
  `SOURCES.md`; look for typos, wrong sandhi, broken padas, missing or doubled
  verses, wrong verse numbers. Never silently change the text: log each
  emendation in `SOURCES.md`.
- **Translation.** Check each `gloss` for fidelity (no invented content, names
  and terms consistent, tentative where the Sanskrit is corrupt).
- **Word-by-word** (`tools/words/<slug>.txt`). Run `python tools/words_check.py
  <slug>`; examine every LOW flag, check meanings and compound splits.
- **Build and verify.** `python tools/build_stotra.py <slug>`;
  `.claude/skills/add-stotra/scripts/verify.py --data <slug>` (not for `src:"tel"`).
- **Record.** Write findings and fixes to `tools/reviews/<slug>.md` and update
  `tools/reviews/status.json` (`reviewer`, `date`, `fixed`, `open`).

## Rules
Fix what is clearly wrong; list uncertain points as open rather than guessing.
Commit locally with the usual Co-Authored-By trailer; push only if asked.
