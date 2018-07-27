#!/bin/python3
import sys
sys.path.append('../')

import adt

"""
1-pass, in-place modification, using odd/even pointers and switching flag.
O(1) space complexity + O(n) running time complexity.
"""
def oddEvenList(head):
  # base case - empty or singleton
  if not head or not head.next:
    return head

  odd_head = odd = head
  even_head = even = head.next

  isOdd = True            # `switching' flag
  curr = head.next.next   # traversal pointer
  while curr:
    if isOdd:
      odd.next = curr
      odd = curr
    else:
      even.next = curr
      even = curr

    isOdd = not isOdd   # toggle flag
    curr = curr.next    # advance pointer

  even.next = None      # new list tail
  odd.next = even_head  # bridge odd's tail to even's head
  return head


if __name__ == "__main__":
  print("Enter space-separated integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))

  head = adt.array_to_list(nums)
  print(head)

  head = oddEvenList(head)
  print(head)
