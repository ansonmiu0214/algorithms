## Problem
Given a linked list, rotate the list to the right by `k` places, where `k` is non-negative.

## Example
```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```
```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

[Source](https://leetcode.com/problems/rotate-list/description/)

## Approach
Break down the problem logically.
1. Find the length of the linked list through pointer traversal, capturing the nodes in an array.
2. Compute the index of the new head through modulo.
3. Redirect the old tail's next pointer to the head to form a circular linked list.
4. Update the next pointer of the new tail (found by nodes[new_head_idx-1]) to point to None to break the cycle.

Given that the linked list has `n` nodes, the complexity analysis is as follow:
* O(n) linked list traversal + O(1) mod calculation + O(1) `next' pointer update = O(n) running time complexity
* O(n) space complexity for storing the nodes

An alternative implementation for the same algorithm would be to not use the array to save space, but the `next' pointer updates will incur O(n) running time as well, although O(2n) running time is still O(n).
