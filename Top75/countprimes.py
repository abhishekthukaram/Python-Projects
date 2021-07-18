"""
Count the number of primes for a given number
"""

import math


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            if self.isprime(i):
                count += 1
        return count

    def isprime(self, number):
        if number <= 1:
            return False
        else:
            for i in range(2, int(number / 2) + 1):
                if number % i == 0:
                    return False
        return True


"""
Issue in the above solution Time Taken more , Optimized solution below 
"""

def countPrimes(n: int) -> int:
    if n < 3:
        return 0
    count = 0
    primes = [True] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        print(not primes[i])
        if not primes[i]:
            print("Entering If Loop", i )
            continue
        print(primes)
        # mark all multiplies of i not prime
        for j in range(i * i, n, i):
            print(j)
            primes[j] = False

    for i in range(2, n):
        if primes[i]:
            count += 1
    return count


print(countPrimes(21))