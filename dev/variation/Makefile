all: graph2phon.hfst scn2ipa.hfst
graph2phon.hfst: graph2phon.regex
	hfst-regexp2fst -S $< | hfst-fst2fst -w -o $@

%.twol.hfst: %.twol
	hfst-twolc --resolve $< -o $@

%.lexc.hfst: %.lexc
	hfst-lexc $< -o $@

%.hfst: %.twol.hfst %.lexc.hfst
	hfst-compose-intersect -1 scn2ipa.lexc.hfst -2 scn2ipa.twol.hfst -o $@
