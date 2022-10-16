#!/usr/bin/env python3

import re
import sys

enz_dict = {}

with open('/Users/student/programming_repository/files/pset_files/bionet.txt' , 'r') as file_obj:
	for i in range(9):
		next(file_obj)
	for line in file_obj:
		line = line.rstrip()
		enz_list = re.split(r'\s{2,}', line)
		if line:
			enz_ID = enz_list[0]
			enz_recseq = enz_list[1]
			enz_dict[enz_ID] = enz_recseq
			
input_enz = sys.argv[1]
input_file = sys.argv[2] ## file should be an absoulte path ideally to avoid errors

print(f'Selected enzyme: {input_enz}')
print(f'Selected file: {input_file}')

fa_dict = {}		

with open(input_file , 'r') as in_file:
	for line in in_file:
		if '>' in line:
			gene_id = line.rstrip('\n')
			fa_dict[gene_id] = ''
		else:
			seq = line.rstrip('\n')
			fa_dict[gene_id] += seq 

carat_dict = {}

## NOTE: below this is old code for only ApoI, not the input_enz as of 10-16-22. The code below needs to be modified to take any input enzyme.

## lines 21-28 add carats at the ApoI cut sites for each sequence from the input fasta file
## seqs with carats get stored into a new dict {carat_dict} with gene_id:carat_seq
for gene in fa_dict:				## iterate over each key in {fa_dict}, could be cleaned up by using fa_dict.items()
		carat_dict[gene] = ''		## creates an empty dict value in {carat_dict} for current gene
		seq = fa_dict[gene]			## defines the variable 'seq' as the value in {fa_dict} of the current gene
		rest_sites = re.findall(r'([AG])(AATT[CT])', seq)		## finds and stores all ApoI restriction sites present in 'seq' in a list variable [rest_sites]
		print(f'\nThe number of restriction sites in {gene} is: {len(rest_sites)}')			## prints the number of restriction sites found in current gene
		carat_seq = re.sub(r'([AG])(AATT[CT])', r'\1^\2', seq)	## places a ^ at the cut site within each restriction site in 'seq', stores result in new variable 'carat_seq'
		print(f"\nThe number of carats in {gene}'s carat seq is: {carat_seq.count('^')}\n")	## prints the number of carats in 'carat_seq'
		carat_dict[gene] += carat_seq		## adds the 'carat_seq' as the value of the current gene in {carat_dict}

## lines 31-40 fragment each carat seq at the ^, determines fragment length and sorts fragment from longest to shortesy
for gene in carat_dict:
	temp_seq = carat_dict[gene]
	frags = temp_seq.split('^')			## returns a list of fragments cut at every ^ in the carat_seq of the gene of interest
	n = 1														## create a variable to give each fragment a number id
	for frag in frags:							## iterate over the list of frgaments for the current gene
		frag_len = len(frag)					## get the length of each fragment
		print(f'The length of fragment {n} in {gene} is: {frag_len}')			## prints the length of each frag for current gene
		n += 1 												## add 1 to the frag number id for the current gene
		gel_frags = sorted(frags, key=len, reverse=True)									## sort OG list of frags for current gene by length (lg-sm)
	print(f'\nThe sorted fragments of {gene} are: {gel_frags}\n')				## print the sorted list for each gene



