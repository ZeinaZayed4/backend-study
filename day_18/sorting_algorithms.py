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


def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)


def merge(l, r):
    result = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])

    return result


def quick_sort(a, s, e):
    if (e - s + 1) <= 1:
        return a

    pivot = a[e]
    l = s
    for i in range(s, e):
        if a[i] < pivot:
            a[l], a[i] = a[i], a[l]
            l += 1

    a[e] = a[l]
    a[l] = pivot

    quick_sort(a, s, l - 1)
    quick_sort(a, l + 1, e)

    return a


a = [8, 7, 9, 3, 2, 1, 5, 4, 6]
print(f"Original: \n\t{a}")
print(f"Bubble Sort: \n\t{bubble_sort(a.copy())}")
print(f"Selection Sort: \n\t{selection_sort(a.copy())}")
print(f"Insertion Sort: \n\t{insertion_sort(a.copy())}")
print(f"Merge Sort: \n\t{merge_sort(a.copy())}")
print(f"Quick Sort: \n\t{quick_sort(a.copy(), 0, 8)}")
