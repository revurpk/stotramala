# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
"""Fetch Sanskrit Wikisource's Vālmīki Rāmāyaṇa raw wikitext, politely.

Lists every page under रामायणम्/, then pulls their wikitext 50 titles per
request (prop=revisions), DELAY seconds apart, with back-off on HTTP errors.
Cached per batch, so a rerun resumes. Writes pages.json {title: wikitext}.
usage: fetch.py OUTDIR
"""
import hashlib, json, pathlib, sys, time, urllib.error, urllib.parse, urllib.request

API = "https://sa.wikisource.org/w/api.php"
UA = {"User-Agent": "stotramala-source/1.0 (personal research; https://github.com/revurpk/stotramala)"}
DELAY = 3.0
out = pathlib.Path(sys.argv[1]); cache = out / "cache"; cache.mkdir(parents=True, exist_ok=True)
log = open(out / "fetch.log", "a", encoding="utf-8", buffering=1)
last = [0.0]

def get(params):
    key = hashlib.sha1(json.dumps(params, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    f = cache / f"{key}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    # POST: fifty Devanāgarī titles make too long a URL (HTTP 414)
    body = urllib.parse.urlencode({**params, "format": "json", "formatversion": "2"}).encode()
    for k in range(8):
        wait = DELAY - (time.time() - last[0])
        if wait > 0:
            time.sleep(wait)
        last[0] = time.time()
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(API, data=body, headers=UA), timeout=120).read())
            f.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
            return d
        except urllib.error.HTTPError as e:
            ra = e.headers.get("Retry-After")
            pause = int(ra) if ra and ra.isdigit() else min(300, 15 * 2 ** k)
            log.write(f"HTTP {e.code}; sleeping {pause}s\n"); time.sleep(pause)
        except Exception as e:
            log.write(f"{type(e).__name__}: {e}; retry\n"); time.sleep(15 * (k + 1))
    raise RuntimeError("giving up")

titles, cont = [], {}
while True:
    d = get({"action": "query", "list": "allpages", "apprefix": "रामायणम्/", "apnamespace": 0,
             "aplimit": "500", **cont})
    titles += [p["title"] for p in d["query"]["allpages"]]
    if "continue" not in d:
        break
    cont = {k: v for k, v in d["continue"].items() if k != "continue"}
log.write(f"{len(titles)} titles\n")
pages = {}
for i in range(0, len(titles), 50):
    batch = titles[i:i + 50]
    d = get({"action": "query", "prop": "revisions", "rvprop": "content|ids", "rvslots": "main",
             "titles": "|".join(batch), "redirects": "0"})
    for p in d["query"]["pages"]:
        if "revisions" in p:
            r = p["revisions"][0]
            pages[p["title"]] = {"rev": r["revid"], "text": r["slots"]["main"]["content"]}
    log.write(f"{min(i + 50, len(titles))}/{len(titles)} pages\n")
json.dump(pages, open(out / "pages.json", "w", encoding="utf-8"), ensure_ascii=False)
log.write(f"DONE {len(pages)} pages\n")
