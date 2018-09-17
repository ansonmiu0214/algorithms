#!/bin/python3
import sys
sys.path.append('../')

from collections import deque
from adt import TreeNode

"""
Use level order traversal to reach nodes at level `depth-1` to modify. Handle base cases
of empty tree and inserting at root depth separately.
"""
def addOneRow(root, val, depth):
  # base case: empty tree, nothing to do
  if root is None:
    return root

  # base case: insert at root depth,
  # put current root as left subtree of new root as per spec
  if depth == 1:
    newRoot = TreeNode(val)
    newRoot.left = root
    return newRoot

  # setup level order traversal
  lvlToModify = depth - 1
  queue = deque([(root, 1)])

  while queue:
    node, lvl = queue.popleft()

    if lvl < lvlToModify:
      # add children as required
      if node.left:
        queue.append((node.left, lvl + 1))

      if node.right:
        queue.append((node.right, lvl + 1))

    else:
      # insert new row here
      newLeft = TreeNode(val)
      newLeft.left = node.left
      node.left = newLeft
    
      newRight = TreeNode(val)
      newRight.right = node.right
      node.right = newRight

  return root


if __name__ == "__main__":
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.right = TreeNode(6)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(1)
  root.right.left = TreeNode(5)

  print("Original tree:")
  print(root)
 
  val, depth = 1, 2
  print("Inserting a row of {}s at depth {}...".format(val, depth))

  root = addOneRow(root, val,depth)
  print(root)
