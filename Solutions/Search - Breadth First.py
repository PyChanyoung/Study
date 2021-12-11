from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breathFirstSearch(self, array):
        queue = deque([self])
        while queue:
            current = queue.popleft()
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
