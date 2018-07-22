#!/bin/python3

"""
Use classic DP algorithm for finding longest common subsequence between wordand word[::-1] with O(n^2) running time complexity where n = len(word)
"""
def longestPalindromicSubsequence(word):
  length = len(word)

  # initialise DP array
  table = [[0 for col in range(length + 1)] for row in range(length + 1)]

  for row in range(1, length + 1):
    curr = word[row - 1]
    for col in range(1, length + 1):
      other = word[length - col]

      if curr == other:
        table[row][col] = table[row - 1][col - 1] + 1
      else:
        table[row][col] = max(table[row - 1][col], table[row][col - 1])

  result = reconstruct(table, word, length, length)
  return table[length][length], result

def reconstruct(table, word, row, col):
  if row == 0 or col == 0:
    return ""

  diag = table[row - 1][col - 1]
  left = table[row][col - 1]
  up = table[row - 1][col]

  curr = table[row][col]
  prev = max(diag, left, up)
  if curr == prev + 1:
    return reconstruct(table, word, row - 1, col - 1) + word[row - 1]

  if prev == left:
    return reconstruct(table, word, row, col - 1)

  return reconstruct(table, word, row - 1, col)


if __name__ == "__main__":
  print("Enter word: ", end="")
  word = input().strip()

  length, subsequence = longestPalindromicSubsequence(word)
  print("Longest palindromic subsequence is {} of length {}.".format(subsequence, length))
