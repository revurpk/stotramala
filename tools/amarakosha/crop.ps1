# Copyright 2026 Pradyumna Revur — CC BY 4.0 (see LICENSE)
# Crop a window out of a full-size leaf of the 1882 print (archive.org 20231127_20231127_1402),
# for reading a doubtful akṣara. Coordinates are in the full scan (3066 × 4885). Nothing is committed.
# usage: crop.ps1 OUTDIR LEAF X Y W H
param([string]$Out, [int]$Leaf, [int]$X, [int]$Y, [int]$W, [int]$H)
Add-Type -AssemblyName System.Drawing
$src = Join-Path $Out ("n{0:D3}-full.jpg" -f $Leaf)
if (-not (Test-Path $src)) {
    Invoke-WebRequest -UseBasicParsing -UserAgent "stotramala-source/1.0" `
        -Uri "https://archive.org/download/20231127_20231127_1402/page/n${Leaf}_w3066.jpg" -OutFile $src
}
$img = [System.Drawing.Image]::FromFile($src)
$bmp = New-Object System.Drawing.Bitmap $W, $H
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.DrawImage($img, (New-Object System.Drawing.Rectangle 0, 0, $W, $H), (New-Object System.Drawing.Rectangle $X, $Y, $W, $H), [System.Drawing.GraphicsUnit]::Pixel)
$dst = Join-Path $Out ("crop-n{0:D3}-{1}-{2}.png" -f $Leaf, $X, $Y)
$bmp.Save($dst); $img.Dispose(); $bmp.Dispose()
$dst
