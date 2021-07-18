import math

import math
def countPrimes(n):
    count = 0
    if n ==1 or n == 0 or n < 0:
        return 0
    integer_compare = int(math.sqrt(n))
    for i in range(2,n):
        for j in range(2, integer_compare):
            if i%j != 0:
                count+=1
    return count


print(countPrimes(10))
print(countPrimes(1))
print(countPrimes(0))
"""
def countPrimes(number):
    count = 0
    integer_compare = int(math.sqrt(number))
    for j in range(1, integer_compare+1):
        #print(j)
        if number%j == 0:
            print("It is divisible by {}".format(j))
            count += 1
    return count
    #print(count)
    if count == 1:
        return "Prime"
    return "Not a Prime number"


print(countPrimes(10))
"""
