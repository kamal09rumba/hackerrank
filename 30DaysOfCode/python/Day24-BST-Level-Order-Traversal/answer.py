#!/usr/bin/python

### Task #### 
# A level-order traversal, also known as a breadth-first search, visits each level of a tree's 
# nodes from left to right, top to bottom. You are given a pointer, 'root' , pointing to the root 
#of a binary search tree. Complete the levelOrder function provided in your editor so that
# it prints the level-order traversal of the binary search tree.

import sys

class Node:
	def __init__(self,data):
		self.left  = self.right = None
		self.data  = data
class Solution:
	def insert(self,root,data):
		if root is None:
			root = Node(data)
		else:
			if data <= root.data:
				cur = self.insert(root.left,data)
				root.left = cur
			else:
				cur = self.insert(root.right,data)
				root.right = cur
		return root
	def levelOrder(self,root):
		s = ''
		if root:
			queue   = [root]
			while(queue):
				node    = queue.pop()
				s += str(node.data)+' ' 
				if node.left:
					queue.insert(0,node.left)
				if node.right:
					queue.insert(0,node.right)
		print s	
T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
	data = int(raw_input())
	root = myTree.insert(root,data)
myTree.levelOrder(root)