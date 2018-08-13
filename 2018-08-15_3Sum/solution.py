#!/bin/python3

"""
O(n(log(n)) sorting + (O(n) loop * O(n) two-sum) = O(n^2) running time complexity
O(1) space complexity using built-in library in-place sort.

Iterate through all possible starting elements and run twoSum on the remainder of the list.Skip any duplicates when moving pointers to ensure no duplicate solutions are added to the solution set.
"""
def threeSum(nums, target = 0):
  nums.sort()

  res = []
  end = len(nums)

  for i in range(end - 2):
    curr = nums[i]
    if i > 0 and nums[i - 1] == nums[i]:
      continue

    lookFor = target - curr

    left, right = i + 1, end - 1
    while left < right:
      leftVal, rightVal = nums[left], nums[right]
      cand = leftVal + rightVal
      if cand == lookFor:
        res.append([curr, leftVal, rightVal])

      if cand < lookFor:
        # lower than lookFor, move left pointer forward for larger val
        left += 1

        # skip duplicates
        while left < right and nums[left - 1] == nums[left]:
          left += 1

      else:
        # move right pointer backward for smaller val
        right -= 1
        while left < right and nums[right + 1] == nums[right]:
          right -= 1
  
  return res


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  solutionSet = threeSum(nums)
  print("Solution set:")
  for solution in solutionSet:  print(solution)
