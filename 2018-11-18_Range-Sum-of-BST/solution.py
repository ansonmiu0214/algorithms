#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

'''
Recursive approach with base case defined on empty node.
A tree node can either be part of the range or not.
If it isn't part of the range, recurse into the correct branch (depending on its val).
If it is part of the range, both branches can be part of the range, so recurse into both and return both sums along with the node's value.
'''
def rangeSumBST(root, L, R):
  if not root:
    return 0

  val = root.val
  if val < L:
    return rangeSumBST(root.right, L, R)

  if val > R:
    return rangeSumBST(root.left, L, R)

  leftSum = rangeSumBST(root.left, L, R)
  rightSum = rangeSumBST(root.right, L, R)
  return leftSum + rightSum + val


if __name__ == "__main__":
  root = TreeNode(10)
  root.left = TreeNode(5)
  root.right = TreeNode(15)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(7)
  root.right.right = TreeNode(18)

  print(root)
  print("Enter space-separated range <L> <R>: ", end="")
  L, R = list(map(int, input().strip().split()))

  res = rangeSumBST(root, L, R)
  print(res)


