## Problem
Given an array of citations __sorted in ascending order__ (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index `h` if `h` of his/her `N` papers have __at least__ `h` citations each, and the other `N − h` papers have __no more than__ `h` citations each."

**Note:** 
If there are several possible values for h, the maximum one is taken as the h-index.

**Follow up:**
* This is a follow up problem to [H-Index](https://leetcode.com/problems/h-index/description/), where `citations` is now guaranteed to be sorted in ascending order.
* Could you solve it in logarithmic time complexity?

## Example
```
Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

[Source](https://leetcode.com/problems/h-index-ii/description/)

## Approach
Take advantage of the sorted list of `citations` to interpret the h-index differently.

```
h-index(citations) = x <==> citations[n-x-1] <= x && citations[n-x] >= x 

where n = len(citations)
```

Let `idx` = `n-x`.
Apply an iterative binary search approach to find `idx` that satisfies the condition and return `x` through computing `x = n - idx`.

* O(log(n)) running time complexity through binary search
* O(1) space complexity only using left/right pointers
