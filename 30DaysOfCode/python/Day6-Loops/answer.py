#!/usr/bin/python

#Task 
#Given an integer, 'n' , print its first '10'  multiples. Each multiple 'nxi'  (where 1<=i<=10 ) should be printed on a new line in the form: n x i = result.


n=int(raw_input('Enter an integer :'))

print 'Using for loop:'
for i in range(1,11):
 result = n*i
 print str(n)+' x '+str(i)+' = '+str(result)

print 'Using while loop: '
x=0
while(x<10):
 x=x+1
 result=n*x
 print str(n)+' x '+str(x)+' = '+str(result)

