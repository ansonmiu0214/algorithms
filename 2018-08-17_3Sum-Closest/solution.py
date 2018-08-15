#!/bin/python3

"""
Same strategy as 3Sum problem, but keep track of minimum absolute difference w.r.t. @param target.
"""
def threeSumClosest(nums, target):
  components = []
  diff = None
  end = len(nums)
  
  for i in range(end - 2):
    curr = nums[i]

    lookFor = target - curr
    left, right = i + 1, end - 1

    while left < right:
      currVal = nums[left] + nums[right]
      currDiff = currVal - lookFor
      if diff is None or abs(currDiff) < abs(diff):
        diff = currDiff
        components = [curr, nums[left], nums[right]]

      if currVal < lookFor:
        left += 1
      else:
        right -= 1
      

  return target + diff, components 


if __name__ == "__main__":
  print("Enter space-separated numbers: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  print("Enter target ", end="")
  target = int(input().strip())

  closest, components = threeSumClosest(nums, target)
  operands = " + ".join(list(map(str, components)))

  print("The sum that is closest to {} is {}. ({} = {})".format(target, closest, operands, target))
