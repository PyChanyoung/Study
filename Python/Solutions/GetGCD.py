def getGDC(A, B):
    if A % B == 0:
        return B
    return getGDC(B, A % B)


print(getGDC(24, 64))
