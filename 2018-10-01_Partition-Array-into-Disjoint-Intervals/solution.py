#!/bin/python3

"""
Looking for smallest i such that max(A[:i]) <= min(A[i:]).
Do preprocessing to calculate max(A[:i]) and min(A[i:]) first, then
iterate from i = 0 upwards to find first successful i.
"""
def partitionDisjoint(A):
  end = len(A)

  # calculate maxFromLeft
  # maxFromLeft[i] = max(A[:(i+1)])
  leftMax = A[0]
  maxFromLeft = [leftMax]
  for idx in range(1, end):
    leftMax = max(leftMax, A[idx])
    maxFromLeft.append(leftMax)

  # calculate minFromRight
  # minFromRight[i] = min(A[end-i:])
  rightMin = A[-1]
  minFromRight = [rightMin]
  for idx in range(end-2, -1, -1):
    rightMin = min(rightMin, A[idx])
    minFromRight.append(rightMin)

  # iterate and find first successful index
  for idx in range(end):
    if maxFromLeft[idx] <= minFromRight[end-idx-2]:
      return idx + 1

  return -1


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  A = list(map(int, input().strip().split(' ')))

  index = partitionDisjoint(A)
  if index == -1:
    print("Cannot partition as required")
  else:
    print("Split into {} and {}".format(A[:index], A[index:]))
