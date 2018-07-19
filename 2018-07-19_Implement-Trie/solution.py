#!/bin/python3

class Trie:

  """
  Multiway-trie so height is at most word length
  """
  def __init__(self, letter = ""):
    self.next = dict()


  def insert(self, word):
    # Base case
    if not word:
      self.next["end"] = True
      return

    letter, *rest = word
    if letter not in self.next:
      self.next[letter] = Trie(letter)

    self.next[letter].insert(rest)


  def search(self, word):
    if not word:
      return "end" in self.next

    letter, *rest = word
    if letter not in self.next:
      return False

    return self.next[letter].search(rest)


  def startsWith(self, prefix):
    if not prefix:
      return True

    letter, *rest = prefix
    if letter not in self.next:
      return False

    return self.next[letter].startsWith(rest)


trie = Trie()
commands = {'insert': lambda word: trie.insert(word),
            'search': lambda word: print(trie.search(word)),
            'prefix': lambda prefix: print(trie.startsWith(prefix)),
           }


if __name__ == "__main__":
  cmd = 'insert'
  options = list(commands.keys())
  print("Commands: {}".format(str(options)))
  while cmd != 'exit':
    print("Enter space-separated command and argument: ", end="")
    parsed = list(input().strip().split(' '))
    cmd = parsed[0]
    if cmd in commands:
      option, arg = parsed
      commands[option](arg)

  
