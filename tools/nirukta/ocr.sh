#!/bin/sh
# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# OCR pages of Sarup's 1927 Nirukta (archive.org in.ernet.dli.2015.282287): fetch the
# full scan of each leaf, clean it (clean.py), run Tesseract's Sanskrit model.
# Nothing fetched is committed.  usage: ocr.sh OUTDIR TESSDATA PYTHON LEAF...
OUT=$1; TD=$2; PY=$3; shift 3
T="${TESSERACT:-tesseract}"
HERE=$(dirname "$0")
mkdir -p "$OUT"
for n in "$@"; do
  f="$OUT/n$n.jpg"
  [ -s "$f" ] || { curl -sL -A "stotramala-source/1.0" -o "$f" "https://archive.org/download/in.ernet.dli.2015.282287/page/n$n.jpg"; sleep 1; }
  "$PY" -I "$HERE/clean.py" "$f" "$OUT/n$n.png" --median 3 --thresh 145 --scale 0.5
  "$T" "$OUT/n$n.png" "$OUT/n$n" --tessdata-dir "$TD" -l san --psm 4 >/dev/null 2>&1
  echo "$n $(wc -c < "$OUT/n$n.txt")"
done
