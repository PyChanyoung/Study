def nodeDepths(root):
    sumOfDepths = 0
    stack = [{'node': root, 'depth': 0}]
    while stack:
        newNode = stack.pop()
        node, depth = newNode["node"], newNode["depth"]
        if node is None:
            continue
        sumOfDepths += newNode['depth']
        stack.append({'node': node.right, 'depth': depth+1})
        stack.append({'node': node.left, 'depth': depth+1})
    return sumOfDepths


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(nodeDepths(root))
