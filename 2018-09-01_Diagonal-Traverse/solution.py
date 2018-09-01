#!/bin/python3

from pprint import pprint

"""
Use `row', `col' variables to keep track of coordinates and `up' boolean flag
to keep track of direction. Handle edge cases as required. Traverses all cells
once, resulting in O(MN) running time complexity where M, N refers to the 
number of rows and columns of the matrix respectively.
"""
def findDiagonalOrder(matrix):
	res = []
	M = len(matrix)
	
	# edge case of empty matrix
	if M == 0:	return res

	N = len(matrix[0])

	# set up coordinate variables and direction flag
	row, col, up = 0, 0, True

	while row < M and col < N:
		res.append(matrix[row][col])

		if up:
			row -= 1
			col += 1

			# handle base cases of going too high or too right
			if row < 0 or col == N:
				up = not up

				if col == N:
					# exceeded rightmost end
					row += 2				# increment by 2 because previously decremented by 1
					col = N - 1
				else:
					# exceeded topmost row
					row = 0
	
		else:
			row += 1
			col -= 1

			# handle base cases of going too low or too left
			if col < 0 or row == M:
				up = not up

				if row == M:
					# exceeded bottom row
					col += 2				# increment by 2 because previously decremented by 1
					row = M - 1
				else:
					# exceeded leftmost end
					col = 0

	return res


if __name__ == "__main__":
	print("Enter the number of rows: ", end="")
	M = int(input().strip())

	matrix = []
	for row in range(1, M + 1):
		print("Enter space-separated integers for row {}: ".format(row), end="")
		matrix.append(list(map(int, input().strip().split(' '))))	

	pprint(matrix)
	res = findDiagonalOrder(matrix)
	pprint(res)	
