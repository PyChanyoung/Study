def fibo(n):
    lastTwo = [1, 1]
    count = 2
    while count < n:
        lastTwo[0], lastTwo[1] = lastTwo[1], lastTwo[0] + lastTwo[1]
        count += 1
    return lastTwo[1] if n >= 2 else lastTwo[0]


print(fibo(99))
