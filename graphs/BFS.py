from collections import deque


# class V:
#     def __init__(self, neigh, name):
#         self.d = None
#         self.parent = None
#         self.neigh = neigh
#         self.name = name
#         self.start = None
#         self.end = None


# def BFS(G, s):
#     Q = deque()
#     for i in range(len(G)):
#         G[i] = V(G[i], i)
#     G[s].d = 0
#     Q.append(s)
#     while Q:
#         u = Q.popleft()
#         for i in G[u].neigh:
#             if G[i].d == None:

#                 G[i].d = G[u].d+1
#                 G[i].parent = u
#                 Q.append(i)

#     for i in range(len(G)):
#         print("id: ", G[i].name, "fala: ", G[i].d, " parent ", G[i].parent)


# def sPath(G, f, s):
#     BFS(G, f)
#     i = s
#     print()
#     while i != f:
#         print("id: ", G[i].name, "fala: ", G[i].d, " parent ", G[i].parent)
#         i = G[i].parent
#     print("id: ", G[i].name, "fala: ", G[i].d, " parent ", G[i].parent)


def BFS(G, s):
    n = len(G)
    inf = float('inf')
    visited = [None for _ in range(n)]
    Q = deque()
    Q.append(s)
    visited[0] = inf
    while Q:
        v = Q.popleft()
        for i in range(n):
            if G[v][i] and visited[i] == None:
                Q.append(i)
                visited[i][0] = v
    print(visited)
