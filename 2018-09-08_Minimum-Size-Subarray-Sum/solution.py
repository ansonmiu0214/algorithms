#!/bin/python3

"""
Greedy sliding window approach.
"""
def minSubArrayLen(s, nums):
	end = len(nums)
	
	# base case: empty array
	if end == 0:
		return 0, None, None

	# setup variables for window
	res = None
	left, right = 0, 0
	curr = nums[0]
	resLeft, resRight = 0, 0

	while right < end:
		if curr < s:
			# less than required, extend window but take care of array bound
			right += 1
			if right == end:	
				break

			curr += nums[right]

		else:
			# update window size
			window = right - left + 1
			
			if res is None or window < res:
				res = window
				resLeft, resRight = left, right

			# attempt to shrink window, with edge case of window already being 1
			if left == right:
				right += 1
				if right == end:
					break

				curr += nums[right]

			curr -= nums[left]
			left += 1

	return (0, None, None) if res is None else (res, resLeft, resRight)
			

if __name__ == "__main__":
	print("Enter minimum sum: ", end="")
	s = int(input().strip())

	print("Enter space-separated array elements: ", end="")
	nums = list(map(int, input().strip().split(' ')))

	windowSize, left, right = minSubArrayLen(s, nums)
	if windowSize == 0:
		print("No subarray in nums with sum at least {}.".format(s))
	else:
		print("Minimum subarray with sum at least {} is nums[{}:{}], where sum({}) = {}.".format(s, left, right + 1, nums[left:right + 1], sum(nums[left:right+1])))

