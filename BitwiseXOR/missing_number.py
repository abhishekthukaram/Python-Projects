"""
Given an array of n−1 integers in the range from 1 to  n find the one number that is missing from the array.
Example:
Input: 1, 5, 2, 6, 4
Answer: 3
"""


def missing_number(input_array):
    n = len(input_array)+1
    array_sum = 0
    for i in range(1 , n+1):
        array_sum+=i
    for number in input_array:
        array_sum-=number
    return array_sum


print(missing_number([1,5,2,6,4]))