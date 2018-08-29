## Problem
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

**Note:**
* If there is no such window in S that covers all characters in T, return the empty string `""`.
* If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## Example
```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

[Source](https://leetcode.com/problems/minimum-window-substring/description/)

## Approach
Sliding window approach with the use of dictionaries and sets to keep track of letter frequency since t can contain duplicate letters. Extend window if match not found and shrink window if match found to find smaller window that still matches.

Given that M = len(s) and N = len(T), the complexity analysis is as follow:
* O(N) patternFreq setup + O(M) windowFreq setup + O(M) lettersMatched init + (O(M) sliding window * O(1) dictionary lookups) = O(M + N) running time complexity
* O(N) patternFreq size + O(M) windowFreq size + O(N) lettersMatched size = O(M + N) space complexity
