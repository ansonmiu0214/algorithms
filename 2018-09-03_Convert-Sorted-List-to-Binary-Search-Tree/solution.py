#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode, ListNode, array_to_list

"""
Recursive approach defined on empty/singleton list as base cases.
Maintain height balance by recursing on left/right partitions defined by the midpoint.
Midpoint obtained using the tortoise-hare algorithm.
"""
def sortedListToBST(head):
	# base case: empty list
	if head is None:
		return None

	# base case: singleton list
	if head.next is None:
		return TreeNode(head.val)

	# use tortoise-hare algorithm to find midpoint, keeping track of mid's prev
	prev, left, right = None, head, head
	while right.next:
		# advance left pointer
		prev = left
		left = left.next

		# advance right pointer
		right = right.next
		if right.next is None:
			break
		right = right.next

	# partition w.r.t. midpoint defined by left
	prev.next = None

	# recursively build children
	leftChild = sortedListToBST(head)
	rightChild = sortedListToBST(left.next)

	# create, setup and return root node
	root = TreeNode(left.val)
	root.left = leftChild
	root.right = rightChild
	return root


if __name__ == "__main__":
	head = array_to_list([-10, -3, 0, 5, 9])
	print("Linked list:")
	print(head)
	print()

	root = sortedListToBST(head)
	print("BST:")
	print(root)
