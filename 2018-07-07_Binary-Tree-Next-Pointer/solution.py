#!/bin/python3

from collections import deque

class TreeLinkNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.next = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, str(self.left) if self.left else "", str(self.right) if self.right else "")

"""
BFS approach to connect nodes at the same level.
"""
def connect(root):
	if not root:	return

	queue = deque([(root, 0)])
	while queue:
		curr, lvl = queue.popleft()
		if curr.left:		queue.append((curr.left, lvl + 1))
		if curr.right:	queue.append((curr.right, lvl + 1))

		if queue:
			other, other_lvl = queue[0]
			if lvl == other_lvl:	curr.next = other


def print_level(root):
	res = []
	curr = root
	while curr:
		res.append(curr.val)
		curr = curr.next
	print(res)

if __name__ == "__main__":
	root = TreeLinkNode(3)
	root.left = TreeLinkNode(2)
	root.right = TreeLinkNode(4)
	root.right.left = TreeLinkNode(5)

	print(root)
	connect(root)

	print_level(root.left)
