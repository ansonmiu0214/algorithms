## Problem
We have a string `S` of lowercase letters, and an integer array `shifts`.

Call the _shift_ of a letter, the next letter in the alphabet, (wrapping around so that `'z'` becomes `'a'`). 

For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.

Now for each `shifts[i] = x`, we want to shift the first `i+1` letters of `S`, `x` times.

Return the final string after all such shifts to `S` are applied.

**Note:**
1. `1 <= S.length = shifts.length <= 20000`
2. `0 <= shifts[i] <= 10 ^ 9`

## Example
```
Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
```

[Source](https://leetcode.com/problems/shifting-letters/description/)

## Approach
Avoid doing O(n^2) work by preprocessing `shifts` array to compute the
cumulative shift per letter, then applying them all at once. Wraparound from 'z' to 'a'
handled by applying modulo to the new index (computed w.r.t. 0 at first before offsetting
by ord('a') to get the required ordinal value).

* O(n) preprocessing + O(n) traversal to get new letters = O(n) running time complexity
* O(n) space complexity for storing new cumulative shifts
