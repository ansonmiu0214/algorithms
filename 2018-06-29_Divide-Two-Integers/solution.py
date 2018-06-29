#!/bin/python3

"""
Inner loop runs O(log(x/y)) with divisor/quotient doubling every time.
"""
def divide(dividend, divisor):
	if dividend == 0: return 0
	is_positive = ~((dividend > 0) ^ (divisor > 0))
	quotient = 0
	x, y = abs(dividend), abs(divisor)

	while x >= y:
		inner_quo, inner_divisor = 1, y
		while inner_divisor + inner_divisor < x:
			inner_divisor += inner_divisor
			inner_quo += inner_quo
		quotient += inner_quo
		x -= inner_divisor

	res = quotient if is_positive else -quotient
	bound = 2147483648
	return min(res, bound - 1) if is_positive else max(res, -bound)


if __name__ == "__main__":
	print("Enter space-separated dividend and divisor: ", end="")
	dividend, divisor = list(map(int, input().strip().split(' ')))
	res = divide(dividend, divisor)
	print("{} // {} = {}".format(dividend, divisor, res))
