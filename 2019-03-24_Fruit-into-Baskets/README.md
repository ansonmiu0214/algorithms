## Problem
In a row of trees, the `i`-th tree produces fruit with type `tree[i]`.

You start at any tree of your choice, then repeatedly perform the following steps:

1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

**Note:**
1. `1 <= tree.length <= 40000`
2. `0 <= tree[i] < tree.length`

## Examples
```
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
```
```
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0,1].
```
```
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2]. 
If we started at the first tree, we would only collect [1,2].
```
```
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
```

[Source](https://leetcode.com/problems/fruit-into-baskets/)

## Approach
This problem reduces to finding the length of the longest subarray that contains at most 2 unique elements.

Dynamic programming approach: in general, solutions to problems of this type can be defined inductively. This problem relates to subarrays rather than subsequences, so suffices to just keep track of the immediate previous solution rather than a table of previous solutions. 

For each index, keep track of the length of the longest subarray that contains at most 1 unique element, at most 2 unique elements along with that 2nd unique element.

Trivial solution starting from tree[n-1] - can only collect 1.
For a solution starting from tree[i]:

* If `tree[i] == tree[i+1]`, extend all counts
* If `tree[i] != tree[i+1]` but `tree[i]` is the same element as the 2nd element of the longest subarray of 2 unique starting from `tree[i+1]`, extend that particular count
* Otherwise, reset all counts


* O(n) time complexity
* O(1) space complexity for the accumulators

