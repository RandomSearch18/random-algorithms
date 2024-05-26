from random import shuffle
from time import perf_counter, perf_counter_ns


def is_sorted(array: list) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def bogosort(array: list) -> list:
    while not is_sorted(array):
        shuffle(array)
    return array


def bogosort_demo(array: list):
    print(f"Sorting {len(array)} item(s)... ", end="")
    start_time = perf_counter_ns()
    sorted_array = bogosort(array)
    elapsed_time_ms = (perf_counter_ns() - start_time) / 1_000_000
    print(f"Done in {elapsed_time_ms:.3f} ms: {sorted_array}")


if __name__ == "__main__":
    bogosort_demo([3, 2, 1])
    bogosort_demo([3, 2, 1])
    bogosort_demo([3, 2, 1])
    bogosort_demo([3, 2, 1, 0])
    bogosort_demo([3, 2, 1, 9, 10])
    bogosort_demo([9, 3, 7, 5, 6, 4, 8])
    bogosort_demo([9, 3, 7, 5, 6, 4, 8, 99])
    bogosort_demo([9, 3, 7, 5, 6, 4, 8, 2, 1, 0])
    bogosort_demo([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    bogosort_demo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bogosort_demo([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    bogosort_demo([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    bogosort_demo([99, 53, 77, 205, 66, 44, 88, 22, 11, 0, -99, 999, 1000])
