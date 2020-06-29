import sys
import panphon.distance

f = open(sys.argv[1]).readlines()

dst = panphon.distance.Distance()

print("word1\tipa1\tword2\tipa2\tfast_levenshtein_distance\tweighted_feature_edit_distance")

for line in f:
	line = line.strip().split('\t')

	w1 = line[0].strip()
	w2 = line[2].strip()
	ipa1 = line[1].strip()
	ipa2 = line[3].strip()

	if(w1 != w2):
		fast_levenshtein_distance = dst.fast_levenshtein_distance(w1, w2)
		weighted_feature_edit_distance = dst.weighted_feature_edit_distance(ipa1, ipa2)

		print('\t'.join([w1, ipa1, w2, ipa2, str(fast_levenshtein_distance), str(weighted_feature_edit_distance)]))