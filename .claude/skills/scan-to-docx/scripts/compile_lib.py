"""Shared by build_docx.py and build_html.py: parse a compilation file and
lint its text. No third-party dependencies.

COMPILATION FILE (UTF-8, the single source of truth — edit this, rebuild the
outputs):

    # title: Śrī Rudra — collected readings
    # compiler: P. Revur
    # note: optional free text for the cover
    # toc: 3            (heading depth in the contents: 1 snippets, 2 = ##, 3 = ###)

    === snippet
    title: Mahānyāsa prayoga
    source: Nityakarma-Pūjā Prakāśika (Telugu)
    file: C:\\Users\\net\\Documents\\Books\\Devotional\\mahanyasam.pdf
    pages: 622-697
    script: tel
    accents: yes
    status: modern edition (©) — personal compilation
    note: anything the reader should know (uncertain lines, damage…)
    ---
    [p. 622]
    ## అథ పంచాంగ రుద్ర ధ్యానమ్
    first line of text
    second line of text

    a blank line starts a new stanza / paragraph
    [?ग?] marks an uncertain reading, [...] an illegible stretch
    ### a sub-section heading
    [fn 1] footnote text, placed where the page prints it

Header keys are free-form except `source` (required) and `script` (dev, tel,
kan, tam, mal, gu, bn, iast, mixed; default dev). In the text:

    ## heading / ### heading   a section / sub-section (contents + bookmarks)
    [p. 626]                   a page marker (printed page number)
    [fn 1] …                   a footnote, kept where the page prints it

Everything else after `---` is text, kept exactly as written.
"""
import re
import unicodedata

SCRIPTS = {
    "dev": (0x0900, 0x097F), "bn": (0x0980, 0x09FF), "gu": (0x0A80, 0x0AFF),
    "tam": (0x0B80, 0x0BFF), "tel": (0x0C00, 0x0C7F), "kan": (0x0C80, 0x0CFF),
    "mal": (0x0D00, 0x0D7F),
}
# Vedic signs that attach to any Indic script
VEDIC = set(range(0x0951, 0x0955)) | set(range(0x1CD0, 0x1D00)) | set(range(0xA8E0, 0xA900))
SHARED = {0x0964, 0x0965}                     # daṇḍa, double daṇḍa (shared by all)

PAGE = re.compile(r"^\[p\.\s*([^\]]+)\]$")
FOOT = re.compile(r"^\[fn\s*([^\]]*)\]\s*(.*)$")
HEAD = re.compile(r"^(#{2,3})\s+(.*)$")


def parse(path):
    text = open(path, encoding="utf-8").read()
    meta, snippets, cur, body = {}, [], None, None
    for raw in text.splitlines():
        line = raw.rstrip()
        if cur is None and line.startswith("#"):
            k, _, v = line[1:].partition(":")
            meta[k.strip().lower()] = v.strip()
            continue
        if line.strip() == "=== snippet":
            if cur is not None:
                cur["blocks"] = _blocks(body)
                snippets.append(cur)
            cur, body = {"_head": True}, None
            continue
        if cur is None:
            continue
        if cur.get("_head"):
            if line.strip() == "---":
                cur.pop("_head"); body = []
            elif line.strip():
                k, _, v = line.partition(":")
                cur[k.strip().lower()] = v.strip()
        else:
            body.append(unicodedata.normalize("NFC", raw.rstrip()))
    if cur is not None:
        cur.pop("_head", None)
        cur["blocks"] = _blocks(body or [])
        snippets.append(cur)
    for n, s in enumerate(snippets, 1):
        s.setdefault("script", "dev")
        s["id"] = f"s{n}"
        if "source" not in s:
            raise SystemExit(f"snippet without a 'source:' line: {s}")
        k = 0
        for b in s["blocks"]:
            if b["kind"] in ("h2", "h3"):
                k += 1; b["id"] = f"s{n}-{k}"
    return meta, snippets


def _blocks(lines):
    """Text lines -> blocks: stanza, h2, h3, page, fn."""
    out, cur = [], []

    def flush():
        if cur:
            out.append({"kind": "stanza", "lines": list(cur)}); cur.clear()

    for l in lines:
        s = l.strip()
        if not s:
            flush(); continue
        if m := PAGE.match(s):
            flush(); out.append({"kind": "page", "text": m.group(1).strip()}); continue
        if m := HEAD.match(s):
            flush(); out.append({"kind": "h2" if len(m.group(1)) == 2 else "h3",
                                 "text": m.group(2).strip()}); continue
        if m := FOOT.match(s):
            flush(); out.append({"kind": "fn", "mark": m.group(1).strip(), "text": m.group(2)}); continue
        cur.append(l)
    flush()
    return out


def text_lines(s):
    """Every line of Indic text in a snippet (stanzas, headings, footnotes)."""
    for b in s["blocks"]:
        if b["kind"] == "stanza":
            yield from b["lines"]
        elif b["kind"] in ("h2", "h3", "fn"):
            yield b["text"]


def toc(meta, snippets):
    """[(level, id, text, page)] for the contents, to the depth in `# toc:`."""
    depth = int(meta.get("toc", 3))
    out = []
    for s in snippets:
        marks = [b["text"] for b in s["blocks"] if b["kind"] == "page"]
        page = marks[0] if marks else s.get("pages", "").split("-")[0].strip()
        out.append((1, s["id"], s.get("title") or s["source"], page))
        for b in s["blocks"]:
            if b["kind"] == "page":
                page = b["text"]
            elif b["kind"] in ("h2", "h3") and int(b["kind"][1]) <= depth:
                out.append((int(b["kind"][1]), b["id"], b["text"], page))
    return out


def script_of(ch):
    cp = ord(ch)
    for name, (a, b) in SCRIPTS.items():
        if a <= cp <= b and cp not in SHARED and cp not in VEDIC:
            return name
    return None


def lint(snippets):
    """Warnings for mistakes that are easy to miss by eye."""
    warn = []
    for n, s in enumerate(snippets, 1):
        for line in text_lines(s):
            where = f"snippet {n} ({s['source'][:40]}): {line[:50]}"
            for word in re.split(r"\s+", line):
                scr = {script_of(c) for c in word} - {None}
                if len(scr) > 1:
                    warn.append(f"mixed scripts {sorted(scr)} in one word «{word}» — {where}")
            # Unicode order is base + vowel sign + anusvāra/visarga + svara
            for m in re.finditer(r"[\u0951\u0952\u1CD0-\u1CFF](?=[\u093E-\u094C\u0C3E-\u0C4C"
                                 r"\u0CBE-\u0CCC\u0902\u0903\u0C02\u0C03\u0C82\u0C83])", line):
                warn.append(f"accent before a vowel sign/anusvāra (U+{ord(m.group()):04X}) — "
                            f"put the svara after them — {where}")
            if re.search(r"[\u200B\uFEFF]", line):
                warn.append(f"zero-width space / BOM in text — {where}")
            if re.search(r"[A-Za-z]", line) and s["script"] not in ("iast", "mixed") \
                    and not re.search(r"\[\?|\[\.\.\.\]", line):
                warn.append(f"Latin letters in a {s['script']} snippet — {where}")
            if "\u25CC" in line:
                warn.append(f"dotted circle ◌ pasted into text — {where}")
        pages = [b["text"] for b in s["blocks"] if b["kind"] == "page"]
        nums = [int(p) for p in pages if p.isdigit()]
        for a, b in zip(nums, nums[1:]):
            if b != a + 1:
                warn.append(f"page markers jump {a} -> {b} in snippet {n} — a page skipped?")
    return warn


def has_accents(snippets):
    return any(ord(c) in VEDIC for s in snippets for l in text_lines(s) for c in l)


UNCERTAIN = re.compile(r"\[\?(.*?)\?\]|\[\.\.\.\]|\[…\]")
