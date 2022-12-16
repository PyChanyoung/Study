def getIntegerTriangle(matrix):
    for rowIdx in range(1, len(matrix)):
        for idx in range(len(matrix[rowIdx])):
            current = -1
            if idx > 0:
                current = max(current, matrix[rowIdx-1][idx-1])
            if idx < len(matrix[rowIdx])-1:
                current = max(current, matrix[rowIdx-1][idx])
            matrix[rowIdx][idx] += current
    return max(matrix[-1])


matrix = [[7],
          [3, 8],
          [8, 1, 0],
          [2, 7, 4, 4],
          [4, 5, 2, 6, 5]]
print(getIntegerTriangle(matrix))
