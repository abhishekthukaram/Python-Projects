"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""

def isPalindrome(s):
    punc = '''!()-[]{};:'"\, <>./`?@#$%^&*_~'''
    string_compare = ""
    for i in s:
        if i not in punc:
            string_compare+=i
    print(string_compare)
    final_output = string_compare.lower()
    return final_output[::] == final_output[::-1]


print(isPalindrome("`l;`` 1o1 ??;l`"))

