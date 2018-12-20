## Problem
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each `node` of each tree in the answer **must** have `node.val = 0`.

You may return the final list of trees in any order.

**Note:**
* `1 <= N <= 20`

## Examples
```
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
```
![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png](Example)

## Approach
Bottom-up dynamic programming, identify the optimal substructure in the recurrence relation:
* allPossibleFBT(1) = [singleton node]
* allPossibleFBT(2) = []
* allPossibleFBT(n) = sum of ( allPossibleFBT(i) * allPossibleFBT(j) ) for all i, j such that i + j + 1 = n

* O(N) outer for loop * O(N) inner for loop = O(N^2) running time complexity
* O(N) space complexity for memoisation
