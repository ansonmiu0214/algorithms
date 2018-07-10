#!/bin/python3

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, self.left or "", self.right or "")


def sumNumbers(root):
	if root is None:	return 0
	return sum(map(int, number_from_paths(root)))

def number_from_paths(root):
	val = str(root.val)

	# Leaf node
	if not (root.left or root.right):
		return [val]

	# Recursively map and prepend curr val as prefix
	res = []
	if root.left:
		res += list(map(lambda x: val + x, number_from_paths(root.left)))

	if root.right:
		res += list(map(lambda x: val + x, number_from_paths(root.right)))

	return res


if __name__ == "__main__":
	root = TreeNode(3)
	root.left = TreeNode(1)
	root.right = TreeNode(2)

	print("Tree: {}".format(root))
	print("Sum: {}".format(sumNumbers(root)))
