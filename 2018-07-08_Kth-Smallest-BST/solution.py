#!/bin/python3

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    return "Node {} ({}) ({})".format(self.val, str(self.left) if self.left else "", str(self.right) if self.right else "")

"""
Precondition: k is always valid.
Using inorder traversal approach with counter and halting at k.
"""
def kthSmallest(root, k):
  queue = deque([(root, False)])
  count = 0
  while queue:
    curr, seen = queue.pop()
    if (curr.left or curr.right) and not seen:
      # add children (and self) to stack
      if curr.right:  queue.append((curr.right, False))
      queue.append((curr, True))
      if curr.left:   queue.append((curr.left, False))

    else:
      count += 1
      if count == k:  return curr.val

  return None


if __name__ == "__main__":
  root = TreeNode(5)
  root.right = TreeNode(6)
  root.left = TreeNode(3)
  root.left.right = TreeNode(4)
  root.left.left = TreeNode(2)
  root.left.left.left = TreeNode(1)

  print("Tree: {}".format(root))
  print("Enter number from 1 to 6: ", end="")
  k = int(input().strip())
  print("{}-smallest: {}".format(k, kthSmallest(root, k)))
      
