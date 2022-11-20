# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:53:17 2022

@author: Filipe Pacheco

"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOperations(arr):
  # Write your code here
  max_int = 10
  arrs = arr.copy()
  arrs.sort() # sorted array
  output = 0
  while arrs != arr and output < max_int:
      aux = 0 # break point
      output += 1
      if arr[0] > arr[1]:
          aux_arr = arr[:2].copy()
          aux_arr.reverse()
          arr[:2] = aux_arr
      else:
          while arr[aux] < arr[aux+1] and aux < len(arr):
              aux += 1 
          
          aux_arr = arr[aux:].copy()
          aux_arr.reverse()
          arr[aux:] = aux_arr
  
  return output
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
  