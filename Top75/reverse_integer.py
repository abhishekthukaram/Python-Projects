"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to
go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


def reverse(x):
    count = 0
    if x > 2**31-1 or x < -2 **31-1:
        return False
    if x < 0:
        check_positive = True
        x = x * -1
    else:
        check_positive = False
    while x >0:
        extract = x%10
        count = count*10 + extract
        x = x//10
    if check_positive:
        count = count * -1
    if count > 2**31-1 or count < 2**31-1:
        return False
    return count


print(reverse(123))