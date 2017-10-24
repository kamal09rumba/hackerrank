#!/usr/bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(raw_input().strip())
def main():
    s = str(raw_input().strip())
    count=0
    evens=''
    odds=''
    for i in s:
        if(count%2==0):
            evens+=i
        else:
            odds+=i
        count+=1
    #print evens+' '+odds
    return evens+' '+odds
    #return evens,odds
for i in range(0,n):
    print(main())
    #j=main()
    #print j[0]+' '+j[1]
