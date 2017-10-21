#!usr/bin/python

#input Format
#The first line contains an integer, , denoting the size of the array. 
#The second line contains  space-separated integers representing the array's elements.

#Output Format
#Print the sum of the array's elements as a single integer.

import sys

def simpleArraySum(n,ar):
# using python built-in function more details
# https://docs.python.org/2/library/functions.html#sum
# return sum(ar)
 j=0
 for i in ar:
  j=j+i
 return j
n  	= int(raw_input('enter an integer: ').strip())
ar 	= map(int,raw_input('enter N space-seperated integers: ').strip().split(' '))
result	= simpleArraySum(n,ar)
print(result) 

