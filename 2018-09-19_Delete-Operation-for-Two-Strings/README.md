## Problem
Given two words `word1` and `word2`, find the minimum number of steps required to make `word1` and `word2` the same, where in each step you can delete one character in either string.

**Note:**
1. The length of given words won't exceed 500.
2. Characters in given words can only be lower-case letters.

## Example
```
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```

[Source](https://leetcode.com/problems/delete-operation-for-two-strings/description/)

## Approach
Adapt the Levenshtein distance algorithm as follow:
1. Treat insertion as deletion (inserting into another word is equivalent to deleting from the original word).
2. Deletion is treated as is.
3. Replacement is treated as two deletions, or to be more verbose, replacing both characters with the empty string.

Given that m = len(word1) and n = len(word2), the complexity analysis is as follow:
* O(mn) running time complexity
* O(mn) space complexity
