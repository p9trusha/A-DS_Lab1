def buble_sort(arr):
    i = 0
    is_sort = False
    n = len(arr)
    while i < n - 1 and not is_sort:
        is_sort = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sort = False
        i += 1
    return arr
