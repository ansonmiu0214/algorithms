## Problem
Given a string containing only three types of characters: `'('`, `')'` and `'*'`, write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
2. Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
3. Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
4. `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string.
5. An empty string is also valid.

**Note:** The string size will be in the range [1,100].

## Examples
```
Input: "()"
Output: True
```
```
Input: "(*)"
Output: True
```
```
Input: "(*))"
Output: True
```

[Source](https://leetcode.com/problems/valid-parenthesis-string/description/)

## Approach
Dynamic programming approach - optimal substructure defined on the predicate valid[i][j], which is true iff s[i]...s[j] forms a valid parenthesis.

Base cases on the diagonal and upper diagonal: valid[i][i] can only be true for the empty string (where s[i] == '*'), and valid[i][i+1] holds iff s[i] can be an opening and s[j] can be a closing. To refine the logic with the wildcard, valid[i][i+1] holds iff s[i] is not a closing and s[j] is not an opening.

For other values, valid[i][j] relies on the filled in cells of the table. Either:
* s[i] can open, s[j] can close, and s[i+1]...s[j-1] os valid
* There is some k such that s[i]...s[k] and s[k+1]...s[j] are valid.

A special case is if s[i] is the wildcard, which can be an empty string, in which case if s[i+1]...s[j] is a valid parenthesis string, then s[i]...s[j] is too.

Given that n is the length of the input string, the complexity analysis is as follow:

* O(n) upper diagonal base case init + (O(n^2) table loop * O(n) innermost loop for all possible ks) = O(n^3) running time complexity
* O(n^2) space complexity for table

