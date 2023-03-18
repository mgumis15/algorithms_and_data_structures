# Mateusz Mazur
# Przekształciłem podstawowy algorytm w taki sposób, żeby szukał on najdłuższego podciągu malejącego, idąc od końca tablicy (pozwala to na łatwiejsze wypisanie w poprawnej kolejności). Tablicę "rodziców" przekształcicłem na tablicę dwuwymiarową, abym mógł przechowywać indeksy wszystkich elementów spełniających warunki. Po tej operacji dla każdego elementu, który rozpoczyna jeden z największych ciągów wywołuję funkcję rekurencyjną, w której (poprzez zapisywanie w tablicy) zbieram każdy możliwy ciąg razem i wypisuję. Ilość wypisń pełengo ciągu daje nam całkowitą ilość takich ciągów. Algorytm ma złożoność O(n^2) tak jak oryginał.
from random import seed, randint


def LIS(A):
    # funkcja wypisująca
    def printLIS(A, P, i, k, ile, tab=[]):
        if P[i]:
            for j in range(len(P[i])-1, -1, -1):
                printLIS(A, P, P[i][j], k, ile, tab+[A[i]])
        else:
            if(len(tab)+1 == k):
                for j in range(len(tab)):
                    print(tab[j], end=" ")
                print(A[i])
                ile[0] += 1

    n = len(A)
    F = [1]*n
    P = [[]for _ in range(n)]
    # szukanie najdłuższych ciągów
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if A[j] > A[i] and F[i] <= F[j]+1:
                F[i] = F[j]+1
                P[i].append(j)
    k = max(F)
    ile = [0]
    # szukanie pierwszych elementów ciągów
    for i in range(n):
        if F[i] == k:
            printLIS(A, P, i, k, ile)
    print(ile[0])


seed(42)


A = [2, 1, 4, 3]
LIS(A)
