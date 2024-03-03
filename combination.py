# C = n! / k! * (n-k)!


def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n = 2
k = 5

print(combination(n, k))