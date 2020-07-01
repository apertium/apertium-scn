# Extract bi-/trigrams, frequency and lowest weight 

# Input:
#! # z ù c c [ a r -> 0 ] u [ 0 -> r o ] #	2.0
#! # z [ ù -> u ] c c [ a -> u ] r u #	1.25
#! # z ù c c [ a -> u ] r u #	1.0
#! # z ù c c [ h i -> u ] r u #	0.875

# Output:
# 1297	r [ i -> e ] #	0.5	# l [ i -> ì ] c c a r [ i -> e ] #
# 414	t [ u -> o ] #	0.0	# [ c -> 0 ] [ 0 -> ç ] i a t [ u -> o ] #
# 198	r [ u -> o ] #	0.0	# a b a c i u r r [ u -> o ] #
# 188	n [ u -> o ] #	0.0	# d a n n [ u -> o ] #
 
f=$(basename $1)
if [[ $2 == "2" ]]; then
	cat $1 | egrep -o -e '. \[[^]]*\]' -e '\[[^]]*\] .'  | sort -f | uniq -c | sort -gr  | sed 's/^ *//g' | sed 's/ /@/1' > /tmp/${f}.patterns
elif [[ $2 == "3" ]]; then
	cat $1 | egrep -o -e '. \[[^]]*\] .' | sort -f | uniq -c | sort -gr  | sed 's/^ *//g' | sed 's/ /@/1' > /tmp/${f}.patterns
elif [[ $2 == "1" ]]; then
	cat $1 | egrep -o -e '\[[^]]*\]' | sort -f | uniq -c | sort -gr  | sed 's/^ *//g' | sed 's/ /@/1' > /tmp/${f}.patterns
else
	echo "Specify unigrams bigrams or trigrams.";
	exit -1;
fi
for i in `cat /tmp/${f}.patterns | tr ' ' '_'`; do 
	w=`echo $i | cut -f2 -d'@' | tr '_' ' ' | sed 's/\[/\\\[/g' | sed 's/\]/\\\]/g'`; 
	cat ${f} | grep "$w" | awk -F'\t' '{print $2"\t"$1}' | sort -n | head -1 | sed "s/^/$i\t/g" | tr '_' ' ' | sed 's/@/\t/g' ;
done

# [ ?* | [ ?* g [ 0 -> h ] i ?* ]::1 ]
