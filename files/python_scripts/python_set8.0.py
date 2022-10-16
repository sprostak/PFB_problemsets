#!/usr/bin/env python3

import sys
import re

fa_dict = {}
input_file = sys.argv[1]

def fasta_parse(self):
	for line in self:
		if '>' in line:
			gene_id = line.rstrip('\n')
			fa_dict[gene_id] = ''
		else:
			seq = line.rstrip('\n')
			fa_dict[gene_id] += seq 

with open(input_file) as file_obj:
	fasta_parse(file_obj)

## from here below does not work. need to modify it so gene_id and nt counts are associated. Syntax error on line 30 as of 10-16-2022
comp_dict = {}
gene_comp = {}

for k,v in fa_dict.items():
	a_count = v.count('A')
	t_count = v.count('T')
	c_count = v.count('C')
	g_count = v.count('G')
	comp_dict[k] = ['A' a_count, 'T' t_count,'C' c_count, 'G' g_count]

print(comp_dict)


