## Problem
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Example
```
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

[Source](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)

## Approach
Recursive approach with base cases defined on the empty list and singleton list. Height balance maintained by recursing on left/right partitions defined by the midpoint of the list. The midpoint is found through applying the tortoise-hare algorithm.

* O(n(log(n))) running time complexity defined by the recurrence equation T(n) = 2T(n/2) + O(n) for recursion and finding the midpoint respectively
* O(1) space complexity for pointers
