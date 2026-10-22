# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write the Vālmīki Rāmāyaṇa data files from the parsed Wikisource text.

Input is sargas.json from parse.py. Output, in tools/stotras/:

  ramayana.py              the whole work: links to each kāṇḍa's contents
  ramayana-<K>.py          a kāṇḍa's contents (K = 1 … 7)
  ramayana-<K>-<NN>.py     the verses, whole sargas, up to MAX verses a page

Each line is converted Devanāgarī → IAST by the skill's dev2iast (daṇḍas as
| and ||); an interpolated sarga printed inside a page (Araṇya 56A) gets its
own heading. Sargas listed in HOLD are left out (see SOURCES §5.25). An
existing data file is left alone unless --force is given.

usage: gen.py SARGAS.json [--force] [--only K …]
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
from dev2iast import dev2iast  # noqa: E402

MAX = 150
OUT = TOOLS / "stotras"
KANDAS = [("बालकाण्डम्", "1", "Bālakāṇḍa"), ("अयोध्याकाण्डम्", "2", "Ayodhyākāṇḍa"),
          ("अरण्यकाण्डम्", "3", "Araṇyakāṇḍa"), ("किष्किन्धाकाण्डम्", "4", "Kiṣkindhākāṇḍa"),
          ("सुन्दरकाण्डम्", "5", "Sundarakāṇḍa"), ("युद्धकाण्डम्", "6", "Yuddhakāṇḍa"),
          ("उत्तरकाण्डम्", "7", "Uttarakāṇḍa")]
# typed on Wikisource as a word-split reading aid, not as the received text:
# held until they are re-keyed from a print (SOURCES §5.25)
HOLD = {"2": set(range(48, 89)), "3": {14, 15}}
NOTE = ("Vālmīki's Rāmāyaṇa in the vulgate text, from Sanskrit Wikisource. "
        "Verse numbers are the e-text's, sarga by sarga. Translations will follow.")
FOOTER = ("Source: Sanskrit Wikisource — वाल्मीकिरामायणम् (vulgate text; public "
          "domain), converted to IAST; repairs to the e-text's numbering are listed "
          "in SOURCES §5.25; translations original")


def iast(line):
    line = re.sub(r"\s+", " ", line).strip()
    t = dev2iast(line.replace("ॐ", "ओं")).replace("॥", "||").replace("।", "|").replace("ऽ", "'")
    t = re.sub(r"\s*\|\|\s*", " || ", t)
    t = re.sub(r"(?<!\|)\s*\|(?!\|)\s*", " | ", t)
    return t.strip()


def verse(n, lines):
    padas = [iast(l) for l in lines]
    # a line ending in "-" runs on into the next (a word split across lines): no daṇḍa
    padas = [p if i == len(padas) - 1 or p.endswith(("|", "-")) else p + " |" for i, p in enumerate(padas)]
    return {"padas": padas, "num": f"|| {n} ||", "gloss": ""}


def colophon(text):
    t = iast(re.sub(r"(?:॥|।।)\s*[०-९0-9.\-\s]*(?:॥|।।)?\s*$", "", text))
    return t.rstrip(" |") + " ||" if t else ""


def q(s):
    return repr(s) if isinstance(s, bool) else json.dumps(s, ensure_ascii=False)


def write(slug, st, force):
    path = OUT / f"{slug}.py"
    if path.exists() and not force:
        return False
    secs = st.pop("sections")
    body = ["# -*- coding: utf-8 -*-",
            "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
            "# Vālmīki Rāmāyaṇa (vulgate), Sanskrit Wikisource → IAST; written by",
            "# tools/ramayana/gen.py, now edited by hand. See SOURCES §5.25.",
            "",
            "def _v(padas, num, gloss=\"\"):",
            "    return {\"padas\": padas, \"num\": num, \"gloss\": gloss}",
            "",
            "",
            "STOTRA = {"]
    for k, v in st.items():
        body.append(f"    {q(k)}: {q(v) if not isinstance(v, list) else '[' + ', '.join('(' + ', '.join(q(x) for x in t) + ')' for t in v) + ']'},")
    body.append('    "sections": [')
    for s in secs:
        if "padas" in s:
            body.append("    _v([" + ",\n        ".join(q(p) for p in s["padas"]) + f"], {q(s['num'])}),")
        elif "links" in s:
            body.append('    {"links": [')
            body += [f"        ({q(a)}, {q(b)}, {q(c)})," for a, b, c in s["links"]]
            body.append("    ]},")
        else:
            body.append(f"    {q(s)},")
    body += ["    ],", "}", ""]
    path.write_text("\n".join(body), encoding="utf-8", newline="\n")
    return True


def sarga_sections(no, rec):
    secs = [{"heading": f"Sarga {no}"}]
    secs += [verse(n, ls) for n, ls in rec["verses"]]
    for p in rec.get("parts", []):
        label = re.match(r"([०-९0-9]+)\s*(\S*)", p["label"])
        tag = label.group(1).translate(str.maketrans("०१२३४५६७८९", "0123456789")) + ("A" if label.group(2).startswith("अ") else "")
        secs.append({"heading": f"Sarga {tag} · interpolated (prakṣipta)"})
        secs += [verse(n, ls) for n, ls in p["verses"]]
    if rec.get("colophon"):
        secs.append({"colophon": colophon(rec["colophon"])})
    return secs


def main(argv):
    if not argv:
        sys.exit(__doc__)
    data = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    force = "--force" in argv
    only = set(argv[argv.index("--only") + 1:]) if "--only" in argv else None
    plan = []
    for dev, code, name in KANDAS:
        sargas = sorted((int(s), r) for s, r in data[dev].items() if int(s) not in HOLD.get(code, ()))
        pages, cur, n = [], [], 0
        for no, rec in sargas:
            size = len(rec["verses"]) + sum(len(p["verses"]) for p in rec.get("parts", []))
            if cur and (n + size > MAX or no != cur[-1][0] + 1):   # a held gap starts a new page
                pages.append(cur); cur, n = [], 0
            cur.append((no, rec)); n += size
        if cur:
            pages.append(cur)
        plan.append(((dev, code, name), pages))
    flat = [(row, i) for row, pages in plan for i in range(len(pages))]
    href = lambda row, i: f"ramayana-{row[1]}-{i + 1:02d}-iast.html"
    rng = lambda page: f"{page[0][0]}" + (f"–{page[-1][0]}" if len(page) > 1 else "")
    written = []
    for pi, (row, pages) in enumerate(plan):
        dev, code, name = row
        links = []
        for i, page in enumerate(pages):
            nv = sum(len(r["verses"]) + sum(len(p["verses"]) for p in r.get("parts", [])) for _, r in page)
            links.append((f"{i + 1} · sarga{'s' if len(page) > 1 else ''} {rng(page)}", href(row, i), f"{nv} verses"))
            if only and code not in only:
                continue
            k = flat.index((row, i))
            nav = []
            if k:
                nav.append(("‹ previous", href(*flat[k - 1])))
            nav.append((f"{name} · contents", f"ramayana-{code}-iast.html"))
            if k + 1 < len(flat):
                nav.append(("next ›", href(*flat[k + 1])))
            secs = [s for no, rec in page for s in sarga_sections(no, rec)]
            st = {"deity": "ramayana",
                  "doc_title": f"Vālmīki Rāmāyaṇa · {name} · sarga{'s' if len(page) > 1 else ''} {rng(page)}",
                  "app_title": f"Rāmāyaṇa {code}·{rng(page)}",
                  "h1": "Vālmīki Rāmāyaṇa",
                  "subtitle": f"{name} · sarga{'s' if len(page) > 1 else ''} {rng(page)}",
                  "note": NOTE, "toc": True, "nav": nav, "footer": FOOTER, "sections": secs}
            if write(f"ramayana-{code}-{i + 1:02d}", st, force):
                written.append(f"ramayana-{code}-{i + 1:02d}")
        if only and code not in only:
            continue
        nav = []
        if pi:
            nav.append((f"‹ {plan[pi - 1][0][2]}", f"ramayana-{plan[pi - 1][0][1]}-iast.html"))
        nav.append(("all kāṇḍas", "ramayana-iast.html"))
        if pi + 1 < len(plan):
            nav.append((f"{plan[pi + 1][0][2]} ›", f"ramayana-{plan[pi + 1][0][1]}-iast.html"))
        held = sorted(HOLD.get(code, ()))
        nsarga = sum(len(p) for p in pages)
        st = {"deity": "ramayana", "doc_title": f"Vālmīki Rāmāyaṇa · {name}",
              "app_title": f"Rāmāyaṇa {code}", "h1": "Vālmīki Rāmāyaṇa",
              "subtitle": f"{name} · contents · {nsarga} sargas in {len(pages)} pages",
              "note": NOTE + (f" Sargas {held[0]}–{held[-1]} are not yet included: the e-text gives "
                              "them as a word-split reading aid, and they are being re-keyed "
                              "from a printed edition." if held else ""),
              "nav": nav, "footer": FOOTER, "sections": [{"links": links}]}
        if write(f"ramayana-{code}", st, force):
            written.append(f"ramayana-{code}")
    if not only:
        top = [(row[2], f"ramayana-{row[1]}-iast.html",
                f"{sum(len(p) for p in pages)} sargas · {len(pages)} page{'s' if len(pages) > 1 else ''}")
               for row, pages in plan]
        st = {"deity": "ramayana", "doc_title": "Vālmīki Rāmāyaṇa", "app_title": "Vālmīki Rāmāyaṇa",
              "h1": "Vālmīki Rāmāyaṇa", "subtitle": "the seven kāṇḍas",
              "note": NOTE, "footer": FOOTER, "sections": [{"links": top}]}
        if write("ramayana", st, force):
            written.append("ramayana")
    print(f"{len(written)} data files written; {len(flat)} verse pages in all")
    for row, pages in plan:
        print(f"  {row[2]}: {len(pages)} pages")
    return written


if __name__ == "__main__":
    main(sys.argv[1:])
