

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, atual_node):
        if value < atual_node.value:
            if atual_node.left is None:
                atual_node.left = Node(value)
            else:
                self._insert(value, atual_node.left)
        
        elif value > atual_node.value:
            if atual_node.rigth is None:
                atual_node.rigth = Node(value)
            else:
                self._insert(value, atual_node.rigth)
            
        else:
            print("Valor duplicado")
    
    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    def _find(self, value, atual_node):
        if value > atual_node.value and atual_node.rigth:
            return self._find(value, atual_node.rigth)
        elif value < atual_node.value and atual_node.left:
            return self._find(value, atual_node.left)
        if value == atual_node.value:
            return True

bst = BinaryTree()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(11))
