"""
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
Name it merge_lists(lst1, lst2).
"""

def merge_lists(lst1, lst2):
    pos_lst1 = 0
    pos_lst2= 0
    index_result = 0
    result = []
    for i in range(len(lst1) + len(lst2)):
        result.append(i)
    while (pos_lst1 < len(lst1)) and (pos_lst2 < len(lst2)):
        if lst1[pos_lst1] < lst2[pos_lst2]:
            result[index_result] = lst1[pos_lst1]
            index_result += 1
            pos_lst1 += 1
        else:
            result[index_result] = lst2[pos_lst2]
            index_result += 1
            pos_lst2 += 1
    while (pos_lst1 < len(lst1)):
        result[index_result] = lst1[pos_lst1]
        index_result += 1
        pos_lst1 += 1
    while (pos_lst2 < len(lst2)):
        result[index_result] = lst2[pos_lst2]
        index_result += 1
        pos_lst2 += 1
    return result


print(merge_lists([1,3,4,5]
                  ,[2,6,7,8]))