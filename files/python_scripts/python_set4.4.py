#!/usr/bin/env python3

## SMP 10-12-2022


list1 =  ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for i in list1:
	print(i)
	print(len(i), i, sep='\t') 
	
list2 = [(len(i),i) for i in list1]
print(list2) 

list3 = [(list1.index(i), len(i), i) for i in list1]
print(list3)





