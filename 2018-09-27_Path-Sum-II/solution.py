#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode
from collections import deque

"""
Trace paths iteratively through BFS and keep track of path and sum so far.
Compare sum so far with target when leaf is reached.
"""
def pathSum(root, target):
  res = []
  
  # handle base case of empty tree
  if root is None:
    return res

  # setup queue for breadth-first search
  # keep track of traversal node, path so far and sum so far
  queue = deque([(root, [root.val], root.val)])
  while queue:
    node, path, sumSoFar = queue.popleft()

    leaf = node.left is None and node.right is None
    if leaf:
      if sumSoFar == target:
        res.append(path)

    # add children to queue
    # tree can contain negative numbers so cannot "shortcircuit"
    # if sumSoFar already exceeds target (since val could be negative)
    if node.left:
      queue.append((node.left, path + [node.left.val], sumSoFar + node.left.val))

    if node.right:
      queue.append((node.right, path + [node.right.val], sumSoFar + node.right.val))

  return res


if __name__ == "__main__":
  root = TreeNode(5)
  root.left = TreeNode(4)
  root.right = TreeNode(8)
  root.left.left = TreeNode(11)
  root.left.left.left = TreeNode(7)
  root.left.left.right = TreeNode(2)
  root.right.left = TreeNode(13)
  root.right.right = TreeNode(4)
  root.right.right.left = TreeNode(5)
  root.right.right.right = TreeNode(1)

  print("Tree:")
  print(root)
 
  print()
  print("Enter target: ", end="")
  target = int(input().strip())

  paths = pathSum(root, target)
  print(paths)
