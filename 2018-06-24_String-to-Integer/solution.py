#!/bin/python3

"""
Transition table via DFA construction.
"""
def atoi(str):
	# set up state transition table
	next_state = []

	# trim whitespace
	str = str.strip(" ")

	# set up transition table
	digits = "0123456789"
	tokens = ['+', '-'] + list(digits)
	digit_transitions = [3] * len(digits)
	next_state.append(dict(zip(tokens, [1, 2] + digit_transitions)))
	next_state.append(dict(zip(digits, digit_transitions)))
	next_state.append(dict(zip(digits, digit_transitions)))
	next_state.append(dict(zip(digits, digit_transitions)))

	res, matched, int_res = "", False, 0
	int_min = - (2 ** 31)
	int_max = -int_min - 1
	end = len(str)

	curr_state = 0
	for i in range(end):
		letter = str[i]

		# leave loop on error state
		if letter not in next_state[curr_state]:
			break	

		curr_state = next_state[curr_state][letter]
		res += letter

		# update flag for accepting state
		if not letter in "+-":
			matched = True

	# return default on error state
	if not matched:
		return int_res

	# normalise result
	int_res = int(res)
	return max(int_min, int_res) if int_res < 0 else min(int_max, int_res)


if __name__ == "__main__":
	print("Enter number to convert: ", end="")
	str = input()
	num = atoi(str)
	print("The converted number is: {}".format(num))
