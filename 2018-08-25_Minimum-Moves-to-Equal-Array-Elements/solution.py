#!/bin/python3

"""
Identify that the optimal solution involves making all numbers equal to the median.
Sorting the list can allow us to find the median, and this operation has O(n(log(n))) running time complexity using the library sort() functino.
"""
def minMoves(nums):
  nums.sort()
  median = nums[len(nums) // 2]
  return sum([abs(median - num) for num in nums]), median


if __name__ == "__main__":
  print("Enter space-separated numbers: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  moves, target = minMoves(nums)
  print("At least {} increments/decrements to make all numbers equal to {}.".format(moves, target))
