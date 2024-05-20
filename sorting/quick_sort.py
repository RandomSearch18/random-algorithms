def quick_sort(array: list):
    if len(array) <= 1:
        print(f"Array {array} is already sorted")
        return array
    print(f"Sorting {array}")
    pivot = len(array) // 2
    left = 0
    right = len(array) - 1
    while left <= right and right != pivot and left != pivot:
        while array[left] < array[pivot] and array[left] != array[pivot]:
            left += 1
        while array[right] > array[pivot] and array[right] != array[pivot]:
            right -= 1
        print(f"Swapped <{left}>{array[left]} with <{right}>{array[right]}")
        array[left], array[right] = array[right], array[left]
    array[right], array[pivot] = array[pivot], array[right]

    return quick_sort(array[: pivot - 1]) + [array[pivot]] + quick_sort(array[pivot:])


print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
print(quick_sort([1, 0, 0, 1, 1, 0, 1]))
print(quick_sort([1, 2, 3, 4, 5]))
print(quick_sort([5, 4, 3, 2, 1]))
