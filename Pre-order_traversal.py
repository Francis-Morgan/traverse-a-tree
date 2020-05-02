class Node:

    def __init__(self, val = 0,left = None, right = None):

        self.left = left
        self.right = right
        self.val = val


    def PreorderTraversal(self, root):
        arr = []
        if root is not None:
            arr.append(root.data)
            arr += self.PreorderTraversal(root.left)
            arr += self.PreorderTraversal(root.right)
        return arr

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)

print(root.PreorderTraversal(root))

