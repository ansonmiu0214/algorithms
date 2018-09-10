## Problem
You are given `coins` of different denominations and a total `amount` of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Note:**
You may assume that you have an infinite number of each kind of coin.

## Examples
```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```
```
Input: coins = [2], amount = 3
Output: -1
```

[Source](https://leetcode.com/problems/coin-change/description/)

## Approach
Bottom-up dynamic programming approach solving the recurrence equation, where change(x) is the fewest number of coins needed to make $x.

1. change(0) = 0
2. change(x) = min{change(x - coin) + 1} for coin in coins

Given that there are C coins in the denomination, the complexity analysis is as follow:

* O(C*amount) running time complexity for the loops
* O(C*amount) space complexity for the DP table
