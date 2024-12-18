# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import numpy as np

primeSec = []

def quad(a, b, n):
    return n**2 + a*n + b

def isPrime(n):
    isprime = True
    for i in range(2, int(np.sqrt(np.abs(n))) + 1, 1):
        if n % i == 0:
            isprime = False
    return isprime

def sol():
    for a in range (-1000, 1000):
        for b in range(-1000, 1000):
            n = 0
            while isPrime(quad(a, b, n)):
                n += 1
            primeSec.append([a,b,n])
            #print(primeSec)
            #print([a, b, n])
        

sol()
numPrimes = [i[2] for i in primeSec]
k = numPrimes.index(max(numPrimes))
print(primeSec[k])
l = primeSec[k]
a,b,n = l
print(a*b)
print(quad(a,b,n))