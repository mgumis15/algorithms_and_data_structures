# DONE
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        ifSwapped = False
        for j in range(0, n - i - 1):
            if(arr[j] > arr[j+1]):
                swap(arr, j, j+1)
                ifSwapped = True

        if (ifSwapped == False):
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
