#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

"""
Recursive approach, return true iff either root1 is equivalent to root2,
or if root1 is `flip equivalent` to root2.
"""
def flipEquiv(root1, root2):
  # Base cases: both empty (true, vacuously equiv) or either empty (false; not equiv)
  empty_left = root1 is None
  empty_right = root2 is None  

  if empty_left or empty_right:
    return empty_left and empty_right

  # Base case: root node is different, return False
  if root1.val != root2.val:
    return False

  r1_left = root1.left
  r1_right = root1.right
  r2_left = root2.left
  r2_right = root2.right

  return (flipEquiv(r1_left, r2_right) and flipEquiv(r1_right, r2_left)) or (flipEquiv(r1_left, r2_left) and flipEquiv(r1_right, r2_right))


if __name__ == "__main__":
  root1 = TreeNode(1)
  root1.left = TreeNode(2)
  root1.right = TreeNode(3)

  root2 = TreeNode(1)
  root2.left = TreeNode(3)
  root2.right = TreeNode(2)

  print("1: {}".format(root1))
  print("2: {}".format(root2))
  print(flipEquiv(root1, root2))

  root2.right = TreeNode(3)
  print("2: {}".format(root2))
  print(flipEquiv(root1, root2))
