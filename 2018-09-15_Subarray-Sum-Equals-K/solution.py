#!/bin/python3

"""
Use cumulative sum approach to try all possible starting/stopping indices.
"""
def subarraySum(nums, k):
	end = len(nums)
	if end == 0:
		return 0

	count = 0

	# try all possible starting points
	for start in range(end):
		totalSum = nums[start]
		if totalSum == k:
			count += 1

		# try all possible stopping points
		for stop in range(start+1, end):
			totalSum += nums[stop]
			if totalSum == k:
				count += 1

	return count


if __name__ == "__main__":
	print("Enter space-separated integers: ", end="")
	nums = list(map(int, input().strip().split(' ')))

	print("Enter target sum: ", end="")
	k = int(input().strip())

	res = subarraySum(nums, k)
	print("There {} {} subarray{} that sum to {}.".format("is" if res == 1 else "are", res, "" if res == 1 else "s", k))
