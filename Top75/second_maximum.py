"""
Implement a function find_second_maximum(lst) which returns the second largest element in the list.
"""
def find_second_maximum(lst):
    maxiumum = lst[0]
    second_max = lst[1]
    if len(lst) ==2:
        if second_max < maxiumum:
            return second_max
    else:
        for i in range(2, len(lst)):
            if (lst[i] > second_max) and (lst[i] < maxiumum):
                second_max = lst[i]
            elif lst[i] > maxiumum:
                second_max = maxiumum
                maxiumum = lst[i]
    return second_max


print(find_second_maximum([9,2,3,6]))