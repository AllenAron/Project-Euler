## What is the sum of the digits of the number 2**1000?

a = 2**(1000)
s = str(a)
sum = 0

for i in range(len(s)):
    sum = sum + int(s[i])

print(sum)