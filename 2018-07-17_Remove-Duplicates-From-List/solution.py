#!/bin/python3

import sys
sys.path.append('../')

import adt

def deleteDuplicates(head):
  if head is None:  return None

  # dummy head node
  dummy = adt.ListNode('0')
  dummy.next = head

  prev = dummy
  while prev.next:
    # set up window of same values
    end = curr = prev.next
    val = curr.val

    # move pointer until end or values differ
    while end.next and end.next.val == val:
      end = end.next

    if curr == end:
      # no deletion - move to next
      prev = curr
    else:
      # delete [curr, end]
      prev.next = end.next

  return dummy.next


if __name__ == "__main__":
  print("Enter space-separated numbers: ", end="")
  nums = sorted(list(map(int, input().strip().split(' '))))

  head = adt.array_to_list(nums)
  print(head)

  head = deleteDuplicates(head)
  print(head)
