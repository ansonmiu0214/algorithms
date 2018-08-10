#!/bin/python3

"""
DP approach. O(n) running time complexity and space complexity.
Identify base cases for 1- and 2-digit numbers.
Edge cases with 0 (false), multiples of 10 (1 way).
"""
def numDecodings(s):
  count = len(s)
  
  # initialise array
  table = [None for _ in range(count)]

  def decode(s, curr, end):
    if curr == end:
      return False, 0

    if table[curr]:
      return table[curr]

    oneDigit = int(s[curr:(curr+1)])
    twoDigit = int(s[curr:(curr+2)])

    if curr + 1 == end:
      table[curr] = oneDigit != 0, 1 if oneDigit != 0 else 0
      return table[curr]

    if curr + 2 == end:
      valid, res = False, 0

      if twoDigit < 10:
        table[curr] = False, 0
        return table[curr]

      if twoDigit <= 26:
        if twoDigit % 10 == 0:
          valid, res = True, 1
        else:
          valid, res = True, 2

        table[curr] = valid, res
        return table[curr]

      if twoDigit % 10 != 0:
        valid, res = True, 1

      table[curr] = valid, res
      return table[curr]

    if oneDigit == 0:
      table[curr] = False, 0
      return table[curr]

    res = 0
    valid1, option1 = decode(s, curr+1, end)
    valid2, option2 = decode(s, curr+2, end)
    
    valid1 = valid1 and oneDigit > 0
    valid2 = valid2 and twoDigit > 0 and twoDigit <= 26

    if valid1:  res += option1
    if valid2:  res += option2

    table[curr] = valid1 or valid2, res
    return table[curr]

  valid, possible = decode(s, 0, count)
  return possible if valid else 0


if __name__ == "__main__":
  print("Enter number: ", end="")
  n = input().strip()

  ways = numDecodings(n)
  print("{} ways".format(ways))
