# Mateusz Mazur
# Algorytm oparłem o algorytm Dijkstry, przeszukując dla każdego wierzchołka najmniejszego cyklu, w jakim ten wierzchołek się znajduje, poprzez łączenie już przetworzonych ścieżek. Algorytm działa w O(V^3), V^2 - algorytm dikstry razy V-wywołania dla każdego wierzchołka
# Pamięciowo zawiera się w V^2
from copy import deepcopy
from queue import PriorityQueue


def min_cycle(G):
    inf = float('inf')

    # Klasa oznaczająca wierzchołek
    class Node:
        def __init__(self, name):
            self.name = name
            self.parent = None
            self.d = inf
            self.visited = False

    # algorytm Dijkstry, oparty na kolejce priorytetowej
    # G-graf,n-ilość wierzchołków,f-wierzch. początkowy, minC- długość już znalezionego, najkrótszego cyklu
    def Dijkstra(G, n, f, minC):
        T = [Node(i) for i in range(n)]
        T[f].d = 0
        Q = PriorityQueue()
        Q.put((T[f].d, T[f].name))
        ODP = []
        minV = (None, None)
        while not Q.empty():
            v = Q.get()
            if v[1] != f:
                T[v[1]].visited = True
            for i in range(n):
                if G[v[1]][i] > 0:
                    if T[i].visited != True:
                        if relax(T[v[1]], T[i], G[v[1]][i]):
                            Q.put((G[v[1]][i]+v[0], i))
                    elif i != T[v[1]].parent:
                        if minC > G[v[1]][i]+v[0]+T[i].d:
                            minC = G[v[1]][i]+v[0]+T[i].d
                            minV = (v[1], i)

        ODP = []
        # zwrot najmniejszego cyklu dla danego wejściowego wierzchołka
        if minV[0] and minV[1]:
            getPath(T, ODP, f, minV[0])
            getPath(T, ODP, f, minV[1])
            ODP.append(f)
        return (ODP, minC)

    # Funkcja relaksująca ścieżki
    def relax(u, v, w):
        if v.d > u.d + w:
            v.d = u.d+w
            v.parent = u.name
            return True
        return False

    # Funkcja zwracająca najkrótszą ścieżkę między wierzchołkami startowym i końcowym
    def getPath(T, ODP, f, cur):
        if cur != f:
            getPath(T, ODP, f, T[cur].parent)
            ODP.append(cur)

    minC = inf
    n = len(G)
    OUT = []
    # Wywołanie Dijkstry dla każdego wierzchołka
    for i in range(n):
        otp = Dijkstra(G, n, i, minC)
        if minC > otp[1]:
            OUT = otp[0]
            minC = otp[1]
    return OUT


# sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
# funkcja zwraca prawidłowy wynik


G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

LEN = 7


GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)


if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
