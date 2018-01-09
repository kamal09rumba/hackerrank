#!/usr/bin/python

import sys
from datetime import date
class Library:
	def calculate(self,returnDate,dueDate):
		returnDate = date(returnDate[2],returnDate[1],returnDate[0])
		dueDate    = date(dueDate[2],dueDate[1],dueDate[0])
		fine = 0
		days = 0
		if returnDate > dueDate:
			if returnDate.year == dueDate.year:
                if returnDate.month == dueDate.month:
                    fine = 15*(returnDate.day - dueDate.day)
                else:
                    fine = 500*(returnDate.month - dueDate.month)
            else:
				fine = 10000
		return fine

returnDate = map(int,raw_input().split())
dueDate    = map(int,raw_input().split())
obj = Library()
res = obj.calculate(returnDate,dueDate)
print res