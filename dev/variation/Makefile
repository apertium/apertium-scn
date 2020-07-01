all: graph2phon.hfst
graph2phon.hfst: graph2phon.regex
	hfst-regexp2fst -S $< | hfst-fst2fst -w -o $@
