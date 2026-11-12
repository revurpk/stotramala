# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/nirukta.py, the contents page of Yāska's Nirukta: the Nighaṇṭu it
comments on, then the twelve adhyāyas and the pariśiṣṭa, each with its subtitle.  usage: gen_contents.py"""
import importlib.util, json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent


def subtitle(slug):
    spec = importlib.util.spec_from_file_location("m", TOOLS / "stotras" / f"{slug}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.STOTRA["subtitle"]


def main():
    links = [("Nighaṇṭu", "nighantu-iast.html",
              "The Vedic word-lists on which Yāska’s Nirukta is a commentary: five adhyāyas, 78 khaṇḍas")]
    for n in range(1, 14):
        if (TOOLS / "stotras" / f"nirukta-{n}.py").exists():
            sub = subtitle(f"nirukta-{n}").replace("Yāska's Nirukta, ", "")
            links.append(("Pariśiṣṭa" if n == 13 else f"Adhyāya {n}", f"nirukta-{n}-iast.html", sub))
    st = {"deity": "veda", "doc_title": "Nirukta", "app_title": "Nirukta", "h1": "Nirukta",
          "subtitle": "Yāska’s commentary on the Nighaṇṭu · twelve adhyāyas and the pariśiṣṭa",
          "note": ("The oldest surviving treatise on Vedic etymology. The text is Lakshman Sarup’s critical "
                   "edition (1927); each khaṇḍa has an English heading and summary."),
          "footer": ("Source: Lakshman Sarup, The Nighaṇṭu and the Nirukta: Sanskrit text (University of the "
                     "Panjab, 1927; public domain); editorial notes in SOURCES §5.30–5.31"),
          "sections": [{"links": links}]}
    q = lambda v: repr(v) if isinstance(v, bool) else json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           "# Contents of the Nirukta; written by tools/nirukta/gen_contents.py.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in st["sections"]] + ["    ],", "}", ""]
    (TOOLS / "stotras" / "nirukta.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"nirukta contents: {len(links)} entries")


if __name__ == "__main__":
    main()
