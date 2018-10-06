## Problem
Given a sorted integer array without duplicates, return the summary of its ranges.

## Examples
```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```
```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```

[Source](https://leetcode.com/problems/summary-ranges/description/)

## Approach
Iterative approach using 2 pointers to keep track of range.
While loop conditions handle any index out-of-bound runtime errors.

* O(n) running time complexity for traversal
* O(n) space complexity for result array, ignoring which would result in O(1) space complexity for the pointers
