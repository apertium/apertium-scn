import sys
import re

regex = r"\[ (.*) -> (.*) \]"
subst = "[ \\2 -> \\1 ]"

f = open(sys.argv[1]).readlines()

rules_done = set(())

for line in f:
	linet = line.strip().split('\t')
	rule = linet[1].strip()

	if(rule.strip() not in rules_done):
		rules_done.add(rule)
		print(line.strip())

	result = re.sub(regex, subst, rule, 0, re.MULTILINE)

	if(result.strip() not in rules_done):
		rules_done.add(result)
		print('\t'.join([linet[0], result, linet[2], linet[3]]))
