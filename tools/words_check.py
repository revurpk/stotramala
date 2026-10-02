# -*- coding: utf-8 -*-
"""Word-by-word glosses: dump the verses to gloss, and check the glosses.

    python tools/words_check.py --dump <slug> [FROM TO]   numbered verses
    python tools/words_check.py [<slug> …]                coverage + sanity

The check joins each verse's glossed words and compares them with the verse
text, ignoring sandhi-level differences, so a skipped or mistyped word shows
up as a low score. It cannot tell whether a meaning is right.
"""
import difflib
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "tools" / "stotras"
WORDS = ROOT / "tools" / "words"


def verses(slug):
    spec = importlib.util.spec_from_file_location("m", DATA / f"{slug}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return [s for s in mod.STOTRA["sections"] if isinstance(s, dict) and "padas" in s]


def plain(p):
    """A pada without svara marks and daṇḍas."""
    return re.sub(r"[_^|]", "", p).strip()


def norm(s):
    s = re.sub(r"[_^]", "", s.lower())
    # every nasal counts as one: pages differ in writing ṃ or the class nasal
    for a, b in (("ṃ", "n"), ("ṅ", "n"), ("ñ", "n"), ("ṇ", "n"), ("m", "n"), ("ం", "మ"), ("ḥ", ""), ("ః", "")):
        s = s.replace(a, b)
    return re.sub(r"[\s\-|.,;:!?'’()\[\]0-9।॥–—“”‌‍]", "", s)


def read(slug):
    out = {}
    p = WORDS / f"{slug}.txt"
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            n, rest = line.split(None, 1)
            out[int(n)] = [it.split(" = ", 1) for it in rest.split(" | ")]
    return out


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if argv and argv[0] == "--dump":
        vs = verses(argv[1])
        a, b = (int(argv[2]), int(argv[3])) if len(argv) > 3 else (1, len(vs))
        for i, v in enumerate(vs, 1):
            if a <= i <= b:
                print(i, " / ".join(plain(p) for p in v["padas"]))
        return
    slugs = argv or sorted(p.stem for p in DATA.glob("*.py") if not p.stem.startswith("gita-bhashya"))
    tot = have = 0
    for slug in slugs:
        vs, W = verses(slug), read(slug)
        low = []
        for i, v in enumerate(vs, 1):
            if i in W:
                r = difflib.SequenceMatcher(None, norm(" ".join(v["padas"])),
                                            norm(" ".join(w for w, _ in W[i])), autojunk=False).ratio()
                if r < 0.84:
                    low.append((i, round(r, 2)))
        miss = [i for i in range(1, len(vs) + 1) if i not in W]
        extra = [i for i in W if i > len(vs)]
        tot += len(vs)
        have += len(vs) - len(miss)
        print(f"{slug:32} {len(vs) - len(miss):4}/{len(vs):<4}"
              + (f" missing {miss[:6]}{'…' if len(miss) > 6 else ''}" if miss and W else "")
              + (f" EXTRA {extra}" if extra else "") + (f" LOW {low}" if low else ""))
    print(f"total {have}/{tot}")


if __name__ == "__main__":
    main(sys.argv[1:])
