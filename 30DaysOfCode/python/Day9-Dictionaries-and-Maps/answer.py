#!/usr/bin/python

import sys
n = int(raw_input('Enter an integer:\n').strip())
phoneBook = []
for i in range(1,n+1):
 si = str(raw_input('enter space seperated name and number\n'))
 so = si.split()
 #print so
 value = so[0],so[1]
 phoneBook.append(value)
#print dict(phoneBook)
phoneBook = dict(phoneBook) # dict() constructor builds dictionaries directly from sequences of key-value pairs
for i in range(1,n+1):
 query = str(raw_input('query??\n')) 
 if query in phoneBook:
  print query+'='+ phoneBook[query]
 else:
  print 'Not found'
