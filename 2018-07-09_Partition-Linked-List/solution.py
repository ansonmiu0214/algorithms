#!/bin/python3

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		return str(self.val) + (("->" + str(self.next)) if self.next else "")


def linked_list_from_list(arr):
	nodes = list(map(lambda x: ListNode(x), arr))
	head = nodes[0]
	curr = head
	for node in nodes[1:]:
		curr.next = node
		curr = node
	return head


def partition(head, x):
	if head is None:
		return head

	# partition linked list based on x
	smaller, others = partition_tuple(head, x)
	if smaller is None:
		return others

	# link smaller to others
	curr = smaller
	while curr.next:
		curr = curr.next

	curr.next = others
	return smaller

"""
Recursive approach to return a tuple of 2 linked lists (x, y) where all elements of x are less than @param target and the rest in y.
"""
def partition_tuple(head, target):
	if head is None:
		return None, None

	smaller, others = partition_tuple(head.next, target)
	if head.val < target:
		head.next = smaller
		return head, others
	else:
		head.next = others
		return smaller, head


if __name__ == "__main__":
	print("Enter space-separated numbers as your list: ", end="")
	nums = list(map(int, input().strip().split(' ')))
	print("Enter partitioning target: ", end="")
	k = int(input().strip())

	head = linked_list_from_list(nums)
	print("Before partition:")
	print(head)

	head = partition(head, k)
	print("After partition:")
	print(head)
