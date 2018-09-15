## Problem
Given an array of integers `nums` and an integer `k`, you need to find the total number of continuous subarrays whose sum equals to `k`.

**Note:**
1. The length of the array is in range [1, 20000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integers `k` is [-1e7, 1e7].

## Example

[Source](https://leetcode.com/problems/subarray-sum-equals-k/description/)

## Approach
Use the cumulative sum approach to compute all possible subarray sums in with O(n^) running time complexity, and make use of this being defined on all possible starting/stopping indices to compute the running total within those loops to eliminate any space required for a cumulative sum array.

* O(n) possible starting indices * O(n-1) possible ending indices per start = O(n^2) running time complexity
* O(1) space complexity
