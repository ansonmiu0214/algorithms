## Problem
You have a list of `words` and a `pattern`, and you want to know which `words` in words matches the pattern.

A word matches the pattern if there exists a permutation of letters `p` so that after replacing every letter `x` in the pattern with `p(x)`, we get the desired word.

__(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)__

Return a list of the words in `words` that match the given pattern. 

You may return the answer in any order.

## Example
```
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
```

[Source](https://leetcode.com/problems/find-and-replace-pattern/description/)

## Approach
Validate word by word, using 2 dictionaries to validate the bijection and take advantage of constant time lookups at the cost of incurred space.

Given that n = len(pattern) and m = len(words), the complexity analysis is as follow:
* O(1) dictionary lookups * O(n) lookups per letter * O(m) validations per word = O(mn) running time complexity
* O(2n) space complexity for 2 dictionaries to keep track of bijection = O(n) space complexity 
