"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.
"""

"""
def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(1, n + 1):
        if i in nums:
            print("REACGED")
            nums.remove(i)
            print("AFTER UPDATE",nums)
        else:
            nums.append(i)
            print(nums)

    return nums

"""
#Option 2 :

def findDisappearedNumbers(nums):
    n = len(nums)
    result = []
    result_dict = {}
    for i in nums:
        if i in result_dict.keys():
            result_dict[i] += 1
        else:
            result_dict[i] = 1
    for element in range(1, n + 1):
        if element in result_dict.keys():
            result_dict[element] -= 1
        else:
            result.append(element)
    return result


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))