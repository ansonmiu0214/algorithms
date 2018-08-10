#!/bin/python3

from collections import deque

"""
Stack-based approach with predefined function pointers.
"""
def evaluateRPN(tokens):

  funcs = {
    '+': lambda x, y: int(x + y),
    '-': lambda x, y: int(x - y),
    '*': lambda x, y: int(x * y),
    '/': lambda x, y: int(x / y)
  }

  stack = deque()
  for token in tokens:
    if token in funcs:
      op2 = stack.pop()
      op1 = stack.pop()

      stack.append(funcs[token](op1, op2))
    else:
      stack.append(int(token))

  return stack[0]


if __name__ == "__main__":
  print("Enter space-separated tokens: ", end="")
  tokens = list(map(str, input().strip().split(' ')))

  res = evaluateRPN(tokens)
  print("Answer: {}".format(res))
