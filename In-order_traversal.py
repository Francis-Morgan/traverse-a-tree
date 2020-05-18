

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
        
    def in_order(self, root):
        tree = []
        if root:
            tree += self.in_order(root.left)
            tree.append(root.val)
            tree += self.in_order(root.right)
        return tree
            
    
root = Node('F')
root.left = Node('B')
root.right = Node('G')
root.left.left = Node('A')
root.right.right = Node('I')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.right.right.left = Node('H')
root.left.right.right = Node('E')

print(root.in_order(root))

