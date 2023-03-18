from math import inf


def frog(A):
    print(A)
    n = len(A)
    # Na końcu ma się minimalnie tyle energii ile zawiera ostatnie pole
    mini = f(n - 1, A[n - 1], A)
    # Maksymalna ilość energii na końcu
    suma = sum(A)-n
    print(suma)
    for i in range(1, suma):
        mini = min(mini, f(n - 1, i + A[n - 1], A))
    return mini

# Oblicza minimalną liczbę skoków żaby do punktu i mając e energii


def f(i, e, A):
    # Nie możemy mieć ujemnej energii
    if e < 0:
        return inf
    if i == 0:
        # Sprawdzenie czy znaleźliśmy jakieś rozwiązanie
        if e == A[0]:
            return 0
        return inf
    mini = f(0, e + i - A[i], A) + 1
    for j in range(1, i):
        mini = min(mini, f(j, e + (i - j) - A[i], A) + 1)
    return mini


A = [2, 1, 2, 1, 1, 8]
A = [2, 2, 1, 0, 0]
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(frog(A))
