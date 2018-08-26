## Problem
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

**Note:** Your solution should run in O(log(n)) time and O(1) space.

## Examples
```
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
```
```
Input: [3,3,7,7,10,11,11]
Output: 10
```

[Source](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)

## Approach
Binary search approach with case-by-case analysis on how the midpoint partitions the array (e.g. if midpoint partitions array into odd-length sublists, recurse to right iff nums[mid] == nums[mid-1]), with the base case defined on the singleton array. Iterative implementation using `left`/`right` pointers eliminate recursion stack overhead.

* O(log(n)) running time complexity, where n = len(nums)
* O(1) space complexity
