#!/bin/python3

from collections import deque

"""
Stack-based approach, with preprocessing on path string by tokenising path components
through the '/' delimiter to extract directories and eliminate extraneous '/' characters simultaneously.
Going 'up' a folder pops the stack (if non-empty). The simplified path is obtained by joining the remaining
elements of the stack with '/'.
"""
def simplifyPath(path):
	dirs = deque()

	# tokenise and remove extraneous '/' characters
	places = list(filter(lambda x: x != "", path.strip().split('/')))

	for place in places:
		# current directory, can ignore
		if place == '.':
			continue

		# spec specifies base case of '/../' == '/', so only pop stack if it is non-empty
		if place == '..':
			if dirs:
				dirs.pop()
		else:
			dirs.append(place)

	return "/" + "/".join(dirs)


if __name__ == "__main__":
	print("Enter path: ", end="")
	path = input().strip()

	simplified = simplifyPath(path)
	print("Simplified: " + simplified)
			
