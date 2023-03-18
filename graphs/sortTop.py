from collections import deque


class V:
    def __init__(self, neigh, name):
        self.d = None
        self.parent = None
        self.neigh = neigh
        self.name = name
        self.start = None
        self.end = None


time = 0
G = [[1, 2], [], [3, 5], [4], [1, 5], [6], [7], []]


def DFS(G):
    res = []

    def DSFVisit(G, u, res):
        global time
        time += 1
        G[u].strat = time
        G[u].d = True
        for v in G[u].neigh:
            if not G[v].d:
                G[v].parent = G[u]
                DSFVisit(G, v, res)
        res.append(G[u].name)
        time += 1
        G[u].end = time
    D = ["a", "b", "c", "d", "e", "f", "g", "h"]
    Q = deque()
    for i in range(len(G)):
        G[i] = V(G[i], i)
    for u in range(len(G)):
        if not G[u].d:
            DSFVisit(G, u, res)
    res.reverse()
    print(res)


DFS(G)
