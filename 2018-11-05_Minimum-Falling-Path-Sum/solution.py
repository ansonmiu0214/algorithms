#!/bin/python3

"""
Bottom-up DP problem with additional handling on (literal) edge cases.
O(n^2) running time complexity where A has dimension nxn.
"""
def minFallingPathSum(A):
  count = len(A)

  # Initialise base cases (bottom row falling path sum = cell value)
  table = [[A[i][j] for j in range(count)] for i in range(count)]

  for row in range(count - 2, -1, -1):
    for col in range(count):
      cell = A[row][col]
      option = min(table[row + 1][max(col - 1, 0)],
                   table[row + 1][col],
                   table[row + 1][min(col + 1, count - 1)])

      table[row][col] = cell + option

  return min(table[0])


if __name__ == "__main__":
  print("Enter n where grid = nxn: ", end="")
  n = int(input().strip())

  A = []
  for i in range(n):
    print("Row {}: ".format(i + 1), end="")
    row = list(map(int, input().strip().split(' ')))
    A.append(row)

  val = minFallingPathSum(A)
  print(val)
      
