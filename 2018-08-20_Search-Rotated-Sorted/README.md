## Problem
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of `O(log n)`.

## Examples
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

[Source](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

## Approach
Iterative divide-and-conquer algorithm based on binary search.
At least 1 of the 2 partitions must be sorted, so use nums[left], nums[mid], nums[right] to determine and run binary search on that partition iteratively, shrinking the window defined by the left/right pointers.

* O(log(n)) running time complexity
* O(1) space complexity
