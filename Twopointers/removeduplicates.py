"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing
the duplicates in-place return the length of the subarray that has no duplicate in it.
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
"""

"""
Method1: Use Dict
"""

def remove_duplicates1(arr):
  result = {}
  for i in arr:
    if i not in result:
      result[i]=1
    else:
        if result[i] == 0:
            del result[i]
  return len(result)


print(remove_duplicates1([2, 2, 2, 11]))
print(remove_duplicates1([2, 3, 3, 3, 6, 9, 9]))


"""
Method2: Use 2 pointers
"""

def remove_duplicates(arr):
    non_duplicate = 1
    compare = 1
    while compare < len(arr):
        if arr[non_duplicate-1] != arr[compare]:
            arr[non_duplicate] = arr[compare]
            non_duplicate+=1
        compare+=1
    return non_duplicate

print(remove_duplicates([2, 2, 2, 11]))
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
