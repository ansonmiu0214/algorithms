#!/bin/python3

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, str(self.left) if self.left else "", str(self.right) if self.right else "")


def isValidBST(root, low = None, high = None):
	# empty tree is vacuously valid
	if not root:	return True

	if root.left:
		if not root.left.val < root.val:				return False
		if low and not low < root.left.val:			return False

	if root.right:
		if not root.right.val > root.val:				return False
		if high and not high > root.right.val:	return False	

	return isValidBST(root.left, low, root.val) and isValidBST(root.right, root.val, high)


if __name__ == "__main__":
	tree = TreeNode(0)
	tree.left = TreeNode(1)
	tree.right = TreeNode(2)

	print("{} is {}.".format(tree, "valid" if isValidBST(tree) else "not valid"))

	tree.right.val = 3
	tree.val = 2
	print("{} is {}.".format(tree, "valid" if isValidBST(tree) else "not valid"))
