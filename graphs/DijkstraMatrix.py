
inf = float('inf')


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.visited = False
        self.d = inf


def Dijkstra(G, f, l):
    n = len(G)
    T = [Node(i) for i in range(n)]
    T[f].d = 0

    for u in range(n):
        minK = inf
        v = -1
        for i in range(n):
            if not T[i].visited and minK > T[i].d:
                minK = T[i].d
                v = i
        T[v].visited = True
        for i in range(n):
            if G[v][i] > 0 and not T[i].visited:
                relax(T[v], T[i], G[v][i])

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

Dijkstra(G, 0, 2)
