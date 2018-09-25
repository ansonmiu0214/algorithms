## Problem
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
```
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
```

**Note:**
* All of the nodes' values will be unique.
* `p` and `q` are different and both values will exist in the binary tree.

## Examples
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
```
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

[Source](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

## Approach
Compute parent information of all nodes through level order traversal. Traverse the paths from p and q to the root respectively, keeping track of the seen nodes; the first common seen node will be the LCA.

Given that there are n nodes in the tree, the complexity analysis is as follow:
* O(n) tree traversal + O(n) backtrack since problem did not state balanced tree so worst case would be a linked list = O(n) running time complexity
* O(n) space complexity for storing parent information per node

