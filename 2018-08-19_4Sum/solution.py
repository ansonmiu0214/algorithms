#!/bin/python3

"""
O(n^3) running time complexity.
Iteratively run 3Sum - an O(n^2) algorithm - on each potential starter.
"""
def fourSum(nums, target):
  nums = sorted(nums)
  end = len(nums)

  res = []
  for i in range(end-3):
    a = nums[i]

    # skip if duplicate 1st value handled before
    if i > 0 and a == nums[i-1]:
      continue

    for j in range(i+1, end-2):
      b = nums[j]

      # skip if duplicate 2nd value handled before
      if j > i+1 and b == nums[j-1]:
        continue

      # apply usual 3Sum technique
      lookFor = target - a - b
      left, right = j+1, end-1
      while left < right:
        c, d = nums[left], nums[right]
        cand = c + d

        if cand == lookFor:
          res.append([a,b,c,d,])
 
        # increase sum if cand < lookFor
        # also skip if duplicate handled before
        if cand < lookFor:
          left += 1
          while left < right and nums[left] == nums[left-1]:
            left += 1
        else:
          right -= 1
          while left < right and nums[right] == nums[right+1]:
            right -= 1
  
  return res


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))
 
  print("Enter target: ", end="")
  target = int(input().strip())

  solutionSet = fourSum(nums, target)

  print("A solution set is: ")
  print("[")
  count = len(solutionSet)
  for i, solution in enumerate(solutionSet):
    print("  {}{}".format(solution, "," if i+1 < count else ""))
  print("]")
