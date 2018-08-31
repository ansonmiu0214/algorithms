#!/bin/python3

"""
Apply find-and-replace incrementally, from left to right (achieved by sorting). Replace with target if source matches, and keep track of the 'end' pointer (the last char replaced), so any intervals not covered by the index can be known and the original chars are copied down.
"""
def findReplaceString(S, indexes, sources, targets):
	res = ""
	end = 0

	data = sorted(zip(indexes, sources, targets))
	for idx, src, target in data:
		# add previously missed characters from original to fill the gap
		res += S[end:idx]
		end = idx

		srcLen = len(src)
		if S[idx:(idx+srcLen)] == src:
			# include target if matched
			res += target
			end += srcLen

	# need to add on any residual letters
	res += S[end:len(S)]
	return res


if __name__ == "__main__":
	print("Enter string: ", end="")
	S = input().strip()

	print("Enter indexes: ", end="")
	indexes = list(map(int, input().strip().split(' ')))

	print("Enter sources: ", end="")
	sources = input().strip().split(' ')

	print("Enter targets: ", end="")
	targets = input().strip().split(' ')

	output = findReplaceString(S, indexes, sources, targets)
	print(output)
