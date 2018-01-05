#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
class BubbleSort:
    def __init__(self):
        self.numSwaps = 0
        self.array    = []
    def swap(self,n,a):
    	arrayLength = len(a)
        lastUnsorted =  arrayLength-1
        isSorted    = False
        while isSorted != True:
            isSorted = True
            for i in range(lastUnsorted):
                if a[i]>a[i+1]:
                    a[i],a[i+1] = a[i+1],a[i]
                    self.numSwaps += 1
                    isSorted = False
            lastUnsorted -= 1
            # since last element of array after swap is largest.
            # so , we can decrease the range for looping process
        self.array = a
obj = BubbleSort()
obj.swap(n,a)
print "Array is sorted in {} swaps.".format(obj.numSwaps)
print "First Element: {}".format(obj.array[0])
print "Last Element: {}".format(obj.array[n-1])