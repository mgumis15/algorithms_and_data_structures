from queue import PriorityQueue


inf = float('inf')


class Node:
    def __init__(self, name):
        self.name = name
        self.d = inf
        self.parent = None


def prim(G):
    n = len(G)
    T = [Node(i) for i in range(n)]
    T[0].d = 0
    Q = PriorityQueue()
    Q.put((T[0].d, 0))
    while not Q.empty():
        v = Q.get()
        for i in range(n):
            if G[v[1]][i] > 0 and G[v[1]][i] < T[i].d:
                T[i].parent = v[1]
                T[i].d = G[v[1]][i]
                Q.put((G[v[1]][i], i))
    for e in T:
        print(e.name, e.d, e.parent)


G = [
    [0, 4, 0, 0, 1, 1],
    [4, 0, 2, 0, 2, 0],
    [0, 2, 0, 8, 0, 0],
    [0, 0, 8, 0, 3, 6],
    [1, 2, 0, 3, 0, 2],
    [1, 0, 0, 6, 2, 0]


]

prim(G)
