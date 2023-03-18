
inf = float('inf')


def FloydWarshall(G):
    n = len(G)

    D = [[inf for i in range(n)]for j in range(n)]
    P = [[None for i in range(n)]for j in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = 0
            elif G[i][j]:
                D[i][j] = G[i][j]
                P[i][j] = i
    for i in range(n):
        for v in range(n):
            for u in range(n):
                if D[v][u] > D[v][i]+D[i][u]:
                    D[v][u] = D[v][i]+D[i][u]
                    P[v][u] = P[i][u]
