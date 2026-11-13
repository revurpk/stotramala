# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Draft tools/stories/pancatantra.src.txt from the Sanskrit Wikisource pages saved in scratch/pt/ (see SOURCES §11).
Each story is (title, file, first line, last line [, stop-marker]); output is for hand review."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = ROOT / "scratch" / "pt"
def clean(l):
    l = re.sub(r"<[^>]+>", "", l)
    l = re.sub(r"\[https?://[^\]]*\]", "", l)
    l = re.sub(r"॥\s*पञ्च_([०-९0-9.]+)\s*॥", lambda m: " ॥ " + m.group(1) + " ॥", l)
    l = re.sub(r"॥\s*([०-९0-9]+)\s*॥", r"॥ \1 ॥", l)
    l = re.sub(r"[।]{2}\s*([०-९0-9]+)\s*[।]{2}", r"॥ \1 ॥", l)
    l = l.replace("-", "") if False else l
    return re.sub(r"\s+", " ", l).strip()
MARK = re.compile(r"॥\s*[०-९0-9.]+\s*॥\s*$")
def units(lines):
    out, buf = [], []
    def flush():
        nonlocal buf
        if buf: out.append(buf); buf = []
    for l in lines:
        l = clean(l)
        if not l or l == "---": continue
        if len(l) < 32 and not MARK.search(l): flush(); out.append([l]); continue
        if MARK.search(l): buf.append(l); flush(); continue
        if len(l) >= 120: flush(); out.append([l]); continue
        buf.append(l)
    flush(); return out
def story(title, segs):
    ls = []
    for fn, a, b, stop in segs:
        seg = (RAW / fn).read_text(encoding="utf-8").splitlines()[a - 1:b]
        if stop:
            for i, l in enumerate(seg):
                if stop in l: seg = seg[:i + 1]; seg[-1] = seg[-1][:seg[-1].index(stop) + len(stop)]; break
        ls += seg
    return "# " + title + "\n\n" + "\n\n".join("\n".join(u) for u in units(ls)) + "\n"
SPECS = {
 "monkey": ("The Monkey and the Wedge | कीलोत्पाटिवानरकथा", [("pt_01.txt", 98, 98, "प्राग् एव निवेदितम्")]),
 "drum": ("The Jackal and the Drum | शृगालदुन्दुभिकथा", [("pt_03.txt", 97, 102, None)]),
 "crab": ("The Crane and the Crab | बककुलीरककथा", [("pt_05.txt", 246, 283, None)]),
 "crow": ("The Crows and the Black Snake | वायसकृष्णसर्पकथा", [("pt_05.txt", 287, 295, None)]),
 "hare": ("The Lion and the Hare | भासुरकसिंहशशककथा", [("pt_05.txt", 308, 308, None), ("pt_05.txt", 335, 357, None), ("pt_06.txt", 2, 28, None)]),
 "jackal": ("The Blue Jackal | चण्डरवशृगालकथा", [("pt_06.txt", 148, 165, None)]),
}
if __name__ == "__main__":
    out = "\n".join(story(*SPECS[k]) for k in (sys.argv[1:] or SPECS))
    sys.stdout.write(out)
