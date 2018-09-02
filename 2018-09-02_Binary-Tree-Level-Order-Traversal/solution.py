#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode
from collections import deque

"""
Breadth-first search approach using queue.
"""
def levelOrder(root):
	res = []
	
	# handle edge case of empty tree (where root is None)
	if root is None:	return res

	# setup queue
	queue = deque([(root, 0)])
	currLvl = 0			# current level
	lvlNodes = []		# nodes on current level

	while queue:
		curr, depth = queue.popleft()
		
		# enqueue children if they exist
		if curr.left:		queue.append((curr.left, depth + 1))
		if curr.right:	queue.append((curr.right, depth + 1))

		# reset lvlNodes list if crossing depth boundary
		if depth > currLvl:
			currLvl = depth
			res.append(lvlNodes)
			lvlNodes = []

		lvlNodes.append(curr.val)

	if lvlNodes:	res.append(lvlNodes)
	return res


if __name__ == "__main__":
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)

	print(root)
	nodes = levelOrder(root)

	print(nodes)
