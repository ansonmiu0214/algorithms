## Problem
Given an array `A`, partition it into two (contiguous) subarrays `left` and `right` so that:

* Every element in `left` is less than or equal to every element in `right`.
* `left` and `right` are non-empty.
* `left` has the smallest possible size.

Return the __length__ of `left` after such a partitioning.  It is guaranteed that such a partitioning exists.

**Note:**
1. `2 <= A.length <= 30000`
2. `0 <= A[i] <= 10^6`
3. It is guaranteed there is at least one way to partition `A` as described.

## Examples
```
Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```
```
Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
```

[Source](https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/)

## Approach
Looking for smallest `i` such that `max(A[:i]) <= min(A[i:])`.
Do preprocessing to calculate `max(A[:i])` and `min(A[i:])` first, then
iterate from `i = 0` upwards to find first successful `i`.

* O(n) preprocessing + O(n) iteration = O(n) running time complexity
* O(2n) arrays = O(n) space complexity
