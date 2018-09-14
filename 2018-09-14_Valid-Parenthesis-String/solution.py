#!/bin/python3

"""
DP approach with base cases on diagonal and upper diagonal.
"""
def checkValidString(s):
	count = len(s)

	# empty string base case
	if count == 0:
		return True

	# setup DP table with base case along diagonal: valid iff can be empty string
	valid = [[i == j and s[i] == '*' for j in range(count)] for i in range(count)]

	# setup upper diagonal: valid iff left can be open and right can be close
	for i in range(count-1):
		valid[i][i+1] = s[i] != ')' and s[i+1] != '('

	for i in range(count-2, -1, -1):
		start = s[i]

		# shortcircuit: no need to check if starting bracket is close
		if start == ')':
			continue

		for j in range(i+1, count):
			end = s[j]

			# shortcircuit: no need to check if end bracket is open
			if end == '(':
				continue

			# if wildcard start, only require s[i+1]...s[j] to be valid
			if start == '*' and valid[i+1][j]:
				valid[i][j] = True
				continue

			# valid condition: s[i] as '(', s[i+1]...s[j] valid, s[j] as ')'
			if valid[i+1][j-1]:
				valid[i][j] = True
				continue

			# find midpoint k such that s[i]...s[k] and s[k+1]...s[j] are valid
			for k in range(i+1, j):	
				if valid[i][k] and valid[k+1][j]:
					valid[i][j] = True
					break

	return valid[0][count-1]


if __name__ == "__main__":
	print("Enter parenthesis string: ", end="")
	s = input().strip()

	valid = checkValidString(s)
	print("Valid" if valid else "Not Valid")
