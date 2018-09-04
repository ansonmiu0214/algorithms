#!/bin/python3

"""
Greedy left-to-right comparison with edge cases on handling equivalent versions
with trailing zeros using all(...).
"""
def compareVersion(version1, version2):
	nums1 = list(map(int, version1.split('.')))
	nums2 = list(map(int, version2.split('.')))

	len1 = len(nums1)
	len2 = len(nums2)
	end = min(len1, len2)

	for i in range(end):
		if nums1[i] < nums2[i]:	return -1
		if nums1[i] > nums2[i]:	return 1

	if len1 < len2:
		return 0 if all(map(lambda x: x == 0, nums2[end:])) else -1
	
	if len1 > len2:
		return 0 if all(map(lambda x: x == 0, nums1[end:])) else -1

	return 0


if __name__ == "__main__":
	print("Enter version 1: ", end="")
	version1 = input().strip()

	print("Enter version 2: ", end="")
	version2 = input().strip()

	cmp = compareVersion(version1, version2)
	if cmp == 0:
		print("{} and {} are the same version.".format(version1, version2))
	elif cmp < 0:
		print("{} is older than {}.".format(version1, version2))
	else:
		print("{} is newer than {}.".format(version1, version2))
