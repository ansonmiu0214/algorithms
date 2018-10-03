## Problem
Given an absolute path for a file (Unix-style), simplify it. 

In a UNIX-style file system, a period (`'.'`) refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period (`".."`) moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

**Corner cases:**
* Did you consider the case where path = `"/../"`? In this case, you should return `"/"`.
* Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`. In this case, you should ignore redundant slashes and return `"/home/foo"`.

## Examples
```
path = "/home/", => "/home"
```
```
path = "/a/./b/../../c/", => "/c"
```
```
path = "/a/../../b/../c//.//", => "/c"
```
```
path = "/a//b////c/d//././/..", => "/a/b/c"
```

[Source](https://leetcode.com/problems/simplify-path/description/)

## Approach
Stack-based approach, with preprocessing on path string by tokenising path components
through the `'/'` delimiter to extract directories and eliminate extraneous `'/'` characters simultaneously.
Going 'up' a folder pops the stack (if non-empty). The simplified path is obtained by joining the remaining
elements of the stack with `'/'`.

Given that the path has `n` components, the complexity analysis is as follow:
* O(n) running time complexity
* O(n) space complexity, since worst case can be going down `n` folders deep
