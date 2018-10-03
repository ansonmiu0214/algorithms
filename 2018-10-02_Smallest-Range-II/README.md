## Problem
Given an array `A` of integers, for each integer `A[i]` we need to choose either `x = -K` or `x = K`, and add `x` to `A[i]` (only once).

After this process, we have some array `B`.

Return the smallest possible difference between the maximum value of `B` and the minimum value of `B`.

**Note:**
1. `1 <= A.length <= 10000`
2. `0 <= A[i] <= 1000
3. `0 <= K <= 10000`

## Examples
```
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
```
```
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
```
```
Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
```

[Source](https://leetcode.com/problems/smallest-range-ii/description/)

## Approach
Make the list sorted first, so `A[0] <= ... <= A[n-1]`. Recognise that `A[i] += K` is equivalent to `A[i] += {0, 2*K}`. Iterate through the list and attempt to add 2*K to A[i] to reduce the range.

In each iteration:
1. Local maximum would either be the tail or A[i] + 2K - this is because there is no need to consider A[-1] + 2K as A[-1] is maximum by default.
2. Local minimum would either be the next item we do not modify (`A[i+1]`) or `A[0] + 2K` - this is because we are trying to minimise the range, so there is no need to consider A[0] + 0 as A[0] is already the minimum by default.

* O(n(log(n))) running time complexity for library sort
* O(1) space using in-place library sort

