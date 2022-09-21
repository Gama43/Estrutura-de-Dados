class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        atual = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while atual.next != self.head:
                atual = atual.next
            atual.next = new_node
        self.head = new_node

    def print_list(self):
        atual = self.head
        while atual:
            print(atual.data)
            atual = atual.next
            if atual == self.head:
                break

    def remove(self, key):
        if self.head.data == key:
            atual = self.head
            while atual.next != self.head:
                atual = atual.next
            atual.next = self.head.next
            self.head = self.head.next
        else:
            atual = self.head
            prev = None
            while atual.next != self.head:
                prev = atual
                atual = atual.next
                if atual.data == key:
                    prev.next = atual.next
                    atual = atual.next

    def josephus(self):
        pass


n = 10
l = CircularLinkedList()
for i in range(n, 0, -1):
    l.append(i) 
l.print_list()
