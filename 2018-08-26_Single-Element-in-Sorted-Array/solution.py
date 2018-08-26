#!/bin/python3

"""
Binary search approach with special case analysis on how the midpoint partitions the array (as odd- and even-length sublists need to be handled differently), with the base case on the singleton list. Iterative implementation removes the recursive stack overhead using constant left/right pointers and achieves O(log(n)) running time complexity.
"""
def singleNonDuplicate(arr):
  left, right = 0, len(arr) - 1
  while left != right:
    # binary search approach
    mid = (left + right) // 2

    if (mid - left) % 2 == 0:
      # midpoint partitions into even-length sublists on either side

      if arr[mid] == arr[mid-1]:
        # left partition is even-length, so midpoint shouldn't equal left adjacent element
        # recurse left
        right = mid - 2
      elif arr[mid] == arr[mid+1]:
        # same argument for right
        left = mid + 2
      else:
        # base case: not equal to any adjacent, so already found
        return arr[mid]

    else:
      # midpoint partitions into odd-length sublists on either side
      # same logical case-by-case analysis as above, but for odd-length sublists

      if arr[mid] == arr[mid-1]:    left = mid + 1
      elif arr[mid] == arr[mid+1]:  right = mid - 1
      else:                         return arr[mid]
        
  return arr[left]


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ' )))

  nonDuplicate = singleNonDuplicate(nums)
  print("Non-duplicate element is: {}".format(nonDuplicate))
