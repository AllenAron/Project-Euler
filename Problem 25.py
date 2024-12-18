## What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibomacci():
    f0 = 1
    f1 = 1
    i = 2
    while len(str(f1)) < 1000:
        temp = f1
        f1 = f1 + f0
        f0 = temp
        i = i + 1
    return i

print(fibomacci())