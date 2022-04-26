from collections import deque


def escapeFromLabyrinth(matrix):
    queue = deque([(0, 0)])
    x_dir = [-1, +1, 0, 0]
    y_dir = [0, 0, -1, +1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newX = x + x_dir[i]
            newY = y + y_dir[i]

            if newX < 0 or newX >= len(matrix) or newY < 0 or newY >= len(matrix[0]):
                continue
            if matrix[newX][newY] == 0:
                continue
            if matrix[newX][newY] == 1:
                matrix[newX][newY] = matrix[x][y] + 1
                queue.append((newX, newY))
    return matrix[-1][-1]


matrix = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

print(escapeFromLabyrinth(matrix))
