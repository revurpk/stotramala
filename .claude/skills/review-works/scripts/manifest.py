#!/usr/bin/env python3
"""List every work on the site, grouped into series, with unit counts and review status.

  python .claude/skills/review-works/scripts/manifest.py            # all series
  python .claude/skills/review-works/scripts/manifest.py --pending  # only unreviewed
  python .claude/skills/review-works/scripts/manifest.py --series saptashati

Status lives in tools/reviews/status.json: {"<slug>": {"reviewer": "...", "date": "...", "fixed": n, "open": n}}
"""
import json, re, sys, importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "tools" / "stotras"
WORDS = ROOT / "tools" / "words"
STATUS = ROOT / "tools" / "reviews" / "status.json"


def series_of(slug):
    s = re.sub(r"(-\d+)+$", "", slug)
    s = re.sub(r"-(purva|uttara|sukta|[a-z]+-\d+)$", "", s) if s.startswith("saptashati") else s
    return s


def units(slug):
    """Number of verse units, counted the same way tools/words_check.py counts them."""
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import words_check
        return len(words_check.verses(slug))
    except Exception:
        return -1


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    status = json.loads(STATUS.read_text(encoding="utf-8")) if STATUS.exists() else {}
    only_pending = "--pending" in argv
    want = argv[argv.index("--series") + 1] if "--series" in argv else None
    groups = {}
    for p in sorted(DATA.glob("*.py")):
        groups.setdefault(series_of(p.stem), []).append(p.stem)
    for ser, slugs in sorted(groups.items()):
        if want and ser != want:
            continue
        done = [s for s in slugs if s in status]
        if only_pending and len(done) == len(slugs):
            continue
        n = sum(max(units(s), 0) for s in slugs)
        w = sum(1 for s in slugs if (WORDS / f"{s}.txt").exists())
        print(f"{ser:34} pages {len(slugs):4}  verses {n:6}  words {w:3}/{len(slugs):<4} reviewed {len(done)}/{len(slugs)}")


if __name__ == "__main__":
    main(sys.argv[1:])
