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
            print("Sobrevivente:" , atual.data)
            atual = atual.next
            if atual == self.head:
                break

    def __len__(self):
        atual = self.head
        count = 0
        while atual:
            count += 1
            atual = atual.next
            if atual == self.head:
                break
        return count

    def remove_node(self, node):
        if self.head == node:
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
                if atual == node:
                    prev.next = atual.next
                    atual = atual.next


    def josephus(self, step):
        atual = self.head

        while len(self) > 1:
            count = 0
            p = atual
            while count != step -1:
                atual = atual.next
                count += 1
            if p == atual:
                print("Remove:", atual.next.data)
                self.remove_node(atual.next)
            
            else:
                print("Remove:", atual.data)
                self.remove_node(atual)
            atual = atual.next
    

n = 10
m = 3

l = CircularLinkedList()
for i in range(n, 0, -1):
    l.append(i) 

l.josephus(m)
l.print_list()