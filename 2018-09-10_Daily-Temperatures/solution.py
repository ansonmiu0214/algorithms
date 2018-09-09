#!/bin/python3

"""
Dynamic programming approach but filling in result table in reverse, sinc
the last element is always 0 (no day warmer than final day). Use the result
table to skip ahead since, if temp[i] > temp[j], skipping to temp[j + res[j]]
skips the days, k, such that temp[k] < temp[j], of which it is guaranteed that
temp[i] > temp[k], so no need to check.
"""
def dailyTemperatures(temperatures):
	end = len(temperatures)

	# base case: empty list
	if end == 0:
		return []

	res = [0 for _ in range(end)]

	# reverse loop
	for i in range(end - 2, -1, -1):
		curr = temperatures[i]
		
		j = i + 1
		# skip pointer ahead if index j not warmer than index i
		# don't skip if we know there isn't a temperature warmer than index j
		while not temperatures[j] > curr and not res[j] == 0:
			j += res[j]

		if curr < temperatures[j]:
			res[i] = j - i
		else:
			res[i] = 0

	return res


if __name__ == "__main__":
	print("Enter space-separated integers as temperatures: ", end="")
	temperatures = list(map(int, input().strip().split(' ')))

	res = dailyTemperatures(temperatures)
	print(res)
