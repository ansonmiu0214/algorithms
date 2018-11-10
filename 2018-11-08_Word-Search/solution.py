#!/bin/python3

'''
# Return true iff target occurs in the grid.
def wordSearch(grid, target):
  rows = len(grid)
  cols = len(grid[0])

  seen = {}

  def dfs(x, y, word):
    idx = x * rows + y
    seen[idx] = True
    print("x={} y={} grid={} word={}".format(x, y, grid[x][y], word))
    print(seen)

    if word == []:
      del seen[idx]
      return True

    head, *rest = word
    if grid[x][y] != head:
      del seen[idx]
      return False

    upIdx = (x-1) * rows + y
    if x > 0 and upIdx not in seen:
      if dfs(x-1, y, rest):
        return True

    downIdx = (x+1) * rows + y
    if x < rows - 1 and downIdx not in seen:
      if dfs(x+1, y, rest):
        return True

    leftIdx = x*rows + (y-1)
    if y > 0 and leftIdx not in seen:
      if dfs(x, y-1, rest):
        return True

    rightIdx = x*rows + (y+1)
    if y < cols - 1 and rightIdx not in seen:
      if dfs(x, y+1, rest):
        return True

    del seen[idx]
    print("backtrack x={} y={} seen={}".format(x, y, seen))
    return False
'''

# Returns the set of words in the trie that are also in the grid.
def wordSearch(grid, trie):
  rows = len(grid)
  cols = len(grid[0])

  seen = {}

  found = set()

  def dfs(x, y, trieNode, word=""):
    idx = x * rows + y
    seen[idx] = True

    if trieNode.isEnd:
      found.add(word)

    if x < 0 or y < 0 or x == rows or  y == cols:
      del seen[idx]
      return

    head = grid[x][y]
    # print("({},{}) head={} matched={}".format(x, y, head, word))
    if head not in trieNode.next:
      del seen[idx]
      return

    nextTrie = trieNode.next[head]

    upIdx = (x-1) * rows + y
    newWord = word + str(head)
    if x >= 0 and upIdx not in seen:
      dfs(x-1, y, nextTrie, newWord)

    downIdx = (x+1) * rows + y
    if x < rows and downIdx not in seen:
      dfs(x+1, y, nextTrie, newWord)

    leftIdx = x*rows + (y-1)
    if y >= 0 and leftIdx not in seen:
      dfs(x, y-1, nextTrie, newWord)

    rightIdx = x*rows + (y+1)
    if y < cols and rightIdx not in seen:
      dfs(x, y+1, nextTrie, newWord)

    del seen[idx]
    return


  for x in range(rows):
    for y in range(cols):
      dfs(x, y, trie)

  return found
  

class TrieNode:

  def __init__(self):
    self.next = {}
    self.isEnd = False 

  def insert(self, word):
    if len(word) == 0:
      self.isEnd = True
      return

    head, *rest = word
    if head in self.next:
      self.next[head].insert(rest)
    else:
      node = TrieNode()
      node.insert(rest)
      self.next[head] = node 

  def __repr__(self):
    res = ""
    if self.isEnd:
      res += "."

    for nxt in self.next:
      res += "("
      res += (nxt + str(self.next[nxt]))
      res += ")"

    return res


if __name__ == "__main__":
  '''
  grid = [['h','a','p'],
          ['a','y','p'],
          ['d','a','r']]

  words = ["happy", "prada", "happier", "hyr"]
  trie = TrieNode()
  for word in words:
    trie.insert(word)

  # target = "happy"
  # target = "prada"
  # found = wordSearch(grid, target)

  found = wordSearch(grid, trie) 
  print(found)
  '''

  print("Number of rows: ", end="")
  rows = int(input().strip())

  grid = []
  for idx in range(rows):
    print("Row {}: ".format(idx + 1), end="")
    grid.append(list(input().strip()))

  print()
  print("Space-separated words: ", end="")
  words = input().strip().split()

  trie = TrieNode()
  for word in words:
    trie.insert(word)

  print(trie)

  found = wordSearch(grid, trie)
  print(found)
