# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:40:14 2022

@author: filip
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findEncryptedWord(s):
  # Write your code here
  new_s = ""
  if len(s) % 2 == 0:
      len_s = len(s)//2-1
  else:
      len_s = len(s)//2
  aux_s = s[len_s]
  aux_left = s[:len_s]
  aux_right = s[len_s+1:]
  
  if len(aux_left) > 2:
      aux_left = aux_left[len(aux_left)//2]+aux_left[len(aux_left)//2:]+aux_left[:len(aux_left)//2+1]
  if len(aux_right) > 2:
      aux_right = aux_right[len(aux_right)//2]+aux_right[len(aux_right)//2:]+aux_right[:len(aux_right)//2+1]

 
  return aux_s+aux_left+aux_right










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  check(expected_1, output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  