def getMostGroup(array):
    array.sort()
    count = 0
    group = 0
    for i in array:
        count += 1
        if count >= i:
            group += 1
            count = 0
    return group


array = [2, 3, 1, 2, 2]
print(getMostGroup(array))
