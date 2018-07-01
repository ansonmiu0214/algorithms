#!/bin/python3

from collections import deque

"""
Stack-based approach to keep track of bracket depth in LIFO.
Running time complexity of O(n).
"""
def isValid(s):
	brackets = { '(' : ')', '[': ']', '{': '}' }

	stack = deque()
	count = 0

	for letter in s:
		if letter in brackets:
			stack.append(letter)		# keep track of open brackets
			count += 1
		else:
			if count == 0:
				return False					# not expecting closing

			open_bracket = stack.pop()
			count -= 1
			if brackets[open_bracket] != letter:
				return False					# not the closing expected

	return count == 0						# stack should be empty now


if __name__ == "__main__":
	print("Enter bracket pattern: ", end="")
	s = input().strip()
	print("Pattern '{}' is {}.".format(s, "valid" if isValid(s) else "not valid"))
