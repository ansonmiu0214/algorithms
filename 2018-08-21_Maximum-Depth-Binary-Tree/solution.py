#!/bin/python3
import sys
sys.path.append('../')

import adt

"""
Recursive solution with base case on empty tree.
"""
def maxDepth(root):
  if not root:  return 0
  return max(maxDepth(root.left), maxDepth(root.right)) + 1


if __name__ == "__main__":
  root = adt.TreeNode(2)
  root.left = adt.TreeNode(3)
  root.right = adt.TreeNode(4)
  root.right.right = adt.TreeNode(2)
  root.right.right.right = adt.TreeNode(5)

  print(root)
  depth = maxDepth(root)
  print("Max depth = {}".format(depth))
