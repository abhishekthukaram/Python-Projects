"""
Check which number occurs once
"""
def find_single_number1(arr):
    for i in arr:
        if arr.count(i) <=1:
            return i
    return -1


"""
Method 2: Using XOR Operatioon 
"""
def find_single_number(input_array):
    num = 0
    for i in input_array:
        num = num^i
    return num


print(find_single_number([1,5,2,6,4]))