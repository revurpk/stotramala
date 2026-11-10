# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Write tools/stotras/nighantu.py from the transcription tools/nirukta/nighantu.txt.

nighantu.txt: one khaṇḍa a line (closing ॥ N ॥); "# N" opens adhyāya N; "= …" is a
closing line in Sanskrit (a colophon); "+ …" an editorial note in English, optionally
followed by ": [ Sanskrit ]" (the summary verse some manuscripts add), set as a rubric
and a small passage; "@N" records the leaf; other "#" lines are comments.
The English glosses are original (GLOSS below), one for each khaṇḍa.
usage: gen_nighantu.py
"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS.parent / ".claude" / "skills" / "add-stotra" / "scripts"))
from dev2iast import dev2iast  # noqa: E402

ADHYAYA = {1: "Adhyāya 1 · the physical world: earth, sky, light, night, dawn, cloud, speech, water, rivers, horses, fire",
           2: "Adhyāya 2 · people and action: work, offspring, the body, desire, food, strength, wealth, cattle, anger, motion, battle",
           3: "Adhyāya 3 · qualities and acts: many and few, great, home, worship, happiness, form, truth, seeing, praise, the sage, sacrifice",
           4: "Adhyāya 4 · Naigama-kāṇḍa: single obscure words of the hymns",
           5: "Adhyāya 5 · Daivata-kāṇḍa: the deities, by the region of the world they belong to"}
GLOSS = {
    (1, 1): "Names of the earth — twenty-one.", (1, 2): "Names of gold — fifteen.",
    (1, 3): "Names of the mid-air, the space between earth and sky — sixteen.",
    (1, 4): "Words shared by sky and heaven — six.", (1, 5): "Names of the rays of light — fifteen.",
    (1, 6): "Names of the quarters of space — eight.", (1, 7): "Names of night — twenty-three.",
    (1, 8): "Names of dawn — sixteen.", (1, 9): "Names of day — twelve.",
    (1, 10): "Names of the cloud — thirty.", (1, 11): "Names of speech — fifty-seven.",
    (1, 12): "Names of water — a hundred and one.", (1, 13): "Names of rivers — thirty-seven.",
    (1, 14): "Names of the horse — twenty-six.",
    (1, 15): "Teams named for particular gods: Indra's two bays, Agni's red mare, the Sun's tawny mares, the Aśvins' asses, Pūṣan's goats, the Maruts' dappled deer, the Dawns' ruddy cows, Savitṛ's dark horses, Bṛhaspati's many-coloured team, Vāyu's team — ten.",
    (1, 16): "Verbs meaning “to blaze, to shine” — eleven.", (1, 17): "Names of flame, of what blazes — eleven.",
    (2, 1): "Names of work, of action — twenty-six.", (2, 2): "Names of offspring — fifteen.",
    (2, 3): "Names of men, of human beings — twenty-five.", (2, 4): "Names of the arms — twelve.",
    (2, 5): "Names of the fingers — twenty-one (twenty-two in the longer recension).",
    (2, 6): "Verbs meaning “to desire” — eighteen.", (2, 7): "Names of food — twenty-seven (twenty-eight in the longer recension).",
    (2, 8): "Verbs meaning “to eat” — ten.", (2, 9): "Names of strength — twenty-eight.",
    (2, 10): "Names of wealth — twenty-eight.", (2, 11): "Names of the cow — nine.",
    (2, 12): "Verbs meaning “to be angry” — ten.", (2, 13): "Names of anger — eleven.",
    (2, 14): "Verbs meaning “to go, to move” — a hundred and twenty-two.",
    (2, 15): "Names of what is swift — twenty-six.", (2, 16): "Names of what is near — eleven.",
    (2, 17): "Names of battle — forty-six.", (2, 18): "Verbs meaning “to pervade, to reach” — ten.",
    (2, 19): "Verbs meaning “to strike, to kill” — thirty-three.", (2, 20): "Names of the thunderbolt — eighteen.",
    (2, 21): "Verbs meaning “to rule” — four.", (2, 22): "Names of the lord, the master — four.",
    (3, 1): "Names of “much, many” — twelve.", (3, 2): "Names of “small, little” — eleven.",
    (3, 3): "Names of “great” — twenty-five.", (3, 4): "Names of the house — twenty-two.",
    (3, 5): "Verbs meaning “to serve, to worship” — ten.", (3, 6): "Names of happiness — twenty.",
    (3, 7): "Names of form, of beauty — sixteen.", (3, 8): "Names of what is praiseworthy — ten.",
    (3, 9): "Names of wisdom — eleven.", (3, 10): "Names of truth — six.",
    (3, 11): "Verbs meaning “to see” — eight.",
    (3, 12): "Particles of mixed sense — nine words, the last of the lists of synonyms.",
    (3, 13): "The particles and phrases of comparison: “like this”, “as this”, “like fire”, and so on.",
    (3, 14): "Verbs meaning “to praise, to worship” — forty-four.", (3, 15): "Names of the wise — twenty-four.",
    (3, 16): "Names of the praiser, the singer of hymns — thirteen.", (3, 17): "Names of sacrifice — fifteen.",
    (3, 18): "Names of priests — eight.", (3, 19): "Verbs meaning “to ask, to beg” — seventeen.",
    (3, 20): "Verbs meaning “to give” — ten.", (3, 21): "Verbs meaning “to request, to urge” — four.",
    (3, 22): "The two verbs meaning “to sleep”.", (3, 23): "Names of the well — fourteen.",
    (3, 24): "Names of the thief — fourteen.", (3, 25): "Names of what is hidden — six.",
    (3, 26): "Names of what is far — five.", (3, 27): "Names of what is old — six.",
    (3, 28): "Names of what is new — six.",
    (3, 29): "Words that come in pairs, each with two senses — twenty-six.",
    (3, 30): "Names of heaven and earth together, in the dual — twenty-four.",
    (4, 1): "The first list of single words of the hymns, each explained on its own in the Nirukta — sixty-two.",
    (4, 2): "The second list — eighty-four.", (4, 3): "The third list — a hundred and thirty-three.",
    (5, 1): "The deities of the earth headed by Agni — three.",
    (5, 2): "The other deities of the earth, those of the āprī hymns and the objects praised as gods — thirteen.",
    (5, 3): "Deified things and pairs: the horse, the bird, frogs, dice, pressing-stones, the chariot, the drum, the quiver, weapons, the mortar, rivers, waters, plants, night, the forest, faith, earth … — thirty-six.",
    (5, 4): "The deities of the mid-air headed by Vāyu — thirty-two.",
    (5, 5): "The other deities of the mid-air, with the goddesses — thirty-six.",
    (5, 6): "The deities of the sky headed by the Aśvins — thirty-one.",
}
NOTE = ("The Nighaṇṭu, the Vedic word-lists on which Yāska wrote the Nirukta: lists of synonyms (adhyāyas 1–3), "
        "obscure words (4) and deities (5). The text is Lakshman Sarup's critical edition (1927). Words in square "
        "brackets are found in only part of the manuscripts. Sarup prints svaras, which are not carried here. "
        "The glosses are a plain English key to each list.")
FOOTER = ("Source: Lakshman Sarup, The Nighaṇṭu and the Nirukta: Sanskrit text (University of the Panjab, 1927; "
          "public domain), read off the scan on archive.org and converted to IAST; editorial notes in SOURCES "
          "§5.30; glosses original")


def iast(s):
    t = dev2iast(re.sub(r"\s+", " ", s).strip())
    t = t.replace("॥", "||").replace("।", "|").replace("ऽ", "'")
    return re.sub(r"\s+", " ", t).strip()


def main():
    secs, adh, done = [], 0, set()
    for raw in (HERE / "nighantu.txt").read_text(encoding="utf-8").splitlines():
        l = raw.strip()
        if not l or l.startswith("@"):
            continue
        m = re.match(r"#\s*([1-5])$", l)
        if m:
            adh = int(m.group(1))
            secs.append({"heading": ADHYAYA[adh]})
            continue
        if l.startswith("#"):
            continue
        if l.startswith("="):
            secs.append({"colophon": iast(l[1:]).rstrip(" |") + " ||"})
            continue
        if l.startswith("+"):
            note, _, skt = l[1:].partition(": [")
            secs.append({"rubric": note.strip().rstrip(":") + ("." if not note.strip().endswith(".") else "")})
            if skt:
                secs.append({"padas": [iast("[ " + skt.strip())], "num": "", "gloss": "", "prose": True})
            continue
        m = re.search(r"॥\s*([०-९]+)\s*॥\s*$", l)
        if not m:
            sys.exit(f"unparsed line: {l[:60]}")
        n = int(m.group(1).translate(str.maketrans("०१२३४५६७८९", "0123456789")))
        body = l[:m.start()].strip()
        secs.append({"padas": [iast(body)], "num": f"|| {n} ||", "gloss": GLOSS[(adh, n)]})
        done.add((adh, n))
    missing = set(GLOSS) - done
    if missing:
        sys.exit(f"khaṇḍas not in the transcription: {sorted(missing)}")
    st = {"deity": "veda", "doc_title": "Nighaṇṭu", "app_title": "Nighaṇṭu", "h1": "Nighaṇṭu",
          "subtitle": "The Vedic word-lists commented on by Yāska · five adhyāyas, 78 khaṇḍas", "note": NOTE,
          "footer": FOOTER, "toc": True, "sections": secs}
    q = lambda v: repr(v) if isinstance(v, bool) else json.dumps(v, ensure_ascii=False)
    out = ["# -*- coding: utf-8 -*-", "# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)",
           "# Nighaṇṭu, from Sarup's 1927 edition (tools/nirukta/nighantu.txt) → IAST; written by",
           "# tools/nirukta/gen_nighantu.py. See SOURCES §5.30.", "", "STOTRA = {"]
    out += [f"    {q(k)}: {q(v)}," for k, v in st.items() if k != "sections"]
    out += ['    "sections": ['] + [f"    {s!r}," for s in secs] + ["    ],", "}", ""]
    (TOOLS / "stotras" / "nighantu.py").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(len(done), "khaṇḍas written")


if __name__ == "__main__":
    main()
