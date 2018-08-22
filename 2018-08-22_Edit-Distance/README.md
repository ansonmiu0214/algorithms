## Problem
Given two words `word1` and `word2`, find the minimum number of operations required to convert `word1` to `word2`.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

## Examples
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

[Source](https://leetcode.com/problems/edit-distance/description/)

## Approach
Dynamic programming approach using 2D table where table[x][y] = editDistance(word1[:x], word2[:y]).
Base cases defined on table[x][y] = max(x,y) where x == 0 or y == 0 because you must insert/delete that many letters to convert between the word and the empty string.
Other cases consider the editDistance scenarios of insert/delete/replace/do-nothing and pick the optimal answer with min(...).

* O(mn) running time complexity where m = len(word1) and n = len(word2)
* O(1) space complexity
