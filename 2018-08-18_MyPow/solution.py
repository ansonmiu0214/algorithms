#!/bin/python3

"""
Divide-and-conquer approach with special care on negative powers.
Recognise negative power at top level and perform reciprocal on result,
but still invoke the power function on a positive exponent.

O(log(n)) running time complexity.
"""
def myPow(x, n):
  res = dcPower(x, abs(n))
  return res if n > 0 else 1/res

def dcPower(x, n):
  if n == 0:  return 1

  half, rem = divmod(n, 2)
  other = dcPower(x, half)
  res = other * other

  return res if rem == 0 else res * x


if __name__ == "__main__":
  print("Enter space-separated integers, x and n, to compute x^n: ", end="")
  x, n = list(map(int, input().strip().split(' ')))

  res = myPow(x, n)
  print("{} ** {} = {}".format(x, n, res))
