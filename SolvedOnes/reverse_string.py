"""
Write a function that reverses a string. The input string is given as an array of characters s.
"""
def reverse_string(s):
    left = 0
    right = len(s)-1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1
    return s


print(reverse_string(['h','e', 'l', 'l','o']))
print(reverse_string(['A','b', 'h','i']))