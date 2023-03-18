# Problem komiwojażera

from math import sqrt
inf = float('inf')
x = 0


def komi(C):

    def tspf(i, j, F, P):
        print(i, j, "\n")
        if F[i][j] != inf:
            return F[i][j]
        if i == j-1:
            best = inf
            s = i
            for k in range(j-1):
                temp = tspf(k, j-1, F, P)+dist(C[k], C[j], "min")
                if(temp < best):
                    best = temp
                    s = k
            P.append(s)
            F[j-1][j] = best
        else:
            F[i][j] = tspf(i, j-1, F, P)+dist(C[j-1], C[j], "else")
        return F[i][j]

    global inf
    n = len(C)
    F = [[inf]*n for _ in range(n)]
    F[0][1] = dist(C[0], C[1], "")
    P = []
    O = []
    end = inf
    for i in range(n-1):
        suma = tspf(i, n-1, F, P)+dist(C[i], C[n-1], "end")
        P.append(i)
        if suma < end:
            end = suma
            O = P
        P = []
        for tab in F:
            print(tab)
    print(O)
    for i in O:
        print(C[i][0], end=" ")
    for i in range(len(C)-1, -1, -1):
        if i == 0 or i not in O:
            print(C[i][0],  end=" ")
    return end


def dist(t1, t2, title):
    global x
    x += 1
    print(sqrt((t2[1]-t1[1])**2+(t2[2]-t1[2])**2), title)
    return sqrt((t2[1]-t1[1])**2+(t2[2]-t1[2])**2)


# C = [["Wrocław", 0, 2], ["Warszawa", 5, 3], [
#     "Gdansk", 2, 4], ["Kraków", 4, 1], ["Szczeciń", 6, 1]]
# C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdansk", 2, 4], ["Kraków", 3, 1]]
C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], [
    'F', 8, 3], ['G', 7, 4], ['H', 2, 4], ['I', 0.5, 2.5], ['J', 1.5, 3.5]]

C.sort(key=lambda city: city[1])
print(komi(C))
# print(dist(C[0], C[2])+dist(C[2], C[4]) +
#       dist(C[4], C[3])+dist(C[3], C[1])+dist(C[1], C[0]))
