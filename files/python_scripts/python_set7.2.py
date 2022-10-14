#!/usr/bin/env python3

## SMP 10-13-2022

import re

fa_dict = {}

with open('/Users/student/programming_repository/files/pset_files/test.fasta', 'r') as file_obj:
	for line in file_obj:
		if '>' in line:
			gene_id = re.search(r'>(\w+\s.*)', line)
			matches = gene_id.groups()
		else:
			seq = line.rstrip('\n')			
			fa_dict[matches[0]] = seq

print(fa_dict)


