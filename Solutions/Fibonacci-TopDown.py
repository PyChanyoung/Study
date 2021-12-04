def fibo(n, memoize):
    if n not in memoize:
        memoize[n] = fibo(n-1, memoize) + fibo(n-2, memoize)
    return memoize[n]


print(fibo(99, {1: 1, 2: 1}))
