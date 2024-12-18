## What is the 10 001st prime number?

import math

def isPrime(n):
    isprime = True
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            isprime = False
            break
    return isprime

primes = []
primes.append(2)
i = 1
while len(primes) <= 10001:
    i = i + 2
    if isPrime(i):
        primes.append(i)

print(primes[10001])