"""
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
Find the two numbers that appear only once.
"""
def find_single_numbers(nums):
    result = []
    for each_number in nums:
        if nums.count(each_number) == 1:
            result.append(each_number)
    return result


print(find_single_numbers([2, 1, 3, 2]))