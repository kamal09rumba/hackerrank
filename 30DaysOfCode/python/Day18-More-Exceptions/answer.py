#!/usr/bin/python

import sys

class Calculator:
	def power(self,n,p):
		if n>0 and p>0:
			return pow(n,p)
		else:
			raise Exception('n and p should be non-negative')

myCalculator = Calculator()
T = int(raw_input())
for i in range(T):
	n,p = map(int, raw_input().split())
	try:
		ans = myCalculator.power(n,p)
		print ans
	except Exception,e:
		print e