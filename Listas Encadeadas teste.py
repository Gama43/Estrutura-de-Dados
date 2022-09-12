

class Pessoa:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head = Pessoa()

    def append(self, data):
        nova_pessoa = Pessoa(data)
        atual = self.head
        while atual.next != None:
            atual = atual.next
        atual.next = nova_pessoa
    
    def tamanho(self):
        atual = self.head
        total = 0
        while atual.next != None:
            total += 1
            atual = atual.next
        return total
    
    def display(self):
        elems = []
        atual_pessoa = self.head
        while atual_pessoa.next !=None:
            atual_pessoa = atual_pessoa.next
            elems.append(atual_pessoa.data)
        print (elems)

    def get(self, index):
        if index >= self.tamanho():
            return None
        atual_idx = 0
        atual_pessoa = self.head
        while True:
            atual_pessoa = atual_pessoa.next
            if atual_idx == index: return atual_pessoa.data
            atual_idx += 1

    def remove(self, index):
        if index >= self.tamanho():
            return 
        atual_idx = 0
        atual_pessoa = self.head
        while True:
            ultima_pessoa = atual_pessoa
            atual_pessoa = atual_pessoa.next
            if atual_idx == index:
                ultima_pessoa.next = atual_pessoa.next
                return
            atual_idx += 1
        
