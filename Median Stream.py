# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:36:19 2022

@author: filip
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMedian(arr):
  # Write your code here
  
  output = [arr[0]] # first array number
  
  for i in range(1,len(arr)):
      aux_arr = arr[:i+1] # select the numbers to be calculated
      aux_arr.sort()
      aux_l = len(aux_arr)//2 # size of interation
      if len(aux_arr) % 2 == 0: # checks if the array's lenght is even
          output.append(int(.5*(aux_arr[aux_l-1] + aux_arr[aux_l])))
      else: # the length is odd
          output.append(aux_arr[aux_l])              
          
  
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
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  