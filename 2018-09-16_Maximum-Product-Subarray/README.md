## Problem
Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

## Examples
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

[Source](https://leetcode.com/problems/maximum-product-subarray/description/)

## Approach
Same strategy as maximum subarray sum - keep track of local max and local min and determinethe next local max/min using the previous result, where the choices are either to extend the link (i.e. prevMax * curr) or start a new subarray (i.e. curr).

* O(n) running time complexity, where n = len(nums)
* O(1) space complexity 
