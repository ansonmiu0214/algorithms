#!/bin/python3

from collections import deque

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, self.left or "", self.right or "")


def zigzagLevelOrder(root):
	# base case
	if root is None:		return []

	res = []
	curr_lvl = 0			# keep track of current level
	curr = deque()		# nodes in current level
	queue = deque([(root, 0)])

	while queue:
		node, lvl = queue.popleft()
		# save prev level if accessing next level
		if lvl != curr_lvl:
			res.append(list(curr))
			curr = deque()
			curr_lvl = lvl

		# forward on even-levels, else backwards
		if lvl % 2 == 0:	curr.append(node.val)
		else:							curr.appendleft(node.val)

		# recurse to children if required
		if node.left:		queue.append((node.left, lvl + 1))
		if node.right:	queue.append((node.right, lvl + 1))

	if curr:	res.append(list(curr))
	return res


if __name__ == "__main__":
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)

	print("Tree:")
	print(root)

	print()
	print("Zigzag level traversal:")
	print(zigzagLevelOrder(root))
