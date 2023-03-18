# Mazur Mateusz
from random import randint, shuffle, seed


def linearselect(A, k):
    # Lekko zmodyfikowana funkcja partition z quicksorta, w której następuje wywołanie naszej funkcji magicznych piątek do znajdowania pivota (wartośći). Jako, że w założeniu liczby się nie powtarzają, to nasz pivot jest unikalny, więc znajduję go w tablicy i reszta dzieje sięjuż tak jak w "tradycyjnej" funkcji
    def partition(A, l, r):
        x = magicMediana(A, l, r)
        for i in range(l, r+1):
            if A[i] == x:
                A[r], A[i] = A[i], A[r]
        i = l-1
        for j in range(l, r):
            if A[j] < x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    # Do sortowania małych wycinków tablicy (maks. 5 elemntów) używam Insertion sorta, który spisuję się przy tym świetnie
    def insertionSort(A, left, rigth):
        i = left
        while i <= rigth:
            j = i
            while j > left and A[j-1] > A[j]:
                A[j], A[j-1] = A[j-1], A[j]
                j -= 1
            i += 1

    # Ta funkcja obsługuje szukanie naszego pivota, działa ona bez użycia dodatkowych tablicych, dzięki czemu zmniejsza się jej zapotrzebowanie na pamięć (i tak już jest rekurencyjna, więc to może mieć znaczenie)
    def magicMediana(A, left, right):
        ind = left
        for i in range(left, right+1, 5):
            if i+4 > right:
                insertionSort(A, i, right)
                x = ((right)-i)//2+i
                A[x], A[ind] = A[ind], A[x]
            else:
                insertionSort(A, i, i+4)
                A[i+2], A[ind] = A[ind], A[i+2]
            ind += 1
        if (ind-left) > 5:
            return magicMediana(A, left, ind-1)
        else:
            insertionSort(A, left, ind-1)
            return A[left+(ind-left)//2]

    # Główna funkcja rekurencyjna, obsługująca wyszukiwanie odpowiedniego przedziału do przeszukiwania oraz zwracająca finalny wynik
    def magicFives(A, l, r, k):
        if l == r:
            return A[l]
        q = partition(A, l, r)
        if k == q:
            return A[q]
        elif k > q:
            return magicFives(A, q+1, r, k)
        else:
            return magicFives(A, l, q-1, k)

    return magicFives(A, 0, len(A)-1, k)


seed(42)

n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
