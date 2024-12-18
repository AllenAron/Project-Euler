# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def catNum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum < n:
        return -1
    if sum == n:
        return 0
    if sum > n:
        return 1

for i in range(15):
    print(catNum(i))