## What is the largest prime factor of the number 600851475143?

import math
import numpy as np


def primeFactors(n):
    if isPrime(n):
        a.append(n)
        return
    for i in range(2, int(math.sqrt(n)) + 1, 1):  # since an odd number cant have even factors
        if n % i == 0: # then i & n/i are factors
            primeFactors(i) # check for further factors
            primeFactors(int(n/i))
            return


def isPrime(n):
    isprime = True
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            isprime = False
    return isprime


a = []
primeFactors(99999)
print(a)
print(max(a))
