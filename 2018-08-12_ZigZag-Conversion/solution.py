#!/bin/python3

"""
O(n) space and running time complexity.
Reorganise characters in array indexed by row, then print result by joining the rows.
Emulate zigzag behaviour with row variable and diag boolean flag.
"""
def convert(s, numRows):
	# base case
	if numRows == 1:	return s

	res = ["" for _ in range(numRows)]
	row, diag, end = 0, False, numRows - 1

	for letter in s:
		res[row] += letter
		
		if row == end:	diag = True
		elif row == 0:	diag = False

		if diag:	row -= 1
		else:			row += 1

	return "".join(res)


if __name__ == "__main__":
	print("Enter space-separated string and numRows: ", end="")
	s, numRows = input().strip().split(' ')

	res = convert(s, int(numRows))
	print(res)
