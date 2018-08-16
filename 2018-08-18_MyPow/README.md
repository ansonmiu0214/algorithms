## Problem
Implement `pow(x, n)`, which calculates x raised to the power n (xn).

**Note:**
* -100.0 < x < 100.0
* n is a 32-bit signed integer, within the range [−231, 231 − 1]

## Examples
```
Input: 2.00000, 10
Output: 1024.00000
```
```
Input: 2.10000, 3
Output: 9.26100
```
```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/(2^2) = 1/4 = 0.25
```

[Source](https://leetcode.com/problems/powx-n/description/)

## Approach
Divide-and-conquer recursive approach with base case where n = 0, with special care taken on handling negative powers at the top level, since divmod(-1,2) = (-1,1) will cause an infinite loop, so the power to recurse on must not be negative.

* O(log(n)) running time complexity with recurrence equation T(n) = T(n/2) + O(1)
* O(1) space complexity
