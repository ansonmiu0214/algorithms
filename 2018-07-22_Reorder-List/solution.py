#!/bin/python3

import sys
sys.path.append('../')

import adt

def reorderList(head):
  if not head:  return

  # first pass to get all nodes
  res = []
  curr = head
  count = 0
  while curr:
    res.append(curr)
    curr = curr.next
    count += 1

  left, right = 0, count - 1
  forward = True

  # relink until converge
  while left != right:
    if forward:
      res[left].next = res[right]
      left += 1
    else:
      res[right].next = res[left]
      right -= 1

    # toggle
    forward = not forward

  # create new end of list
  res[left].next = None


if __name__ == "__main__":
  print("Enter space-separted integers: ", end="")
  nums = list(map(int, input().strip().split(' ')))
  head = adt.array_to_list(nums)

  print(head)
  reorderList(head)
  print(head)
