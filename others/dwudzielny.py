from collections import deque


# Te nie są
# G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [4, 2, 6], [5, 7], [6]]

# G = [[2, 3, 5, 6], [2, 4, 6], [0, 1, 7, 9], [0, 4, 9], [1, 3, 5, 7, 8], [
#     0, 4, 10], [0, 1, 8, 10], [2, 4, 10], [4, 6, 9], [2, 3, 8, 10], [5, 6, 7, 9]]


# Te są
# G = [[1, 3], [0, 2, 4], [1, 3], [0, 2, 4], [1, 3]]

#
G = [[3, 4], [3, 4], [3], [0, 1, 2], [0, 1]]


class V:
    def __init__(self, neigh, name):
        self.d = None
        self.parent = None
        self.neigh = neigh
        self.name = name
        self.start = None
        self.end = None


time = 0


#! <BFS>

def BSF(G, s):
    Q = deque()
    for i in range(len(G)):
        G[i] = V(G[i], i)
    G[s].d = 1
    Q.append(s)
    while Q:
        u = Q.popleft()
        for i in G[u].neigh:
            if G[i].d == G[u].d:
                return False
            if G[i].d == None:
                G[i].d = (G[u].d+1) % 2
                Q.append(i)
    return True


print(BSF(G, 0))
