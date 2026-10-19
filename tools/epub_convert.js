// Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
//
// Script conversion for build_epub.py. It runs the page's own code: the
// teltools transliterator and the converter functions (prep … computed) are
// read out of the shell page at run time, so the e-book renders every line
// exactly as the site does.
//
//   stdin:  {"shell": path, "src": "iast"|"tel", "script": "iast"|"dev"|"tel",
//            "svara": bool, "items": [{"t": text, "w": bool}, …]}
//   stdout: ["converted", …]   (same order)
//
// "w" marks a word-by-word entry, whose compound hyphens are kept and each
// member converted on its own, as on the page.
"use strict";
const fs = require("fs");
const vm = require("vm");

const req = JSON.parse(fs.readFileSync(0, "utf8").replace(/^﻿/, ""));
const shell = fs.readFileSync(req.shell, "utf8");
const scripts = [...shell.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1]);
const tel = scripts.find(s => s.includes("teltools.js"));
const page = scripts.find(s => s.includes("function computed("));
if (!tel || !page) throw new Error("shell page: transliterator or converter not found");
const a = page.indexOf("var DIG"), b = page.indexOf("var SLUG");
if (a < 0 || b < a) throw new Error("shell page: converter block not found");

// minimal browser stand-ins for the few globals the converter block touches
const ctx = {
  module: { exports: {} },
  document: {
    documentElement: { dataset: { src: req.src } },
    createElement: () => ({ getContext: () => ({}) }),
  },
};
ctx.exports = ctx.module.exports;
ctx.window = ctx;
vm.createContext(ctx);
vm.runInContext(tel, ctx);
if (typeof ctx.teltools === "undefined") ctx.teltools = ctx.module.exports;
vm.runInContext(page.slice(a, b) + "\nthis.__computed = computed; this.__strip = stripSvara;", ctx);

const sc = req.script;
const one = s => ctx.__computed(req.svara || req.src === "tel" ? s : ctx.__strip(s), sc);
const out = req.items.map(({ t, w }) =>
  w && t.indexOf("-") > 0 ? t.split("-").map(one).join("-") : one(t));
process.stdout.write(JSON.stringify(out));
