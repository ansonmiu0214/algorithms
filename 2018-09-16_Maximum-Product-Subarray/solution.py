#!/bin/python3

"""
Same strategy as maxSum problem by keeping track of maxSoFar and minSoFar.
Optimised the O(n) space to O(1) by using local variables since we only need 
to keep track of local max and local min.
"""
def maxProduct(nums):
  end = len(nums)
  if end == 0:
    return 0

  localMax = localMin = globalMax = nums[0]
  for i in range(1, end):
    curr = nums[i]

    nextLocalMax = max(curr * localMax, curr * localMin, curr)
    nextLocalMin = min(curr * localMax, curr * localMin, curr)

    localMax = nextLocalMax
    localMin = nextLocalMin
     
    globalMax = max(globalMax, localMax)

  return globalMax


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  res = maxProduct(nums)
  print("Maximum product subarray: {}".format(res))
