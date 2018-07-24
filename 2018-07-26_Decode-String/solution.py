#!/bin/python3

def decodeString(s):
  res, _ = decode(s)
  return res

"""
Returns tuple of inner result and the rest of the unprocessed.
"""
def decode(s):
  res = ""
  while s:
    letter = s[0]
    i = 1

    # parse count
    if s[:i].isnumeric():
      while s[:(i+1)].isnumeric():
        i += 1

      number = s[:i]
      count = int(number)
      
      # recursive call
      inner, s = decode(s[(i+1):])
 
      # append to result
      res += (inner * count)

    elif letter == ']':
      return res, s[1:]

    else:
      res += letter
      s = s[1:]

  return res, ""


if __name__ == "__main__":
  print("Enter input string: (e.g. 3[a]2[bc]) ", end="")
  pattern = input().strip()

  print(decodeString(pattern))
