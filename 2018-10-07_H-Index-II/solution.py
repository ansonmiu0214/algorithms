#!/bin/python3

from math import ceil

"""
Take advantage of the sorted list of citations to interpret the h-index differently.
h-index(citations) = x <==> citations[n-x-1] <= x && citations[n-x] >= x where n = len(citations)

Let idx = n-x.
Apply an iterative binary search approach to find idx that satisfies the condition and return x through computing x = n - idx. 
"""
def hIndex(citations):
	end = len(citations)

	# base case: no citations, so h-index is trivial
	if end == 0:
		return 0

	# initialise binary search index pointers
	left, right = 0, end - 1

	while left < right:
		mid = ceil((left + right) / 2)
		sub = mid - 1

		x = end - mid
		if citations[mid] >= x:
			if citations[sub] <= x:
				return x

			# shift window lower, even citations[mid-1] is greater than x
			right = sub
		else:
			# shift window higher, even citations[mid] is less than x
			left = mid

	# edge case: left == right, so narrowed down to singleton range
	x = end - left
	return x if citations[left] >= x else 0
			

if __name__ == "__main__":
	print("Enter space-separated integers for citations: ", end="")
	citations = sorted(list(map(int, input().strip().split(' '))))

	index = hIndex(citations)
	print("This author has an h-index of {}.".format(index))
