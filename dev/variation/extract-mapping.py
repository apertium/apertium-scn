import sys

#z i t a ||| t s i t̪ a	0-0 1-2 2-3 3-4
#z i t t u ||| t s i t̪ t̪ u	0-0 1-2 2-3 3-4 4-5
#z i t u ||| t s i t̪ u	0-0 1-2 2-3 3-4
#z i u ||| t s i u	0-0 1-2 2-3
#z ù c c a r u ||| t s u k k a ɾ u	0-0 1-2 2-3 3-4 4-5 5-6 6-7

for line in sys.stdin.readlines():
	line = line.strip().replace('|||', '\t')

	row = line.split('\t')
	
	if len(row) != 3:
		print(row)
		continue
		
	orth = row[0].strip().split(' ')
	ipa = row[1].strip().split(' ')
	alig = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in row[2].strip().split(' ')]
	# ['z', 'u'] ['t', 's', 'u'] [(0, 0), (1, 2)]

	for (s, t) in alig:
		print(ipa[t], orth[s])
#	print(orth, ipa, alig)

	
