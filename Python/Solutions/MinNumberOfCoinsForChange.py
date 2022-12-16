def minNumberOfCoinsForChange(n, denoms):
    numCoins = [float("inf") for amount in range(n + 1)]
    print(numCoins)
    numCoins[0] = 0

    for denom in denoms:
        for amount in range(denom, n + 1):
            numCoins[amount] = min(numCoins[amount], numCoins[amount - denom] + 1)
    return numCoins[n] if numCoins[n] != float("inf") else -1


n = 135
denoms = [39, 45, 130, 40, 4, 1]
print(minNumberOfCoinsForChange(n, denoms))
