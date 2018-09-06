## Problem
We are given the head node `root` of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

**Note:**
* The binary tree will have at most 100 nodes.
* The value of each node with only be 0 or 1.

## Examples
```
Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```
![example_1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

```
Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```
![example_2](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

```
Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```
![example_3](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

[Source](https://leetcode.com/problems/binary-tree-pruning/description/)

## Approach
Recursive approach, making sure that _the recursive calls are made first_ before assessing whether the node should be deleted. The base cases are the empty node (where it is simply returned), and a leaf node with value 0 (where the empty node should be returned as it should be deleted from the tree).

* O(n) running time complexity, where n is the number of nodes
* O(1) space complexity with implicit stack space for the recursive calls
