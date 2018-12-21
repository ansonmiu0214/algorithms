#!/bin/python3

'''
Greedy approach: make use of element frequencies and proceed with the constraint that, if there are x occurrences of n, then there must be at least x occurrences of 2*n in the array. Remove these occurrences (as they are matched), then proceed until all possible removals are made. The array can be reordered if there are no more elements at the end. Edge case of 0s are ignored (since 0*0 = 0), so just need to enforce there is an even number of 0s.
'''
def canReorderDoubled(A):
  if not A:
    return True

  # Setup frequency table
  table = {}
  for num in A:
    if num == 0:
      continue

    table[num] = (table[num] + 1) if num in table else 1

  # Iterate through elements by ascending absolute value
  keys = sorted(list(table.keys()), key=abs)

  for num in keys:
    if num not in table:
      continue

    target = num << 1
    if target not in table:
      # Double does not exist
      return False

    freq = table[num]
    if freq > table[target]:
      # Double does not occur as often as original value
      return False

    # Decrement table[target] frequency by table[num]
    # since number of matches equals table[num]
    if table[target] == freq:
      del table[target]
    else:
      table[target] -= freq

    del table[num]

  return table == {}


if __name__ == "__main__":
  print("Enter list of numbers: ", end="")
  nums = list(map(int, input().strip().split()))

  if len(nums) % 2 != 0:
    print("False - input array not even length.")
  else:
    res = canReorderDoubled(nums)
    print(res)
