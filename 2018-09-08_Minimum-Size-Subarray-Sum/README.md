## Problem
Given an array of `n` positive integers and a positive integer `s`, find the minimal length of a contiguous subarray of which the sum ≥ `s`. If there isn't one, return `0` instead.

## Example
```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

[Source](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

## Approach
Greedy sliding window approach - extend window if subarray sum < s, shrink window otherwise, and keep track of the minimum-sized window.

* O(n) running time complexity where n = len(nums)
* O(1) space complexity for pointer variables used to define window
