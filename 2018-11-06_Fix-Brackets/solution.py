#!/bin/python3

from collections import deque

def fixBrackets(s):
  res = []

  brackets = { '(', ')', '{', '}', '[', ']' }
 
  openBrackets = { '(', '[', '{' }
  bracketPairs = { ')': '(', ']': '[', '}': '{' }

  openStack = deque([])
  openFreq = { '(': 0, '[': 0, '{': 0 }

  for idx, char in enumerate(s):
    if char not in brackets:
      res.append(char)
      continue

    if char in openBrackets:
      res.append(char)
      openStack.append((idx, char))
      openFreq[char] += 1
      continue

    matchingOpen = bracketPairs[char]
    if openFreq[matchingOpen] == 0:
      res.append("")
      continue

    while matchingOpen != openStack[-1][1]:
      idxToRemove, bracketToRemove = openStack.pop()
      res[idxToRemove] = ""
      openFreq[bracketToRemove] -= 1

    openStack.pop()
    res.append(char)
    openFreq[matchingOpen] -= 1

  while openStack:
    idxToRemove, _ = openStack.pop()
    res[idxToRemove] = ""

  return "".join(res)


if __name__ == "__main__":
  print("Enter input string: ", end="")
  s = input().strip()

  res = fixBrackets(s)
  print(res)

