from pickle import TRUE


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


def get_distances(A, x):
    '''Compute distances between x and every city
    in the distance matrix A'''
    n = len(A)
    dist = [-1]*n
    q = Queue(n)
    dist[x] = 0
    q.push(x)
    while(not q.is_empty()):
        y = q.pop()
        for i in range(n):
            if A[y][i] == 1 and dist[i] == -1:
                dist[i] = dist[y] + 1 #tabule
                q.push(i) #D
    return dist

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

linha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7  }

start_node = 0
dist = get_distances(A, start_node)
print(dist)

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
origem = input()
destino = input()
origem = (3,3)
#linha_origem = linha[origem[0]]
#col_origem = int(origem[1])-1

for m in movimentos:
    d = origem[0]+ m[0], origem[1]+ m[1]
    print(d)

    if d[0] > 0 and d[0] < 7 and d[1] > 0 and d[1] < 7 and A[d[0]][d[1]] == -1:

        


