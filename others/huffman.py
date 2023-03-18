# Mateusz Mazur
# Algorytm używa kolejki priorytetowej (oparta na min-heapie, więc przyjmuję złożoność n*logn). Algorytm pobiera dwie najmniejsze wartości z kolejki i zastępuje je jednym elementem, będących sumą tych elementów oraz zapisuje w tym elemencie indeksy elementów będących jego dziećmi. Złożoność w pesymistycznym przypadku sięga O(n^2) (n (pętla while) *n ( w najgorszym przypadku ilość dopisywania do znaków do dzieci)). Wypisywanie odbywa się w czasie liniowym O(n). Złożoność pamięciowa pozostaje O(n), ponieważ sukcesywanie jedne elementy są zastępowane przez inne (zmniejszająca się ilość obiektów w kolejce jest proporcjonalna do zwiększającej się w tych obiektach listy indeksów dzieci)

from queue import PriorityQueue


S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]


def huffman(S, F):

    inf = float('inf')
    n = len(F)
    # Tablica na kody znaków
    T = [""]*n
    que = PriorityQueue()
    # Utworzenie kolejki priorytetowej (przyjmujemy n*logn)
    for i in range(n):
        que.put((F[i],  [i], S[i]))
    # Właściwy algorytm niefizycznego budowania drzewa oraz aktualizacji kodów
    while que:
        a = que.get()
        if que.empty():
            break
        b = que.get()
        for i in a[1]:
            T[i] = "1"+T[i]
        for i in b[1]:
            T[i] = "0"+T[i]
        que.put((a[0]+b[0], a[1]+b[1], inf))
    suma = 0
    # Obliczanie ilości znaków do zapisania całego wyrażenia oraz tak jak w poleceniu, wypisywanie kodów.
    for i in range(n):
        suma += len(T[i])*F[i]
        print(S[i], ": ", T[i])
    print("dlugosc napisu: ", suma)


huffman(S, F)
