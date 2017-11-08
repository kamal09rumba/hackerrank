#!/usr/bin/python

import sys

def factorial(n):
 num=1
 if n<2:
  return num
 else:
  for i in range(n,0,-1):
   num *= i
  return num

if __name__ == "__main__":
 n=int(raw_input('enter a number\n').strip())
 result = factorial(n)
 print str(n)+'! = '+str(result)
