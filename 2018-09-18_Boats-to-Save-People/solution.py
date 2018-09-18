#!/bin/python3

"""
Greedy approach by matching heaviest passenger with lightest - if weight exceeds,
let the heavier passenger use the boat on its own as it is possible for an alternative
to match with the lighter passenger.
"""
def numRescueBoats(people, limit):
  people.sort()

  lightIdx= 0
  heavyIdx = len(people) - 1
  numBoats = 0
  boats = []

  # greedily match heaviest and lightest person
  while lightIdx < heavyIdx:
    twoWeight = people[lightIdx] + people[heavyIdx]
    
    # need at least one boat for both cases
    numBoats += 1
    
    if twoWeight <= limit:
      # boat can carry two people
      boats.append((people[lightIdx], people[heavyIdx]))
      lightIdx += 1
      heavyIdx -= 1
    else:
      # greedily carry the heaviest person
      boats.append((people[heavyIdx]))
      heavyIdx -= 1

  # need one more boat to carry the middle passenger 
  if lightIdx == heavyIdx:
    boats.append((people[heavyIdx]))
    numBoats += 1

  return numBoats, boats


if __name__ == "__main__":
  print("Enter space-separated weights: ", end="")
  people = list(map(int, input().strip().split(' ')))

  print("Enter boat weight limit: ", end="")
  limit = int(input().strip())

  numBoats, boats = numRescueBoats(people, limit)
  print("{} boat{} required, organised as follow:".format(numBoats, "" if numBoats == 1 else ""))
  print(boats)
    
