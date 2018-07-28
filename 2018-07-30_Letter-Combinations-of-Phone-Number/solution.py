#!/bin/python3

mapping = dict(zip(map(str, range(2, 10)), ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]))

def letterCombinations(number):
	if number == "":
		return []

	return findCombos(list(number))

"""
Recursive solution operating on list of digits.
"""
def findCombos(digits):
	if digits == []:
		return [""]

	# split into head/tail for recursion
	curr, *rest = digits
	combos = findCombos(rest)

	letters = mapping[curr]
	return [letter + combo for combo in combos for letter in letters]


if __name__ == "__main__":
	print("Enter number [2-9]: ", end="")
	nums = str(input().strip())

	print(letterCombinations(nums))
