# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import math

def isPythTriplet(a, b, c):
    return a**2 + b**2 == c**2

for i in range(1000):
    for j in range(1000):
            k = math.sqrt(i**2 + j**2)
            if isPythTriplet(i, j, k) and i+j+k == 1000:
                print(i, j, k)
                print(i*j*k)