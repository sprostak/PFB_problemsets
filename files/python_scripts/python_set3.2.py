#!/usr/bin/env python3

import sys

##SMP 10-12-2022

user_input = sys.argv[1] ## stores user input dna seq as a variable
dna = user_input.upper() ## ignores case in dna seq from command line user input, all nts are capital when using dna variable

r_seq = "GAATTC"

r_cut_site = dna.find(r_seq)
r_cut_nuc = r_cut_site + 1

print(r_cut_site)

print(f'EcoRI will cut after nt {r_cut_nuc} which is {dna[r_cut_site]}' ) 



