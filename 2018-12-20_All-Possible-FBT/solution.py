#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode

'''
Bottom-up DP approach with base cases for 0 (none), 1 (singleton tree) and 2 (none).
'''
def allPossibleFBT(N):
  table = [[]] + [[TreeNode(0)]] + [[] for _ in range(N)]
  #if N < 3:
  #  return table[N]

  for i in range(3, N+1):
    # List of possible FBTs for `i` nodes, solves subproblem for N=i    
    res = []

    # Iterate through all possible pairs of left/right idxs
    # Previous smaller subproblem solved and memoised in table
    for leftIdx in range(1, i-1):
      # Require that leftIdx + rightIdx + 1 (root) = i
      rightIdx = i-1-leftIdx

      lefts = table[leftIdx]
      rights = table[rightIdx]

      for left in lefts:
        for right in rights:
          # Build node and add ro 
          root = TreeNode(0)
          root.left = left
          root.right = right
          res.append(root)

    table[i] = res

  return table[N]


if __name__ == "__main__":
  print("Enter N: ", end="")
  N = int(input().strip())

  trees = allPossibleFBT(N)
  print("Possibilities: {}".format(len(trees)))
  print(trees)
