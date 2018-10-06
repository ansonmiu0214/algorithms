#!/bin/python3

"""
Iterative approach using 2 pointers to keep track of range.
While loop conditions handle any index out-of-bound runtime errors.
"""
def summaryRanges(nums):
	res = []
	end = len(nums)
	if end == 0:
		return res

	# setup pointers
	left = right = 0

	while right < end:
		start = nums[left]
		stop = nums[right]

		target = start + 1

		# increment `right` whilst range is consecutive
		while right + 1 < end:
			if nums[right + 1] != target:
				break

			stop += 1
			target += 1
			right += 1

		if start == stop:
			# no range
			res.append("{}".format(start))
		else:
			# format range as required
			res.append("{}->{}".format(start, stop))

		# advance pointers to move to next ist element
		right += 1
		left = right

	return res


if __name__ == "__main__":
	print("Enter space-separated numbers: ", end="")
	nums = sorted(list(map(int, input().strip().split(' '))))

	ranges = summaryRanges(nums)
	print(ranges)
