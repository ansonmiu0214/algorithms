#!/bin/python3

"""
Avoid doing O(n^2) work by preprocessing `shifts` array to compute the
cumulative shift per letter, then applying them all at once. Wraparound from 'z' to 'a'
handled by applying modulo to the new index (computed w.r.t. 0 at first before offsetting
by ord('a') to get the required ordinal value).
"""
def shiftingLetters(S, shifts):
  # 1st letter gets every shift in the array,
  # 2nd letter gets every shift in the array except shifts[0], etc...
  shiftAcc = sum(shifts)
  finalShifts = []

  for shift in shifts:
    finalShifts.append(shiftAcc)
    shiftAcc -= shift

  initOffset = ord('a')
  NUM_OF_CHARS = 26

  # Define per-letter shifting function
  def shiftLetter(letter, shift):
    oldIdx = ord(letter) - initOffset
    newIdx = (oldIdx + shift) % NUM_OF_CHARS
    return chr(newIdx + initOffset)

  return "".join([shiftLetter(letter, finalShifts[idx]) for idx, letter in enumerate(S)])


if __name__ == "__main__":
  print("Enter initial string: ", end="")
  S = input().strip()

  print("Enter space-separated shifts: ", end="")
  shifts = list(map(int, input().strip().split(' ')))

  res = shiftingLetters(S, shifts)
  print(res)
