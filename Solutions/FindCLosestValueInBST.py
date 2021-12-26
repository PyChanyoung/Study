def findClosestValueInBst(tree, target):
    current = tree
    closest = tree.value
    while current is not None:
        if abs(target-closest) > abs(target-current.value):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:  # when target == current.value
            return current.value
        return closest

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Test
if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.left.left.left = BST(1)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.right.left.right = BST(14)
    k = 12
    print(findClosestValueInBst(root, k))
