

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        self.inserir_final(node)
    
    def inserir_final(self, nova_node):
        if self.head is None:
            self.head = nova_node
    
    def printar(self):
        pass


l = CircularLinkedList()
n = int(input())
m = int(input())


for i in range(1, n + 1):
    l.append(i)
