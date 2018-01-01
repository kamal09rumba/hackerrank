#!/usr/bin/python

## Task 
#  Complete the Difference class by writing the following:

# -- A class constructor that takes an array of integers as a parameter and saves it to the elements  
#    instance variable.
# -- A computeDifference method that finds the maximum absolute difference between any 2 numbers 
#    in 'N' and stores it in the 'maximumDifference' instance variable.


import sys

class Difference:
	def __init__(self,a):
		self.a = a
	def computeDifference(self):
		diff     = []
		arr 	 = self.a
		arr_len  = len(arr)
		for i in range(arr_len):
			if i+1 < arr_len:
			 for j in range(i+1,arr_len):
			  diff.append(abs(arr[i]-arr[j]))
		# print(diff)
		self.maximumDifference = max(diff) 
_ = raw_input('Enter length of Array:-\n')
a = [int(e) for e in raw_input('Enter numbers :-\n').split(' ')]
d = Difference(a)
d.computeDifference()
print 'Maximum Difference between array element:-\n{}'.format(d.maximumDifference)