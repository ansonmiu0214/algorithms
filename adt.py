#!/bin/python3

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		return str(self.val) + ("->{}".format(self.next) if self.next else "")


def array_to_list(vals):
	res = list(map(lambda x: ListNode(x), vals))
	for i in range(len(vals) - 1):
		res[i].next = res[i + 1]

	return res[0]

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "Node {} ({}) ({})".format(self.val, self.left or "", self.right or "")
