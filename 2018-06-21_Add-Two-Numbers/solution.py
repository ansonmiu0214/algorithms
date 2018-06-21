#!/bin/python3

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
   def addTwoNumbers(self, l1, l2):
      """
      :type l1: ListNode
      :type l2: ListNode
      :rtype: ListNode
      """
        
      if l1 is None and l2 is None:
          return None
        
      left, right = l1, l2
      carry = 0
        
      head = prev = None
      while left is not None or right is not None:
          total = carry
          if left is not None:
              total += left.val
              left = left.next
                
          if right is not None:
              total += right.val
              right = right.next
                
          # update carry
          carry = total // 10
          
          # normalise total
          total = total % 10
            
          curr = ListNode(total)
          if prev is not None:
              prev.next = curr
          else:
              head = curr
                
          prev = curr
        
        
      if carry > 0:
        prev.next = ListNode(carry)
    
      return head
