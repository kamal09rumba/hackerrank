#!/usr/bin/python

import sys

from abc import ABCMeta, abstractmethod

class Book:
	__metaclass__ = ABCMeta

	def __init__(self,title,author):
		self.title = title
		self.author = author
	@abstractmethod
	def display(self):
		pass

class MyBook(Book):
	def __init__(self,title,author,price):
		super(MyBook,self).__init__(title,author)
		#Book.__init__(self,title,author)
		self.price = price
	def display(self):
		print 'Title: {}'.format(self.title)
		print 'Author: {}'.format(self.author)
		print 'Price: {}'.format(self.price)

title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()