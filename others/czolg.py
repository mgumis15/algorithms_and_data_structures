# Problem a) obliczyć minimalną liczbę tankowań, aby dotrzeć do punktu t
# Czołg jedzie na najdalżą możliwą stację, na którą pozwala mu pojemność baku


def minT(A, l, t):
    A.append((t, 0))
    n = len(A)
    if t < l:
        return 0
    if l < A[0][0]:
        return "Brak możliwości dojazdu"
    T = []
    currP = 0
    for i in range(n):

        if currP+l >= t:
            return T
        if i+1 >= n:
            return "Brak możliwości dojazdu :("
        if currP+l < A[i+1][0]:
            print(currP, A[i][0])
            T.append(i)
            currP = A[i][0]


# Problem b1)
def minPriceT(A, l, t):
    inf = float('inf')
    A.append((t, -1))
    n = len(A)
    currP = 0
    currInd = -1
    fuel = l
    price = 0
    T = []
    minv = (0, inf)
    for i in range(currInd+1, n):
        if A[i][0] > currP+l:
            break
        if minv[1] > A[i][1]:
            minv = (i, A[i][1])

    currInd = minv[0]
    currP = A[minv[0]][0]
    fuel = l-currP
    while currP+fuel < t:
        minv = (inf, inf)
        for i in range(currInd+1, n):
            if A[i][0] > currP+l:
                break
            if A[currInd][1] > A[i][1]:
                dif = A[i][0]-(currP+fuel)

                if dif >= 0:
                    fuel = 0
                    price += A[currInd][1]*dif
                else:
                    fuel = dif*(-1)
                T.append((currInd, i))
                currP = A[i][0]
                currInd = i
                minv = (inf, inf)
                break
            else:
                if A[i][1] < minv[1]:
                    minv = (i, A[i][1])
        if minv[1] != inf:
            dif = l-fuel
            price += A[currInd][1]*dif
            fuel = l-(A[minv[0]][0]-currP)
            T.append((currInd, minv[0]))
            currP = A[minv[0]][0]
            currInd = minv[0]
    return price


# Problem b2)
# Rozwiązanie zachłanne czerpiące inspirację z podpunktu a, czyli szukamy stacji z najniższą ceną, do której jesteśmy w stanie dotrzeć. Skoro i tak tankujemy do pełna to wybieramy najtańszą stację, która jest w zasięgu. Złożoność w najgorszym przypadku O(!n)


def fullT(A, l, t):
    inf = float('inf')

    n = len(A)
    if t < l:
        return 0
    if l < A[0][0]:
        return "Brak możliwości dojazdu"
    T = []
    currP = 0
    currInd = -1
    price = 0
    while currP+l < t:
        minv = (0, inf)
        for i in range(currInd+1, n):
            if A[i][0] > currP+l:
                break
            if minv[1] > A[i][1]:
                minv = (i, A[i][1])

        T.append(minv[0])
        currInd = minv[0]
        price += (A[currInd][0]-currP)*A[currInd][1]
        currP = A[currInd][0]
    print(T)
    return price


# A = [(15, 3), (30, 5), (42, 4), (59, 7), (77, 5)]
# A = [(15, 4), (25, 5), (40, 4), (60, 3), (75, 2)]
# A = [(1, 1), (9, 10), (15, 10), (16, 5), (17, 1), (27, 30)]
A = [(1, 0.8), (2, 1), (3, 0.8)]
# S = [8, 11, 15, 16]
# P = [40, 7, 15, 12]
# A = []
# for i in range(len(S)):
#     A.append((S[i], P[i]))
print(fullT(A, 2, 4))
