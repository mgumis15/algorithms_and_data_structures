from random import randint, seed


def heapify(T, n, i):
    print(T)
    l = 2*i+1
    r = 2*i+2
    m = i
    if l < n and T[l] > T[m]:
        m = l
    if r < n and T[r] > T[m]:
        m = r
    if m != i:
        T[i], T[m] = T[m], T[i]
        heapify(T, n, m)


def buildheap(T):
    n = len(T)
    for i in range((n-2)//2, -1, -1):
        print(T[i], i)
        heapify(T, n, i)


def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)


def addItem(T, item):
    buildheap(T)
    print(T)
    T.append(item)
    n = len(T)-1
    def par(x): return (x-1)//2
    while T[par(n)] < T[n] and par(n) >= 0:
        T[par(n)], T[n] = T[n], T[par(n)]

        d = input("")
        n = par(n)


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]


print("przed sortowaniem: ", T)

buildheap(T)

print("po sortowaniu    : ", T)
