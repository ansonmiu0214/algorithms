#!/bin/python3

class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None
    self.child = None

  def __repr__(self):
    res = str(self.val)
    if self.next:
      res += " -> {}".format(str(self.next))
  
    if self.child:
      res += "\n{}".format(str(self.child))

    return res


"""
Recursive approach.
"""
def flatten(head):
  if not head:
    return head

  if head.next:
    head.next = flatten(head.next)

  if head.child:
    # flatten child
    child = flatten(head.child)
    
    # connect end of flattened child to head's next
    curr = child
    while curr.next:
      curr = curr.next

    # amend pointers (next and prev if necessary)
    curr.next = head.next
    if head.next:
      head.next.prev = curr

    # head should point to children next
    head.next = child
    child.prev = head

    # clear children
    head.child = None

  return head



if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.child = Node(7)
  head.child.next = Node(8)

  print("Original:")
  print(head)

  head = flatten(head)

  print("Flattened:")
  print(head)
