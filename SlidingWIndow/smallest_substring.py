"""
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
Input: [3, 4, 1, 1, 6], S=8
Output: 3
"""

def smallest_subarray_with_given_sum(s, arr):
    min_length = 9999999
    start_position = 0
    array_sum = 0
    for array_position in range(len(arr)):
        array_sum+=arr[array_position]
        while array_sum>=s:
            min_length = min(min_length, (array_position-start_position+1))
            array_sum -= arr[start_position]
            start_position += 1
    return min_length


print(smallest_subarray_with_given_sum(8,[3, 4, 1, 1, 6]))
print(smallest_subarray_with_given_sum(7,[2, 1, 5, 2, 8]))
print(smallest_subarray_with_given_sum(8,[3, 4, 1, 1, 6]))