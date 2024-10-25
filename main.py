from random import randint, seed
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from buble_sort import buble_sort
from merge_sort import merge_sort
from shell_sort import shell_sort, shell_gaps, hibbard_gaps, pratt_gaps
from quick_sort import quick_sort
from heap_sort import heap_sort
import time


def main():
    a = input()
    a = a[1:-2].split(", ")
    for n in a:
        print(n)
    seed(0)
    max_len_arr = 1000000
    len_arrs = list(range(0, max_len_arr + 1, max_len_arr // 20))
    sorted_arrs = [[0 for _ in range(i)] for i in len_arrs]
    # reverse_sorted_arrs = [list(range(i, 0, -1)) for i in len_arrs]
    random_arrs = [[randint(0, length // 2) for _ in range(length)] for length in len_arrs]
    almost_sorted_arrs = [arr[:len(arr) // 10] + merge_sort(arr[len(arr) // 10:]) for arr in random_arrs]
    #arr_gaps = [shell_gaps(i) for i in len_arrs]
    times = []
    for i in range(21):
        start_time = time.time()
        arr = insertion_sort(sorted_arrs)
        finish_time = time.time()
        print(finish_time - start_time)
        times.append(finish_time - start_time)
    print(times)


if __name__ == '__main__':
    main()
