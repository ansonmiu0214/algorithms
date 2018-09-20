## Problem
A robot is located at the top-left corner of a `m` x `n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![illustration](https://leetcode.com/static/images/problemset/robot_maze.png)

## Examples
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```
```
Input: m = 7, n = 3
Output: 28
```

[Source](https://leetcode.com/problems/unique-paths/description/)

## Approach
Bottom-up dynamic programming approach, where the DP table entry `numPaths[x][y]` is the solution to uniquePaths with inputs x+1 and y+1 (due to array indexing differences). Base case defined on the rightmost and bottom edges, since given the moves result in only one trivial way to reach the finish cell (by following the edge).

* O(mn) running time complexity (to fill the table)
* O(mn) space complexity (for the table)
