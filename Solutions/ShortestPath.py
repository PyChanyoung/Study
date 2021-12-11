from collections import deque


def shortestPath(paths, cities, minimumDistance, startingCity):
    pathDic = [[] for _ in range(cities+1)]
    shortestPath = [-1] * (cities + 1)
    shortestPath[startingCity] = 0
    # print(pathDic)
    # print(shortestPath)

    for path in paths:
        pathDic[path[0]].append(path[1])
    # print(pathDic)

    queue = deque([startingCity])
    while queue:
        current = queue.popleft()
        # print(current)
        for next in pathDic[current]:
            # print(next)
            if shortestPath[next] == -1:
                shortestPath[next] = shortestPath[current]+1
                queue.append(next)
    answer = []
    for city, distance in enumerate(shortestPath):
        if distance == minimumDistance:
            answer.append(city)
    return answer if answer else [-1]


paths = [[1, 2], [1, 3], [2, 3], [2, 4]]
cities = 4
minimumDistance = 2
startingCity = 1

print(shortestPath(paths, cities, minimumDistance, startingCity))
