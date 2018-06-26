#!/bin/python3

"""
O(n) running time complexity + O(1) space complexity.
Returns tuple of boolean condition and array of swap-indices.

@ret (isBuddy, is)
where isBuddy ==> (A[is[0]] == B[is[1]] && A[is[1]] == B[is[0]])
"""
def buddyStrings(A, B):
	# Defensive length checks
	if len(A) != len(B):
		return False

	pairs = list(zip(A, B))
	seen = dict()
	diff = None
	diffCount = 0
	hasDuplicate = False
	swapIndex = duplicateIndex = []

	for i, (x, y) in list(enumerate(pairs)):
		if x == y:
			# Check for duplicate as possible swap
			if x in seen:
				hasDuplicate = True
				duplicateIndex = [seen[x], i]
			else:
				seen[x] = i

		elif diffCount == 0:
			# Record difference and increment count
			diff = (x, y)
			diffCount += 1
			swapIndex = [i]
		else:
			diffCount += 1
			if diffCount > 2:
				return False

			a, b = diff
			if x != b or y != a:
				return False

			swapIndex.append(i)

	return diffCount == 2 or hasDuplicate, swapIndex + duplicateIndex


if __name__ == "__main__":
	print("Enter two space-separated strings: ", end="")
	A, B = input().strip().split(' ')
	status, indices = buddyStrings(A, B)

	if status:
		print("Strings '{}' and '{}' can be made equivalent by swapping indices {} and {}.".format(A, B, indices[0], indices[1]))
	else:
		print("Strings '{}' and '{}' cannot be made equivalent with 1 swap.".format(A, B))
