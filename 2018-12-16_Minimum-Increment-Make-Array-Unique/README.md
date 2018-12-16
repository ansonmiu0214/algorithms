## Problem
Given an array of integers `A`, a _move_ consists of choosing any `A[i]`, and incrementing it by 1.

Return the least number of moves to make every value in `A` unique.

## Examples
```
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
```
```
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
```

[Source](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)

## Approach
Greedy approach: sort in ascending order and iterate through, keeping track of last seen number so the minimum increment is the amount needed to update the current element to an unseen number.

* O(n(log(n))) sorting + O(n) traversal = O(n(log(n))) running time complexity
* O(1) space complexity (due to using in-place sorting)
