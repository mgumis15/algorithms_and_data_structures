# Done
def insertionSort(A, k):
    for n in range(len(A)-1, 0, -1):
        if len(A[n-1]) <= k:
            i = n
            break

    if k == 0:
        n = 0
    i = n
    while i < len(A):
        j = i
        while j > n and A[j-1][k] > A[j][k]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1


def radixSort(A):
    i = 0
    while i < len(A):
        j = i
        while j > 0 and len(A[j-1]) > len(A[j]):
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1
    i = len(A[-1])-1
    while i >= 0:
        insertionSort(A, i)
        i -= 1


A = [
    "nie", "zmienia", "czy", "wstydzic", "czy", "go", "narody", "slyna", "z", "dom", "i", "w", "szlacheckim", "stanie", "trudno", "zaradzic", "wolal", "gosci", "wysoko"
]
T = [
    "nie", "zmienia", "czy", "wstydzic", "czy", "go", "narody", "slyna", "z", "dom", "i", "w", "szlacheckim", "stanie", "trudno", "zaradzic", "wolal", "gosci", "wysoko"
]

print(A, "\n")
radixSort(A)
print(A, "\n")
T.sort()
print(T)
if T == A:
    print("OK")
