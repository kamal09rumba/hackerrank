#!/usr/bin/python

#We define the rating for Alice's challenge to be the triplet A=(a0,a1,a2) , 
# and the rating for Bob's challenge to be the triplet B=(b0,b1,b2).

#Your task is to find their comparison points by comparing 'a0' with 'b0' , 'a1'  with 'b1' ,and 'a2' with 'b2'.

#If 'ai>bi', then Alice is awarded  point.
#If 'ai<bi', then Bob is awarded  point.
#If 'ai==bi', then neither person receives a point.


import sys

def solve(a0,a1,a2,b0,b1,b2):
 a = 0
 b = 0
 if(a0>b0):
  a = a+1
 elif(a0<b0):
  b = b+1
 else:
  a=a
  b=b
 if(a1>b1):
  a=a+1
 elif(a1<b1):
  b=b+1
 else:
  a=a
  b=b
 if(a2>b2):
  a=a+1
 elif(a2<b2):
  b=b+1
 else:
  a=a
  b=b
 return a,b

a0,a1,a2= raw_input('Enter 3 space-seperated integer:').strip().split(' ')
a0,a1,a2= [int(a0),int(a1),int(a2)]
b0,b1,b2= raw_input('Enter 3 space-seperated integer:').strip().split(' ')
b0,b1,b2= [int(b0),int(b1),int(b2)]
result = solve(a0,a1,a2,b0,b1,b2)
print " ".join(map(str,result))
