#!/bin/python3

"""
Dynamic programming solution with recurrence equation:
coinChange(n) = coinChange(n-coin) for each coin in denomination.
"""
def coinChange(amount, coins):
  nums = len(coins)

  # base case: 1 (trivial) way to make $0
  table = [1] + [0 for _ in range(amount)]

  for coin in coins:
    for val in range(coin, amount + 1):
      table[val] += table[val - coin]
  
  return table[amount]


if __name__ == "__main__":
  print("Enter amount: ", end="")
  amount = int(input().strip())

  print("Enter space-separated coin denomination: ", end="")
  coins = list(map(int, input().strip().split(' ')))
 
  res = coinChange(amount, coins)
  print("{} way{} to make ${} with {}".format(res, "" if res == 1 else "s", amount, coins))
