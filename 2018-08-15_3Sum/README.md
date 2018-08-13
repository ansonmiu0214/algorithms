## Problem
Given an array nums of `n` integers, are there elements `a`, `b`, `c` in `nums` such that `a + b + c = 0`? Find all unique triplets in the array which gives the sum of zero.

**Note:** The solution set must not contain duplicate triplets.

## Example
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

[Source](https://leetcode.com/problems/3sum/description/)

## Approach
Iterate through all possible starting elements and run twoSum on the remainder of the list.Skip any duplicates when moving pointers to ensure no duplicate solutions are added to the solution set.

* `O(n(log(n))` sorting + (`O(n)` loop * `O(n)` two-sum) = `O(n^2)` running time complexity
* `O(1)` space complexity using built-in library in-place sort.
