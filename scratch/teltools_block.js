// teltools.js — pure-JavaScript ports of the teltools transliterators.
// Importable everywhere: browser <script> (global `teltools`), Node
// require(), and ESM default import (via interop).
//
//   trans(text)     English RTS / ITRANS-style romanized -> Telugu
//   tel2hin(text)   Telugu -> Devanagari (exact ISCII codepoint shift)
//   hin2tel(text)   Devanagari -> Telugu (exact ISCII codepoint shift)
//   dev2iast(text)  Devanagari -> IAST
//   tel2iast(text)  Telugu -> IAST
//   iast2tel(text)  IAST -> Telugu
//
// `trans` is a line-for-line port of src/lib.rs trans(): the same key table,
// the same descending-lexicographic key scan with multi-match per pass, the
// same context rules (Consonant + Consonant/Vowel -> alt form with virama),
// the same halant insertion and <tag> skipping — verified byte-identical
// against trans.exe over a shared corpus (see test/).
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.teltools = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  var HALANT = "్";

  // ── trans: romanized -> Telugu ─────────────────────────────────────────
  // [key, result, alt_result, context] — context: V=Vowel, C=Consonant, M=Mark
  // Consonant alt defaults to virama+result (as in lib.rs).
  var E = [
    [".N", "ఁ", "ఁ", "V"], [".n", "ం", "ం", "V"],
    ["M", "ం", "ం", "V"], ["H", "ః", "ః", "V"],
    ["^a", "ఄ", "ఄ", "V"],
    ["a", "అ", "", "V"], ["aa", "ఆ", "ా", "V"], ["A", "ఆ", "ా", "V"],
    ["i", "ఇ", "ి", "V"], ["ii", "ఈ", "ీ", "V"], ["I", "ఈ", "ీ", "V"],
    ["u", "ఉ", "ు", "V"], ["uu", "ఊ", "ూ", "V"], ["U", "ఊ", "ూ", "V"],
    ["R^i", "ఋ", "ృ", "V"], ["L^i", "ఌ", "ౄ", "V"],
    ["^e", "఍", "౅", "V"], ["e", "ఎ", "ె", "V"],
    ["E", "ఏ", "ే", "V"], ["ee", "ఏ", "ే", "V"], ["ai", "ఐ", "ై", "V"],
    ["^o", "఑", "౉", "V"], ["o", "ఒ", "ొ", "V"],
    ["O", "ఓ", "ో", "V"], ["oo", "ఓ", "ో", "V"], ["au", "ఔ", "ౌ", "V"],
    [".a", "ఽ", "ఽ", "V"],
    ["XAA", "ౕ", "ౕ", "V"], ["XAI", "ౖ", "ౖ", "V"], ["XAU", "౗", "౗", "V"],
    ["R^I", "ౠ", "ౠ", "V"], ["L^I", "ౡ", "ౡ", "V"],
    ["XL^i", "ౢ", "ౢ", "V"], ["XL^I", "ౣ", "ౣ", "V"],
    ["k", "క", null, "C"], ["kSh", "క్ష", null, "C"], ["x", "క్ష", null, "C"],
    ["kh", "ఖ", null, "C"], ["g", "గ", null, "C"], ["ga.N", "గ్ం", null, "C"],
    ["gh", "ఘ", null, "C"], ["~N", "ఙ", null, "C"], ["N^", "ఙ", null, "C"],
    ["ch", "చ", null, "C"], ["chh", "ఛ", null, "C"], ["j", "జ", null, "C"],
    ["jh", "ఝ", null, "C"], ["~n", "ఞ", null, "C"], ["JN", "ఞ", null, "C"],
    ["T", "ట", null, "C"], ["Th", "ఠ", null, "C"], ["D", "డ", null, "C"],
    ["Dh", "ఢ", null, "C"], ["N", "ణ", null, "C"],
    ["t", "త", null, "C"], ["th", "థ", null, "C"], ["d", "ద", null, "C"],
    ["dh", "ధ", null, "C"], ["n", "న", null, "C"], ["N.", "఩", null, "C"],
    ["p", "ప", null, "C"], ["ph", "ఫ", null, "C"], ["b", "బ", null, "C"],
    ["bh", "భ", null, "C"], ["m", "మ", null, "C"],
    ["y", "య", null, "C"], ["r", "ర", null, "C"], ["R", "ఱ", null, "C"],
    ["l", "ల", null, "C"], ["L", "ళ", null, "C"], [".L", "ఴ", null, "C"],
    ["v", "వ", null, "C"], ["w", "వ", null, "C"],
    ["sh", "శ", null, "C"], ["S", "శ", null, "C"],
    ["Sh", "ష", null, "C"], ["shh", "ష", null, "C"],
    ["s", "స", null, "C"], ["h", "హ", null, "C"],
    ["cs", "ౘ", null, "C"], ["dz", "ౙ", null, "C"],
    ["^n", "఼", "఼", "M"], [".h", "్", "్", "M"],
    [".r", "౓", "౓", "M"], [".e", "౔", "౔", "M"],
    ["0", "౦", "౦", "M"], ["1", "౧", "౧", "M"], ["2", "౨", "౨", "M"],
    ["3", "౩", "౩", "M"], ["4", "౪", "౪", "M"], ["5", "౫", "౫", "M"],
    ["6", "౬", "౬", "M"], ["7", "౭", "౭", "M"], ["8", "౮", "౮", "M"],
    ["9", "౯", "౯", "M"],
    ["^.", "̇", "̇", "M"], ["_.", "̣", "̣", "M"],
    ["om", "ॐ", "ॐ", "M"], ["OM", "ॐ", "ॐ", "M"], ["AUM", "ॐ", "ॐ", "M"],
    ["'", "॑", "॑", "M"], ["\\_", "॒", "॒", "M"],
    ["|", "।", "।", "M"], ["||", "॥", "॥", "M"],
    [".H", "౸", "౸", "M"],
    ["1/4o", "౹", "౹", "M"], ["2/4o", "౺", "౺", "M"], ["3/4o", "౻", "౻", "M"],
    ["1/4e", "౼", "౼", "M"], ["2/4e", "౽", "౽", "M"], ["3/4e", "౾", "౾", "M"],
    [".t", "౿", "౿", "M"],
    ["\\kar", "᳐", "᳐", "M"], ["\\shr", "᳑", "᳑", "M"], ["\\prn", "᳒", "᳒", "M"],
    ["\\nih", "᳓", "᳓", "M"], ["\\yms", "᳔", "᳔", "M"], ["\\yais", "᳕", "᳕", "M"],
    ["\\yis", "᳖", "᳖", "M"], ["\\ykis", "᳗", "᳗", "M"], ["\\cb", "᳘", "᳘", "M"],
    ["\\ykiss", "᳙", "᳙", "M"], ["\"", "᳚", "᳚", "M"], ["\\3s", "᳛", "᳛", "M"],
    ["\\ka", "᳜", "᳜", "M"], ["\\.b", "᳝", "᳝", "M"], ["\\..b", "᳞", "᳞", "M"],
    ["\\2.b", "᳞", "᳞", "M"], ["\\3.b", "᳟", "᳟", "M"], ["\\ais", "᳡", "᳡", "M"],
    ["\\vs", "᳢", "᳢", "M"], ["\\vu", "᳣", "᳣", "M"], ["\\van", "᳥", "᳥", "M"],
    ["\\vut", "᳧", "᳧", "M"], ["\\vat", "᳨", "᳨", "M"], ["\\aag", "ᳩ", "ᳩ", "M"],
    ["\\abg", "ᳪ", "ᳪ", "M"], ["\\avg", "ᳫ", "ᳫ", "M"], ["\\avgt", "ᳬ", "ᳬ", "M"],
    ["\\3k", "᳭", "᳭", "M"], ["\\6n", "ᳮ", "ᳮ", "M"], ["\\ln", "ᳯ", "ᳯ", "M"],
    ["\\avs", "ᳲ", "ᳲ", "M"]
  ];
  var MAP = {};
  for (var i0 = 0; i0 < E.length; i0++) {
    var k0 = E[i0][0], r0 = E[i0][1], a0 = E[i0][2], c0 = E[i0][3];
    if (a0 === null) a0 = HALANT + r0;
    MAP[k0] = { r: r0, a: a0, c: c0 };
  }
  // Descending lexicographic — identical to Rust's BTreeMap keys().rev().
  var KEYS = Object.keys(MAP).sort().reverse();

  function transLine(line) {
    var out = "", i = 0, context = "O", skipTag = false;
    while (i < line.length) {
      var ch = line[i];
      if (ch === "<") skipTag = true;
      else if (ch === ">") skipTag = false;
      if (skipTag) {
        if (context === "C") out += HALANT;
        out += ch; i++; context = "O";
        continue;
      }
      var found = false;
      for (var ki = 0; ki < KEYS.length; ki++) {
        var key = KEYS[ki];
        if (line.startsWith(key, i)) {
          found = true;
          i += key.length;
          var v = MAP[key];
          out += (context === "C" && (v.c === "C" || v.c === "V")) ? v.a : v.r;
          context = v.c;
          // (like the Rust loop, keep scanning later keys at the new index)
        }
      }
      if (!found) {
        if (context === "C") out += HALANT;
        out += line[i]; i++; context = "O";
      }
    }
    if (context === "C") out += HALANT;
    return out;
  }

  function trans(text) {
    return String(text).split("\n").map(transLine).join("\n");
  }

  // ── Telugu <-> Devanagari: exact ISCII codepoint shifts ────────────────
  var HIN_KEEP = { 0x950: 1, 0x951: 1, 0x952: 1, 0x953: 1, 0x954: 1, 0x964: 1, 0x965: 1 };

  function tel2hin(text) {
    var out = "";
    for (var i = 0; i < text.length; i++) {
      var cp = text.charCodeAt(i);
      out += (cp >= 0x0C00 && cp <= 0x0C7F) ? String.fromCharCode(cp - 0x300) : text[i];
    }
    return out;
  }

  function hin2tel(text) {
    var out = "";
    for (var i = 0; i < text.length; i++) {
      var cp = text.charCodeAt(i);
      out += (cp >= 0x0900 && cp <= 0x097F && !HIN_KEEP[cp])
        ? String.fromCharCode(cp + 0x300) : text[i];
    }
    return out;
  }

  // ── Devanagari -> IAST (port of lib.rs dev2iast) ───────────────────────
  var D_CONS = { "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ṅ",
    "च": "c", "छ": "ch", "ज": "j", "झ": "jh", "ञ": "ñ",
    "ट": "ṭ", "ठ": "ṭh", "ड": "ḍ", "ढ": "ḍh", "ण": "ṇ",
    "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
    "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
    "य": "y", "र": "r", "ल": "l", "व": "v",
    "श": "ś", "ष": "ṣ", "स": "s", "ह": "h", "ळ": "ḷ" };
  var D_MATRA = { "ा": "ā", "ि": "i", "ी": "ī", "ु": "u", "ू": "ū",
    "ृ": "ṛ", "ॄ": "ṝ", "ॢ": "ḷ",
    "े": "e", "ै": "ai", "ो": "o", "ौ": "au" };
  var D_VOW = { "अ": "a", "आ": "ā", "इ": "i", "ई": "ī", "उ": "u", "ऊ": "ū",
    "ऋ": "ṛ", "ॠ": "ṝ", "ऌ": "ḷ",
    "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au" };
  var D_STRIP = { 0x900: 1, 0x93C: 1, 0x951: 1, 0x952: 1, 0x953: 1, 0x954: 1, 0x200C: 1, 0x200D: 1 };

  function dev2iast(s) {
    var out = "", pending = false;
    for (var i = 0; i < s.length; i++) {
      var ch = s[i], cp = s.charCodeAt(i);
      if (D_STRIP[cp]) continue;
      if (D_CONS[ch] !== undefined) {
        if (pending) out += "a";
        out += D_CONS[ch];
        pending = true;
      } else if (cp === 0x94D) {          // virama
        pending = false;
      } else if (D_MATRA[ch] !== undefined) {
        out += D_MATRA[ch];
        pending = false;
      } else if (D_VOW[ch] !== undefined) {
        if (pending) { out += "a"; pending = false; }
        out += D_VOW[ch];
      } else if (cp === 0x902) {          // anusvara
        if (pending) { out += "a"; pending = false; }
        out += "ṃ";
      } else if (cp === 0x903) {          // visarga
        if (pending) { out += "a"; pending = false; }
        out += "ḥ";
      } else {
        if (pending) { out += "a"; pending = false; }
        out += ch;
      }
    }
    if (pending) out += "a";
    return out;
  }

  function tel2iast(s) { return dev2iast(tel2hin(s)); }

  // ── IAST -> Telugu (port of lib.rs iast2tel) ───────────────────────────
  var I_CONS2 = { "kh": "ఖ", "gh": "ఘ", "ch": "ఛ", "jh": "ఝ", "ṭh": "ఠ",
    "ḍh": "ఢ", "th": "థ", "dh": "ధ", "ph": "ఫ", "bh": "భ" };
  var I_CONS1 = { "k": "క", "g": "గ", "ṅ": "ఙ", "c": "చ", "j": "జ", "ñ": "ఞ",
    "ṭ": "ట", "ḍ": "డ", "ṇ": "ణ", "t": "త", "d": "ద", "n": "న",
    "p": "ప", "b": "బ", "m": "మ", "y": "య", "r": "ర", "l": "ల",
    "ḻ": "ళ", "v": "వ", "ś": "శ", "ṣ": "ష", "s": "స", "h": "హ" };
  var I_MATRA = { "a": "", "ā": "ా", "i": "ి", "ī": "ీ", "u": "ు", "ū": "ూ",
    "ṛ": "ృ", "ṝ": "ౄ", "ḷ": "ౢ", "ḹ": "ౣ", "e": "ే", "ē": "ే", "o": "ో", "ō": "ో" };
  var I_VOW = { "a": "అ", "ā": "ఆ", "i": "ఇ", "ī": "ఈ", "u": "ఉ", "ū": "ఊ",
    "ṛ": "ఋ", "ṝ": "ౠ", "ḷ": "ఌ", "ḹ": "ౡ", "e": "ఏ", "ē": "ఏ", "o": "ఓ", "ō": "ఓ" };

  function iast2tel(frag) {
    var s = String(frag).toLowerCase();
    var out = "", i = 0, n = s.length;
    function consAt(j) {
      if (j >= n) return null;
      if (j + 1 < n && I_CONS2[s.substr(j, 2)] !== undefined) return s.substr(j, 2);
      if (I_CONS1[s[j]] !== undefined) return s[j];
      return null;
    }
    while (i < n) {
      var c = consAt(i);
      if (c) {
        out += (c.length === 2 ? I_CONS2[c] : I_CONS1[c]);
        i += c.length;
        if (i + 1 < n && s[i] === "a" && (s[i + 1] === "i" || s[i + 1] === "u")) {
          out += (s[i + 1] === "i") ? "ై" : "ౌ";
          i += 2;
        } else if (i < n && I_MATRA[s[i]] !== undefined) {
          out += I_MATRA[s[i]];
          i += 1;
        } else {
          out += HALANT;
        }
        continue;
      }
      if (i + 1 < n && s[i] === "a" && (s[i + 1] === "i" || s[i + 1] === "u")) {
        out += (s[i + 1] === "i") ? "ఐ" : "ఔ";
        i += 2;
        continue;
      }
      if (I_VOW[s[i]] !== undefined) {
        out += I_VOW[s[i]];
        i += 1;
        continue;
      }
      var ch = s[i];
      if (ch === "ṁ" || ch === "ṃ") out += "ం";
      else if (ch === "ḥ") out += "ః";
      else out += frag[i] !== undefined ? frag[i] : ch;
      i += 1;
    }
    return out;
  }

  return {
    trans: trans,
    tel2hin: tel2hin,
    hin2tel: hin2tel,
    dev2iast: dev2iast,
    tel2iast: tel2iast,
    iast2tel: iast2tel
  };
});
