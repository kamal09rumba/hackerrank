#!/usr/bin/python
import sys


S = raw_input('enter a value :- \n').strip()
try:
	s = int(S)
	print s
except ValueError:
	#excepts valueError in our cass if string cann't convert into number
	print 'Bad String'	