#!/bin/python3

def isValidSerialisation(preorder):
  nodes = preorder.split(',')
  end = len(nodes)

  # invoke recursive validator on nodes in list form
  nextIndex, isValid = isValidPreorder(nodes, 0, end)

  # nextIndex should equal end because should have processed all nodes
  return isValid and nextIndex == end


"""
Recursive approach with base cases defined for empty list and null ('#') node.
Returns tuple of next index to be processed and whether subtree is valid.
"""
def isValidPreorder(nodes, currIndex, end):
  if currIndex == end:
    return currIndex, False

  node = nodes[currIndex]
  if node == '#':
    return currIndex + 1, True

  # validate left subtree
  leftNext, leftValid = isValidPreorder(nodes, currIndex + 1, end)
  if not leftValid:
    return leftNext, leftValid

  # validate right subtree using remains from left subtree
  return isValidPreorder(nodes, leftNext, end)


if __name__ == "__main__":
  print("Enter comma-separated nodes of BST preorder traversal to validate ('#' denotes null sentinel): ")

  preorder = input().strip()
  print(isValidSerialisation(preorder))
