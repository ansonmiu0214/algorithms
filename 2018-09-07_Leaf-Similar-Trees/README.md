## Problem
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

![example-image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

**Note:**
Both of the given trees will have between 1 and 100 nodes.

[Source](https://leetcode.com/problems/leaf-similar-trees/description/)

## Approach
Recursive approach to first find the leaves then compare the arrays. Base cases defined on the empty tree and the leaf, where the `getLeaves` function always returns a list of node values.

* O(m + n) running time complexity, where m and n are the number of nodes in root1 and root2 respectively
* O(1) space complexity with implicit stack space for recursion
