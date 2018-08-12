## Problem
Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and `n` is at least 2.

## Example
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

[Source](https://leetcode.com/problems/container-with-most-water/description/)

## Approach
Start with window defined by the input list. Maintain window and maximum area accumulator. Greedily shrink the window depending on which side has the shorter line such that we look for a taller line with the potential of a greater area. 

* `O(n)` running time complexity
* `O(1)` space complexity
