#!/bin/python3

from collections import deque

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


def array_to_tree(vals):
  if not vals:
    return None

  first, *rest = vals
  root = TreeNode(first)

  end = len(rest)

  queue = deque([root])
  i = 0
  while i < end:
    node = queue.popleft()
    if rest[i]:
      node.left = TreeNode(rest[i])
      queue.append(node.left)

    i += 1
    if i == end:
      break

    if rest[i]:
      node.right = TreeNode(rest[i])
      queue.append(node.right)
    i += 1

  return root

