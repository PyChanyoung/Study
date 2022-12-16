def makeOne(n):
    memoize = {1: 0}
    for i in range(2, n+1):
        memoize[i] = memoize[i-1] + 1
        if i % 2 == 0:
            memoize[i] = min(memoize[i], memoize[i//2]+1)
        if i % 3 == 0:
            memoize[i] = min(memoize[i], memoize[i//3]+1)
        if i % 5 == 0:
            memoize[i] = min(memoize[i], memoize[i//5]+1)
    return memoize[n]


x = 26
print(makeOne(x))
