## Which starting number, under one million, produces the longest Collatz sequence?

s = []

def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return collatz(n/2) + 1
    else:
        return collatz(3*n + 1) + 1
    
for i in range(1, int(1e6)+1):
    s.append(collatz(i))
    
print(s.index(max(s)) + 1)