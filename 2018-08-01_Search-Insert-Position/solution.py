#!/bin/python3

def searchInsert(nums, target):
  if nums == []:
    return 0

  mid = len(nums) // 2
  val = nums[mid]

  if target == val:
    return mid
  elif target > val:
    return searchInsert(nums[mid+1:], target) + (mid + 1)
  else:
    return searchInsert(nums[:mid], target)


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = sorted(list(set(map(int, input().strip().split(' ')))))

  print("Enter target: ", end="")
  target = int(input().strip())
  
  index = searchInsert(nums, target)
  print("Input list: {}".format(nums))
  print("{} should be at index {}".format(target, index)) 
