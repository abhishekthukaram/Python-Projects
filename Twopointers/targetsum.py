"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
"""

def pair_with_targetsum(arr, target_sum):
  left_array, right_array = 0, len(arr)-1
  while left_array < right_array:
    if arr[left_array] + arr[right_array] == target_sum:
      return [left_array, right_array]
    if arr[left_array] + arr[right_array] > target_sum:
      right_array-=1
    else:
      left_array+=1
  return [-1,-1]


print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11],11))