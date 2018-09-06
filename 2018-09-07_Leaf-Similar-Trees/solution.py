#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

"""
Recursive approach to find leaves first then compare values.
"""
def leafSimilar(root1, root2):
  return getLeaves(root1) == getLeaves(root2)

def getLeaves(root):
  # base case: empty tree
  if root is None:
    return []

  # base case: leaf
  if root.left is None and root.right is None:
    return [root.val]

  return getLeaves(root.left) + getLeaves(root.right)


if __name__ == "__main__":
  root1 = TreeNode(3)
  root1.left = TreeNode(5)
  root1.right = TreeNode(7)

  root2 = TreeNode(10)
  root2.left = TreeNode(1)
  root2.left.left = TreeNode(5)
  root2.right = TreeNode(7)

  print("Tree 1: {}".format(root1))
  print("Tree 2: {}".format(root2))

  similar = leafSimilar(root1, root2)
  print("Both trees are{} leaf similar.".format("" if similar else " not"))
