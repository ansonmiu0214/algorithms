#!/bin/python3

def totalFruit(tree):
	'''
	DP approach of finding longest subarray with 2 elements
	'''

	n = len(tree)
	last = n - 1

	# accumulate most optimal result
	prevType = tree[last]		# tree type of previous
	countOneType = 1				# longest subarray, from prev, with 1 unique
	countTwoType = 1				# longest subarray, from prev, with 2 unique
	secondType = prevType		# 2nd tree type for longest subarray with 2 unique
	
	acc = countTwoType			# max accumulator of longest subarray with 2 unique

	for i in range(n-2, -1, -1):
		currType = tree[i]

		newCountOneType = 1 if currType != prevType else (countOneType + 1)
		newCountTwoType = (countOneType + 1) if (currType != prevType and currType != secondType) else (countTwoType + 1)
		newSecondType = prevType if currType != prevType else secondType

		# update accumulators
		prevType = currType
		countOneType = newCountOneType
		countTwoType = newCountTwoType
		secondType = newSecondType
		
		acc = max(acc, countTwoType)

	return acc


if __name__ == "__main__":
	print("Enter space-separated trees: ", end="")
	tree = list(map(int, input().strip().split()))

	res = totalFruit(tree)
	print(res)
