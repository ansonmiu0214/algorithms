#!/bin/python3

from collections import deque

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		if not self.next:	return str(self.val)
		return str(self.val) + "->" + str(self.next)

"""
x_i = len(lists[i]) -> O(sum(x_i) for i = 1 to len(lists))
"""
def merge_k_sorted(lists):
	if lists == []:		return None
	count = len(lists)
	lists = deque(lists)
	while count > 1:
		lists.append(merge_two_lists(lists.popleft(), lists.popleft()))
		count -= 1
	
	return lists[0]

"""
n = len(list1), m = len(list2) -> O(n + m)
"""
def merge_two_lists(list1, list2):
	if list1 is None:		return list2
	if list2 is None:		return list1

	if list1.val < list2.val:
		list1.next = merge_two_lists(list1.next, list2)
		return list1

	list2.next = merge_two_lists(list1, list2.next)
	return list2


def array_to_list(nums):
	res = list(map(lambda n: ListNode(n), nums))
	
	for i in range(len(nums) - 1):
		res[i].next = res[i + 1]

	return res[0]

if __name__ == "__main__":
	list1 = array_to_list([1,3,5,7,9])
	list2 = array_to_list([2,4,6,8,10])
	list3 = array_to_list([-1,90,120])

	lists = [list1, list2, list3]
	print(lists)

	print(merge_k_sorted(lists))
