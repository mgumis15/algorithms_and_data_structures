# O(n*maxW)
# F(i,w)=największy zysk jaki można osiągnąć wybierając spośród przedmiotów od 0 do i nie przekraczając wagi w
# F(0,w)=0 dla W[0]>w; P[0] dla w[0]<=w
# f(i,0)=0
# f(i,w)=max(f(i-1,w),f(i-1,w-W[i])+P[i]) (zakładamy, że w>>W[i])
def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0]*(MaxW+1) for _ in range(n)]
    for w in range(W[0], MaxW+1):
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, MaxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]]+P[i])
        for e in F:
            print(e)
        print()
    return F[n-1][MaxW]


def getSolution(F, W, P, i, w):
    if i < 0:
        return []
    if i == 0:
        if w >= W[0]:
            return [0]
        return []
    if w >= W[i] and F[i][w] == F[i-1][w-W[i]]+P[i]:
        return getSolution(F, W, P, i-1, w-W[i])+[i]
    return getSolution(F, W, P, i-1, w)


W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
MaxW = 24
print(knapsack(W, P, MaxW))
