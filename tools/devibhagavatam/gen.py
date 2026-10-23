# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write the Devī Bhāgavatam data files.

Input: adhyayas.json from parse.py, and khemraj.tsv (readings of the 1902 Khemraj
print adopted over the e-text). Output, in tools/stotras/:

  devibhagavatam.py             contents of the whole work
  devibhagavatam-SS.py          a skandha's contents (00 = the māhātmya)
  devibhagavatam-SS-AA.py       one adhyāya a page

Devanāgarī → IAST by the skill's dev2iast. An existing data file is left alone
unless --force is given.  usage: gen.py ADHYAYAS.json [--force] [--only SS …]
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
from dev2iast import dev2iast  # noqa: E402

OUT = TOOLS / "stotras"
# skandhas a Khemraj scan covers (SOURCES §5.27); the rest is the e-text alone
SCANNED = {"0": "all", "1": "all", "2": "all", "3": "all", "4": "1–9", "7": "all",
           "8": "all", "9": "all", "10": "all", "12": "11–14"}
SAMPLED = {"0": "1", "1": "5", "2": "6", "3": "7", "4": "6", "7": "3–4", "8": "8", "9": "8", "10": "7", "12": "12"}
NAME = lambda part: "Māhātmya" if part == "0" else f"Skandha {part}"


def iast(line):
    t = dev2iast(re.sub(r"\s+", " ", line.replace("ॐ", "ओं")).strip())
    t = t.replace("॥", "||").replace("।", "|").replace("ऽ", "'")
    t = re.sub(r"\s*\|\|\s*", " || ", t)
    t = re.sub(r"(?<!\|)\s*\|(?!\|)\s*", " | ", t)
    return re.sub(r"\s+", " ", t).strip(" -–—:")


def loose(s):
    """A regex matching s with any spacing (the e-text's word division varies)."""
    return re.compile(r"\s*".join(re.escape(c) for c in s.replace(" ", "")))


def apply_khemraj(data):
    report = []
    ops = [l.split("\t") for l in (HERE / "khemraj.tsv").read_text(encoding="utf-8").splitlines()
           if l.strip() and not l.startswith("#")]
    for part, ch, n, op, old, new, *where in ops:
        vs = data[part][ch]["verses"]
        i = next((k for k, v in enumerate(vs) if v["n"] == int(n)), None)
        if i is None:
            report.append(f"{part}.{ch}.{n} {op}: verse not found"); continue
        v = vs[i]
        if op == "r":
            rx = loose(old)
            hit = [k for k, l in enumerate(v["lines"]) if rx.search(l)]
            if not hit:
                report.append(f"{part}.{ch}.{n} r: '{old}' not found"); continue
            v["lines"][hit[0]] = rx.sub(new, v["lines"][hit[0]], count=1)
        elif op == "drop":                                  # a contributor's note set as a line
            rx = loose(old)
            keep = [l for l in v["lines"] if not rx.fullmatch(l.strip())]
            if len(keep) == len(v["lines"]):
                report.append(f"{part}.{ch}.{n} drop: '{old}' not found"); continue
            v["lines"] = keep
        elif op == "head":
            rx = loose(old)
            keep = [l for l in v["lines"] if not rx.fullmatch(l.strip(" ।॥"))]
            if len(keep) == len(v["lines"]):
                report.append(f"{part}.{ch}.{n} head: '{old}' not found"); continue
            v["lines"] = keep
            data[part][ch]["head"] = (data[part][ch].get("head", "") + " " + old).strip()
        elif op == "split":
            rx = loose(old)
            k = next((k for k, l in enumerate(v["lines"]) if k and rx.match(l)), None)
            prev = vs[i - 1]["n"] if i else 0
            if k is None or prev != int(n) - 2:
                report.append(f"{part}.{ch}.{n} split: already resolved or no gap"); continue
            first = {"n": int(n) - 1, "lines": v["lines"][:k], "sp": v["sp"]}
            vs[i:i + 1] = [first, {**v, "lines": v["lines"][k:], "sp": []}]
    return report


def verse_secs(v):
    secs = [{"speaker": iast(s)} for s in v["sp"]]
    padas = [iast(l) for l in v["lines"] if iast(l)]
    padas = [p if i == len(padas) - 1 or p.endswith(("|", "-")) else p + " |" for i, p in enumerate(padas)]
    d = {"padas": padas, "num": f"|| {v['n']} ||" if v["n"] else "", "gloss": ""}
    if not v["n"]:
        d["prose"] = True
    return secs + [d]


def footer(part):
    sc = SCANNED.get(part)
    chk = (f"checked against the Khemraj print (Śrī Veṅkaṭeśvara Press, Bombay, 1902) where it disagrees "
           f"with the e-text's numbering, and by sample (adhyāya {SAMPLED[part]})" if sc else
           "this skandha is not in the available scans of the Khemraj print and has not been checked against a print")
    return ("Source: Sanskrit Wikisource — देवीभागवतपुराणम् (public domain), converted to IAST; " + chk +
            "; repairs and readings listed in SOURCES §5.27; translations original")


def q(s):
    return repr(s) if isinstance(s, bool) else json.dumps(s, ensure_ascii=False)


def write(slug, st, force):
    path = OUT / f"{slug}.py"
    if path.exists() and not force:
        return False
    secs = st.pop("sections")
    body = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
            "# Devī Bhāgavatam, Sanskrit Wikisource → IAST (with Khemraj readings); written by",
            "# tools/devibhagavatam/gen.py. See SOURCES §5.27.", "", "STOTRA = {"]
    for k, v in st.items():
        body.append(f"    {q(k)}: {q(v) if not isinstance(v, list) else '[' + ', '.join('(' + ', '.join(q(x) for x in t) + ')' for t in v) + ']'},")
    body.append('    "sections": [')
    body += [f"    {s!r}," for s in secs]
    body += ["    ],", "}", ""]
    path.write_text("\n".join(body), encoding="utf-8", newline="\n")
    return True


def main(argv):
    data = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    force, only = "--force" in argv, set(argv[argv.index("--only") + 1:]) if "--only" in argv else None
    for r in apply_khemraj(data):
        print("khemraj.tsv:", r)
    parts = sorted(data, key=int)
    flat = [(p, int(c)) for p in parts for c in sorted(data[p], key=int)]
    href = lambda p, c: f"devibhagavatam-{int(p):02d}-{c:02d}-iast.html"
    written, top = [], []
    for p in parts:
        chs = sorted(data[p], key=int)
        links = []
        for c in map(int, chs):
            rec = data[p][str(c)]
            n = sum(1 for v in rec["verses"] if v["n"])
            title = iast(rec["head"]) if rec.get("head") else ""
            links.append((f"Adhyāya {c}", href(p, c), (title + " · " if title else "") + f"{n} verses"))
            if only and f"{int(p):02d}" not in only:
                continue
            k = flat.index((p, c))
            nav = ([("‹ previous", href(*flat[k - 1]))] if k else []) + [(f"{NAME(p)} · contents", f"devibhagavatam-{int(p):02d}-iast.html")] \
                + ([("next ›", href(*flat[k + 1]))] if k + 1 < len(flat) else [])
            secs = [{"speaker": title}] if title else []
            for v in rec["verses"]:
                secs += verse_secs(v)
            if rec.get("colophon"):
                secs.append({"colophon": iast(rec["colophon"]).rstrip(" |") + " ||"})
            st = {"deity": "devibhagavatam", "doc_title": f"Devī Bhāgavatam · {NAME(p)} · adhyāya {c}",
                  "app_title": f"Devī Bhāgavatam {p}·{c}", "h1": "Devī Bhāgavatam",
                  "subtitle": f"{NAME(p)} · adhyāya {c}" + (f" of {len(chs)}"),
                  "note": "The Śrīmad Devī Bhāgavata Mahāpurāṇa in Sanskrit, from Sanskrit Wikisource. Translations will follow.",
                  "nav": nav, "footer": footer(p), "sections": secs}
            if write(f"devibhagavatam-{int(p):02d}-{c:02d}", st, force):
                written.append(1)
        nverses = sum(1 for c in chs for v in data[p][c]["verses"] if v["n"])
        top.append((NAME(p), f"devibhagavatam-{int(p):02d}-iast.html", f"{len(chs)} adhyāyas · {nverses:,} verses"
                    + ("" if p in SCANNED else " · not checked against a print")))
        if only and f"{int(p):02d}" not in only:
            continue
        i = parts.index(p)
        nav = ([(f"‹ {NAME(parts[i - 1])}", f"devibhagavatam-{int(parts[i - 1]):02d}-iast.html")] if i else []) + [("all skandhas", "devibhagavatam-iast.html")] \
            + ([(f"{NAME(parts[i + 1])} ›", f"devibhagavatam-{int(parts[i + 1]):02d}-iast.html")] if i + 1 < len(parts) else [])
        st = {"deity": "devibhagavatam", "doc_title": f"Devī Bhāgavatam · {NAME(p)}", "app_title": f"Devī Bhāgavatam {p}",
              "h1": "Devī Bhāgavatam", "subtitle": f"{NAME(p)} · contents · {len(chs)} adhyāyas",
              "note": "The Śrīmad Devī Bhāgavata Mahāpurāṇa in Sanskrit, from Sanskrit Wikisource. Translations will follow.",
              "nav": nav, "footer": footer(p), "sections": [{"links": links}]}
        if write(f"devibhagavatam-{int(p):02d}", st, force):
            written.append(1)
    if not only:
        st = {"deity": "devibhagavatam", "doc_title": "Devī Bhāgavatam", "app_title": "Devī Bhāgavatam",
              "h1": "Devī Bhāgavatam", "subtitle": "Śrīmad Devī Bhāgavata Mahāpurāṇa · the māhātmya and twelve skandhas",
              "note": "The Śrīmad Devī Bhāgavata Mahāpurāṇa in Sanskrit, from Sanskrit Wikisource, with readings "
                      "checked against the 1902 Khemraj print where its scans reach. Translations will follow.",
              "footer": ("Source: Sanskrit Wikisource — देवीभागवतपुराणम् (public domain), converted to IAST; numbering slips "
                         "and a sample of readings checked against the Khemraj print (Śrī Veṅkaṭeśvara Press, Bombay, "
                         "1902) where its scans reach; repairs and readings listed in SOURCES §5.27; translations original"),
              "sections": [{"links": top}]}
        if write("devibhagavatam", st, force):
            written.append(1)
    print(len(written), "data files written")


if __name__ == "__main__":
    main(sys.argv[1:])
