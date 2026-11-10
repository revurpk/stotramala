#!/bin/sh
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# OCR the main text of pages of Sarup's 1927 Nirukta (archive.org in.ernet.dli.2015.282287):
# fetch the full scan of each leaf, crop what lies above the footnote rule (maintext.py),
# run Tesseract's Sanskrit model. Nothing fetched is committed.
# usage: ocrmain.sh OUTDIR TESSDATA PYTHON LEAF...   (writes mN.png, mN.txt)
OUT=$1; TD=$2; PY=$3; shift 3
T="${TESSERACT:-tesseract}"
HERE=$(dirname "$0")
mkdir -p "$OUT"
for n in "$@"; do
  f="$OUT/n$n.jpg"
  [ -s "$f" ] || { curl -sL -A "stotramala-source/1.0" -o "$f" "https://archive.org/download/in.ernet.dli.2015.282287/page/n$n.jpg"; sleep 1; }
  "$PY" -I "$HERE/maintext.py" "$f" "$OUT/m$n.png" >/dev/null
  "$T" "$OUT/m$n.png" "$OUT/m$n" --tessdata-dir "$TD" -l san --psm 6 >/dev/null 2>&1
  echo "$n $(wc -c < "$OUT/m$n.txt")"
done
