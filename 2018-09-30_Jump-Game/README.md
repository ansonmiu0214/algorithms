## Problem
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

## Examples
```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
```

[Source](https://leetcode.com/problems/jump-game/description/)

## Approach
Since the jump intervals are non-negative, a greedy approach
can be taken to keep track of the furthest index that can be reached.
This index is updated as the function iterates through the array,
and will terminate when the end is reached or when an unreachable index
is reached (detected when the maximum index reachable is less than the
current index).

* O(n) running time complexity
* O(1) space complexity
