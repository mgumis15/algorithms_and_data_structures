inf = float('inf')


class Node:
    def __init__(self, name):
        self.name = name
        self.d = inf
        self.parent = None


def BellmanFord(G, n):
    T = [Node(i) for i in range(n)]
    T[0].d = 0

    for i in range(n-1):

        for edge in G:
            if T[edge[0]].d+edge[2] < T[edge[1]].d:
                T[edge[1]].d = T[edge[0]].d+edge[2]
                T[edge[1]].parent = edge[0]
    for edge in G:
        if T[edge[0]].d+edge[2] < T[edge[1]].d:
            print("Ujemny cykl")
            return None

    for i in range(1, n):
        # print(T[i].name, T[i].d, T[i].parent)
        print("The distance of vertex", i,
              "from the source is", T[i].d, end='.')
        print(" Its path is [ 0 ", end='')
        printPath(T, i)
        print("]")


def printPath(T, v):
    if T[v].parent:
        printPath(T, T[v].parent)
    print(v, end=" ")


G = [
    (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
    (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
]
BellmanFord(G, 5)
