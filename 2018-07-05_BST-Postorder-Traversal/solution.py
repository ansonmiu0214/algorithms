#!/bin/python3

from collections import deque

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, str(self.left) if self.left else "", str(self.right) if self.right else "")

"""
Stack-based approach
"""
def postorderTraversal(root):
	res = []
	if not root:
		return res

	queue = deque([root])
	while queue:
		curr = queue.pop()
		if curr.left or curr.right:
			queue.append(curr)
			
			if curr.right:
				queue.append(curr.right)
				curr.right = None

			if curr.left:
				queue.append(curr.left)
				curr.left = None

		else:
			res.append(curr.val)

	return res


if __name__ == "__main__":
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)

	print("Tree: {}".format(root))
	print("Post-order traversal: {}".format(postorderTraversal(root)))
