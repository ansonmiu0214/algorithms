#!/bin/python3

from pprint import pprint

# Depth-first search approach, column by column from left to right.
def solveNQueens(n):
  '''
  Return the list of n-queen configurations for an nxn grid
  such that no queen threatens another.
  '''

  def makeGrid(queenCells, emptySymbol='.'):
    '''
    Given a list of coordinates for each queen's position,
    returns a list representation of the grid.
    '''
    grid = [[emptySymbol for _ in range(n)] for _ in range(n)]
    for row, col in queenCells:
      grid[row][col] = 'Q'
      grid[row] = ''.join(grid[row])
    return grid

  configs = []
  finalCol = n - 1

  threatIdxs = {}       # map of threat indices to frequencies
  queenCells = set()

  def dfs(row, col=0):
    '''
    Place queen on board, update list of threatened cells, continue DFS.
    '''
    
    # Place queen on board
    queenCells.add((row, col))

    # Base case: all queens placed on board
    if col == finalCol:
      config = makeGrid(queenCells)
      configs.append(config)
      queenCells.remove((row, col))
      return

    rowIdx = row * n
 
    # Compute indices that current queen will threaten
    # No need to look to the left of the board (by DFS)
    currThreats = {}
    
    # Row
    for nextCol in range(col + 1, n):
      idxToAdd = rowIdx + nextCol
      currThreats[idxToAdd] = True

      if idxToAdd not in threatIdxs:
        threatIdxs[idxToAdd] = 1
      else:
        threatIdxs[idxToAdd] += 1

    # Diagonal up
    for idx, upRow in enumerate(range(row - 1, -1, -1)):
      nextCol = col + (idx + 1)
      if nextCol == n:
        break

      idxToAdd = (upRow * n) + nextCol
      currThreats[idxToAdd] = True

      if idxToAdd not in threatIdxs:
        threatIdxs[idxToAdd] = 1
      else:
        threatIdxs[idxToAdd] += 1

    # Diagonal down
    for idx, downRow in enumerate(range(row + 1, n)):
      nextCol = col + (idx + 1)
      if nextCol == n:
        break

      idxToAdd = (downRow * n) + nextCol
      currThreats[idxToAdd] = True

      if idxToAdd not in threatIdxs:
        threatIdxs[idxToAdd] = 1
      else:
        threatIdxs[idxToAdd] += 1

    # Explore each row for next column in DFS
    nextCol = col + 1
    for nextRow in range(n):
      nextIdx = nextRow * n + nextCol
      if nextIdx not in threatIdxs:
        dfs(nextRow, nextCol)

    # Backtrack: remove threats CREATED BY THIS QUEEN.
    # Because a cell can be threatened by MULTIPLE QUEENS, a frequenc table (map) is used
    # instead of a set. Delete map entry when frequency count is 0.
    for idx in currThreats:
      threatIdxs[idx] -= 1
      if threatIdxs[idx] == 0:
        del threatIdxs[idx]

    queenCells.remove((row, col))


  for row in range(n):
    dfs(row)

  return configs


if __name__ == "__main__":
  print("Enter grid size (n): ", end="")
  n = int(input().strip())

  configs = solveNQueens(n)
  count = len(configs)
  print("There {} {} solution{} for a {}-by-{} grid.".format("is" if count == 1 else "are", count, "" if count == 1 else "s", n, n))
  pprint(configs)
