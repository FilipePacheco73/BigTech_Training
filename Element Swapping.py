# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:40:41 2022

@author: Filipe Pacheco

"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMinArray(arr, k):
  # Write your code here
  aux_count = len(arr)-1 # count to auxiliate the backwards direction of swaps
  arr_test = arr.copy() # copy for test
  for i in range(k):
      if arr_test[aux_count-1] > arr_test[aux_count]: #check condition
          aux = arr_test[aux_count-1] #receive the temp variable
          arr_test[aux_count-1] = arr_test[aux_count]
          arr_test[aux_count] = aux
      aux_count -= 1
      
  aux_count = len(arr)-2
  arr_test2 = arr.copy() # copy for test
  for i in range(k):
      if arr_test2[aux_count-1] > arr_test2[aux_count]: #check condition
          aux = arr_test2[aux_count-1] #receive the temp variable
          arr_test2[aux_count-1] = arr_test2[aux_count]
          arr_test2[aux_count] = aux
      aux_count -= 1
      
  if arr_test[0] < arr_test[1]:
      arr = arr_test 
  else:
      arr = arr_test2
  
  return arr
  









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
  n_1 = 3
  arr_1 = [5, 3, 1]
  k_1 = 2 
  expected_1 = [1, 5, 3]
  output_1 = findMinArray(arr_1,k_1)
  check(expected_1, output_1)

  n_2 = 5
  arr_2 = [8, 9, 11, 2, 1]
  k_2 = 3
  expected_2 = [2, 8, 9, 11, 1]
  output_2 = findMinArray(arr_2,k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  