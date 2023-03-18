# Algorytm do znajdowania mostów za pomocą alg. Tarjana (DFS)
# ! JESZCZE NIE ZAIMPLEMENTOWANE  W OGÓLE
time = 0


def mostyTarjana(G):
    n = len(G)
    inf = float('inf')

    def DSFVisit(G, ODP, D, low, visited, parent,  u):
        global time
        time += 1
        n = len(G)
        visited[u] = True
        D[u] = time
        low[u] = time
        for i in range(n):
            if G[u][i] and not visited[i]:
                parent[i] = u
                DSFVisit(G, ODP, D, low, visited, parent, i)
                if low[i] < low[u]:
                    low[u] = low[i]

            elif G[u][i] and visited[i] and parent[u] != i:
                if low[u] > D[i]:
                    low[u] = low[i]

        if low[u] == D[u] and parent[u] != None:
            ODP.append((parent[u], u))

    low = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    D = [inf for _ in range(n)]
    ODP = []
    for u in range(n):
        if not visited[u]:
            DSFVisit(G, ODP, D, low, visited, parent, u)
    return ODP


G = [
    [False, True, True, False, False, False],
    [True, False, True, False, True, False],
    [True, True, False, False, False, False],
    [False, False, False, False, True, True],
    [False, True, False, True, False, True],
    [False, False, False, True, True, False],
]
G = [
    [False, True, True, True, False, False, False, False, False,
        False, False, False, False, False, False, False, False],
    [True, False, True, False, False, False, False, False, False,
        False, False, False, False, False, True, False, False],
    [True, True, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False,
        False, False, True, True, False, False, False, False],
    [False, False, False, False, False, False, True, False, False,
        True, False, False, False, False, False, False, False],
    [False, False, False, False, False, True, False, True, True,
        False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, False, False,
        False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, False, False,
        False, False, False, False, False, False, False, False],
    [False, False, False, False, False, True, False, False, False,
        False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, True, False],
    [False, False, False, False, True, False, False, False, False,
        False, False, False, False, False, False, True, False],
    [False, False, False, False, True, False, False, False, False,
        False, False, False, False, False, False, True, False],
    [False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, True, False, True],
    [False, True, False, False, False, False, False, False, False,
        False, False, False, False, True, False, False, True],
    [False, False, False, False, False, False, False, False, False,
        False, True, True, True, False, False, False, False],
    [False, False, False, False, False, False, False, False, False,
        False, False, False, False, True, True, False, False]
]

print(mostyTarjana(G))
