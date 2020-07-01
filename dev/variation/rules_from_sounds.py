import sys
import panphon.distance

f = open(sys.argv[1]).readlines()

dst = panphon.distance.Distance()
#print(f)
for i in f:
	i = i.strip()
	for j in f:
		j = j.strip()
		if(i == j):
			#print("hello")
			continue
		else:
			#print(i,j)
			weighted_feature_edit_distance = dst.weighted_feature_edit_distance(i, j)
			if(weighted_feature_edit_distance <= 0.5):
				print("[[ ", i, " -> ", j, " ]]", "\t", weighted_feature_edit_distance)
