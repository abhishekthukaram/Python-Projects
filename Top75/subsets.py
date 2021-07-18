"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsets(nums):
    result = []
    result.append([])
    for i in nums:
        n = len(result)
        print(i)
        for j in range(n):
            subset = 