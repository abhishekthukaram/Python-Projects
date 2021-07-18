"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of
size ‘k’.
"""


def maximum_subarray(input_array, array_size):
    max_sum = 0
    array_sum = 0
    start_position = 0
    for array_start in range(len(input_array)):
        array_sum+=input_array[array_start]
        if array_start >= array_size-1:
            max_sum = max(max_sum, array_sum)
            array_sum-=input_array[start_position]
            start_position+=1
    return max_sum


print(maximum_subarray([2, 1, 5, 1, 3, 2], 3))
print(maximum_subarray([2, 3, 4, 1, 5], 2))