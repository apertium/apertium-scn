import panphon.distance

f = open('scn-ipa.tsv').readlines()

dst = panphon.distance.Distance()

word_ipa = []
for line in f:
	#print(line)
	line = line.strip().split('\t')
	if(len(line) < 2):
		continue

	word = line[0].strip()
	ipa = line[1].strip()
	word_ipa.append([word,ipa])

for i in word_ipa:
	for j in word_ipa:
		if(i == j):
			continue
		fast_levenshtein_distance = dst.fast_levenshtein_distance(i[0], j[0])
		if (fast_levenshtein_distance < len(i[0])):
			weighted_feature_edit_distance = dst.weighted_feature_edit_distance(i[1], j[1])
			
			if(weighted_feature_edit_distance <= 0.5):
				print('\t'.join([i[0], i[1], j[0], j[1], str(fast_levenshtein_distance), str(weighted_feature_edit_distance)]))
