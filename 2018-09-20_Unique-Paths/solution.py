#!/bin/python3

"""
Bottom-up dynamic programming approach with base case on right/bottom edges.
"""
def uniquePaths(m, n):
	# initialise DP table
	# numPaths[x][y] = uniquePaths(x+1, y+1)
	numPaths = [[1 for _ in range(n)] for _ in range(m)]

	for x in range(m):
		# ignore cases on right/bottommost edges since already set to 1
		if x == 0:	continue

		for y in range(n):
			if y == 0:	continue

			numPaths[x][y] = numPaths[x-1][y] + numPaths[x][y-1]
	
	return numPaths[m-1][n-1]


if __name__ == "__main__":
	print("Enter space-separated integers representing number of rows and columns:")
	m, n = list(map(int, input().strip().split(' ')))

	numPaths = uniquePaths(m, n)
	print("{} unique path{} to get from (1, 1) to ({}, {}) only by moving either right or down.".format(numPaths, "" if numPaths == 1 else "s", m, n))

	
