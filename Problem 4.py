## Find the largest palindrome made from the product of two 3-digit numbers

def isPalindrome(n):
    n = str(n)
    for i in range(int(len(n)/2)):
        if not n[i] == n[len(n)-i-1]:
            return False
    return True

def findPalindrome(s):
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if isPalindrome(i*j):
                s.append(i*j)

a = []
findPalindrome(a)
print(max(a))
