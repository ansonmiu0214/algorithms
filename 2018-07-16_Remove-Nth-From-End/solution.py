#!/bin/python3

import sys
sys.path.append('../')

import adt

def removeNthFromEnd(head, n):
	temp = adt.ListNode(0)
	temp.next = head

	# setup window
	curr = end = temp
	for _ in range(n):	end = end.next

	# move end to last elem of list so curr.next points to deletion node
	while end.next:
		curr = curr.next
		end = end.next

	# pointer manipulation
	curr.next = curr.next.next
	return curr.next if curr == temp else head

if __name__ == "__main__":
	print("Enter space-separated integers as list: ", end="")
	nums = adt.array_to_list(list(map(int, input().strip().split(' '))))
	
	print("Enter n: ", end="")
	n = int(input().strip())

	print("Original list: {}".format(nums))
	print("Modified list: {}".format(removeNthFromEnd(nums, n)))
