#!/bin/python3

"""
Top-down dynamic programming approach where match[x][y] := isMatch(s[x:], p[y:]).

If p[y] == '?', letter/pattern is consumed so match[x][y] = match[x+1][y+1]
If p[y] == '*', consume pattern and find a match for each of the suffixes, so match[x][y] = or { match[z][y+1] } for z in [x..n) where n = len(s)
Else, p[y] is a regular letter so matching is trivial. 
"""
def isMatch(s, p):
	m = len(s)

	# preprocessing on pattern
	# successive '*'s can be collapsed
	newP = ""
	isWild = False

	for letter in p:
		if letter == '*' and not isWild:
			isWild = True
			newP += letter
		else:
			isWild = False
			newP += letter

	p = newP
	n = len(p)

	# setup table
	match = [[None for _ in range(n+1)] for _ in range(m+1)]

	# define checking function that uses memoisation on table
	def checkMatch(strIdx, patIdx):
		# if table has result, use it directly
		if match[strIdx][patIdx] is not None:
			return match[strIdx][patIdx]

		# base case: used all string and all pattern
		if strIdx == m and patIdx == n:
			match[strIdx][patIdx] = True
			return match[strIdx][patIdx]

		# base case: used all string and some pattern remaining
		# this matches iff the remaining pattern are all '*'
		# which matches all empty sequence (since no string remaining)
		if strIdx == m:
			allWild = True
			for idx in range(patIdx, n):
				if p[idx] != '*':
					allWild = False
					break

			match[strIdx][patIdx] = allWild
			return match[strIdx][patIdx]

		# base case: used all pattern and some string remaining
		# always false - pattern must match whole string
		if patIdx == n:
			match[strIdx][patIdx] = False
			return match[strIdx][patIdx]

		# extract letters from string and pattern
		letter = s[strIdx]
		token = p[patIdx]

		if token == '?' or letter == token:
			# consume letter and token
			match[strIdx][patIdx] = checkMatch(strIdx + 1, patIdx + 1)
			return match[strIdx][patIdx]

		if token == '*':
			# consume token
			# test remaining pattern on each remaining suffix, including this
			# only require one match to succeed
			hasMatch = False
			for idx in range(strIdx, m+1):
				if checkMatch(idx, patIdx + 1):
					hasMatch = True
					break

			match[strIdx][patIdx] = hasMatch
			return match[strIdx][patIdx]

		if letter == token:
			match[strIdx][patIdx] = checkMatch(strIdx + 1, patIdx + 1)
			return match[strIdx][patIdx]

		# at this stage, must be the case that letter != token
		match[strIdx][patIdx] = False
		return match[strIdx][patIdx]

	return checkMatch(0, 0)


if __name__ == "__main__":
	print("Enter string: ", end="")
	s = input().strip()

	print("Enter pattern: ", end="")
	p = input().strip()

	match = isMatch(s, p)
	print(match)
