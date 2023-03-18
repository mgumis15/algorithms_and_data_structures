from collections import deque
# O(VE^2), algoytm maksymalnego przepływu Edmonda Karpa (Użycie BFS'u do szukania ścieżek)


def max_flow(C, s, t):

    # policz maksymalny przepływ z s do t
    # c[i][j] to przepustowosc krawedzi z i do j
    # jesli c[i][j] > 0 to c[j][i] = 0
    inf = float('inf')
    n = len(C)
    F = [[0 for _ in range(n)]for _ in range(n)]

    def BFS(C, F, s, t):
        n = len(C)
        inf = float('inf')
        visited = [None for _ in range(n)]
        Q = deque()
        Q.append(s)
        visited[0] = inf
        var = False
        while Q:
            v = Q.popleft()
            for i in range(n):
                if C[v][i]-F[v][i] > 0 and visited[i] == None:
                    visited[i] = v
                    if i == t:
                        return visited

                    Q.append(i)
            if var:
                break
        return None
    maxFlow = 0
    path = BFS(C, F, s, t)
    while path != None:
        minf = inf
        i = t
        while i != s:
            minf = min(C[path[i]][i]-F[path[i]][i], minf)
            i = path[i]
        i = t
        while i != s:
            F[path[i]][i] += minf
            F[i][path[i]] -= minf
            i = path[i]
        maxFlow += minf
        path = BFS(C, F, s, t)

    return maxFlow


C = [[0 for j in range(4)] for i in range(4)]
C[0][1] = 2
C[0][2] = 1
C[1][2] = 1
C[1][3] = 1
C[2][3] = 2
# C = [[0, 10, 8, 0, 0, 0],
#      [0, 0, 5, 5, 0, 0],
#      [0, 4, 0, 0, 10, 0],
#      [0, 0, 9, 0, 10, 3],
#      [0, 0, 0, 6, 0, 14],
#      [0, 0, 0, 0, 0, 0]]
print(max_flow(C, 0, 3))  # wypisze 3
