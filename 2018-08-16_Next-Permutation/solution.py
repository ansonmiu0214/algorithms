#!/bin/python3

def nextPermutation(nums):
  # find largest i such that nums[i] < nums[i+1]

  end = len(nums)
  for i in range(end-2, -1, -1):
    if not nums[i] < nums[i+1]:
      continue

    # nums[i+1:] is in descending order
    # next permutation needs a new nums[i] that is
    # larger than the current one

    # find the first element that is larger than nums[i] and swap
    j = end - 1
    while nums[j] < nums[i]:
      j += 1

    nums[i], nums[j] = nums[j], nums[i]
    
    # next permutation will have nums[i+1:] be in ascending order
    nums[i+1:] = reversed(nums[i+1:])
    return
  
  # all elements in nums is descending: reverse the list
  nums.reverse()


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))
  print("Original: {}".format(nums))

  nextPermutation(nums)
  print("Next: {}".format(nums))
