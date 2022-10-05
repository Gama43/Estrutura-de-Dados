
class Queue:
    def __init__(self, max_size):
        self.__items = [None]*(max_size + 1)
        self.__first = 0
        self.__last = 0

    def is_empty(self):
        return self.__first == self.__last

    def is_full(self):
        return (self.__last + 1) % len(self.__items) == self.__first

    def push(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.__items[self.__last] = item
        self.__last = (self.__last + 1) % len(self.__items)

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.__items[self.__first]
        self.__first = (self.__first + 1) % len(self.__items)
        return item

movimentos = [
                (1,2),
                (1,-2),
                (2,1),
                (2,-1),
                (-1, -2),
                (-1,2),
                (-2,-1),
                (-2,1)
                ]


A = [
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1]
]

def get_distances(A, x):
    n = len(A)
    dist = [-1]*n
    q = Queue(n)
    dist[x] = 0
    q.push(x)
    while(not q.is_empty()):
        y = q.pop()
        for i in range(n):
              if d[0] > 0 and d[0] < 7 and d[1] > 0 and d[1] < 7 and A[d[0]][d[1]] == -1:
                dist[i] = A[d] + 1 #tabelar
                q.push(d) #tem que ser o d
    return dist




linha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7  }
origem = 'a1'
destino = 'b2'
linha_origem = linha[origem[0]]
col_origem = int(origem[1])-1
linha_destino = linha[origem[0]]
col_destino = int(destino[1])-1

inicio = (linha_origem, col_origem)
fim = (linha_destino, col_destino)



for m in movimentos:
    d = inicio[0]+ m[0], inicio[1]+ m[1]
    dist = get_distances(A, d)
print(dist)
