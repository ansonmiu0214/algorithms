#!/bin/python3

"""
'Sorts' half the array for O(n/2) == O(n) running time complexity and O(1) space complexity.
"""
def median(A, B):
	m, n = len(A), len(B)
	total = m + n
	notEven = total % 2 > 0

	target = total // 2
	if notEven:
		target += 1

	left = right = val = 0

	for count in range(target):
		if left == m:
			val = B[right]
			right += 1
		elif right == n:
			val = A[left]
			left += 1
		elif A[left] < B[right]:
			val = A[left]
			left += 1
		else:
			val = B[right]
			right += 1

	if notEven:
		return val

	if left == m:
		return (val + B[right]) / 2
	
	if right == n:
		return (val + A[left]) / 2

	return (val + min(A[left], B[right])) / 2


def median_log(A, B):
	m, n = len(A), len(B)

	inf = 999999999
	A = [-inf] + A + [inf]
	B = [-inf] + B + [inf]

	total = m + n
	notEven = total % 2 > 0
	target = total // 2
	if notEven:
		target += 1

	i, j = 1, n + 1
	left_max = right_min = 0

	while True:
		index = i + j - 2

		left_max = max(A[i-1], B[j-1])
		right_min = min(A[i], B[j])

		if index == target:
			if left_max <= right_min:
				break

			j -= 1
		elif index < target:
			i += 1
		else:
			j -= 1

	if notEven:	
		return left_max


	return (left_max + right_min) / 2



if __name__ == "__main__":
	print("Enter the first array with space-separated integers: ", end="")
	nums1 = list(map(int, input().strip().split(' ')))

	print("Enter the second array with space-separated integers: ", end="")
	nums2 = list(map(int, input().strip().split(' ')))  
	
	nums1.sort()
	nums2.sort()
	res = median(nums1, nums2)
	# res = median_log(nums1, nums2)
	print("The median is {}.".format(res))

