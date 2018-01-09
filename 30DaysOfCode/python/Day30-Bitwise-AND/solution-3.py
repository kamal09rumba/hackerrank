#!/usr/bin/python

import sys
t = int(raw_input().strip())
for a0 in xrange(t):
	n,k = raw_input().strip().split()
	n,k = [int(n),int(k)]
	res = 0
	for i in range(1,n+1):
		for j in range(i+1,n+1):
			# print i,j
			cur = i&j
			if cur>res and cur<k:
				res = cur
	print res