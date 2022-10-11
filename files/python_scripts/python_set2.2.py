#!/usr/bin/env python3

import sys

test_list = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]


for i in test_list:
	if i > 0:
		message = "is positive"
		print(i,message)
		if i < 50:
			message = "is positive and less than 50"
			print(i,message)
		if i < 50 and i/2 == True:
			message = "is positive, less than 50, and even"
			print(i,message)
		if i > 50:
			message = "is positive and greater than 50"
			print(i,message)
		if i > 50 and i/3 == True:
			message = "is positive, greater than 50, and divisible by 3"
			print(i,message)
	elif i <0 :
		message = "is negative"
		print(i,message)
	else:
		message = "is zero"
		print(i,message)
