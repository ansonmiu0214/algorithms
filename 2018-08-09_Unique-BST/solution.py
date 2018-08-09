#!/bin/python

"""
O(n^2) DP solution.
numTrees(n) = numTrees(0) * numTrees(n-1) + numTrees(1) * numTrees(n-2) + ...
Sum of products accumulated in DP array; use of product accounts for different possible combinations.
No need to use 2D table because number of unique BSTs that store 1..k is the same as the number of unique BSTs that store r..(r+k) for any r, so can just use 1-dimensional DP array.
Input of each product pair (e.g. numTrees(0) and numTrees(n-1)) sum to n-1 because root is excluded.
"""
def numTrees(n):
  if n == 1:
    return 1

  count = [1 for _ in range(n+1)]
  count[2] = 2

  for i in range(3, n+1):
    uniqueTrees = 0
    for j in range(i):
      uniqueTrees += count[j] * count[i-j-1]
    count[i] = uniqueTrees

  return count[n]


if __name__ == "__main__":
  print("Enter positive integer: ", end="")
  n = int(input().strip())

  res = numTrees(n)

  print("There {} {} unique binary search tree{} that store range [1..{}]".format("is" if n == 1 else "are", res, "" if n == 1 else "s", n))
