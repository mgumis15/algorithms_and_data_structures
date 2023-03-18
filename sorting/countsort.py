# Done
from random import randint


def countsort(T, k):
    C = [0]*k
    B = [0]*len(T)
    for i in range(len(T)):
        C[T[i]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        C[T[i]] -= 1
        B[C[T[i]]] = T[i]
    for i in range(len(T)):
        T[i] = B[i]


n = 15
k = 5
T = [randint(0, k-1) for _ in range(n)]
print(T)
countsort(T, k)
print(T)


# Dla zamiany z litery na cyfrę (np. do indeksu) używamy f. ord(char) - 97; np.ord("a")-97=0
