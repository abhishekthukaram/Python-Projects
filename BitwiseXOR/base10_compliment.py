"""
Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7
as “0111” in binary.
The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0
to a 1. For example, the binary complement of “1010” is “0101”.
"""

def compliment_number(number):
    bit_count , n = 0, number
    while n>0:
        bit_count+=1
        n=n>>1
    print("Number of bits is", bit_count)
    all_bits = pow(2, bit_count) -1
    return number ^ all_bits


print(compliment_number(255))