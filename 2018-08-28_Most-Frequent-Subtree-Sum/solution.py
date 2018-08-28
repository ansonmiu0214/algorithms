#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

"""
Recursively compute subtree sums and keep track of frequency table and result accumulator.
"""
def findFrequentSubtreeSum(root):
  # build lookup table of sum-to-frequency
  sumFreqTable = {}

  # keep track of highest frequency
  highestFreq, res = 0, []

  """
  Helper function to recursively compute subtree sums and populate table
  """
  def getSum(node):
    nonlocal highestFreq, res

    if not node:
      return 0

    subtreeSum = getSum(node.left) + getSum(node.right) + node.val
    if subtreeSum in sumFreqTable:
      sumFreqTable[subtreeSum] += 1
    else:
      sumFreqTable[subtreeSum] = 0

    # update highest frequency accumulator
    freq = sumFreqTable[subtreeSum]
    if freq > highestFreq:
      highestFreq = freq
      res = [subtreeSum]
    elif freq == highestFreq:
      res.append(subtreeSum)

    return subtreeSum

  getSum(root)
  return res


if __name__ == "__main__":
  root = TreeNode(5)
  root.left = TreeNode(2)
  root.right = TreeNode(-5)
  print(root)

  sums = findFrequentSubtreeSum(root)
  print(sums)
