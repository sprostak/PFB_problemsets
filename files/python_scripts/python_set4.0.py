#!/usr/bin/env python3

import sys

## SMP 10-12-2022

fave_things = ['dogs','cats', 'lions', 'tigers' , 'fat-bears']

print(f'OG list: {fave_things}')
print(f'OG middle element: {fave_things[2]}')

fave_things[2] = 'corn'

print(f'New list: {fave_things}')

fave_things.append('purple')

print(f'New list: {fave_things}')

fave_things.insert(0, 'ghosts')

print(f'New list: {fave_things}')

fave_things.insert(2, 'frogs')

print(f'New list: {fave_things}')

fave_things.pop()

print(f'New list: {fave_things}')

fave_things.pop(0)

print(f'New list: {fave_things}')

fave_things.pop(3)

print(f'New list: {fave_things}')

print(type(','.join(fave_things)))





