#!/bin/python3

from collections import deque

"""
Greedy approach - first sort the intervals then attempt to merge successive ones. Keep a current one in hand to compare with the others. If a merge is successful, keep the merged current one and proceed with others in the queue; otherwise, advance the current interval.
"""
def merge(intervals):
	# bsae case: empty list to begin with
	if not intervals:
		return intervals

	# greedy lexicographic sorting
	curr, *rest = sorted(intervals)
	candidates = deque(rest)

	res = []
	while candidates:
		lo2, up2 = candidates.popleft()
		
		lo1, up1 = curr
		if lo2 <= up1:
			# merge and update current
			curr = [min(lo1, lo2), max(up1, up2)]
		else:
			# add current to results list and move onto comparing using `other'
			res.append(curr)
			curr = [lo2, up2]

	res.append(curr)
	return res
			

if __name__ == "__main__":
	print("Enter list of intervals to merge: ", end="")
	vals = list(map(int, input().strip().split(' ')))
	
	if len(vals) % 2 != 0:
		print("Invalid input - need even number of integers to construct intervals.")
		exit()	

	intervals = []
	for idx in range(0, len(vals), 2):
		intervals.append([vals[idx], vals[idx+1]])

	print("Before: {}".format(intervals))
	merged = merge(intervals)
	print("After: {}".format(merged))
	
