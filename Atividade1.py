
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        atual = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
            self.size += 1
        else:
            while atual.next != self.head:
                atual = atual.next
            atual.next = new_node
            self.size += 1
        self.head = new_node

 

    def remove_node(self, node):
        if self.head == node:
            atual = self.head
            while atual.next != self.head:
                atual = atual.next
            atual.next = self.head.next
            self.head = self.head.next
            self.size -= 1
        else:
            atual = self.head
            prev = None
            while atual.next != self.head:
                prev = atual
                atual = atual.next
                if atual == node:
                    prev.next = atual.next
                    atual = atual.next
                    self.size -= 1


    def josephus(self, step):
        atual = self.head

        while self.size> 1:
            count = 0
            p = atual
            while count != step:
                atual = atual.next
                count += 1
            if p == atual:
                self.remove_node(atual.next)
            
            else:
                self.remove_node(atual)
            atual = atual.next
        if self.size == 1:
            print("Usando n={}, m={}, resultado={}".format(n, step, atual.data))
            sobrevivente = atual.data
            return sobrevivente

x = int(input())

ll = CircularLinkedList()
for c in range(x):
    n = int(input())
    m = int(input())
    for i in range(n, 0, -1):
        ll.append(i)
    ll.josephus(m)
    ll.head=None
