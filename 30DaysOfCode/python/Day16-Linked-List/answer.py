#!/usr/bin/python
import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    # class solution is gonna wrap our head i.e. not all the element on node
    # can access the head directly
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next	
    def insert(self,head,data):
    	if head is None:
    		head = Node(data)
    	else:
    		current = head
            # walk through the end of the linked list.
            # How do we know that we are not at the end of the linked list??
            # well, as long as there's something after the linked list
    		while current.next != None:
    			current = current.next
    		current.next = Node(data)
    	return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
