# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write the Pōtana Bhāgavatam data files from the extracted text.

Input is items.json from extract.py (Pōtana's verses and the edition's
section titles, in book order) and headings.tsv (our English heading for
each section). Output is one data file per page in tools/stotras/:

  bhagavatam.py              the whole work: links to each part's contents
  bhagavatam-<P>.py          a part's contents (P = 01 … 12, 05a/05b, 10a/10b)
  bhagavatam-<P>-<NN>.py     the verses, a few story sections to a page

Pages hold whole sections, up to MAX units; a longer section is split evenly,
its later pieces headed "(continued)". The Rukmiṇī Kalyāṇam translations and
word lists, and the Gajendra Mokṣam translations, are carried over from those
pages. The data files are the source of truth once written: an existing file
is left alone unless --force is given.

usage: gen.py ITEMS.json [--force] [--only P …]
"""
import difflib, json, math, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS))
import build_stotra  # noqa: E402

MAX = 120
OUT = TOOLS / "stotras"
LABEL = re.compile(r"^([ఀ-౿]{1,7})\.\s*")
PROSE = {"వ", "గద్య", "గద్యము", "గ"}
GENERIC = re.compile(r"^(శ్రీ\s*మహాభాగవతము|.*స్కంధము.*|పద్యగద్యసూచి)$")

# part → (code, name, TTD volume, series no., editor)
PARTS = [
    ("1", "01", "Skandha 1", "I", "1237", "Vidwan Mudivarthi Kondamacharyulu"),
    ("2", "02", "Skandha 2", "I", "1237", "Vidwan Mudivarthi Kondamacharyulu"),
    ("3", "03", "Skandha 3", "II", "1238", "Vidwan Mudivarthi Kondamacharyulu"),
    ("4", "04", "Skandha 4", "III", "1239", "Dr. Samudrala Lakshmanaiah"),
    ("5.1", "05a", "Skandha 5 · first āśvāsa", "III", "1239", "Dr. Samudrala Lakshmanaiah"),
    ("5.2", "05b", "Skandha 5 · second āśvāsa", "III", "1239", "Dr. Samudrala Lakshmanaiah"),
    ("6", "06", "Skandha 6", "IV", "1240", "Dr. Samudrala Lakshmanaiah"),
    ("7", "07", "Skandha 7", "IV", "1240", "Dr. Samudrala Lakshmanaiah"),
    ("8", "08", "Skandha 8", "V", "1241", "Dr. Samudrala Lakshmanaiah"),
    ("9", "09", "Skandha 9", "V", "1241", "Dr. Samudrala Lakshmanaiah"),
    ("10.1", "10a", "Skandha 10 · first part", "VI", "1242", "Dr. Samudrala Lakshmanaiah"),
    ("10.2", "10b", "Skandha 10 · second part", "VII", "1243", "Dr. Samudrala Lakshmanaiah"),
    ("11", "11", "Skandha 11", "VIII", "1244", "Dr. Samudrala Lakshmanaiah"),
    ("12", "12", "Skandha 12", "VIII", "1244", "Dr. Samudrala Lakshmanaiah"),
]
ROMAN_SK = {"I": "1 & 2", "II": "3", "III": "4 & 5", "IV": "6 & 7", "V": "8 & 9",
            "VI": "10-1", "VII": "10-2", "VIII": "11 & 12"}
NOTE = ("Bammera Pōtana's Telugu Bhāgavatam as printed by Tirumala Tirupati "
        "Devasthanams. The Telugu is the source; the IAST is a reading aid. "
        "Each verse keeps the book's metre label (క. kandam, సీ. sīsam, వ. "
        "vacanam …) and line breaks. Translations will follow.")


def footer(vol, series, editor):
    return (f"Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, "
            f"Vol. {vol} (Skandha {ROMAN_SK[vol]}), ed. {editor}, T.T.D. Religious "
            f"Publications Series No. {series}, Tirumala Tirupati Devasthanams, "
            "Tirupati, first edition 2017 — Pōtana's verses only (public domain); "
            "the edition's commentary is not reproduced; section headings and "
            "translations original")


def load_headings():
    h = {}
    for line in (HERE / "headings.tsv").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            part, first, text = line.split("\t")
            h[(part, int(first))] = text
    return h


def sections(items, part):
    """The part's story sections: [{"first": n, "units": […]}], generic titles
    dropped, a title with no verses folded into the next."""
    out, titled = [], False
    for it in items:
        if it["sk"] != part:
            continue
        if "head" in it:
            titled = titled or not GENERIC.match(it["head"])
            continue
        if titled or not out:
            out.append({"units": []}); titled = False
        out[-1]["units"].append(it)
    for s in out:
        s["first"] = s["units"][0]["num"]
    return out


def paginate(secs, heads, part):
    """Group sections into pages of at most MAX units (a long one split)."""
    pieces = []
    for s in secs:
        title = heads[(part, s["first"])]
        k = math.ceil(len(s["units"]) / MAX)
        size = math.ceil(len(s["units"]) / k)
        for i in range(k):
            pieces.append((title + (" (continued)" if i else ""), s["units"][i * size:(i + 1) * size]))
    pages, cur, n = [], [], 0
    for title, units in pieces:
        if cur and n + len(units) > MAX:
            pages.append(cur); cur, n = [], 0
        cur.append((title, units)); n += len(units)
    if cur:
        pages.append(cur)
    # a short tail page joins the one before it rather than stand alone
    if len(pages) > 1 and n < 25 and sum(len(u) for _, u in pages[-2]) + n <= MAX + 25:
        tail = pages.pop()
        pages[-1] += tail
    return pages


def carried():
    """Translations (and word lists) from the highlight pages, by (part, num)."""
    out = {}
    st = build_stotra.load_data("rukmini-kalyanam")
    for s in st["sections"]:
        if isinstance(s, dict) and "padas" in s:
            n = int(re.sub(r"\D", "", s["num"]))
            gloss = re.sub(r"^\[[^\]]+\]\s*", "", s["gloss"])   # metre is in the text now
            out[("10.1", n)] = {"gloss": gloss, "words": s.get("words")}
    return out


def gajendra(items):
    """Gajendra Mokṣam's verses carry no numbers; match them to skandha 8 by text."""
    out = {}
    st = build_stotra.load_data("gajendra-moksham")
    norm = lambda ls: re.sub(r"[^ఀ-౿]", "", LABEL.sub("", " ".join(ls)))
    eight = [it for it in items if it["sk"] == "8" and "num" in it]
    for s in st["sections"]:
        if not (isinstance(s, dict) and "padas" in s):
            continue
        a = norm(s["padas"])
        r, it = max((difflib.SequenceMatcher(None, a, norm(it["lines"]), autojunk=False).ratio(), it)
                    for it in eight if abs(len(norm(it["lines"])) - len(a)) < len(a) * 0.3)
        if r > 0.8:
            out[("8", it["num"])] = {"gloss": s["gloss"]}
    return out


def verse(it, extra):
    lines = list(it["lines"])
    m = LABEL.match(lines[0])
    if m:
        lines[0] = f"{m.group(1)}. " + lines[0][m.end():]   # "క.ఆ …" → "క. ఆ …"
    label = m.group(1) if m else lines[0].strip(" .")
    v = {"padas": lines, "num": f"॥ {it['num']} ॥" if "num" in it else "", "gloss": ""}
    if label in PROSE:
        v["prose"] = True
    e = extra.get((it["sk"], it.get("num")))
    if e:
        v["gloss"] = e["gloss"]
        if e.get("words"):
            v["words"] = e["words"]
    return v


def q(s):
    # a Python literal: JSON quoting suits str/list/dict, but not True/False
    return repr(s) if isinstance(s, bool) else json.dumps(s, ensure_ascii=False)


def write(slug, st, force):
    path = OUT / f"{slug}.py"
    if path.exists() and not force:
        return False
    secs = st.pop("sections")
    body = ["# -*- coding: utf-8 -*-",
            "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
            "# Telugu-LANGUAGE work (src=\"tel\"). Pōtana's Telugu Bhāgavatam, TTD edition;",
            "# written by tools/bhagavatam/gen.py, now edited by hand. See SOURCES §6.12.",
            "",
            "def _v(lines, num, prose=False, gloss=\"\", words=None):",
            "    v = {\"padas\": lines, \"num\": num, \"gloss\": gloss}",
            "    if prose:",
            "        v[\"prose\"] = True",
            "    if words:",
            "        v[\"words\"] = words",
            "    return v",
            "",
            "",
            "STOTRA = {"]
    for k, v in st.items():
        body.append(f"    {q(k)}: {q(v) if not isinstance(v, list) else '[' + ', '.join('(' + ', '.join(q(x) for x in t) + ')' for t in v) + ']'},")
    body.append('    "sections": [')
    for s in secs:
        if "padas" in s:
            args = ["[" + ",\n        ".join(q(p) for p in s["padas"]) + "]", q(s["num"])]
            if s.get("prose"):
                args.append("prose=True")
            if s["gloss"]:
                args.append("gloss=" + q(s["gloss"]))
            if s.get("words"):
                args.append("words=" + q(s["words"]))
            body.append("    _v(" + ", ".join(args) + "),")
        elif "links" in s:
            body.append('    {"links": [')
            body += [f"        ({q(a)}, {q(b)}, {q(c)})," for a, b, c in s["links"]]
            body.append("    ]},")
        else:
            body.append(f"    {q(s)},")
    body += ["    ],", "}", ""]
    path.write_text("\n".join(body), encoding="utf-8", newline="\n")
    return True


def main(argv):
    if not argv:
        sys.exit(__doc__)
    items = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    force = "--force" in argv
    only = set(argv[argv.index("--only") + 1:]) if "--only" in argv else None
    heads, extra = load_headings(), {**carried(), **gajendra(items)}
    plan = []                                     # (part row, pages)
    for row in PARTS:
        secs = sections(items, row[0])
        missing = [s["first"] for s in secs if (row[0], s["first"]) not in heads]
        if missing:
            sys.exit(f"headings.tsv: no heading for part {row[0]} at {missing}")
        plan.append((row, paginate(secs, heads, row[0])))
    flat = [(row, i) for row, pages in plan for i in range(len(pages))]
    href = lambda row, i: f"bhagavatam-{row[1]}-{i + 1:02d}-iast.html"
    written = []
    for pi, (row, pages) in enumerate(plan):
        part, code, name, vol, series, editor = row
        foot = footer(vol, series, editor)
        links = []
        for i, page in enumerate(pages):
            units = [u for _, us in page for u in us]
            nums = [u["num"] for u in units if "num" in u]
            links.append((f"{i + 1} · verses {nums[0]}–{nums[-1]}", href(row, i),
                          " · ".join(t for t, _ in page if not t.endswith("(continued)")) or page[0][0]))
            if only and code not in only:
                continue
            k = flat.index((row, i))
            nav = []
            if k:
                nav.append(("‹ previous", href(*flat[k - 1])))
            nav.append((f"{name} · contents", f"bhagavatam-{code}-iast.html"))
            if k + 1 < len(flat):
                nav.append(("next ›", href(*flat[k + 1])))
            secs = []
            for title, us in page:
                secs.append({"heading": title})
                secs += [verse(u, extra) for u in us]
            st = {"src": "tel", "deity": "bhagavatam",
                  "doc_title": f"Pōtana Bhāgavatam · {name} · {i + 1}",
                  "app_title": f"Bhāgavatam {part}·{i + 1}",
                  "h1": "Pōtana Bhāgavatam",
                  "subtitle": f"{name} · {i + 1} of {len(pages)} · verses {nums[0]}–{nums[-1]}",
                  "note": NOTE, "toc": True, "nav": nav, "footer": foot, "sections": secs}
            if write(f"bhagavatam-{code}-{i + 1:02d}", st, force):
                written.append(f"bhagavatam-{code}-{i + 1:02d}")
        if only and code not in only:
            continue
        nav = []
        if pi:
            nav.append((f"‹ {plan[pi - 1][0][2]}", f"bhagavatam-{plan[pi - 1][0][1]}-iast.html"))
        nav.append(("all parts", "bhagavatam-iast.html"))
        if pi + 1 < len(plan):
            nav.append((f"{plan[pi + 1][0][2]} ›", f"bhagavatam-{plan[pi + 1][0][1]}-iast.html"))
        n_units = sum(len(us) for page in pages for _, us in page)
        st = {"src": "tel", "deity": "bhagavatam",
              "doc_title": f"Pōtana Bhāgavatam · {name}",
              "app_title": f"Bhāgavatam {part}",
              "h1": "Pōtana Bhāgavatam",
              "subtitle": f"{name} · contents · {n_units} verses in {len(pages)} pages",
              "note": NOTE, "nav": nav, "footer": foot, "sections": [{"links": links}]}
        if write(f"bhagavatam-{code}", st, force):
            written.append(f"bhagavatam-{code}")
    # the whole work
    top = []
    for row, pages in plan:
        n_units = sum(len(us) for page in pages for _, us in page)
        top.append((row[2], f"bhagavatam-{row[1]}-iast.html",
                    f"{n_units:,} verses · {len(pages)} page{'s' if len(pages) > 1 else ''}"))
    st = {"src": "tel", "deity": "bhagavatam",
          "doc_title": "Pōtana Bhāgavatam", "app_title": "Pōtana Bhāgavatam",
          "h1": "Pōtana Bhāgavatam",
          "subtitle": "Śrī Mahābhāgavatamu · the twelve skandhas in Telugu",
          "note": NOTE + " Two episodes also have pages of their own, with "
                  "translations: Gajendra Mokṣam and Rukmiṇī Kalyāṇam.",
          "nav": [("Gajendra Mokṣam", "../vishnu/gajendra-moksham-iast.html"),
                  ("Rukmiṇī Kalyāṇam", "../vishnu/rukmini-kalyanam-iast.html")],
          "footer": "Source: Bammera Pōtanāmātya, Śrī Mahābhāgavatamu with Commentary, "
                    "Vols. I–VIII, T.T.D. Religious Publications Series Nos. 1237–1244, "
                    "Tirumala Tirupati Devasthanams, Tirupati, first edition 2017 — "
                    "Pōtana's verses only (public domain); the edition's commentary is "
                    "not reproduced; section headings and translations original",
          "sections": [{"links": top}]}
    if not only and write("bhagavatam", st, force):
        written.append("bhagavatam")
    print(f"{len(written)} data files written; {len(flat)} verse pages in all")
    for row, pages in plan:
        print(f"  {row[0]:>5}: {len(pages)} pages, sizes "
              + ", ".join(str(sum(len(us) for _, us in p)) for p in pages))
    return written


if __name__ == "__main__":
    main(sys.argv[1:])
