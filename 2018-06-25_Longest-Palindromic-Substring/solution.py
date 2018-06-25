#!/bin/python3

def longestPalindrome(s):
	length = len(s)
	end = length + 1
	res_start = res_end = res_len = 0

	# init DP table
	table = [[False for _ in range(end)] for _ in range(end)]

	for iter_len in range(1, end):
		iter_end = end - iter_len

		# checking for palindromes of length @iter_len starting at @start
		for start in range(iter_end):
			# init to True for base case of iter_len == 1 (trivial palindrome)
			isPalindrome = True

			if iter_len == 2:
				# base case of length 2 - must be repeated chars
				isPalindrome = s[start] == s[start + 1]

			elif iter_len > 2:
				# s[i:j] is palindrome <==> s[i+1:j-1] is palindrome && s[i] == s[j]
				isPalindrome = table[start + 2][start + iter_len - 1] and s[start] == s[start + iter_len - 1]

			# update table
			table[start + 1][start + iter_len] = isPalindrome

			# update accumulator result if longer palindrome found
			if isPalindrome and iter_len > res_len:
				res_len = iter_len
				res_start, res_end = start, start + iter_len

	# return sliced palindrome substring
	return s[res_start:res_end]


if __name__ == "__main__":
	print("Enter input string: ", end="")
	s = input().strip()
	palindrome = longestPalindrome(s)
	print("The longest palindromic substring is '{}' of length {}.".format(palindrome, len(palindrome)))
