#!/bin/python3

from collections import deque

"""
Dynamic programming approach using 2D table and identifying the recurrence relation where
table[i][j] = distance for making word1[:i] into word2[:j]. O(m*n) running time complexity
where m = len(word1) and n = len(word2)
"""
def editDistance(word1, word2):
  len1, len2 = len(word1), len(word2)

  # initialise using maximum 'coordinate' for base cases when i=0 or j=0
  # where the distance is max(i,j) to insert all letters into the empty string
  table = [[max(i, j) for j in range(len2 + 1)] for i in range(len1 + 1)]

  for row in range(1, len1 + 1):
    letter1 = word1[row - 1]
    for col in range(1, len2 + 1):
      letter2 = word2[col - 1]

      # figure out possible editDistances using DP table
      # no increment on replace if letters match (do nothing)
      caseInsert = table[row][col - 1] + 1
      caseDelete = table[row - 1][col] + 1
      caseReplace = table[row - 1][col - 1] + (0 if letter1 == letter2 else 1)

      table[row][col] = min(caseInsert, caseDelete, caseReplace)

  # reconstruct solution
  row, col = len1, len2
  operations = deque()
  while row > 0 or col > 0:
    letterDelete = word1[row - 1]
    letterInsert = word2[col - 1]

    if table[row][col] == table[row][col - 1] + 1:
      operations.appendleft('Insert {}'.format(letterInsert))
      col -= 1
    elif table[row][col] == table[row - 1][col] + 1:
      operations.appendleft('Delete {}'.format(letterDelete))
      row -= 1
    else:
      row -= 1
      col -= 1
      if letterDelete != letterInsert:
        operations.appendleft('Replace {} with {}'.format(letterDelete, letterInsert))
      else:
        operations.appendleft('Keep {}'.format(letterInsert))


  return table[len1][len2], list(operations)


if __name__ == "__main__":
  print("Enter 2 space-separated words: ", end="")
  word1, word2 = input().strip().split(' ')

  distance, operations = editDistance(word1, word2)
  print("Edit distance = {}".format(distance))

  for i, operation in enumerate(operations):
    print("{}) {}".format(i+1, operation))
