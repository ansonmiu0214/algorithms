#!/bin/python3

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	# Haskell-style representation
	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, self.left or "", self.right or "")


"""
Tree utils
"""
def insert(tree, val):
	if tree is None:
		return Node(val)

	if val < tree.val:
		tree.left = insert(tree.left, val)
		return right_rotate(tree)

	tree.right = insert(tree.right, val)
	return left_rotate(tree)


def left_rotate(node):
	root = node.right
	node.right = root.left
	root.left = node
	return root

def right_rotate(node):
	root = node.left
	node.left = root.right
	root.right = node
	return root

def dll_print(head):
	curr = head
	while curr is not None:
		print(curr.val, end="")
		if curr.right is not None:
			print(" -> ", end="")
		else:
			print()
		curr = curr.right


"""
Entry point
"""
def	bst_to_dll(tree, recursion):
	if recursion:
		bst_to_dll_rec(tree)
	else:
		bst_to_dll_iter(tree)

"""
Recursive approach: recursve on non-None children and update pointers.
"""
def bst_to_dll_rec(tree):
	if tree.left is not None:
		bst_to_dll_rec(tree.left)

		# find rightmost
		curr = tree.left
		while curr.right is not None:
			curr = curr.right

		# update pointers
		curr.right = tree
		tree.left = curr

	if tree.right is not None:
		bst_to_dll_rec(tree.right)

		# find leftmost
		curr = tree.right
		while curr.left is not None:
			curr = curr.left

		# update pointers
		curr.left = tree
		tree.right = curr

	return

"""
Iterative approach: 1-pass for in-order traversal + 1-pass for pointer updates; no recursion stack overhead at the cost of O(n) memory for temporary array.
"""
from collections import deque

def bst_to_dll_iter(tree):
	queue = deque()
	queue.append(tree)
	temp_array = []

	# in-order traversal
	while queue:
		curr = queue.popleft()
		if curr.left is not None:
			child = curr.left
			curr.left = None
			queue.appendleft(curr)
			queue.appendleft(child)
		else:
			temp_array.append(curr)

			if curr.right is not None:
				queue.appendleft(curr.right)

	# update pointers
	prev = None
	i, end = 0, len(temp_array)
	while i < end:
		curr = temp_array[i]
		
		if prev is not None:
			prev.right = curr
			curr.left = prev

		prev = curr
		i += 1


if __name__ == "__main__":
	print("Enter list of space-separated numbers to construct tree:")
	arr = list(map(int, input().strip().split(' ')))

	tree = None
	for num in arr:
		tree = insert(tree, num)

	print("***")
	print("Tree: {}".format(tree))
	print("***")

	print("Recursion? [y/n] ", end="")
	recursion = input().strip().lower() == "y"

	bst_to_dll(tree, recursion)

	curr = tree
	while curr.left is not None:
		curr = curr.left

	print("***")
	print("Doubly Linked List: ", end="")
	dll_print(curr)
	print("***")
