"""
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’
numbers out of the total ‘n+1’ numbers, find the missing number.
"""
"""
Method1
"""
def find_missing_number(nums):
  n = len(nums)
  for i in range(n):
    if i not in nums:
      return i
  return -1


"""
Meghod 2 : Using Cyclic Sort
"""

