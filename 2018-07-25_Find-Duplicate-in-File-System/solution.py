#!/bin/python3

import re

def findDuplicate(paths):
  duplicate_content = set()
  content_to_path = dict()

  for entry in paths:
    path, *files = entry.split(' ')

    for item in files:
      # split using brackets as delimiters
      name, content, _ = re.split('\(|\)', item)

      name = path + "/" + name
      if content in content_to_path:
        # add path to hash table
        duplicate_content.add(content)
        content_to_path[content].append(name)
      else:
        # add new entry to hash table
        content_to_path[content] = [name]
  
  # extract paths grouped by content
  return list(map(lambda content: content_to_path[content], duplicate_content))


if __name__ == "__main__":
  paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
  print(paths)

  files = findDuplicate(paths)
  print(files)
