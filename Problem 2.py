## By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

f0 = 1
f1 = 1
sum = 0
while(f1 < 4e6):
    temp = f1
    f1 = f1+f0
    f0 = temp
    if f1 % 2 == 0:
        sum = sum + f1
print(sum)
