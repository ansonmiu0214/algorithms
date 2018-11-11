#!/bin/python3

def diffWaysToCompute(string):
  
  # Map of operator (char) to the function
  ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y
  }

  # Top-down memoisation - map of (sub)expression to possible values
  memo = {}

  def compute(string):
    if string in memo:
      return memo[string]

    res = []
    
    # Find operator, partition and compute
    for idx, char in enumerate(string):
      # Ignore numbers
      if char not in ops:
        continue

      # Partition on this index
      left, right = string[:idx], string[idx+1:]

      leftVals = memo[left] if left in memo else compute(left)
      rightVals = memo[right] if right in memo else compute(right)

      combinedVals = [ops[char](left, right) for left in leftVals for right in rightVals]
      res += combinedVals

    # Base case: no operator, purely numeric
    if not res:
      res = [int(string)]

    memo[string] = res
    return res

  return compute(string)


if __name__ == "__main__":
  print("Enter expression (only support +,-,*): ", end="")
  string = input().strip()

  values = diffWaysToCompute(string)
  print(values)
