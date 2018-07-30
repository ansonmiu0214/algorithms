#!/bin/python3

import time

"""
O(n^2) DP solution with predicate VP(i,j) defined as "s[i:(j+1)] is valid parenthesis".
"""
def longestValidParentheses_slow(s):
  res = 0
  count = len(s)
  
  if count == 0:
    return res

  # using False as init since VP(i,i) := False
  table = [[False for _ in range(count)] for _ in range(count)]

  # init VP(i,i+1) := s[i] == '(' and s[i+1] == ')'
  for i in range(count - 1):
    if s[i] == '(' and s[i+1] == ')':
      res = max(res, 2)
      table[i][i+1] = True

  # general case
  for row in range(count - 1, -1, -1):
    this = s[row]
   
    # ignore if not open bracket
    if this != '(':
      continue

    # '()' defines intervals of 2, already did [row+1]
    for col in range(row + 3, count, 2):
      that = s[col]

      # ignore if not close bracket
      if that != ')':
        continue

      curr = col - row + 1

      # wrap case: inner substring is valid parentheses
      if table[row+1][col-1]:
        table[row][col] = True
        res = max(res, curr)
        continue

      # adjacent case: VP(i,k) and VP(k+1,j) for some k
      for k in range(row + 1, col - 1, 2):
        if table[row][k] and table[k+1][col]:
          table[row][col] = True
          res = max(res, curr)
          break

  return res


"""
O(n) DP solution with table[x] := length of LVP ending at s[x]
"""
def longestValidParentheses(s):
  count = len(s)
  table = [0 for _ in range(count)]
  res = 0

  for i in range(1, count):
    curr, prev = s[i], s[i-1]

    # seeing [old] + "()", can extend LVP ending at [old]
    if curr == ')' and prev == '(':
      table[i] = table[i-2] + 2
      res = max(res, table[i])

    elif curr == ')' and prev == ')':
      old_lvp = table[i-1]        # length of LVP ending at s[i-1]
      old_open = i - table[i-1]   # index of opening of LVP ending at s[i-1]
      open_index = old_open - 1   # index of opening of LVP ending at s[i]

      if open_index >= 0 and s[open_index] == '(':
        inner_len = table[i-1]
        outer_adj = table[open_index - 1]    # currently closing VP(open_index, i) so carry over from table[open_index - 1]
        table[i] = inner_len + outer_adj + 2
        res = max(res, table[i])

  return res
      

if __name__ == "__main__":
  print("Enter string: ", end="")
  s = input().strip()

  # O(n^2) solution
  start = time.perf_counter()
  res = longestValidParentheses_slow(s)
  stop = time.perf_counter()
  
  print("O(n^2) algorithm: {}".format(res))
  print("Elapsed: {}".format(stop - start))

  # O(n) solution
  start = time.perf_counter()
  res = longestValidParentheses(s)
  stop = time.perf_counter()

  print("O(n) algorithm: {}".format(res))
  print("Elapsed: {}".format(stop - start))
