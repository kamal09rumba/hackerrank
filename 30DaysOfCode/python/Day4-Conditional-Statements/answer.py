#!/usr/bin/python
import sys
N=int(raw_input('Enter A Valid Number: ').strip())
if(N%2==1):
 print 'Odd Number'
elif(N%2==0 and N<=5):
 print 'even number but inside the range of 5'
elif(N%2==0 and 5<N<=20):
 print 'even number but inside the range of 5 to 20'
elif(N%2==0 and N>20):
 print 'even number but number is greater then 20'
