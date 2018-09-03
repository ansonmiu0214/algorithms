## Problem
Given a tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

**Note:**
1. The number of nodes in the given tree will be between 1 and 100.
2. Each node will have a unique integer value from 0 to 1000.

## Example
```
Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
```

[Source](https://leetcode.com/problems/increasing-order-search-tree/description/)

## Approach
Recursive approach with base case defined on the empty tree. Pointer manipulation required to make root node be the rightmost child of the processed left subtree.

* O(n) running time complexity, where n is the number of nodes in the tree
* O(1) space complexity with implicit stack space used for recursive calls
