#!/usr/bin/python

import sys
res = []
max_no = []
t = int(raw_input().strip())
for a0 in xrange(t):
	n,k = raw_input().strip().split()
	n,k = [int(n),int(k)]
	s   = range(1,n+1)
	for i in range(n):
		for j in range(n-(i+1)):
			# print s[i],s[i+j+1]
			# print s[i]&s[i+j+1]
			res.append(s[i]&s[i+j+1])
	max_no = sorted(l for l in res if l < k)
	print max_no
	del max_no[:]#clears list (i.e. empties the array max_no)
	del res[:]