#!/bin/bash

# 1297	r [ i -> e ] #	0.5	# l [ i -> ì ] c c a r [ i -> e ] #
# 412	t [ u -> o ] #	0.0	# [ c -> ç ] i a t [ u -> o ] #

frequency_bound=5

if [[ $2 != "" ]]; then
	frequency_bound=$2
fi

first="true"
echo "[ ?* | ["
for line in `cat $1 | tr ' ' '@' | tr '\t' '%'`; do 
	f=$(echo $line | cut -f1 -d'%')
	if [[ ${f} -lt ${frequency_bound} ]]; then
		break	
	else
		if [[ ${first} == "true" ]]; then
			first="false";
		else
			echo " .o.";
		fi
	fi
	echo ${line} | tr '%' '\t' | tr '@' ' ' | cut -f2,3 | sed 's/^/  [ [ ?* /g' | sed 's/\t/ ?* ]::/g' | sed 's/$/ ]/g' | python3 -c 'import sys; sys.stdout.write(sys.stdin.read().replace("# ?*", ".#.").replace("?* #", ".#."));' | tr -d '\n'

#| sed 's/\?\* #/.#./g' | sed 's/# \?\*/.#./g'
done
echo ""
echo "] ]"

# Now compile with: hfst-regexp2fst -S -o
