inf = float('inf')
G = [
    [inf, 5, inf, inf, 11, 2, inf, inf, inf],
    [5, inf, 6, 4, inf, inf, inf, inf, inf],
    [inf, 6, inf, inf, inf, inf, inf, inf, inf],
    [inf, 4, inf, inf, inf, inf, inf, inf, inf],
    [11, inf, inf, inf, inf, inf, 7, 1, 2],
    [2, inf, inf, inf, inf, inf, 3, inf, inf],
    [inf, inf, inf, inf, 7, 3, inf, inf, inf],
    [inf, inf, inf, inf, 1, inf, inf, inf, inf],
    [inf, inf, inf, inf, 2, inf, inf, inf, inf],

]


def minp(G, x, y):
    n = len(G)

    def DFSVisit(G, n, last, u, y):
        global inf
        if u != y:
            curr = False
            for i in range(n):
                if G[u][i] < G[last][u]:
                    curr = DFSVisit(G, n, u, i, y)
                    if curr:
                        print(u)
                        return True
                    G[u][i] = inf
            return False
        else:
            print(u)
            return True
    print(DFSVisit(G, n, x, x, y))


minp(G, 0, 6)
