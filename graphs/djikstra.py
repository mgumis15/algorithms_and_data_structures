from queue import PriorityQueue
inf = float('inf')


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.d = inf


def Dijkstra(G, f, l):
    n = len(G)
    T = [Node(i) for i in range(n)]
    T[f].d = 0
    Q = PriorityQueue()
    Q.put((T[f].d, T[f].name))
    while not Q.empty():
        v = Q.get()
        for i in range(n):
            if G[v[1]][i] > 0 and i != T[v[1]].parent:
                if relax(T[v[1]], T[i], G[v[1]][i]):
                    Q.put((G[v[1]][i]+v[0], i))
    print(f, end=" ")
    getPath(T, f, l)


def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d+w
        v.parent = u.name
        return True
    return False


def getPath(T, f, cur):
    if cur != f:
        getPath(T, f, T[cur].parent)
        print(T[cur].name, end=" ")


G = [
    [0, 1, 5, 0, 0],
    [1, 0, 2, 8, 7],
    [5, 2, 0, 3, 0],
    [0, 8, 3, 0, 1],
    [0, 7, 0, 1, 0]
]

Dijkstra(G, 0, 4)
