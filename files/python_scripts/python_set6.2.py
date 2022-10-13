#!/usr/bin/env python3


num_lines = 0
char_total = 0

with open('/Users/student/programming_repository/files/pset_files/test.fastq' , 'r') as seq_file:
	for line in seq_file:
		line = line.rstrip('\n')
		num_lines += 1	
		char_per_line = len(line)	
		char_total += char_per_line
		print(f'The number of characters in line is : {char_per_line}')

avg_line_len = char_total/num_lines


print(f'The number of lines in the file is: {num_lines}')
print(f'The total number of characters is: {char_total}')
print(f'The avg length of a line is: {avg_line_len}')


