"""
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def singleNumber(nums):
    for i in nums:
        if nums.count(i) ==1:
            return i


print(singleNumber([1,1,2,2,3]))