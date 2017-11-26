### Task ### 
#Given a base-10 integer,n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

#!/usr/bin/python

import sys

n = int(raw_input('Enter Decimal Number:-\n').strip())
binary = []
while ( n>0):
 r = n%2
 n = n/2
 binary.append(r)
binary = binary[::-1]
print binary
count = 0
lastdigit = 0
cone = []
for i in binary:
 if i == 1:
   if lastdigit == 1:
    count = count+1 ##counts max consecutive number
   elif lastdigit == 0:
    count = 1 ## reset counter
   else:
    count += 1 ## max consecutive number is 1
 else:
  cone.append(count)
 lastdigit = i 
#print max(cone)
if not cone:
 print count
else:
 if max(cone)>count:
  print max(cone)
 else:
  print count 
