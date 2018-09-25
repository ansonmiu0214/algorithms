#!/bin/python3
import sys
sys.path.append('../')

from adt import ListNode, array_to_list

"""
Break down problem into multiple stages: find length of linked list, then determine the index of the new head through modulo and adjust the `next' pointers for the new head and new tail before returning the new head.
"""
def rotateRight(head, k):
	# base case: list is empty
	if head is None:
		return head

	# find length of linked list through traversal
	length = 0
	nodes = []
	curr = head

	while curr:
		nodes.append(curr)
		length += 1
		curr = curr.next

	# compute index of new head
	new_head_idx = length - (k % length)
	if new_head_idx == length:
		# no need to rotate
		return head

	# new_head.prev becomes the tail
	nodes[new_head_idx-1].next = None

	# previous tail now points to head
	nodes[length-1].next = head

	return nodes[new_head_idx]


if __name__ == "__main__":
	print("Enter space-separated integers for original list: ", end="")
	nums = list(map(int, input().strip().split(' ')))

	print("Enter rotation integer: ", end="")
	k = int(input().strip())

	nums = array_to_list(nums)
	print("Original list:")
	print(nums)

	nums = rotateRight(nums, k)
	print("Rotated list:")
	print(nums)

	
