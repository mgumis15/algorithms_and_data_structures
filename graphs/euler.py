# Mateusz Mazur
# Złożoność (V^2)  V- liczba wierzchołków (samo kopiowanie tablicy to złożoność V^2)
# Złożoność pamięciowa 2*V^2+V+E (dwie macierze sąsiedztwa + tablica na wielkość stopni (pozwala nam w czasie liniowym sprawdzać warunki oraz w funkcji sprawdzającej ograniczyć niepotrzebne wywołania pętli) + wielkość stosu/tablica wyjściowa)
from collections import deque


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


def euler(G):

    n = len(G)
    # Zapisuje(tylko dla połowy macierzy, ponieważ jest ona symetryczna względem przekątnej) stopnie wierzchołków i sprawdzam warunek konieczny o ich parzystości.
    # Jednocześnie tworzę nową macierz sąsiedztwa, aby nie niszczyć macierzy wchodzącej
    V = [[False for j in range(n)]for i in range(n)]
    T = [0 for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            if G[i][j]:
                T[i] += 1
                T[j] += 1
                V[i][j] = True
                V[j][i] = True
    for i in T:
        if i % 2 != 0:
            return None
    Q = deque()
    ODP = []

    # Funkcja wyszukująca ścieżki Eulera
    def DSFVisit(V, T, ODP, Q, f,  u):
        # Używam wcześniej stworzonej tablicy stopni po to, aby nie musieć sprawdzać całego wiersza tablicy, jeżeli nie ma żadnej krawędzi. Jeżeli stopień jest niezerowy, sprawdzam w czasie O(n), która krawędź istnieje i tam się poruszamy
        if T[u] > 0:

            Q.append(u)
            for i in range(n):
                if V[u][i]:
                    V[u][i] = False
                    V[i][u] = False
                    T[i] -= 1
                    T[u] -= 1
                    # Jeżeli w następnym kroku wracamy do naszego wierzchołka początkoweo (dopełnia się jeden cykl) to ustawiamy indeks początku cyklu na ten wierzchołek
                    if i != f:
                        DSFVisit(V, T, ODP,  Q, f,  i)
                    else:
                        DSFVisit(V, T, ODP,  Q, i,  i)
                    break
        else:
            # Jeżeli krawędź zostaje przetworzona jest dodawana do wyjściowej tablicy
            ODP.append(u)
            # Jeżeli nasz stos nie jest pusty, zdejmujemy z niego kolejne elementy aż do trafienia na nieprzetworzny wierzchołek lub do wyczerpania stosu
            if Q:
                u = Q.pop()
                DSFVisit(V, T, ODP,  Q, u,  u)

    DSFVisit(V, T, ODP, Q, 0, 0)
    # Sprawdzenie, czy graf jest spójny (sprawdzam czy wszytkie stopnie się wyzerowały). Można też użyć na początku algorytmu DFS i jeżeli liczba odwiedzonych krawędzi byłaby mniejsza po pierwszym pełnym przejściu od ilości wierzchołków oznacza, że graf nie jes spójny.
    for i in T:
        if i != 0:
            return None
    # Zwracam listę
    return ODP


print(euler(G))
