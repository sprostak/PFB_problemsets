#!/usr/bin/env python3

## SMP 10-12-2022

taxa = ['sapiens', 'erectus','neanderthanlenis']

print(taxa)

print(f'The second element of taxta is: {taxa[1]}')


print(type(taxa))  ## prints the variable type that taxa is, which is a list

species = ", ".join(taxa)

print(species)


print(type(",".join(taxa)))

print(species[1])

type(species)

sorted_list_alpha = sorted(taxa, key=str.lower, reverse=False)

print(sorted_list_alpha)

sorted_list_length = sorted(taxa, key=len, reverse=False)
print(sorted_list_length)
