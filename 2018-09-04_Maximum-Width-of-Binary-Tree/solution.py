#!/bin/python3
import sys
sys.path.append('../')

from collections import deque
from adt import TreeNode

"""
Breadth-first search approach for level-order traversal with accumulator to keep track
of maximum width. Width computed by difference in node index on start/end nodes per level.
Node index allows width calculations that accounts for null nodes in between and does not
require creating arbitrary null nodes.
"""
def widthOfBinaryTree(root):
  # base case of empty tree
  if root is None:
    return 0

  queue = deque([(root, 0, 0)])   # stores [(TreeNode, lvl, index)]
  currLvl = 0
  res = 0
  start, end = 0, 0               # index of start- and end-nodes within level
  
  while queue:
    curr, lvl, idx = queue.popleft()

    if lvl > currLvl:
      # update result accumulator with level width
      res = max(res, end - start)
      currLvl = lvl
      start = idx
      end = idx

    end = idx   # update end node index
    if curr.left:
      queue.append((curr.left, lvl + 1, 2 * idx + 1))

    if curr.right:
      queue.append((curr.right, lvl + 1, 2 * idx + 2))

  res = max(res, end - start) + 1
  return res


if __name__ == "__main__":
  root = TreeNode(1)
  root.left = TreeNode(3)
  root.right = TreeNode(2)
  root.left.left = TreeNode(5)
  root.right.left = TreeNode(9)
  root.right.right = TreeNode(7)

  print(root)
  width = widthOfBinaryTree(root)

  print("Maximum width: {}".format(width))
