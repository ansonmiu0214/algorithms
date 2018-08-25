## Problem
Given a **non-empty** integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

## Example
```
Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
```

[Source](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)

## Approach
Identify that the optimal solution (minimising moves to equalise array elements) involves making them equal the median. Sorting the list allows us to find the median.

* O(n(log(n))) sorting + O(n) summation = O(n(log(n))) running time complexity
* O(1) space complexity due to in-place sorting
