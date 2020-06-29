f = open('cdiffs_with_weights.tsv').readlines()


for line in f[1:]:
	line = line.strip().split('\t')

	#change = line[0].split(' ')
	#change = ''.join(change)



	print(line[0].strip() + '\t' + str(float(line[1])))

