#!/bin/python3

def subsets(nums):
  if nums == []:  return [[]]

  val = nums[0]
  next_sets = subsets(nums[1:])

  res = list(next_sets)
  for subset in next_sets:
    copy = list(subset)
    copy.append(val)
    res.append(copy)

  return res


if __name__ == "__main__":
  print("Enter space-separated items: ", end="")
  items = input().strip().split(' ')

  print(items)
  print(subsets(items))
  
