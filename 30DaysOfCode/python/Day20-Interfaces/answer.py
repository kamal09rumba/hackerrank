#!/usr/bin/python
import sys
# calculates the sum of divisor of a number
number = int(raw_input('Enter a number :- \n'))

sum = 0
for i in range(1,number+1):
	if number%i == 0:
		# print number%i,i
		sum += i
print sum