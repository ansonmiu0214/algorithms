#!/bin/python3

"""
Iterative divide-and-conquer approach by using middle to determine which partition
to run 'normal binary search'. At least one partition must be sorted already for the
input list to be a rotated sorted list.
"""
def search(nums, target):
  # base case
  if not nums:  return -1

  left, right = 0, len(nums) - 1
  while left < right:
    mid = (left + right) // 2

    if nums[left] <= nums[mid]:
      # left partition is sorted - run normal binary search there
      if target >= nums[left] and target <= nums[mid]:
        right = mid
      else:
        left = mid + 1

    else:
      # right partition is sorted - run normal binary search there
      if target >= nums[mid] and target <= nums[right]:
        left = mid
      else:
        right = mid - 1


  return left if nums[left] == target else -1


if __name__ == "__main__":
  print("Enter rotated-sorted array: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  print("Enter target: ", end="")
  target = int(input().strip())

  index = search(nums, target)
  if index < 0:
    print("{} cannot be found.".format(target))
  else:
    print("{} found at nums[{}]".format(target, index))
