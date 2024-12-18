# Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    sum = 0
    for i in range(int(n/2)):
        if n % (i + 1) == 0:
            sum += i + 1
    return sum

def amicable(x, y):
    return x == y


sum = 0
for i in range (10000):
    if amicable(i, d(i)):
        sum += i + d(i)
print(sum)