#!/bin/python3

class Iterator:
  def __init__(self, nums):
    self.nums = nums

  def hasNext(self):
    return self.nums != []

  def next(self):
    val = self.nums[0]
    self.nums = self.nums[1:]
    return val


class PeekingIterator:
  def __init__(self, iterator):
    self.iterator = iterator
    self.temp = None

  def peek(self):
    if not self.temp:
      self.temp = self.iterator.next()

    return self.temp

  def next(self):
    val = self.temp
    if val:
      self.temp = None
      return val

    return self.iterator.next()

  def hasNext(self):
    return (self.temp is not None) or self.iterator.hasNext()


if __name__ == "__main__":
  print("Enter space-separated numbers to initialise PeekIterator: ", end="")
  nums = list(map(int, input().strip().split(' ')))
  iterator = PeekingIterator(Iterator(nums))

  print("Commands: (peek | next | hasNext | exit)")
  while True:
    print("> ", end="")
    cmd = input().strip()
    if cmd == 'peek':
      print(iterator.peek())
    elif cmd == 'next':
      print(iterator.next())
    elif cmd == 'hasNext':
      print(iterator.hasNext())
    elif cmd == 'exit':
      exit(0)
