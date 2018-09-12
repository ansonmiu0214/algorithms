#!/bin/python3
import sys
sys.path.append('../')

from adt import ListNode, array_to_list

"""
Iterative approach using flag to keep track of a connected component
over the iterations.
"""
def numComponents(head, G):
	# convert to set to take advantage of membership function
	candidates = set(G)

	curr = head			# linked list traversal pointer
	count = 0				# return value
	linked = False	# true iff on a linked component 

	while curr:
		if curr.val in candidates:
			linked = True
		else:
			# increment count and reset flag
			# if previous elements were linked
			if linked:
				count += 1
				linked = False
	
		curr = curr.next

	# handle edge case where the list ends on a linked component
	if linked:	count += 1
	return count


if __name__ == "__main__":
	print("Enter space-separated numbers: ", end="")
	nums = list(map(int, input().strip().split(' ')))

	print("Enter space-separated candidates: ", end="")
	G = list(map(int, input().strip().split(' ')))

	head = array_to_list(nums)
	print(head)

	count = numComponents(head, G)
	print("There {} {} connected component{}.".format("is" if count == 1 else "are", count, "" if count == 1 else "s"))

