
class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.disc = -1
        self.low = -1
        self.visited = False


time = 0


def SSS(G):
    n = len(G)
    T = [Node(i) for i in range(n)]
    ODP = []
    for i in range(n):
        if T[i].disc == -1:
            sssDFS(G, n, T, i, ODP)


def sssDFS(G, n, T, ind, ODP):
    global time
    v = T[ind]
    v.disc = time
    v.low = time
    v.visited = True
    time += 1
    ODP.append(ind)

    for i in range(n):
        if G[ind][i] != 0:
            if T[i].disc == -1:
                sssDFS(G, n, T, i, ODP)
                v.low = min(v.low, T[i].low)
            elif T[i].visited:
                v.low = min(v.low, T[i].disc)
    w = -1
    if v.low == v.disc:
        while w != ind:
            w = ODP.pop()
            print(w)
            T[w].visited = False
        print()


G = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
]

SSS(G)
