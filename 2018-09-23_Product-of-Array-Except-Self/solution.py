#!/bin/python3

"""
To avoid division, use 2 passes to get product up to [:n] and product from [n+1:] onwards.
"""
def productExceptSelf(nums):
  res = []
  count = len(nums)

  upAcc = 1
  for idx in range(count):
    res.append(upAcc)   # res[idx] = product of nums[:idx]
    upAcc *= nums[idx]

  downAcc = 1
  for idx in range(count-1, -1, -1):
    res[idx] *= downAcc # res[idx] = product(nums[:idx]) * product(nums[end-1]...nums[idx+1])
    downAcc *= nums[idx]
 
  return res


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  res = productExceptSelf(nums)
  print(res)
