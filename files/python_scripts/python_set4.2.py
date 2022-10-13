#!/usr/bin/env python3

## SMP 10-12-2022

count = 1
n = 1

while n <=1000:
	count = count * n 
	n = n + 1

print(f'Factorial of 1000 done')


list1 = [101,2,15,22,95,33,2,27,72,15,52]

for element in list1:
	if element % 2 == 0:
		print(element)

sorted_list1 = sorted(list1 , key=None)
print(sorted_list1)

evens = []
odds =[]

for i in sorted_list1:
	if i % 2 == 0:
		evens.append(i)
	if i % 2 != 0:
		odds.append(i)

print(f'the sum of evens is: {sum(evens)}')
print(f'the sum of odds is: {sum(odds)}')


for x in range(100):
	print(x+1)

list2 = [y for y in range(100)]
print(list2)







