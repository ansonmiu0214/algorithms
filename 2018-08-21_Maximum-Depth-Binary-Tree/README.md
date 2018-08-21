## Problem
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Note**: A leaf is a node with no children.

## Example
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```
return its depth = 3

[Source](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

## Approach
Recursive solution with base case defined on `None`.

* O(n) running time complexity because there is no precondition that the input tree is balanced; if such precondition exists, this would have O(log(n)) running time complexity
* O(1) space complexity

