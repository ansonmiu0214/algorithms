#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

"""
Recursive approach, with care to first make the recursive calls to prune subtrees
before evaluating whether the current node should be removed. Base cases defined on 
the empty tree and a leaf node with value 0.
"""
def pruneTree(root):
  # base case: empty tree
  if root is None:
    return root

  # recursive calls to prune children
  root.left = pruneTree(root.left)
  root.right = pruneTree(root.right)

  # evaluate whether current node should be pruned by 2nd base case
  if root.val == 0 and root.left is None and root.right is None:
    return None
  
  return root


if __name__ == "__main__":
  root = TreeNode(1)
  root.right = TreeNode(0)
  root.right.left = TreeNode(0)
  root.right.right = TreeNode(1)

  print("Before pruning:")
  print(root)

  root = pruneTree(root)
  print()
  print("After pruning:")
  print(root)
