#!/usr/bin/python
import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
maxsum = []
m = arr
for i in range(6):
 for j in range(6):
  if(j+2<6 and i+2<6):
   temp_sum = m[i][j]+m[i][j+1]+m[i][j+2]+m[i+1][j+1]+m[i+2][j]+m[i+2][j+1]+m[i+2][j+2]
   #adds hourglass line by line 
   maxsum.append(temp_sum)
print max(maxsum)
