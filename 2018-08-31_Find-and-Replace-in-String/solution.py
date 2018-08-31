#!/bin/python3

def findReplaceString(S, indexes, sources, targets):
	res = ""
	offset = 0
	end = 0

	data = sorted(zip(indexes, sources, targets))
	for idx, src, target in data:
		# add previously missed characters from original to fill the gap
		res += S[end:idx]
		end = idx

		srcLen = len(src)
		if S[idx:(idx+srcLen)] == src:
			res += target
			offset += len(target) - srcLen
			end += srcLen

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
