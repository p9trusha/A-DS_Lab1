def selection_sort(arr):
    len_arr = len(arr)
    for i in range(0, len_arr - 1):
        i_min_el = i
        for j in range(i + 1, len_arr):
            if arr[i_min_el] > arr[j]:
                i_min_el = j
        if i != i_min_el:
            arr[i], arr[i_min_el] = arr[i_min_el], arr[i]
    return arr
