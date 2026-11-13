# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/dhatu-NN.py (Learn pages: the Dhātupāṭha) from tools/dhatu/partNN.txt, and
tools/stotras/dhatu.py, the contents page.  Same line format as tools/perry/gen_perry.py
(## heading, ¶ prose, V word | English | Telugu, "%" subtitle, "!" note for SOURCES).
usage: gen_dhatu.py NN      (one part)      gen_dhatu.py contents"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
NOTE = ("The Dhātupāṭha, the list of verbal roots that goes under Pāṇini’s name, in the form Westergaard "
        "edited it and Böhtlingk reprinted it (1887). Sanskrit follows the script switch above, so the list "
        "reads in Devanāgarī, Telugu or IAST. Each entry gives the root’s number, the root, and its meaning "
        "as the Dhātupāṭha states it; the English and Telugu after the dash are the editor’s.")
FOOTER = ("Source: Otto Böhtlingk, Pāṇini’s Grammatik (Leipzig, 1887; public domain), “Der Dhātupāṭha nach "
          "N. L. Westergaard”, read off the scan on archive.org; editorial notes in SOURCES §8.2; English and "
          "Telugu glosses original")
q = lambda v: repr(v) if isinstance(v, bool) else json.dumps(v, ensure_ascii=False)


def write(slug, st, comment):
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)", comment, "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in st["sections"]] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"{slug}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")


def part(nn):
    src = (HERE / f"part{nn:02d}.txt").read_text(encoding="utf-8").splitlines()
    secs, vocab = [], None
    sub = next(x.strip()[1:].strip() for x in src if x.strip().startswith("%"))
    for raw in src:
        l = raw.strip()
        if not l or l[0] in "%!#@":
            if not l.startswith("##"):
                continue
        kind = "##" if l.startswith("##") else l[0]
        if kind != "V" and vocab is not None:
            secs.append({"vocab": vocab}); vocab = None
        if kind == "##":
            secs.append({"heading": l[2:].strip()})
        elif kind == "¶":
            secs.append({"para": l[1:].strip()})
        elif kind == "V":
            f = [x.strip() for x in l[1:].split("|")]
            if len(f) != 3:
                sys.exit(f"expected 3 fields: {l[:70]}")
            vocab = (vocab or []) + [f]
        else:
            sys.exit(f"unparsed: {l[:70]}")
    if vocab is not None:
        secs.append({"vocab": vocab})
    st = {"deity": "learn", "doc_title": f"Dhātupāṭha · {sub.split(':')[0]}", "app_title": f"Dhātupāṭha {nn}",
          "h1": "Dhātupāṭha", "subtitle": sub, "note": NOTE, "footer": FOOTER, "toc": False, "sections": secs}
    write(f"dhatu-{nn:02d}", st, f"# Dhātupāṭha, part {nn} (tools/dhatu/part{nn:02d}.txt); written by tools/dhatu/gen_dhatu.py. See SOURCES §8.2.")
    print(f"dhatu-{nn:02d}: {len(secs)} sections")


def contents():
    links = []
    for f in sorted(HERE.glob("part[0-9][0-9].txt")):
        nn = int(f.stem[4:])
        m = re.search(r"^%\s*(.+)$", f.read_text(encoding="utf-8"), re.M)
        links.append((f"Part {nn}", f"dhatu-{nn:02d}-iast.html", m.group(1).strip()))
    st = {"deity": "learn", "doc_title": "The Dhātupāṭha", "app_title": "Dhātupāṭha", "h1": "The Dhātupāṭha",
          "subtitle": "Pāṇini’s list of verbal roots, in ten classes, with meanings in Sanskrit, English and Telugu",
          "note": NOTE, "footer": FOOTER,
          "sections": [{"rubric": "The ten classes in order, in parts of about a hundred and fifty roots."}, {"links": links}]}
    write("dhatu", st, "# Contents of the Dhātupāṭha pages; written by tools/dhatu/gen_dhatu.py.")
    print(f"dhatu contents: {len(links)} parts")


if __name__ == "__main__":
    a = sys.argv[1]
    contents() if a == "contents" else part(int(a))
