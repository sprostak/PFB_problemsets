#!/usr/bin/env python3

## SMP 10-13-2022

import re


## open the fasta file of interest
## NOTE: this code may be slow for long fasta files as the .read() method is used on the file object

with open('/Users/student/programming_repository/files/pset_files/Python_07_ApoI.fasta' , 'r') as file_obj:
	line_list = file_obj.readlines()    ## read the lines of the fasta file into a list and store the list in a variable
	print(f'The file list is: {line_list}\n\n\n') 

	for line in line_list: ## iterate over each element (i.e., line) in the file list
		line = line.rstrip('\n') ## remove the new line characters from each line in the file
		matches = re.findall(r'([AG])(AATT[CT])' , line) ## finds the restriction sequence in each line, returns list
		print(f'''
matches list for line: {matches}

number of restriction sites for line: {len(matches)}
''' )
		cut_seq = re.sub(r'([AG])(AATT[CT])', r'\1^\2', line)
		caret_count = cut_seq.count('^')
	
	print(f'Number of ^ in new seq: {caret_count}')

	print(f'''
matches list: {matches}

number of restriction sites: {len(matches)}
''' )

print(f'Number of ^ in new seq: {caret_count}')

frags = cut_seq.split('^')
print(frags)

	

