## Problem
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

## Examples
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:

P   A   H   N
A P L S I I G
Y   I   R
```
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

[Source](https://leetcode.com/problems/zigzag-conversion/description/)

## Approach
Iteratively organise characters into the correct rows and read off line by line. Keep track of correct row using `row` variable and emulate behaviour of on-column or on-diagonal using `diag` boolean flag.

* `O(n)` running time complexity.
* `O(n)` space complexity.
