# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/python
import sys

phoneBook = []
n = int(raw_input('').strip())
for i in range(1,n+1):
    si=str(raw_input(''))
    so=si.split()
    value = so[0],so[1]
    phoneBook.append(value)
phoneBook = dict(phoneBook)
for j in range(1,n+1):
    query = str(raw_input(''))
    if query in phoneBook:
        print query+'='+phoneBook[query]
    else:
        print 'Not found'
