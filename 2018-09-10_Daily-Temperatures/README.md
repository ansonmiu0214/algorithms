## Problem
Given a list of daily `temperatures`, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.

**Note:**
The length of temperatures will be in the range	`[1, 30000]`. Each temperature will be an integer in the range `[30, 100]`.

## Example
```
Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

[Source](https://leetcode.com/problems/daily-temperatures/description/)

## Approach
Dynamic programming approach but filling in the result array in reverse, since the last element of the result array is the trivial base case (no day warmer than the last day, so that result element is 0).

The worst case input would be one where the while loop will need to traverse every element (and thus, increment j at every traversal). It can be proven that this traversal can only happen at most once for the whole `temperatures` list, thus results in at most O(2n) running time performance, which falls under O(n).

Let `temperatures = [..., x, 10, 1, 2, 3, 4, ..., 9]`
When computing res[i] where temperatures[i] = 10, it is clear that the while loop will visit each element in the subarray [1, 2, 3, 4, ..., 9], which is the worst case traversal as mentioned above.

The element, x, can either be < 10 or >= 10.
1. If x < 10, then the while loop will be skipped since a warmer temperature is already found.
2. If x >= 10, then the while loop runs only once, because x will then compare with the last temperature in the list at index k where k = len(temperatures) - 1, but res[k] = 0 which terminates the loop.

Any element preceding x follows the same argument as above, so the running time is at most (1 * (n - 1)) + (n * 1) = 2n - 1, resulting in O(n) performance.

* O(n) running time complexity where n = len(temperatures), as analysed above
* O(1) space complexity since the result must be in a separate list anyway, so no additional space incurred
