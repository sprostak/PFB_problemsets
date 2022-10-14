#!/usr/bin/env python3

##SMP 10-13-2022

import re


with open('/Users/student/programming_repository/files/pset_files/Python_07.fasta', 'r') as file_obj:
	for line in file_obj:
		if '>' in line:
			gene_id = re.search(r'>(\w{2}\S+)\s(.*)', line)
			matches = gene_id.groups()
			print(f'''\nid: {matches[0]}
desc: {matches[1]}''')

