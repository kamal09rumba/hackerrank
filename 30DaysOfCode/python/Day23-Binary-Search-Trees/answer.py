#!/usr/bin/python

## Binary Search Tree ##
# left node <= root node <= right node
import sys

class Node:
	def __init__(self,data):
		self.left = self.right = None
		self.data = data
class Solution:
	def insert(self,root,data):
		if root is None:
			root = Node(data)
		else:
			#comparing prev node data with new data
			if data <= root.data:
				cur 	   = self.insert(root.left,data)
				root.left  = cur
			else:
				cur        = self.insert(root.right,data)
				root.right = cur
		return root
	def getHeight(self,root):
		if root:
			height = 0
			left   = 0
			right  = 0
			if root.left:
				left  = 1+self.getHeight(root.left)
			if root.right:
				right = 1+self.getHeight(root.right)
			height = max(left,right)
			return height
		else:
			return 0
T 		= int(raw_input())
myTree  = Solution() 
root	= None
for i in range(T):
	data = int(raw_input())
	root = myTree.insert(root,data)
height = myTree.getHeight(root)
print height

