"""
Implement a function right_rotate(lst, k) which will rotate the given list by k. This means
that the right-most elements will appear at the left-most position in the list and so on.
You only have to rotate the list by one element at a time.
"""


def right_rotate(lst, k):
    start = 0
    if len(lst) == 0:
        return []
    else:
        while start < k:
            element = lst.pop(-1)
            print(element)
            lst.insert(0, element)
            start += 1
    return lst


print(right_rotate([10,20,30,40,50], 3))