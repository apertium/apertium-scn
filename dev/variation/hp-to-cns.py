import sys, re, hfst

tf = hfst.HfstInputStream('graph2phon.hfst') 
af = hfst.HfstInputStream('../../scn.automorf.hfst') 
ipaify = tf.read() 
analyser = af.read() 

# cat scn.hitparade.txt  | sed 's/^ *//g' | sed 's/[AEIOUaeiouàèìòùÀÈÌÒÙ]/@/g' | cut -f2- -d' ' | grep -v ' ' | uconv -x lower | grep '^[aáàâbcçdđḍeéèêfghiíìîjklmnoóòôpqrsštuúùûvxyz@]\+$'  | sort -u  

dico = {}
#devowel = re.compile('[aáàâeéèêíìîoóòôuúùû]')

def degem(s):
	o = s
	for i in 'bcçdđḍfghjklmnpqrsštvxyz':
		o = o.replace(i+i, i)
	return o
		

for line in sys.stdin.readlines():
	line = line.strip()
	row = line.split(' ')
	if len(row) != 2:
		continue

	form = row[1].lower()
	
	k = re.sub('[aáàâeéèêíïiìîoóòôuúùû]', '@', form)
	k = degem(k)

	if k not in dico:
		dico[k] = []

	dico[k].append(form)

for k in dico:
	if len(dico[k]) <= 1:
		continue
	dico[k] = list(set(dico[k]))
	for x in dico[k]:
		print('%s\t%s\t%s' % (k, x, ipaify.lookup(x)[0][0]))
	
	
