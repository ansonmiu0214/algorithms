## Problem
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

**Note:** The total number of elements of the given matrix will not exceed 10,000.

## Example
```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:
![Diagonal_Traverse](https://leetcode.com/static/images/problemset/diagonal_traverse.png "Diagonal Traverse")
```

[Source](https://leetcode.com/problems/diagonal-traverse/description/)

## Approach
Encode the traversal logic using (row, col) to keep track of current coordinates and up to keep track of traversal direction, with edge cases of going out-of-bounds handled within the loop.

Given that M = len(matrix) and N = len(matrix[0]), the complexity analysis of this solution is as follow:
* O(MN) running time complexity
* O(1) space complexity with `row`, `col` and `up` variables

