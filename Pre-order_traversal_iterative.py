# Python program to perform iterative preorder traversal 

# Узел бинарного дерева 
class Node:
    def __init__(self,val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def PreorderTraversal(self,root):
        
        # Если корень дерева None
        if root is None:
            return []
        
        # Создадим стек, где временно будут хранится значения узлов дерева
        # В списке tree будем хранить значения дерева
        # Добавим в стек корень дерева
        stack = []
        tree = []
        stack.append(root)
        
        # С помощю метода pop() удаляем и присваеваем node значение узла
        # Добавляем его в хранилище tree
        # Если узел имеет правого потомка - добавляем его в стек
        # Если узел имеет левого потомка - добавляем его в стек
        # Обратите внимание, что сначало мы будем удалять из стека значения левых потомков
        # потом уже правых
        
        while len(stack) > 0:
            
            node = stack.pop()
            tree.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        
        return tree
    
root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)
print(root.PreorderTraversal(root))
        
        
        
