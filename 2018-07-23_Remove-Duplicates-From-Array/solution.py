#!/bin/python3

def removeDuplicates(nums):
  end = len(nums)
  start = offset = 0

  while start + offset < end:
    # shift by offset
    nums[start] = nums[start + offset]
    val = nums[start]
    count = 0

    curr = start
    while True:
      new_curr = curr + offset
      if not (new_curr < end and nums[new_curr] == val):
        break

      # shift by offset, increment count and progress
      nums[curr] = nums[new_curr]
      count += 1
      curr += 1

    # nums[start:curr] have all elements equal to val
    # `count' is number of occurrences of val
    if count > 2:
      # update offset
      offset += (count - 2)
      start += 2
    else:
      start = curr

  return end - offset


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = sorted(list(map(int, input().strip().split(' '))))
  
  print("Before: {}".format(nums))
  end = removeDuplicates(nums)
  print("After: {}".format(nums[:end]))
