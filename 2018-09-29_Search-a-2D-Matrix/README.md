## Problem
Write an efficient algorithm that searches for a value in an `m` x `n` matrix. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

## Examples
```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```
```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

[Source](https://leetcode.com/problems/search-a-2d-matrix/description/)

## Approach
Take advantage of the sorted nature of the 2D matrix to apply binary search to first find the target row, then apply binary search on the target row to find the cell.

* O(log(m) + log(n)) running time complexity for 2 instances of binary search
* O(1) space complexity for lo/hi variables
