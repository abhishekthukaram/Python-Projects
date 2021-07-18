"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""
"""
METHOD1
"""


def find_averages_of_subarrays(arr,K):
    result = []
    for i in range(len(arr)-K +1):
        array_sum = 0
        for j in range(i, i+K):
            array_sum+=arr[j]
        result.append(array_sum/K)
    return result


print(find_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

"""
Method 2: Sliding window Approach
"""


def slidearray(input_array, array_size):
    result_array = []
    array_sum , array_start = 0.0, 0
    for array_end in  range(len(input_array)):
        array_sum+=input_array[array_end]
        if array_end >= array_size-1:
            result_array.append(array_sum/array_size)
            array_sum -= input_array[array_start]
            array_start+=1
    return result_array


print(slidearray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
