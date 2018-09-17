## Problem
Given the `root` of a binary tree, then value `v` and depth `d`, you need to add a row of nodes with value `v` at the given depth `d`. The root node is at depth 1.

The adding rule is: given a positive integer depth `d`, for each NOT null tree nodes `N` in depth `d-1`, create two tree nodes with value `v` as `N`'s left subtree root and right subtree root. And `N`'s __original left subtree__ should be the left subtree of the new left subtree root, its __original right subtree__ should be the right subtree of the new right subtree root. If depth `d` is 1 that means there is no depth `d-1` at all, then create a tree node with value `v` as the new root of the whole original tree, and the original tree is the new root's left subtree.

**Note:**
1. The given d is in range [1, maximum depth of the given tree + 1].
2. The given binary tree has at least one tree node.

## Examples
```
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

```
```
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
```

[Source](https://leetcode.com/problems/add-one-row-to-tree/description/)

## Approach
Using level order traversal to reach depth d-1 for modification. Edge cases of an empty tree and modifying at root depth are handled separately. Level order traversal achieved by using a queue to iterate through nodes. Traversal shortcircuits at depth d since there is no need to modify nodes beyond the depth.

* O(n) running time complexity where n is the number of nodes in the tree, and this worst case occurs when inserting into the maximum depth of the tree
* O(2^d) space complexity, since there is at most 2^d nodes at depth d of a complete binary tree and this space is incurred when visiting that level
