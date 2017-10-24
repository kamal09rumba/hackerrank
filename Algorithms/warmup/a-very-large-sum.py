#!/usr/bin/python

##Input Format
#The first line of the input consists of an integer 'N'. The next line contains 'N'  space-separated integers contained in the array.
##Output Format
#Print a single value equal to the sum of the elements in the array.


import sys
def aVeryBigSum(n, ar):
    # Complete this function
    return sum(ar)
    #result = 0
    #for i in ar:
    #    result += i
    #return result

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
