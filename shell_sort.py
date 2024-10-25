from math import log2, floor, ceil


def shell_sort(arr, gaps):
    s = 0
    for gap in gaps:
        k = 0
        for i in range(gap, len(arr)):
            a = arr[i]
            j = i
            while j >= gap and a < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
                k += 1
            arr[j] = a
        s += k
    return arr


def shell_gaps(n):
    return [n // (2 ** i) for i in range(1, floor(log2(n) + 1))]


def hibbard_gaps(n):
    return [2 ** i - 1 for i in range(floor(log2(n)), 0, -1)]


def pratt_gaps(n):
    gaps = []
    max_power2 = ceil(log2(n))
    for i in range(max_power2 - 1, -1, -1):
        for j in range(i + 1):
            gap = (2 ** (i - j)) * (3 ** j)
            if gap >= n / 2:
                break
            gaps.append(gap)
    gaps.sort(reverse=True)
    return gaps


