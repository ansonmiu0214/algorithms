## Problem
Given the `root` node of a binary search tree, return the sum of values of all nodes with value between `L` and `R` (inclusive).

The binary search tree is guaranteed to have unique values.

**Note:**
1. The number of nodes in the tree is at most `10000`.
2. The final answer is guaranteed to be less than `2^31`.

## Examples
```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
```
```
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

[Source](https://leetcode.com/problems/range-sum-of-bst/)

## Approach
Recursive approach with base case defined on the empty node - just return 0.
A non-empty node can either be part of the range or not.

If it is part of the range, its children can be part of the range too. Recurse into both branches and sum the values along with the node's value.

If not, then one of the children is part of the range. Recurse into the left if the current node value exceeds the upper bound, and the right if the current node value is below the lower bound.


