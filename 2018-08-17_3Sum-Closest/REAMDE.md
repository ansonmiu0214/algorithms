## Problem
Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## Example
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

[Source](https://leetcode.com/problems/3sum-closest/description/)

## Approach
Same strategy as 3Sum (examine all possible 'starters' and apply O(n) 2-sum algorithm on the rest of the array, but keep track of the minimum absolute difference w.r.t. target.

* O(n) possible 'starters' * O(n) for running 2 sum on each starter = O(n^2) running time complexity
* O(1) space complexity for minimum absolute difference variable
