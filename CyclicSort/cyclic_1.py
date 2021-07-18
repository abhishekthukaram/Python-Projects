"""
Write a function to sort the objects in-place on their creation sequence number in
O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only
the sequence numbers, though each number is actually an object.
"""


def cyclicsort(input_array):
    i = 0
    while i <len(input_array):
        j = input_array[i]-1
        if input_array[i] != input_array[j]:
            input_array[i], input_array[j] = input_array[j], input_array[i]
        else:
            i+=1

    return input_array


print(cyclicsort([1, 2, 6, 4, 3, 2]))


