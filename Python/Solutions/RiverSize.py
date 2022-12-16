def riverSize(array):
    visited = [[False for col in range(len(array[0]))]
               for row in range(len(array))]
    answer = []

    for row in range(len(array)):
        for col in range(len(array[0])):
            if visited[row][col]:
                continue
            riverSizeHelper(array, visited, row, col, answer)
    return len(answer)


def riverSizeHelper(array, visited, row, col, answer):
    possible = [(row, col)]
    size = 0
    while possible:
        row, col = possible.pop()
        if visited[row][col]:
            continue
        visited[row][col] = True
        if array[row][col] != 0:
            continue
        getNeighbors(array, row, col, possible)
        size += 1
    if size > 0:
        answer.append(size)


def getNeighbors(array, row, col, possible):
    if row > 0:
        possible.append((row-1, col))
    if row < len(array)-1:
        possible.append((row+1, col))
    if col > 0:
        possible.append((row, col-1))
    if col < len(array[0])-1:
        possible.append((row, col+1))


array = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]

print(riverSize(array))
