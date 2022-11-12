# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:01:06 2022

@author: filip
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here

  aux = 0
  minimal = 20
  check_arr = arr # create a copy
  check_arr.sort(reverse=True) # sort array
  
  while aux < len(arr)-1:
      temp = check_arr[aux+1]
      check_arr[aux+1] = check_arr[aux]
      check_arr[aux] = temp
      aux += 1
      
      maximal = [] # contains the awkwardness
      for i in range(len(arr)-1):
          maximal.append(abs(check_arr[i]-check_arr[i+1]))
          
      maximal.append(abs(check_arr[-1]-check_arr[0]))
      
      if minimal > max(maximal):
          minimal = max(maximal)
    
  return minimal











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
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  