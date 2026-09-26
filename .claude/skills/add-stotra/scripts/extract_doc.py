#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract a Word document (.docx, or Word's "Save as Web Page" .htm/.html)
into numbered paragraphs, in the original script AND in IAST.

WHY THIS EXISTS: devotional texts often arrive as the user's own Word
compilation keyed from a printed booklet, frequently in Telugu script.
Two traps make naive extraction wrong:

  • Word's HTML hard-wraps its SOURCE lines (~80 cols) mid-paragraph. Those
    newlines are ordinary spaces; splitting on them chops words and verses.
    Paragraph = <p>/<h*>/<li>/<td> (html) or <w:p> (docx) — nothing else.
  • Multi-column TABLES (ācamana names, aṣṭottaras, nyāsa, placement grids)
    flatten ROW by ROW, interleaving the columns — e.g. keśava, śrīdhara,
    puruṣottama, nārāyaṇa, … instead of keśava, nārāyaṇa, mādhava, ….
    So every table is printed in BOTH readings (row-major and column-major);
    choose per table, and set-check name lists against the standard sequence
    (pipeline.md §8). Some tables really are row-major (placement grids of
    name | direction pairs).

Telugu and Devanāgarī are both converted (Telugu via dev2iast.tel2dev); Latin
passes through. Numeric entities (&#3126;) — how Word HTML stores Telugu under
a windows-1252 charset — are decoded.

    python extract_doc.py <file.docx|file.htm> [--out PREFIX]

With --out, writes PREFIX.src.txt (original script) and PREFIX.iast.txt;
otherwise prints the IAST. Lines are `NNNN<TAB>text` for paragraphs and
`Tnn<TAB>…` for tables (a header, `row k:` lines, then one `cols:` line with
the column-major reading). srcdiff.py reads the .iast.txt directly.
"""
import html
import html.parser
import pathlib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from dev2iast import dev2iast, tel2dev  # noqa: E402

BLOCK = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "div"}


def to_iast(s):
    if re.search(r"[ఀ-౿]", s):
        s = tel2dev(s)
    if re.search(r"[ऀ-ॿ]", s):
        s = dev2iast(s)
    return s.replace("ऽ", "'").replace("॥", "||").replace("।", "|")


def clean(s):
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


# ───────────── Word HTML ─────────────
class _Html(html.parser.HTMLParser):
    """Stream of ('p', text) and ('table', [[cell, …], …]) items."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.buf = [], []
        self.skip = 0                       # inside <style>/<script>/<xml>
        self.tables = []                    # stack of row lists
        self.row = self.cell = None

    def _flush_para(self):
        t = clean("".join(self.buf)); self.buf = []
        if not t:
            return
        if self.cell is not None:
            self.cell.append(t)
        else:
            self.items.append(("p", t))

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script", "xml"):
            self.skip += 1
        elif tag == "table":
            self._flush_para(); self.tables.append([])
        elif tag == "tr" and self.tables:
            self.row = []; self.tables[-1].append(self.row)
        elif tag in ("td", "th") and self.row is not None:
            self._flush_para(); self.cell = []
        elif tag == "br":
            self._flush_para()
        elif tag in BLOCK:
            self._flush_para()

    def handle_endtag(self, tag):
        if tag in ("style", "script", "xml"):
            self.skip = max(0, self.skip - 1)
        elif tag in ("td", "th") and self.cell is not None:
            self._flush_para()
            self.row.append(" / ".join(self.cell)); self.cell = None
        elif tag == "tr":
            self.row = None
        elif tag == "table" and self.tables:
            rows = [r for r in self.tables.pop() if any(c for c in r)]
            if rows:
                self.items.append(("table", rows))
        elif tag in BLOCK:
            self._flush_para()

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


def read_html(path):
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("cp1252", errors="replace")
    text = re.sub(r"(?s)<!--.*?-->", "", text)
    p = _Html(); p.feed(text); p._flush_para()
    return p.items


# ───────────── .docx ─────────────
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _ptext(p):
    out = []
    for el in p.iter():
        if el.tag == W + "t":
            out.append(el.text or "")
        elif el.tag in (W + "tab", W + "br", W + "cr"):
            out.append(" ")
    return clean("".join(out))


def read_docx(path):
    with zipfile.ZipFile(path) as z:
        body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    items = []
    for el in body:
        if el.tag == W + "p":
            t = _ptext(el)
            if t:
                items.append(("p", t))
        elif el.tag == W + "tbl":
            rows = []
            for tr in el.iter(W + "tr"):
                cells = [" / ".join(filter(None, (_ptext(p) for p in tc.iter(W + "p"))))
                         for tc in tr.findall(W + "tc")]
                if any(cells):
                    rows.append(cells)
            if rows:
                items.append(("table", rows))
    return items


# ───────────── output ─────────────
def render(items, conv):
    lines, n, t = [], 0, 0
    for kind, val in items:
        if kind == "p":
            lines.append(f"{n:04d}\t{conv(val)}"); n += 1
            continue
        t += 1
        ncol = max(len(r) for r in val)
        lines.append(f"T{t:02d}\ttable {len(val)} rows × {ncol} cols — choose a reading")
        for k, r in enumerate(val, 1):
            lines.append(f"T{t:02d}\trow {k}: " + " | ".join(conv(c) for c in r))
        cols = [conv(r[c]) for c in range(ncol) for r in val if c < len(r) and r[c]]
        lines.append(f"T{t:02d}\tcols: " + " · ".join(cols))
    return "\n".join(lines) + "\n"


def main(argv):
    if not argv:
        sys.exit(__doc__)
    path = pathlib.Path(argv[0])
    items = read_docx(path) if path.suffix.lower() == ".docx" else read_html(path)
    np = sum(1 for k, _ in items if k == "p"); nt = len(items) - np
    if "--out" in argv:
        prefix = pathlib.Path(argv[argv.index("--out") + 1])
        prefix.with_suffix(".src.txt").write_text(render(items, lambda s: s), encoding="utf-8")
        prefix.with_suffix(".iast.txt").write_text(render(items, to_iast), encoding="utf-8")
        print(f"{np} paragraphs, {nt} tables -> {prefix}.src.txt / {prefix}.iast.txt")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(render(items, to_iast))


if __name__ == "__main__":
    main(sys.argv[1:])
