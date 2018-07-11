#!/bin/python3

from collections import deque

base = ord('0')
radix = 10

def multiply(num1, num2):
	num1, num2 = str_to_int(num1), str_to_int(num2)
	return int_to_str(num1 * num2)


def str_to_int(num):
	res = 0
	for digit in num:
		res *= 10
		res += ord(digit) - base
	return res


def int_to_str(num):
	if num == 0:	return '0'

	res = deque()
	while num > 0:
		num, digit = divmod(num, radix)
		res.appendleft(chr(digit + base))

	return ''.join(res)


if __name__ == "__main__":
	print("Enter two space-separated non-negative numbers: ", end="")

	num1, num2 = list(input().strip().split(' '))

	print("{} x {} = {}".format(num1, num2, multiply(num1, num2)))
