# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Wire one built Perry lesson into index.html, README.md and SOURCES.md §8.1.
usage: wire.py NN FIRST_LEAF LAST_LEAF FIRST_PAGE LAST_PAGE
The lesson's "! …" lines (tools/perry/lessonNN.txt) are appended to SOURCES as notes."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "perry"))
from gen_perry import ROMAN  # noqa: E402

nn, l0, l1, p0, p1 = (int(x) for x in sys.argv[1:6])
R, Rp = ROMAN[nn], ROMAN[nn - 1]
rd = lambda f: (ROOT / f).read_text(encoding="utf-8")
wr = lambda f, s: (ROOT / f).write_text(s, encoding="utf-8", newline="")

s = rd("index.html")
a = f'      <li><a href="stotra/learn/perry-{nn-1:02d}-iast.html">Lesson {Rp}</a></li>\n'
assert a in s
s = s.replace(a, a + f'      <li><a href="stotra/learn/perry-{nn:02d}-iast.html">Lesson {R}</a></li>\n')
s = re.sub(r"lessons 1–\d+ so far", f"lessons 1–{nn} so far", s)
wr("index.html", s)

s = rd("README.md")
row = next(l for l in s.split("\n") if l.startswith("| Learn | A Sanskrit Primer"))
new = re.sub(r"lessons I–[IVXL]+ so far", f"lessons I–{R} so far", row)
new = new[: -len(" |")] + f" · [{R}](stotra/learn/perry-{nn:02d}-iast.html) |"
wr("README.md", s.replace(row, new))

s = rd("SOURCES.md")
s = re.sub(r"Lessons I–[IVXL]+ are done so far", f"Lessons I–{R} are done so far", s)
a = "). Public domain: published 1885"
assert s.count(a) == 1
s = s.replace(a, f"; Lesson {R} = leaves n{l0}–n{l1} = pp. {p0}–{p1}" + a)
notes = [x.strip()[1:].strip() for x in rd(f"tools/perry/lesson{nn:02d}.txt").splitlines() if x.strip().startswith("!")]
if notes:
    s = s.rstrip("\n") + "\n" + "".join(f"- Lesson {R}: {n}\n" for n in notes)
wr("SOURCES.md", s)
print("wired lesson", R)
