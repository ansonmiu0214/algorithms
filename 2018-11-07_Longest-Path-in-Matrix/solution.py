#!/bin/python3

def longestPath(grid):
  numRows = len(grid)
  numCols = len(grid[0])

  # Setup DP table
  # table[i][j] := longest path starting at cell (i, j)
  table = [[None for _ in range(numCols)] for _ in range(numRows)]
  seen = [[False for _ in range(numCols)] for _ in range(numRows)]

  def explore(i, j, count=1):
    if table[i][j] is not None:
      return

    longestFurtherPath = 0
    if i > 0 and grid[i][j] + 1 == grid[i-1][j]:
      # Go up
      explore(i-1, j, count+1)
      longestFurtherPath = max(longestFurtherPath, table[i-1][j])

    if i < numRows - 1 and grid[i][j] + 1 == grid[i+1][j]:
      # Go down
      explore(i+1, j, count+1)
      longestFurtherPath = max(longestFurtherPath, table[i+1][j])

    if j > 0 and grid[i][j] + 1 == grid[i][j-1]:
      # Go left
      explore(i, j-1, count+1)
      longestFurtherPath = max(longestFurtherPath, table[i][j-1])

    if j < numCols - 1 and grid[i][j] + 1 == grid[i][j+1]:
      # Go right
      explore(i, j+1, count+1)
      longestFurtherPath = max(longestFurtherPath, table[i][j+1])

    table[i][j] = 1 + longestFurtherPath
    return


  for row in range(numRows):
    for col in range(numCols):
      if table[row][col] is None:
        explore(row, col)
  
  res = 0  
  for row in range(numRows):
    for col in range(numCols):
      res = max(res, table[row][col])

  return res


if __name__ == "__main__":
  grid = [[1,2,9],[5,3,8],[4,6,7]]
  res = longestPath(grid)
  print(res)
