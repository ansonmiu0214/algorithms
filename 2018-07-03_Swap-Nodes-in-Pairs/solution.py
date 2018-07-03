#!/bin/python3

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		res = [self.val]
		curr = self
		while curr.next:
			curr = curr.next
			res.append(curr.val)
		return str(res)

"""
Solution based on inductive approach through reasoning base/inductive cases.
"""
def swapPairs(head):
	if not head:
		return None				# 0 items

	if not head.next:
		return head				# 1 item

	# > 1 items
	new_head = head.next
	tail = head.next.next
	new_head.next = head
	new_head.next.next = swapPairs(tail)
	return new_head


if __name__ == "__main__":
	print("Enter space-separated integers: ", end="")
	nums = list(map(int, input().strip().split(' ')))
	nodes = list(map(lambda x: ListNode(x), nums))
	
	count = len(nums)
	for i in range(count - 1):
		nodes[i].next = nodes[i+1]

	print("Original list: {}".format(nums))
	head = nodes[0] if nodes else None
	head = swapPairs(head)

	print("New list: {}".format(head))
	
