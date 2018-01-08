#!/usr/bin/python
import sys
## use Primality test to find prime number 
def checkPrime(num):
	if num == 1:
			return False
	else:
		square_root = int(num**0.5)
		for i in range(2,square_root+1):
			if (num%i == 0) and (num != i):
				return False
		return True
T = int(raw_input())
for i in range(T):
	number = int(raw_input())
	if checkPrime(number):
		print "Prime Number"
	else:
		print "Not prime"
