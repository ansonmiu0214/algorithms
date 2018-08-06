#!/bin/python3
import sys
sys.path.append('../')

import adt

from collections import deque

"""
Stack-based approach.
"""
def preorderTraversal(root):
  if not root:
    return []

  res = []
  queue = deque([root])
  while queue:
    curr = queue.pop()
    res.append(curr.val)

    if curr.right:  queue.append(curr.right)
    if curr.left:   queue.append(curr.left)

  return res


if __name__ == "__main__":
  root = adt.TreeNode(1)
  root.right = adt.TreeNode(2)
  root.right.left = adt.TreeNode(3)

  print(root)
  traversal = preorderTraversal(root)

  print(traversal)
