#!/usr/bin/env python3

## SMP 10-13-2022

import re


with open('/Users/student/programming_repository/files/pset_files/Python_07_Nobody.txt', 'r') as file_obj, open('/Users/student/programming_repository/files/pset_files/Josh.txt', 'w') as out_file:
	file_string = file_obj.read()
	re.findall('Nobody', file_string)
	replace_string = file_string.replace("Nobody","Josh")
	out_file.write(replace_string)

print(f'Found all Nobodys!')
print(f'Replaced all Nobodys!')
print(f'Wrote new poem to file!')
