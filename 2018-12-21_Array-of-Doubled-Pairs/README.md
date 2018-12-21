## Problem
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that `A[2 * i + 1] = 2 * A[2 * i]` for every `0 <= i < len(A) / 2`.

**Note:**
1. `0 <= A.length <= 30000`
2. `A.length` is even
3. `-10000 <= A[i] <= 100000`

## Examples
```
Input: [3,1,3,6]
Output: false
```
```
Input: [2,1,2,6]
Output: false
```
```
Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
```
```
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.
```

## Approach
Greedy approach: make use of element frequencies and proceed with the constraint that, if there are x occurrences of n, then there must be at least x occurrences of 2n in the array. Remove these occurrences (as they are matched), then proceed until all possible removals are made. The array can be reordered if there are no more elements at the end. Edge case of 0s are ignored (since 0\*0 = 0), so just need to enforce there is an even number of 0s.

* O(n) array iteration + O(n(log(n))) sorting + O(n) dict iteration = O(n(log(n))) running time complexity
* O(n) space complexity for dict frequency table
