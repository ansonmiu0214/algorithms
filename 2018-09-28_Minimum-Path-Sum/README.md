## Problem
Given a m x n `grid` filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

## Example
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

[Source](https://leetcode.com/problems/minimum-path-sum/description/)

## Approach
Dynamic programming approach, with base cases on the left- and top-edges.
1. Top-left corner := min path sum is trivial
2. Top row := must come from cell to the left
3. Leftmost column: must come from cell above
4. Rest := min(from\_above, from\_left) + cell value

* O(mn) running time complexity
* O(mn) space complexity
