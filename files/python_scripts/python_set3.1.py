#!/usr/bin/env python3

## second file of python mod 3 problem set 1
## SMP 10-12-2022

import sys



user_input = sys.argv[1] ##this will take the dna sequence is pasted in the command line when running this script file and store it
dna = user_input.upper() ##this will make dna seq all uppercase

## lines 14-22 calculate dna seq length, individual nt counts regardless of case, and AT and GC % regardless of case
## line 22 is a sanity check to make sure AT+GC is 100%
dna_length = len(dna)
a_count = dna.count('A')
t_count = dna.count('T')
c_count = dna.count('C')
g_count = dna.count('G')

dna_at_content = ((a_count + t_count)/dna_length) * 100
dna_gc_content = ((c_count + g_count)/dna_length) * 100
Total = dna_at_content + dna_gc_content

## lines 26-30 print the results of the AT and GC % surrounded by lines of asteriks to delineate the text on the command line
print(f'*\n*\n*\n*')
print(f'''The AT contnet of dna is: {dna_at_content}
The GC content of dna is: {dna_gc_content}
The total of dna content is: {Total}''') 
print(f'*\n*\n*\n*')


dna_subset = dna[101:202] ## this line stores nts 100-200 from dna into a new variable

## lines 36-38 print the result of pulling nts 100-200 from dna surrounded by lines of asteriks to delineate on command line
print(f'''Nucleotides 100-200 are:
{dna_subset}''')
print(f'*\n*\n*\n*')


## lines 42-50 change each nt in dna to a new unique character, chnages the unique character to the corresponding nt's complement
## the dna complement is stored in the dna_comp variable and is completed once all ys (which originally were Ts) are Gs
## the reverse complement is stored in the dna_revcomp variable and just the revers of the dna_comp variable
dna_hold1 = dna.replace('A', 'w')
dna_hold2 = dna_hold1.replace('T', 'x')
dna_hold3 = dna_hold2.replace('C', 'y')
dna_hold4 = dna_hold3.replace('G', 'z')
dna_hold5 = dna_hold4.replace('w', 'T')
dna_hold6 = dna_hold5.replace('x', 'A')
dna_hold7 = dna_hold6.replace('y', 'G')
dna_comp = dna_hold7.replace('z','C')
dna_revcomp = dna_comp[::-1]

## lines 55-57 print the reverse compliment delinated on the command line from other data by astriks
print(f'''The reverse complement of dna is:
{dna_revcomp}''')
print('*\n*\n*\n*')






