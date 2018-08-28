## Problem
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

**Note:** You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

## Examples
```
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.
```
```
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.
```

[Source](https://leetcode.com/problems/most-frequent-subtree-sum/description/)

## Approach
Recursively compute subtree sums and keep track of the sums' frequencies as well as the accmulator for the most frequent sum, with the base case defined on the subtree sum of a `None` node.

* O(n) subtree computation + O(1) return result = O(n) running time complexity where n is the number of nodes in the tree
* O(n) sum-to-frequency dictionary + O(1) highest frequency counter + O(n) result list = O(n) space complexity
