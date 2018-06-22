#!/bin/python3


def longest_substring_no_repeat(s):
	end = len(s)
	left = right = 0
	res = curr = 0
	substring = ""
	seen = set()

	while right < end:
		if s[right] in seen:
			if curr > res:
				substring = s[left:right]
				res = curr

			while s[right] in seen:
				seen.remove(s[left])
				left += 1
				curr -= 1

		curr += 1
		seen.add(s[right])
		right += 1

	if curr > res:
		substring = s[left:right]
		res = curr

	return res, substring


if __name__ == "__main__":
	print("Enter word: ", end="")
	s = input().strip()
	res, substring = longest_substring_no_repeat(s)
	print("Longest substring without repeated characters is '{}' of length {}.".format(substring, res))
	
