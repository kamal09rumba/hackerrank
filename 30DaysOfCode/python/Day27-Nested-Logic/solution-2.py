#!/usr/bin/python

import sys
from datetime import date
class Library:
	def calculate(self,return_date,due_date):
		return_date 	  = return_date.split()
		due_date    	  = due_date.split()
		return_date_year  = int(return_date[2])
		return_date_month = int(return_date[1])
		return_date_day   = int(return_date[0])
		due_date_year     = int(due_date[2])
		due_date_month    = int(due_date[1])
		due_date_day      = int(due_date[0])

		return_date = date(return_date_year,return_date_month,return_date_day)
		due_date    = date(due_date_year,due_date_month,due_date_day)
		days		= return_date - due_date
		days		= days.days
		fine 		= 0

		#book is returned before expected date so no fine is charged
		if days < 0:
			return fine
		else:
			if return_date_year == due_date_year:
				if return_date_month == due_date_month:
					fine = 15*days
					return fine
				else:
					fine = 500*(return_date_month-due_date_month)
					return fine
			else:
				fine = 10000
				return fine

# return_date = raw_input()
return_date = '9 6 2015'
# due_date	= raw_input()
due_date	= '6 6 2015'
obj = Library()
res = obj.calculate(return_date,due_date)
print res