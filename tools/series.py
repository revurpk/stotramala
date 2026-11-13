# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Navigation for works that span several pages (the Learn lessons, the Nirukta, the Gītā …).

One registry, SERIES, lists each such work. tools/build_stotra.py asks series.apply(slug, st)
for every page it builds, and the page gets:

  * "nav"  — ‹ previous · contents · next ›, shown under the title and again at the foot of the
             page. A series with auto=True has it computed here from the files in tools/stotras
             (so a new lesson joins the chain by existing); the older works (Bhāgavatam,
             Rāmāyaṇa …) keep the hand-written "nav" their generators write, and get the foot copy.
  * "jump" — a collapsed "all lessons" list of every page of the series, for the short series
             (jump=True), so a reader can go straight to any part.

An entry:
  id          short name
  pat         regex on the slug; its first group is the page's number (or None for explicit order)
  order       optional explicit list of slugs (when the pages are not simply numbered)
  contents    slug of the contents page (None: no contents page, or the entry's own contents_href)
  contents_href  a href, relative to the pages, used when the contents is not a page of this work
  contents_label, label(n), jump_title, jump_label(n)   words shown
  auto        compute "nav" here
  jump        add the jump list

A contents page (e.g. tools/stotras/perry.py) is an ordinary page: it has no "series" itself.
"""
import pathlib
import re

DATA = pathlib.Path(__file__).resolve().parent / "stotras"


def roman(n):
    out = ""
    for v, s in ((40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")):
        while n >= v:
            out += s
            n -= v
    return out


_PERRY_NAMES = {"intro": "introduction", "gloss-1": "glossary I", "gloss-2": "glossary II", "appendix": "appendix"}
_PERRY_JUMP = {"intro": "intro", "gloss-1": "gloss I", "gloss-2": "gloss II", "appendix": "appx"}
_PERRY_ORDER = {"intro": 0, "gloss-1": 1001, "gloss-2": 1002, "appendix": 1003}


SERIES = [
    dict(id="perry", pat=r"perry-(\d+|intro|gloss-1|gloss-2|appendix)$", contents="perry", contents_label="all lessons",
         label=lambda n: _PERRY_NAMES.get(n) or f"lesson {roman(n)}", jump_title="all lessons",
         jump_label=lambda n: _PERRY_JUMP.get(n) or roman(n), auto=True, jump=True),
    dict(id="dhatu", pat=r"dhatu-(\d+)$", contents="dhatu", contents_label="all parts",
         label=lambda n: f"part {n}", jump_title="all parts", jump_label=lambda n: str(n), auto=True, jump=True),
    dict(id="subhashita", pat=None, jump_title="the śatakas", auto=False, jump=True,
         order=["subhashita-niti", "subhashita-shringara", "subhashita-vairagya", "subhashita-sumati", "subhashita-vemana"],
         jump_label=lambda n: n),
    dict(id="nirukta", pat=r"nirukta-(\d+)$", contents="nirukta", contents_label="Nirukta · contents",
         label=lambda n: "pariśiṣṭa" if n == 13 else f"adhyāya {n}", jump_title="all adhyāyas",
         jump_label=lambda n: "pariśiṣṭa" if n == 13 else str(n), auto=True, jump=True),
    dict(id="gita", pat=r"gita-bhashya-(\d+)$", jump_title="all chapters",
         jump_label=lambda n: str(n), auto=False, jump=True),
    dict(id="saptashati", pat=None, jump_title="all parts", auto=False, jump=True,
         order=["saptashati-purva", "saptashati-sukta"] + [f"saptashati-{i:02d}" for i in range(1, 14)]
         + ["saptashati-uttara"],
         jump_label=lambda n: n),
]

_JUMP_NAMES = {"subhashita-niti": "nīti", "subhashita-shringara": "śṛṅgāra", "subhashita-vairagya": "vairāgya", "subhashita-sumati": "sumati", "subhashita-vemana": "vemana", "saptashati-purva": "pūrva", "saptashati-sukta": "sūkta", "saptashati-uttara": "uttara"}


def _members(s):
    """Ordered [(slug, number)] of the pages of series s that exist."""
    if s.get("order"):
        return [(sl, _JUMP_NAMES.get(sl, str(int(sl.rsplit("-", 1)[1])) if sl.rsplit("-", 1)[1].isdigit() else sl))
                for sl in s["order"] if (DATA / f"{sl}.py").exists()]
    rx = re.compile(s["pat"])
    found = []
    for p in DATA.glob("*.py"):
        m = rx.match(p.stem)
        if m:
            g = m.group(1)
            found.append((_PERRY_ORDER[g] if g in _PERRY_ORDER else int(g), p.stem, g))
    return [(sl, g if g in _PERRY_ORDER else n) for n, sl, g in sorted(found)]


def _href(slug):
    return f"{slug}-iast.html"


def find(slug):
    for s in SERIES:
        if s.get("order"):
            if slug in s["order"]:
                return s
        elif re.match(s["pat"], slug):
            return s
    return None


def apply(slug, st):
    """Add "nav" (if the series computes it) and "jump" to the page data st, in place."""
    s = find(slug)
    if not s:
        return st
    members = _members(s)
    if not members:
        return st
    slugs = [m[0] for m in members]
    nums = dict(members)
    i = slugs.index(slug)
    if s.get("auto") and not st.get("nav"):
        nav = []
        if i > 0:
            nav.append(("‹ " + s["label"](nums[slugs[i - 1]]), _href(slugs[i - 1])))
        if s.get("contents"):
            nav.append((s["contents_label"], _href(s["contents"])))
        if i + 1 < len(slugs):
            nav.append((s["label"](nums[slugs[i + 1]]) + " ›", _href(slugs[i + 1])))
        st["nav"] = nav
    if s.get("jump") and len(slugs) > 1:
        lab = s["jump_label"]
        st["jump"] = {"title": s["jump_title"],
                      "links": [(lab(n), _href(sl), sl == slug)
                                for sl, n in members]}
    return st
