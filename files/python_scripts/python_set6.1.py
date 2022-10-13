#!/usr/bin/env python3

seq_dict = {}

with open('/Users/student/programming_repository/files/pset_files/Python_06.seq.txt', 'r') as seq_file:
	for line in seq_file:
		gene_id,seq = line.split() ##splits on white space
		seq_dict[gene_id] = seq

for gene_id in seq_dict:
	dna = seq_dict[gene_id]
	dna_hold1 = dna.replace('A', 'w')
	dna_hold2 = dna_hold1.replace('T', 'x')
	dna_hold3 = dna_hold2.replace('C', 'y')
	dna_hold4 = dna_hold3.replace('G', 'z')
	dna_hold5 = dna_hold4.replace('w', 'T')
	dna_hold6 = dna_hold5.replace('x', 'A')
	dna_hold7 = dna_hold6.replace('y', 'G')
	dna_comp = dna_hold7.replace('z','C')
	dna_revcomp = dna_comp[::-1]

print(f'>{gene_id} revcomp\n{dna_revcomp}')



