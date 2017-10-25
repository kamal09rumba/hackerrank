#!/usr/bin/python

#Print the elements of array A in reverse order as a single line of space-separated numbers.

import sys

n=int(raw_input('Enter an integer').strip());
arr=map(int,raw_input('enter space seperate integers: ').strip().split(' '))
j=''
for i in arr[::-1]:
 j += str(i)+' '
print j
