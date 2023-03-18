# Mateusz Mazur
from random import randint, seed


def mergesort(T):
    # funkcja rekurencyjna, dzieląca tablice na podtablice
    def intMergesort(T, l, r):
        if r > l:
            mid = (l+(r-1))//2
            intMergesort(T, l, mid)
            intMergesort(T, mid+1, r)
            merge(T, l, mid, r)

    # funkcja scalająco-sorutjąca
    def merge(T, l, mid, r):
        # wyznaczenie dwóch podtablic (są już posortowane)
        if l != mid:
            L = T[l:mid+1]
            R = T[mid+1:r+1]
        else:
            L = [T[l]]
            R = T[(mid+1):r+1]
        # scalanie podtablic w  posortowanym porządku do tablicy docelowej
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[l+k] = L[i]
                i += 1
            else:
                T[l+k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            T[l+k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[l+k] = R[j]
            j += 1
            k += 1
    intMergesort(T, 0, len(T)-1)
    return T


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
print("przed sortowaniem: T =", T)

T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
    if T[i] > T[i+1]:
        print("Błąd sortowania!")
        exit()

print("OK")
