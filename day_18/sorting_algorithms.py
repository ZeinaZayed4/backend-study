def bubble_sort(a: list[int]):
    n = len(a)
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        if not flag:
            break
    return a


def selection_sort(a: list[int]):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(a: list[int]):
    n = len(a)
    for i in range(1, n):
        cur = a[i]
        j = i - 1

        while j >= 0 and a[j] > cur:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a


a = [8, 7, 9, 3, 2, 1, 5, 4, 6]
print(f"Original: \n\t{a}")
print(f"Bubble Sort: \n\t{bubble_sort(a.copy())}")
print(f"Selection Sort: \n\t{selection_sort(a.copy())}")
print(f"Insertion Sort: \n\t{insertion_sort(a.copy())}")
