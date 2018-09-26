## Problem
Given a binary tree and a sum, find all __root-to-leaf__ paths where each path's sum equals the iven sum.

**Note:** A leaf is a node with no children.

## Example
Given the folloiwng binary tree and `sum = 22`:
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```
Return:
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

[Source](https://leetcode.com/problems/path-sum-ii/description/)

## Approach
Iterative approach through exploring path sums by breadth-first search. Only compare sum-so-far with the target value when leaf node reached.

Given that there are n nodes in the tree, the complexity analysis is as follow:
* O(n) traversal * O(1) addition per traversal = O(n) running time complexity
* O(n) space complexity for queue
