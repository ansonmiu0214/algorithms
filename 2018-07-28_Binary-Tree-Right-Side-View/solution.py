#!/bin/python3
import sys
sys.path.append('../')

import adt
from collections import deque

"""
BFS approach, only append to result on level change.
"""
def rightSideView(root):
  res = []
  if not root:  return res

  queue = deque([(root, 0)])
  depth = 0
  prev = None

  while queue:
    curr, lvl = queue.popleft()

    if lvl > depth:
      depth = lvl
      res.append(prev)

    if curr.left:   queue.append((curr.left, lvl + 1))
    if curr.right:  queue.append((curr.right, lvl + 1)) 

    prev = curr.val

  if prev:  res.append(prev)
  return res


if __name__ == "__main__":
  root = adt.TreeNode(1)
  root.left = adt.TreeNode(2)
  root.right = adt.TreeNode(3)
  root.left.right = adt.TreeNode(5)
  root.right.right = adt.TreeNode(4)

  print(root)

  rhs = rightSideView(root)
  print("RHS: {}".format(rhs))
