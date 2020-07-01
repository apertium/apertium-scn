all: graph2phon.hfst scn2ipa.hfst
graph2phon.hfst: graph2phon.regex
	hfst-regexp2fst -S $< | hfst-fst2fst -w -o $@

%.hfst: %.twol
	hfst-twolc --resolve $< -o $@
