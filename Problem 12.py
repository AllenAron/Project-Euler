## What is the value of the first triangle number to have over five hundred divisors?

import math

def findTriangularNumber(m):
    sum = 0
    for i in range(1, m + 1):
        sum = sum + i
    return sum

def findDivisors(n):
    a = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n/i)
    return a

i = 1
n = 0
while(True):
    n = n + i
    if len(findDivisors(n)) >= 500:
        print(n)
        break
    i = i + 1
