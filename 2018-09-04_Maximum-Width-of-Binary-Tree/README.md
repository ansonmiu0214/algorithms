## Problem
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a **full binary tree**, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the `null` nodes between the end-nodes are also counted into the length calculation.

## Examples
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```
```
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```
```
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```
```
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```

[Source](https://leetcode.com/problems/maximum-width-of-binary-tree/description/)

## Approach
Breadth-first search approach to achieve level-order traversal. Use difference between node indices to keep track of width. For a node with index i, its left- and right-child have index 2\*i+1 and 2\*i+2 respectively. This method allows the computed width to account for the null nodes in between the end nodes, and the algorithm does not have to generate arbitrary null nodes to make up for those gaps.

* O(n) running time complexity, where n is the number of non-null nodes within the tree.
* O(n) space complexity for the queue
