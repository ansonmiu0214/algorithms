## Problem
Given a binary tree, return the __level order traversal__ of its nodes' values. (i.e., from left to right, level by level).

## Example
```
Input:
    3
   / \
  9  20
    /  \
   15   7

Output:
[
  [3],
  [9,20],
  [15,7]
]
```

[Source](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

## Approach
Breadth-first search approach with queue.

* O(n) running time complexity, where n refers to the number of nodes.
* O(n) space complexity, since the queue is at most the maximum width of the tree at any given time.
