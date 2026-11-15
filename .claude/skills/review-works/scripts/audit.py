#!/usr/bin/env python3
"""Mechanical checks on a work, and a reader for reviewing it.

  audit.py <slug> …             flags for those pages
  audit.py --series <name>      flags for every page of a series
  audit.py --all --summary      one line per series: flag counts by code
  audit.py --show <slug> [FROM TO]     text + translation + words, unit by unit
  audit.py --sample <slug> [N]         a fixed sample of N units (default 12):
                                       first, last, every flagged unit, then
                                       units picked by a seed made from the slug

The flags find what a script can find. They do not judge whether a
translation or a gloss is right: that is the reviewer's job.

Codes
  T-NOGLOSS   unit has no sentence translation (reported once per page with a count)
  T-MARK      translation carries a doubt marker (tentative, corrupt, [?] …)
  T-RATIO     translation much shorter or longer than the text suggests
  T-PUNCT     unbalanced quotes or brackets in the translation
  X-CHAR      character that does not belong in IAST text
  X-DUP       unit repeats the text of another unit on the page
  X-NUM       verse numbers do not run in order
  X-EMPTY     unit with an empty pada
  W-NONE      page has no word-by-word sidecar (reported once)
  W-MISS      unit missing from the sidecar
  W-EXTRA     sidecar has a unit the page does not
  W-LOW       glossed words do not add up to the unit's text (score given)
  W-FORM      malformed sidecar line (segment without " = ", empty side)
  W-CHAR      character that does not belong in an IAST word
  P-NOPAGE    the built HTML page is missing
"""
import difflib, hashlib, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import words_check as wc  # noqa: E402
from manifest import series_of  # noqa: E402

IAST = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
           "āīūṛṝḷḹṃṁḥṅñṭḍṇśṣĀĪŪṚṜḶḸṂḤṄÑṬḌṆŚṢ"
           " -_^|'’‘“”\"().,;:!?—–…∗*[]/0123456789ऽ")
MARK = re.compile(r"\[\?\]|\(\?\)|\btentative|\bcorrupt|\buncertain|\bunclear|\bobscure\b|"
                  r"\bbroken\b|\btruncated|\bdoubtful|\bconjectur|\bperhaps\b|\blit\. ?\?", re.I)
PAIRS = [("(", ")"), ("[", "]"), ("“", "”")]


def load(slug):
    import importlib.util
    spec = importlib.util.spec_from_file_location("m", wc.DATA / f"{slug}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.STOTRA


def generated(slug):
    """The generator named in the data file's header, or ''."""
    head = (wc.DATA / f"{slug}.py").read_text(encoding="utf-8")[:700]
    m = re.search(r"(?:written|generated|built) by\s+(\S+\.py)", head, re.I)
    return m.group(1) if m else ""


def sidecar(slug):
    """({unit: [[word, meaning]…]}, [(lineno, problem)])."""
    out, bad = {}, []
    p = wc.WORDS / f"{slug}.txt"
    if not p.exists():
        return None, bad
    for ln, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) < 2 or not parts[0].isdigit():
            bad.append((ln, "line does not start with a unit number"))
            continue
        n, items = int(parts[0]), []
        if n in out:
            bad.append((ln, f"unit {n} given twice"))
        for seg in parts[1].split(" | "):
            if " = " not in seg:
                bad.append((ln, f"unit {n}: segment without ' = ': {seg[:40]!r}"))
                continue
            w, m = seg.split(" = ", 1)
            if not w.strip() or not m.strip():
                bad.append((ln, f"unit {n}: empty word or meaning in {seg[:40]!r}"))
            if "|" in m or " = " in m:
                bad.append((ln, f"unit {n}: separator inside a meaning: {seg[:40]!r}"))
            items.append([w, m])
        out[n] = items
    return out, bad


def score(v, items):
    return difflib.SequenceMatcher(None, wc.norm(" ".join(v["padas"])),
                                   wc.norm(" ".join(w for w, _ in items)), autojunk=False).ratio()


def audit(slug):
    """[(code, unit or 0, detail)]"""
    S = load(slug)
    tel = S.get("src") == "tel"
    vs = [s for s in S["sections"] if isinstance(s, dict) and "padas" in s]
    F = []
    if not (ROOT / "stotra" / S["deity"] / f"{slug}-iast.html").exists() and \
       not list((ROOT / "stotra").glob(f"*/{slug}*.html")):
        F.append(("P-NOPAGE", 0, "no built page found"))
    nog = [i for i, v in enumerate(vs, 1) if "gloss" in v and not (v.get("gloss") or "").strip()
           and not v.get("te") and not v.get("en")]
    if nog:
        F.append(("T-NOGLOSS", 0, f"{len(nog)} of {len(vs)} units have no translation"
                  + ("" if len(nog) == len(vs) else f": {nog[:12]}{'…' if len(nog) > 12 else ''}")))
    seen, last = {}, None
    for i, v in enumerate(vs, 1):
        text = " ".join(v["padas"])
        if any(not p.strip() for p in v["padas"]):
            F.append(("X-EMPTY", i, "empty pada"))
        if not tel:
            odd = sorted({c for c in text if c not in IAST})
            if odd:
                F.append(("X-CHAR", i, " ".join(f"{c!r} U+{ord(c):04X}" for c in odd)))
        key = wc.norm(text)
        if len(key) > 24:
            if key in seen:
                F.append(("X-DUP", i, f"same text as unit {seen[key]}"))
            else:
                seen[key] = i
        m = re.search(r"\d+", v.get("num") or "")
        if m:
            n = int(m.group())
            if last is not None and n not in (last + 1, 1) and n != last:
                F.append(("X-NUM", i, f"number {n} follows {last}"))
            last = n
        g = (v.get("gloss") or "").strip()
        if g:
            if MARK.search(g):
                F.append(("T-MARK", i, MARK.search(g).group(0)))
            for a, b in PAIRS:
                if g.count(a) != g.count(b):
                    F.append(("T-PUNCT", i, f"{g.count(a)} {a} against {g.count(b)} {b}"))
            if not tel and len(key) > 30:
                r = len(g) / len(text)
                if r < 0.25 or r > 5:
                    F.append(("T-RATIO", i, f"translation is {r:.2f}× the text's length"))
    W, bad = sidecar(slug)
    if W is None:
        F.append(("W-NONE", 0, "no word-by-word sidecar"))
    else:
        for ln, why in bad:
            F.append(("W-FORM", 0, f"line {ln}: {why}"))
        for i, v in enumerate(vs, 1):
            if i not in W:
                F.append(("W-MISS", i, "unit not glossed"))
                continue
            r = score(v, W[i])
            if r < 0.84:
                F.append(("W-LOW", i, f"score {r:.2f}"))
            if not tel:
                odd = sorted({c for w, _ in W[i] for c in w if c not in IAST})
                if odd:
                    F.append(("W-CHAR", i, " ".join(f"{c!r} U+{ord(c):04X}" for c in odd)))
        for n in sorted(W):
            if n > len(vs):
                F.append(("W-EXTRA", n, "sidecar unit beyond the page's last unit"))
    return F


def show(slug, units):
    S = load(slug)
    vs = [s for s in S["sections"] if isinstance(s, dict) and "padas" in s]
    W, _ = sidecar(slug)
    for i in units:
        if not 1 <= i <= len(vs):
            continue
        v = vs[i - 1]
        print(f"── {slug} unit {i}  {v.get('num') or ''}")
        for p in v["padas"]:
            print("   " + wc.plain(p))
        if (v.get("gloss") or "").strip():
            print("   ⇒ " + v["gloss"].strip())
        if W and i in W:
            print("   · " + " | ".join(f"{w} = {m}" for w, m in W[i]))


def sample(slug, n):
    S = load(slug)
    total = len([s for s in S["sections"] if isinstance(s, dict) and "padas" in s])
    if not total:
        return []
    pick = {1, total} | {u for _, u, _ in audit(slug) if u}
    rnd = random.Random(int(hashlib.sha1(slug.encode()).hexdigest()[:8], 16))
    rest = [i for i in range(1, total + 1) if i not in pick]
    rnd.shuffle(rest)
    pick |= set(rest[:max(0, n - 2)])
    return sorted(pick)


def all_slugs():
    return sorted(p.stem for p in wc.DATA.glob("*.py"))


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv:
        print(__doc__)
        return
    if argv[0] == "--show":
        S = load(argv[1])
        total = len([s for s in S["sections"] if isinstance(s, dict) and "padas" in s])
        a, b = (int(argv[2]), int(argv[3])) if len(argv) > 3 else (1, total)
        show(argv[1], range(a, b + 1))
        return
    if argv[0] == "--sample":
        show(argv[1], sample(argv[1], int(argv[2]) if len(argv) > 2 else 12))
        return
    summary = "--summary" in argv
    if "--all" in argv:
        slugs = all_slugs()
    elif "--series" in argv:
        want = argv[argv.index("--series") + 1]
        slugs = [s for s in all_slugs() if series_of(s) == want]
    else:
        slugs = [a for a in argv if not a.startswith("--")]
    by_series = {}
    for slug in slugs:
        try:
            F = audit(slug)
        except Exception as e:  # a page that cannot be loaded is itself a finding
            F = [("P-LOAD", 0, f"{type(e).__name__}: {e}")]
        if summary:
            d = by_series.setdefault(series_of(slug), {})
            for code, _, _ in F:
                d[code] = d.get(code, 0) + 1
            continue
        gen = generated(slug)
        print(f"{slug}: {len(F)} flag(s)" + (f"   [generated by {gen}: fix upstream]" if gen else ""))
        for code, u, detail in F:
            print(f"  {code:10} {('unit ' + str(u)) if u else 'page':10} {detail}")
    for ser, d in sorted(by_series.items()):
        print(f"{ser:36} " + ("  ".join(f"{k} {v}" for k, v in sorted(d.items())) or "clean"))


if __name__ == "__main__":
    main(sys.argv[1:])
