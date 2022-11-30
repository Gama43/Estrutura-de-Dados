class Graph:

        def __init__(self, vertices):
            self.vertices = vertices
            self.adj_list = {}

            for vertice in self.vertices:
                self.adj_list[vertice] = []
            
        def add_edge(self, vertice, edge):
            self.adj_list[vertice].append(edge)
            self.adj_list[edge].append(vertice)

        def print_adj(self):
            for vertice in self.vertices:
                print(vertice, ':', self.adj_list[vertice])


def bfs(grafo, start, goal):
        visited = []
        fila = [[start]]
        while fila:
            path = fila.pop(0)
            ele = path[-1]

            if ele not in visited:
                vizinhos = grafo[ele]
            
                for vizinho in vizinhos:
                    new_path = list(path)
                    new_path.append(vizinho)
                    fila.append(new_path)
                
                    if vizinho == goal:
                        print(len(new_path))
                        return
                visited.append(ele)


v = int(input())
a,b = input().split(',')
a = int(a)
b = int(b)
v_lista = []

for i in range(1, v+1):
    v_lista.append(i)

g = Graph(v_lista)

while a != -1:
    g.add_edge(a, b)
    a,b = input().split(',')
    a = int(a)
    b = int(b)
    


bfs(g.adj_list, 1, v ) 
