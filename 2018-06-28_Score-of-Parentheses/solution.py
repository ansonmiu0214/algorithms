#!/bin/python3

from collections import deque

def scoreOfParentheses(S):
	total = 0
	stack = deque()

	while S != "":
		if S[:2] == "()":
			# match token, increment score, advance
			total += 1
			S = S[2:]

		elif S[:1] == "(":
			# push current total onto stack, reset and advance
			stack.append(total)
			total = 0
			S = S[1:]

		else:		# precondition of balanced, so must be ")"
			# pop, accumulate and multiply
			total = (total * 2) + stack.pop()
			S = S[1:]

	return total


if __name__ == "__main__":
	print("Enter parentheses string to score: ", end="")
	s = input().strip()
	score = scoreOfParentheses(s)
	print("Score: {}".format(score))
