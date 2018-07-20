#!/bin/python3

def findKthLargest(nums, k):
  mid = len(nums) // 2
  target = nums[mid]

  # quick select partition
  less, more = partition(nums[:mid] + nums[(mid + 1):], target)

  count = len(more)
  if count == k - 1:
    # k-1 elements greater than target
    return target

  if count >= k:
    # kth largest is greater than target
    return findKthLargest(more, k)

  return findKthLargest(less, k - count - 1)

def partition(arr, target):
  less, more = [], []
  for num in arr:
    if num < target:  less.append(num)
    else:             more.append(num)

  return less, more


if __name__ == "__main__":
  print("Enter space-separated numbers: ", end="")
  nums = list(map(int, input().strip().split(' ')))
  
  print("Enter k for kth-largest: ", end="")
  k = int(input().strip())

  print("kth largest = {}".format(findKthLargest(nums, k)))
