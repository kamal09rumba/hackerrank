#!/usr/bin/python

#Given a square matrix of size 'NxN' , calculate the absolute difference between the sums of its diagonals.

import sys
n=int(raw_input().strip())
a=[]
for a_i in xrange(n):
 a_temp=map(int,raw_input().strip().split(' '))
 a.append(a_temp)
l = len(a)
count=0
count_rev=l-1
pd=0
sd=0
for i in a:
 pd+=i[count]
 sd+=i[count_rev]
 count+=1
 count_rev-=1
print 'sum of primary diagonal = ', pd
print 'sum of secondary diagonal = ', sd
print 'Difference: ',abs(pd-sd)
