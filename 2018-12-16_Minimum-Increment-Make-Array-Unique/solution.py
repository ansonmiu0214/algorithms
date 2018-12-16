#!/bin/python3

"""
Greedy approach: sort in ascending order and iterate through,
keeping track of last seen number so the minimum increment is the amount
needed to update the current element to an unseen number.
"""
def minIncrementForUnique(A):
  if not A:
    return 0

  A.sort()

  count = 0
  lastSeen, *rest = A

  for el in rest:
    if el > lastSeen:
      lastSeen = el
    else:
      lastSeen += 1
      increment = lastSeen - el
      count += increment

  return count


if __name__ == "__main__":
  print("Enter list: ", end="")
  arr = list(map(int, input().strip().split()))

  count = minIncrementForUnique(arr)
  print(count)
