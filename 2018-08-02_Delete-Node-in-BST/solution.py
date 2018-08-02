#!/bin/python3
import sys
sys.path.append('../')

import adt

def deleteNode(root, target):
  # base case - not found
  if not root:
    return root

  # base case - found
  val = root.val
  if target == val:
    return delete(root)

  # recursive cases
  if target < val:
    root.left = deleteNode(root.left, target)
  else:
    root.right = deleteNode(root.right, target)
  return root


def delete(node):
  # base cases - return other child if one is empty
  if not node.left:
    return node.right

  if not node.right:
    return node.left

  newRoot = findLeftMost(node.right)
  newRight = deleteLeftMost(node.right)
  newRoot.left = node.left
  newRoot.right = newRight
  return newRoot


def findLeftMost(node):
  if not node.left:
    return node

  return findLeftMost(node.left)


def deleteLeftMost(node):
  if not node.left:
    return node.right

  node.left = deleteLeftMost(node.left)
  return node



if __name__ == "__main__":
  root = adt.TreeNode(5)
  root.left = adt.TreeNode(3)
  root.right = adt.TreeNode(6)
  root.left.left = adt.TreeNode(2)
  root.left.right = adt.TreeNode(4)
  root.right.right = adt.TreeNode(7)
 
  print(root)

  print("Enter deletion target: ", end="")
  target = int(input().strip())

  root = deleteNode(root, target)
  print(root)
