#!/bin/python3

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, str(self.left) if self.left else "", str(self.right) if self.right else "")


def print_linked_list(root):
	res = []
	curr = root
	while curr:
		res.append(curr.val)
		curr = curr.right
	
	print(res)


def flatten(root):
	if root:
		if root.right:
			flatten(root.right)
		
		if root.left:
			flatten(root.left)
			
			# reconnect pointers
			curr = root.left
			while curr.right:
				curr = curr.right

			# tail of left list point to start of right list
			curr.right = root.right

			# curr should point to start of left list next
			root.right = root.left
		
			# reset left list
			root.left = None


if __name__ == "__main__":
	tree = TreeNode(1)
	tree.left = TreeNode(2)
	tree.left.left = TreeNode(3)
	tree.left.right = TreeNode(4)
	tree.right = TreeNode(5)
	tree.right.right = TreeNode(6)

	print("Tree: {}".format(tree))
	flatten(tree)
	print_linked_list(tree)
