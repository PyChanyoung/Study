def factorial(N):
    current = 1
    while N > 0:
        current *= N
        N -= 1
    return current


print(factorial(5))
