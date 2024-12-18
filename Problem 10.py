## Find the sum of all the primes below two million

import math

def isPrime(n):
    isprime = True
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            isprime = False
            break
    return isprime

i = 1
sum = 2
while i <= 2e6:
    i = i + 2
    if isPrime(i):
        sum = sum + i
print(sum)