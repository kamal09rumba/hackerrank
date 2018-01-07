#!/usr/bin/python

#### Task 
# A Node class is provided for you in the editor. 
# A Node object has an integer data field, 'data' , and a Node instance pointer, 'next' , pointing to
# another node (i.e.: the next node in a list).

import sys

class Node:
	def __init__(self,data):
		self.next = None
		self.data = data
class Solution:
	def insert(self,head,data):
		p = Node(data)
		if head == None:
			head = p
		elif head.next == None:
			head.next = p
		else:
			start = head
			while (start.next != None):
				start = start.next
			start.next = p
		return head

	def display(self,head):
		current = head
		while current:
			print current.data
			current = current.next
	def removeDuplicates(self,head):
		# print vars(head)
		prev = head
		s    = set()
		s.add(prev.data)
		cur  = prev.next
		while cur:
			if cur.data in s:
				prev.next = cur.next
			else:
				s.add(cur.data)
				prev = cur
			cur = cur.next
		return head 
""" # another solution
		current = check = head
		while current:

			while check.next is not None:
				if check.next.data == current.data:
					check.next = check.next.next
				else:
					check = check.next
			current = check = current.next
		return head
"""
mylist= Solution()
T=int(input())
# T = 6
head=None
# data = [1,2,2,3,3,4]
for i in range(T):
    data=int(input())
    # head=mylist.insert(head,data[i])
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);