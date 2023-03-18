from collections import deque

time = 0


class V:
    def __init__(self, neigh, name):
        self.d = None
        self.parent = None
        self.neigh = neigh
        self.name = name
        self.start = None
        self.end = None


def DFS(G):

    def DSFVisit(G, u):
        global time
        time += 1
        G[u].strat = time
        G[u].d = True
        for v in G[u].neigh:
            if not G[v].d:
                G[v].parent = G[u]
                DSFVisit(G, v)
        time += 1
        G[u].end = time
    Q = deque()
    for i in range(len(G)):
        G[i] = V(G[i], i)

    for u in range(len(G)):
        if not G[u].d:
            DSFVisit(G, u)
