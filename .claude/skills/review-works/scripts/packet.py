#!/usr/bin/env python3
"""Review records and the human review packets made from them.

A review of a series is recorded in tools/reviews/<series>.json:

  {"series": "meghaduta-purva",
   "reviewer": "claude-fable-5-2", "date": "2026-11-14",
   "coverage": "full" | "sample" | "mechanical",
   "scope": "what was and was not checked, in a sentence or two",
   "items": [
     {"slug": "meghaduta-purva", "unit": 14,      # unit 0 = the page as a whole
      "area": "text" | "translation" | "words" | "source" | "wiring",
      "status": "fixed" | "open",
      "issue": "what is wrong or doubtful",
      "change": "for fixed items: what was changed",
      "options": ["A …", "B …"],                  # open items: the choices
      "recommend": "A, because …",                # open items: the reviewer's pick
      "decision": ""}                             # filled in by the human
   ]}

  packet.py build [<series> …]   write tools/reviews/packets/<series>.md for each
                                 record (all records if none named), refresh
                                 status.json and tools/reviews/README.md
  packet.py collect [<series> …] copy the Decision lines the human wrote in the
                                 packets back into the records
  packet.py decided              list open items that now have a decision
  packet.py check                validate every record

`build` runs `collect` first, so decisions written in a packet survive a rebuild.
An item is identified by slug, unit, area and a hash of its issue text.
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "tools" / "reviews"
PACK = REV / "packets"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import words_check as wc  # noqa: E402
import audit  # noqa: E402

AREAS = {"text", "translation", "words", "source", "wiring"}
STATES = {"fixed", "open"}
COVER = {"full", "sample", "mechanical"}


def iid(it):
    h = hashlib.sha1(it["issue"].encode("utf-8")).hexdigest()[:6]
    return f"{it['slug']}:{it['unit']}:{it['area']}:{h}"


def records(names=None):
    out = []
    for p in sorted(REV.glob("*.json")):
        if p.name == "status.json" or (names and p.stem not in names):
            continue
        out.append((p, json.loads(p.read_text(encoding="utf-8"))))
    return out


def validate(p, r):
    errs = []
    for k in ("series", "reviewer", "date", "coverage", "scope", "items"):
        if k not in r:
            errs.append(f"missing key {k}")
    if r.get("coverage") not in COVER:
        errs.append(f"coverage must be one of {sorted(COVER)}")
    if r.get("series") != p.stem:
        errs.append("series does not match the file name")
    seen = set()
    for n, it in enumerate(r.get("items", []), 1):
        w = f"item {n}"
        for k in ("slug", "unit", "area", "status", "issue"):
            if k not in it:
                errs.append(f"{w}: missing {k}")
        if errs and errs[-1].startswith(w):
            continue
        if not (wc.DATA / f"{it['slug']}.py").exists():
            errs.append(f"{w}: no such page {it['slug']}")
        if it["area"] not in AREAS:
            errs.append(f"{w}: area {it['area']!r}")
        if it["status"] not in STATES:
            errs.append(f"{w}: status {it['status']!r}")
        if it["status"] == "fixed" and not it.get("change"):
            errs.append(f"{w}: a fixed item needs 'change'")
        if it["status"] == "open" and not (it.get("options") and it.get("recommend")):
            errs.append(f"{w}: an open item needs 'options' and 'recommend'")
        if iid(it) in seen:
            errs.append(f"{w}: duplicate of an earlier item")
        seen.add(iid(it))
    return errs


def collect(names=None):
    n = 0
    for p, r in records(names):
        f = PACK / f"{p.stem}.md"
        if not f.exists():
            continue
        found = {}
        for m in re.finditer(r"<!-- id: (\S+) -->(.*?)(?=<!-- id: |\Z)", f.read_text(encoding="utf-8"), re.S):
            d = re.search(r"^\*\*Decision:\*\*[ \t]*(.*?)\s*(?=^---|^## |\Z)", m.group(2), re.S | re.M)
            if d and d.group(1).strip():
                found[m.group(1)] = " ".join(d.group(1).split())
        changed = False
        for it in r["items"]:
            d = found.get(iid(it))
            if d and d != it.get("decision", ""):
                it["decision"], changed = d, True
                n += 1
        if changed:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return n


def unit_block(slug, unit, cache):
    """The page text, translation and words of a unit, as markdown."""
    if not unit:
        return ""
    if slug not in cache:
        S = audit.load(slug)
        cache[slug] = ([s for s in S["sections"] if isinstance(s, dict) and "padas" in s],
                       audit.sidecar(slug)[0] or {})
    vs, W = cache[slug]
    if not 1 <= unit <= len(vs):
        return ""
    v = vs[unit - 1]
    out = ["> " + wc.plain(p) + "  " for p in v["padas"]]
    if v.get("num"):
        out[-1] = out[-1].rstrip() + "  " + v["num"].replace("|", "‖").replace("‖‖", "‖") + "  "
    if (v.get("gloss") or "").strip():
        out += [">", "> *" + v["gloss"].strip() + "*"]
    if unit in W:
        out += [">", "> <sub>" + " · ".join(f"{w} = {m}" for w, m in W[unit]) + "</sub>"]
    return "\n".join(out) + "\n"


def page_link(slug):
    S = audit.load(slug)
    hits = list((ROOT / "stotra").glob(f"*/{slug}-iast.html"))
    rel = hits[0].relative_to(ROOT).as_posix() if hits else f"stotra/{S['deity']}/{slug}-iast.html"
    return f"[{slug}](../../../{rel})"


def build(names=None):
    PACK.mkdir(parents=True, exist_ok=True)
    collect(names)
    status = {}
    sp = REV / "status.json"
    if sp.exists():
        status = json.loads(sp.read_text(encoding="utf-8"))
    for p, r in records(names):
        errs = validate(p, r)
        if errs:
            print(f"{p.name}: NOT BUILT\n  " + "\n  ".join(errs))
            continue
        cache = {}
        opn = [it for it in r["items"] if it["status"] == "open"]
        fixed = [it for it in r["items"] if it["status"] == "fixed"]
        L = [f"# Review packet · {r['series']}", "",
             f"Reviewed {r['date']} by `{r['reviewer']}` · coverage: **{r['coverage']}**", "",
             r["scope"], "",
             f"**{len(opn)} item(s) need your decision; {len(fixed)} fixed in the review.**", ""]
        if opn:
            L += ["Write your answer after **Decision:** under each item (a letter, or your own words),",
                  "then ask for the decisions to be applied. Leave it empty to keep things as they are.", ""]
            L += ["## Needs your decision", ""]
            for n, it in enumerate(opn, 1):
                where = f"unit {it['unit']}" if it["unit"] else "whole page"
                L += [f"### {n}. {page_link(it['slug'])} · {where} · {it['area']}",
                      f"<!-- id: {iid(it)} -->", ""]
                blk = unit_block(it["slug"], it["unit"], cache)
                if blk:
                    L += [blk]
                L += [f"**Issue.** {it['issue']}", ""]
                L += [f"- {o}" for o in it["options"]] + [""]
                L += [f"**Recommended.** {it['recommend']}", "",
                      f"**Decision:** {it.get('decision', '')}", "", "---", ""]
        if fixed:
            L += ["## Fixed in the review", "",
                  "| Page | Unit | Area | Issue | Change |", "|---|---|---|---|---|"]
            for it in fixed:
                esc = lambda s: s.replace("|", "\\|").replace("\n", " ")
                L.append(f"| {it['slug']} | {it['unit'] or '—'} | {it['area']} | {esc(it['issue'])} | {esc(it['change'])} |")
            L.append("")
        (PACK / f"{p.stem}.md").write_text("\n".join(L), encoding="utf-8")
        slugs = sorted(q.stem for q in wc.DATA.glob("*.py") if audit.series_of(q.stem) == r["series"])
        for s in slugs:
            status[s] = {"reviewer": r["reviewer"], "date": r["date"], "coverage": r["coverage"],
                         "fixed": sum(1 for it in fixed if it["slug"] == s),
                         "open": sum(1 for it in opn if it["slug"] == s)}
        print(f"{p.stem}: {len(opn)} open, {len(fixed)} fixed → tools/reviews/packets/{p.stem}.md")
    sp.write_text(json.dumps(status, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    rows = []
    for p, r in records():
        if validate(p, r):
            continue
        o = sum(1 for it in r["items"] if it["status"] == "open")
        d = sum(1 for it in r["items"] if it["status"] == "open" and it.get("decision"))
        f = sum(1 for it in r["items"] if it["status"] == "fixed")
        rows.append(f"| [{r['series']}](packets/{r['series']}.md) | {r['coverage']} | {r['date']} | {o} | {d} | {f} |")
    (REV / "README.md").write_text("\n".join(
        ["# Reviews", "",
         "One record (`<series>.json`) and one packet (`packets/<series>.md`) per reviewed work.",
         "The packets list what needs a human decision; see `.claude/skills/review-works`.", "",
         "| Work | Coverage | Date | Open | Decided | Fixed |", "|---|---|---|---|---|---|"] + rows + [""]),
        encoding="utf-8")


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv:
        print(__doc__)
        return
    cmd, names = argv[0], set(argv[1:]) or None
    if cmd == "build":
        build(names)
    elif cmd == "collect":
        print(f"{collect(names)} decision(s) collected")
    elif cmd == "decided":
        collect()
        for p, r in records():
            for it in r["items"]:
                if it["status"] == "open" and it.get("decision"):
                    print(f"{it['slug']} unit {it['unit']} [{it['area']}] {it['issue'][:70]}\n    → {it['decision']}")
    elif cmd == "check":
        bad = 0
        for p, r in records(names):
            for e in validate(p, r):
                bad += 1
                print(f"{p.name}: {e}")
        print("ok" if not bad else f"{bad} problem(s)")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
