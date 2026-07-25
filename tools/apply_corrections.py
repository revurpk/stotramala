#!/usr/bin/env python3
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Merge a reviewer's exported corrections into the repository.

Each stotra page carries a review/correction facility: a reader turns on
"suggest a correction", edits any line's rendering in the current script,
and exports a JSON file. This tool merges that export into

    tools/corrections/<slug>.json

which build_stotra.py bakes into `window.STOTRA_CORRECTIONS` — an
override that beats the automatic transliteration for the named lines.
The IAST in the data files stays the single source of truth; corrections
only touch the Devanāgarī / Telugu (or IAST display) of specific lines.

Usage:

    python tools/apply_corrections.py <exported-file.json> [more.json ...]
    python tools/apply_corrections.py --list          # show stored overrides

The exported file looks like:
    { "slug": "kanakadhara-stotram",
      "corrections": { "12": { "tel": "…", "dev": "…" } },
      "iast":        { "12": "the source IAST, for the reviewer's reference" } }

After merging, rebuild:  python tools/build_stotra.py <slug>
Review the diff before committing.
"""

import json
import pathlib
import sys

# the output carries Devanāgarī / Telugu; force UTF-8 so it prints on any console
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

CORR_DIR = pathlib.Path(__file__).resolve().parent / "corrections"
VALID_SCRIPTS = {"dev", "tel", "iast"}


def store_path(slug):
    return CORR_DIR / f"{slug}.json"


def load(slug):
    p = store_path(slug)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save(slug, data):
    CORR_DIR.mkdir(parents=True, exist_ok=True)
    ordered = {k: data[k] for k in sorted(data, key=lambda x: int(x))}
    store_path(slug).write_text(
        json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def merge_file(path):
    exp = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    slug = exp.get("slug")
    if not slug:
        sys.exit(f"{path}: no 'slug' field")
    corr = exp.get("corrections", {})
    store = load(slug)
    changed = 0
    for idx, scripts in corr.items():
        for sc, text in scripts.items():
            if sc not in VALID_SCRIPTS:
                print(f"  skip {idx}/{sc}: unknown script")
                continue
            cur = store.get(idx, {}).get(sc)
            if cur != text:
                store.setdefault(idx, {})[sc] = text
                changed += 1
                print(f"  line {idx} [{sc}] → {text}")
    save(slug, store)
    print(f"{slug}: {changed} correction(s) merged into {store_path(slug).name}")


def list_all():
    if not CORR_DIR.exists():
        print("no corrections stored")
        return
    for p in sorted(CORR_DIR.glob("*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        n = sum(len(v) for v in data.values())
        print(f"{p.stem}: {n} override(s) over {len(data)} line(s)")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    if argv[0] == "--list":
        list_all()
        return
    for path in argv:
        merge_file(path)


if __name__ == "__main__":
    main(sys.argv[1:])
