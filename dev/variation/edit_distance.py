import sys
import panphon.distance

f = open(sys.argv[1]).readlines()

dst = panphon.distance.Distance()

print("word1\tipa1\tword2\tipa2\tfast_levenshtein_distance\tdogol_prime_distance\tfeature_edit_distance\thamming_feature_edit_distance\tweighted_feature_edit_distance")

for line in f:
	line = line.strip().split('\t')

	w1 = line[0]
	w2 = line[2]
	ipa1 = line[1]
	ipa2 = line[3]

	fast_levenshtein_distance = dst.fast_levenshtein_distance(ipa1, ipa2)
	dogol_prime_distance = dst.dogol_prime_distance(ipa1, ipa2)
	feature_edit_distance = dst.feature_edit_distance(ipa1, ipa2)
	hamming_feature_edit_distance = dst.hamming_feature_edit_distance(ipa1, ipa2)
	weighted_feature_edit_distance = dst.weighted_feature_edit_distance(ipa1, ipa2)

	print('\t'.join([w1, ipa1, w2, ipa2, str(fast_levenshtein_distance), str(dogol_prime_distance), str(feature_edit_distance), str(hamming_feature_edit_distance), str(weighted_feature_edit_distance)]))