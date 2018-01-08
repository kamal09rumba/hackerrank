#!/usr/bin/python

import sys

class CheckPrimeNumber:
	def checkPrime(self,num):
	    for i in range(2,num):
	        if num%i == 0:
	    		return 'Not Prime'
	    return 'Prime'    
T = int(raw_input().strip())
for i in range(T):
    number = int(raw_input().strip())
    obj    = CheckPrimeNumber()
    res	   = obj.checkPrime(number)
    print res
    