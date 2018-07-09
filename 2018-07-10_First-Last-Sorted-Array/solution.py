#!/bin/python3

"""
Divide-and-conquer recursive approach defined on base cases.
"""
def searchRange(nums, target):
	default = [-1, -1]

	# base case: empty array (not found)
	if not nums:	return default

	mid = len(nums) // 2
	if mid == 0:
		# base case: singleton array (either found or not found)
		return [0, 0] if nums[0] == target else default

	left = searchRange(nums[:mid], target)
	right = searchRange(nums[mid:], target)

	if right == default:	return left

	# adapt RHS offset
	right = list(map(lambda x: x + mid, right))
	if left == default:		return right

	return [left[0], right[1]]


if __name__ == "__main__":
	print("Enter space-separated numbers: ", end="")
	nums = list(map(int, input().strip().split(' ')))
	nums.sort()	

	print("Enter target: ", end="")
	target = int(input().strip())
	
	print("Sorted list: {}".format(nums))
	print("Target '{}' found in range {}.".format(target, searchRange(nums, target)))
