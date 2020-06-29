#!/bin/bash
input="./variation/scn-ipa.wikt-uniq-distances.tsv"

while IFS= read -r line
do
  echo "$line" > tempfile
  #cat tempfile
  cut -f 1 tempfile | sed -e 's/\(.\)/\1 /g' > foo
  cut -f 3 tempfile | sed -e 's/\(.\)/\1 /g' > bar
  iconv -f utf-8 -t latin1 foo > fool
  iconv -f utf-8 -t latin1 bar > barl

  #cat fool
  #cat barl
  wdiff -n fool barl | iconv -f latin1 -t utf-8 | sed -e 's/-] {+/ -> /g' -e 's/-]/ -> 0 ]/g' -e 's/{+/[ 0 -> /g' -e 's/\[-/[ /g' -e 's/+}/ ]/g' > temp2
  #cat temp2
  cut -f 5,6 tempfile > temp_weights
  paste temp2 temp_weights > final_temp

  rm tempfile foo bar fool barl temp2 temp_weights

  cat final_temp

done < "$input"


#cut -f 1 variation/scn-ipa.wikt-seq2seq | sed -e 's/\(.\)/\1 /g' > foo
#cut -f 3 variation/scn-ipa.wikt-seq2seq | sed -e 's/\(.\)/\1 /g' > bar
##iconv -f utf-8 -t latin1 foo > fool
#iconv -f utf-8 -t latin1 bar > barl
#wdiff -n fool barl | iconv -f latin1 -t utf-8 | sed -e 's/-] {+/ -> /g' -e 's/-]/ -> 0 ]/g' -e 's/{+/[ 0 -> /g' -e 's/\[-/[ /g' -e 's/+}/ ]/g' > variation/repls.regex
