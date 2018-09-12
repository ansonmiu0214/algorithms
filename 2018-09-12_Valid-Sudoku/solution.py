#!/bin/python3

"""
Logical approach in checking rows, columns and squares.
"""
def isValidSudoku(board):
	SIZE = 9
	SQUARE = 3

	# Generic function to check for duplicates in coordinates
	def isValid(coords):
		seen = set()
		for row, col in coords:
			val = board[row][col]
			if val == ".":	continue
			if val in seen:	return False
			seen.add(val)
		return True

	def isValidRow(row):
		coords = [(row, y) for y in range(SIZE)]
		return isValid(coords)

	def isValidCol(col):
		coords = [(x, col) for x in range(SIZE)]
		return isValid(coords)

	# Check whether a sudoku square is valid
	def isValidSquare(idx):
		quo, rem = divmod(idx, SQUARE)
		rows = range(quo * SQUARE, (quo + 1) * SQUARE)
		cols = range(rem * SQUARE, (rem + 1) * SQUARE)
		coords = [(x, y) for x in rows for y in cols]
		return isValid(coords)

	for i in range(SIZE):
		if not (isValidRow(i) and isValidCol(i) and isValidSquare(i)): 
			return False
	
	return True


if __name__ == "__main__":
	board = [
		["5","3",".",".","7",".",".",".","."],
  	["6",".",".","1","9","5",".",".","."],
  	[".","9","8",".",".",".",".","6","."],
  	["8",".",".",".","6",".",".",".","3"],
  	["4",".",".","8",".","3",".",".","1"],
  	["7",".",".",".","2",".",".",".","6"],
  	[".","6",".",".",".",".","2","8","."],
  	[".",".",".","4","1","9",".",".","5"],
  	[".",".",".",".","8",".",".","7","9"]
	]
	
	print(board)
	print(isValidSudoku(board))
