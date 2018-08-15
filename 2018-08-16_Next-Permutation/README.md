## Problem
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

## Examples
```
1,2,3 → 1,3,2
```
```
3,2,1 → 1,2,3
```
```
1,1,5 → 1,5,1
```

[Source](https://leetcode.com/problems/next-permutation/description/)

## Approach
1. Look for the element that needs to move: from right to left, find index i such that nums[i] < nums[i+1]
2. Need to find the new value for nums[i]: since nums[i+1:] is guaranteed to be in descending order, scan from right to left to find index j such that nums[j] > nums[i]
3. Swap values in nums[i] and nums[j]
4. nums[i+1:] now needs to be in ascending order (for smallest lexicographic order), so reverse nums[i+1:].

* O(n) search-for-i + O(n) search-for-j + O(1) swap + O(n) reverse = O(n) running time complexity
* O(1) space complexity with index variables and array element pointers
