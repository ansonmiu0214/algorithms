#!/bin/python3

"""
Dynamic programming approach.
"""
def minPathSum(grid):
  m, n = len(grid), len(grid[0])
  
  # setup DP table
  table = [[0 for _ in range(n)] for _ in range(m)]

  for x in range(m):
    for y in range(n):
      val = grid[x][y]

      if x == 0 and y == 0:
        # top-left corner: no choice
        table[x][y] = val

      elif x == 0:
        # top row: must have come from cell to the left
        table[x][y] = table[x][y-1] + val

      elif y == 0:
        # left column: must have come from cell above
        table[x][y] = table[x-1][y] + val

      else:
        # take minimum path either from left or above
        table[x][y] = min(table[x][y-1], table[x-1][y]) + val

  return table[m-1][n-1]


if __name__ == "__main__":
  print("Enter the number of rows in the grid: ", end="")
  m = int(input().strip())

  grid = []
  for row in range(m):
    print("Enter space-separated integers for row {}".format(row + 1))
    grid.append(list(map(int, input().strip().split(' '))))

  res = minPathSum(grid)
  print("Minimum path sum = {}".format(res))
