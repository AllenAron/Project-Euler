## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sum = 0
sq = 0

for i in range(101):
    sum = sum + i**2
    sq = sq + i
print((sq**2)-sum)
