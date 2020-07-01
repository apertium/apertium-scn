import panphon.distance
import sys

def print_to_stderr(*a): 
  
    # Here a is the array holding the objects 
    # passed as the arguement of the function 
    print(*a, file = sys.stderr) 
  
print_to_stderr("Hello World") 

f = open(sys.argv[1]).readlines()

dst = panphon.distance.Distance()
count = 0

checked_set = set(())
words_done = set(())

word_ipa = []
for line in f:
	#print(line)
	line = line.strip().split('\t')
	if(len(line) < 2):
		continue

	word = line[0].strip().lower()
	ipa = line[1].strip()
	word_ipa.append([word,ipa])

total = len(word_ipa)

for i in word_ipa:
	count +=1
	print_to_stderr(float(count/total))
	for j in word_ipa:
		if(i[0] in words_done):
			continue
		if(i[0] == j[0]):
			continue
		fast_levenshtein_distance = dst.fast_levenshtein_distance(i[0], j[0])
		if (fast_levenshtein_distance < 5):
			weighted_feature_edit_distance = dst.weighted_feature_edit_distance(i[1], j[1])

			if((i[0]+'\t'+j[0]) in checked_set or (j[0]+'\t'+i[0]) in checked_set):
				continue
			else:
				checked_set.add(i[0]+'\t'+j[0])
			
			if(weighted_feature_edit_distance <= 1):
				
				words_done.add(j[0])
				print('\t'.join([i[0], i[1], j[0], j[1], str(fast_levenshtein_distance), str(weighted_feature_edit_distance)]))
