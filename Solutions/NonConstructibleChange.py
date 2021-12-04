def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0

    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
    return currentChange + 1


coins = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))
