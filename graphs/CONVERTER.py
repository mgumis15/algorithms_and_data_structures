
inf = float('inf')


def listArrToMatrix(G):
    nG = len(G)
    n = -inf

    for i in range(nG):
        if G[i][0] > n:
            n = G[i][0]
        if G[i][1] > n:
            n = G[i][1]
    n += 1
    T = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(nG):
        T[G[i][0]][G[i][1]] = G[i][2]
        T[G[i][1]][G[i][0]] = G[i][2]
    for i in range(n):
        print(T[i], ",")


def MatrixToWeightSingleArray(G):
    n = len(G)
    T = [[]for i in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                T[i].append((j, G[i][j]))
    for i in range(n):
        print(T[i], ",")


def WeightSingleArrayToMatrix(G):
    n = len(G)
    T = [[0 for i in range(n)]for i in range(n)]

    for i in range(n):
        for el in G[i]:
            T[i][el[0]] = el[1]
    for i in range(n):
        print(T[i], ",")
# listArrToMatrix EG
# G = [[0, 1, 2],
#      [0, 2, 4],
#      [1, 0, 2],
#      [1, 2, 10],
#      [1, 4, 12],
#      [1, 5, 100],
#      [2, 0, 4],
#      [2, 1, 10],
#      [2, 3, 3],
#      [3, 2, 3],
#      [3, 4, 2],
#      [4, 3, 2],
#      [4, 1, 12],
#      [4, 5, 1],
#      [5, 1, 100],
#      [5, 4, 1]]


# listArrToMatrix(G)

# G = [[0, 4, 0, 0, 0, 0, 0, 0, 8],
#      [4, 0, 8, 0, 0, 0, 0, 0, 11],
#      [0, 8, 0, 3, 0, 5, 0, 4, 0],
#      [0, 0, 3, 0, 2, 14, 0, 0, 0],
#      [0, 0, 0, 2, 0, 1, 0, 0, 0],
#      [0, 0, 5, 14, 1, 0, 3, 0, 0],
#      [0, 0, 0, 0, 0, 3, 0, 6, 1],
#      [0, 0, 4, 0, 0, 0, 6, 0, 7],
#      [8, 11, 0, 0, 0, 0, 1, 7, 0]]
# G = [[(1, 4), (2, 3)], [(3, 2)],  [(3, 5)],  []]
G = [[0, 6, 0, 5, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 4, 4],
     [0, 0, 0, 0, 4, 5, 0],
     [0, 0, 4, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 3],
     [0, 0, 0, 0, 0, 0, 0]
     ]
MatrixToWeightSingleArray(G)
