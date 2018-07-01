## Problem
Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

## Examples
```
Input: "()"
Output: true

```
```
Input: "()[]{}"
Output: true
```

```
Input: "(]"
Output: false
```

```
Input: "([)]"
Output: false
```

```
Input: "{[]}"
Output: true
```

[Source](https://leetcode.com/problems/valid-parentheses/description/)
