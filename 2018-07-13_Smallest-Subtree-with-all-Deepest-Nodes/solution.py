#!/bin/python3

from collections import deque

class TreeNode():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
 
  def __repr__(self):
    return "Node {} ({}) ({})".format(self.val, self.left or "", self.right or "")


def subtreeWithAllDeepest(root):
  if root is None:  return root

  lvl_to_nodes = dict()
  queue = deque([(root, 0)])

  # need to augment node with parent info
  root.parent = root
  deepest = 0

  while queue:
    curr, lvl = queue.popleft()
    if curr.left or curr.right:
      # add children to queue with correct level
      if curr.left:
        curr.left.parent = curr
        queue.append((curr.left, lvl + 1))

      if curr.right:
        curr.right.parent = curr
        queue.append((curr.right, lvl + 1))
  
    else:
      # update deepest level if required
      if deepest < lvl:
        deepest = lvl

    if lvl in lvl_to_nodes:
      lvl_to_nodes[lvl].append(curr)
    else:
      lvl_to_nodes[lvl] = [curr]

  # iteratively + greedily find unique node whose descendants are all deepest nodes
  nodes = lvl_to_nodes[deepest]
  if len(nodes) == 1:   return nodes[0]
  while True:
    # if all nodes share same parent, return
    parents = set(map(lambda x: x.parent, nodes))
    if len(parents) == 1:
      for node in parents:  return node

    # iterate on the parents
    nodes = parents

  return None
  

if __name__ == "__main__":
  root = TreeNode(3)
  root.left  = TreeNode(5)
  root.right = TreeNode(1)
  root.left.left = TreeNode(6)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(0)
  root.right.right = TreeNode(8)
  root.left.right.left = TreeNode(7)
  root.left.right.right = TreeNode(4)

  print("Tree:")
  print(root)
  print()

  print("Subtree with all deepest nodes:")
  print(subtreeWithAllDeepest(root))
  
