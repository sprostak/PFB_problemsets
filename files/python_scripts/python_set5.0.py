#!/usr/bin/env python3

## SMP 10-13-2022

import sys

fav_dict = {'dog' : 'husky', 'cat' : 'cole', 'tree' : 'pine', 'band' : 'Paramore'}
keys = list(fav_dict.keys())

print(f'''My fave dog from dict: {fav_dict['dog']}''')

fav_thing = 'cat'
print(f'''My fave thing called from variable: {fav_dict[fav_thing]}''')


fav_dict['organism'] = 'Bd'
print(f'''Updated dict: {fav_dict}''')
fav_dict['organism'] = 'Spun'
print(f'''Changed value of organism: {fav_dict}''')

print('*\n*\n*\n*')

print(f'''The options for your favorite thing are:
{keys}''')
print('*\n*\n*\n*')

usr_key = input("Enter the category of  your favorite thing : ")
print(f'''The user key entered is: {usr_key}''')
print('*\n*\n*\n*')
print(f'''The value of the user key is: {fav_dict[usr_key]}''')


print('*\n*\n*\n*')
usr_value = input(f'''Enter the new value of {usr_key}: ''')

fav_dict[usr_key] = usr_value

print(f'''Your favorite {usr_key} is now {usr_value}''')
print(f'''Fav_dict is now: {fav_dict}''')




