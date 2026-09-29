#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Written for the Ramakrishna Math Gītā-bhāṣya PDF (SOURCES §7.4); see
# references/pipeline.md §9. Usage:  from priyaanka import convert# -*- coding: utf-8 -*-
"""Priyaanka (legacy, glyph-encoded Telugu DTP font) -> Unicode Telugu.

The PDF's text layer stores glyph codes in visual order: consonant bodies,
talakaṭṭu ticks, vowel-sign pieces, subscript (vattu) glyphs after the vowel
sign, and a few pieces (ra-vattu, e-signs) *before* the base they belong to.
We tokenise glyphs, group them into akṣaras, and emit canonical Unicode:
base + (virāma + consonant)* + vowel sign + anusvāra/visarga.
"""
import re
import unicodedata

V = "్"  # virāma
VIR = V

# ---- glyph classes -------------------------------------------------------
BASE = {  # consonant bodies (inherent a unless a sign follows)
    "H": "క", "‰": "క", "K": "చ", "[": "జ", "*": "జ", "V": "ఙ", "&": "ఞ",
    "\\": "ట", ">": "ట", "@": "ట", "_": "డ", "}": "ణ", "`": "త", "^": "ద",
    "#": "న", "<": "న", "Ñ": "ప", "á": "ప", "|": "బ", "É": "బ", "=": "వ",
    '"': "వ", "Ü": "య", "~": "ర", "Å": "ల", "Ö": "ల", "â": "శ", "+": "ష",
    "ë": "ష", "ã": "స", "™": "స", "Ç": "హ", "Q": "గ", "M": "ఖ", "Y": "ఖ",
    "à": "ళ",
}
COMPOSITE = {  # glyphs carrying consonant(s) + vowel
    "q": ("వ", "ి"), "g": ("వ", "ీ"), "x": ("న", "ి"), "h": ("న", "ీ"),
    "k": ("ద", "ి"), "n": ("ద", "ీ"), "i": ("ర", "ి"), "s": ("ర", "ీ"),
    "u": ("త", "ి"), "f": ("త", "ీ"), "t": ("శ", "ి"), "j": ("శ", "ీ"),
    "z": ("చ", "ి"), "p": ("చ", "ీ"), "l": ("జ", "ి"), "r": ("జ", "ీ"),
    "y": ("గ", "ి"), "w": ("గ", "ీ"), "e": ("ల", "ి"), "b": ("ల", "ీ"),
    "a": ("బ", "ి"), "c": ("బ", "ీ"), "d": ("ఖ", "ి"), "v": ("ఖ", "ీ"),
    "A": ("జ", "ు"), "E": ("జ", "ూ"), "†": ("న", "ు"),
    "N": ("శ్ర", "ీ"), "G": ("స్త్ర", ""), "R": ("ష్ట్ర", ""),
}
INDEP = {"J": "అ", "P": "ఆ", "W": "ఇ", "D": "ఈ", "L": "ఉ", "T": "ఊ",
         "Z": "ఎ", "U": "ఏ", "S": "ఐ", "X": "ఒ", "F": "ఓ", "B": "ఔ"}
TICK = set("¨«°»ÆíõŒ◊")
SIGN = {  # vowel signs following the base
    "å": "ా", "ê": "ా", "Í": "ా", "ß": "ా", "•": "ా", "®": "ా", "": "ా",
    "≤": "ి", "˜": "ి", "ç": "ి", "‘": "ీ", "©": "ీ",
    "∞": "ు", "Ù": "ు", "Ω": "ు", "μ": "ు", "ï": "ు", "√": "ు",
    "Ä": "ూ", "Ó": "ూ", "˙": "ూ", "¥": "ూ", "Ø": "ూ",
    "Õ": "ే", "Ë": "ే", "ı": "ే",
    "≥": "ె", "ˇ": "ె", "‹": "ె", "˘": "ొ", "⁄": "ొ",
    "À": "ో", "’": "ో", "È": "ో", "Ÿ": "ో",
    "Ò": "ౌ", "“": "ౌ", "ø": "ౌ", "œ": "ౌ", "∫": "ౌ",
    "·": "ౖ", "ÿ": "ౖ", "Â": "ౖ",
    "$": "ృ",
}
HOOK = {"∞": "", "Ú": "ు", "∂": "ా", "¸": "ూ"}   # on మ/య/ఘ
HOOK_PLAIN = {"∞": "ు", "Ú": "ు", "∂": "ూ", "¸": "ూ"}
PRE = {"ˆ": "ే", "¿": "ే", "Ô": "ె", "Ã": "ె"}
PRE_RA = set("„¢")
VATTU = {
    "‡": "మ", "Î": "త", "ﬁ": "వ", "º": "య", "÷": "థ", "ú": "ధ", "Ì": "ద",
    "≈": "శ", "¡": "ల", "Û": "చ", "˚": "జ", "˝": "ఞ", "‚": "ణ", "¬": "ష",
    "›": "హ", "¯": "క", "Ê": "ప", "ƒ": "బ", "æ": "గ", "ö": "ఖ", "Δ": "ష",
    "ª": "ఠ", "ì": "ట", "¤": "డ", "û": "స", "ﬂ": "న", "…": "ఘ",
}
VIRAMA = set("£ü±ò")
ASP_BASE = {"è": {"ద": "ధ", "బ": "భ", "డ": "ఢ", "చ": "ఛ", "ట": "ఠ", "గ": "ఘ", "జ": "ఝ"},
            "ä": {"ద": "థ", "ట": "ఠ"},
            "¶": {"ప": "ఫ"}}
ASP_VATTU = {"చ": "ఛ", "బ": "భ", "ద": "ధ", "గ": "ఘ", "ట": "ఠ", "జ": "ఝ", "ప": "ఫ"}
MOD = {"O": "ం", "ó": "ః"}
HOOKABLE = {"వ": "మ", "ఫ": "ఘ", "య": "య"}
TAIL = "Ï"          # హ's tail (inherent a); elsewhere Ï is ా
PUNCT = {"—": "’", "–": "–", "-": "ఽ"}


class Ak:
    __slots__ = ("base", "vattus", "signs", "mods", "pre", "pre_ra", "hook", "tail", "ind")

    def __init__(self, base, ind=False):
        self.base, self.ind = base, ind
        self.vattus, self.signs, self.mods, self.pre = [], [], [], []
        self.pre_ra, self.hook, self.tail = False, None, False

    def emit(self):
        base = self.base
        signs = list(self.pre) + list(self.signs)
        if self.hook is not None:
            if base in HOOKABLE:
                base = HOOKABLE[base]
                if "ె" in signs and self.hook in "∂Ú":
                    signs.remove("ె"); signs.append("ో" if self.hook == "∂" else "ొ")
                elif self.hook != "∞" or not signs:
                    if HOOK[self.hook]: signs.append(HOOK[self.hook])
            else:
                signs.append(HOOK_PLAIN[self.hook])
        if base == "హ" and not self.tail and not signs and not self.ind and not self.vattus:
            pass  # bare హ body; resolved by data (see notes)
        out = base
        for v in self.vattus:
            out += V + v
        if self.pre_ra:   # ra-phala precedes a final ya-phala: త్ర్య
            if out.endswith(V + "య"): out = out[:-2] + V + "ర" + V + "య"
            else: out += V + "ర"
        # combine vowel signs
        s = "".join(signs)
        s = (s.replace("ౖె", "ై").replace("ేౖ", "ై").replace("ెూ", "ో").replace("ెు", "ొ").replace("ుృ", "ృ"))  # ె+ౖ=ై, ె+ూ-hook=ో, ె+ు-hook=ొ, ు-hook before ృ (ష్టృ)
        out += s + "".join(self.mods)
        return out


SEQ = [  # multi-glyph sequences, rewritten before tokenising (order matters)
    ("|∞∞", "\uE010"), ("|∞¸", "\uE011"),
    ("∞∞", "Ú"), ("∞∂", "¸"),   # some pages double the hook
    ("~°≠", "\uE012"), ("~Ú", "\uE013"), ("~¸", "\uE014"),
    ("$Ï", "\uE015"), ("÷û", "\uE016"), ("~î", "\uE017"), ("iî", "\uE018"),
]
INDEP.update({"\uE010": "ఋ", "\uE011": "ౠ"})
BASE.update({"\uE012": "ఝ", "\uE017": "ఠ", "é": "ర"})
COMPOSITE.update({"m": ("ళ", "ీ"), "o": ("ళ", "ి")})
SIGN.update({"Á": "ొ", "∏": "ొ", "ô": "ి"})
VATTU.update({"§": "ళ", "]": "ర"})
VIRAMA.update("∑π")
COMPOSITE.update({"\uE013": ("య", "ి"), "\uE014": ("య", "ీ"), "\uE018": ("ఠ", "ి")})
SIGN.update({"\uE015": "ౄ"})


POST = set(TICK) | set(SIGN) | set(HOOK) | set(VATTU) | VIRAMA | set("èä¶ùÏC")
POSTSPACE = re.compile(" +([" + re.escape("".join(sorted(POST - {"-"}))) + "])")


def convert(text):
    # the PDF inserts spaces before glyphs that hang off a base (స్మ $తి)
    text = POSTSPACE.sub(r"\1", text)
    for a, b in SEQ:
        text = text.replace(a, b)
    out, cur, pend_pre, pend_ra = [], None, [], False

    def flush():
        nonlocal cur
        if cur is not None:
            out.append(cur.emit())
            cur = None

    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c in PRE:
            pend_pre.append(PRE[c]); i += 1; continue
        if c in PRE_RA:
            pend_ra = True; i += 1; continue
        if c in BASE or c in COMPOSITE or c in INDEP:
            flush()
            if c in BASE:
                cur = Ak(BASE[c])
            elif c in COMPOSITE:
                b, s = COMPOSITE[c]
                cur = Ak(b)
                if s: cur.signs.append(s)
            else:
                cur = Ak(INDEP[c], ind=True)
            cur.pre, pend_pre = pend_pre, []
            cur.pre_ra, pend_ra = pend_ra, False
            i += 1; continue
        if cur is not None:
            if c in TICK:
                i += 1; continue
            if c == TAIL:
                if cur.base == "హ" and not cur.vattus: cur.tail = True
                else: cur.signs.append("ా")
                i += 1; continue
            if c in HOOK and (cur.base in HOOKABLE or cur.hook is None and c in "∞Ú∂¸"):
                if cur.base in HOOKABLE and cur.hook is None and not cur.vattus:
                    cur.hook = c
                else:
                    cur.signs.append(HOOK_PLAIN[c])
                i += 1; continue
            if c == "$" and cur.signs and cur.signs[-1] in ("ి", "ీ"):
                cur.vattus.append("ర"); i += 1; continue   # ra-vattu after i/ī (సంస్క్రియ)
            if c in SIGN:
                cur.signs.append(SIGN[c]); i += 1; continue
            if c in VATTU:
                cur.vattus.append(VATTU[c]); i += 1; continue
            if c == "C":
                cur.vattus.append("ప"); cur.signs.append("ు"); i += 1; continue
            if c == "\uE016":
                cur.vattus += ["స", "థ"]; i += 1; continue
            if c in VIRAMA:
                cur.signs.append(VIR); i += 1; continue
            if c in MOD:
                cur.mods.append(MOD[c]); i += 1; continue
            if c in ASP_BASE:
                tbl = ASP_BASE[c]
                if cur.vattus and cur.vattus[-1] in ASP_VATTU:
                    cur.vattus[-1] = ASP_VATTU[cur.vattus[-1]]
                elif cur.base in tbl:
                    cur.base = tbl[cur.base]
                i += 1; continue
            if c == "ù":
                if cur.vattus and cur.vattus[-1] in ASP_VATTU:
                    cur.vattus[-1] = ASP_VATTU[cur.vattus[-1]]
                i += 1; continue
        # anything else ends the akṣara
        flush()
        if c == "-" and out and i + 1 < n and text[i + 1] not in " \n":
            out.append("ఽ")
        elif c == "I":
            if text[i:i + 2] == "II": out.append("॥"); i += 1
            else: out.append("।")
        elif c == "\x0b":
            pass
        elif c in MOD:   # anusvāra after an avagraha (తేజోఽంశ)
            out.append(MOD[c])
        else:
            out.append(PUNCT.get(c, c) if c in "—" else c)
        i += 1
    flush()
    return unicodedata.normalize("NFC", "".join(out))
