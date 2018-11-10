## Problem
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.

![Example Image](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

## Example
```
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

[Source](https://leetcode.com/problems/n-queens/description/)

## Approch
Optimised backtracking algorithm column-by-column.
Keep track of 'threatened' cell indices to allow for backtracking when violation detected.
It is possible that one cell is threatened by multiple queens, so the threatened cell data structure needs to account for this and backtracking from one queen does not remove the entry if other queens on the board are still threatening that cell.

* O(n^n) running time complexity 
* O(n^2) space complexity - at most n^2 cells in the 'threatened' cells structure
