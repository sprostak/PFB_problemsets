#!/usr/bin/env python3

## SMP 10-13-2022

fa_dict = {}

with open('/Users/student/programming_repository/files/pset_files/test.fasta', 'r') as file_obj:
	for line in file_obj:
		if '>' in line:
			gene_id = line.rstrip('\n')
		else:
			seq = line.rstrip('\n')
			fa_dict[gene_id] = seq
		





