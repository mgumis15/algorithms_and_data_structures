# Mateusz Mazur
# Algorytm wyszukiwania ścieżki opieram o algorytm Dijkstry, tylko zamiast szukać i zapisywać najkrótszą ścieżkę, zapisuję minimalny przepływ w danej ścieżce, a algorytm relaksujący bierze maximum ze sprawdzanych minimalnych przepływości. Złożonośc będzie taka jak Dijkstry + liniowe sporządzenie tablicy z wierzchołkami: O(ElogV+V). Złożoność pamięciowa będzie V*E z wejściowej tablicy. Kolejka priorytetowa da mi wierzchołki posortowane po największych dotychczasowych przepływościach, ponieważ sortuje ona po liczbach przeciwnych "-".
from copy import deepcopy
from queue import PriorityQueue


def max_extending_path(G, s, t):
    inf = float('inf')

    # Klasa dla każdego wierzchołka
    class Node:
        def __init__(self, name):
            self.name = name
            self.parent = None
            self.min = -inf
            self.visited = False

    # Zmodyfikowany alg. Dijkstry
    def Dijkstra(G, OUT, f, l):
        n = len(G)
        T = [Node(i) for i in range(n)]
        T[f].min = inf
        Q = PriorityQueue()
        Q.put((-T[f].min, T[f].min, T[f].name))

        while not Q.empty():
            v = Q.get()
            T[v[2]].visited = True
            for e in G[v[2]]:
                if not T[e[0]].visited:
                    if relax(T[e[0]], T[v[2]],  e[1]):
                        Q.put((-T[e[0]].min, T[e[0]].min, e[0]))

        OUT.append(f)
        getPath(T, OUT, f, l)

    # F. relaksacyjna
    def relax(u, v, w):
        if u.min < v.min and u.min < w:
            if w < v.min:
                u.min = w
            else:
                u.min = v.min
            u.parent = v.name
            return True
        return False

    # F. zwracająca znalezioną ścieżkę
    def getPath(T, OUT, f, cur):
        if cur != f:
            getPath(T, OUT, f, T[cur].parent)
            OUT.append(T[cur].name)

    OUT = []
    Dijkstra(G, OUT, s, t)
    return OUT


# sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
# funkcja zwraca prawidłowy wynik


G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3

s = 0
t = 3
C = 3


GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)


if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)


capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
