"""
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and
return the new length of the array.
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
"""

"""
Method1: Use dict method
"""

def remove_element(arr, key):
    result = {}
    count= 0
    for i in arr:
        if i in result:
            result[i]+=1
        else:
            result[i] = 1
    for key_value in result.keys():
        if key_value != key:
            count+=1
    return count


print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_element([2, 11, 2, 2, 1],2))


"""
Method2: Use 2 pointer
"""
def remove_element2(arr, key):
    next_element = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element+=1
    return next_element


print(remove_element2([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_element2([2, 11, 2, 2, 1],2))




