# done
from random import randint, seed


def quicksort(T, l, r):
    while l < r:
        q = partition(T, l, r)

        if (q-l) <= (r-q):
            quicksort(T, l, q-1)
            l = q+1
        else:
            quicksort(T, q+1, r)
            r = q-1


def partition(T, l, r):
    q = randint(l, r)
    T[r], T[q] = T[q], T[r]
    x = T[r]
    i = l-1
    for j in range(l, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


seed(37)

n = 10
T = [randint(1, 10) for i in range(10)]


print("przed sortowaniem: ", T)

quicksort(T, 0, 9)
print("po sortowaniu    : ", T)
