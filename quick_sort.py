import sys
sys.setrecursionlimit(1000000)


def divide(arr, elem):
    left_arr = []
    right_arr = []
    for i in range(1, len(arr)):
        if arr[i] < elem:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
    i = len(left_arr)
    arr = left_arr + [elem] + right_arr
    return arr, i


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        arr, i = divide(arr, arr[0])
        return quick_sort(arr[:i]) + [arr[i]] + quick_sort(arr[i+1:])
