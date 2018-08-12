#!/bin/python3

"""
O(n) time complexity, O(1) space complexity.
Maintain window and max area result.
Shrink window greedily, move the side of the window pointing to the shorter height to look for a taller line.
"""
def maxArea(height):
  left, right = 0, len(height) - 1
  res = (right - left) * min(height[left], height[right])
  resLeft, resRight = left, right

  while left < right:
    if height[left] < height[right]:  left += 1
    else:                             right -= 1

    val = (right - left) * min(height[left], height[right])
    if val > res:
      res = val
      resLeft, resRight = left, right
  return res, resLeft, resRight


if __name__ == "__main__":
  print("Enter space-separated heights: ", end="")
  height = list(map(int, input().strip().split(' ')))

  area, left, right = maxArea(height)
  print("Max area: {} using height[{}:{}]".format(area, left, right + 1))
