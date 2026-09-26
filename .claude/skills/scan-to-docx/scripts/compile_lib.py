"""Shared by build_docx.py and build_html.py: parse a compilation file and
lint its text. No third-party dependencies.

COMPILATION FILE (UTF-8, the single source of truth — edit this, rebuild the
outputs):

    # title: Śrī Rudra — collected readings
    # compiler: P. Revur
    # note: optional free text for the cover

    === snippet
    source: Mahānyāsam, Vavilla Ramaswamy Sastrulu & Sons, Madras 1937
    file: C:\\Users\\net\\Documents\\Books\\Devotional\\mahanyasam.pdf
    pages: 3-4
    script: dev
    accents: yes
    status: public domain (1937 print)
    note: anything the reader should know (uncertain lines, damage…)
    ---
    first line of text
    second line of text

    a blank line starts a new stanza / paragraph
    [?ग?] marks an uncertain reading, [...] an illegible stretch

Header keys are free-form except `source` (required) and `script` (dev, tel,
kan, tam, mal, gu, bn, iast, mixed; default dev). Everything after `---`
until the next `=== snippet` is the text, kept exactly as written.
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
                cur["text"] = _stanzas(body)
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
        cur["text"] = _stanzas(body or [])
        snippets.append(cur)
    for s in snippets:
        s.setdefault("script", "dev")
        if "source" not in s:
            raise SystemExit(f"snippet without a 'source:' line: {s}")
    return meta, snippets


def _stanzas(lines):
    out, cur = [], []
    for l in lines:
        if l.strip():
            cur.append(l)
        elif cur:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
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
        for st in s["text"]:
            for line in st:
                where = f"snippet {n} ({s['source'][:40]}): {line[:50]}"
                for word in re.split(r"\s+", line):
                    scr = {script_of(c) for c in word} - {None}
                    if len(scr) > 1:
                        warn.append(f"mixed scripts {sorted(scr)} in one word «{word}» — {where}")
                # Unicode order is base + vowel sign + anusv\u0101ra/visarga + svara
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
    return warn


def has_accents(snippets):
    return any(ord(c) in VEDIC for s in snippets for st in s["text"] for l in st for c in l)


UNCERTAIN = re.compile(r"\[\?(.*?)\?\]|\[\.\.\.\]|\[…\]")
