#!/bin/python3

"""
O(n) space complexity + O(n) running time complexity where n = len({set of supported letters})
Iterative solution using predefined descending order of numbers with Roman numeral character.
"""
def intToRoman(num):
  lookup = list(zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
                    ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']))

  res = ""
  for val, letter in lookup:
    quotient, num = divmod(num, val)
    res += (letter * quotient)
  return res


if __name__ == "__main__":
  print("Enter an integer less than 4000: ", end="")
  num = int(input().strip())
  
  roman = intToRoman(num)
  print("Roman numberal: {}".format(roman))
