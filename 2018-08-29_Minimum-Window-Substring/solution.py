#!/bin/python3

"""
Sliding window approach with use of dictionaries and sets to keep track of letter frequency since @param t can contain duplicate letters, and the letter frequencies of each letter in the window must be at least that of in @param t. The use of frequency tables (implemented as Python dictionaries) allow for O(1) lookups and updates to achieve O(n) running time complexity at the cost of O(n) space complexity.
"""
def minWindow(s, t):
	mainLength, patternLength = len(s), len(t)

	# base case: pattern longer than main string
	if mainLength < patternLength:
		return ""

	window = None
	
	# setup pattern letter frequency table
	patternFreq = {}
	for letter in t:
		if letter in patternFreq:	patternFreq[letter] += 1
		else:											patternFreq[letter] = 1

	# setup window pointers and letter frequency table
	left, right = 0, patternLength
	windowFreq = {}
	for letter in s[left:right]:
		if letter in windowFreq:	windowFreq[letter] += 1
		else:											windowFreq[letter] = 1

	# initialise matched letters on initial window
	matchedCount = 0
	lettersMatched = set()		# prevent adding frequencies for duplicate letters
	for letter in windowFreq:
		if letter in patternFreq and windowFreq[letter] >= patternFreq[letter]:
			matchedCount += patternFreq[letter]
			lettersMatched.add(letter)

	# main sliding window loop
	while right <= mainLength:
		if matchedCount == patternLength:
			# update minimum window
			if window is None or len(window) > (right - left):
				window = s[left:right]

			# advance left pointer and update frequencies
			if windowFreq[s[left]] == 1:	del windowFreq[s[left]]
			else:													windowFreq[s[left]] -= 1

			# update matched count if removing letter in pattern
			if s[left] in patternFreq:
				if s[left] not in windowFreq or windowFreq[s[left]] < patternFreq[s[left]]:
					matchedCount -= patternFreq[s[left]]
					lettersMatched.remove(s[left])

			left += 1

		else:
			if right == mainLength:	break

			# advance right pointer and update frequencies
			if s[right] in windowFreq:	windowFreq[s[right]] += 1
			else:												windowFreq[s[right]] = 1

			# update matched count if adding letter in pattern
			if s[right] in patternFreq:
				if windowFreq[s[right]] >= patternFreq[s[right]] and s[right] not in lettersMatched:
					matchedCount += patternFreq[s[right]]
					lettersMatched.add(s[right])

			right += 1

	return "".join(window) if window else ""


if __name__ == "__main__":
	print("Enter the main string: ", end="")
	s = input().strip()

	print("Enter the lookup pattern: ", end="")
	t = input().strip()

	window = minWindow(s, t)
	print("Smallest window: {}".format(window))
