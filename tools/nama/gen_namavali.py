# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/<slug>.py for an aṣṭottaraśatanāmāvali from tools/nama/<name>.names.txt
(one name per line, in the dative as in the nāmāvali:  नाम | English meaning).  The names are set nine to a verse-block
as 'oṃ … namaḥ' lines, with the meanings in the translation fold.   usage: gen_namavali.py NAME|all"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
import dev2iast as D  # noqa: E402
NOTE = ("The {n} names of {who}, each as ‘{fmt}’, nine to a block, with the meaning of each name in the fold below. "
        "The text is that of the Tirumala Tirupati Devasthanams publication ‘Vividha Devatā Aṣṭottara Śata-Sahasranāmāvali’ (1st ed. 2012), {pp}; "
        "I have kept its readings, including a few that look like slips, and listed those in SOURCES §12.2.")
TTD = "Text: Tirumala Tirupati Devasthanams, Vividha Devatā Aṣṭottara Śata-Sahasranāmāvali (1st ed. 2012), {pp}; English meanings original; editorial notes in SOURCES §12.2"
META = {
 "ganesha108": dict(slug="ganesha-ashtottara-shatanamavali", deity="ganesha", t="Gaṇeśa Aṣṭottaraśatanāmāvaliḥ", app="Gaṇeśa 108 Names", who="Gaṇeśa", sub="The 108 Names of Gaṇeśa", pp="pp. 1–2"),
 "shiva108": dict(slug="shiva-ashtottara-shatanamavali", deity="shiva", t="Śiva Aṣṭottaraśatanāmāvaliḥ", app="Śiva 108 Names", who="Śiva", sub="The 108 Names of Śiva", pp="pp. 39–41"),
 "lakshmi108": dict(slug="lakshmi-ashtottara-shatanamavali", deity="devi", t="Lakṣmī Aṣṭottaraśatanāmāvaliḥ", app="Lakṣmī 108 Names", who="Lakṣmī", sub="The 108 Names of Lakṣmī", pp="pp. 36–38"),
 "krishna108": dict(slug="krishna-ashtottara-shatanamavali", deity="vishnu", t="Kṛṣṇa Aṣṭottaraśatanāmāvaliḥ", app="Kṛṣṇa 108 Names", who="Kṛṣṇa", sub="The 108 Names of Kṛṣṇa", pp="pp. 33–35"),
 "anjaneya108": dict(slug="anjaneya-ashtottara-shatanamavali", deity="hanuman", t="Āñjaneya Aṣṭottaraśatanāmāvaliḥ", app="Āñjaneya 108 Names", who="Āñjaneya (Hanumān)", sub="The 108 Names of Āñjaneya", pp="pp. 52–54"),
 "venkatesha108": dict(slug="venkateshwara-ashtottara-shatanamavali", deity="venkateshwara", t="Veṅkaṭeśa Aṣṭottaraśatanāmāvaliḥ", app="Veṅkaṭeśa 108 Names", who="Veṅkaṭeśa", sub="The 108 Names of Śrī Veṅkaṭeśvara", pp="pp. 24–28"),
 "lalita108": dict(slug="lalita-ashtottara-shatanamavali", deity="devi", t="Lalitā Aṣṭottaraśatanāmāvaliḥ", app="Lalitā 108 Names", who="Lalitā", sub="The 108 Names of Lalitā", pp="pp. 42–46", fmt="lalita"),
 "subrahmanya108n": dict(slug="subrahmanya-ashtottara-shatanamavali", deity="subrahmanya", t="Subrahmaṇya Aṣṭottaraśatanāmāvaliḥ", app="Subrahmaṇya 108 Names (nāmāvali)", who="Subrahmaṇya", sub="The 108 Names of Subrahmaṇya, as a nāmāvali", pp="pp. 47–48"),
}
def iast(line): return re.sub(r"\s+", " ", D.dev2iast(line.replace("ॐ", "oṃ ").replace("ऽ", "'")).replace("॥", "||").replace("।", "|")).strip()
def main(name):
    m = META[name]
    rows = [l.split("|", 1) for l in (HERE / f"{name}.names.txt").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    rows = [(a.strip(), b.strip()) for a, b in rows]
    secs = []
    for i in range(0, len(rows), 9):
        ch = rows[i:i + 9]
        padas = [(f"{iast(n)} namo namaḥ" if m.get("fmt") == "lalita" else f"oṃ {iast(n)} namaḥ") for n, _ in ch]
        gloss = " ".join(f"{i + j + 1}. {mean[0].upper() + mean[1:]}." for j, (_, mean) in enumerate(ch))
        secs.append({"padas": padas, "num": f"|| {i + 1}–{i + len(ch)} ||", "gloss": gloss})
    st = {"deity": m["deity"], "doc_title": m["t"], "app_title": m["app"], "h1": m["t"], "subtitle": m["sub"], "note": NOTE.format(n=len(rows), who=m["who"], pp=m["pp"], fmt=("… namo namaḥ" if m.get("fmt") == "lalita" else "oṃ … namaḥ")) + (" Each name is preceded in the print by ‘oṃ aiṃ hrīṃ śrīṃ’." if m.get("fmt") == "lalita" else ""),
          "footer": TTD.format(pp=m["pp"]),
          "sections": secs}
    q = lambda v: json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           f"# {m['t']}; written by tools/nama/gen_namavali.py from tools/nama/{name}.names.txt. See SOURCES §12.2.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / f"{m['slug']}.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{m['slug']}: {len(rows)} names" + ("" if len(rows) == 108 else f"  *** {len(rows)}, NOT 108 ***"))
if __name__ == "__main__":
    for n in (list(META) if sys.argv[1] == "all" else sys.argv[1:]): main(n)
