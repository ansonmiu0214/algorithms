#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

"""
Recursive approach with pointer manipulation to let the root node be the rightmost child of the processed left subtree.
"""
def increasingBST(root):
  # base case: empty tree
  if root is None:
    return root

  newRoot = root
  if root.left:
    # recursive call handles left subtree and returns that new root
    newRoot = increasingBST(root.left)

    # put `root` as rightmost child of `newRoot`
    root.left = None
    curr = newRoot

    while curr.right:
      curr = curr.right

    curr.right = root

  root.right = increasingBST(root.right)
  return newRoot


if __name__ == "__main__":
  root = TreeNode(5)
  root.left = TreeNode(3)
  root.right = TreeNode(6)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(4)
  root.left.left.left = TreeNode(1)
  root.right.right = TreeNode(8) 
  root.right.right.left = TreeNode(7)
  root.right.right.right = TreeNode(9)

  print(root)
  
  newRoot = increasingBST(root)
  print(newRoot)
