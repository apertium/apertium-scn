cut -f 1 variation/scn-ipa.wikt-seq2seq | sed -e 's/\(.\)/\1 /g' > foo
cut -f 3 variation/scn-ipa.wikt-seq2seq | sed -e 's/\(.\)/\1 /g' > bar
iconv -f utf-8 -t latin1 foo > fool
iconv -f utf-8 -t latin1 bar > barl
wdiff -n fool barl | iconv -f latin1 -t utf-8 | sed -e 's/-] {+/ -> /g' -e 's/-]/ -> 0 ]/g' -e 's/{+/[ 0 -> /g' -e 's/\[-/[ /g' -e 's/+}/ ]/g' > variation/repls.regex
