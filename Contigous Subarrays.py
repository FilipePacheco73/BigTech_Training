# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:16:49 2022

@author: Filipe Pacheco

"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(arr):
  # Write your code here
  output = []
  for i in range(len(arr)):
      sub_set = []
      sub_set.append(arr[i])
      for j in range(1,i+1):
          if max(arr[j-1:i]) < arr[i]:
              sub_set.append(arr[j-1:i+1])
              
      for j in range(len(arr),i+1,-1):
          if max(arr[i:j]) <= arr[i]:
              sub_set.append(arr[i:j])
 
      output.append(len(sub_set))
               
  return output
  
  
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  