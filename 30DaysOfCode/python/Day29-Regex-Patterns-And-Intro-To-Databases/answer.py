#!/usr/bin/python
import sys
import re
pat   = "@gmail.com$"
names = []
N = int(raw_input().strip())
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if(re.search(pat,emailID,re.IGNORECASE)):
        names.append(firstName)
for i in sorted(names):
    print i