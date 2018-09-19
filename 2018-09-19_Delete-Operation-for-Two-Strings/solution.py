#!/bin/python3

"""
Use Levenshtein distance approach by interpreting the 3 operations w.r.t. pure deletion:
1. Inserting into word1 = deletion from word2
2. Deletion from word1 = [as is]
3. Replace x in word1 with y = delete x from word1 and delete y from word2
"""
def minDistance(word1, word2):
  m, n = len(word1), len(word2)
  
  # setup DP table
  table = [[max(x, y) if x == 0 or y == 0 else 0 for y in range(n+1)] for x in range(m+1)]

  for row in range(1, m+1):
    this = word1[row-1]

    for col in range(1, n+1):
      that = word2[col-1]

      if this == that:
        # no deletion required
        table[row][col] = table[row-1][col-1]
      else:
        # choose minimum from 3 possible delete cases
        delFromOne = table[row-1][col] + 1
        delFromTwo = table[row][col-1] + 1
        delBoth = table[row-1][col-1] + 2

        table[row][col] = min(delFromOne, delFromTwo, delBoth)

  return table[m][n]


if __name__ == "__main__":
  print("Enter space-separated word1 and word2: ", end="")
  word1, word2 = input().strip().split(' ')

  distance = minDistance(word1, word2)
  print("{} deletion operation{} required.".format(distance, "" if distance == 1 else "s"))
