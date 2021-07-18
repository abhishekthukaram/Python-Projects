"""
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th
index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest,
and so on. In other words, all the even-numbered indices will have the largest numbers in the list in
descending order and the odd-numbered indices will have the smallest numbers in ascending order.
"""

def find_max(lst):
    maxi = -999999
    if len(lst) ==1:
        print("Reached")
        return lst[0]
    elif len(lst) != 0:
        for i in lst:
            if i > maxi:
                maxi = i
    else:
        pass
    return maxi

def find_min(lst):
    mini = 999999
    if len(lst) != 0:
        for i in lst:
            if i < mini:
                mini = i
    else:
        pass
    return mini


def max_min(lst):
    result = [0] * len(lst)
    time_range = len(lst)
    start = 0
    while start < time_range:
        get_max = find_max(lst)
        lst.remove(get_max)
        result[start] = get_max
        if start == len(result)-1:
            break
        start+=1
        get_min = find_min(lst)
        lst.remove(get_min)
        result[start] = get_min
        start+=1

    return result


print(max_min([1,2,3,4,5]))