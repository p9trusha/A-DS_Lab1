def merge(a, b):
    arr = []
    i_a, i_b = 0, 0
    len_a, len_b = len(a), len(b)
    while i_a < len_a and i_b < len_b:
        if a[i_a] <= b[i_b]:
            arr.append(a[i_a])
            i_a += 1
        else:
            arr.append(b[i_b])
            i_b += 1
    arr += a[i_a:] + b[i_b:]
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    return merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:]))
