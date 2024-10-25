def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        a = arr[i]
        j = i
        while j > 0 and a < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = a
    return arr
