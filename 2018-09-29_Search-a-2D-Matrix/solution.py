#!/bin/python3

from math import ceil

"""
Take advantage of the sorted nature of the 2D matrix by applying
binary search to find the target row, then applying binary search
on the target row to find the target cell.
"""
def searchMatrix(matrix, target):
  # determine row/column dimensions
  # handle base case where there is either 0 rows or 0 columns
  # in which case the element is trivially non-existent in the matrix
  numRows = len(matrix)
  if numRows == 0:
    return False

  numCols = len(matrix[0])
  if numCols == 0:
    return False

  # binary search to find target row
  # iterative implementation to save recursion overhead
  rowLo, rowHi = 0, numRows - 1
  while rowLo < rowHi:
    mid = ceil((rowLo + rowHi) / 2)
    
    if target < matrix[mid][0]:
      rowHi = mid - 1
    else:
      rowLo = mid

  targetRow = matrix[rowLo]

  # binary search to find target cell within target row
  colLo, colHi = 0, numCols - 1
  while colLo < colHi:
    mid = ceil((colLo + colHi) / 2)

    if target < targetRow[mid]:
      colHi = mid - 1
    else:
      colLo = mid

  return target == targetRow[colLo]


if __name__ == "__main__":
  print("Enter number of rows in the matrix: ", end="")
  numRows = int(input().strip())

  matrix = []
  for idx in range(numRows):
    print("Enter space-separated integers for row {}:".format(idx + 1))
    matrix.append(list(map(int, input().strip().split(' '))))

  print()
  print("Enter target number to find: ", end="")
  target = int(input().strip())

  found = searchMatrix(matrix, target)
  print(found)
