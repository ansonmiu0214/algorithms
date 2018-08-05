#!/bin/python3

from functools import cmp_to_key

"""
Define custom comparator based on S.
Lookups are O(1) and Python uses merge sort, so overall O(n(log(n))) running time complexity.
"""
def customSortString(S, T):
	# generate lookup table with letter as key
	lookup = dict(map(lambda x: (x[1], x[0]), enumerate(S)))

	# define custom comparator
	def cmp(x, y):
		if not x in lookup:	return 1
		if not y in lookup:	return -1
		return lookup[x] - lookup[y]

	# return sorted string
	return "".join(sorted(T, key=cmp_to_key(cmp)))


if __name__ == "__main__":
	print("Enter sorted character string: ", end="")
	S = input().strip()

	print("Enter string to sort: ", end="")
	T = input().strip()

	res = customSortString(S, T)
	print("Custom sorted string: {}".format(res))
