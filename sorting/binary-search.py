# DONE
def binarySearch(T, k):
    l = 0
    r = len(T) - 1
    while l <= r:
        p = (l + r) // 2
        if T[p] == k:
            return p
        elif T[p] < k:
            l = p + 1
        else:
            r = p - 1
    return -1
