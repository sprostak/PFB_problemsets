#!/usr/bin/env python3

import sys

test_value =int(sys.argv[1])


if test_value == 20:                    ##this block prints only if the test value is equal to 20
	message = "matches 20"
	print(test_value,message)
else:                                  ##this block will print if the test value does not equal 20 exactly
	message = "does not match 20"
	print(test_value,message)


 
 
if test_value > 0:                ##this block will see if the test value is postivie, if positve other tests will be done
	message = "is positive"
	print(test_value,message)
	if test_value < 50:       ##this block will resturn if the test value is positive and less than 50
		message = "is positive and less than 50"
		print(test_value,message)
	if test_value < 50 and test_value/2 == True:        ##this block will return if the test value is positive, less than 50 and even
		message = "is positive, less than 50, and is even"
		print(test_value,message)
	elif test_value > 50:          ##this block will return if the test value is positive and greater than 50
		message = "is positive and larger than 50"
		print(test_value,message)
		if test_value/3:       ##this block will return if the test value is positive, less than 50, and divisible by 3
			message = "is positive, larger than 50, and divisible by 3"
			print(test_value,message)
elif test_value < 0:      ##this block will return if the test value is negative
	message = "is negative"
	print(test_value,message)
else:       ##this block will return if the test value is zero
	print("Test value is 0")

