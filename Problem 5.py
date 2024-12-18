## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

found = False
k = 0

while not found:
    k = k + 1
    for i in range(2, 25):
        if not k % i == 0:
            break
        elif i == 20:
            found = True
            break

print(k)