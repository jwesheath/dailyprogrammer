#!/bin/bash

python3 life.py life000.txt

txtfiles=($(ls | grep .txt))

for name in ${txtfiles[@]}
do
  enscript -p ${name%.*}.ps $name --no-header
  ps2pdf ${name%.*}.ps ${name%.*}.pdf
  convert ${name%.*}.pdf -alpha off -quality 100% ${name%.*}.png
done

pngnames=()

for name in ${txtfiles[@]}
do
  pngnames+="${name%.*}.png "
done

convert -delay 50 ${pngnames[@]} -loop 0 animated.gif

rm *.txt *.ps *.pdf *.png
