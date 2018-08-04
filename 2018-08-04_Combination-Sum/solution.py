#!/bin/python3

"""
DFS approach on all indices with base case when target <= 0.
Sort array first so no need to do further DFS if array element exceeds target.
O(n(log(n))) running time complexity where n = len(nums)
"""
def combinationSum(nums, target):
	nums.sort()
	res = []

	dfs(nums, target, 0, len(nums), [], res)
	return res


def dfs(array, key, index, end, path, res):
	if key < 0:
		return

	if key == 0:
		res.append(path)
		return

	for i in range(index, end):
		num = array[i]
		dfs(array, key - num, i, end, path + [num], res)


if __name__ == "__main__":
	print("Enter space-separated numbers: ", end="")
	nums = list(map(int, input().strip().split(' ')))

	print("Enter target: ", end="")
	target = int(input().strip())

	solutionSet = combinationSum(nums, target)
	print("Solution set:")
	print(solutionSet)
