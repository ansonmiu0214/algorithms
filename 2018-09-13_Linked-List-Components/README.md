## Problem
We are given `head`, the head node of a linked list containing **unique integer values**.

We are also given the list `G`, a subset of the values in the linked list.

Return the number of connected components in `G`, where two values are connected if they appear consecutively in the linked list.

**Note:**
* If `N` is the length of the linked list given by `head`, `1 <= N <= 10000`.
* The value of each node in the linked list will be in the range `[0, N - 1]`.
* `1 <= G.length <= 10000`.
* `G` is a subset of all values in the linked list.

## Examples
```
Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
```
```
Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
```

[Source](https://leetcode.com/problems/linked-list-components/description/)

## Approach
Iterative approach using a pointer to traverse the linked list and a boolean flag to keep track of connected components over the iteration, since seeing 3 consecutive elements within the array counts as 1 single connected component.

* O(n) running time complexity, where n is the length of the linked list
* O(m) space complexity, where m is the size of G - this is used to create a new set from the list G to benefit from O(1) set lookups, but at the cost of this extra space; the alternative would be to keep the array as it is, which leads to O(1) space complexity but O(nm) running time complexity due to O(m) membership lookups in the array
