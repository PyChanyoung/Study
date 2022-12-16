def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    lst = [array[0], max(array[0], array[1])]

    for i in range(2, len(array)):
        lst[0], lst[1] = lst[1], max(lst[1], lst[0] + array[i])
    return lst[1]


array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))
