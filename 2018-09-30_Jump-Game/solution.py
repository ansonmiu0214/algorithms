#!/bin/python3

"""
Since the jump intervals are non-negative, a greedy approach
can be taken to keep track of the furthest index that can be reached.
This index is updated as the function iterates through the array,
and will terminate when the end is reached or when an unreachable index
is reached (detected when the maximum index reachable is less than the
current index).
"""
def canJump(nums):
  maxReachable = 0
  end = len(nums)
  target = end - 1

  for idx in range(end):
    if maxReachable < idx:
      return False

    if maxReachable == target:
      return True

    maxReachable = max(maxReachable, idx + nums[idx])

  return True


if __name__ == "__main__":
  print("Enter space-separated integers for maximum jump lengths: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  res = canJump(nums)
  print(res)
