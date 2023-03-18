from queue import PriorityQueue
from LZRFindUnion import Node, find, union


def kruskal(G, n):
    T = [Node(i) for i in range(n)]
    G.sort(key=lambda x: x[2])
    out = []
    for el in G:
        x = find(T[el[0]])
        y = find(T[el[1]])
        if x.val != y.val:
            union(x, y)
            out.append(el)
    print(out)


G = [(0, 1, 1), (0, 5, 12), (1, 2, 5), (1, 5, 7),
     (2, 3, 3000), (2, 4, 4), (2, 5, 6), (3, 4, 9), (4, 5, 8)]

kruskal(G, 6)
