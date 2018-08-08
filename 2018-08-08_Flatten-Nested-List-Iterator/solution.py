#!/bin/python3

class NestedIterator:
  def __init__(self, nestedList):
    self.items = flatten(nestedList)
    self.curr = 0
    self.end = len(self.items)

  def next(self):
    res = self.items[self.curr]
    self.curr += 1
    return res

  def hasNext(self):
    return self.curr < self.end


def flatten(nestedList):
  res = []
  for item in nestedList:
    if isinstance(item, list):
      res += flatten(item)
    else:
      res.append(item)
  return res


if __name__ == "__main__":
  array = [1, [4, [6,7], [8, 9, 10], 12]]
  print(array)

  iterator = NestedIterator(array)
  while iterator.hasNext():
    print(iterator.next())
  
