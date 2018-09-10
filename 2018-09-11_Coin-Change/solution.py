#!/bin/python3

"""
Bottom-up dynamic programming approach with base case on '0 coins needed to
make $0', with O(C*amount) running time complexity and space complexity where
C is the number of coins in the input denomination set.
"""
def coinChange(coins, amount):
	# initialise DP table
	res = [0] + [-1 for _ in range(amount)]

	for curr in range(1, amount + 1):
		# try each denomination
		for coin in coins:
			coinTooBig = coin > curr
			cannotBuildResidual = res[curr - coin] < 0

			# skip coin if cannot build result
			if coinTooBig or cannotBuildResidual:
				continue

			count = res[curr - coin] + 1
			if res[curr] == -1 or count < res[curr]:
				res[curr] = count

	return res[amount]


if __name__ == "__main__":
	print("Enter space-separated coin denominations: ", end="")
	coins = list(map(int, input().strip().split(' ')))

	print("Enter amount to make: ", end="")
	amount = int(input().strip())

	change = coinChange(coins, amount)
	if change < 0:
		print("Cannot use coin set to build ${}.".format(amount))
	else:
		print("{} coin{} needed to build ${}.".format(change, "" if change == 1 else "s", amount))
