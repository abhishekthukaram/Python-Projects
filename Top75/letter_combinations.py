"""
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.
"""
import itertools
def letterCombinations(digits):
    result_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    result = []
    temp_list = []
    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        return result_dict[digits]
    else:
        for number in digits:
            temp_list.append(result_dict[number])
        answer = list(itertools.product(*temp_list))
        print(answer)
        for element in answer:
            result.append("".join(element))
    return result


print(letterCombinations('234'))