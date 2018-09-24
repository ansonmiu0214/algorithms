## Problem
Given a collection of intervals, merge all overlapping intervals.

## Examples
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```
```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
```

[Source](https://leetcode.com/problems/merge-intervals/description/)

## Approach
Greedy method - sort the list of intervals lexicographically and always compare 2 successive intervals (kept in a queue).

If they can be merged, replace the current with the merged interval. Else, append the current to the result array (guaranteed no more merge opportunities) and continue the process with the next interval as current.

Given that there are n intervals to merge, the complexity analysis is as follow:
* O(n(log(n))) sorting + O(n) loop = O(n(log(n))) running time complexity
* O(n) space for sorted list + O(n) queue = O(n) space complexity
