#!/bin/python3

"""
Solve the problem for one word (using dictionaries to validate bijection) and filter over the entire list.
"""
def findAndReplacePattern(words, pattern):
  
  # define lambda validate function
  def validate(word):
    # two maps to validate the bijection
    wordToPattern, patternToWord = {}, {}

    for wordLetter, patternLetter in zip(word, pattern):
      if wordLetter not in wordToPattern and patternLetter not in patternToWord:
        wordToPattern[wordLetter] = patternLetter
        patternToWord[patternLetter] = wordLetter
      elif wordLetter in wordToPattern and wordToPattern[wordLetter] != patternLetter:
        return False
      elif patternLetter in patternToWord and patternToWord[patternLetter] != wordLetter:
        return False

    return True

  return list(filter(validate, words))


if __name__ == "__main__":
  print("Enter space-separated words: ", end="")
  words = list(map(lambda x: x.strip(), input().strip().split(' ')))

  print("Enter pattern: ", end="")
  pattern = input().strip()

  validWords = findAndReplacePattern(words, pattern)
  print(validWords)
