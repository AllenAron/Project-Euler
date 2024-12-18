def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def com(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0
for i in range(101):
    for j in range(i):
        if com(i,j) > 1_000_000:
            count += 1

print(count)