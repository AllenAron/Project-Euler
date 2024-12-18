## Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open('largesum.txt', 'r')

numbers = [int(line) for line in f.readlines()]
sum = 0
for line in numbers:
    sum += line
print(sum)