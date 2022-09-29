class Empty(Exception):
    pass

class LinkedQueue:

    class _Node:
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0                     

    def __len__(self):
        print(self._size)
        return self._size


    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element             

    def enqueue(self, e):
        newest = self._Node(e, None)           
        if self.is_empty():
            self._head = newest               
        else:
            self._tail._next = newest
        self._tail = newest                    
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                    
            self._tail = None                     
        return answer
    

def cavalo(começo, fim):
    pass