def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    oneIdx, twoIdx = 0, 0
    smallestPair = [arrayOne[0], arrayTwo[0]]
    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        first, second = arrayOne[oneIdx], arrayTwo[twoIdx]
        if abs(first - second) < abs(smallestPair[1]-smallestPair[0]):
            smallestPair[0], smallestPair[1] = first, second
        if first == second:
            return
        elif first > second:
            twoIdx += 1
        else:
            oneIdx += 1
    return smallestPair


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo))
