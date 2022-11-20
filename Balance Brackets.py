# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:38:42 2022

@author: Filipe Pacheco

"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s):
  # Write your code here
  s_len = len(s) # take the lenght of s
  s_left = s[:s_len//2] # divide the s array into a left part
  s_right = s[s_len//2:] # divide the s array into a right part
  count = 0 # aux var to count the matchs
  
  for i in range(s_len//2):
    if s_left[i] == "{" and s_right[s_len//2-i-1] == "}": # check the pair
        count += 1
    if s_left[i] == "[" and s_right[s_len//2-i-1] == "]": # check the pair
        count += 1
    if s_left[i] == "(" and s_right[s_len//2-i-1] == ")": # check the pair
        count += 1
              
  if count == s_len//2: #check if is balanced
      output = True
  else:
      output = False
  
  return output



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
  s1 = "{[(])}"
  expected_1 = False
  output_1 = isBalanced(s1)
  check(expected_1, output_1)

  s2 = "{{[[(())]]}}"
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  