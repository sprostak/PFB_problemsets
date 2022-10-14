#!/usr/bin/env python3
## SMP 10-14-2022
import re

fa_dict = {}

with open('/Users/student/programming_repository/files/pset_files/Python_07_ApoI.fasta' , 'r') as file_obj:

## lines 12-18 sort through the inputed fasta file and store gene ids and their seqs in a dict
	for line in file_obj:
		if '>' in line:
			gene_id = line.rstrip('\n')
			fa_dict[gene_id] = ''
		else:
			seq = line.rstrip('\n')
			fa_dict[gene_id] += seq 

print(fa_dict)  	
carat_dict = {}

## lines 25-?? add carats at the ApoI cut sites for each sequence from the input fasta file
for gene in fa_dict:
		carat_dict[gene] = ''
		seq = fa_dict[gene]
		rest_sites = re.findall(r'([AG])(AATT[CT])', seq)
		print(f'\nThe number of restriction sites in {gene} is: {len(rest_sites)}')
		carat_seq = re.sub(r'([AG])(AATT[CT])', r'\1^\2', seq)
		print(f"\nThe number of carats in {gene}'s carat seq is: {carat_seq.count('^')}")
		carat_dict[gene] += carat_seq
print(carat_dict)






